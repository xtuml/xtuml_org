---
redirect_from:
  - "/community/topic/xtuml-editor-installation-on-various-platforms/"

layout: "topic"
title: "xtUML Editor Installation on Various Platforms"
date: "2013-02-07"
permalink: "/forums/topic/xtuml-editor-installation-on-various-platforms/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**cort** · February 7, 2013 at 10:54 pm

See notes on Ubuntu installation in “How to install xtUML Editor on Ubuntu”

In this topic we can paste in help for other distros…

Here is some info on Linux Mint (originally posted in LinkedIn – Executable UML):

Having some issues installing linux version, would appreciate any pointers; thanks. Here’s what I’ve done so far:

1\. chmod +x the downloaded .ixl file
2. tried to run: got “no such file or directory”
3. discovered download is a 32 bit exe; I have 64 linux install (linux mint 14)
4. ran ‘sudo apt-get install ia32-libs’
5. re-ran download, which ran & created a new dir ~/mgc/install.ixl (had to manually kill this after the copy message)
6. ‘cd ~/mgc/install.ixl’
7. ‘./install’
8. GUI launcher runs however it says it “no sources found”
9. tried navigating through the various sub dirs, but nothing found. There’s a ‘data’ subdir which seems the most likely; it contains 2 files (installData.xml.gz & mgc.pkginfo). However the installer doesn’t seem to recognise it.

Thanks for any suggestions.
…..
One problem I encountered installing on Ubuntu was that /bin/sh was actually linked to dash rather than bash, like rhel expects, which caused the install to not complete. Changing the symbolic link to bash and rerunning the install fixed the problem.
…..
thanks for the suggestion. Made the change and noticed that the installer hadn’t hung, it had opened the gui installer which was minimised on the task bar. Restored that and install completed OK.

(Thanks to the original posters.)

---

**keithbrown** · March 6, 2013 at 8:55 pm

Added a [FAQ item]({{ '/faqs/' | relative_url }}) that directs users to this page (and potentially other forum discussions).
