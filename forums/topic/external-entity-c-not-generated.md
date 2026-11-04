---
redirect_from:
  - "/community/topic/external-entity-c-not-generated/"

layout: "topic"
title: "External Entity .c not generated"
date: "2024-02-11"
permalink: "/forums/topic/external-entity-c-not-generated/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Schmill** · February 11, 2024 at 12:58 pm

I created EE with a bridge operation in the domain, but it is not generated in the src folder. also created one outside of a domain, but no luck either.

Am I missing something?
Thank you.

---

**cort** · February 11, 2024 at 1:57 pm

You should create it inside the domain unless you do some special packaging to make it appear in the domain.

Is the EE referenced by action language? Perhaps MC-3020 is optimizing it out.

Look for information in the Console after the code gen runs.

---

**Schmill** · February 11, 2024 at 3:56 pm

Thats it! once referenced by the action it is generated.

Thank you.
