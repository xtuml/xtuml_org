---
redirect_from:
  - "/community/topic/xtuml-git-classes-with-attribute-amnesia-how-to-restore/"

layout: "topic"
title: "xtuml + git = Classes with attribute amnesia. How to restore."
date: "2013-10-30"
permalink: "/forums/topic/xtuml-git-classes-with-attribute-amnesia-how-to-restore/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**sfinnie** · October 30, 2013 at 10:03 pm

Lest anyone have the same palpitations I had today, a story with a happy ending…

TL;DR is: there seems to be way for the editor to get out of sync with the underlying .xtuml files. This can happen if, for example, you use git for version control, create a branch and then revert to master.

The result is: the model can appear to lose attributes for classes on a diagram.
The solution is: close the model editing canvas, refresh the project & re-open the editor canvas.

That’s it. If anyone has a better explanation/solution I’d be grateful if you’d post. Thanks.

And now the full story…

I spent several hours modelling, assiduously checking into git at regular intervals. Wanted to do some refactoring so created a branch after making sure everything was committed. Tried changes on the branch but they didn’t work. Thought “oh well, that’s what branches are for” and switched back to master. Opened up the model and… approx one third of classes had lost all attributes. Cue palpitations.

Looked at the underlying .xtuml files and they still seemed to include the missing attributes. Selected the model in Model Explorer & did a ‘refresh’ – at which point all classes disappeared from diagram, leaving only relationships. Had a few more palpitations then closed the model canvas.

Re-opened the canvas and, joy of joys, all restored. Large sigh of relief.

---

**keithbrown** · October 31, 2013 at 12:58 pm

Thank you for pointing out the workaround you found.

What version of EGit are you using? The next version of xtUML Editor will include EGit 2.3. If you are not on 2.3, I suggest you upgrade to that version now (Use “Help \> Install New Software…” and point at this p2 repository: [http://download.eclipse.org/egit/updates-2.3](http://download.eclipse.org/egit/updates-2.3)).

Regards,
Keith

---

**sfinnie** · October 31, 2013 at 3:32 pm

Hi Keith

I don’t use EGit, I use msysgit on the command line (v1.8.4), Windows XP.

– S.

---

**cort** · November 4, 2013 at 2:51 pm

Scott,

You point out a general issue. It is possible to get the memory model in xtUML out of sync with the persisted files. There are a few ways to do this. All of them involve “changing the files out from under the editor”. You can accomplish this with git, SVN, vi and notepad. :)

In the field we see this mostly in the same way you did. Different CM systems (and even different packagings of the same CM system) follow differing conventions with regard to change sets. You happened to run into git’s conventions on keeping “superset” files around when switching branches from your command line.

I recommend maintaining the faith in your CM system. And we recommend git, because of its popularity, growing adoption and distributed nature. Just expect a few more heart palpitations over the weeks/months of learning the subtleties. I in right where you are.

Kind Regards,
Cort

---

**sfinnie** · November 4, 2013 at 3:05 pm

Hi Cort, thanks for the post. Will trust git to “do the right thing” and believe…!

– S.
