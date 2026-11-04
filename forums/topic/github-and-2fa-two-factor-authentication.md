---
redirect_from:
  - "/community/topic/github-and-2fa-two-factor-authentication/"

layout: "topic"
title: "Github and 2FA (Two Factor Authentication)"
date: "2015-02-17"
permalink: "/forums/topic/github-and-2fa-two-factor-authentication/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**keithbrown** · February 17, 2015 at 3:34 pm

In order to support an extra layer of security on github.com, the xtUML organization uses github’s 2FA mechanism. This involves:

1\) Configuring 2FA on your github.com account (See [https://help.github.com/articles/about-two-factor-authentication/](https://help.github.com/articles/about-two-factor-authentication/) . We set up using SMS. You can use TOTP if you prefer.)

2\) Create an access token (See [https://help.github.com/articles/creating-an-access-token-for-command-line-use/](https://help.github.com/articles/creating-an-access-token-for-command-line-use/)) You use this token instead of a password when connecting to a github repository from the command line or in egit inside BridgePoint.
a) If you already have connections set up to github repositories, you can change the credentials to use the new access token instead of your password.

- Open the Git Repository Exploring perspective, expand the repository
- Expand “Remotes”.
- Expand each remote you have set up.
- Next, go through each pull and push config under each remote, right-click and choose “Change Credentials…” Enter your username and in the password field enter your access token.
