---
redirect_from:
  - "/community/topic/bridgepoint-uml2-activities-diagrams-support/"

layout: "topic"
title: "BridgePoint UML2 Activities & Diagrams support"
date: "2016-11-13"
permalink: "/forums/topic/bridgepoint-uml2-activities-diagrams-support/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**toni.siljamaki@gmail.com** · November 13, 2016 at 9:51 pm

Hello all.
What is the plan for BP improvementrs wrt Activity Diagram support and their execution in the near future?

I have just checked the BridgePoint Activities support in BP550 and its current metamodel version.
E.g. the following UML2 capabilities are not supported:

CallBehaviorAction = call a sub-activity – not possible
CallOperationAction = call an operation (= execute some action language processing) – not possible
AcceptEventAction = specify the trigger – not possible
SendSignalAction = specify the signal – not possible
ControlFlow – not supported
ObjectFlow – not supported

BridgePoint is now also the Papyrus-xtuml project, Papyrus is based on Eclipse UML2, Alf activities can be executed in Moka.

Activity Diagrams are utilized by a proprietary Ericsson DSL for defining directed acyclic graphs (DAG) to support Carl Hewitt’s actor model for multicore SW development. [https://www.youtube.com/watch?v=7erJ1DV_Tlo](https://www.youtube.com/watch?v=7erJ1DV_Tlo)

The whole idea with this proprietary E/// UML2-based Baseband DSL is to simplify software development for the Ericsson Multi Core Architecture (EMCA). Q: When will these Papyrus capabilities be supported also in BridgePoint/Papyrus-xtuml ???

Regards/Toni

Additional information: Thesis report and conference paper on the Ericsson Baseband DSL

Thesis report can be found here: [https://gupea.ub.gu.se/bitstream/2077/40135/1/gupea_2077_40135_1.pdf](https://gupea.ub.gu.se/bitstream/2077/40135/1/gupea_2077_40135_1.pdf)
Conference paper can be found here: [https://www.conference-publishing.com/list.php?Event=SLE15](https://www.conference-publishing.com/list.php?Event=SLE15)
Paper abstract can be read here: [http://dl.acm.org/citation.cfm?id=2814253](http://dl.acm.org/citation.cfm?id=2814253)

From the paper abstract by Salome Maro et al:
Domain Specific Languages (DSLs) are an established means of reducing the gap between problem and solution domains. DSLs increase productivity and improve quality as they can be tailored to exactly fit the needs of the problem to be solved.

From the thesis report by Salome Maro:
Compared to General Purpose Languages (GPLs), a DSL focuses on the patterns that are used in a specific domain therefore avoiding all the general notations that are not needed within the domain. This makes creation of applications easier and designers can write less code (as little as 2%) than when using a GPL.

---

**cort** · November 15, 2016 at 2:37 am

Hi Toni,

Thanks for the post.

Activity Diagrams have not been discussed much among the users that I regularly work with. However, there may be development that I have no visibility to.

Since most of the long-time BridgePoint development shops are not using the Activity Diagrams in Papyrus-xtUML (BridgePoint), there is discussion of deprecating the BP version in favor of native Papyrus Activity Diagrams as part of the BP merge with the Papyrus Platform.

What do you think?

P.S. For engineers wanting to add functionality such as this start here: [developers]({{ '/participate/developers/' | relative_url }})
