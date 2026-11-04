---
redirect_from:
  - "/community/topic/window-stuck-maximized-tip/"

layout: "topic"
title: "Window stuck maximized tip"
date: "2017-02-27"
permalink: "/forums/topic/window-stuck-maximized-tip/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Lee Riemenschneider** · February 27, 2017 at 1:04 pm

Ran into this issue today. It is a general eclipse problem. I maximized a package canvas and was unable to minimize it by any means (double-click tab, restore button on view, restore button on sidebar, …). Minimizing and restoring didn’t fix the problem. Opening other views didn’t fix the problem. Restarting BridgePoint didn’t fix the problem. Opening another perspective and going back to the xtUML Modeling perspective made the sidebar buttons go away. (Worse!)

The solution was to open another perspective, close the xtUML Modeling perspective, and then reopen the xtUML Modeling perspective.

---

**cort** · February 27, 2017 at 2:13 pm

There is a “reset perspective” under one of the menus. I think Window-\>Perspective-\>Reset Perspective.
