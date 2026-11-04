---
redirect_from:
  - "/community/topic/bridge-operation-call-with-return-value-hangs-in-verifier/"

layout: "topic"
title: "Bridge Operation call with return value hangs in verifier."
date: "2024-04-14"
permalink: "/forums/topic/bridge-operation-call-with-return-value-hangs-in-verifier/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Schmill** · April 14, 2024 at 7:00 am

Hi,
`self.Att = Bridge::Op(p1:"p");`
The above line gets stuck while running verifier but completes without an issue in executable (MC 3020).

---

**Schmill** · April 14, 2024 at 7:14 am

is there any workaround?
Thanks.

---

**cort** · April 14, 2024 at 11:34 am

Is Bridge implemented in action language?

---

**Schmill** · April 14, 2024 at 11:54 am

It is blank and no special markings. I also created a reproducible standalone project in the latest release.

---

**cort** · April 14, 2024 at 2:36 pm

That is the problem. The return value needs to come from somewhere.
You can “implement” or “stub out” your bridge operations with action language in the bridge activities.

---

**Schmill** · April 15, 2024 at 12:46 am

Ohhh! makes sense:)

Is there any way to have the C code exposed to the verifier? I need to inspect strings, and I’m trying to create a wrapper to the strtok function with a bridge.

---

**cort** · April 15, 2024 at 8:31 am

No. Verifier lives firmly in the interpreted action language world… with a few integrations/customizations with Java.

---

**Schmill** · April 15, 2024 at 12:10 pm

Okay, thanks.
