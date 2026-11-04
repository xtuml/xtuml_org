---
redirect_from:
  - "/community/topic/integrating-xtuml-design-processes-with-existing-legacy-code/"

layout: "topic"
title: "Integrating xtUML Design Processes With Existing Legacy Code"
date: "2014-12-04"
permalink: "/forums/topic/integrating-xtuml-design-processes-with-existing-legacy-code/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**dark_sloth** · December 4, 2014 at 3:09 am

Hi all,

I’ve decided to move towards a more disciplined and repeatable process at work, which means I need to spend more time on design. I’ve tried in the past, but the structure of the older code means it’s difficult to simply just design new parts (I think I’ve got an idea codewise, new functionality is a good chance to abstract away from the cruft and refactor a bit while putting new unit tests in place) and slot them in, meaning I can’t really use an automated model compiling process unfortunately.

I do, however, want my code to be properly documented so we can see at a glance how it behaves. My question is, should I just treat the legacy code as an outside service in the model until it’s gradually refactored into something more coherent, or is there a better way to do this?

Thanks in advance!

- This topic was modified 11 years, 2 months ago by [![](https://secure.gravatar.com/avatar/4ee226bb42873b42c67c942e7d9352d542fdcfab19326e424c9cb88f0ff9d3db?s=14&amp;d=mm&amp;r=g)dark_sloth]({{ '/user/sgream/' | relative_url }}).

---

**Lee Riemenschneider** · December 4, 2014 at 8:11 pm

I’ve beat my head against this wall many times. :-) If nothing else, the practice of modeling can give a better understanding of the requirements and help identify possible re-factoring points.

Here’s some things I’ve done in the past:
1) Construct a domain chart for the system: this will help you identify the subject matters, but might not match the structure of the code.

2\) Model a single subject matter domain and integrate it with existing code: this usually involves changing some existing code to better align with the domain boundaries. This works as either a code replacement or code addition task, but can be impossible if the code has really poor encapsulation.

3\) Model a single subject matter as a way to document how the code should be meeting the requirements. If nothing else, this will give you a model you might be able to use at some future point when the legacy code gets too crufty. It also gives you a good point to design tests from; almost like having an independent test team working from requirements rather than your code.

I’ve never had any luck with auto reverse engineering. It either gave me a spaghetti model or a model that didn’t give much benefit over looking at the code. i.e., no abstraction.

The best path is to get buy-in from management and co-workers (also something I haven’t had much luck with), so you’re modeling effort isn’t viewed as wasted time. You’ll also get better help from subject matter experts within the company, if the effort is seen as value added.

---

**dark_sloth** · December 4, 2014 at 8:44 pm

Yeah, I’ve been pretty staunch that I’m designing and documenting everything before I sit down to code from now. My manager is a bit skeptical that designing everything is worth my time, but it’s got to the point of complexity where no one person knows exactly what any of the subsystems do, and when we learn it’s gone within a month or two (I understand how most of the UI works, for example, but because it’s old style WinForms and a lot of the logic is tied in with the code behind rather than properly abstracted in functional modules). It’s about time we had some technical documentation, I’m adamant xtUML will solve at least 75-80% of that need :)

Oh well, I’ll try this for 2 or 3 months and then make my mind up on whether it suits our needs. It’ll be an interesting experiment, at the very least

---

**keithbrown** · December 4, 2014 at 9:13 pm

xtUML provides two different approaches to interface modeled software with existing/realized/legacy software: External Entities and Realized Components. There is documentation in the help about each as well as a whole module (Module 18 – Realized Code Integration) in the Modeling with xtUML online course on this website ([on line courses]({{ '/learn/on-line-courses/' | relative_url }})).

Lee made a great suggestion to start by picking a small piece of new functionality to model. Your model of new functionality can be implemented in xtUML and include a modeled interface to the key points of interaction with legacy code.

---

**dark_sloth** · December 7, 2014 at 11:01 am

Ah, excellent. I was looking for something like that and turned up [this]({{ '/assets/uploads/2013/04/BridgePoint_xtUML_Modeling_Exercises.pdf' | relative_url }}), which has a couple of errors in it.

Thanks for the ideas, I’ll let you know how it goes and see if my observations line up with yours, seeing as it seems to be the cause of a few headaches :) Not that I think I’ll have anything new to share, but might be worth getting the knowledge out there
