---
redirect_from:
  - "/community/topic/declaring-domain-specific-in-oal-expressions/"

layout: "topic"
title: "Declaring Domain-specific in OAL expressions"
date: "2024-01-04"
permalink: "/forums/topic/declaring-domain-specific-in-oal-expressions/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Schmill** · January 4, 2024 at 1:41 pm

Whenever I have to pass a \<\<dataType\> variable to an operation/event I would create an attribute for the self context in OAL. is there a more elegant way to declare a local variable of the data type without having to add a class attribute?

Thank you.

- This topic was modified 2 years, 1 month ago by [![](https://secure.gravatar.com/avatar/3040dde2b0b01d2ea433fda15866ec95296afd183c3e8807c9693f8e2edd2eab?s=14&amp;d=mm&amp;r=g)Schmill]({{ '/user/schmill/' | relative_url }}).

---

**cort** · January 4, 2024 at 1:46 pm

There is not a more elegant way.
There is another equally awkward way.
You can create a function that returns that type… like I said, awkward.

---

**Schmill** · January 4, 2024 at 2:23 pm

Thank you
