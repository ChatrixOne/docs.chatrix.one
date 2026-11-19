---
title: Chatrix.One for Android
icon: material/android
---

# Chatrix.One for Android

**Chatrix.One** for Android is based on [Conversations](https://codeberg.org/iNPUTmice/Conversations) and adds a few features to it. It is open source (GPL-3.0 license) and works with any XMPP provider, not only Chatrix.One.

## What Chatrix.One adds

| Feature | Where in the app |
|:--------|:-----------------|
| Quick gestures: swipe left to quote, swipe right to react, double-tap to copy. Each gesture can also be set to **Share with…** | **Settings → Interface → Message gestures** |
| A row of reactions, the full emoji picker and keyboard input | long-press a message |
| Optional notifications when someone reacts to your message (off by default) | **Settings → Notifications → Notify on reactions**, and per chat in the chat menu |
| Voice messages at 1×, 1.5× or 2×. The speed is remembered and can be changed while playing | the small button in the bottom line of a voice message |
| Link previews (off by default): a card with the title, website and picture of a link | **Settings → Privacy → Link previews** |
| Chatrix.One texts in all 39 languages of the app | **Settings → Interface → Language** |
| Chatrix.One colours, launcher and notification icons, chat backgrounds (also per chat) | |
| Welcome screen with a Chatrix.One sign-up link; any other XMPP provider still works | first start |

## Privacy

Link previews
:   Only for links in your own messages and in messages from people in your contact list (also in group chats), never when Tor is on. Each link is loaded once and kept on the phone. The website of the link sees your IP address, as when you open the link yourself.

Crash reports
:   Only sent when you choose to.

Update check
:   Versions installed by hand from GitHub can check once a day for a new version and show a notification. The check sends no identifiers and can be turned off. It is off when Tor is on, and off when installed through Obtainium, because Obtainium handles updates itself.

## Install

Install Chatrix.One with Obtainium: see [Chatrix.One with Obtainium](obtainium.md). Obtainium also tells you when a new version is out.

Chatrix.One installs next to Conversations (its own package `one.chatrix.app`). To move your accounts, create a backup in Conversations and restore it in Chatrix.One.

## Version numbers

A version such as `2.21.3-cx1.1` means: based on Conversations 2.21.3. `-cx1` is the first Chatrix.One release on that Conversations version, `-cx1.1`, `-cx1.2`, … are Chatrix.One releases after it. All releases and their notes are in the [GitHub releases](https://github.com/ChatrixOne/Chatrix.One-android/releases).

* * *

Back to [Clients](../clients.md).
