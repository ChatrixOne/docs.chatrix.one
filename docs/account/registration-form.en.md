---
title: Online Registration
icon: material/file-document-edit
---

# Online Registration

<figure markdown>
   ![Register New Account](../resources/img/register.svg){: width="800" }
   <figcaption>Online registration form for <b>Chatrix.One</b></figcaption>
</figure>

The page allows you to self-register an **XMPP** account on this server. Your **JID** (**Jabber ID**) will be in the format `username@chatrix.one`. Please read the instructions carefully to fill in the fields correctly.

## Username

The username **JID** (**Jabber ID**) is **not** case sensitive. It is recommended to use only lowercase letters. The usernames `TestUser`, `testUser`, `TESTuser`, etc. will be interpreted as: `testuser@chatrix.one`. Special characters `"` `&` `'` `/` `:` `<` `>` `@` are not allowed in the profile name. To separate the names, you can use the characters: `.` `_` `-`. For example: `test.user` or `test_user` etc.

Only the username is entered, without the server part. For example: If the user is `john@chatrix.one` you enter just `john`.

!!! failure "Important"

    Usernames like `administrator@chatrix.one`, `xmppadmin@chatrix.one`, `admin_team@chatrix.one`, `moderator@chatrix.one` and similar are prohibited. Any accounts whose names resemble an admin account will be deleted **WITHOUT** warning!

    !!! quote ""

        Currently, the server has only one administrator with the address: admin:simple-maildotru:chatrix.one

## Server

This field should be automatically filled in. Check if it says: `chatrix.one`

## Password

By default, the server does not allow the use of weak passwords of the type `123456`, `abc123`, etc. I advise you to use password management software (**Password Manager**) to generate a password that is difficult to crack.

Do not tell anyone your password, not even the administrators of this **XMPP** server. You will later be able to change your password using your **XMPP** client or from the [change password page](https://chatrix.one/user/change_password/).

!!! tip "Tip"

      Some **XMPP** clients can store the password on the computer, but for security reasons it is recommended that you only do this on your personal device.

  Remember your password or write it down on a piece of paper in a safe place. It is best to use password management software. In **XMPP** there is no (at least not yet) an automated way to recover the password in case you forget it. If this happens you will need to register a new account.

## Password verification

Here you will need to re-enter your chosen password. It must match what you entered in the **Password** field.

## Challenge - **CAPTCHA**

In order to protect against bots, you need to enter a six-digit code. You will see a challenge generated as a picture. If the task seems too difficult for you, you can refresh the page with ++f5++ to generate a new challenge.

!!! info "Information"

     In case you don't see a **CAPTCHA** code, you may have a browser extension installed that is blocking the preview. In this case, temporarily disable the extension or use a different web browser.

[Account Registration](https://chatrix.one/join/){ .md-button }
