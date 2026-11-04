---
redirect_from:
  - "/community/topic/goldfish-brain-using-time-in-a-model/"

layout: "topic"
title: "goldfish brain - using time in a model?"
date: "2017-08-31"
permalink: "/forums/topic/goldfish-brain-using-time-in-a-model/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**sfinnie** · August 31, 2017 at 1:55 pm

It’s been a while and the grey matter is creaking.

How do I use the time / timer functions? I have some OAL in a state that fails to parse:

\[code title=””\]self.commitmentDate = TIM::current_date();

create event instance cooling_off_complete of Commitment2:cooling_off_complete() to self;
cooling_off_period = TIM::timer_start(microseconds: 30\*24\*60\*50\*1000, cooling_off_complete);
\[/code\]

The TIM external entity isn’t found on lines 1 & 3. I can’t remember how to add it – would be grateful of a reminder.

Thanks,
Scott.

---

**keithbrown** · August 31, 2017 at 2:24 pm

Hi Scott,

Add a new package to your model, then right-click on it and in the CME pick “Add built-in external entities”

Of course, you can also copy and paste EEs from one model (like example GPS Watch or MicrowaveOven) to another.

Best,
Keith

---

**sfinnie** · August 31, 2017 at 3:05 pm

Ahh – easy when you know how :)

Thanks Keith.
