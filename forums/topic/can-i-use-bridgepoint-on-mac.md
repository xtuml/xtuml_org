---
redirect_from:
  - "/community/topic/can-i-use-bridgepoint-on-mac/"

layout: "topic"
title: "Can I use BridgePoint on MAC?"
date: "2013-05-26"
permalink: "/forums/topic/can-i-use-bridgepoint-on-mac/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**TI** · May 26, 2013 at 12:34 am

Some potential customers asks this.
Can we use BridgePoint on Mac ?

---

**cort** · May 29, 2013 at 7:36 pm

The xtUML Editor and BridgePoint are tested on Linux and Windows.
The Verifier (eXecute) and model compilers will not run directly on Mac, yet.
The xtUML Editor is purely an Eclipse application, so it can run on Mac. But the installer does not run on Mac (so you must copy the plugins into your own Mac-installed Eclipse).

Your mileage may vary. :)

---

**cort** · May 29, 2013 at 8:23 pm

In addition, I have personal experience running BridgePoint on Mac using a Linux VM. Using X, you can make a very nice Mac experience.

1\) Install a Linux VM
2) Install XQuartz (X for Mac)
3) Start your Linux VM
4) Log in to your Linux VM using “ssh -Y username@linuxvmname”
5) Run the xtUML Editor Launcher

Now the xtUML Editor will run on the Mac desktop. The Linux VM desktop is not needed.
