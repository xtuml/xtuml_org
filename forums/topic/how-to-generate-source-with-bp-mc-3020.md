---
redirect_from:
  - "/community/topic/how-to-generate-source-with-bp-mc-3020/"

layout: "topic"
title: "How to generate source with BP MC-3020"
date: "2023-11-09"
permalink: "/forums/topic/how-to-generate-source-with-bp-mc-3020/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Schmill** · November 9, 2023 at 9:15 am

Hi there,
I would like the MC-3020 to generate source files so I can accomplish something similar to what is described here:

> [Include external header file]({{ '/include-external-header-file/' | relative_url }})

When I build my project, only documentation and SQL is generated but no source. perhaps you could refer me to a document that describe how to set up source generation.

Thank you.

---

**cort** · November 9, 2023 at 9:45 am

The easiest way to learn is to look at an example project. In BridgePoint go to Help and then QuickStart. You will see example projects that you can import. Import the Microwave Oven project. It is completely set up to generate and compile C code using MC-3020.

---

**Schmill** · November 9, 2023 at 10:08 am

The microwave example is very useful, but unfortunately my project isn’t configured properly to produce the source. I
The document states that:

“When the sample MicrowaveOven project was created, the following downstream tools were selected:
•MC-3020 as the translationcomponent
•CDT builderas the compiler/linker”

I assume that this is the CDT that produces the source? So my question would be: how can I add it to my project that has only the MC and the docgen?

Thank you.

---

**cort** · November 9, 2023 at 10:19 am

I think you can right click on the project and go to BridgePoint Utilities -\> Add Model Compilers.

---

**Schmill** · November 9, 2023 at 10:43 am

Perfect, Thank you.
