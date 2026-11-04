---
redirect_from:
  - "/community/topic/state-machine-limitations/"

layout: "topic"
title: "State machine limitations"
date: "2013-10-07"
permalink: "/forums/topic/state-machine-limitations/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**andersivner** · October 7, 2013 at 8:01 am

Hi!

I cannot find exit actions on states, and it does not seem to be possible to do nested states. Is this a deliberate limitation in xtUML state machines, and if so why?

Thanks,

/Anders

---

**Lee Riemenschneider** · October 11, 2013 at 11:49 am

This topic comes up every time a new Executable UML forum pops up. :-)

If you look in the help documentation, the metamodel state machine description shows support for both Moore (action on entry) and Mealy (action on transition) support, but as far as I know, the xtUML Editor only supports Moore state machines. It should be noted that Moore and Mealy are 100% convertible to each other.

Harel (nested states) isn’t recommended. Here’s a quote from Marc Balcer, “Executable UML does not employ the full Harel statechart formalism, complete with substates and state history, precisely because such things, in practice, tend to hide abstractions. Modeling is supposed to expose abstractions.”, from the [Yahoo! Executable UML group](http://groups.yahoo.com/neo/groups/executableuml/conversations/messages/474)

H.S. Lahman also expressed this view, “Complex state machines usually indicate poor object cohesion (too many responsibilities). \[I regard even thinking about using Harel as a similar symptom. B-)\]” [here](http://groups.yahoo.com/neo/groups/executableuml/conversations/messages/686).

To sum up the Mellor and Lahman comments, nested states hide the abstracted dynamics of the model, and are only desired, if you’ve improperly abstracted the class model. Exposing more rules of the system in your class models greatly reduces the complexity in the dynamics (states and actions). The most convincing argument is redrawing your Harel state model as a Moore or Mealy state model. ;-)

---

**poj** · October 15, 2013 at 5:27 pm

The xtUML Editor supports both actions on entry and actions on transition, but actions on transitions are much less visible, and therefore harder to understand when looking at a state machine. Double-clicking on a transition opens an action editor for the transition action.

---

**cort** · November 4, 2013 at 3:00 pm

[@poj]({{ '/user/poj/' | relative_url }}), there is a very slight visible “…” on the transitions that contain action language.

@andersivener, to support [@lwriemen]({{ '/user/lwriemen/' | relative_url }}) do a net search on “Deterministic versus Non-Deterministic Finite State Automata” especially regarding testing.

The door is not closed on adding richness to xtUML state machines, but any such richness would need to be configurable, so that users could disable it to maintain the deterministic testability.

Cort

---

**Domonkos Asztalos** · January 7, 2014 at 2:14 pm

@Lee can you provide a particular elaborated example reference for “The most convincing argument is redrawing your Harel state model as a Moore or Mealy state model. ;-)” ?

Domi

---

**Lee Riemenschneider** · March 1, 2014 at 1:46 am

@Domonkos Most of the nested state machines I’ve seen are based on a complex functional breakdown. Redrawing the nesting on a single-level state diagram ends up looking like spaghetti and meatballs. You usually don’t have to redraw much to make the point that you have a very complex mess. I haven’t ever seen an example put online.

In Executable UML, we manage complexity in the class model, so the complexity doesn’t get pushed down into the state machines and action language (process models). This exposes dependencies and constraints much better.
