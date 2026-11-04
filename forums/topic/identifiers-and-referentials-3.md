---
redirect_from:
  - "/community/topic/identifiers-and-referentials-3/"

layout: "topic"
title: "Identifiers and Referentials"
date: "2016-10-24"
permalink: "/forums/topic/identifiers-and-referentials-3/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**cort** · October 24, 2016 at 9:49 am

**Identifiers and Referential Attributes (aka IDs and Referentials, Keys and Foreign Keys)**
Class identifiers and referential attributes are useful within class models and modeling from at least three perspectives: Model (the artifact), Modeling (the process), Architecture (the implementation). Separation of concerns is a virtue in domain modeling. Polluting one domain with information used primarily by another domain is discouraged. The role of identifiers and referential attributes differs between the application being modeled, the process of modeling that application and the architecture that implements the application.
**Model (the artifact)**
Models of real-world domains involve abstractions (classes) that have significant populations of more than one instance. Often it is necessary to find or otherwise distinguish these class instances one from another. It is critical that such a class is modeled with attributes and/or associations that enable the unique identification and selection of a desired instance. Such an attribute or attribute set which allows identification of a desired instance is called an identifier. Identifiers can be be universally unique, unique across the complete instance population of the class or be unique within a particular scope (“scoped identifier”). At the modeling level, an identifier need be unique only within the instance population of its use. In other words, an identifier must uniquely identify an instance only within the desired selection scope.
In a model an association can be “formalized” by copying the identifier of a referred-to class into the referring class participating in the association. This can be useful to capture, in data, information that clarifies or disambiguates.
However, the practice of formalizing all associations as a matter of course is discouraged. Formalization of associations with identifiers and referential attributes must be used sparingly when necessary to clarify abstractions. The line drawn between the classes is the association; duplication of this information violates one fact in one place.
**Modeling (the process)**
Building models of an application is a process (an exercise) in and of itself. There are techniques that are applied to this process. The goal is to end up with an excellent model (the artifact) of the subject matter. The process of building the model may involve temporary information that is not ultimately part of the modeled application.
Establishing identifiers (scoped or otherwise) and referential attributes (foreign keys) can be a valuable exercise while building models. Building models involves discovering useful abstractions of conceptual entities within a domain. Thinking about the identifiability of an instance within a class instance population is an important aspect of this process. As such, while modeling, recognizing and adding identifiers is encouraged.
The process of formalizing associations with referential attributes can serve as a way to test associations. However, once the process of successfully testing the association is complete, formalized referential attributes may be discarded. Referential attribute sets must remain in the model only if demanded by the modeled domain for clarification or resolving ambiguities.
**Architecture (the implementation)**
The architecture represents the patterns applied to realize a modeled system. Consistent rules are applied to implement modeling concepts into chosen deployment technologies. One such concept is that of association. The architecture must supply a means for realizing the links between instances. In other words, run-time connections between instances of associated classes must be implemented.
There exist several strategies to realize associations within a modeled instance population. Relational databases have historically employed a keyed approach that insists upon an explicit identifier for each modeled class (table). A related class (table) must carry a foreign key that matches the identifier of the related class. This is an effective, established, well-understood and time-tested approach to relating instance sets. It is one way but not the only way.
Other choices of architecture exist. It is important that architectural choices do not unnecessarily constrain the application. Thus, if an architecture is using an ID/referential approach to realizing association links, the application must be protected from knowledge of this choice. The application cannot be “polluted” with architecture or implementation details.

- This topic was modified 9 years, 3 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}). Reason: added one fact in one place
