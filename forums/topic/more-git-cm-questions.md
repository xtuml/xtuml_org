---
redirect_from:
  - "/community/topic/more-git-cm-questions/"

layout: "topic"
title: "More Git / CM questions"
date: "2017-03-29"
permalink: "/forums/topic/more-git-cm-questions/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**micke.x** · March 29, 2017 at 9:05 am

Hi,

I am still struggling with understanding the capabilities of Compare and Merge for models, using Egit.

I have read the document in Help.
I have looked at the Tuturial videos in Module 5 of the Modelling with xtUML on-line course.

Recently, I have switched BP version to a Nightly Build from last week: 6.2.4

Are there any restrictions not mentioned in these sources?

One of my scenarios is that I am trying to merge two branches, with basically some arbitrary simple model changes in one or both branches.
Typically, I
– add some attribute to a class
– rename another attribute
– rename a class
– delete an attribute

Following the instruction video on Git Merge, I am almost not able to handle any conflicts at all.
“Copy all non-conflicting changes” simply does not perform anything.
The same with “Copy selected change from right to left”.
The only change I am allowed to make a merge decision on correctly (from the above changes) is when an attribute is removed, then “Copy selected change from right to left” works fine.

Can you provide any more detailed instructions or information on restrictions or defects in this area.

I believe I am using Git correctly, i.e. using the correct Merge mode (anyway, I have tried both…).

---

**keithbrown** · March 30, 2017 at 3:26 pm

Hello micke.x,

The process you describe does not sound like you’re really going off into the weeds. And, there are no known defects in this area. I recommend you capture reproduction steps and raise an issue in the bug tracker ([http://support.onefact.net](http://support.onefact.net))

Regards,
Keith

---

**keithbrown** · March 30, 2017 at 3:26 pm

Hello micke.x,

The process you describe does not sound like you’re really going off into the weeds. And, there are no known defects in this area. I recommend you capture reproduction steps and raise an issue in the bug tracker ([http://support.onefact.net](http://support.onefact.net))

Regards,
Keith
