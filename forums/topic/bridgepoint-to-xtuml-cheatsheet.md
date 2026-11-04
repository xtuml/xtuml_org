---
redirect_from:
  - "/community/topic/bridgepoint-to-xtuml-cheatsheet/"

layout: "topic"
title: "BridgePoint to xtUML Cheatsheet"
date: "2016-04-27"
permalink: "/forums/topic/bridgepoint-to-xtuml-cheatsheet/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Lee Riemenschneider** · April 27, 2016 at 11:34 am

This is something I always have to try to keep in my mind, ever since BridgePoint added Components for system-level modeling capability.

These terms are going to be laid out as BridgePoint on the left and xtUML on the right.

\* *Project* – **N/A**
\* *Package* – **N/A**
\* *Component Package (Outer)* – **Domain**
\* *Nested Component* – **N/A (not allowed)**
\* *Component Package (Inner)* – **Subsystem**
\* *Port* – **N/A**
\* *Interface* – **N/A**
\* *Interface Signal* – **Bridge**
\* *Interface Operation* – **Bridge (Synchronous Service)**

---

**Lee Riemenschneider** · April 27, 2016 at 11:56 am

Forgot one:

\* *External Entity* – **External Entity (with caveats)**

This one deserves a little explanation. The pre-system modeling BridgePoint only modeled one domain, so EEs were used to represent all other domains. With system modeling, the EE only represents a domain not visible in the system.
