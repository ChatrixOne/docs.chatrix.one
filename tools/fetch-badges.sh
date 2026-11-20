#!/usr/bin/env sh
# Refreshes the XMPP Providers and XMPP Network Graph badges in
# docs/assets/badges/. The Status page serves them from this site, so the
# visitor's browser never contacts those services. If a download fails or
# is not a plain SVG, the committed copy stays and the build goes on.

DIR="docs/assets/badges"

fetch() {
  url="$1"
  dest="$DIR/$2"
  tmp="$(mktemp)"
  if curl -fsSL --max-time 20 -o "$tmp" "$url" \
    && [ "$(wc -c < "$tmp")" -le 51200 ] \
    && head -c 200 "$tmp" | grep -q '<svg' \
    && ! grep -qiE '<script|javascript:|<foreignObject|[[:space:]]on[a-z]+=' "$tmp"; then
    mv "$tmp" "$dest"
    chmod 644 "$dest"
    echo "updated $dest"
  else
    rm -f "$tmp"
    echo "kept the committed $dest (download failed or not a plain SVG)"
  fi
}

fetch "https://data.xmpp.net/providers/v2/badges/chatrix.one.svg" xmpp-providers.svg
fetch "https://xmppnetwork.goodbytes.im/badge/chatrix.one.svg" xmpp-network.svg
