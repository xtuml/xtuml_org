---
redirect_from:
  - "/community/topic/how-to-import-the-book-store-models/"

layout: "topic"
title: "How to import the book store models"
date: "2023-07-14"
permalink: "/forums/topic/how-to-import-the-book-store-models/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Schmill** · July 14, 2023 at 6:23 am

I’m referring to the models provided by the executableumlbook.com
The instructions provided in the pdf appears outdated and I don’t understand how to import these .bak files.

Thank you.

---

**cort** · July 14, 2023 at 9:03 am

Hello Schmill,

I am glad to know you are reading Executable UML.

The .bak files referenced on the web site are so old that they are not supported for import into BridgePoint. It is theoretically possible, but you would need to have several versions of BridgePoint from the various years since 2002. You would import them into BP 5.1 2002. Then you would upgrade them into intervening year versions of BridgePoint. The current (open source) version of BridgePoint cannot understand the .bak format from so long ago. :(

Cheers,
Cort

---

**Schmill** · July 14, 2023 at 9:43 am

Thank you for the explanation. this is unfortunate, a really nice book.

Are there any alternative models in the test repository that cover a complex system? I could be missing something, but the Microwave seems very limited for the lack of interactions and is limited to a single domain.

---

**cort** · July 14, 2023 at 11:32 am

Yes. There are many example pedagogical as well as real application models.

With a modern version of BridgePoint (found here: [https://s3.amazonaws.com/xtuml-releases/nightly-build/buildfiles.html](https://s3.amazonaws.com/xtuml-releases/nightly-build/buildfiles.html)), you can view and edit a number of other pedagogical and real-world applications.

In Help-\>Quick Start, you can quickly find the GPS Watch, which is still a teaching example but more complex.

On GitHub in xtuml/models you will find dozens of examples. Real-world applications include ‘vitalsigns’, ‘ec’ and ‘mail’.

[https://github.com/xtuml/models](https://github.com/xtuml/models)

Cheers,
Cort

---

**Schmill** · July 14, 2023 at 5:35 pm

Thank you very much
