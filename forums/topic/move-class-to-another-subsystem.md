---
redirect_from:
  - "/community/topic/move-class-to-another-subsystem/"

layout: "topic"
title: "Move class to another subsystem?"
date: "2013-10-03"
permalink: "/forums/topic/move-class-to-another-subsystem/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**sfinnie** · October 3, 2013 at 1:24 pm

Hello, wonder if this is possible?

I have some classes in a subsystem (package) that I want to move into another. Is this possible without deleting/re-creating the classes?

Thanks.

---

**keithbrown** · October 4, 2013 at 8:22 pm

Yes. In either the Model Explorer tree view or on the graphical canvas, select the items you wish to move. Then right-click on one of the selected items. In the menu, choose “Cut” or “Copy” depending on if you want to move the items or duplicate the items. Next, right-click on the target package in the Model Explorer or on the target package’s graphical canvas and select “Paste” to complete the action (either move or duplicate).

---

**Martin** · November 1, 2013 at 2:39 pm

So that means that the cut and paste does not change any GUUID in the xtuml file?
Does this also means that it is a move of a file level also? Think about this as CM issue, you dont want to have a new file item being created.

---

**cort** · November 4, 2013 at 2:40 pm

In cut/copy/paste the UUIDs are re-calculated. Associations between semantic elements are reconnected as intelligently as feasible.

---

**Travis London** · November 4, 2013 at 3:36 pm

To be more specific, not all elements support reconnection (or a true move). Currently the following elements support referring element reconnection:

Datatype
Interface
Component
Interface Reference
Executable Property

So at this point cutting a class would cause any referring object to become unrelated. Imported classes would become unassigned.

On the file level it would not be a move at this point. There would be a new folder/file creation and a folder/file deletion.
