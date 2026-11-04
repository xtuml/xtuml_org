---
redirect_from:
  - "/community/topic/formalization-increasing-tool-usability/"

layout: "topic"
title: "Formalization - Increasing tool usability"
date: "2016-02-01"
permalink: "/forums/topic/formalization-increasing-tool-usability/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**poj** · February 1, 2016 at 8:48 pm

A couple of weeks ago, I held a course in using BridgePoint to work with xtUML models. During the course I tried to gather some of the things that the attendees thought would make their life easier when using the tool.
Some of the things is small changes in the tool, some requires a bit more work. This is the first of a couple of topics discussing such feature proposals.

The first thing is the handling of prefixes when you formalize an association. Today you are asked to provide a prefix for the identifier. This works great in many cases, but is a bit cumbersome if the identifier you use to formalize consists of multiple attributes. All the referential attributes gets the same prefix. If the identifier of a class C2 consist of two attributes, C1_ID and ID, where C1_ID is referential and has a prefix set, and you formalize an association from C2 to C3, setting no prefix, two referential attributes are added to C3, with the same name. For the user it is not directly visible that the name C1_ID in C2 is constructed with a prefix, and this is not directly obvious.
Here the tool should be changed to set the prefix mode of a referential attribute to “Referred to Prefix” if no prefix is provided. In that way any prefix already added is preserved.
What do you think about that feature change?

Actually, looking at referential attributes, it could be useful to have an additional prefix mode available, “Prefixed Referred Name”, which results in the name of an attribute to be the displayed name of the referred to attribute, with a local prefix added. If such a choice was added, that could be a reasonable default choice for prefix mode of referential attributes, since it makes prefixes behave the way most new users would expect. One other approach would be to change the behavior of the “No Prefix” prefix mode to use the name, not the root name, of the referred to attribute, but that would break existing models.
