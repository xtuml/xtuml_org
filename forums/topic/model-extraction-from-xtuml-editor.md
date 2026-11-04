---
redirect_from:
  - "/community/topic/model-extraction-from-xtuml-editor/"

layout: "topic"
title: "Model extraction from xtUML editor?"
date: "2014-04-19"
permalink: "/forums/topic/model-extraction-from-xtuml-editor/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**lunkpeter** · April 19, 2014 at 2:43 pm

Hello,

My name is Peter Lunk and I have a few questions regarding the accessibility of the model being developed in the xtUML editor.

I am working on an Eclipse plug-in that is responsible for transforming different tool-specific state machine models into a unified, tool independent, EMF-based model. I would like to try if this functionality can be extended to xtUML models as well. To achieve this, I need to access and scan the xtUML model, based on which I can build the unified model.

In previous posts, I have read that there is an API that can be used to access the model, however, I could not find any documentation regarding it. I would be grateful if you could point me to the right direction.

Many thanks,
Peter Lunk

---

**cort** · April 22, 2014 at 2:25 pm

Hello Peter,

We have some docs on this that we are digging up and preparing to post. You are not the first to ask for this, so we are also preparing a more complete, technical doc generated from the meta-model. Look for it in the next day or two.

Kind Regards,
Cort

---

**cmccausl** · April 23, 2014 at 2:39 pm

Hi Peter,

I checked in a document for you in
[GitHub](https://github.com/xtuml/editor/blob/master/doc-editor/HOWTO/HOWTO%20Interface%20to%20the%20xtUML%20Editor%20from%20java.md)

It shows you how to interface with the xtUML editor from java code.

Please let us know if this gives you what you need.

best regards,

Campbell

---

**lunkpeter** · April 23, 2014 at 3:36 pm

Hello,

Thank you very much for the quick response, I will look into it.

Regards,

Peter Lunk
