---
redirect_from:
  - "/community/topic/database-errors/"

layout: "topic"
title: "Database errors"
date: "2024-05-16"
permalink: "/forums/topic/database-errors/"
forum: "Miscellaneous"
forum_slug: "miscellaneous"
forum_url: "/forums/miscellaneous/"
---

**DCE_Matt** · May 16, 2024 at 6:40 am

Hello,

I’ve been using xtUML for some time and I have to say it’s a fantastic tool but one thing I’ve noticed, as my model gets larger I start getting database corruption.

The corruption takes the form of all my class operations are visible from the class level package but I’m unable to access them from the model explorer, the only way I found around this is to take daily backups and copy and paste the corrupted parts back into my model.

Is there anything I can do to recover database corruption ?

Many thanks

Matt

---

**cort** · May 16, 2024 at 9:40 am

I have been using xtUML for a very long time. It is fantastic, but I have never trusted it (or any tool) without having a version control system underneath. I recommend using git. This way, when something goes wrong you can go back to the last good commit.

This is also important for learning what is going wrong. I have worked with large models and found that the size of the model is not the problem. There have been specific bugs that can be reported and fixed when a diff of the before and after is available.

Cheers,
Cort

---

**DCE_Matt** · May 16, 2024 at 10:05 am

Hi Cort,

I’m already using git but taking a regular manual backups too.

Good idea, I’ll do a comparison between a broken and good version to see what changed. I’ll post up the difference too.

Cheers

Matt
