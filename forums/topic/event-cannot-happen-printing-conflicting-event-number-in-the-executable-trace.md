---
redirect_from:
  - "/community/topic/event-cannot-happen-printing-conflicting-event-number-in-the-executable-trace/"

layout: "topic"
title: "[Event cannot happen] printing conflicting event number in the executable trace"
date: "2024-02-01"
permalink: "/forums/topic/event-cannot-happen-printing-conflicting-event-number-in-the-executable-trace/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Schmill** · February 1, 2024 at 7:39 am

When using the verifier, I get a well formatted message indicating the event that cannot happen in the current state. but when observing the trace oof the generated executable, I can only see the state number.

I tried to modify the dispatch function by adding `printf( "Event: %s \n", GetOoaEventNumber( event )); ` but unfortunately this yields null.

How can I trace the conflicting event Number?

Thank you.

---

**cort** · February 1, 2024 at 10:34 am

Did you mark the state transition tracing on? (.invoke MarkStateTransitionTracingOn( “\*” ))
This mark is found in the domain.mark file.

---

**Schmill** · February 1, 2024 at 11:07 am

Indeed this mark is enabled. but I do not get the event number, here is a sample trace:
`Event cannot happen: ND current_state = 3`

---

**cort** · February 1, 2024 at 11:21 am

Hmm, that looks like it should work.

---

**Schmill** · February 1, 2024 at 11:53 am

I used the `UserEventCantHappenCalloutf` now with the line `printf( "Event: %hhu in state: %hhu \n", event_number,current_state);`
prints:
`Event: 0 in state: 3`
Also cheeked in another place with different Cannot Happen, it is also 0.

---

**Schmill** · February 2, 2024 at 9:15 am

It appears that I was confused by the fact that event_number does not correspond to the event numbers displayed in Bridgepoint, so 0 is a valid number.

---

**cort** · February 2, 2024 at 11:03 am

Right, there is a mapping. Because BridgePoint allows event numbers to be anything. And the dispatcher needs to index into an array.
