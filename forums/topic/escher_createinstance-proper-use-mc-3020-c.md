---
redirect_from:
  - "/community/topic/escher_createinstance-proper-use-mc-3020-c/"

layout: "topic"
title: "Escher_CreateInstance proper use MC-3020 C"
date: "2023-12-05"
permalink: "/forums/topic/escher_createinstance-proper-use-mc-3020-c/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Schmill** · December 5, 2023 at 3:47 pm

I make thousands of calls to Escher_CreateInstance on the same stack as a result of reading a file. the executable crashes after 10 calls to Escher_CreateInstance .

I can only assume that this is a safety mechanism, is there a mark I should enable or some kind of a flush function I can use?

Thanks.

---

**cort** · December 5, 2023 at 3:51 pm

By default, MC-3020 allows for 10 instances of each class.
You can mark these numbers to be higher.
You can also enable dynamic memory allocation.
These marking features are explained in detail in the MC-3020 User Guide.
Cheers!
Cort

---

**Schmill** · December 5, 2023 at 4:05 pm

Thank you!
