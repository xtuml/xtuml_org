---
redirect_from:
  - "/community/topic/where-to-put-the-referential-attributes/"

layout: "topic"
title: "Where to put the referential attributes?"
date: "2018-06-28"
permalink: "/forums/topic/where-to-put-the-referential-attributes/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · June 28, 2018 at 12:17 pm

I recently put this together for some work I’m doing. It only lists the preferred locations. Leon Starr used to have a paper that showed the non-preferred locations, which are allowed by BridgePoint, but it should be noted that they do not conform to the relational model.

All rules are reflexive. e.g., 1c:1 follows the same rule as 1:1c

1:1 – choose either side
1:1c – 1c
1:M – M
1:Mc – Mc
1c:1c – use associative object
1c:M – use associative object
1c:Mc – use associative object
M:M – use associative object
Mc:M – use associative object
Mc:Mc – use associative object

---

**Lee Riemenschneider** · June 29, 2018 at 10:32 am

Sorry. Let’s do this again, in UML.

All rules are reflexive. e.g., 0..1:1 follows the same rule as 1:0..1

1:1 – choose either side
1:0..1 – 0..1
1:1..\* – 1..\*
1:\* – \*
0..1:0..1 – use associative object
0..1:1..\* – use associative object
0..1:\* – use associative object
1..\*:1..\* – use associative object
\*:1..\* – use associative object
\*:\* – use associative object
