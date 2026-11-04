---
redirect_from:
  - "/community/topic/why-arent-interfaces-tied-to-components/"

layout: "topic"
title: "Why Aren't Interfaces Tied To Components?"
date: "2013-08-30"
permalink: "/forums/topic/why-arent-interfaces-tied-to-components/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Lee Riemenschneider** · August 30, 2013 at 1:01 pm

As I’ve been working more with the “component representing domain” direction, I’ve noticed that bridges via interfaces appear to be very loosely linked to the component domain. For example, look at the HeartRateMonitor component in the GPS Watch example model. The HeartRateMonitor domain is “reused” via the Library package, but the interfaces to the domain are specified outside of the HeartRateMonitor domain (and even the Library) via the HeartRateMonitorInterfaces package. Are they really considered separable? As a lark, you can add a provided interface onto the HeartRateMonitor component and formalize it to the Location interfaces. Why is this allowed? Is there any reason for this separation?

My other problem with this separation comes from where the action language within the bridge occurs. It is now limited to the system integration of components. If an analyst wanted to add a procedural model to a bridge, it is now not possible. This includes domain functions. One would have to contrive a system around the domain to even allow a reuse scenario that doesn’t involve making a package of functions, that would then have to be called from the interface, most likely of the same name. Am I missing something, or is this a real issue?

---

**Lee Riemenschneider** · August 30, 2013 at 2:53 pm

Looks like I misspoke about where the action language within the bridge occurs. I’m looking at too many things at once. The action language is tied to the interface at the component, once it is formalized to the external package interface. This is still a separation of interface (bridge) definition from component (domain) definition, and the procedural model is still more dynamic than it should be.

---

**Lee Riemenschneider** · September 3, 2013 at 7:00 pm

External Entities look like they are a related topic, mainly due to connecting their interfaces. Right now the provided EEs (Time, Logging and Architecture) are all included via a External Entities package and using the External Entity element. This is a disconnect from the component direction and introduces some ambiguity on how best to construct the EEs around your domain model. I think BridgePoint needs to go “all in” on the concept of components and make the EEs into components. I think this will be greatly enhanced by being able to internalize the domain interfaces into the component.

---

**cort** · September 5, 2013 at 2:31 pm

Hi Lee (and others),

Packages are missing in your discussion of “visibility” and “separateness” of components and interfaces. Packages are used to manage and associate the visibility of these elements.

If an analyst wishes to closely tie an interface to a component (or pair of components), the interface can be defined in a package (the same package) together with its “closely related” components.

However, if an analyst is modeling with a more generally reusable interface, the interface can be declared “at a higher level of visibility” in the package hierarchy.

I have seen both arrangement correctly modeled. Sometimes the interface is truly “private” between 2 specific components. But in other cases (like debugging/instrumentation), an interface is highly reusable between multiple pairs of components in a system.

---

**cort** · September 5, 2013 at 2:37 pm

Now, regarding EEs…

It is noted and agreed that there is some overlap between the concept of External Entity (EE) and component.

The syntactic difference lies in the fact that you must explicitly connect components across interfaces. With EEs, you simply “call them” (invoke their bridges).

Semantically, I could recommend that EEs be used as “common library elements” while components/interfaces contain (and restrict) the application communication.

The example of a math library (a MATH EE with bridges sqrt, sin, cos, etc.) serves to illustrate. It would be a bit “heavy” to ask modelers to explicitly show all connections to such a generally and widely used module.

Like other elements, EEs can be managed in packages. EEs can exist outside of components and be referred to from inside of components (“shared EEs”). EEs can also be private to the internal model elements of a component.

I hope this helps illustrate some of the thinking.

- This reply was modified 12 years, 5 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).

---

**Lee Riemenschneider** · September 6, 2013 at 2:56 am

I don’t understand why a port interface on a component can’t be formalized to an interface defined within the component. Domain functions should be tightly coupled to the domain.

If the same component port interface was reused as a EE, like the Time EE, then you’d want to be able to formalize the port to some test interface (which could also be managed with the component). This is where I see the linkage between these concepts.

From the analyst perspective, reusing an interface might introduce domain pollution, as you are addressing the services from the other domain’s perspective rather than your own domain’s perspective.

In the system build case, the bridge calls and the domain function might not align, and you’d need an interface with external functionality to map between the two component ports. I haven’t looked at this case too closely from the new component view. I guess I need to run through some more use cases.

---

**Lee Riemenschneider** · September 6, 2013 at 11:55 am

Things have gone from disconnected to horrifying. I was playing with the GPS Watch example model some more, looking at EE and interface usage.

First let me list my assumptions: (Many based on the out-of-date “System Modeling with Components” document)
1. Components have replaced the former graphical representation of domains.
2. Interfaces have replaced bridges/domain functions. (Revisiting said document shows that domain functions are no longer considered the external interface.)
3. EEs are deprecated. (which per this discussion no longer seems true)
4. A component diagram is used to show the domain chart.

I didn’t expect any of this to affect the way one models a domain. The horror came when I opened the state model for the Display class in the Tracking domain(?). I noticed that there were two different event designators, Display_A(n) and UI. The UI designator referred to the UI domain(?), and I thought it unpleasant that formalizing the interface signal to an event would change the event in the model. From looking at the tree for Display, it looked like there was a local version of the same event, which there *MUST* be or the domain model couldn’t be complete and stand-alone. What was really horrifying is when I unformalized the interface; the event disappeared from the Display tree and the state model reverted to no event assigned.

This is bad behavior, but not surprising, given that the xtUML_Metamodel is looking like spaghetti these days. I think some thought needs to be given to what is method (metamodel domain), what is graphical representation (not metamodel domain), and what needs to use them (tool application domain(s)).

- This reply was modified 12 years, 5 months ago by [![](https://secure.gravatar.com/avatar/2beeed50ad01495a2bb8456ccfd23100a3ae303e29fc1a90ee450c7cf5e79641?s=14&amp;d=mm&amp;r=g)Lee Riemenschneider]({{ '/user/lwriemen/' | relative_url }}).
