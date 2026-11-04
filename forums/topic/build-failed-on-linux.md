---
redirect_from:
  - "/community/topic/build-failed-on-linux/"

layout: "topic"
title: "Build failed on Linux"
date: "2022-07-11"
permalink: "/forums/topic/build-failed-on-linux/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**kae-made** · July 11, 2022 at 10:21 pm

Hi, current BridgePoint build environment doesn’t work.

Now that I find the cause so I share it.
python command doesn’t exist in latest Debian and Ubuntu. The python command of them is not python but python3. So python command can’t be found during build then build error happens.
This problem is resolved by the following tips.

sudo mv /usr/bin/python3 /usr/bin/python.

By this, I’ve verified that the build runs to the end.
But created executable files are only for Linux and Mac.
I want it for Windows.
Please let me know how to create bridgepoint.exe file.

Regards,

---

**cort** · July 12, 2022 at 8:02 am

If you are getting both the Mac and Linux builds, you can also get the Windows build. This requires the Windows x86 cross-compiler installation of gcc.
