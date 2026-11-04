---
redirect_from:
  - "/community/topic/thread-terminates-randomly/"

layout: "topic"
title: "Thread terminates randomly"
date: "2015-08-24"
permalink: "/forums/topic/thread-terminates-randomly/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**benjo123** · August 24, 2015 at 8:20 am

Dear All,

I have come across with some issues regarding BridgePoint’s thread handling. I start 3 threads from Java code. Sometimes not all the threads are started, however in the Java code they should start from one after another. If I restart several times the Verifier, then it works. (It is not the business logic in the Java code that prevents the thread from running.)

I have experienced, that BridgePoint allows at most 3 Java threads to run in my code. If I want to start more than 3 threads, BridgePoint kills the latter ones.

Another issue regarding threading: if 3 threads run simultaneously, BridgePoint terminates one after a while.

Do you have any idea, why BridgePoint is so strict with running Java threads?

Thank you for the help in advance.

Best regards,
Ben

---

**keithbrown** · August 24, 2015 at 1:25 pm

Hi Ben,

I’m not aware of anything BridgePoint does to explicitly restrict Java threads. I suggest you follow the Developer’s getting started guide ([https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/Developer%20Getting%20Started%20Guide.md](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/Developer%20Getting%20Started%20Guide.md)) to build BridgePoint yourself.

Once you have it built you can use the you can run the Debug Launch Configuration “Eclipse Application \> BP Application”. Then you can use the JDT debugger to set breakpoints, see the stack, watch variables, look at threads, etc…

Verifier is implemented in the org.xtuml.bp.debug.ui plug-in. I suggest you start by looking around in there.

Regards,
Keith

---

**benjo123** · August 24, 2015 at 1:51 pm

Hi Keith,

Thank you for the answer. I will let you know how far I went.

Regards,
Ben
