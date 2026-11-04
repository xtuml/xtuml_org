---
redirect_from:
  - "/community/topic/ooa-20-questions-delayed-events/"

layout: "topic"
title: "OOA '20 Questions: delayed events"
date: "2019-09-26"
permalink: "/forums/topic/ooa-20-questions-delayed-events/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · September 26, 2019 at 2:39 pm

# Method: Event Dispatch (1)

## delayed events

***simultaneous expired timers (delayed events)***

How should simultaneously expired
delayed events be dispatched?

\[Scenario\] Consider a domain with empty event
queues and 3 pending timers. All 3 delayed events
are past their expiration time. The first 2 delayed
events in the queue have the same expiration time.

---

**Lee Riemenschneider** · September 27, 2019 at 4:54 pm

There should be an architecture recommended best practice for handling this, or maybe it could be a part of the model compiler options to handle it.
It’s probably not a good idea to have multiple threads managing the event queue. ;-)
