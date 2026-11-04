---
redirect_from:
  - "/community/topic/can-xtuml-utilize-papyrus-uml-models-and-vice-versa/"

layout: "topic"
title: "Can xtUML utilize Papyrus UML models and vice versa?"
date: "2016-05-01"
permalink: "/forums/topic/can-xtuml-utilize-papyrus-uml-models-and-vice-versa/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**Rob** · May 1, 2016 at 9:39 pm

Can xtUML utilize Papyrus models and vice versa? If so, is there any examples of how this is done? Is this done with UML-RT?

---

**cort** · May 2, 2016 at 12:50 am

Hello Rob,

The key to your question is ‘utilize’.

xtUML and UML-RT define modeling dialects that are expressed in UML diagrams and action language or C++ that result in executable models.

Papyrus-RT (UML-RT) uses Papyrus as the graphics modeling platform. BridgePoint (xtUML) uses its own diagramming plugins today but is migrating to Papyrus platform over the next several months.

It will depend on what you mean by utilize to work toward a more clear answer.

Regards,
Cort

---

**keithbrown** · May 2, 2016 at 1:14 pm

Hi Rob,

You may also be interested to know that the xtUML team has created a prototype demonstration that shows a xtUML model working together and communicating with a capsule written in Papyrus-RT. See [https://www.youtube.com/watch?v=f6LPv5Ln19k](https://www.youtube.com/watch?v=f6LPv5Ln19k) .

Cheers,
Keith
