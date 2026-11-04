---
redirect_from:
  - "/community/topic/using-xtuml-without-bridgepoint/"

layout: "topic"
title: "Using xtUML without BridgePoint"
date: "2013-09-11"
permalink: "/forums/topic/using-xtuml-without-bridgepoint/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**fredbasset** · September 11, 2013 at 7:27 pm

Tempted by the idea of an OpenSource Executable UML editor I downloaded xtUML…

I may be missing something obvious, but I can’t see a way to get my Models out of xtUML or a way to access them programatically inside Eclipse, in order to write my own code generator. The ‘Export’ menu option is the closest I’ve got, but that seems to be identical to the Eclipse workspace files (ie SQL insert statements into a proprietary schema).

I’ve downloaded the source code from the git repository in the hope of being able to use that, but this appears to be only a tiny fraction of the code needed to run the xtUML Editor.

Can someone point me in the right direction, or is the xtUML Editor not useful without a BridgePoint licence?

Thanks

---

**Lee Riemenschneider** · September 17, 2013 at 11:39 am

In what format do you want the models? The xtUML Editor help files have sections on the translation process and the Rule Specification Language. This is the approach that was taken at my previous employ to create an in-house model compiler. I was very happy to get a license for the MC-3020, as it was a much better compiler.

The only external format is XMI, and I’m not sure how to export to that format anymore.

---

**cort** · September 23, 2013 at 2:39 pm

Hi fredbasset,

Your data is your data. :)

There are a few ways to access the data.

1\) You have the data in the file system in the SQL format.
2) You can export the model with or without graphics in the SQL format.
3) There is a java API such that you can access the data in memory using java plugins (eclipse extensions).
4) Buy/build a model compiler.

The format for 1 and 2 is open and published. The xtUML Editor delivers the xtUML meta-model in source model format. If you go to Help-\>Welcome-\>QuickStart you can create an example project with the xtUML Metamodel.

3 requires that you sling some java.

4 requires a license to a model compiler.

I hope this helps.
