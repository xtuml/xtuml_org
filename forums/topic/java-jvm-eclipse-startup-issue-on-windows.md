---
redirect_from:
  - "/community/topic/java-jvm-eclipse-startup-issue-on-windows/"

layout: "topic"
title: "java / jvm & eclipse startup issue on Windows"
date: "2015-08-04"
permalink: "/forums/topic/java-jvm-eclipse-startup-issue-on-windows/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**keithbrown** · August 4, 2015 at 5:51 pm

A user extracted the BridgePoint 5 Windows zipfile on Windows8, then ran Launcher.bat. He was promptly greeted with an eclipse/java error dialog that said:

“Java was started but returned exit code=1”
then had a long list of parameters to the java invocation.

The error dialog clearly points to a Java problem launching the JVM. In this case, we solved the problem by editing Launcher.bat. We replaced the existing “set BP_JVM=” line that points to javaw.exe with this line:

\[code title=””\]set BP_JVM=%BPHOMEDIR%/jre/bin/client/jvm.dll\[/code\]

Using the new line, BridgePoint starts without issue.
