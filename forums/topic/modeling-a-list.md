---
redirect_from:
  - "/community/topic/modeling-a-list/"

layout: "topic"
title: "Modeling a list"
date: "2017-11-16"
permalink: "/forums/topic/modeling-a-list/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**xthunderheartx** · November 16, 2017 at 1:52 pm

Can anybody give me the title of the video which gives an example of modeling a list? It was incidental to the subject of the video so a search doesn’t yield anything. It’s a reflective association but can’t remember the details …

Thx-KDP

---

**cort** · November 16, 2017 at 2:00 pm

I am not sure how to find it in the videos, but I can point you to an example.

In GPS Watch, look at TrackPoint. It has a reflexive for ordering (in a list). Also, TrackLog has 2 relationships to TrackPoint ‘has first’ and ‘has last’. So, these are the head and tail of the linked list. There are operations that do the insert into the list.

I am sure you know you can get GPS Watch from the Help-\>Welcome-\>Quick Start page in BridgePoint.

Cort
