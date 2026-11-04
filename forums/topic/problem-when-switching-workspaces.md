---
redirect_from:
  - "/community/topic/problem-when-switching-workspaces/"

layout: "topic"
title: "Problem when switching workspaces"
date: "2019-08-07"
permalink: "/forums/topic/problem-when-switching-workspaces/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Clive** · August 7, 2019 at 11:30 am

I decided to create a second workspace. So I ended up with WS1 (original) and WS2 (additional) workspaces. I had been happily modeling in WS1 but wanted to switch to WS1 to add some tweaks. The first time I switched I closed down BP (which had WS2 open) and started up BP again and selected WS1. There seemed to be no issues/errors and the heading on the title bar of the BP window was correct, but there was nothing listed in the Model Explorer – not a thing. Also, the perspectives for xtUML models and debugging showed up in ‘fade’ mode. I’ve tried all sorts of things including importing xtuml models and switching workspaces while BP is open. NOTHING, including no errors! I can still open WS2.

Any clues? By the way, I checked the workspace contents and all seems to be in order in terms of structure and the various artefacts and components I had created.

---

**Lee Riemenschneider** · August 7, 2019 at 11:49 am

How did you go about creating WS2?

Where does the model for each WS reside?

Any clues in the workspace/.metadata/.log (or ,bak_0.log)?

---

**Bob Mulvey** · August 7, 2019 at 11:51 am

Hi Clive,
I suspect perhaps you used import existing project into workspace? The issue wouod be that you cant have more than 1 copy of the same model in a workspace. Eclipse has a lot of rope available to hang yourself :). The tool tries to watch for cases where multiple models with duplicate UUIDs are placed in the same workspace. If it sees this it will remove the xtuml nature from the duplicate project (2nd one added). With no xtuml nature there is no model to show in the xtuml perspective. It will warn you before it removes the nature though, you should have seen the warning if this is what happened.

I still dont think this explains every thing you wrote, but it sounds like it.

You could look at the error log view for more hints. Also, Im not sure what you mean by “fade mode”?

---

**Clive** · August 8, 2019 at 12:30 am

Gentlemen: Thanks for the feedback. I’ve done some delving into stuff in the .metadata files which I’ll report on shortly.

Lee: I created the second WS (WS2) from a fresh start of BP and chose a new directory at the same level as the existing ‘workspace’ (WS1). The new directory is not a sub-directory of ‘workspace'(WS1). The existing models for WS1 all resided in WS1. WS2 contained new models, not related to anything in WS1.

Looking into the .metadata directory for each of the workspaces WS1 and WS2 there are some obvious differences in the .log files in terms of normal operation and failed operation. It seems that normal operation inserts an !ENTRY log and nothing more. For a failed operation the .log file contains entries such as:

!ENTRY org.eclipse.ui 4 0 2019-08-07 20:42:29.310
!MESSAGE Unhandled event loop exception
!STACK 0
java.lang.ClassCastException: org.xtuml.bp.core.ui.tree.ModelCheckedTreeViewer should return an instance of ITreeSelection from its getSelection() method.

followed by a significant list of java references. This list ends with:

!SESSION 2019-08-07 20:43:31.522 ———————————————–
eclipse.buildId=unknown
java.version=1.8.0_212
java.vendor=Oracle Corporation
BootLoader constants: OS=macosx, ARCH=x86_64, WS=cocoa, NL=en_AU
Framework arguments: -keyring /Users/cliveboughton/.eclipse_keyring
Command-line arguments: -os macosx -ws cocoa -arch x86_64 -keyring /Users/cliveboughton/.eclipse_keyring

As an aside I could find the “.eclipse_keyring” file in my home directory.

Another aside is that I couldn’t find a way to access the error log file from BP – not in keeping with the Help manual. So all my searches were done from the command line outside of BP. There was nothing in the other files within the .metadata directory that suggested anything was wrong.

Is there a particular procedure or naming convention I should follow in creating new workspaces? To get around the problem I’m experiencing, should I simply create another workspace and transfer or import the WS1 files into?

Bob: I guess the equivalent of ‘fade’ for me is ‘greyed-out’ such as ‘greyed-out’ items in a menu suggesting that selection will cause no action.

Regards.

---

**John Wolfe** · August 8, 2019 at 6:27 pm

As for workspace conventions, I would suggest the following:
1. Place them on a local (not network, cloud, or other remote) filesystem.
2. Keep all workspaces outside of the BridgePoint installation directory.
3. Do not nest a workspace inside another workspace.
4. Keep the path names “short” and avoid spaces within the path name. (There was a time when Windows had issues with long path names and path names containing spaces, but I think those problems have been resolved.)
5. Use a configuration management system (I’d suggest Git unless you have a strong preference for another one) and commit coherent change sets frequently so that you are always in a position to delete your workspaces and create and populate new ones from the repository. Consider workspaces as temporary and rely on your CM repo as the primary source for your models.

---

**Clive** · August 9, 2019 at 4:51 am

PROBLEM SOLVED John asked several questions and ultimately asked me to send him a copy of my workspaces. I obliged!

The problem turned out to be a little peculiar. Somehow I had managed to select the ‘minimisation’ icon from the icon list that can be exposed on the extreme RHS of the BP/Eclipse window. This had the effect of hiding everything (including the Model Explorer pane and any open element tabs in the central window etc.) To get things back to normal John found that I needed to re-click the minimisation icon and then ‘unhide’ everything. I managed to do the latter by going to the ‘Show View’ option under ‘Window’.

Anyway, the good news is that I don’t have a workspace problem (after all). It had to be something strange that I did. Something I really don’t remember doing! I’m beginning to feel that I should have a continuous video monitoring every action I undertake. :-)

Again, thank you all for your willingness to help and advise. Much appreciated.

Regards.
