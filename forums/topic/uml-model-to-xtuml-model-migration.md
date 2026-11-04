---
redirect_from:
  - "/community/topic/uml-model-to-xtuml-model-migration/"

layout: "topic"
title: "UML Model to xtUML Model Migration"
date: "2025-06-10"
permalink: "/forums/topic/uml-model-to-xtuml-model-migration/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**mugesh** · June 10, 2025 at 1:24 am

I have an existing UML model created in MagicDraw and I want to migrate it to BridgePoint for further development, as manually replicating all the UML diagrams and model elements in BridgePoint is not feasible. I understand that BridgePoint doesn’t seem to support importing XMI files directly.

Are there any existing integrations or tools that facilitate the migration of UML models from MagicDraw to BridgePoint? Or is there any recommended workaround for this issue?

---

**cort** · June 10, 2025 at 9:18 am

The XMI import/export capability was deprecated some time ago.

There is a newer textual representation of xtUML called ‘Textual xtUML’. The specification and examples can be found here: [https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/notes/12330_textual_xtuml/12330_textual_xtuml.adoc](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/notes/12330_textual_xtuml/12330_textual_xtuml.adoc)

Here is a youtube video discussion of Textual xtUML: [https://youtu.be/MxJMVdFjtzE](https://youtu.be/MxJMVdFjtzE)

If you can get the model semantics of you MagicDraw model converted into Textual xtUML, then you can import those semantics. BridgePoint then has the capability to render graphics automatically. Understand that you will lose your spacing and layout. There is no known way to preserve diagram layout.

Best wishes!

Cortland Starrett
