---
redirect_from:
  - "/community/topic/corrupted-library-message-on-launch-of-bp-on-fedora-25/"

layout: "topic"
title: "Corrupted library message on launch of BP on Fedora 25"
date: "2017-09-27"
permalink: "/forums/topic/corrupted-library-message-on-launch-of-bp-on-fedora-25/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Clive** · September 27, 2017 at 1:36 am

I have installed BP on Fedora 25 which comes standard with Java 1.8. The first problem I faced was that ‘lib/ld-linux.so.2’ failed to provide a correct ELF interpretation and that the directory did not exist. I attempted to fix this by making a symbolic link to ‘/usr/lib64/ld-linux-x86-64.so.2’, but this merely ave me a new message “…/Launcher.sh: line 14 \<my BPHOMEDIR\>/eclipse/eclipse: Accessing a corrupted shared library”.
I presume that this library is ‘libjvm.so’. Any clues as to the direction I should take to get BP going on Fedora 25. would be much appreciated.

---

**keithbrown** · September 27, 2017 at 1:45 am

Hello Clive,

I suggest you grab the nightly build from the download page rather than the community edition. There have been some packaging improvements since the community edition was last published. Hopefully that will resolve the issue.

Cheers,
Keith
