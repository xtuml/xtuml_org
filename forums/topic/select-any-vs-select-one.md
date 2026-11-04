---
redirect_from:
  - "/community/topic/select-any-vs-select-one/"

layout: "topic"
title: "select any VS select one"
date: "2013-08-06"
permalink: "/forums/topic/select-any-vs-select-one/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dean** · August 6, 2013 at 5:11 pm

I was recently asked to clarify the difference between “select any” and “select one”. While both selections return either a single matching instance or an empty set, the usage of select one is more restrictive. The general rule I follow is that

> **select one** is used only in the specific case of making a selection across a 0..1 relationship. In all other cases use **select any** when wanting only a single instance.

This rule applies equally to single relationships and relationship chains where select one can only be used in chains containing only 0..1 relationships.

---

**Lee Riemenschneider** · August 13, 2013 at 2:47 am

I found the term, “a 0..1 relationship”, a little confusing. I understand that you mean “towards a 0..1 relationship end”, but you also should include “towards a 1 relationship end” and “for selecting an associative class” to cover all the cases for using “select one”. e.g., all the cases where there can only be one related instance.
