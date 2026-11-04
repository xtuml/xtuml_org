---
redirect_from:
  - "/community/topic/bp-4-2-w7-update-causes-could-not-create-virtual-machine/"

layout: "topic"
title: "BP 4.2 - W7 update causes \"...could not create virtual machine\""
date: "2015-03-13"
permalink: "/forums/topic/bp-4-2-w7-update-causes-could-not-create-virtual-machine/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**John Wolfe** · March 13, 2015 at 7:36 pm

Last night W7 updated itself, and this morning, attempts to invoke BridgePoint 4.2 resulted in “Could not create the Java virtual machine.”
BridgePoint is distributed with a Java run-time environment (JRE) which may be a bit past its sell-by date. I pulled a newer version (8u40), adjusted Launcher.bat to use it, and this solved the problem. When selecting a new JRE, remember that BP 4.2 for Windows is distributed with a 32-bit version of Eclipse, so you’ll need a 32-bit JRE.
