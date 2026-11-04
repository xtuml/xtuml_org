---
redirect_from:
  - "/community/topic/external-entities/"

layout: "topic"
title: "External Entities"
date: "2018-06-19"
permalink: "/forums/topic/external-entities/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**Rob** · June 19, 2018 at 1:25 am

I am using External Entities and added an operation to an external entity . I recompiled. However, the new operation does not work. Any troubleshooting hints?

---

**keithbrown** · June 19, 2018 at 1:39 am

I’m not sure what you mean by “does not work”, but I can explain a point about using EEs that might help.

When you translate your project, an .c will be created in the src/ folder. You then need to copy that file to the gen/ folder and put your implementation of the internals into the functions. Next time you translate, the empty/structural EE will be created in the src/ folder, then the build process will copy the .c from the gen/ folder into the src/ overwriting the blank one that is there.

So, when you add a new operation, you need to edit the function signature into the .c in the gen/ folder so at the end of translation your full-fledged EE ends up in src/ .

You might also check out Module 18 – Realized components in the learning course.

---

**Rob** · June 19, 2018 at 1:03 pm

Sorry for the vague explanation, It does not recognize the new operation when called from the model. I did not edit the function signature in the /c gen/folder. I will give that a try. Thanks.

---

**cort** · June 19, 2018 at 1:55 pm

There is a Property on the External Entity called ‘Realized’. If you want to interpret your OAL in bridges (operations on the EE), then set ‘Realized’ to false.
