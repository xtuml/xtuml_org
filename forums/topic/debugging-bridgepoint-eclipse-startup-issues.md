---
redirect_from:
  - "/community/topic/debugging-bridgepoint-eclipse-startup-issues/"

layout: "topic"
title: "Debugging BridgePoint / Eclipse startup issues"
date: "2015-06-04"
permalink: "/forums/topic/debugging-bridgepoint-eclipse-startup-issues/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**keithbrown** · June 4, 2015 at 7:57 pm

A user reports that BridgePoint 5 fails to start properly on their machine:

> I have downloaded 5.0.0 for Linux. I have unzipped it in an installation folder, but when I run the Launcher.sh eclipse starts but there is no xtUML perspective to be found. The splash screen shows xtUML and and the BridgePoint logo. I have tried to find the xtUML perspectives via “Window-\>Open Perspective-\>Others” but no xtUML perspectives are present.

This thread will discuss debugging this problem.

---

**keithbrown** · June 4, 2015 at 8:01 pm

======================================================
Using Eclipse OSGi debug console window (OSGi console)
======================================================

Windows:
————
\_- Open Launcher.bat
\_- Change BP_JVM setting to use java.exe instead of javaw.exe
\_- add \[code\]-console \[/code\] to the eclipse.exe command line before \[code title=””\]-vm %BP_JVM%\[/code\]

Linux:
————
\_- Open Launcher.sh
\_- add \[code title=””\]-console \[/code\] to the eclipse command line before \[code title=””\]-vm \$BP_JVM\[/code\]

All:
————
– Run the Launcher script
\_R A console window appears during the launch. You will see the \[code title=””\]osgi\> \[/code\] prompt. The following commands are to be entered in this osgi console.

osgi commands for debugging:
– \[code title=””\]ss\[/code\]
This command lists all registered plugins and their status

– \[code title=””\]ss \[/code\]
This lists a subset based on the matches. For example: ss org.xtuml.bp.core

– \[code title=””\]diag \[/code\] (e.g. \[code title=””\]diag org.xtuml.bp.core\[/code\])
Displays unsatisfied constrains for the given bundle

– \[code title=””\]start \[/code\]
Attempts to force load the specified plugin (the id comes from the \[code title=””\]ss\[/code\] result). Try \[code title=””\]start \[/code\]

\_- \[code title=””\]close\[/code\]
Shutdown and exit OSGi

---

**keithbrown** · June 4, 2015 at 8:15 pm

Ignore all the “1. ” in the previous post. The forum formatter is inserting those as line numbers for all code blocks.

---

**keithbrown** · June 12, 2015 at 6:21 pm

In this case, the root of the issue is that the user wasn’t able to use a shared/multi-user (and readonly) installation. The issue is fixed with a simple command run by the system admin. Additional information has been added to the FAQ: [https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/FAQ.md#sharedinstall](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/FAQ.md#sharedinstall)
