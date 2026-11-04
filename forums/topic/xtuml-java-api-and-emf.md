---
redirect_from:
  - "/community/topic/xtuml-java-api-and-emf/"

layout: "topic"
title: "xtUML Java API and EMF"
date: "2017-01-24"
permalink: "/forums/topic/xtuml-java-api-and-emf/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Anonymous** · January 24, 2017 at 10:40 am

Hi all,

I have seen some plans about an [EMF-based Java API](http://onefact.net/2016/06/27/model-api/) for xtUML model manipulations. I’d like to ask about the status of this API, and if we can access it. Also does this mean that the Java-MC will generate an EMF ecore representation of the compiled xtUML model, or only EMF-compatible Java code will be generated?

Thanks,
Daniel Segesdi

---

**cort** · January 26, 2017 at 4:06 pm

Hello Daniel,

The current Java API has not changed since this post. Progress includes preparations and infrastructure progress simply to get ready for the migration. A study was done together with people from EclipseSource to explore the options of making this move. Each option requires significant work. We have some experiments in mind.

A twist to the approach is presently looking attractive. It is desirable to use EMF only in-memory. The persistence format would human-readable parseable text. An Xtext parser will do the loading and serializing. Significant progress in this regard has occurred with a new action language called MASL. The first structural elements to be persisted as text are the signatures and parameters of the functions and operations.

In both cases, an ecore API would be exposed for the metamodel.

I hope this helps.

Cort
