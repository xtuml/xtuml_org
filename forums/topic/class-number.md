---
redirect_from:
  - "/community/topic/class-number/"

layout: "topic"
title: "Class number"
date: "2017-03-02"
permalink: "/forums/topic/class-number/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**micke.x** · March 2, 2017 at 3:57 pm

Classes in xtUML has an optional (?) property of a “class number”.
At least, this is described as optional in the Executable UML book.

Is it really optional in BridgePoint?
Can you remove the property?
Or turn the autonumbering assignment off?
Or turn off the checking of this property?

Although such a property may be useful, I have have a hard time realizing the benefit of a mandatory property.

My problem is that, by design, it ruins parallel team work, for a very simple and trivial change.
Independently added classes to the same scope in parallel branches will always create a merge conflict because of this, unnecessarily.

---

**Lee Riemenschneider** · March 2, 2017 at 4:34 pm

It sounds like your team is independently creating the same class model. I think this is a mistake, but even if you could turn off the class number, you would encounter the same merging problem for the class identifier (not visible on diagram).

From a pure xtUML standpoint, all you should need to guarantee uniqueness of a class is the class name and the domain name (as a referential attribute). BridgePoint doesn’t currently take this approach. (You can load the ooaofooa from the Welcome page.) Identifiers of model elements in BridgePoint are currently undergoing some revision, but I don’t know what the final form or timeline will be.

You could file this as an issue. I think it is valid. The class numbering is a vestigial element that probably no one would miss.

---

**Dennis Tubbs** · March 14, 2017 at 3:18 am

I for one would miss the class number. I am using it as part of a unique identifier in a home rolled structured text model compiler. I am not going to go into all the details, but the resulting structured text will be, and must be, readable by many people besides the modeler. The class number helps tie the code back to the model.

---

**Lee Riemenschneider** · March 16, 2017 at 7:51 pm

Thanks for the input, Dennis! It’s always better to hear that somebody is using an attribute before its removed. :-)

Looking at the OOAofOOA, I see that only Obj_ID is marked as an identifier, and I know BridgePoint will complain about duplicate Key_Lett values.
\* Name should be I2
\* SS_ID appears to be unused now, but SS_ID and Numb should be I3.

I know numbering used to be tied to the Subsystem. It looks like Package is now responsible for numbering, so all the classes hanging on to SS_ID should probably be related to Package and SS_ID should be replaced with a reference to Package_ID.

IAC, adding an option to turn off class autonumbering should be possible.

---

**micke.x** · March 20, 2017 at 12:10 pm

Well, my scenario is not actual team work, it is just my personal experiments with the capabilities of the existing compare and merge facilities in the tool.

The independently added classes mentioned are not intended to have any direct relation to eachother, they are added in two different parallel feature branches as part of the needed extensions for each feature.
Naming is not a problem/issue – any added classes in this scenario will clash beacuse of the implicit class numbering.
Another possibility (apart from removing class numbering completely) is either to relax its semantics (checking) or to offer recalculation of the numbering after certain model changes, such as merge.

I guess code generators could always tie to either name resolution by scope or context or tie to the guid, instead of a volatile numbering principle.

I also noticed that it is difficult to explore some common refactoring changes of the model, since the tool does not seem to support moving of model elements. This is problematic from a change perspective, since the model change of “Move” then needs to be represented with two changes (“delete” + “create”) instead of one (“move”). This means that there will in these scenarios always be two merge decisons, that are difficult to relate two each other, instead of only one merge decision.
Many pairs of merge decisions like this, that the user must be able to keep track of manually, without any model-based support, of course increases the risk for mistakes, making merge unnecessarily complex and fragile to human mistakes.

---

**keithbrown** · March 20, 2017 at 1:19 pm

Model element move support was added to BridgePoint in v5.8. It is available in the nightly build download if you want to try it out.

The user interface action is via Cut/Paste, but the tool now treats this as a single internal action (that is, “move”).

You can enter a bug report/feature request at [http://support.onefact.net](http://support.onefact.net) for class numbering changes.

---

**keithbrown** · March 20, 2017 at 1:20 pm

Model element move support was added to BridgePoint in v5.8. It is available in the nightly build download if you want to try it out.

The user interface action is via Cut/Paste, but the tool now treats this as a single internal action (that is, “move”).

You can enter a bug report/feature request at [http://support.onefact.net](http://support.onefact.net) for class numbering changes.

---

**micke.x** · March 22, 2017 at 10:20 am

Lovely!
I definitely want to try out what refactoring changes that now are possible to do in a model-based fashion..
So the guids are preserved in this “smart” cut/paste operation?

Thanks for the tip!

---

**keithbrown** · March 22, 2017 at 12:22 pm

Yes, the IDs of elements are preserved during the new move (cut/paste).

---

**micke.x** · March 22, 2017 at 3:02 pm

What are the limitations of model element move?
From a refactoring point of view, It seems to work for packages and classes,
but not for state machines, attributes, operations, states or events.
At least the cut operation does not seem available for these model elements…

---

**micke.x** · June 28, 2017 at 2:41 pm

The inconistency in merged models does not only happen for classes, it exists also for all other auto-numbered properties:
• Class Number
• Association Number
• State Number
• Event Number
It also affects the property “State Machine Event Derived Label”, since this is partly defined by the property “Event Number”, as well as the “Association Name”, since this is based on the Association Number.

The result after Merge is a model with a lot of problem reports such as:
“Found another state under the same state machine with the same state number. InstanceStateMachine.xtuml /MicrowaveOven/models/MicrowaveOven/components/MicrowaveOven/Microwave Oven/Door/InstanceStateMachine MicrowaveOven::components::MicrowaveOven::Microwave Oven::Door::Instance State Machine::new state Problem”

These properties are clearly not designed with parallel development in mind.

If it was up to me, I would have removed all these autonumbered/named properties altogether and changed the action syntax for referring to some of these, such as referring to event name only rather than event derived label – it is a fragile language construct.
I realize that this is not likely to happen…

A more reasonable approach is: the Merge feature (BridgePoint code) has to consider this and renumber clashing numbered properties while Merging, to avoid the inconsistencies and have a smoother Merge.

---

**keithbrown** · June 29, 2017 at 12:19 pm

That is an interesting suggestion. I suggest you raise it as a feature request at [http://support.onefact.net](http://support.onefact.net)
