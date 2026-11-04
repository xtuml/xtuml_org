---
redirect_from:
  - "/community/topic/bp-4-2-0-win-unable-to-translate/"

layout: "topic"
title: "BP 4.2.0 win - unable to translate"
date: "2015-03-04"
permalink: "/forums/topic/bp-4-2-0-win-unable-to-translate/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**zjasz** · March 4, 2015 at 7:05 am

Hi,

I just downloaded the BP’s latest version 4.2.0 and tried to use C++ compiler but failed with the error below:

\[code title=”build output”\]Wed Mar 4 07:47:48 2015
xtumlmc_build -home C:/MentorGraphics/BridgePoint420/eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.mc.cpp.source_4.2.0/ -l2s -e -d code_generation -O ../../src/
Upgrading translation workspace: code_generation
NOTE: Domain code 0 allocated for this import.
NOTE: The domain code you have entered has already been used/allocated, but will allow this import to proceed normally.
sys.arc: 0: ERROR: Could NOT open File ‘C:/MentorGraphics/BridgePoint420/eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.mc.cpp.source_4.2.0//mc3020/arc/sys.arc’.

Error Occurred During File Generation… (Number of Errors: 1)
Code generation complete.
Wed Mar 4 07:47:48 2015
\[/code\]

it does in case of C source as well but it works for C binary.
Please advise how to get rid of this issue.
Many thanks.

---

**cort** · March 5, 2015 at 11:15 pm

Hi ZJasz,

You are missing the model compiler archetypes (which are not yet part of the standard install). Get them from [https://github.com/xtuml/mc](https://github.com/xtuml/mc). Copy these in the the c++.source/mc3020/arc folder. You will need to rename “sysc” to “specialized”.

To get C source, rename “c” to “specialized”.

Let me know how it goes.

Cort
