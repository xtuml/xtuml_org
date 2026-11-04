---
redirect_from:
  - "/community/topic/kde-and-eclipse/"

layout: "topic"
title: "KDE and eclipse"
date: "2014-11-20"
permalink: "/forums/topic/kde-and-eclipse/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Travis London** · November 20, 2014 at 3:16 pm

Just in-case any others hit this problem…

If you use KDE and run eclipse it may crash randomly when using the GTK Oxygen theme. If you go to Configure Desktop \> Application Appearance \> GTK and change the theme from oxygen-gtk to any other it should no longer crash.

---

**Travis London** · November 20, 2014 at 3:42 pm

Additionally I had to add this to /eclipse/eclipse.ini

-Dorg.eclipse.swt.browser.DefaultType=mozilla

Otherwise the crashes would occur anytime eclipse attempted to access the browser.

---

**Travis London** · November 20, 2014 at 3:49 pm

Actually it appears you can leave the oxygen-gtk theme, as long as you set the default browser type.

Note the system here is openSUSE 13.1
