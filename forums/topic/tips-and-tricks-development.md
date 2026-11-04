---
redirect_from:
  - "/community/topic/tips-and-tricks-development/"

layout: "topic"
title: "Tips and Tricks (Development)"
date: "2015-02-04"
permalink: "/forums/topic/tips-and-tricks-development/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**Travis London** · February 4, 2015 at 8:20 pm

This topic will host various tips and tricks when developing xtUML. These can include all processes through development. They can include tips and tricks about the other tools used to build xtUML.

- This topic was modified 10 years, 9 months ago by [![](https://secure.gravatar.com/avatar/ea6d2e68d9e24480faf46673da88124c2c221ff2d8107d66a7a34d3548928a08?s=14&amp;d=mm&amp;r=g)Bob Mulvey]({{ '/user/rmulvey/' | relative_url }}).

---

**Travis London** · February 4, 2015 at 8:24 pm

When working with unit tests in the xtUML editor certain Windows 7 settings must be configured. These are:

\_- Configure Windows Vista or Windows 7 for unit test running
– Bring up the Windows Color and Appearance settings
– Right click on the desktop background and select Personalize
– In Vista select the Windows Color and Appearance hyperlink
– In Windows 7 select the Windows Color hyperlink
– In the window that appears, change the following attributes:
– Active Title Bar Size: 25 Font: Trebuchet 10
– Border Padding Size: 0
– Caption Buttons Size: 25
– Icon Size: 32 Font: Tahoma 8
– Inactive Title Bar Size: 25 Font: Trebuchet 10
– Menu Size: 19 Font: Tahoma 8
– Message Box Font: Tahoma 8
– Palette Title Size: 17 Font: Tahoma 8
– Selected Items Size: 19 Font: Tahoma 8
– Tooltip Font: Tahoma 8
– If you have a smaller screen or resolution potential you may need to
configure the start menu to not always be on top, or set it to auto-hide.
– Note: Do NOT use the Windows setting that scaling text to make it easier to see.
This setting, in Windows 7, is found here:
Personalize \> Display \> “Make it easier to read what is on your machine”
That setting must be set to “smaller” 100%

Without these settings the expected results will not match up.

Once you have configured these you will see an Unsaved theme in the Windows configuration area. Here you can right click and then save the theme to BridgePoint Tests. This will easily allow you to switch to these settings only when running the tests.

---

**Travis London** · February 4, 2015 at 8:33 pm

Java templates.

– Go to Window \> Preferences
– Navigate to Java \> Editor \> Templates
– Click the New… button
– Give the template a name
– Select it’s Context type (for instance Java)
– Give it a description
– Enter the java code you want auto-completion for
– Click OK
– In the Preferences window click Apply and OK

Now while in a java editor you can use control space, type the start of the template name, and find the name of your template (Also you can hit control space twice to see only templates). Hitting enter will apply the code block.

---

**Bob Mulvey** · March 31, 2015 at 1:19 pm

When getting started as a BridgePoint developer, use this Developer’s Getting Started document:
[https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/Developer%20Getting%20Started%20Guide.md](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/Developer%20Getting%20Started%20Guide.md)
