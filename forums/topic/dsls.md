---
redirect_from:
  - "/community/topic/dsls/"

layout: "topic"
title: "DSLs"
date: "2014-10-11"
permalink: "/forums/topic/dsls/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Lee Riemenschneider** · October 11, 2014 at 1:30 pm

I just finished watching [Session #5: xtUML and Domain-specific Modeling](https://www.youtube.com/watch?v=Z3hDKAZwdEk)

I’m not all that familiar with DSLs, but the autosampler one in the video struck me as not being abstract enough. In my mind, the user commands would be:
\[code title=”Autosampler DSL example”\]reset;
sample quantity=5 time=60 sequential;
reset\[/code\]

Those commands would then be passed to the model, where the knowledge of:
reset -\> carousel home
sample-\>loop for quantity, needle up/down, time delay, and carousel rotation.

Any thoughts?

- This topic was modified 11 years, 4 months ago by [![](https://secure.gravatar.com/avatar/2beeed50ad01495a2bb8456ccfd23100a3ae303e29fc1a90ee450c7cf5e79641?s=14&amp;d=mm&amp;r=g)Lee Riemenschneider]({{ '/user/lwriemen/' | relative_url }}). Reason: Video not present

---

**Dan George** · December 6, 2014 at 5:43 am

Lee, it depends on who the programmer is. If it is a auto sampler product developer, they might want finer control. Even if it is for an end user, I can imaging a number of use cases where the reset and sample commands are too abstract. The point of a DSL is that the language is very close to the domain expert’s lingo. It would be a good conversation to have with a real life auto sampler domain expert.

I just watched that video tonight. It struck me that xtUML can define the semantics of the language. I’m not a DSL expert but I’ve been looking into it a bit. It seems like DSL methods define abstract syntax but the semantics are concrete. How to represent a certain construct is abstract but the semantics are “hard coded” by what the translator. We could use xtUML to formally specify the relationships, both static and dynamic between the abstract syntax objects..

---

**toni.siljamaki@gmail.com** · January 9, 2015 at 9:00 pm

Ciao guys.

Could you please clarify what constitutes the actual “DSL” in the action-language-like code snippets being referred to above, and in the Session \#5 video, wrt DSL modeling and languages?

Regards/Toni

---

**toni.siljamaki@gmail.com** · January 10, 2015 at 10:49 pm

Hi again.

As I’m currently not updated on the very latest developments of BridgePoint xtUML technology, and wrt the Session \#5 video referred to above on how “DSL’s can be modelled using xtUML”, can you please also clarify how this new DSL is formally defined in BridgePoint xtUML, and then deployed as a new DS languange for a wider user base in a development organization? :)

The Session \#5 video currently looks more like Shlaer-Mellor-style domain specific modeling using a DS vocabolary while discussing the modelled domain, rather than discussing the definition of a new DS language.

Regards/Toni

---

**cort** · January 12, 2015 at 12:14 am

In the case of the Microwave Oven, the discussion is strictly academic.

In the case of the autosampler, the example comes from industry. This device ( [http://www.basinc.com/products/culex/](http://www.basinc.com/products/culex/) ) uses a much more developed version of the demonstrated model. The DSL was defined using xtUML. The device was deployed to the field with the basic services provided by primitives (command) of the DSL. New “methods” (biological and chemical techniques) were deployed (and still are) over the years using the DSL to modify the behavior of the deployed system.

---

**Lee Riemenschneider** · January 12, 2015 at 8:17 pm

Hello Toni,

How does a DSL come to exist? Does it need anything more than a domain analysis?

Wikipedia says “A domain-specific language (DSL) is a computer language specialized to a particular application domain.” [[Wikipedia]](http://en.wikipedia.org/wiki/Domain-specific_language)

[Martin Fowler](http://martinfowler.com/books/dsl.html) says, “DSLs are small languages, focused on a particular aspect of a software system.”, and Stephen Mellor has referred to domains as aspects.

I think the interfaces of an xtUML/Shlaer-Mellor domain and the domain-specific data types are basically a DSL. Again, I don’t have familiarity with using DSLs (per typical definition), but when they first started coming out I thought they looked awfully familiar.

---

**toni.siljamaki@gmail.com** · January 16, 2015 at 11:31 pm

Hello Lee.

Aspects are more cross-cutting concerns like security, memory management, multi-core or cloud, fault-tolerance, traceability etc. more likely to come into play when targeting some specific “platform” at model transformation time, hence a concern to be supported by some target-specific model compilers. (= not part of metalevel M0 domain analysis)

A DSL (or here a DSML) is defined and designed as a widely deployable and specialized modeling language (at M2 metalevel), focusing on supporting modeling of a certain domain (at M1 metalevel), like telecom network architectures, for instance.

You can check out our presentation at EclipseCon Europe to get the idea and big picture of it.
[https://www.eclipsecon.org/europe2014/conference/session-slides](https://www.eclipsecon.org/europe2014/conference/session-slides)

Your proprietary DSL (for instance) is deployed as DSL-plugins in Eclipse for wide use, supporting the UI customizations your DSL need, and your DS language model validation defined in OCL in your DSL.

I disagree with the statement that DSLs are small languages, focusing only on a particular aspect of a system, and that it only has to do with a certain domain of a system.

We must not forget needed UI customizations for your DSML. :)

---

**toni.siljamaki@gmail.com** · January 30, 2015 at 11:07 pm

Hi again Lee.

If you have any additional interest in Open Source DSML development we are presenting at
MODPROD 2015 next week. [http://www.modprod.liu.se](http://www.modprod.liu.se)

It will show how DMSL’s come to exist, and how DS users put requirements leading up to its develpment.
Enjoy. :)
