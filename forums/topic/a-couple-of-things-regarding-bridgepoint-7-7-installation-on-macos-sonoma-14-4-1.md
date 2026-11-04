---
redirect_from:
  - "/community/topic/a-couple-of-things-regarding-bridgepoint-7-7-installation-on-macos-sonoma-14-4-1/"

layout: "topic"
title: "A couple of things regarding BridgePoint 7.7 installation on MacOS Sonoma 14.4.1"
date: "2024-04-15"
permalink: "/forums/topic/a-couple-of-things-regarding-bridgepoint-7-7-installation-on-macos-sonoma-14-4-1/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Clive** · April 15, 2024 at 1:55 am

In recently upgraded my MacOS from Monterey to Sonoma. All went well, so I decided to download BP7.7 after finding that BP7.5 seemed to work OK!
Downloading BP 7.7 on Sonoma is no problem. Installing it is/was a little tricky. Actually by following the instructions on the xtUML.org download page everything seems to install, but when attempting to open BP 7.7 a message pops up indicating that using version 11.0.11 JVM will not work. My immediate response was to install openjdk17 using the command “brew install openjdk17”. However during this latter installation another message popped up indicating that I needed to install the Apple Command Line Tools! Huh! I had installed them previously on Monterey, but the Sonoma directory structure is slightly different. So, I actually needed to upgrade to CommandLineTools 15.3 to be compatible with Sonoma. I did this via logon to Apple Developer and downloaded them as a .dmg file. (NOTE: the usual command of “xcode-select –install” didn’t seem to work).
After having downloaded and installed the CommandLineTools and then successfully downloaded and installed openjdk17 and then activating BP7.7, the same message concerning the JVM version was displayed. Whaatt!! However, looking closely at the instructions at the end of the opnejdk17 installation, I noticed an important link needed to be set:
“sudo ln -sfn /usr/local/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-17.jdk”. Once this was done, I was able to activate BP 7.7 on Sonoma with no apparent problems.
