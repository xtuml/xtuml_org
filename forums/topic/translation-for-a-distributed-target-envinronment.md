---
redirect_from:
  - "/community/topic/translation-for-a-distributed-target-envinronment/"

layout: "topic"
title: "Translation for a Distributed Target Envinronment"
date: "2014-12-12"
permalink: "/forums/topic/translation-for-a-distributed-target-envinronment/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dan George** · December 12, 2014 at 6:53 pm

Using the example project from Mellor-Balcer, if the Publisher instance and BookProduct instances actually run on two different processors, would the following AOL need to be rewritten?

\[code title=””\]**select one** bookPublisher **related by** newBook-\>publisher\[R1\];
\[/code\]

If not, what approaches could be used to translate from that statement to the actual code? There is not explicit bridge reference in the above code.

Thanks,
Dan

---

**Lee Riemenschneider** · December 14, 2014 at 4:27 am

I think the model compiler could handle this, if it had a way to mark classes as distributed (i.e., not directly accessible). There would have to be consideration given to the xtUML timing rules, so some kind of synchronous IPC would need to be available. Any and all interactions with the class would have to use a similar mechanism.

Just out of curiosity, can you come up with a scenario where such an architecture is desired?

---

**Dan George** · December 14, 2014 at 6:12 am

An input processing card detects signal type. An output processing card needs to know incoming signal type to produce the correct output. Between the banks of these two types of cards is a signal router. Functionally, the user wants to route inputs to outputs and expects the outputs to correspond to input signal type automatically. For non-functional reasons, the system consists of three different kinds of cards, each with processing and communication capability.

There are lots of these sorts of cases where different processing units all supply information to each other to get an overall job done.

Lahman has opined that if you have objects in the same domain existing on separate processors, you’ve “screwed up” the domain partitioning. He emphasizes not to forget about the ‘D’ in OOAD. Non-functional requirements, like a distributed processing environment, can affect the models. Still, I think that is a matter of practicality and if we had model compilers with effective marks we’d take advantage of abstracting to this degree.

Of course, if we cannot figure out how to build the compiler, we have to break the problem down and couple the structure of the functional model to architecture.

I’m trying to understand to what degree the model can be architecture independent. To me, the more the model can be independent of non-functional requirements and constraints, the more reusable it will be. Is there something inherent in the method that says you cannot abstract above a distributed architecture?

---

**cort** · December 14, 2014 at 9:58 pm

Dan, the short answer is that such an architecture can be built. The BridgePoint C model compiler actually supports this case selecting instances among \_threads\_. It is a small bit of architectural code generation to support “instances in separate tasks”.

While modeling, it is O.K. to wonder about generated code upon occasion, but do not let it steer your analysis-level decisions.

---

**Dan George** · December 14, 2014 at 11:08 pm

Cort,
that’s good to know and gives me a good pointer for further exploration.

I’m asking precisely because I want to see how decoupled the analysis can be from the target using the BP xtUML tools. The last thing I want is to receive a model from an analyst that, although very clearly and correctly states the functional requirements for the implementation, turns out to require elaboration before it can be translated to the actual target. Deploying into a distributed processing environment seems like a good test case.

Best,
Dan
