---
redirect_from:
  - "/community/topic/ooa-20-questions-event-queue-overrun/"

layout: "topic"
title: "OOA '20 Questions: event queue overrun"
date: "2019-09-26"
permalink: "/forums/topic/ooa-20-questions-event-queue-overrun/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · September 26, 2019 at 2:46 pm

# Method: Event Dispatch (2)

## event queue overrun

***dispatch of delayed events in the face of full queues***

Should delayed events be dispatched when expired
without regard to the presence of non-delayed events?

\[Scenario\] Consider a domain with non-empty event queues and
pending timers. At least one delayed event is past its expiration time.

\[Edge Case\] Consider a cyclic, “self-stimulating” state machine (or
interacting set of state machines) that spins with no delay.
The concept of ‘simulated time’ or ‘Discrete Event Simulation’ may
inform this discussion.

---

**Lee Riemenschneider** · September 27, 2019 at 4:59 pm

Again, like Event Dispatch (1), this should be part of the architecture definition. This could be handled like some operating systems handle threads/processes via a series of priority boosts until the neglected process gets a high enough priority to be handled.

---

**Nils** · February 17, 2020 at 1:16 pm

I agree, this is an issue for the Platform Specific Model (PSM) to handle, similar to a stack overflow. The Plaform Independent Model (PIM) just assumes (and correctly so) that events are delivered. This is true for bridges as well as class instances. If there are explicit requirements on QoS, then that should either be modeled in the PIM or formulated as a requirement on the particular PSM.

/Nils
