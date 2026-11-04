---
redirect_from:
  - "/community/topic/overlapping-supertypes/"

layout: "topic"
title: "Overlapping Supertypes"
date: "2017-11-27"
permalink: "/forums/topic/overlapping-supertypes/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dennis Tubbs** · November 27, 2017 at 8:25 pm

I have super type (Super_A) with six sub types. Four of the sub types have a second super type (Super_B). All sub type classes will be sub types of Super_A. How do I formalize the relationships to avoid having two identifying attributes in the sub types that are related to both super types? Even better would there be a way to formalize the super type relationship for Super_B so that it’s identifier would come from its sub types?

In general, is there a reason why the ability to add a prefix is not included in the formalization dialog for super / sub type relationships?

---

**Levi** · November 27, 2017 at 10:06 pm

The answer is to combine referential attributes in the subtypes.

In the past, BridgePoint has had the ability to combine referential attributes that refer to the same base attribute as a way to enforce constraints in the data model. Recently, the rules of when you can combine referential attributes have loosened and you can now combine any two referential attributes of the same type (they don’t need to refer to the same base). See this issue for more on that: [https://support.onefact.net/issues/9446](https://support.onefact.net/issues/9446), [https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/notes/9446_merge_attrs_int.md](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/notes/9446_merge_attrs_int.md)

Attributes can be combined by selecting one of the attributes, right click -\> Combine With… and selecting the attribute that you want to collapse into the attribute that was selected.

To answer the second part of your question, I don’t know of any reason historically why adding a prefix is not part of the formalization wizard for sub/super associations. But of course it is possible to modify the prefix (or use the prefix from the super class) through the properties view.

Hope this helps!
/Levi
