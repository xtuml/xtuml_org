---
redirect_from:
  - "/community/topic/naming-a-referential-attribute/"

layout: "topic"
title: "Naming a Referential Attribute"
date: "2016-08-11"
permalink: "/forums/topic/naming-a-referential-attribute/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**cort** · August 11, 2016 at 2:39 pm

The default for naming referential attributes is to be named the same as the referred-to attribute… and usually with a prefix added.

There may be situations where a user wants to have a completely new name for the referential attribute. This is possible but tricky to do. Here is how.

In the Properties View, first change the Root Name of the referential attribute to the desired value. Then do the following:

Properties-\>Referential Attribute-\>Referential Attribute-\>Referential Attribute Referred to Mode-\>Local Attribute will make the Attribute Root Name change show up on the class diagram.

---

**Bob Mulvey** · August 11, 2016 at 2:59 pm

I find this an interesting one to go look at the meta-model for, to see how it really works. I thought perhaps it may be useful to write the steps I think through to find this spot in the meta-model. To find the right place, my thinking goes something like this…
– I know this affects an attribute, and an attribute is represented in the Subsystem package by class Attribute (O_ATTR). So, this is where I look first.
– Once I get this spot in the meta-model I know that this is not just an attribute we are looking for, it is a referential attribute, and I can see that this is right next to Attribute in Subsystem package, Attribute Reference In Class (O_REF)
-I know I want to see where the name comes from, and I see the attribute RAttr_Name that defines this.
-At this point, I see that O_REF.RAttr_Name is a derived attribute so I open it in the OAL editor to see how it is derived. Furthermore, I see that this attribute has a decent description which is helpful.
-The O_REF.RAttr_Name’s OAL leads me to another derived attribute, O_ATTR.Name whose OAL is pretty clear and additionally contains a nice description.

- This reply was modified 9 years, 6 months ago by [![](https://secure.gravatar.com/avatar/ea6d2e68d9e24480faf46673da88124c2c221ff2d8107d66a7a34d3548928a08?s=14&amp;d=mm&amp;r=g)Bob Mulvey]({{ '/user/rmulvey/' | relative_url }}).
- This reply was modified 9 years, 6 months ago by [![](https://secure.gravatar.com/avatar/ea6d2e68d9e24480faf46673da88124c2c221ff2d8107d66a7a34d3548928a08?s=14&amp;d=mm&amp;r=g)Bob Mulvey]({{ '/user/rmulvey/' | relative_url }}).
