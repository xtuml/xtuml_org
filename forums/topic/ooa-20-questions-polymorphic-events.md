---
redirect_from:
  - "/community/topic/ooa-20-questions-polymorphic-events/"

layout: "topic"
title: "OOA '20 Questions: Polymorphic Events"
date: "2019-09-26"
permalink: "/forums/topic/ooa-20-questions-polymorphic-events/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · September 26, 2019 at 3:13 pm

# Method: Polymorphic Events

Should Polymorphic events be “concrete”
visiting each level of the hierarchy? (K-C)

Should Polymorphic events be “abstract”
consumed at exactly one level of the
hierarchy? (PT)

Should the above be consistent with
sub/super (deferred) class operations?

How shall the Method define a coexistence of
concrete and abstract polymorphic events?

---

**Sean Kavanagh** · September 26, 2019 at 3:50 pm

A long time ago, I created a blog post on this topic that might be worth a read:
[http://ooatool.blogspot.com/search/label/state%20model](http://ooatool.blogspot.com/search/label/state%20model)

---

**Lee Riemenschneider** · September 27, 2019 at 6:55 pm

As many of you have seen before, I don’t believe polymorphic events are real in Shlaer-Mellor. I think the only reason they came into existence is because the process models (action languages) allow selection of supertype instances. Supertype instances don’t really exist in Shlaer-Mellor. All instances of objects are members of a subset, which is drawn as a class (improper subsets) or a supertype-subtype hierarchy (proper subset).
As I wrote [here](https://shlaer-mellor-metamodel.blogspot.com/2012/01/some-ideas.html), “I think the mistaken view of super/subtyping as a relationship is what causes such invalid concepts like polymorphism and having to formalize a super/subtype relationship to enter the Shlaer-Mellor model space.”
In BridgePoint OAL, all events are directed at instances, but selection of an instance can often involve navigating the supertype relationship to see if a subtype exists. This becomes very tedious, so polymorphic events sound like a good idea. As Sean describes above, ASL (and MASL) direct events at objects/classes. This means every member of the set has to handled the event. (The hierarchy priority Sean described sounds like further super/subtype relationship dementia.)
H.S. Lahman and I had a lengthy discussion about broadcast vs targeted events in the now-gone Yahoo! Executable UML group. I don’t remember if Lahman was advocating an object-level broadcast or a domain-wide broadcast (which would require every event label in a domain to be unique), but I think we agreed that every object instance could decide if it needed to handle the event. If you were to support object-broadcast events, you would also remove the need for polymorphic events as every event would be defined at the object level, and available to all subtype state model segments (a term to use if you consider spliced state model to be a good thing (I do!)).
