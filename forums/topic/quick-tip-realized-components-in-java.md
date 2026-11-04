---
redirect_from:
  - "/community/topic/quick-tip-realized-components-in-java/"

layout: "topic"
title: "Quick Tip: Realized Components in Java"
date: "2017-06-05"
permalink: "/forums/topic/quick-tip-realized-components-in-java/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**keithbrown** · June 5, 2017 at 5:46 pm

The BridgePoint Help documentation contains information about creating and running realized components and external entities in Java. See “Help \> Help Contents \> BridgePoint UML Suite Help \> Reference \> Model Verifier Java Interface”.

A user we recently assisted was having trouble running his realized component. The issue turned out to be that when creating a Launch Configuration that uses realized components one \_must\_ turn off (i.e. uncheck) the “Run deterministically” option.

With the option turned off the realized component execution worked as expected.
