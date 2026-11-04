---
redirect_from:
  - "/community/topic/associative-classes-and-referential-attributes/"

layout: "topic"
title: "Associative Classes and Referential Attributes"
date: "2015-11-06"
permalink: "/forums/topic/associative-classes-and-referential-attributes/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · November 6, 2015 at 2:29 am

This topic reared it’s ugly head in discussion of a bug fix between John Wolfe and I. John suggested we continue any further discussion in public, but here’s the thing…”reared it’s ugly head” is a commentary on the history of referential attributes in Shlaer-Mellor/xtUML. Referential attributes have definitely been controversial. The earliest mention of removing them I found is in the [1996 esmug mailing list.]({{ '/assets/uploads/2015/10/esmug_1996.txt' | relative_url }}) The topic keeps coming up throughout the life of the mailing list. Steve Mellor’s post in the 2000 discussion is well worth the read. (Search for “Two points to add to the fray…”) The topic then jumped into the [Yahoo! Executable UML group](https://groups.yahoo.com/neo/groups/executableuml/info) in 2003, and kept cropping up while that group was active.

So…once again into the fray! ;-)

Bug \#578, “GPS Watch: Incorrect conditionality on certain associations”, requested a change to conditional on two relationships that made them conditional on both ends. The recommended place to put the referential attributes in a 0..1:0..1 relationship is in an Associative Class,

so I asked, “should associative classes be added? (Referential attribute recommendation)”

to which John replied, “please help me understand what additional information would be captured by associative classes or how adding referential attributes into the mix would improve the model.”

Lee: “I tend to adopt a strict no NULLs policy when I model, so associative classes whenever there is relational ambiguity.”

John: “I’d like to understand your no-NULLs policy, but we should probably move this conversation to the forum. I lean toward class models with no artificial classes, so I would never add an associative class that does not provide an abstraction of a meaningful concept in the subject matter. I also avoid using referential attributes unless they add value to the model (e.g., when they are part of an identifier).
Associations are a very powerful aspect of the method, and they can be used in a number of ways. Often the absence of a link (a null association) captures quite useful knowledge about the status of the system, so I would never impose a no-NULLs restrictions on my models.”

I think I’ll do a little reading of past conversations, before I submit a reply.

---

**Lee Riemenschneider** · November 6, 2015 at 5:36 pm

After perusing the aforementioned forums, the [miUML discussions](http://www.miuml.org/forum/), and [my own metamodel musings](http://shlaer-mellor-metamodel.blogspot.com/), the only conclusion is that there is no concensus. The xtUML pundentry is split about 50/50 on this topic, so I’ll just have to address John’s question and explain myself.

I have always found a usefulness to addressing referential attributes and their placement when doing analysis of a problem space. I mused in the Yahoo! forum that maturity in modeling might obviate the usefulness of this, but I can’t say I found this to be true. The same goes for contrived identifiers. I can clearly state that I will always put them in my models.

Given the above, I have a real hard time assigning an attribute to a class that is only an attribute *sometimes*. This would be an incomplete model in my mind. I could probably back this up with some words of wisdom from C.J. Date ala. relational, but … This is the crux of my no NULLs rule; it applies only to me, and I’m not proposing otherwise.

Maybe once I finish my metamodel analysis, I’ll have a stronger argument, but for right now, it’s just a preference.

---

**cort** · November 8, 2015 at 7:10 pm

This is going to touch on another aspect I have been thinking about “time” and “role”.

A model is developed in time measure from the first idea through class blitz through adjustments through translation and deployment. Model elements serve different roles. Maybe some model element serve to clarify. And maybe some clarifying model element only serve this role early in the time line described.

So, I wonder if some model element might be used early in the time line and then eliminated when their role has been served as is no longer useful?

---

**Lee Riemenschneider** · November 9, 2015 at 12:58 am

Care to elaborate? \>;-\>

I don’t think there’s any model elements internal to a domain that would be discarded.

Supposing contrived identifiers and referential attributes were the breadcrumbs I needed to get to my model destination. If I let the birds eat them, could I find my way back home, or would I be asking to get put in the oven?
