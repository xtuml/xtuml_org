---
redirect_from:
  - "/community/topic/setup-the-metamodel-project-on-linux/"

layout: "topic"
title: "Setup the metamodel project on Linux"
date: "2013-03-28"
permalink: "/forums/topic/setup-the-metamodel-project-on-linux/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Domonkos Asztalos** · March 28, 2013 at 11:13 am

I couldn’t setup the metamodel project from the welcome menu on Linux (Ubuntu 12.10), while doing the same for windows is not a problem. There is a sand-clock for forever …
Any idea?

---

**keithbrown** · March 28, 2013 at 1:46 pm

Hi Domonkos,

It worked for me when I just tried it, but I’ve seen similar behavior to what you describe in the past. Let’s try to import the metamodel, but do it by hand and bypass the welcome page. Here are the steps:

1\) Create a new project “metamodel”
2) Right-click on it and select “Import…” from the context menu
3) Now expand “BridgePoint \> BridgePoint Model”.
4) Choose “BridgePoint Model”, click “Next \>”
5) Now click “Browse…” and navigate to /eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.welcome\_/models/xtUML_Metamodel.xtuml”
6) Once the file is selected, click “Finish”

The model should be imported. Please let me know if this works or not.

Regards,
Keith

---

**Domonkos Asztalos** · April 9, 2013 at 12:13 pm

Hi Keith,

it did work, thanks!

Regards,
Domonkos
