---
redirect_from:
  - "/community/topic/returning-strings-from-c-functions/"

layout: "topic"
title: "Returning strings from C functions"
date: "2015-01-01"
permalink: "/forums/topic/returning-strings-from-c-functions/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**cort** · January 1, 2015 at 4:58 pm

[The C Programming Language](http://onefact.net/old-testament/)

Kernighan and Ritchie… to get your minds thinking about translating xtUML to C and specifically about returning strings. A technical write-up (analysis note) will follow after the holiday.

---

**cort** · January 2, 2015 at 5:13 pm

Consider the xtUML OAL (object action language) snippet below.

*name* and *logo* are local string variables.
*buffer* is a class.
*scmp* and *simple* are operations which each return a string.
*scmp* takes 2 string parameters.

Notice how the return string from simple is being passed as a parameter into the second invocation of scmp.

name = “BridgePoint”; logo = “xtUML”;

name = buffer::scmp( s1:”action”, s2:”language” );

logo = buffer::scmp( s1:logo, s2:buffer::simple() );

- This reply was modified 11 years, 1 month ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).
- This reply was modified 11 years, 1 month ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).

---

**cort** · January 2, 2015 at 5:25 pm

The MC-3020 model compiler translates the above OAL into C.

C does not have a native string type, so returning strings from functions provides challenges. Namely, a pointer can be returned, but data itself exists “behind the pointer”. This is usually O.K.

However, consider the operations *scmp* and *simple* above. What if the strings returned were local variables formed and calculated inside the scope of the respective functions?

In such a case, the return pointer will point to deallocated stack space. This is not good.

To address this, an analysis has been performed outlining options for changing the MC-3020 model compiler. The analysis is documented here.

[https://github.com/cortlandstarrett/bridgepoint/blob/master/doc-bridgepoint/notes/589_stringtest/586_stringtest.ant.md](https://github.com/cortlandstarrett/bridgepoint/blob/master/doc-bridgepoint/notes/589_stringtest/586_stringtest.ant.md)

Please read the above note and provide your thoughts here.

---

**Lee Riemenschneider** · January 2, 2015 at 6:10 pm

My vote would be for the by reference method. Is there a case for mutiple ways, chosen by marking?

---

**cort** · January 2, 2015 at 7:00 pm

@Lee, why? I want to see/hear objective reasoning and rationale.

---

**keithbrown** · January 2, 2015 at 10:16 pm

Option 5.1.6 (Architectural by-ref param) is my favored choice.

– It avoids re-entrancy problems that a static in the callee (or global scope) would have
– It is a (if not the most) common way of handling this problem in C
– It performs well by avoiding unnecessary copying of data

---

**Lee Riemenschneider** · January 3, 2015 at 12:03 am

I think the main reason I liked it is that it appears to give more flexibility over the span of the call. Consider that we have a pointer that is known by both the callee and the caller. The callee can resize the pointed to memory space, or can write within the original size. The callee can take the value pointed to, send it to another process, and write the returned value into the memory space. i.e., asynchronous handling of a synchronous call.

Of course, there are some further questions raised. Do we need a size parameter, or will all strings be NULL terminated? Is there any danger of overwriting memory?

---

**cort** · January 4, 2015 at 8:13 pm

A factor not documented in the analysis note is the commonality between C and C++.

MC-3020 is both a C and C++ model compiler. The delta between the two model compiler dialects is (perhaps surprisingly) small. Of course C and C++ differ in syntax in some areas, but C can be made “to do things like C++” in most situations. And usually, “doing it like C++” is a Good Thing.

I see potential value in returning strings “like C++ does it”.

---

**Erik Wedin** · January 7, 2015 at 9:32 am

I vote for the 5.1.6 Architectural By-Ref Parameter approach since it seems to eliminate all the problems in the other methods like static/shared variables and fixed size buffers etc. This is a design approach used successfully when we translated xtUML into Ada in our Ada MC.

---

**Erik Wedin** · January 7, 2015 at 9:40 am

It is also important to find an approach the static and run-time analysis tools accepts as erroneous free code.

We are running continuos analysis of our generated code with “cppcheck” ([http://cppcheck.sourceforge.net/](http://cppcheck.sourceforge.net/)) and currently the generated MC3020 triggers a large number of warnings/errors. Some that are valid and some that are not due to the xtUML semantics like instance selections via unconditional associations that would (should) not return a null pointer.

We are using “Valgrind” to perform run-time checks and it flags the return of strings from functions as erroneous.

---

**UltraDark** · January 7, 2015 at 11:24 am

I’ve written a few model compilers over the years that translated to ANSI C and the Architectural By-Ref Parameter option was implemented in the vast majority of invocations.

Its faster, more memory efficient, the string length does not have to predetermined in the callee and its thread safe.

The amount of effort for implementation pals into insignificance considering the effort needed to create the model compiler in the first place and Once It’s Done It’s Done For Everyone Forever (TM).

---

**cort** · January 23, 2015 at 3:02 pm

Thanks, everyone, for the comments. This was an interesting design.

In this design note: [https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/notes/589_stringtest/589_returnstring.dnt.md](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/notes/589_stringtest/589_returnstring.dnt.md)
…you will read that we ended up going with the by-ref parameter design. Even though some may see the “xtuml_string” return design more natural, ANSI C and gcc are simply not quite ready for it.

OIDIDFEF!
