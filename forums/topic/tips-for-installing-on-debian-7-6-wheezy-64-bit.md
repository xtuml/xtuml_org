---
redirect_from:
  - "/community/topic/tips-for-installing-on-debian-7-6-wheezy-64-bit/"

layout: "topic"
title: "Tips for Installing on Debian 7.6 Wheezy 64-bit"
date: "2014-10-12"
permalink: "/forums/topic/tips-for-installing-on-debian-7-6-wheezy-64-bit/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Lee Riemenschneider** · October 12, 2014 at 5:41 am

I installed xtUML Editor 4.1.16 today on Debian Wheezy.

Here’s what additional packages were needed:
ia32-libs ia32-libs-gtk libgtk2.0-0 lib32ncurses5

I’m not sure if lib32ncurses5 is required. I installed it based on a recommendation found in researching the error message in the ~/MentorGraphics/xtUMLEditor/configuration logs.
