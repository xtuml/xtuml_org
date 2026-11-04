---
redirect_from:
  - "/community/topic/formalizing-an-associative-link-relationship/"

layout: "topic"
title: "Formalizing an Associative Link Relationship"
date: "2015-04-27"
permalink: "/forums/topic/formalizing-an-associative-link-relationship/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dennis Tubbs** · April 27, 2015 at 6:33 pm

Has anyone had trouble formalizing a relationship with an associative class? I am creating R1 between class A and class B with an associative link to class C. I add identifiers to all classes. When I formalize the relationship I get the expected referential identifiers in class C. At this point all is well, but once I exit BridgePoint and restart, one of the referential attributes in class C will be orphaned.

Is there a solution other than creating individual relationships to class C?

---

**Lee Riemenschneider** · April 27, 2015 at 7:15 pm

I haven’t seen this and couldn’t reproduce it just now. Which version of BridgePoint?

I have filed a bug report on dangling (orphaned) referential attributes, but in my case, I ended up with extra attributes. My scenario involved restructuring my class model. [https://support.onefact.net/redmine/issues/4831](https://support.onefact.net/redmine/issues/4831)

---

**Dennis Tubbs** · April 27, 2015 at 8:11 pm

I am using version 4.2 of BridgePoint but unless anyone has any other ideas I suspect my installation must have become corrupted because it is even worse now. If I create a new project, create a package and create two classes with a single relationship between them I can formalize the relationship, but if I restart before formalizing the relationship I do not get that option after the restart, even though both classes still have identifying attributes. No errors when running the integrity check on the model.

It has been a while since I have done any modeling, but I cannot believe this wasn’t working before. I will try re-installing.

---

**Dennis Tubbs** · December 23, 2015 at 3:50 pm

I believe I have discovered what was causing this problem. I use Git, but not through BridgePoint/Eclipse. If a Git repository is detected automatically by the tool then this problem would surface. Simple solution was to move the project lower in the directory structure of the repository.
