---
redirect_from:
  - "/community/topic/videos-on-xtuml-channel-on-youtube/"

layout: "topic"
title: "videos on xtUML Channel on YouTube"
date: "2013-05-03"
permalink: "/forums/topic/videos-on-xtuml-channel-on-youtube/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**cort** · May 3, 2013 at 12:54 pm

I just posted 3 new, short videos to youtube. All 3 are HOWTO type videos. All involve the xtUML Editor. 1 involves Verifier and 1 involves model compilation.

1\) HOWTO Build a Simple xtUML Component Diagram from Scratch

Starting from nothing, the simplest ever component diagram is built using xtUML. Two components and an interface are added to a package. Then, the two components are wired together in a simple deployment configuration. Every step is shown. This is a pattern that is used in almost all component models. Message sending in shown in the sequel.

2\) HOWTO Send Messages Between 2 xtUML Components

This video follows from HOWTO Create a Component Diagram from Scratch. It shows how to send messages between components using action language (OAL) in the ports. The simulation engine (Verifier) is then run to send the messages starting with an init message followed by stimulus and response.

3\) HOWTO Add Attributes to Meta-model Classes and Access Them in a Model Compiler

This short HOWTO video shows how to add an attribute to a meta-model class by editing the schema. Then a small model compiler is shown that writes to and reads from the newly added fields. An integer and a string field are added (number and buffer) to the Component (C_C) meta-model class of the xtUML meta-model.

---

**cort** · May 8, 2013 at 2:41 pm

Dean and Keith explain and demonstrate how to create/generate documentation from xtUML models.

[https://www.youtube.com/watch?v=9SKtJrmLZ2c](https://www.youtube.com/watch?v=9SKtJrmLZ2c)

---

**Anonymous** · October 29, 2015 at 7:34 am

Hello, I tried to send messeges between 2 components, I use this tutorial…[https://www.youtube.com/watch?v=7Qb3T9SDJsQ&amp;#8230](https://www.youtube.com/watch?v=7Qb3T9SDJsQ&amp;#8230); I want to debug application, but I don’t have option “Model Verifier application” in Debug Configurations so I cannot debug application. Can you please help me how to Debug this appication?

---

**cort** · October 29, 2015 at 1:14 pm

Hello Dula. Which version of BridgePoint are you running? There is a very recent post of a nightly build that has Verifier turned off (awaiting some additional changes for running on Eclipse Mars).
