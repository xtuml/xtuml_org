---
redirect_from:
  - "/community/topic/connecting-parameters-on-interfaces-with-parameters-in-oal/"

layout: "topic"
title: "connecting parameters on interfaces with parameters in OAL"
date: "2013-04-16"
permalink: "/forums/topic/connecting-parameters-on-interfaces-with-parameters-in-oal/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**cort** · April 16, 2013 at 8:22 pm

Hmm, V_PAR is very “far” from \*PARM and C_PP.
In the C model compiler, we are relaxing the requirement to alphabetize all parameter lists. The parameters are ordered in the model; we will use that ordering.
However, V_PARs are ordered positionally and are labeled and do not need to match up with the ordering of the parameters (\*PARMs) defined on the interfaces.
Basically, I want to connect V_PAR (MC TE_PAR) with its corresponding \*PARM (MC TE_PARM).
It seems that this will be a pretty massive traversal.
Any advice?

---

**Anders** · April 17, 2013 at 12:15 pm

One way of doing it, is as a two pass translation. The meta-model for \*PARM and C_PP is not the most friendly, the definitions are all over the place. First translate all V_PAR, \*PARM and C_PP, for the latter we have condensed all definitions into one place, i.e. a subprogram with formal parameters with an associations back to the OOA meta-model. Additional, each formal parameter has a conditional association to one actual parameter (actually V_VAL), which represents current actual value for that formal parameter. When translating a call using actual values, first select all V_PARs for that call and select the correspondent subprogram. Loop over the V_PARs and make a conditional search among the formal parameters for that particular subprogram, by name in our case, and relate the correspondent V_VAL to the formal parameter as the current actual value. Now you are ready to translate the actual call, by translating the subprogram and its predefined parameter order, or what ever order the formal parameters have, using the association to get current actual value. When translating a call to the same subprogram again, unrelate the previous actual values and relate the new ones before translating the subprogram. Hope you can get some ideas from this.

---

**cort** · May 1, 2013 at 7:23 pm

Thanks, Anders.
The method I used is similar. In the MC model, there is only PARM and not many flavors. So, during initial translation, these PARM instances are created and linked to \*PARM.
Also during initial translation PAR instances are created and linked to V_PAR.
A little bit later, the PARM instances are ordered (by reflexive association) into the correct sequence as defined by the action to which they are connected (operation, function, message, etc). At this time, the traversal is made from PARM to PAR, and the order (as an integer) is copied from PARM to PAR.
When the OAL is translated and the PARs are output in the order dictated by the PARMs.

---

**Anders** · May 2, 2013 at 7:21 am

Cort – thanks for the idea of an integer as position pointer. One question, are you searching among the PARs during the OAL-translation for the order, i.e., 1,2,3,… or do you have an reflexive association for that order of the PARs as for the PARMs?

---

**cort** · May 2, 2013 at 1:03 pm

The PARs are ordered by reflexive according to V_PAR. (This ordering is not used.) The integer Order comes from the PARMs. When generating the code, the Order is searched in the old-fashioned (slow) way.
