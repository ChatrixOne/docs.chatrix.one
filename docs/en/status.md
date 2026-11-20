# Service Status

<div class="cx-status" markdown>
<div markdown>

:material-pulse: Live status
{ .cx-status__eyebrow }

Uptime, ping and incidents of every **Chatrix.One** service, shown live on **status.chatrix.one**.

:material-calendar-check: Planned maintenance: none at the moment.
{ .cx-status__note }

</div>

[View status :octicons-arrow-right-24:](https://status.chatrix.one){ .md-button .md-button--primary }

</div>

## Services right now { #availability }

<div class="cx-services" markdown>

| Service | Status | Ping | 24 hours | 7 days | 30 days |
|:--------|:------:|:----:|:--------:|:------:|:-------:|
| **XMPP** server | ![Status](https://status.chatrix.one/api/badge/121/status?label=&upLabel=Up&downLabel=Down&maintenanceLabel=Maintenance) | ![Ping](https://status.chatrix.one/api/badge/137/ping?label=) | ![Uptime 24 hours](https://status.chatrix.one/api/badge/121/uptime/24?label=) | ![Uptime 7 days](https://status.chatrix.one/api/badge/121/uptime/168?label=) | ![Uptime 30 days](https://status.chatrix.one/api/badge/121/uptime/720?label=) |
| Connections to other servers (federation) | ![Status](https://status.chatrix.one/api/badge/123/status?label=&upLabel=Up&downLabel=Down&maintenanceLabel=Maintenance) | ![Ping](https://status.chatrix.one/api/badge/123/ping?label=) | ![Uptime 24 hours](https://status.chatrix.one/api/badge/123/uptime/24?label=) | ![Uptime 7 days](https://status.chatrix.one/api/badge/123/uptime/168?label=) | ![Uptime 30 days](https://status.chatrix.one/api/badge/123/uptime/720?label=) |
| [Website](https://chatrix.one) | ![Status](https://status.chatrix.one/api/badge/227/status?label=&upLabel=Up&downLabel=Down&maintenanceLabel=Maintenance) | ![Ping](https://status.chatrix.one/api/badge/227/ping?label=) | ![Uptime 24 hours](https://status.chatrix.one/api/badge/227/uptime/24?label=) | ![Uptime 7 days](https://status.chatrix.one/api/badge/227/uptime/168?label=) | ![Uptime 30 days](https://status.chatrix.one/api/badge/227/uptime/720?label=) |
| [Web chat](https://chatrix.one/webchat) | ![Status](https://status.chatrix.one/api/badge/226/status?label=&upLabel=Up&downLabel=Down&maintenanceLabel=Maintenance) | ![Ping](https://status.chatrix.one/api/badge/226/ping?label=) | ![Uptime 24 hours](https://status.chatrix.one/api/badge/226/uptime/24?label=) | ![Uptime 7 days](https://status.chatrix.one/api/badge/226/uptime/168?label=) | ![Uptime 30 days](https://status.chatrix.one/api/badge/226/uptime/720?label=) |
| [Documentation](/en/) | ![Status](https://status.chatrix.one/api/badge/135/status?label=&upLabel=Up&downLabel=Down&maintenanceLabel=Maintenance) | ![Ping](https://status.chatrix.one/api/badge/135/ping?label=) | ![Uptime 24 hours](https://status.chatrix.one/api/badge/135/uptime/24?label=) | ![Uptime 7 days](https://status.chatrix.one/api/badge/135/uptime/168?label=) | ![Uptime 30 days](https://status.chatrix.one/api/badge/135/uptime/720?label=) |
| [Blog](https://blog.chatrix.one) | ![Status](https://status.chatrix.one/api/badge/124/status?label=&upLabel=Up&downLabel=Down&maintenanceLabel=Maintenance) | ![Ping](https://status.chatrix.one/api/badge/124/ping?label=) | ![Uptime 24 hours](https://status.chatrix.one/api/badge/124/uptime/24?label=) | ![Uptime 7 days](https://status.chatrix.one/api/badge/124/uptime/168?label=) | ![Uptime 30 days](https://status.chatrix.one/api/badge/124/uptime/720?label=) |

</div>

Ping is the average of the last 24 hours. Charts and the incident history are on [status.chatrix.one](https://status.chatrix.one).

## Account Registrations

| Type              |Rate Limit              |Status                           |
|:------------------|:----------------------:|-------------------------:|
| Invitation            |One per hour            |![Registration Status](https://status.chatrix.one/api/badge/125/status?label=&upLabel=OPEN&downLabel=CLOSED) |
| Installed Client  |Only with an invite, one per hour from an IP |![Registration Status](https://status.chatrix.one/api/badge/125/status?label=&upLabel=OPEN&downLabel=CLOSED) |

## Compliance and Compatibility - **XMPP**

| Test                    |Result                                                                     |
|:------------------------|--------------------------------------------------------------------------:|
| **XMPP Providers**      | [![XMPP Providers](../assets/badges/xmpp-providers.svg)](https://providers.xmpp.net/provider/chatrix.one/) |
|**XMPP Network Graph** | [![XMPP Network Graph](../assets/badges/xmpp-network.svg)](https://xmppnetwork.goodbytes.im/?focus=chatrix.one) |

## Security and Cryptography

| Test            | Result    |
|:----------------|:---------:|
| DNSSEC and DANE | [![DNSSEC and DANE: A](../assets/badges/dnssec-dane.svg)](https://www.huque.com/bin/danecheck?domain=chatrix.one&port=5223&starttls=None&namecheck=on) |
| CryptCheck | [![CryptCheck: A+](../assets/badges/cryptcheck.svg)](https://cryptcheck.fr/xmpp/chatrix.one) |

## Technical data

### XMPP Server

| Parameter        | Value                          |
|:-----------------|:------------------------------:|
| Processor        | ARM Ampere<sup>&reg;</sup>Altra<sup>&trade;</sup> |
| RAM              | 8GB                            |
| Disk Space       | 64GB (Encrypted)               |
| File System      | ext4                           |
| Operating System | Ubuntu 24.04 (Noble Numbat)    |
| Ejabberd version | 26.09                          |
| Backup           | Daily                          |
| Location         | Switzerland                    |
| Powered with     | 100% Renewable energy          |

#### Information about XEPs

| XEP                                                                                                                       |          Availability          |
|:--------------------------------------------------------------------------------------------------------------------------|:------------------------------:|
--8<-- "includes/xeps.md"

> Checked live on the server. Registration from an app is possible with an invite, after an hCaptcha challenge on the website. Bidirectional server-to-server connections are currently off, because some servers, among them the one behind XMPP Providers, cannot exchange data with Chatrix.One. Message reactions and OMEMO are features of the apps. The server stores and delivers them.

#### Account options { #account-options }

--8<-- "includes/plans-en.md"

> Labels marked *soon* are being prepared and are not active yet.

### Backup server

| Parameter        | Value                |
|:-----------------|:--------------------:|
| Processor        | AMD EPYC 3251        |
| RAM              | 64GB                 |
| Disk Space       | 5TB                  |
| File System      | ZFS (RAIDZ-1)        |
| Operating System | Debian 13 (Trixie)   |
| Location         | Bulgaria             |

## Information about occurred incidents

!!! abstract "Incidents"

     There are currently no documented incidents.

## Update history

### 19.11.2026

#### Chatrix.One for Android 2.21.3-cx1.2

- The whole app is now translated into Bulgarian (Settings, chats, calls, menus);
- The main Settings sections are now translated in 20 more languages.

### 03.11.2026

#### Chatrix.One for Android

- First release of our own Android app, based on [Conversations](https://codeberg.org/iNPUTmice/Conversations) and open source;
- Quick gestures, a long-press menu with reactions and the full emoji picker, Chatrix.One colours and icons, a welcome screen with a Chatrix.One sign-up link;
- Installed with [Obtainium](/en/clients/obtainium) from the GitHub releases, next to Conversations. More on the page [Chatrix.One for Android](/en/clients/chatrix-one).

### 24.10.2026

#### Server Moved to Ubuntu 24.04 LTS

- The server was reinstalled on **Ubuntu 24.04 LTS** with an automated, tested setup;
- All accounts, contacts, message history, group chats and files were carried over.

### 04.10.2026

#### Update Ejabberd to version [26.09](https://github.com/processone/ejabberd/releases/tag/26.09)

- Fixes for several security issues, including remote code execution and a DoS attack through **BOSH**;
- Fixed the order of some XML child elements;
- New option for a proof-of-work **CAPTCHA** challenge.

### 30.07.2026

#### Update Ejabberd to version [26.07](https://github.com/processone/ejabberd/releases/tag/26.07)

- Primarily security and reliability fixes addressing multiple vulnerabilities across authentication, OAuth, PubSub, WebAdmin, file uploads, and web modules;
- Better invite management through new user and admin interfaces;
- Support for ConverseJS 14.

### 25.07.2026

#### Server Downgrade

Due to the drastic increase in hosting costs (thanks to the AI rampocalypse), the available RAM has been reduced from 12GB to 8GB.

### 14.05.2026

#### Complete Redesign of the Documentation Website

The theme has been completely redesigned to visually align with the updated main website [Chatrix.One](https://chatrix.one).

### 10.05.2026

#### New Logo

![Chatrix.One Logo](../assets/logo-dark.svg#only-dark){ width="200" }
![Chatrix.One Logo](../assets/logo-light.svg#only-light){ width="200" }

### 20.04.2026

#### Update Ejabberd to version [26.04](https://github.com/processone/ejabberd/releases/tag/26.04)

- Security release - Limits max memory used by XML parser used to process XMPP payloads, to prevent potential DoS attack.

### 05.04.2026

#### Update Ejabberd to version [26.03](https://github.com/processone/ejabberd/releases/tag/26.03)

- Fix MySQL authentication for TLS connections that required auth plugin switch;
- Improve handling of scram 'wanted to use channel-bindings but was not offered one' flag;
- Add ability for `mod_options` values to depend on other options;
- Don't fail to classify stand-alone chat states;
- Fix some warnings compiling with Erlang/OTP 29;
- Document how to set empty lists in `ejabberdctl` and WebAdmin;
- Add handling of Etag and If-Modified-Since headers to files served by `ejabberd_http` and `mod_http_upload`;
- Ignore whitespaces at end of host header in `ejabberd_http`;
- Add ability to mark that column can be null in `e_sql_schema`;
- Add tests for SASL2;
- Make table cleanup in test more robust;

### 11.02.2026

#### Update Ejabberd to version [26.02](https://github.com/processone/ejabberd/releases/tag/26.02)

- Fixes issue with adding `hats` data in presences send by group chats;
- Removes `mod_muc_occupantid` modules, and integrates its functionality directly into `mod_muc`;
- Fixes issue with reset `occupant-id` values after restart of Ejabberd;
- Improves handling of mediated group chat invitations in `mod_block_stranger`;
- Properly install `mod_invites` templates in `make install` call;
- Better errors in `mod_invites`;
- Accessibility improvements in `mod_invites`;
- Improves handling of request with invalid URL encoded values in request handled by `ejabberd_http`;
- Improves handling of invalid responses to disco queries in `mod_pubsub_serverinfo`;
- Fixes conversion of MUC room configs from Ejabberd older than 21.12;
- Fixes to autologin in WebAdmin.

### 23.01.2026

#### Update Ejabberd to version [26.01](https://github.com/processone/ejabberd/releases/tag/26.01)

- Database Serialization;
- Roster Invites and Invite-based Account Registration.

### 02.01.2026

#### Introduced Self-Hosted Web Chat Client

- Integrated Converse.js version 12.0.0. A web-based chat client, accessible at [https://chatrix.one/webchat](https://chatrix.one/webchat).

### 30.10.2025

#### Update Ejabberd to version [25.10](https://github.com/processone/ejabberd/releases/tag/25.10)

- Added more Ad-Hoc Commands from XEP-0133;
- Updated support for XEP-0317 Hats.

### 25.09.2025

#### Changes in the generation of **TLS** certificates

- The issuer of **[TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)** certificates has been changed from **[ZeroSSL](https://zerossl.com/)** to **[Let's Encrypt](https://letsencrypt.org/)**;
- The algorithm for generating **TLS** certificates has been changed, with the previous **[RSA 2048](https://en.wikipedia.org/wiki/RSA_cryptosystem)** being replaced with **[ECC-384](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography)**.

### 29.08.2025

#### Update Ejabberd to version [25.08](https://github.com/processone/ejabberd/releases/tag/25.08)

- Improvements in Matrix gateway;
- Fixed ACME in Erlang/OTP 28.0.2;
- New `mod_providers` to serve XMPP Providers file;
- Improved Unicode support in configuration;
- New option `conversejs_plugins` to enable OMEMO;
- Easier erlang node name change with `mnesia_change`;
- Colorized interactive log;
- Document API tags in modules.

### 20.07.2025

#### Update Ejabberd to version [25.07](https://github.com/processone/ejabberd/releases/tag/25.07)

- Spam filter with block lists support;
- Support for XEP-0485: PubSub Server Information;
- Support for older Matrix rooms in ejabberd XMPP <-> Matrix Gateway;

### 17.04.2025

#### Update Ejabberd to version [25.04](https://github.com/processone/ejabberd/releases/tag/25.04)

- An important security fix and several bug fixes;
- Fix handling multiple occupant-id;
- New API command.

### 06.03.2025

#### Update Ejabberd to version [25.03](https://github.com/processone/ejabberd/releases/tag/25.03)

- Matrix Gateway Gets Room Support;
- Multiple Simultaneous Password Types;
- Execute API Commands Using XMPP Client.

### 26.12.2024

#### Update Ejabberd to version [24.12](https://github.com/processone/ejabberd/releases/tag/24.12)

- Improvements and bug fixes;
- [XEP-0484: Fast Authentication Streamlining Tokens](https://github.com/processone/ejabberd/releases/tag/24.12#484) - Reduces authentication time, providing faster startup for mobile clients;
- [Commands API v3](https://github.com/processone/ejabberd/releases#apiv3).

### 27.11.2024

#### New Logo Design

![Chatrix.One Logo](../assets/logo-bird-white.png#only-dark){ width="200" }
![Chatrix.One Logo](../assets/logo-bird-blue.png#only-light){ width="200" }

### 30.10.2024

#### Update Ejabberd to version [24.10](https://github.com/processone/ejabberd/releases/tag/24.10)

- XEP-0288: Bidirectional s2s Connections;
- XEP-0480: SASL Upgrade Tasks;
- IQ permission in privileged entities;
- PubSub varied fixes;
- WebAdmin improvements.

### 22.07.2024

#### Update Ejabberd to version [24.07](https://github.com/processone/ejabberd/releases/tag/24.07)

- Mostly a bugfix release for the recent update to version 24.06;
- Few improvements.

### 29.06.2024

#### Update Ejabberd to version [24.06](https://github.com/processone/ejabberd/releases/tag/24.06)

- Improved Web-based administration;
- Improved architecture and **API**.

### 29.02.2024

#### Update Ejabberd to version [24.02](https://github.com/processone/ejabberd/releases/tag/24.02)

- New: Matrix Federation - Provides the ability to connect to Matrix servers;
- Improved communication security by supporting TLS 1.3 and SASL2;
- Improved performance by implementing Bind 2;
- Better message control: Support for XEP-0424 (message retraction). It allows users to manage their message history and remove anything they posted by mistake;
- Optimized server ping via XEP-0198;
- Streamlined API versioning;
- Enhanced Elixir, Mix and Rebar3 Support.

### 14.11.2023

#### Updated Ejabberd to version [23.10](https://github.com/processone/ejabberd/releases/tag/23.10)

- Added support for XEP-0402: PEP Native Bookmarks, which is a significant improvement over XEP-0048: Bookmark Storage. Defines how bookmarks are stored;
- New: `mod_muc_occupantid` with support for XEP-0421: Occupant Id. Used for MUC anonymous rooms, fixing messages and withdrawing messages. Currently, the only client found to support XEP-0421 is Dino - version 0.4 and above;
- Many new options and features. For more information, see the official article on the [ProcessOne](https://www.process-one.net/) web site about what's new in version [23.10](https://www.process-one.net/blog/ejabberd-23-10/).

### 26.04.2023

#### Updated Ejabberd to version [23.04](https://github.com/processone/ejabberd/releases/tag/23.04)

- Many improvements in SQL databases;
- New: `mod_mam` support for [XEP-0425: Message Moderation](https://xmpp.org/extensions/xep-0425.html);
- New: `mod_muc_rtbl` support for **Real-Time Block List for MUC rooms**.

### 20.01.2023

#### Updated Ejabberd to version [23.01](https://github.com/processone/ejabberd/releases/tag/23.01)

- New: Registrations are open, using the online form or an installed client, protected by a **CAPTCHA** challenge.

### 30.10.2022

#### Updated Ejabberd to version [22.10](https://github.com/processone/ejabberd/releases/tag/22.10)

### 16.08.2022

#### Service migration from Prosody [0.12.1](https://prosody.im/doc/release/0.12.1) to Ejabberd [22.05](https://github.com/processone/ejabberd/releases/tag/22.05)

- New virtual server in the Swiss data center of **ORACLE Cloud**;
- New domain.
