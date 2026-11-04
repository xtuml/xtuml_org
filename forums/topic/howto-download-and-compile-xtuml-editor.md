---
redirect_from:
  - "/community/topic/howto-download-and-compile-xtuml-editor/"

layout: "topic"
title: "HOWTO Download and Compile xtUML Editor"
date: "2014-03-25"
permalink: "/forums/topic/howto-download-and-compile-xtuml-editor/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**cort** · March 25, 2014 at 4:19 pm

[https://github.com/xtuml/editor](https://github.com/xtuml/editor)

In the README you can see the link to a HOWTO that has been updated. The full model (xtUML meta-model, a.k.a. OOAofOOA) is present. The full source is present. Build it!

---

**Lee Riemenschneider** · April 2, 2014 at 1:10 am

Looks like it’s not finding antlr. Imported the jar found in eclipse_extensions. The build started complaining about eclipse.org.\* imports, which I couldn’t clear by restarting or touching bp.core files. I would normally expect to have to include these jar files. ???

---

**Bob Mulvey** · April 2, 2014 at 11:39 am

Hi Lee,

That sounds like a JDK bug that we have not found a good permanent solution for. Here is what to do to get around it:
\_- turn off build automatically
\_- open the following file in text mode: com.mentor.nucleus.bp.core/generate.xml
\_- Touch the file (just add a space to a comment), and save the change
\_- From package explorer select all the projects in the workspace, and then select File-\>Refesh to refresh them all
\_- Turn on build automatically
\_Result: All the eclipse.org\* dependencies should now be resolved

---

**Lee Riemenschneider** · April 3, 2014 at 1:39 am

That’s still not working for me.

The thing I don’t understand is how the build can find any of the org.eclipse resources if they’re not on the build path. (At least I can’t find them in Java Build Path.) Adding external jars reduces the errors. I haven’t resolved them all, but I haven’t tried adding all.

---

**Bob Mulvey** · April 3, 2014 at 3:30 pm

You should not need to modify any build settings. I am fairly confident the problem is a dependency issue. I am not sure why it is being so persistent for you. Maybe we could share a desktop session with join.me and I could help you work through it and find the problem? If you want to do this, please add me as a skype contact, my skype contact name is bob_mulvey. Add me as a contact and drop me a message and we will connect and work through this. In the mean time I will keep looking, but I am not yet able to reproduce the problem in a way that touching files and rebuilding doesn’t fix.

---

**Bob Mulvey** · April 3, 2014 at 5:06 pm

I had another thought… Are you using xtUML Editor instillation or a vanilla Eclipse? Please use the xtUML Editor installation if you are not already doing so ([download]({{ '/download/' | relative_url }})).

---

**Lee Riemenschneider** · April 4, 2014 at 5:26 pm

I’m using the xtUML Editor installation, Linux on Ubuntu 13.10 64-bit. I have a few more things to look at before I decide to go the Skype (or Google Hangout, …) route. This’ll be a good Eclipse learning experiment.

---

**Lee Riemenschneider** · April 4, 2014 at 8:02 pm

Just built it under Windows at work. I think I might have seen my mistake. I’ll post again after I try it at home on Ubuntu.

---

**Lee Riemenschneider** · April 5, 2014 at 1:49 pm

Built it under Ubuntu. It was a failure to follow directions on my part, as I created workspaces/xtumlEditor as a Java project before installing the .p2f file.

---

**poj** · April 22, 2014 at 8:53 pm

I’ve managed to build an run the xtUML Editor on Ubuntu, following the instructions, but with one twist.
Initially the built xtUML Editor wouldn’t launch, with an error regarding “org.osgi.framework.BundleException: The activator org.eclipse.ui.internal.WorkbenchPlugin for bundle org.eclipse.ui.workbench is invalid”
The reason for the problem was that one swt Plugin was missing in the launch configuration, org.eclipse.swt.gtk.linux.x86.

---

**lbi** · April 25, 2014 at 8:06 pm

Is it possible to create a plugin from these projects, then to install it in another xtUML editor?

---

**cort** · April 27, 2014 at 8:06 pm

\> Is it possible to create a plugin from these projects, then to install it in another xtUML editor?

Yes.

---

**cort** · May 7, 2014 at 1:08 pm

Yes. If you try and you see the desired plugin(s) did not load, you can use the OSGi console to determine why it did not load and resolve the problem.

Yes… depending on what you mean “recently”. You can see all updates/commits here: [https://github.com/xtuml/editor/network](https://github.com/xtuml/editor/network)

Note, the source will get a significant update within a couple days (to match the newest build).

---

**lbi** · May 9, 2014 at 10:32 am

Is the last xtUML edotor’s (4.1.2) full source is present?

---

**Bob Mulvey** · May 9, 2014 at 11:48 am

Yes, the full source for the binary editor is present.
