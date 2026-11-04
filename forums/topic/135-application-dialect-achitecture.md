---
redirect_from:
  - "/community/topic/135-application-dialect-achitecture/"

layout: "topic"
title: "1,3,5 Application, Dialect Achitecture"
date: "2018-11-20"
permalink: "/forums/topic/135-application-dialect-achitecture/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**cort** · November 20, 2018 at 6:17 pm

1,3,5+ Application, Dialects, Architectures
Posted on November 13, 2018
Shlaer-Mellor modeling has always claimed to provide Platform Independent Models (PIMs) that can be translated with platform specific software architectures. The theory is sound…, but tangible, touchable, downloadable examples can be hard to find.

Several teams of engineers have successfully re-deployed applications onto different targets, and teams have reused their software architectures (model compilers) on multiple applications. However, the teams using these techniques work inside commercial and mil-aero engineering organizations that are not free to share their models openly.

The GPS Watch example model has served as an open source example of BridgePoint xtUML with OAL action language for about a decade. In its original form it runs interpretively and translates into C, C++ and SystemC. For many reasons GPS is a nice subject matter to study. It is used in a variety of applications and industries and is familiar to all. Everyone loves GPS.

GPS Watch now comes in multiple dialects of action language (OAL and MASL) and is translated onto multiple architectures… from the tiny Arduino (2k of RAM) to the Raspberry Pi and to larger distributed Linux architectures.

Look for more dialects and architecture options coming soon!
