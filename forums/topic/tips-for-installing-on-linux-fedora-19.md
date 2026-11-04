---
redirect_from:
  - "/community/topic/tips-for-installing-on-linux-fedora-19/"

layout: "topic"
title: "Tips for Installing on Linux Fedora 19"
date: "2013-11-25"
permalink: "/forums/topic/tips-for-installing-on-linux-fedora-19/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**keithbrown** · November 25, 2013 at 3:28 pm

1\) Tried to run installer. It failed with:

\[code title=””\]bash: ./xtUMLEditor_v4.1.2.ixl: /lib/ld-linux.so.2: bad ELF interpreter: No such file or directory\[/code\]

This appears to be a library compatibility problem. I knew I would want wine
eventually anyway, and thought installing it may pull in the libs I need. So I did:

\[code title=””\]\$ sudo yum install wine
\$ sudo yum install gcc-c++\[/code\]

And let it pull in all the dependencies it wanted to. After the wine install completed, the
installer runs OK, but the installation is still not correct.

2\) The post-install log (in ~/mgc/install.ixl/LOGS/) indicated failure running dos2unix, so:

\[code title=””\]\$ sudo yum install dos2unix\[/code\]

and re-run the the installer. Now the install was good.

3\) However, when I ran Launcher.sh, nothing happens. Looked at log (in ~/MentorGraphics/xtUMLEditor/eclipse/configuration)
and see a SWT/gtk library error. So:

\[code title=””\]\$ sudo yum install compat-libstdc++-33
\$ sudo yum install gtk2.i686\[/code\]

xtUML Editor now starts properly.

---

**Bob Mulvey** · May 8, 2015 at 8:18 pm

BridgePoint now has a developer’s guide that focuses on ubuntu. There is a FAQ that describes linux package-specifIc installation issues (as well as Windows). The Developer’s Getting started will point you to the FAQ,but here are inks:
Developer’s Getting Started: [https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/Developer%20Getting%20Started%20Guide.md](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/Developer%20Getting%20Started%20Guide.md)
FAQ: [https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/FAQ.md](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/FAQ.md)
