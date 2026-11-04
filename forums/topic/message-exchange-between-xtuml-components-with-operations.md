---
redirect_from:
  - "/community/topic/message-exchange-between-xtuml-components-with-operations/"

layout: "topic"
title: "Message Exchange Between Xtuml Components with Operations"
date: "2017-07-18"
permalink: "/forums/topic/message-exchange-between-xtuml-components-with-operations/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Rob** · July 18, 2017 at 1:08 am

I am missing something. When I am implementing an operation (with a return type) defined by an interface between 2 components I am unable to get at any of the instances within the component. I make the operation call from the Provided Interface side. When I use the “select any x from instances of X” to get a handle for an instance I know I have created or the Required Interface side it returns empty.

The implemented code for the interface operation is implemented in the assign component reference with the required interface with the message direction “From the Provider”. Any ideas of what I should consider or an example I can refer to?

Thanks,
Rob

---

**cort** · July 18, 2017 at 1:21 am

Here is OAL from the inbound signal on the GPS Watch example (which you can get from the Help-\>Welcome-\>Quick Start-\>Example Application – GPS Watch.

// If necessary, create a workout session and everything required to
// support it. Then, forward this signal to the workout timer.

WorkoutSession::create();

// Forward this signal, as an event, to the singleton instance of WorkoutTimer.
select any workoutTimer from instances of WorkoutTimer;
generate WorkoutTimer1:startStopPressed() to workoutTimer;

To get to this signal body, I navigated GPS Watch -\> Library -\> Tracking -\> UI -\> UI -\> StartStopPressed.

Here is action language from an interface operation body:

// If necessary, create a workout session and everything required to
// support it. Then, forward this signal to the workout timer.

WorkoutSession::create();

// Forward this signal, as an event, to the singleton instance of WorkoutTimer.
select any workoutTimer from instances of WorkoutTimer;
generate WorkoutTimer1:startStopPressed() to workoutTimer;

To navigate to this I went: GPS Watch -\> Library -\> Location -\> LOC -\> GetLocation

Note that you can set breakpoints and see your instance population in the “Session Explorer” view of xtUML Debugging.

---

**Rob** · July 19, 2017 at 2:45 am

Ok thank you. Another question is why when the verifier is launched do classes within the component package show up twice (replicated) in the “Session Explorer” tab? Under one of the classes seems to capture all the instances of the class and the other there are no instances.

I think this is the part I am confused by.

---

**keithbrown** · July 19, 2017 at 1:38 pm

Using GPS Watch as an example, you will see duplication of the classes if the launch configuration has both the “Library” and “System” packages selected. If you inspect the GPS Watch launch configuration that is included you’ll notice that we only have the “System” package checked. BridgePoint uses the component references and exposes their internals in the session explorer. We don’t actually want to have the Library package checked during the launch.
