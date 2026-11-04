---
redirect_from:
  - "/community/topic/by-ref-event-parameters/"

layout: "topic"
title: "by-ref event parameters"
date: "2015-09-05"
permalink: "/forums/topic/by-ref-event-parameters/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**cort** · September 5, 2015 at 2:20 am

I can pass parameters in many contexts by-ref. There seems to be a restriction on passing by-ref parameters on events. Is this true?

---

**Lee Riemenschneider** · September 6, 2015 at 2:13 am

Given that events are asynchronous, passing by ref has many possible side effects. Also given that nothing in a domain is hidden, passing by ref doesn’t have a lot of value.

---

**keithbrown** · September 6, 2015 at 5:49 pm

I’ll note that there is an open BridgePoint issue for passing by-reference params across interfaces also ([https://support.onefact.net/redmine/issues/7678](https://support.onefact.net/redmine/issues/7678)).
