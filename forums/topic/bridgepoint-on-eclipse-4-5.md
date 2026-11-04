---
redirect_from:
  - "/community/topic/bridgepoint-on-eclipse-4-5/"

layout: "topic"
title: "BridgePoint on Eclipse 4.5"
date: "2015-10-26"
permalink: "/forums/topic/bridgepoint-on-eclipse-4-5/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**keithbrown** · October 26, 2015 at 6:29 pm

We recently promoted code changes to github:xtuml/bridgepoint master branch for eclipse 4.5 support as well as replacing Luna with Mars.1 in github:xtuml/packaging.

These changes have been built and packaged by our build server into an official build that is now available for testing. Please consider this a alpha-level release candidate. It is available at [download]({{ '/download/' | relative_url }}) in the Nightly Builds section.

I have smoke tested model browsing and model translation+compilation. Verifier is known not to work at this time.

This build includes eclipse 4.5 (mars.1), Papyrus-RT 0.7, JRE 8, CDT 8, ANTLR 2.7.6, and the latest BridgePoint 5.1.x development branch.

BridgePoint developers must switch to this build for any new development branches based on master going forward.

---

**cort** · October 26, 2015 at 6:36 pm

I have downloaded and am editing some models (for a paper I am writing). It is running and looks/feels good so far.

---

**keithbrown** · November 11, 2015 at 9:49 pm

A new nightly build has been posted on the Download page here on xtuml-org.hustlefish-sites.com. This new version includes a working Verifier.
