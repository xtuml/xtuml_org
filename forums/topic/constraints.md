---
redirect_from:
  - "/community/topic/constraints/"

layout: "topic"
title: "Constraints?"
date: "2014-12-06"
permalink: "/forums/topic/constraints/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dan George** · December 6, 2014 at 5:12 am

The Executable UML book describes how to use constraints but I’ve not seen anything indicating support for constraints in BridgePoint. Am I just missing it?

---

**cort** · December 9, 2014 at 4:29 pm

Dan, please provide a page number so we can be sure what you are talking about.
Thanks,
Cort

---

**Dan George** · December 9, 2014 at 5:48 pm

Pages 141-146.

Examples are provided in both OCL and action language. I suppose the implication is that constraints can be stated in-line in the state procedures.

However, the class diagrams depict key word type constraints such as \[code title=””\]R5{equal, R1, R6}\[/code\] (Figure 8.21 on page 146) and then the meaning of *equal* is defined in both OCL and action language. Another implication is that placing the constraint in the class model and the compiler will apply it it. No need to express it anywhere else.

---

**Lee Riemenschneider** · December 10, 2014 at 3:51 am

Chapter 8 covers constraints.
\[8.1\] Instance constraints are covered in BridgePoint by attribute\<RMB(Right Mouse Button(if right handed))\>Add to Identifier… (NOTE: IDs are always unique, but I’m not sure where this is enforced. (model compiler callout?))

\[8.2\] Derived attributes are created by attribute\<RMB\>Set as Derived Attribute…
Action language is used for the derivation. I don’t think OCL is supported.

\[8.3\] Referential constraints are covered by association\<RMB\>Formalize
\[8.3.2\] Is covered same as \[8.1\] and \[8.2\]

\[8.4\] Association loops used to be doable in BridgePoint, but I can’t find the method anymore. The Rnum would show up as R5=R1+R6 (IIRC).

There also used to be support for adding ranges to attributes, but I don’t know if that is still available.

---

**Dan George** · December 14, 2014 at 6:22 am

Ah, I was in the typing mindset and needed to be in the RMB mindset. Thanks!

Should I assume that the only constraints needed for xtUML are the ones Lee listed from the book? For example, OCL enables expression of all kinds of constraints. Is the limit on constraint expression similar to the limit on UML? Only a small subset is really needed for the methodology?

---

**toni.siljamaki@gmail.com** · January 9, 2015 at 11:04 pm

Ciao guys.

Not updated on the latest developments of Executable UML (wrt p141-146 in the book, referred to above), and the very latest capabilities in xtUML, but very interested in learning how OCL-defined restrictions comes into play in the current xtUML DSL modeling language definition (= metamodel) in BridgePoint xtUML tooling.

Regards/Toni

---

**toni.siljamaki@gmail.com** · January 17, 2015 at 10:28 pm

Ciao xtUML.org
Please respond.

As we have not been using BP xtUML for some time, I like to understand how OCL is used to define xtUML language constraints in todays version of the BP xtUML.

See also the duscussion under:
[dsls]({{ '/forums/topic/dsls/' | relative_url }})

Regards/Toni
