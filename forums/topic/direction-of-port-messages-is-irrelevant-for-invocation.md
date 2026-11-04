---
redirect_from:
  - "/community/topic/direction-of-port-messages-is-irrelevant-for-invocation/"

layout: "topic"
title: "Direction of port messages is irrelevant for invocation?"
date: "2015-11-04"
permalink: "/forums/topic/direction-of-port-messages-is-irrelevant-for-invocation/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**nukic** · November 4, 2015 at 12:01 pm

Today I noticed some weird behavior with BridgePoint (4.2.0) port messages.
I mistakenly reversed the desired direction of the interface messages (or provision/requirement roles on components), so all messages on port that I intended to be outgoing, were incoming and vice versa.

Consequently, when writing OAL code, for outgoing communication I used incoming messages. And everything worked perfectly, verifier did not complain.

I am aware that you can locally, within component, provide OAL actions for outgoing port messages: this is useful for standalone component testing, for dummy simulation of the remote component port.

However, I did not expect that, when component is connected to remote component, if we invoke incoming message, that it will actually invoke message on remote port of connected component (that has this dummy OAL code for standalone testing defined).

In this way, message direction on port messages is totaly ignored and irrelevant, which should not be the case.
If we invoke incoming port message, syntactic error should be given by the editor. If not that, at least verifier should give warning or an error indicating this is the case.

I noticed this behavior only because I generated code and got strange unexpected compilation errors.

---

**keithbrown** · November 5, 2015 at 2:52 pm

Hi Neno,

I’m pretty sure I’ve seen parse errors before for the “incorrect” conditions you describe, so I wonder if something got broken.

I did a quick test with GPS Watch where I flipped some message directions on the interfaces and re-parsed and I didn’t see any parse errors reported either.

Please enter a bug report for this.
