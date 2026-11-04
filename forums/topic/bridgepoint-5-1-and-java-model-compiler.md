---
redirect_from:
  - "/community/topic/bridgepoint-5-1-and-java-model-compiler/"

layout: "topic"
title: "BridgePoint 5.1 and Java Model Compiler"
date: "2016-01-11"
permalink: "/forums/topic/bridgepoint-5-1-and-java-model-compiler/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**francesco.sibilla@libero.it** · January 11, 2016 at 10:47 am

Does BridgePoint 5.1 include the Java Model Compiler?

The Java MC is available in the Set Model Compiler dialog, but when building it prints:

\[code title=””\]Errors occurred during the build.
Errors running builder ‘Model Compiler Pre-Build’ on project ‘hello’.
No RootPackageName in .project java_export_builder section.\[/code\]

Any suggestion will be appreciated.

Thanks.

Francesco

---

**keithbrown** · January 11, 2016 at 4:57 pm

Hi Francesco,

BridgePoint does not yet include a general purpose Java Model Compiler. The one you see in the chooser is a hook for the custom Java model compiler (called MC-Java) we use to build BridgePoint itself. MC-Java has some special tweaks the only make it suitable for building BridgePoint, but is an example of what could be possible should someone be interested in creating a general-purpose Java MC.

If you are interested, the source code for MC-Java is available alongside the source for the BridgePoint plug-ins in github.com/xtuml/bridgepoint.

Regards,
Keith
