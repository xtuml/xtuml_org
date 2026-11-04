---
redirect_from:
  - "/community/topic/how-do-i-save-or-export/"

layout: "topic"
title: "How do I save or export?"
date: "2016-01-26"
permalink: "/forums/topic/how-do-i-save-or-export/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**JamesB007** · January 26, 2016 at 11:16 am

I’m not even sure which of the two it is I need to do. I’ve been happily developing models on a single machine in 4.2 and I need to work on the same xtUML models on my laptop which is also running BridgePoint xtUML 4.2

What I need to know is, how do I get the project on to my other machine. Should be simple, right?

Can I email it to myself as an attachment? Should I save it and copy the folder(s) to an external memory device (USB stick)? Should I export?

What should be the easiest way to take the models I’ve already worked on and saved and open them up on another machine running the exact same version of xtUML?

---

**keithbrown** · January 26, 2016 at 7:31 pm

The best solution is to create an account on github and store your model project in revision control. Then you can make changes locally on one machine, push the changes up to github and then on the second machine pull down the changes. Make changes on machine 2, push, repeat. Here is an example of an xtUML model in github: [https://github.com/xtuml/models/tree/master/applications/futbol](https://github.com/xtuml/models/tree/master/applications/futbol)

Of course, this requires that you learn a bit about using git. Module 5 in the xtUML Modeling online course will get you started.

If you truly want to go the export + USB stick route, there are two options. See units 4 & 5 of Module 6 in the online course.

---

**Lee Riemenschneider** · January 27, 2016 at 12:18 am

Copying the workspace should work, but the best way to stay in sync is to take Keith’s suggestion and use git (or some other CM). If you don’t want to go to the cloud, there are programs to sync laptop and desktop (I.e., 2 computers). On Linux, I use unison. Even if you are using git, the sync will copy the latest changes bypassing a need to push and pull from the repository.

---

**JamesB007** · January 28, 2016 at 1:24 am

I want to go for simplicity, i.e. as few operations as possible. If this means simply copying files and directories or folders, that would be preferable. I can manage the version control and the synchronisation myself. The project I’ve been working on is in my “users” folder and I created a workspace called “ABS”. Can I just copy all of the files and folders under the ABS folder in users (on a USB device) and copy them from there into a similarly named folder on the other machine?

---

**Lee Riemenschneider** · January 28, 2016 at 7:33 pm

A .metadata folder exists in the root workspace, so you have to copy all of the workspace. ex. if your ABS project was in users/jamesb007/workspace/ABS, then copy workspace to the USB stick.

You might not have to copy any other project folders, besides ABS, but that might get the .metadata data out of sync. I’m not sure what eclipse does when it can’t find project folders.

---

**Lee Riemenschneider** · January 28, 2016 at 7:37 pm

Having said that, if I had to go for copying workspace back and forth vs. export and import, I’d do the export and import. In either case, you won’t have a merge option, so keeping things in sync means making sure you don’t have edits in both places.

---

**JamesB007** · June 23, 2016 at 3:40 pm

Thanks. I finally got round to doing this via the USB stick route – been away from xtUML for a few months – and it worked the first time.

I tried it again and it wasn’t so successful. I now have a project with diagrams and models from one project but the ‘C’ source from another project.

Luckily this is on a machine that I can almost completely wipe clean and start again.

---

**keithbrown** · June 23, 2016 at 5:28 pm

I’m not sure how such a project data mixup could happen. I’ve never seen cross-project pollution like that.

---

**JamesB007** · June 24, 2016 at 9:47 am

Me either! I’ve managed to clean it up and import the project I want. Because the import process only works if there’s already a project open, I’ve created a new but empty one in a new workspace before doing the import. Can I just delete the empty project from this workspace once the project I want has been successfully imported?

---

**keithbrown** · June 24, 2016 at 3:42 pm

Yes, you should be able to delete the empty one.
