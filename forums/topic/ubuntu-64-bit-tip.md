---
redirect_from:
  - "/community/topic/ubuntu-64-bit-tip/"

layout: "topic"
title: "Ubuntu 64-bit tip"
date: "2013-12-06"
permalink: "/forums/topic/ubuntu-64-bit-tip/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Lee Riemenschneider** · December 6, 2013 at 3:15 am

Ran into a problem reinstalling 3.7.2 on 64-bit Ubuntu 13.x with libXtst.6.so. To get around this, install the aforementioned library with:

sudo apt-get install libxtst6:i386

---

**Lee Riemenschneider** · March 3, 2014 at 1:20 am

After messing up my Ubuntu install, I couldn’t find a way to get the installer working again until I ran across a tip to install the following:
sudo apt-get install libgtk2.0-0:i386 libpangox-1.0-0:i386 libpangoxft-1.0-0:i386 libidn11:i386 libglu1-mesa:i386

This is supposedly the path to installing the ia32-libs i386 after Ubuntu 13.10.

---

**Lee Riemenschneider** · March 3, 2015 at 2:42 am

Here’s what it took to get BridgePoint to start on 64-bit Gnome-Ubuntu 14.10:
sudo apt-get install libgtk2.0-0:i386
sudo apt-get install libxtst6:i386
sudo apt-get install gtk2-engines-pixbuf:i386
sudo apt-get install gtk2-engines-murrine:i386
