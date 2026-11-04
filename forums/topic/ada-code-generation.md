---
redirect_from:
  - "/community/topic/ada-code-generation/"

layout: "topic"
title: "Ada code generation"
date: "2015-09-17"
permalink: "/forums/topic/ada-code-generation/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**pvrego** · September 17, 2015 at 12:30 pm

Is it possible to generate Ada code using Bridgepoint? (aka: is there an Ada plugin for Bridgepoint?)

---

**keithbrown** · September 17, 2015 at 1:20 pm

Hello, welcome to the community.

No, BridgePoint does not include an Ada model compiler. BridgePoint has a heritage of usage by developers targeting deeply embedded systems, so the majority of users rely on the C model compiler. The next largest usage is C++. Both those MCs produce code that can run directly on the iron without an RTOS.

We also maintain the SystemC MC, which is useful for developers doing Hardware/Software co-simulation.

Some users have created and maintain their own model compilers in their own shops. These are not publicly available.

BridgePoint is developed with BridgePoint. Much of the tool is modeled in xtUML. The team uses a Java Model Compiler to translate the model into code that is usable in eclipse. MC-Java is targeted for this task and thus is not distributed as a generic Java model compiler.

Cheers,
Keith

---

**Bob Mulvey** · September 17, 2015 at 11:11 pm

The answer to your first question is yes, it is possible to create a model compiler for Ada using BridgePoint. As Keith pointed out there is currently not a public Ada model compiler available though.

---

**Lee Riemenschneider** · September 17, 2015 at 11:19 pm

Ada model compilers have been realized in the past.

Here’s a paper: [http://www.ooatool.com/docs/SDFAda90.pdf](http://www.ooatool.com/docs/SDFAda90.pdf)

Considering the date of the paper, this was a very early attempt at model compilation. IIRC, there was also a presentation given at a later date.

- This reply was modified 10 years, 5 months ago by [![](https://secure.gravatar.com/avatar/2beeed50ad01495a2bb8456ccfd23100a3ae303e29fc1a90ee450c7cf5e79641?s=14&amp;d=mm&amp;r=g)Lee Riemenschneider]({{ '/user/lwriemen/' | relative_url }}). Reason: Additional info

---

**Erik Wedin** · October 9, 2015 at 10:33 am

Hi,

Saab has generated a lot of Ada 95/2005 code for several projects with an in house Ada model compiler, starting in 2003. One presentation of the work was performed on the ModProd conference in Linköping, Sweden ini 2007:
[http://www.modprod.liu.se/workshop_2007/1.46536/talk6-2007.pdf](http://www.modprod.liu.se/workshop_2007/1.46536/talk6-2007.pdf)

A SPARK Ada model compiler was also developed and deployed. That work was presented at the Ada Europe 2010 conference:
– overview: [http://www.disca.upv.es/jorge/ae2010/slides/Guide_to_Industrial_Sessions.pdf](http://www.disca.upv.es/jorge/ae2010/slides/Guide_to_Industrial_Sessions.pdf)
– presentation: [https://www.yumpu.com/en/document/view/28328312/applying-model-driven-architecture-and-spark-ada/17](https://www.yumpu.com/en/document/view/28328312/applying-model-driven-architecture-and-spark-ada/17)

- This reply was modified 10 years, 4 months ago by [![](https://secure.gravatar.com/avatar/c41946e754db53c7472a7dc88144a5075a0a0b79d4accd705836574fcc1dccc6?s=14&amp;d=mm&amp;r=g)Erik Wedin]({{ '/user/erikwedin/' | relative_url }}).
- This reply was modified 10 years, 4 months ago by [![](https://secure.gravatar.com/avatar/c41946e754db53c7472a7dc88144a5075a0a0b79d4accd705836574fcc1dccc6?s=14&amp;d=mm&amp;r=g)Erik Wedin]({{ '/user/erikwedin/' | relative_url }}).

---

**Erik Wedin** · October 9, 2015 at 10:41 am

Another link to the pdf version of the 2010 SPARK Ada presentation:
[http://www.disca.upv.es/jorge/ae2010/slides/IP1-2_Wedin_MDA_and_SPARK.pdf](http://www.disca.upv.es/jorge/ae2010/slides/IP1-2_Wedin_MDA_and_SPARK.pdf)

There have also been two presentations performed regarding Ada & xtUML and VHDL & xtUML at the Shlaer Mellor User Group in 2004. Unfortunately I have not been able to find them on the net.

- This reply was modified 10 years, 4 months ago by [![](https://secure.gravatar.com/avatar/c41946e754db53c7472a7dc88144a5075a0a0b79d4accd705836574fcc1dccc6?s=14&amp;d=mm&amp;r=g)Erik Wedin]({{ '/user/erikwedin/' | relative_url }}).

---

**Lee Riemenschneider** · October 9, 2015 at 12:36 pm

I have a complete collection of all the papers that were on the Project Technology website as well as all the SMUG (Shlaer Mellor User Group) conference presentations and the SMUG mailing list archives.

I think all the papers are present on the OOATool website, but the SMUG stuff isn’t there. I’ll look at getting it all put on this site, if not, I’ll put it up on my website and post a link here.

I even found a binder containing printed copies of it all from back when viewing things online took too long. :-D

---

**Erik Wedin** · October 9, 2015 at 2:37 pm

Great!

---

**Lee Riemenschneider** · October 10, 2015 at 5:10 am

Here’s the 2004 [SMUG presentation on ADA]({{ '/assets/uploads/2015/10/Saab-Ada-Model-Compiler.pdf' | relative_url }}).

Here’s the 2004 [SMUG presentation on VHDL]({{ '/assets/uploads/2015/10/Saab-VHDL-Model-Compiler.pdf' | relative_url }}).

---

**Lee Riemenschneider** · October 10, 2015 at 5:12 am

…and if you want to browse through everything I had it’s [here]({{ '/learn/the-historical-documents/' | relative_url }}).
