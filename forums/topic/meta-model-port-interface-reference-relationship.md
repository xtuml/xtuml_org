---
redirect_from:
  - "/community/topic/meta-model-port-interface-reference-relationship/"

layout: "topic"
title: "Meta-Model Port Interface-Reference Relationship"
date: "2016-12-05"
permalink: "/forums/topic/meta-model-port-interface-reference-relationship/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Bruce** · December 5, 2016 at 8:59 pm

The “Ports” youtube video says “…each port can be tied to only one interface.” at 1:15.

However, the meta-model for single Port associated with many Interface References.

Which one is correct?

---

**cort** · December 6, 2016 at 12:53 am

A port can be “formalized” to only one interface.

However, the port on one component can “connect” to the port (Interface Reference) on the port of another component more than once. This is limited to the client (Requirement) side. A server port (Provider) can connect with multiple clients (Providers).

So, the answer is kinda “both”. :)

---

**Bruce** · December 6, 2016 at 2:43 pm

Thanks for the reply.

I understand: A port can be “formalized” to only one interface.
I understand: However, the port on one component can “connect” to the port (Interface Reference) on the port of another component more than once.
I understand: This is limited to the client (Requirement) side.
I don’t understand: A server port (Provider) can connect with multiple clients (Providers).
Shouldn’t this be: A server port (Provider) can connect with multiple clients (\*Requirers\*).

---

**cort** · December 6, 2016 at 2:50 pm

Yes! My mistake.
