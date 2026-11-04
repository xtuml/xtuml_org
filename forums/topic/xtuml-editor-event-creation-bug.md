---
redirect_from:
  - "/community/topic/xtuml-editor-event-creation-bug/"

layout: "topic"
title: "xtUML Editor Event Creation Bug"
date: "2013-11-04"
permalink: "/forums/topic/xtuml-editor-event-creation-bug/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dennis Tubbs** · November 4, 2013 at 8:31 pm

I noticed the following behavior with the context menu in the Model Explorer when creating an event. To replicate, expand an Instance State Machine in the Model Explorer, the next line will be indented with text “Instance State Machine: Instance State Machine”. Right clicking on either of these lines and selecting the new option will bring up the same context menu. Selecting ‘Event’ from the two context menus has different behavior.

From the first lines context menu an event is created as would be expected, but from the “Instance State Machine: Instance State Machine” line the event is created in whatever state machine is currently displayed in the Graphical Editor window, even if it is the state machine from another component.

This is probably only of interest if you need to create a polymorphic event while editing a sub-type state machine.

Dennis

---

**keithbrown** · November 6, 2013 at 1:57 pm

Hi Dennis,

Thank you for pointing out the problem and the workaround. I imagine you have noticed that some elements have an identically named sub-entry, while others do not. The ones that do correspond to actual files in the file system. The sub-entry is there to allow users to perform config management operations at this file level. While they should behave in the same manner, I recommend getting in the habit of using the context menu entries on the parent item and not the sub-entry item.

I also generally recommend that CM operations be performed from the project level. This will guarantee that any model changes that affect multiple files “stay together” so you don’t have data in the CM repository that isn’t all squared up.

Regards,
Keith
