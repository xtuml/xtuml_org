---
redirect_from:
  - "/community/topic/blacking-out-bp-windows/"

layout: "topic"
title: "Blacking out BP windows"
date: "2021-06-16"
permalink: "/forums/topic/blacking-out-bp-windows/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Clive** · June 16, 2021 at 3:07 am

Since I’ve started using BP 7.1 on MacOS Big Sur I’ve found that the graphical windows containing diagrams (such as class diagrams etc.) display as totally black when activated from tabs. Sometimes, a simple mouse click displays the diagram, but at other times one is required to take other actions to expose the diagrams (such as resizing the window). Again, not a biggy, but it is annoying.

---

**cort** · June 16, 2021 at 9:16 am

I have begun seeing this, too. The next time I see it, I will raise an issue in the tracker with a screenshot.

The quickest work-around is to show/hide the Palette.

---

**Lee Riemenschneider** · June 16, 2021 at 10:25 am

I haven’t been seeing this on Linux (Debian 10) or on my day job, Windows PC, so this must be MacOS specific.

Might be related to this: [https://bugs.eclipse.org/bugs/show_bug.cgi?id=568813](https://bugs.eclipse.org/bugs/show_bug.cgi?id=568813)
