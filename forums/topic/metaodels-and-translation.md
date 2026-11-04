---
redirect_from:
  - "/community/topic/metaodels-and-translation/"

layout: "topic"
title: "Metaodels and Translation"
date: "2016-01-05"
permalink: "/forums/topic/metaodels-and-translation/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · January 5, 2016 at 3:37 am

This is some data concerning a recent conversation on the xtUML Community chat. The big question is who needs to know what to transform an xtUML model into another language (like C, Java, or even another model). Does the xtUML metamodel need to know about the target language? Does the transformation metamodel need to know the internals of the xtUML metamodel? Neither sounded very palatable to the chat participants.

Some definitions for metamodel:
– From Mellor-Balcer Executable UML: A metamodel is a model of a language expressed using a modeling language. … The instances in the metamodel capture the entire semantics of the application, including … the action language. The structure of a \[Executable UML\] repository is defined by the metamodel.
– From MDA Distilled by Mellor, Scott, Uhl, and Weise: a metamodel is a model of the modeling language. A model-driven approach maintains a separate mapping function that transforms the source model into the target model. A mapping function is a collection of rules or algorithms that defines how a particular mapping works. A mapping is the application or execution of a mapping function in order to transform one model into another.

The latter part seems to contain an answer, but can it be improved?

---

**Lee Riemenschneider** · January 5, 2016 at 12:48 pm

Some thoughts:

What about patterns? In Model Driven Architecture with Executable UML by Raistrick, Francis, Wright, Carter, and Wilkie, they have listed some common modeling patterns. Leon Starr’s Executable UML book on class modeling is another good source for patterns. Recognizing and making patterns available for transformation to a target language opens up huge possibilities for optimization of the output.
– parsing of model to discover patterns
— model could be parsed in a transformed representation
– Are patterns metamodel specific?
– How to make patterns available to target language transformer?

What about marks?
– Some marks could be handled in mapping
– Some marks might be applied to patterns or other more complex designations
