---
redirect_from:
  - "/community/topic/adding-exceptions/"

layout: "topic"
title: "Adding exceptions"
date: "2016-07-12"
permalink: "/forums/topic/adding-exceptions/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**Levi** · July 12, 2016 at 2:13 pm

I recently undertook the task of adding a new first class model element to the BridgePoint editor — exception. This work was done as part of the effort to fully support the MASL modeling language. In MASL, a domain declares an exception, giving it a visibility and a name. Visible activities can then catch these exceptions and handle them. In BridgePoint, code needed to be added for creating exceptions, CMEs, persistence, graphics reconciliation, tree hierarchy, and a few other small bits. As it turns out, this changeset is a great prototype for what parts of the source need to be touched to add a model element. Take a look at the implementation note here: [https://github.com/xtuml/bridgepoint/blob/testing/doc-bridgepoint/notes/8544_exception_ui_int.md](https://github.com/xtuml/bridgepoint/blob/testing/doc-bridgepoint/notes/8544_exception_ui_int.md)

---

**Bob Mulvey** · July 12, 2016 at 3:05 pm

Would you please post a link to the pull request too so the actual changeset can be easily seen?

---

**Lee Riemenschneider** · July 13, 2016 at 3:55 pm

What’s the difference between an exception and (i.e.,) a bridge call to the LOG domain?

---

**Levi** · July 14, 2016 at 1:41 pm

An exception provides the modeler an avenue to model exceptional behavior in the application itself. For example, a MASL analyst may model a domain Cellphone, a class Antenna, and an exception TowerUnreachable. A class operation acquireTower() on Antenna may raise the TowerUnreachable exception and handle it in a certain way, or let the caller of acquireTower() to handle the exception. Of course, the same behavior can be modelled with “if” statements and calls to the LOG domain, however exceptions add richness and meaning to the language.

Read more about exceptions in the reference manual here (starting on page 93):
[https://github.com/xtuml/bridgepoint/blob/master/src/org.xtuml.bp.doc/Reference/MASL/LanguageReference/legacy/maslrefman.pdf](https://github.com/xtuml/bridgepoint/blob/master/src/org.xtuml.bp.doc/Reference/MASL/LanguageReference/legacy/maslrefman.pdf)

Note that this is the legacy manual, a detailed explanation of exceptions is not available in the current manual.

Here is the pull request associated with this work:
[https://github.com/xtuml/bridgepoint/pull/155](https://github.com/xtuml/bridgepoint/pull/155)

---

**keithbrown** · July 14, 2016 at 5:40 pm

While running the bp.core JUnit tests I also note that the rename tests are generated. This caused a new test to be generated for renaming S_EXP.

This requires that the testRename1 model in the models repository be updated to include an exception for the test case to use.

---

**Lee Riemenschneider** · July 15, 2016 at 11:41 am

The documentation refers to exceptions as a software architectural concept for use in (e.g.) checking array bounds. i.e., unexpected exceptions. The present way to handle such things in the MC-3020 is through marking, which is part of the architecture domain. Introducing architecture domain concepts into the action language is domain pollution.

Your example shows expected result handling for an event, which isn’t domain pollution, but as present mechanisms exist for handling expected failures, adding another adds complexity (richness and meaning???) to the action language. (I’m very glad OAL doesn’t already have the switch-case vs. if-else complexity.)

So…are the exceptions a replacement to current SW architecture mechanisms, or an addition to the OAL?
