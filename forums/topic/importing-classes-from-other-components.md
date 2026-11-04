---
redirect_from:
  - "/community/topic/importing-classes-from-other-components/"

layout: "topic"
title: "Importing Classes from other components"
date: "2019-08-26"
permalink: "/forums/topic/importing-classes-from-other-components/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Clive** · August 26, 2019 at 12:02 pm

The structure of my model is a PACKAGE containing three (3) COMPONENTS (A, B, C) each of which contains another PACKAGE (A1, B1, C1, respectively) containing only a CLASS DIAGRAM. From what I can gather from the HELP and the STYLE and GUIDE MANUALS I may not be able to create IMPORTED CLASSES in (say) the CD in A1 from the CD in B1 due to certain VISIBILITY RULES. However, it does seem ambiguous. Anyway, I CANNOT indeed do what I suggested above. When I attempt to create an IMPORTED CLASS and ASSIGN it, I am presented with an EMPTY list. I’ve tried to QUALIFY precisely where the required IMPORTED CLASS can be found – but alas I fail.

So! Is there a way, I can IMPORT a CLASS or do I have to resort to reconstructing my model in order to achieve my aim?

BTW, I’ve had no trouble assigning interfaces etc.

Any suggestions would be (again) appreciated.

Clive.

---

**Clive** · September 5, 2019 at 3:10 am

Well! I now know why nobody responded to this one. A somewhat silly question, really! All brought about by not fully appreciating the difference between the old ‘domain/bridge’ approach as compared to the component/interface approach – and doing the latter correctly. My review seems to have exposed one or two minor issues with BridgePoint concerning ‘interfaces’ and ‘sub-components’ which I’ll report on in the right place.
