#!/usr/bin/env python3
"""Compare includes/xeps.md with what a live XMPP server announces.

Logs in with any account (on any server), asks the target server for its
service discovery data and its components', reads the client stream
features a modern app sees, and checks DNS and host-meta. Then it lists
table rows that are not confirmed and announced XEPs missing from the
table.

Some features are only shown to the server's own logged-in users (push,
PEP, roster versioning...). They are listed as "check in an app" instead
of failing.

Usage:
  python3 -I tools/check-xeps.py TARGET JID PASSWORD_FILE
  e.g. python3 -I tools/check-xeps.py chatrix.one someone@example.org ~/pw

Needs python3-slixmpp and dig (dnsutils/bind9-dnsutils).
"""
import asyncio
import pathlib
import re
import socket
import ssl
import subprocess
import sys
import urllib.request

import slixmpp
from slixmpp.exceptions import IqError, IqTimeout

TABLE = pathlib.Path(__file__).resolve().parent.parent / "includes" / "xeps.md"

# Service discovery features and the XEP each one shows.
FEATURES = {
    "jabber:iq:last": "0012",
    "http://jabber.org/protocol/disco#info": "0030",
    "http://jabber.org/protocol/muc": "0045",
    "http://jabber.org/protocol/commands": "0050",
    "vcard-temp": "0054",
    "http://jabber.org/protocol/pubsub": "0060",
    "http://jabber.org/protocol/bytestreams": "0065",
    "jabber:iq:register": "0077",
    "http://jabber.org/protocol/offline": "0160",
    "urn:xmpp:blocking": "0191",
    "urn:xmpp:ping": "0199",
    "urn:xmpp:extdisco:2": "0215",
    "urn:xmpp:carbons:2": "0280",
    "urn:xmpp:mam:2": "0313",
    "http://jabber.org/protocol/muc#stable_id": "0359",
    "urn:xmpp:http:upload:0": "0363",
    "urn:xmpp:reporting:1": "0377",
    "urn:xmpp:occupant-id:0": "0421",
    "urn:xmpp:message-retract:1": "0424",
    "urn:xmpp:serverinfo:0": "0485",
}
# Shown only to the server's own users, or work in the apps.
IN_APP = {"0115", "0153", "0163", "0237", "0352", "0357", "0384",
          "0398", "0401", "0402", "0411"}


class Probe(slixmpp.ClientXMPP):
    def __init__(self, jid, password, target):
        super().__init__(jid, password)
        self.target = target
        self.seen = {}  # XEP -> where it was seen
        self.register_plugin("xep_0030")
        self.add_event_handler("session_start", self.run)

    async def features_of(self, jid):
        try:
            r = await self["xep_0030"].get_info(jid=jid, timeout=20)
        except (IqError, IqTimeout):
            return [], []
        q = r["disco_info"]
        forms = [f.get("var") for f in q.xml.iter("{jabber:x:data}field")]
        return list(q["features"]), forms

    async def run(self, _):
        feats, forms = await self.features_of(self.target)
        jids = [self.target]
        try:
            items = await self["xep_0030"].get_items(jid=self.target, timeout=20)
            jids += [i[0] for i in items["disco_items"]["items"]]
        except (IqError, IqTimeout):
            pass
        for j in jids:
            f, fm = (feats, forms) if j == self.target else await self.features_of(j)
            for name in f:
                if name in FEATURES:
                    self.seen.setdefault(FEATURES[name], j)
            if j == self.target and "abuse-addresses" in fm:
                self.seen.setdefault("0157", j)
            if j == self.target and fm:
                self.seen.setdefault("0128", j)
        self.disconnect()


def stream_features(host, port=5222, ns="jabber:client"):
    """Stream features after STARTTLS. Clients name themselves (from=), as
    modern apps do: ejabberd offers SASL2 only then."""
    frm = f"from='probe@{host}' " if ns == "jabber:client" else ""
    op = (f"<?xml version='1.0'?><stream:stream {frm}to='{host}' "
          f"xmlns='{ns}' xmlns:stream='http://etherx.jabber.org/streams' version='1.0'>")

    def read(s, end):
        b = b""
        while end not in b:
            c = s.recv(65536)
            if not c:
                break
            b += c
        return b.decode(errors="replace")

    with socket.create_connection((host, port), timeout=15) as s:
        s.send(op.encode())
        read(s, b"</stream:features>")
        s.send(b"<starttls xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")
        read(s, b"proceed")
        with ssl.create_default_context().wrap_socket(s, server_hostname=host) as t:
            t.send(op.encode())
            return read(t, b"</stream:features>")


def other_checks(host):
    seen = {}
    f = stream_features(host)
    for ns, xep in (("urn:xmpp:sasl:2", "0388"), ("urn:xmpp:bind:0", "0386"),
                    ("urn:xmpp:sm:3", "0198"), ("urn:xmpp:fast:0", "0484"),
                    ("urn:xmpp:sasl-cb:0", "0440")):
        if ns in f:
            seen[xep] = "stream features"
    s2s = stream_features(host, 5269, "jabber:server")
    if "urn:xmpp:features:dialback" in s2s:
        seen["0220"] = "s2s stream"
    if "urn:xmpp:bidi" in s2s:
        seen["0288"] = "s2s stream"
    srv = subprocess.run(["dig", "+short", "SRV", f"_xmpps-client._tcp.{host}"],
                         capture_output=True, text=True).stdout.strip()
    if srv:
        seen["0368"] = "DNS"
    try:
        hm = urllib.request.urlopen(f"https://{host}/.well-known/host-meta", timeout=15).read().decode()
        if "urn:xmpp:alt-connections" in hm:
            seen["0156"] = "host-meta"
        if "alt-connections:xbosh" in hm:
            seen["0206"] = "host-meta"
    except OSError:
        pass
    return seen


def table_rows():
    rows = {}
    for line in TABLE.read_text().splitlines():
        m = re.search(r"XEP-(\d{4})\]\([^)]*\): ([^|]+?)\s*\|\s*(\S+)", line)
        if m:
            rows[m.group(1)] = (m.group(2), "check" in m.group(3))
    return rows


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    target, jid, pwfile = sys.argv[1:]
    x = Probe(jid, pathlib.Path(pwfile).expanduser().read_text().strip(), target)
    x.connect()
    asyncio.get_event_loop().run_until_complete(x.disconnected)
    seen = {**x.seen, **other_checks(target)}
    rows = table_rows()
    problems = 0
    print(f"{target}: {len(seen)} XEPs seen, {len(rows)} rows in {TABLE.name}\n")
    for xep, (name, ok) in sorted(rows.items()):
        if ok and xep in seen:
            state = f"ok ({seen[xep]})"
        elif ok and xep in IN_APP:
            state = "check in an app"
        elif ok:
            state = "NOT SEEN"
            problems += 1
        elif xep in seen:
            state = f"MARKED OFF, BUT SEEN ({seen[xep]})"
            problems += 1
        else:
            state = "off, as marked"
        print(f"  XEP-{xep} {name[:52]:<52} {state}")
    extra = sorted(set(seen) - set(rows) - {"0128"})
    for xep in extra:
        print(f"  XEP-{xep} seen ({seen[xep]}) but not in the table")
    print(f"\n{problems} row(s) to look at" + (f", {len(extra)} XEP(s) to add" if extra else ""))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
