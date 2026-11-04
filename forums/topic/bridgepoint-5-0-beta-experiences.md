---
redirect_from:
  - "/community/topic/bridgepoint-5-0-beta-experiences/"

layout: "topic"
title: "BridgePoint 5.0 (beta) experiences"
date: "2015-04-22"
permalink: "/forums/topic/bridgepoint-5-0-beta-experiences/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**cort** · April 22, 2015 at 11:14 am

Someone wrote: “Anyone else seen this error, “Unable to read workbench state. Workbench UI layout will be reset. java.lang.NullPointerException”, on opening a 4.2 workspace with 5.0?”

Someone else responded: “Yes. This is expected. A warning/expectation will be in the release notes. We may even recommend that the xtUML perspectives be closed on workspaces before upgrading. That would make a more graceful transition.”

---

**cort** · May 4, 2015 at 1:33 pm

The beta release of BridgePoint 5.0 is on the xtuml-org.hustlefish-sites.com download page now ([download]({{ '/download/' | relative_url }})). This is a “master” build (built from the master branch in the public github repositories). An official BridgePoint 5.0 will differ from this build in only minor ways (tweaks and bug fixes found in final testing).

---

**cort** · May 6, 2015 at 3:14 pm

[![](http://ictoblog.nl/files/WinZip_icon.png)](http://ictoblog.nl/files/WinZip_icon.png)

The new zipfile-based installation simplifies many things. Here are some of my experiences:
– Unzip the file anywhere and just run it.
– Unzip onto the host file system and then run it from a VM on that host files system.
– After “installation”, move the installation folder anywhere; it still works.
