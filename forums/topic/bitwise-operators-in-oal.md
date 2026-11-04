---
redirect_from:
  - "/community/topic/bitwise-operators-in-oal/"

layout: "topic"
title: "Bitwise operators in OAL"
date: "2018-07-27"
permalink: "/forums/topic/bitwise-operators-in-oal/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**John Wolfe** · July 27, 2018 at 1:02 am

To build a domain that knows how to encode, decode, and interpret a message protocol, bitwise operators in OAL would be very useful (e.g., bits 3-5 of byte 1 contain the message length).

Is anyone else craving bitwise operators in OAL?

---

**keithbrown** · July 30, 2018 at 7:20 pm

I have wished for them before and I know other users have as well. In fact, one of the MASL-oriented engineers said this year “MASL doesn’t have bitwise operators, but we’ve often wished it did… maybe we’ll add them one day.”

Apparently this is one of those things that just never quite gets enough traction to make it happen!

---

**Lee Riemenschneider** · July 30, 2018 at 7:43 pm

It never gets much traction, because it’s an implementation concern, not an analysis concern.
e.g., message length occupies bits 3-5 of byte 1 is something you specify in the model compiler for class, message, that has attribute, length.

---

**John Wolfe** · July 30, 2018 at 9:13 pm

@Lee, perhaps I have been thinking about this incorrectly. Message length is but one of many fields — I used it only as an example. Suppose the protocol in question carries all sorts of information that must be extracted from bit fields within bytes (e.g., message length, message type, sensor ID, sensor values, etc.).

Consider how to build a domain that knows about this protocol and how to convert between messages packed into a byte stream and xtUML interface messages. Can you think of a way to do so without coupling the model compiler to the protocol?

In our case we would prefer to use MC-3020 as is.

---

**Lee Riemenschneider** · July 30, 2018 at 11:40 pm

Here’s what I was thinking. The message structure as a class. Class and attribute mark that allow the code to match the byte stream representation.
You probably have something more complex, where a header has to be unpacked before the rest of the message can be processed, which makes my solution a mess of bridge calls. Maybe it’s a bad problem space for xtUML.

---

**John Wolfe** · July 30, 2018 at 11:50 pm

Actually, I think it’s a good problem space for xtUML, as such a domain would allow us to generate code for the protocol in a number of different languages, while maintaining the knowledge of the protocol in precisely one place.

@Lee, are you saying that a need to examine bit fields within bytes (which causes the craving for bitwise operators) makes an application ill-suited for xtUML?

---

**Lee Riemenschneider** · July 31, 2018 at 12:53 am

Bitfields in bytes are a physical storage packing mechanism for a specific implementation of data optimization. The idea of packing and unpacking in the smallest unit of storage might be a domain. Bit fields within bytes are the smallest unit of storage in some languages, but not all. How can we say it is implementation independent enough for inclusion in an AL?

---

**John Wolfe** · July 31, 2018 at 4:32 am

\>How can we say it is implementation independent enough for inclusion in an AL?
Because many other languages, including at least three that treat platform-independence as a primary requirement, do so?

But, let me try to restate the requirements because bitwise operators may be but one solution to the problem at hand.

At its core, this problem is one of mapping a collection of bits to a named field (ref. examples in previous posts). In some cases a field spans multiple bytes while in others it is contained within a single byte.

Ultimately, I would like to build a domain that knows how to:
1. Convert between a stream of bytes and a collection of instances of classes, where class attributes represent message fields. This semantic mapping between a bit field and a semantically named attribute is the crux of the problem.
2. Convert between these class instances and xtUML interface messages.

Bridge operations can likely be used in place of native OAL bitwise operators. But, perhaps I have been staring for too long at hand-written, imperative code that uses bitwise operators to map between bit fields and named message fields (semantics).There may be other approaches that meet the requirements while leveraging existing tooling without coupling the resulting model to non-existent model compiler features.

---

**bgat** · July 31, 2018 at 2:38 pm

> Bitfields in bytes are a physical storage packing mechanism for a specific implementation of data optimization.

Bit fields are TWO very useful things, one of which is a storage packing mechanism.

The other, even-more-useful thing that bit fields provide is atomic, parallel evaluation of multiple related binary conditions. You can do that without bit-aware operators, but the math gets fairly blush-inducing unless you do cryptography on a regular basis.

When I use a bit field in a condition variable, I don’t care about the underlying representation because the value itself is never expressed outside of the scope where I’m using it. (I’m barely even a novice in xtUML, maybe condition variables have no equivalence there.)

- This reply was modified 7 years, 6 months ago by [![](https://secure.gravatar.com/avatar/1dc49ac91dbf664948205689e1999e337f888cf4d46075ec74eef7acb0a21558?s=14&amp;d=mm&amp;r=g)bgat]({{ '/user/bgat/' | relative_url }}).

---

**bgat** · July 31, 2018 at 2:44 pm

When I say “atomic”, I mean in the language “I can do this all on one line” sense. Maybe “concise”, or “terse”, or even “convenient” are better word choices…

Although it’s reasonable to presume that the underlying implementation supports atomicity, I don’t depend on it unless I’m working in a language that explicitly guarantees it.

---

**cort** · July 31, 2018 at 5:07 pm

I would like to see the additional operators in OAL and yet am not sure explicit masking-in of bits is the best approach. Maybe something more declarative rather than imperative…

There is (was?) support in MC-3020 for marking bit fields on attributes (in the comment block) of classes.

Also, a feature to “fix” the extent at a specific location in memory was provided:

[https://xtuml.github.io/docs/mcug/ch04s02.html#idm269943694752](https://xtuml.github.io/docs/mcug/ch04s02.html#idm269943694752)

What are your thoughts on this? If it worked, would it be a workable approach?

---

**Lee Riemenschneider** · July 31, 2018 at 10:12 pm

\[My last reply must have gone to the ether…\]

I’ve encountered whole messages and partial messages. Partial messages have come ordered and unordered; one byte at a time or larger chunks, and I’ve seen bitfields across byte boundaries. I’ve never taken a communication domain model to production. (Leon Starr once told me he was working on one, but I never heard if it got finished.)

Field extraction and recombining was done through bridges.

---

**Lee Riemenschneider** · July 31, 2018 at 10:23 pm

Condition variables equivalence in an xtUML model would be a Flag class with a many to one relationship with a thread. ;-)

“concise” isn’t a goal of class modeling in xtUML, whose goal is to expose information. It can be a goal of the model compiler.

---

**John Wolfe** · August 2, 2018 at 1:37 am

[@Cort]({{ '/user/cort/' | relative_url }}), maybe. Messages vary in length from one type to the next, but each message of a given type is the same length. Fields contained within messages vary from one type to the next. There are over 100 different message types. We could create a class for each message type with attributes leveraging the bitfield capability of MC-3020. If, upon arrival, the byte stream containing a message could be plopped at the base of the extent for the appropriate class, we could avoid imperative bit-whacking, so long as the content of a message does not vary with anything other than the message type. I have vague memories of “if byte 5, bit 3 is active, then bytes 6-7 contain this, otherwise they contain that,” so I need to have a closer look at the protocol.
I have sketched (in my head) the specification-class side of a model that once populated would describe each message type. This approach might eliminate the need to define a class for each message type (instead each one would be defined as preexisting instance data) or leverage the aforementioned model compiler features, but I need to find time to extract said model from my head and try out what I have in mind. However, it’s likely that using PEI data to define message structure is less convenient/accessible than doing so with classes.
