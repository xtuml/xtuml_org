---
redirect_from:
  - "/community/topic/why-does-a-transition-set-mode-a-mode-property-using-signals-video/"

layout: "topic"
title: "Why does a transition set mode a mode property (Using signals ... video)?"
date: "2014-12-04"
permalink: "/forums/topic/why-does-a-transition-set-mode-a-mode-property-using-signals-video/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dan George** · December 4, 2014 at 2:22 am

The “Using Signals as Class State Machine Transitions” shows how OAL can be added to a transition.
1. Lahman recommends Moore FSM notation for reasons listed in his book. Is this good advice but some BridgePoint customers had their own opinions? Or, is it bad advice?
2. If we were going to add OAL to the transition, I thought it would send a signal to the instance based SM. The example actually sets a property instead. I know it is just an example but do I have it wrong? Is it normal to change “modes” by directly changing mode properties instead of sending signals?

Thank you for any insights.

Dan G

---

**Dan George** · December 4, 2014 at 2:24 am

Oops, partial edit should not have left an extra *mode* in the title. Sorry.

---

**Lee Riemenschneider** · December 4, 2014 at 7:39 pm

1\. I don’t remember if it was stated in the Shlaer-Mellor or Mellor-Balcer books or if I read/heard it elsewhere, but Moore and Mealy are mathematically equivalent. It really doesn’t matter which one you use. I agree with Lahman’s preference, but it really doesn’t matter.

2\. I didn’t see anything in the video that said setting the mode attribute was causing a transition in the instance based SM. If it was the intended effect, then you would need to send a signal. The video is just showing simple OAL usage in a transition.

---

**Dan George** · December 4, 2014 at 8:31 pm

Thanks, Lee. Mealy and Moore can always be alternatively used describe the same FSM. Lahman’s reason to adamantly insist on Moore is that Mealy treads on the “I’m done” perspective of events by implying events indicate “Do this.” So, good advice but opinions certainly could vary.

Right. There wasn’t an mention of what changing the mode property meant to the instance, let alone the instance SM. I was conflating mode and state. I looked at the GPS model but the display doesn’t even have an instance, just a class state machine whose actions change properties on instances of other classes and the UI.
