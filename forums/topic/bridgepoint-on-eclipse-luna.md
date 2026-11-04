---
redirect_from:
  - "/community/topic/bridgepoint-on-eclipse-luna/"

layout: "topic"
title: "BridgePoint on Eclipse Luna"
date: "2015-05-15"
permalink: "/forums/topic/bridgepoint-on-eclipse-luna/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Travis London** · May 15, 2015 at 3:14 pm

The BridgePoint tool will be moving to the latest eclipse base (4.x). The version the tool is moving to is the latest which is code named Luna.

The work required for this move is documented here:

[BridgePoint_Luna_Analysis](https://github.com/travislondon/bridgepoint/blob/master/doc-bridgepoint/notes/36_Update_eclipse_base/36_Update_eclipse_base.ant.md)

The analysis will be reviewed and likely modified but gives you a basic idea of the direction.

---

**Ádám Balogh** · May 18, 2015 at 11:38 am

Is it not worth to skip Luna and move directly to Mars which is expected to be released in June?

---

**cort** · May 18, 2015 at 1:09 pm

Hi Ádám,
This is the balancing act that needs to be done each time we move forward on Eclipse. We must balance advancement with stability. Stability is required by our production modeling customers.
We plan to guide the migration and plugin development to be as compatible as possible. And there is work toward an eclipse update site.
So, it is likely that BridgePoint will run and even support development in Mars after this initial move.
Do you have specific design input on Eclipse migration? (both in terms of usage and tool development) Also, is there specific functionality in Mars that you believe is important?
Cort

---

**Ádám Balogh** · May 18, 2015 at 1:17 pm

Hi Cort,

Nothing specific, but I know that a stable (in Eclipse terms :-) ) version of Mars is expected soon. Many things are promised there, but they are mainly EMF related which does not affect BridgePoint.

Ádám

---

**Travis London** · May 22, 2015 at 11:32 pm

Hello all,

I have updated the analysis note according to review minutes. This note still requires a re-review as major observations were observed. We will hold another review and get the note finalized. Then work can proceed.

Regards,
Travis London

---

**Bob Mulvey** · May 26, 2015 at 10:17 pm

Since this is an active development project there is some chat about this now. It is in the development chat: [{{ '/cometchat/modules/chatrooms/index.php/' | relative_url }})

---

**Bob Mulvey** · June 9, 2015 at 9:31 pm

The chat about this topic has been broken out from the main development chat. If you want to follow it, or join in, it is here: [{{ '/cometchat/modules/chatrooms/index.php/' | relative_url }})
