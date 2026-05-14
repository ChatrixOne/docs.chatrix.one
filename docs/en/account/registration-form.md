---
title: Online Registration
icon: material/file-document-edit
---

# Online Registration

The page allows you to self-register an XMPP account on this server. Your **JID** (**Jabber ID**) will be in the format `username@chatrix.one`. Please read the instructions carefully before filling in the fields.

## Challenge - CAPTCHA

To protect against bots, you need to complete a puzzle before proceeding. The process works as follows:

1. Check the **I am a human** checkbox
2. Click **Continue**
3. Solve the puzzle presented to you
4. Click **Continue** once solved

If the puzzle seems too difficult, click **Refresh Challenge** to get a new one. The challenge is also available in multiple languages.

!!! info "Information"

    In case you don't see the CAPTCHA challenge, you may have a browser extension installed that is blocking it. In this case, temporarily disable the extension or use a different web browser.

## Username

The username is **not** case sensitive. Use only lowercase letters. The usernames `TestUser`, `testUser`, `TESTuser` etc. will all be interpreted as `testuser@chatrix.one`. Special characters `"` `&` `'` `/` `:` `<` `>` `@` are not allowed. To separate words, use `.` `_` or `-` — for example `test.user` or `test_user`.

Enter only the username, without the server part. For example: if the desired JID is `john@chatrix.one`, enter just `john`.

!!! failure "Important"

    Usernames like `administrator`, `xmppadmin`, `admin_team`, `moderator` and similar are prohibited. Any account whose name resembles an admin account or contains the word `chatrix` will be deleted **WITHOUT** warning!

    !!! quote ""

        The server has one administrator: `admin@chatrix.one`

## Server

This field is filled in automatically. Check that it shows: `chatrix.one`

## Password

By default, the server does not allow weak passwords such as `123456` or `abc123`. Use a **Password Manager** to generate a strong password.

Do not share your password with anyone, including the server administrators. You can change your password later using your XMPP client or from the [change password page](https://chatrix.one/user/change_password/).

!!! warning "Save your credentials"

    There is no password reset mechanism on this server. If you forget your password, your only option is to register a new account and start over. Write down your username and password and keep them in a safe place, or store them in a password manager such as [Bitwarden](https://bitwarden.com/).

!!! tip "Tip"

    Some XMPP clients can store the password on your device. Only do this on your personal device.

[Register Account](https://chatrix.one/join){ .md-button }
