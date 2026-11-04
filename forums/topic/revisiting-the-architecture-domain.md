---
redirect_from:
  - "/community/topic/revisiting-the-architecture-domain/"

layout: "topic"
title: "Revisiting the Architecture Domain"
date: "2016-05-18"
permalink: "/forums/topic/revisiting-the-architecture-domain/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · May 18, 2016 at 12:29 pm

The Architecture domain used to be drawn in all of the Shlaer-Mellor literature as a conduit between the application and service domains and the underlying platform technologies (e.g., OS and 3GL). It was the black box in which all the translation magic occurred, which was a fair representation in the days of proprietary Shlaer-Mellor/xtUML tools.
Now with the dawning of open source Shlaer-Mellor/xtUML tools, the Architecture domain becomes a misrepresentation. The idea that a single domain can cover the concerns of model generation, marking, model compilation, user-facing model representation, the metamodel rules, and a myriad of other tool-related issues, isn’t very palatable to those familiar with xtUML modeling, but for communication, the Architecture domain is a reasonable facade.
Consider that in the usage of an xtUML modeling tool for application or service domain modeling, using the Architecture domain as a conduit is more informative to audience than listing every domain that composes the tool’s construction, so it’s utility only exists for expressing an overview of the xtUML technology.
