---
redirect_from:
  - "/community/topic/copy-paste-export-diagrams/"

layout: "topic"
title: "copy & paste / export diagrams?"
date: "2013-02-27"
permalink: "/forums/topic/copy-paste-export-diagrams/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**sfinnie** · February 27, 2013 at 10:40 am

Is there a way to get diagrams out the editor & into documents? Have tried the following:

– select all in editor, copy (Ctrl-C) and paste into doc. Pastes the SQL instead of diagrams.
– as above but paste special-\>bitmap. Copies lines only – no text
– File-\>Export: exports SQL only.

Thanks.

---

**cort** · February 27, 2013 at 4:50 pm

On Windows, you simply Copy (or control-c) when the canvas is selected. Do not select specific elements. This brings the image to the clipboard. It can then be pasted into graphics programs (MS Word, etc) in the normal way.

You are correct that SQL can also be copy pasted. It is the SQL that carries the important semantic information when pasting into another xtUML diagram. In this case, the xtUML copy/paste is not simply “dumb graphics” but is the meaning copy/paste of the model elements.

On Linux, I need to test it. IIRC, there may be specific hoops that need to be jumped through.

---

**sfinnie** · February 27, 2013 at 9:31 pm

Thanks Cort.
