---
redirect_from:
  - "/community/topic/adding-built-in-external-entities/"

layout: "topic"
title: "Adding built-in external entities"
date: "2013-10-24"
permalink: "/forums/topic/adding-built-in-external-entities/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dennis Tubbs** · October 24, 2013 at 2:15 pm

Hi,
I am trying to add the built-in Time external entity to my project. I am selecting “Add Built-in External Entities” from the context menu displayed when I right-click on a top level package, but nothing appears to be happening. What am I missing?

Thanks,
Dennis

---

**keithbrown** · October 28, 2013 at 1:15 pm

There is a bug that currently prevents the menu from working as desired. The work around is to open “Help \> Welcome Quick Start” and create the GPS Watch example model. Once the model is created, you will see it contains a “Shared EEs” package. You can either copy and paste the entire package or a specific EE to your own model.

The next version of xtUML Editor will have a fixed “Add EEs” menu as well as contain additional enhancements that allow xtUML Execute to pull EE implementations from a jar file like it currently does with realized components.
