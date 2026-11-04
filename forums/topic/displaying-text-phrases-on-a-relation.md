---
redirect_from:
  - "/community/topic/displaying-text-phrases-on-a-relation/"

layout: "topic"
title: "Displaying text phrases on a relation"
date: "2014-07-23"
permalink: "/forums/topic/displaying-text-phrases-on-a-relation/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**ArtsaN** · July 23, 2014 at 5:35 pm

Hello all,

I’m trying to automatize the process of creating a class diagram,
and I got classes and relations created and displayed on canvas. However,
on relations are showed multiplicity and relation number, but not text phrase.
Any ideas why and how to get text phrases to be shown?
Also, is it possible to “lock” positions of relation name, multiplicity and text phrase to relation itself?
To make them relative to the position of relation, meaning when I move relation, that they move with relation
and have same position and distance with respect to relation as they had before?
Now I need to reposition those classes, change where their relations are connected to classes
(as I understood, this has something to do with connectors?)

Hoping for some help,

A

---

**Travis London** · July 25, 2014 at 5:29 pm

In order to set the details of associations (multiplicity, conditionality, text phrases) you will need to navigate to the proper element and call the set\* methods wrapped in a transaction.

ClassAsSimpleParticipant_c\[\] parts = ClassAsSimpleParticipant_c.getManyR_PARTsOnR207(SimpleAssociation_c.getManyR_SIMPsOnR206(association));
parts\[0\].setCond(1); // 0 = unconditional, 1 = conditional
parts\[0\].setMult(Multiplicity_c.One);
parts\[0\].setTxt_phrs(“some value”);
parts\[1\].setCond(0); // 0 = unconditional, 1 = conditional
parts\[1\].setMult(Multiplicity_c.Many);
parts\[1\].setTxt_phrs(“some value”);

Note that because these associations are not formalized there are two instances of ClassAsSimpleParticipant_c. The first one will match the starting point of the graphical element that was created. This is just one example for a simple association that is not formalized. Look at the Association package in the xtUML metamodel and you will see the other cases that may need to be handled.

Regarding the position of the graphical text, that can certainly be done. However you would need to fork the xtUML editor and modify the ui.graphics plugin to do so. This will require some knowledge of GEF as well as the xtUML graphical metamodel (in the ui.canvas project).

Again positioning classes and the connecting points (anchors) after creating the elements can be done. You again will need an understanding of the xtUML graphical metamodel, but once you set the appropriate values the diagrams will show what you expect.
