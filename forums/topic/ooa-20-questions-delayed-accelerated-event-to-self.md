---
redirect_from:
  - "/community/topic/ooa-20-questions-delayed-accelerated-event-to-self/"

layout: "topic"
title: "OOA '20 Questions: Delayed accelerated event to self"
date: "2019-09-26"
permalink: "/forums/topic/ooa-20-questions-delayed-accelerated-event-to-self/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · September 26, 2019 at 2:51 pm

# Method: Event Dispatch (3)

## Delayed accelerated event to self

***accelerating delayed events***

Is a delayed event to self treated the same as a
delayed event to any instance?

\[Scenario\] An instance state machine sets a timer
and supplies an event directed to itself.

---

**Lee Riemenschneider** · September 27, 2019 at 5:53 pm

I wondered where this question came from until the discussion at xtUML Days 2019. The discussion between Cortland Starrett and Allan Kennedy revealed that often two event queues are used; one for self-directed events, and one for all other events. In my mind, I only imagined one queue (I wasn’t envisioning self-directed events to stack up), where self-directed events went to the top and non-self-directed events went to the bottom.
In any case, delayed events are just events that get fired from the time domain (the queue discussion makes this an interesting concept (more below)), and should get treated as if they were called directly. This means that delayed self-directed events should go to the event queue, and delayed non-self-directed events should go to the normal event queue.
The interesting thing about considering events from the time domain is that the queue discussion also had a queue for external messages. Queue priority was stated as, “empty self-directed queue, then empty event queue, then empty external message queue”, so a timer domain message might be considered as lowest priority. I’m not sure I agree with that priority order, but I also don’t know if it’s specified in an OOA ‘xx. I would want external events to get put in the normal event queue as they are received.

---

**Nils** · February 17, 2020 at 12:27 pm

I’ve heard about this approach with 2 queues as well elsewhere. The thing is, at any given time and for a given class instance, there can be at most 1 self-directed event (non-delayed). Consequently, using a queue for self-directed events is overkill. All that is needed is a simple reference to the last sent self-directed event. When that reference is empty, it’s time to get next event from the queue.

I’m not following you all the way but my understanding of the xtUML formalism is that there 3 kinds of queues; bridge queues, class instance queues and a delay queue (probably what you call the time domain). The delay queue is only a holding place for delayed events waiting for their timer to expire. When that happen, the event is pushed to the class instance queue in the same way as any non-self-directed event. So, refering the original post, the answer is Yes.

Probably a good time to check out if Leslie Lamport has something to say on the subject matter.

/Nils

- This reply was modified 5 years, 12 months ago by [![](https://secure.gravatar.com/avatar/fbfa4355e6d4aabc5918f55562a1246db838ff2c01ee3289ee24d56d8b0a5bfd?s=14&amp;d=mm&amp;r=g)Nils]({{ '/user/nils/' | relative_url }}).
