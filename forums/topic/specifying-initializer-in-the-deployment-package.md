---
redirect_from:
  - "/community/topic/specifying-initializer-in-the-deployment-package/"

layout: "topic"
title: "Specifying Initializer in the Deployment Package"
date: "2016-12-07"
permalink: "/forums/topic/specifying-initializer-in-the-deployment-package/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Bruce** · December 7, 2016 at 6:46 pm

Version: 5.5
Tutorial: HOWTO Send Messages Between 2 xtUML Components
Issue: Specifying Initializer in the Deployment Package

Following the tutorial…
I am able to specify the initializer on the components package but in the deployment package the only choice is “None’

---

**Bruce** · December 8, 2016 at 2:19 pm

I found a manual workaround…

execute init on the client in the deployment package

---

**Bruce** · December 8, 2016 at 3:03 pm

In the tutorial the amp is the client.

amp = requirer = client
