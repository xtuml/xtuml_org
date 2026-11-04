---
redirect_from:
  - "/community/topic/consistent-meta-model-and-schema/"

layout: "topic"
title: "Consistent meta-model and schema"
date: "2016-02-03"
permalink: "/forums/topic/consistent-meta-model-and-schema/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**Martin** · February 3, 2016 at 3:05 pm

I’m looking into the meta-model included in the 5.2 version and comparing the model with the schema in 5.2 of the mc.c.source plugin. These does not seams to be consistent. I thought that the schema was generated based on the meta-model. Is it the intention that these shall differ?
I suppose that the pre_builder output is consistent with the meta-model?

---

**keithbrown** · February 3, 2016 at 6:36 pm

Hi Martin,

Where exactly are you seeing a difference? Are you looking at the ooaofooa metamodel in the org.xtuml.bp.core source code on github or the metamodel project inside the BP welcome?

Regards,
Keith

---

**Martin** · February 4, 2016 at 7:11 am

I’m looking at the meta-model inside the BP Welcome. I think it is mostly classes and associations removed during the specific packages cleanup that still are present in the schema file.

---

**cort** · February 4, 2016 at 2:37 pm

Martin,
You will see them removed in an upcoming community release. You can find a much more recent version in my fork of the mc repository (branch 8019_progen3).
Even it still needs a bit more cleaned out.
Cort

---

**Martin** · February 4, 2016 at 3:53 pm

Hi,

Thanks for information. I’m updating the meta-model copy in our model compiler to be aligned with the 5.2.
