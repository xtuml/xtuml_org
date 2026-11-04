---
redirect_from:
  - "/community/topic/failed-to-run-bridgepoint-modeler-on-mac/"

layout: "topic"
title: "Failed to run BridgePoint Modeler on Mac"
date: "2019-09-27"
permalink: "/forums/topic/failed-to-run-bridgepoint-modeler-on-mac/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**Sean Kavanagh** · September 27, 2019 at 10:19 am

Hi All,

Since I’m having problems getting BridgePoint Developer to build on my Mac, I downloaded the BridgePoint Modeler and tried to run that. It starts up but reports multiple problems in Console:

> Errors occurred during the build.
> Errors running builder ‘Integrated External Tool Builder’ on project ‘org.xtuml.bp.ui.session’.
> Launch configuration type id “org.eclipse.ant.AntBuilderLaunchConfigurationType” does not exist.
> Possible causes:
> Missing specification of a launch type (missing plug-in)
> Incorrect launch configuration XML
> Launch configuration type id “org.eclipse.ant.AntBuilderLaunchConfigurationType” does not exist.
> Possible causes:
> Missing specification of a launch type (missing plug-in)
> Incorrect launch configuration XML

Any help would be appreciated.

Regards, Sean.

---

**Sean Kavanagh** · September 27, 2019 at 10:58 am

Note, xtUML Modeler does run but I’m not sure what functionality is broken because of build errors in console.

Regards, Sean.

---

**Lee Riemenschneider** · September 27, 2019 at 11:36 am

Bob Mulvey and I worked with Sean in the chat, and it turns out he was starting in the workspace he had previously created to build the developer version of BridgePoint. This is why the modeler version was trying to build something on launch. Sean created a new workspace and solved that issue.

I just looked at the example projects in the latest nightly (Build id: 2019-07-26 12:26), and they need to be modified to build them. Here are the steps:
(RMB means Right Mouse Button Click (opens the content menu))
(For GPS Watch, this only needs to be done to the GPS_Watch project)
1. Select the project and Open Project-\>Properties and choose Builders
2. Select (highlighted; don’t uncheck anything) the “Missing builder (org.xtuml.bp.mc.c.binary.export_builder)” and “Model Compiler” and Remove them
3. Apply and close
4. RMB the project and choose BridgePoint Utilities-\>Set Model Compilers
5. Select MC-3020 (C Model Compiler) for C/C++/SystemC, or MASL Exporter for MASL projects.
5.1 If MC-3020 select Next\> then choose the Target language. You don’t need to check the Convert … box
6. Select Finish
7. In Project-\>Properties, Builders, you should now see the model compiler you chose.

---

**Sean Kavanagh** · September 27, 2019 at 2:26 pm

Thanks to Lee and Bob for help on this topic.

Regards, Sean.
