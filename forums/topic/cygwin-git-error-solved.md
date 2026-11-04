---
redirect_from:
  - "/community/topic/cygwin-git-error-solved/"

layout: "topic"
title: "cygwin git error solved"
date: "2013-05-06"
permalink: "/forums/topic/cygwin-git-error-solved/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**keithbrown** · May 6, 2013 at 5:13 pm

I was doing a clean cygwin configure and was getting an error “/usr/lib/git-core/git-remote-https.exe: error while loading shared libraries: ?: cannot open shared object file: No such file or directory” when I tried to use git to clone the github xtuml/models repository.

\$ git clone [https://keithbrown@github.com/xtuml/models.git](https://keithbrown@github.com/xtuml/models.git)

I had the git and git-completion packages installed already but it wasn’t working.

I found that in order to use this method of cloning, I also needed to manually install libsasl2 and ca-certificates cygwin packages. These are not picked up as git package dependencies in cygwin, so they must be selected by hand.
