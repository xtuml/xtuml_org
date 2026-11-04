---
redirect_from:
  - "/community/topic/ooa-20-questions-creation-events/"

layout: "topic"
title: "OOA '20 Questions: Creation Events"
date: "2019-09-26"
permalink: "/forums/topic/ooa-20-questions-creation-events/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · September 26, 2019 at 3:02 pm

# Method: Creation Events

Are creation events a Good Thing and to be
supported in xtUML as today?

Should creation events be deprecated?
(i.e., Is synchronous creation is sufficient?)

---

**Lee Riemenschneider** · September 27, 2019 at 6:00 pm

Creation events are a good thing, even if they are confusingly used as if synchronous creation by newbies.
Consider that the replacement for a creation event is an instance creation followed by an initialization event. Ugly!
