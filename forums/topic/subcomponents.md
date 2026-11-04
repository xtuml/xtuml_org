---
redirect_from:
  - "/community/topic/subcomponents/"

layout: "topic"
title: "subcomponents"
date: "2017-05-11"
permalink: "/forums/topic/subcomponents/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**micke.x** · May 11, 2017 at 3:50 pm

Hi,

is it possible to have a component partitioned into subcomponents?

If so, how do I define the interfaces (ports) of the subcomponents?

Typically, the interfaces of the each subcomponent are subsets of the interfaces of the upper component (i.e. containing only a subset of the signals).

However, it seems like interfaces cannot be specialized or partitioned into subinterfaces…

How is this supposed to work in xtUML?
How do I create a partitioned model like I want in BridgePoint?

I also have a problem wind the send and generate keywords in xtUML, unless I misunderstood something…
To me, they force me to choose between intra- and intercomponent messaging on an early modelling stage when I do not know if the model parts should be partitioned or not.
It limits the usability of the model – I have to make low-level behavior changes when refactoring the architecture.
To me this is a flaw in the language – if it needs to be handled in different ways, this should be sorted out by either code generation or the run-time kernel and not limit/affect the model actions.
Ultimately, when sending a signal, I do not want to have to know if it is sent to a class local in my component, or to a distributed component – it should not concern me how the signal handling outside of my scope is handled/implemented.
If I have a handle, that could be a handle whose uniqueness is guaranteed by the kernel, or by the integration of the components.
If I choose to send via a port, that should work as well – yes, I would have liked to have ports on classes also, as in UML 2…

best regards
Michael

---

**keithbrown** · May 11, 2017 at 4:38 pm

Hi Michael,

Yes, it is possible to nest components. Interfaces and ports are created on nested components exactly the same way that they are created on non-nested components. Interfaces from the containing component may be delegated to an inner component, which sets up automatic forwarding between the inner and outer components. I recommend you take a look at the On-line course “Modeling with xtUML” and check out the Components module to see this in action.

In xtUML, each interface is a complete contract of functionality. If you want to define a smaller subset you simply create a new interface.

“Generate” is used to fire off events to state machines (class to class within the same component). “Send” is used to invoke interface operations and signals (inter-component). Components are black boxes in xtUML. They intentionally hide their internals and force interaction to go through the contractual interfaces.

Finding the right level of abstraction and encapsulation (i.e. subject matter breakdown) is definitely a balancing act at the beginning of a project. This is especially true of large systems with multiple engineers working together. Good luck!

---

**Lee Riemenschneider** · May 11, 2017 at 5:02 pm

I see Keith answered about the mechanics while I was typing this.

I’m going to attempt to answer the “How is this supposed to work in xtUML?” question, but probably not very directly. ;-) (One caveat, I’ve never been very comfortable with components and interfaces; from an analysis perspective, they require more effort without adding benefit.)

xtUML as described in the Mellor and Balcer book doesn’t use components and interfaces. In BridgePoint, components are used to represent domain and interfaces represent bridges to/from the domains. UML doesn’t have domains or bridges as defined by xtUML, so something had to be chosen. Originally it was Packages, but Components seem to be a better fit.

Domains are supposed a black box containing a single subject matter in a system. They should already be at their most decomposed level (from an analysis perspective), so if a component is a domain, then subcomponents don’t make sense. The Mellor and Balcer book does talk about subsystems, but they were only added as a way to partition a large class model for a single domain. Subsystems are a graphical tool concept, and aren’t really part of the xtUML modeling “language”.

---

**micke.x** · May 12, 2017 at 8:35 am

Thank you for the answers.

I am not sure I understand how this is modeled, and how the tool handles the signals/interfaces in practice.

If my top component T is realizing
interface i, containing
signal s1, s2, s3, s4;

And I have two nested subcomponents
Tsub1, realizing
interface i_sub1, containing
signal s1, s2;
and Tsub2, realizing
interface i_sub_2, containing
signal s3, s4;

**How are the signals in the sub-interfaces related to the signals of the top interface?
To me, they are distinct elements/entities – I want them to to be the same elements.**

Or does the tool somehow map signal definitions in different interfaces by name?
Is not interface a scope and a container, defining signals/operations?

The question is really:
“How do I restrict an interface definition so that a sub-component is only allowed to receive a subset of the signals of the interface of the top component?

As I mentioned, what I lack is really to be able to specialize an interface.
Defining a “part-of” association between two interfaces could be an alternative way to model this.

best regards
Michael

---

**micke.x** · May 12, 2017 at 11:07 am

I guess an alternative is to let the top component specify many ports with all the individual sub-interfaces of the sub-components at the lowest leaf level, but it will not be very nice…

Imagine a 7-layer protocol modeled this way – the top component will look like a Christmas tree with hundreds of ports…

/Michael

---

**Lee Riemenschneider** · May 12, 2017 at 3:37 pm

Yes. For components within components, you expose the interfaces through delegation connectors (ports) on the outer component.

This is the second use case for components in BridgePoint, building systems. Components can represent systems or subsystems (note: not xtUML subsystems, as explained in my previous response). The subsystems can either be domains, or have other subsystems nested in them. This use case is purely architectural, so outside of the xtUML modeling domain.

---

**keithbrown** · May 12, 2017 at 5:44 pm

xtUML does not provide a mechanism for modeling Interface hierarchy (a la subtype/supertype class relationships), so you must explicitly define each interface and you could manage the subset of signals by naming convention. You could then model an “impedance matching” component and use port activity OAL to forward the subset appropriately.

I’ve whipped up an example of this (see the screenshot). Please pardon any inaccuracies.
[![](https://s3.amazonaws.com/1f-outgoing/pub/images/interface_subset.png)](https://s3.amazonaws.com/1f-outgoing/pub/images/interface_subset.png)

---

**micke.x** · June 2, 2017 at 9:35 am

Thank you for your detailed answers and example.
I understand what needs to be done.

It would have been nice with a possibility to define this in the structural part of a model (having extended xtUML semantics for this subdelegation), rather than having to specify extra behavior in the model.

The extra behavior will affect the scheduling of the state machines unnecessarily.
Typically there is support for this in most domains / operating systems where a model will be deployed. Anyway, it is not that difficult to implement generic model integration code that implements such an extended xtUML semantics.
