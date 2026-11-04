---
redirect_from:
  - "/community/topic/a-note-about-bridgepoint-release-policy/"

layout: "topic"
title: "A Note About BridgePoint Release Policy"
date: "2015-11-06"
permalink: "/forums/topic/a-note-about-bridgepoint-release-policy/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**keithbrown** · November 6, 2015 at 7:41 pm

A Note About BridgePoint Release Policy

The BridgePoint development process is nearing the point where an official release will be made. One of the ramifications is that we’re down to making the hard choices of which issues will block the release and which ones must be pushed out. At the same time, we’re doing some cleanup on the way we’ve managed the versions inside Redmine for the past 6 months.

A bit of background. Our team’s policy is that any build we publish (nightly or official release) must be uniquely identifiable. Official releases have a version that is higher than a previous release. We’ve also adopted a policy over the past several years that nightly and engineering builds use .. while official releases use ..0 corresponding to ... We don’t use the revision field much, we generally just talk about . release numbers. Our BridgePoint build scripts modify the about.mappings files in some plugins with a timestamp every time a build is done. So, if you look at the “About” information inside eclipse, you will see, for example, “Version: 5.1.0, Build id: 201510231939”. This provides the unique identifier of each build as mentioned previously.

Using the July to December 2015 development cycle as an example, we released BridgePoint 5.0 around the middle of 2015. Immediately after the release we bumped the version number of the plugins to 5.1.0 and continued to do development and publish some community and nightly builds along the 5.1 version line. When we do the next official release of BridgePoint Pro around December 2015 it will be version 5.2.0. As soon as the release is done, we’ll bump the version again to 5.3.0 and resume development along the 5.3 line and the next official release of BridgePoint Pro should be 5.4.0 roughly six months later.

Now, for the cleanup in Redmine I mentioned. When we get near a release, we often do a roadmap shift and push issues down the roadmap so we can only keep release blockers on the current release list and move out any deemed not to be blockers to the next release. During the 5.1 development cycle, we actually had a “v5.1” version in Redmine that some issues were assigned to. These issues will be part of the 5.2 release so they are moved to that list. In the future we don’t plan to have . versions in the system.

We are still learning from the product’s move to open source, and will continue to do our best to improve. One of the things we’re learning is that our old way of assigning issues to the version roadmap is not nimble enough. Our intention going forward is to assign issues to the roadmap when there is an active xtUML community member working on the issue and targeting it to be done for the specific release, or if the community considers an issue critical to the future of the technology. We will be much more selective to assure the roadmap is adhered to. Additionally, we are evaluating a move of BridgePoint to the Eclipse Foundation which would provide more open source structure.

As we approach the anniversary of our first open source release we would like to thank everyone involved. We look forward to a bright future for the technology.
