---
redirect_from:
  - "/community/topic/vhdl/"

layout: "topic"
title: "VHDL"
date: "2015-05-07"
permalink: "/forums/topic/vhdl/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**JamesB007** · May 7, 2015 at 12:03 pm

If there is already a thread for this, I apologise and could someone direct me to it?

I want to open a project (new or existing) with VHDL as the target compiled language rather than C/C++

I’ve read that xtUML can produce VHDL from the UML diagrams but can’t see VHDL as an option language.

Can someone tell me where it is?

- This topic was modified 10 years, 9 months ago by [![](https://secure.gravatar.com/avatar/ea6d2e68d9e24480faf46673da88124c2c221ff2d8107d66a7a34d3548928a08?s=14&amp;d=mm&amp;r=g)Bob Mulvey]({{ '/user/rmulvey/' | relative_url }}).

---

**keithbrown** · May 7, 2015 at 10:36 pm

A while back a student built a prototype VHDL model compiler. The VHDL model compiler selection is a placeholder for a future feature. I can try to dig up a PowerPoint presentation on the topic if that would be of further interest to you.

Are you modeling a VHDL application? I’m always interested in hearing what sort of projects BridgePoint is used for. Have you had a chance to look at the training course here on xtuml-org.hustlefish-sites.com?

---

**JamesB007** · July 30, 2015 at 3:24 pm

Hi Keith. This thread got buried under a load of other stuff I was working on and I’ve just come back to it now. I think you may have seen from my recent chatroom convos that I am interested in automating the process of flashing a microprocessor (originally an FPGA) from UML diagrams and action language. I noticed that there was an option to create a new project with a VHDL model compiler rather than the C/C++ that I have been using currently. Is that only in 5.1? I can’t find it any more now that I am using 4.2

There are so many training courses and videos that I’m never sure where to start. I’m so new to any of this. I didn’t even know what an FPGA was or what flashing a microprocessor meant until five months ago. It’s quite overwhelming sometimes.

That PowerPoint presentation would be good to see.

---

**cort** · July 31, 2015 at 2:32 pm

Hi JamesB and Keith,
I have been digging for that preso; it was created 6 years ago. So far, I have not been able to grab it. Meanwhile, some good stuff that I have not seen in a while has been fun to read.
More later.
Cort

---

**keithbrown** · August 3, 2015 at 2:43 am

Hi James,

The VHDL MC is still in the prototype phase. We have C, C++, and SystemC model compilers that are production-ready. The majority of users model their applications in BridgePoint, then use “Build Project” to create C code for the application. Once you have the C you can cross-compile to a target microprocessor, synthesize, etc…

As far as learning xtUML and BridgePoint, I highly recommend our Getting Started page ([getting started]({{ '/getting-started/' | relative_url }})). This gives you background into why someone would want to use xtUML to model an application. Once you understand “why”, the “Modeling with xtUML” training course linked from there covers “how”. It takes you through the actual mechanics of using BridgePoint itself.

Cheers,
Keith
