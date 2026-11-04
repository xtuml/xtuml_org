---
redirect_from:
  - "/community/topic/connection-between-graphical-and-semantical-metamodels/"

layout: "topic"
title: "Connection between graphical and semantical metamodels"
date: "2014-08-20"
permalink: "/forums/topic/connection-between-graphical-and-semantical-metamodels/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Nastra** · August 20, 2014 at 7:33 am

Hello,

I need to navigate from connectors in graphical metamodel (GD_CON) to an association (R_REL), in semantic metamodel, that connector is connecting. Any idea how?
I do not know how graphical and semantical metamodels are connected, by which relation?

Thank you for your answer,

Nastra

- This topic was modified 11 years, 6 months ago by [![](https://secure.gravatar.com/avatar/0dbd2f184306989e05840d1339723b5e472c3da237dfbd43f9062bcebf063be5?s=14&amp;d=mm&amp;r=g)Nastra]({{ '/user/nastra/' | relative_url }}).
- This topic was modified 11 years, 6 months ago by [![](https://secure.gravatar.com/avatar/0dbd2f184306989e05840d1339723b5e472c3da237dfbd43f9062bcebf063be5?s=14&amp;d=mm&amp;r=g)Nastra]({{ '/user/nastra/' | relative_url }}).

---

**Travis London** · August 21, 2014 at 1:37 pm

Graphical elements are connected to the semantic elements via the represents attribute of the GD_GE instance. The represents attribute will be the associated semantic element. During diagram initialization the ooa_id attribute is read and used to set the represents value.
