---
redirect_from:
  - "/community/topic/how-important-is-referential-formalization-choice/"

layout: "topic"
title: "How important is referential formalization choice?"
date: "2019-09-30"
permalink: "/forums/topic/how-important-is-referential-formalization-choice/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · September 30, 2019 at 12:46 pm

Was wondering about how important the ability to formalize referentials on (e.g.) identifier 1 vs identifier 2 was to the analyst
. This isn’t associated with OOA ’20, just a question for my metamodel work.
The easy case is to always formalize on identifier 1. The second easiest case would be to formalize on all identifiers. I’m thinking that the formalization is a graphical editor nicety for communication purposes, but wondering how the interplay between the model editor domain and the metamodel domain would work.
Any thoughts?

---

**Sean Kavanagh** · October 1, 2019 at 9:56 am

Surely you can only switch formalisation from Id 1 to Id 2 in very simply cases. I prefer to create natural domain specific single or multiple attribute identifiers when ever I can rather than arbitrary single attribute identifiers.

---

**Lee Riemenschneider** · October 1, 2019 at 2:02 pm

I guess I should clarify. When I say “identifier”, I mean the unique identifier for an instance whether it is composed of one or many attributes.
Referentials in BridgePoint are created upon explicit formalization of the relationship in the model editor. The formalize command asks you to choose the identifier (per the terminology I stated above) to use, which then determines which attributes to show as referential attributes.

---

**Lee Riemenschneider** · October 3, 2019 at 12:03 pm

At least looking at this closer made me realize I hadn’t constrained referential attributes to identifiers. (Doh!)

I do have the relationship between non-composition relationships and referential attributes as unconditional on both ends as ‘is formalized by’ M:1 ‘formalizes’, so the metamodel is formalizing all identifiers. I think this is correct. It should be the choice of the model editor to filter the referentials displayed for presentation to the user (via analyst direction).
