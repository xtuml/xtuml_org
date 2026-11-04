---
redirect_from:
  - "/community/topic/configuration-management-of-eclipse-control-files/"

layout: "topic"
title: "Configuration Management of Eclipse control files"
date: "2018-08-07"
permalink: "/forums/topic/configuration-management-of-eclipse-control-files/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**John Wolfe** · August 7, 2018 at 6:57 pm

We are looking for advice on how best to manage Eclipse control files such as .project and .cproject. Our immediate problem involves .cproject.

We routinely build for three different targets:
Windows on x86
Linux on x86
Linux on ARM

We use a separate xtUML/Eclipse project for each configuration of our system. For example, we have a configuration in which the application component under test is directly wired to the test bench component, another in which several glue components are inserted between the application and the test bench, and yet another for the deployment configuration that includes the application and some glue, but no test bench.

Creating 2 or 3 target-platform-specific variants of each of these configuration projects for the sake of maintaining a version of .cproject for each platform is not particularly appealing, as it means maintaining three copies of the contents of /gen.

We plan to factor the glue code out of /gen into a separate project of its own, but that leaves the marking files, which tend to be coupled to the configuration but do not change with the target platform.
