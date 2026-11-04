---
redirect_from:
  - "/community/topic/state-transition-table-and-creation-events/"

layout: "topic"
title: "State Transition Table and Creation Events"
date: "2016-06-10"
permalink: "/forums/topic/state-transition-table-and-creation-events/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · June 10, 2016 at 4:27 pm

I noticed this morning that the definition for the state transition table (STT) in Object Lifecycles: Modeling the World in States, nullifies the need for including creation events. In the OOA96 Report, there is an example STT that includes the creation event and has a row entry (state of instance) labeled as “None”. Off hand, I don’t remember if Executable UML: A Foundation for Model-driven Architecture addresses this, but it seems to me that the example in OOA 96 is wrong.

Here’s my reasoning:
1. While you could include a “None” row, this is the equivalent of declaring a non-state as a member of the set of states, which doesn’t make logical sense.
2. The purpose of the state transition table is to show what happens when an event is sent to a class instance. In the “None” state\[sic\], there is no instance. (Note: class-based state models are orthogonal to the concept of “None”.)
3. The creation event is always a “Can’t Happen” when in an instance state and only targets one transition, so it is very uninteresting to include in the STT.
