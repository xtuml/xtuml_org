---
redirect_from:
  - "/community/topic/using-git/"

layout: "topic"
title: "Using Git"
date: "2017-02-17"
permalink: "/forums/topic/using-git/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**micke.x** · February 17, 2017 at 10:25 am

Anyone having a guideline for how to use Git as CM for xtUML projects?
Or practical tips, what do do / what not to, e.g when it comes to merging.
Resolving merge conflicts using Merge tool, does not seem to be so useful in practice – maybe I am using it wrong…

BridgePoint Structural compare often does not give any real help selecting which change to select – often the change is not even visualized.
Added classes in a package .xtuml file does not appear in this scope/file

Switching to Text Compare does not give that much help either – large chunks of several changes are grouped as one change – it seems to be in a special mode for .xtuml files…
And “Copy current change from left to right” does not seem to work at all – although it is not dimmed.

Changing file extension to .txt for two .xtuml files and comparing these gives better help trying to isolate changes in the storage format, although it is of course very error-prone, if you are forced to work on this level.

Hopefully, I am doing something fundamentally wrong – any help appreciated.

---

**keithbrown** · February 17, 2017 at 1:55 pm

Have you checked out the on-line course here on xtuml-org.hustlefish-sites.com? See Learn \> Online courses and tutorials \> Modeling with xtUML \> Module 5

That module discusses using git for CM of xtUML projects, including merging.

---

**keithbrown** · February 17, 2017 at 1:56 pm

Have you checked out the on-line course here on xtuml-org.hustlefish-sites.com? See Learn \> Online courses and tutorials \> Modeling with xtUML \> Module 5

That module discusses using git for CM of xtUML projects, including merging.

---

**micke.x** · February 17, 2017 at 3:41 pm

Thanks.

Well, I did now,
but I think the conflict examples were somewhat ideal/trivial.

Problematic conflicts, that I am trying to find WoW for include :
– structural non-leaf conflicts, e.g. in each branch a class is added to the same package
– conflicts in action code
– type name change, with propagation to all references (in several files)
