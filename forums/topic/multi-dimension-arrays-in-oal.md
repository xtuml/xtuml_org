---
redirect_from:
  - "/community/topic/multi-dimension-arrays-in-oal/"

layout: "topic"
title: "Multi dimension arrays in OAL"
date: "2013-12-28"
permalink: "/forums/topic/multi-dimension-arrays-in-oal/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**TI** · December 28, 2013 at 3:32 am

Is it possible to use multi dimension arrays in OAL?

Such like , my_array\[3\]\[3\].

If we can use multi dimension arrays, it would be very convenient to implement some datapath algorithms.

//TI.

---

**keithbrown** · January 7, 2014 at 2:48 pm

Multi-dimensional arrays are supported both as transients and modeled attributes. As with single-dimensional transients as arrays in OAL, you must set the maximum extent first:

// Right:
my_array\[1\]\[1\] = 3;
my_array\[0\]\[0\] = 0; // Order of this and next two lines does not matter
my_array\[0\]\[1\] = 1;
my_array\[1\]\[0\] = 2;

// Wrong:
my_array\[0\]\[0\] = 0;
my_array\[0\]\[1\] = 1; // Parser will indicate Array Index Out of Bounds
my_array\[1\]\[0\] = 2;
my_array\[1\]\[1\] = 3;

---

**TI** · January 8, 2014 at 3:47 am

Hi Keith,

Thank you for replying.
I confrimed that I could.

OAL is —
my_array\[1\]\[1\] = 3;
my_array\[0\]\[0\] = 0; // Order of this and next two lines does not matter
my_array\[0\]\[1\] = 1;
my_array\[1\]\[0\] = 2;

LOG::LogInfo(message: “Arrays are descripted below”);
LOG::LogInteger(message:my_array\[0\]\[0\]);
LOG::LogInteger(message:my_array\[0\]\[1\]);
LOG::LogInteger(message:my_array\[1\]\[0\]);
LOG::LogInteger(message:my_array\[1\]\[1\]);

Out put is —
User invoked function: func1
LogInfo: Arrays are descripted below
LogInteger: 0
LogInteger: 1
LogInteger: 2
LogInteger: 3

//TI
