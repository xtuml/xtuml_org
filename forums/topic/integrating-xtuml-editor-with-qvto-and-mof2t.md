---
redirect_from:
  - "/community/topic/integrating-xtuml-editor-with-qvto-and-mof2t/"

layout: "topic"
title: "Integrating xtUML Editor with QVTo and MOF2T"
date: "2014-03-06"
permalink: "/forums/topic/integrating-xtuml-editor-with-qvto-and-mof2t/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dan George** · March 6, 2014 at 7:31 pm

Hi,
I’m looking for ways to get EUML into common use and a free, as in free beer, tool chain is my present tactic. The xtUML Open Source editor is a great candidate for that tool chain. How would I go about integrating it with QVTo and Acceleo (open source MOF2T impl)?

I kind of think my idea is not really the within Mentor’s intent of publishing the editor source. It is a great idea to give xtUML users a way to customize their UI. Extending that to customizing to a different translation engine probably isn’t quite what Mentor had in mind. I do think that BridgePoint should be far superior to any open source contender. However, I can see the possibility that adapting to other translators might be considered an abuse of the privilege. I’d be happy to hear that I’m wrong about that but respectful if I’m right.

Any interest?

Thanks,
Dan

---

**Lee Riemenschneider** · March 6, 2014 at 8:21 pm

Acceleo is already included. (Help-\>About-\>Plugin tab)
I’m not sure what QVTo brings to the table. Are you attempting model-model transformation? (NOTE: Not familiar with QVTo).

I don’t see any way this would violate the terms of usage. I would assume that Mentor would be perfectly happy to take advantage of any good developments.

---

**Dan George** · March 6, 2014 at 10:49 pm

Thanks, Lee. I don’t see Acceleo in my install details. Doesn’t show up in Window-\>Open Perspecitve-\>Other, either. Perhaps you installed it youself? Are you able create an Acceleo project and use the xtUML project as input?

I installed Acceleo myself and I made a try at generateing a report of the Gps Watch model (Gps Watch.xtuml) but didn’t succeed.

Regarding M2M, in my Sparx EA prototype I found M2M to be useful. I still find UML helpful as an aid to 3GL design. I’d make my EUML model and translate that to a C++ PSM. I creatd the prototype C++ PSM manually and then developed the transform to automate. Sparx provides an out-of-the-box C++ code generator that produced the boilerplate text. The body text of generated classes was injected by my M2M translation. I could skip the M2M step. However, if it is possible to do OMG MOF2T then MOF2M (what QVT does) is just a different transform, MOF being the common input to either.

FWI, QVT has to languages: Relations and Operations. QVTo is an implementation of the imperitive, Operations langauge. I am not aware of an impl of the declaritive, Relations language.

---

**cort** · March 7, 2014 at 4:07 pm

Hello Dan,

Lee is right. :) The OSS xtUML Editor is licensed under one of the most liberal licenses available (Apache). There are virtually no restrictions on its public/private/commercial/educational use.

The proliferation of Executable UML is a Good Thing for the business and the engineering community. More modelers mean more people who want to execute and translate models. Some people may be willing to pay for commercial grade execution and translation. Those who do not can build their own. The APIs are opened up.

In any case, the/an editor is the critical front end to the process. It needs to be widely available and accessible. Thus, it is now free.

I hope that more people build execution engines and translators. It is the Right Way.

Kind Regards,
Cort
xtUML Modeler, Teacher and
Mentor Graphics Engineering Manager

---

**Dan George** · March 7, 2014 at 4:25 pm

Hi Cort,
Thank you for getting the moral issue out of the way for me. As a proponent for EUML technology, I want to be careful about unintended negative consequences.

Can you give me a pointer about how to extract the information from the xtUML model? Perhaps I even have everything I need to build my own translation already in the package. I just don’t know where to start.

Thanks again,
Dan

---

**cort** · March 13, 2014 at 12:28 pm

See [how to get model data from and xtuml model]({{ '/forums/topic/how-to-get-model-data-from-and-xtuml-model/' | relative_url }}) for a start.
