---
redirect_from:
  - "/community/topic/document-generation/"

layout: "topic"
title: "Document generation"
date: "2019-11-12"
permalink: "/forums/topic/document-generation/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Clive** · November 12, 2019 at 6:54 am

I was in the process of copying and pasting stuff in a state machine, when I accidentally touched a wrong key to paste an item. The result was the generation of a document laying out everything (diagrams and code). A Docgen Console was created as part of this accidental event. Now I don’t seem to be able to replicate my accidental touch, and I don’t seem to be able to find anything in the BP doco to indicate how I would create such a document. I’ve also looked at the eclipse stuff, but there’s nothing obvious. Any clues?

---

**keithbrown** · November 12, 2019 at 8:10 pm

In older versions of BridgePoint you could right-click on a project, then choose “BridgePoint Utilities \> Create Documentation”.

In newer versions the “Document Generation” is changed to be a first class Builder like any other model compiler. It is managed from the Project Properties \> Builders page. If it is checked then it will run every time you Build the project.
