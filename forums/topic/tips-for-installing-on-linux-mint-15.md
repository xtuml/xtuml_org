---
redirect_from:
  - "/community/topic/tips-for-installing-on-linux-mint-15/"

layout: "topic"
title: "Tips for Installing on Linux Mint 15"
date: "2013-11-25"
permalink: "/forums/topic/tips-for-installing-on-linux-mint-15/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**keithbrown** · November 25, 2013 at 3:41 pm

1\) Installer would not run. There is a JRE 32/64-bit compatibility problem. So:

\[code title=””\]\$ sudo apt-get install ia32-libs-multiarch
\[/code\]

2\) I knew from other linux installs to make sure dos2unix is available:

\[code title=””\]\$ sudo apt-get install dos2unix
\[/code\]

Note, on other ubuntu systems dos2unix does not technically exist. You have to use the “tofrodos” package:

\[code title=””\]\$ sudo apt-get install tofrodos
\$ cd /usr/bin
\$ sudo ln -s fromdos dos2unix
\$ sudo ln -s todos unix2dos
\[/code\]

3\) When running the commercial BridgePoint tool, I know I want tools for code translation, so:
\[code title=””\]\$ sudo apt-get install wine
\$ sudo apt-get install libstdc++5\[/code\]

---

**keithbrown** · February 21, 2014 at 3:14 pm

If you have additional input based on personal experience, please add it here.

- This reply was modified 11 years, 11 months ago by [![](https://secure.gravatar.com/avatar/6ff171c9228db912f70e19b4b7becef5358bb84d05cdc10ad8a78302932ecf21?s=14&amp;d=mm&amp;r=g)keithbrown]({{ '/user/keithbrown/' | relative_url }}).

---

**Bob Mulvey** · September 22, 2014 at 5:27 am

The instructions above also work for Ubuntu 14.04 LTS, but in step 1 to install ia32-lis-multiarch you may need to follow these directions:
[http://stackoverflow.com/questions/23182765/how-to-install-ia32-libs-in-ubuntu-14-04-lts](http://stackoverflow.com/questions/23182765/how-to-install-ia32-libs-in-ubuntu-14-04-lts)

---

**Bob Mulvey** · May 8, 2015 at 8:17 pm

BridgePoint now has a developer’s guide that focuses on ubuntu. There is a FAQ that describes linux package-specifIc installation issues (as well as Windows). The Developer’s Getting started will point you to the FAQ,but here are inks:
Developer’s Getting Started: [https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/Developer%20Getting%20Started%20Guide.md](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/Developer%20Getting%20Started%20Guide.md)
FAQ: [https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/FAQ.md](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/FAQ.md)
