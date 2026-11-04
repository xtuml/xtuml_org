---
redirect_from:
  - "/community/topic/how-to-mark-a-relationship-as-composed/"

layout: "topic"
title: "How to mark a relationship as composed?"
date: "2013-10-03"
permalink: "/forums/topic/how-to-mark-a-relationship-as-composed/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**sfinnie** · October 3, 2013 at 9:48 am

Trying to define a Rel as composed, can’t figure out how to do it.

The docs say it’s possible:

> A slash (“/”) is shown in front of the relationship number if the association is derived (i.e., compositional) with the relationship numbers that compose the association shown in curly braces, separated by commas, e.g., /R3 {R1,R2}.

However I can’t see how to do it. Pointers appreciated.

Thanks,
Scott.

---

**Travis London** · November 4, 2013 at 3:24 pm

The metamodel supports derived associations. The support for creating them was never ported to the new eclipse based tool that I know of.

Regards,
Travis
