# Status Of Services

???- bug "Scheduled maintenance"

     | Date        | Time interval    | Note                                        |
     |:------------|:----------------:|:-------------------------------------------:|
     | 26.10.2024  |05:30 - 6:30 EET  | **XMPP** service interruptions are possible |

## Account Registrations

| Тype              |Rate Limit              |Status                           |
|:------------------|:----------------------:|-------------------------:|
| Online            |One per hour            |![Registration Status](https://uptime.tinyserver.eu/api/badge/141/status?label=&upLabel=OPEN&downLabel=CLOSED) |
| Installed Client  |One per hour from an IP |![Registration Status](https://uptime.tinyserver.eu/api/badge/141/status?label=&upLabel=OPEN&downLabel=CLOSED) |

## Availability - **XMPP**

| Indicator                          | Value                                                                          |
|:-----------------------------------|:------------------------------------------------------------------------------:|
| Average ping for the last 24 hours | ![Ping Average](https://uptime.tinyserver.eu/api/badge/137/ping?label=)        |
| Uptime for the last 24 hours       | ![Uptime 24h](https://uptime.tinyserver.eu/api/badge/121/uptime/24?label=)     |
| Uptime for the last 7 days         | ![Uptime 7 days](https://uptime.tinyserver.eu/api/badge/121/uptime/168?label=) |
| Uptime for the last 30 days        | ![Uptime 7 days](https://uptime.tinyserver.eu/api/badge/121/uptime/720?label=) |

## Compliance and Compatibility - **XMPP**

| Test                    |Result                                                                     |
|:------------------------|--------------------------------------------------------------------------:|
| **XMPP** Compliance     | <a href='https://compliance.conversations.im/server/chatrix.one'><img src='https://compliance.conversations.im/badge/chatrix.one'></a> |
| **XMPP Providers**      | <a href="https://providers.xmpp.net/provider/chatrix.one/"><img alt="chatrix.one badge" src="https://data.xmpp.net/providers/v2/badges/chatrix.one.svg"></a> |
| **IM Observatory**      | <a href='https://xmpp.net/result.php?domain=chatrix.one&type=client'><img src='https://chatrix.one/badge.svg'></a> |
|**SRV** Records / Access | <a href='https://xmpp.love/servers/chatrix.one/results'><img src='https://xmpp.love/servers/chatrix.one/badge' width='201px' height= '18px' alt='xmpp.love score'></a> |

## Availability - Websites

### [Documentation](https://docs.chatrix.one)

| Indicator                          | Value                                                                      |
|:-----------------------------------|:--------------------------------------------------------------------------:|
| Average ping for the last 24 hours |![Ping Average](https://uptime.tinyserver.eu/api/badge/135/ping)            |
| Uptime for the last 24 hours       |![Uptime 24h](https://uptime.tinyserver.eu/api/badge/135/uptime/24?label=)  |
| Uptime for the last 7 days         |![Uptime 24h](https://uptime.tinyserver.eu/api/badge/135/uptime/168?label=) |
| Uptime for the last 30 days        |![Uptime 24h](https://uptime.tinyserver.eu/api/badge/135/uptime/720?label=) |

### [Blog](https://blog.chatrix.one)

| Indicator                          |Value                                                                           |
|:-----------------------------------|:------------------------------------------------------------------------------:|
| Average ping for the last 24 hours | ![Ping Average](https://uptime.tinyserver.eu/api/badge/124/ping?label=)        |
| Uptime for the last 24 hours       | ![Uptime 24h](https://uptime.tinyserver.eu/api/badge/124/uptime/24?label=)     |
| Uptime for the last 7 days         | ![Uptime 7 days](https://uptime.tinyserver.eu/api/badge/124/uptime/168?label=) |
| Uptime for the last 7 days         | ![Uptime 7 days](https://uptime.tinyserver.eu/api/badge/124/uptime/720?label=) |

## Technical data

### XMPP Server

| Parameter        | Value                          |
|:-----------------|:------------------------------:|
| Processor        | ARM Ampere                     |
| RAM              | 12GB                           |
| Disk Space       | 64GB                           |
| File System      | ext4                           |
| Operating System | Ubuntu 22.04 (Jammy Jellyfish) |
| Ejabberd version | 24.7.0                         |
| Backup           | Weekly                         |
| Location         | Switzerland                    |
| Powered with     | 100% Renewable energy          |

<!-- [<img src="https://app.greenweb.org/api/v3/greencheckimage/chatrix.one?nocache=true" alt="This website runs on green hosting - verified by thegreenwebfoundation.org" width="200px" height="95px">](https://www.thegreenwebfoundation.org/green-web-check/?url=chatrix.one) -->

#### Information about XEPs

| XEP                                        | Availability                   |
|:-------------------------------------------|:------------------------------:|
| XEP-0045: Multi-User Chat                  | :material-check-bold:{ .green} |
| XEP-0054: vcard-temp                       | :material-check-bold:{ .green} |
| XEP-0065: SOCKS5 Bytestreams (Proxy)       | :material-check-bold:{ .green} |
| XEP-0077: In-Band Registration             | :material-check-bold:{ .green} |
| XEP-0115: Entity Capabilities              | :material-check-bold:{ .green} |
| XEP-0153: vCard-Based Avatar (MUC)         | :material-check-bold:{ .green} |
| XEP-0156: Discovering Alternative XMPP Connection Methods (HTTP) | :material-check-bold:{ .green} |
| XEP-0157: Contact Addresses for XMPP Services (Abuse) | :material-check-bold:{ .green} |
| XEP-0160: Best Practices for Handling Offline Messages | :material-check-bold:{ .green} |
| XEP-0163: PEP (Avatars / OMEMO)            | :material-check-bold:{ .green} |
| XEP-0191: Blocking Command                 | :material-check-bold:{ .green} |
| XEP-0198: Stream Management                | :material-check-bold:{ .green} |
| XEP-0215: External Service Discovery STUN  | :material-check-bold:{ .green} |
| XEP-0215: External Service Discovery TURN  | :material-check-bold:{ .green} |
| XEP-0258: Security Labels in XMPP          | :octicons-x-12:{ .red}         |
| XEP-0237: Roster Versioning                | :material-check-bold:{ .green} |
| XEP-0280: Message Carbons                  | :material-check-bold:{ .green} |
| XEP-0313: Message Archive Management       | :material-check-bold:{ .green} |
| XEP-0313: Message Archive Management - MUC | :material-check-bold:{ .green} |
| XEP-0313: Message Archive Management (extended usage) | :octicons-x-12:{ .red} |
| XEP-0352: Client State Indication          | :material-check-bold:{ .green} |
| XEP-0357: Push Notifications               | :material-check-bold:{ .green} |
| XEP-0363: HTTP File Upload                 | :material-check-bold:{ .green} |
| XEP-0368: SRV records for XMPP over TLS    | :material-check-bold:{ .green} |
| XEP-0384: OMEMO Encryption                 | :material-check-bold:{ .green} |
| XEP-0386: Bind 2                           | :material-check-bold:{ .green} |
| XEP-0388: Extensible SASL Profile          | :material-check-bold:{ .green} |
| XEP-0398: Avatar Conversion                | :material-check-bold:{ .green} |
| XEP-0402: PEP Native Bookmarks             | :material-check-bold:{ .green} |
| XEP-0411: Bookmarks Conversion             | :material-check-bold:{ .green} |
| XEP-0444: Message Reactions                | :material-check-bold:{ .green} |

#### File upload limits

| Limit                     | Value    |
|:--------------------------|:--------:|
| Single file upload        | 100 MB   |
| Total volume - soft limit | 950 MB   |
| Total volume - hard limit | 1000 MB  |
| Storage period            | 28 days  |

#### Offline message limits

| User           | Total |
|:---------------|:-----:|
| Standard       | 100   |
| Sponsor :star: | 1000  |

### Backup server

| Parameter        | Value                |
|:-----------------|:--------------------:|
| Processor        | AMD EPYC 3251        |
| RAM              | 64GB                 |
| Disk Space       | 5TB                  |
| File System      | ZFS (RAIDZ-1)        |
| Operating System | Debian 12 (Bookworm) |
| Location         | Bulgaria             |

## Information about occurred incidents

!!! abstract "Incidents"

     There are currently no documented incidents.

## Update history

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

#### Service migration from Prosody [0.12.1](https://prosody.im/doc/release/0.12.1) to EJabberd [22.05](https://github.com/processone/ejabberd/ releases/tag/22.05)

- New virtual server in the Swiss data center of **ORACLE Cloud**;
- New domain.
