---
redirect_from:
  - "/community/topic/changing-the-xtuml-editor-model-parts/"

layout: "topic"
title: "Changing the xtUML Editor model parts"
date: "2014-04-23"
permalink: "/forums/topic/changing-the-xtuml-editor-model-parts/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**poj** · April 23, 2014 at 8:56 pm

As a nice little project to get started in understanding I’ve been spending the night looking at adding a small feature to the xtUML Editor, solving a problem that have been irritating me.
If you have different editors opened to a piece of model with the same name (eg. two Operations in two Classes with the same name) it is very hard to know which editor is showing which part of the model. Looking around, I realized that this feature was available for editors showing packages, where the tooltip shows the model path.

So, I looked at the com.mentor.nucleus.bp.ui.graphics.editor.ModelEditor, and the introspection performed in com.mentor.nucleus.bp.ui.graphics.editor.GraphicsEditor, in getTitleToolTip(), where a Getpath(String) method is invoked on the object being edited, if such a method is available.

An equivalent introspection seems to be possible to perform in the text editors also, but that would requiring adding a Getpath operation to a number of the classes in Ooaofooa. Performing such changes in the generated source code may be possible to test the theory that this is working, but it is not a good solution for actually performing these kinds of small usability improvements to the xtUML editor.

When is a solution expected to be available, that makes it possible to actually perform improvements that needs to touch the modeled parts?

---

**Bob Mulvey** · April 24, 2014 at 12:06 pm

Hi,

What you should do is raise an issue for the particular issue you are solving. You do this in Git Issues here: [https://github.com/xtuml/editor/issues](https://github.com/xtuml/editor/issues)

Then, create a branch for your work. We suggest you include the issue number in the branch name. as follows:
\_

Right now what you should do is perform the work, and include comments in your checkins to the branch as you would in any development cycle. You can push the changes into your branch in the origin/master repository any time you wish.

With git, when you include \# in the comments to your branch it puts it into the issue’s comments on checkin. Of course you can also go directly to he issue and add comments/questions. When the work is ready, issue a pull request on the branch. The admins will service the pull request to put the feature into an upcoming release. Questions can also be asked/answered directly in the git issue that you raise.

With regard to the question of being able to generate code from changes made to the meta-model… That is coming in the future, we are working on it. As an example issue I went ahead and created an issue for this topic: [https://github.com/xtuml/editor/issues/15](https://github.com/xtuml/editor/issues/15) Please add to it as you see fit.

I left it to you to create an issue/branch for the particular changes you are making right now. Good luck!

---

**Bob Mulvey** · April 24, 2014 at 12:08 pm

Whoops, the previous comment thought I supplied html tags…
It should read, We suggest you include the issue number in the branch name. as follows: ” git issue “\_” short description “

---

**poj** · April 25, 2014 at 4:41 am

I’ve raised an issue on the actual editor problem, [https://github.com/xtuml/editor/issues/17](https://github.com/xtuml/editor/issues/17)
