---
layout: "article"
title: "Textual xtUML"
date: "2021-12-28"
permalink: "/textual-xtuml/"
tags:
  - "Announcements"
author: "cort"
---

Dear Modelers,

Significant progress has been made on a specifications of textual xtUML and separately of graphics.  This note concerns the specification of textual semantic xtUML.  This spec will serve a few purposes.

1.  It specifies a full notation of structural Shlaer-Mellor textually.
2.  It specifies how models will be persisted under BridgePoint (supplanting the OOA of OOA instance strategy currently employed).
3.  It defines a textual exchange mechanism.
4.  It loosens the coupling between the Method and tooling opening many options for editors, interpreters and translators.  (Human readable semantic text is much more accessible than a collection of OOA of OOA instances.)
5.  It opens dialogue for the addition/deletion of Method and tooling features and potential convergences.

If you like, please review the linked specification.  Syntax and style feedback are fine, but we are really looking for “big picture” issues.  Here are a few substantive topics to think about while reviewing.

- containment
- element identification (fully qualified “paths”)
- scoping and visibility
- type system
- state machine semantics (initial state, terminal state, creation event)
- inclusion (package references)
- exclusion of non-executable elements (use cases, etc)
- action language agnosticism (or multi-theism ;)

What this specification implies:

- diff/merge becomes much more tractable
- Models can be edited outside of BridgePoint (and then sync’d).
- Models can be edited simultaneously with a graphical editor and a textual editor (updating in both directions).
- A variety of editors, interpreters and model compilers can choose to operate upon text rather than OOA of OOA instances.
- Differing diagram editor/renders can be connected (e.g. Flatland) to these semantics.
- Semantics can optionally be reasoned about in unambiguous text rather than (together with) diagrammatic content.

[https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/notes/12330_textual_xtuml/12330_textual_xtuml.adoc](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/notes/12330_textual_xtuml/12330_textual_xtuml.adoc)

The single file example model in this folder is instructive.  It is a textual representation of the GPS Watch.

[https://github.com/xtuml/bridgepoint/tree/master/doc-bridgepoint/notes/12330_textual_xtuml/example](https://github.com/xtuml/bridgepoint/tree/master/doc-bridgepoint/notes/12330_textual_xtuml/example)

There are no dates or deadlines.  The spec is prerequisite to any development.

Kudos to those who have done the heavy lifting and 1F for sponsoring the effort.  And credit is due to the original authors of MASL; we are standing on their shoulders.

Cheers!
