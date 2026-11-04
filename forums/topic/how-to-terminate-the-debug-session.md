---
redirect_from:
  - "/community/topic/how-to-terminate-the-debug-session/"

layout: "topic"
title: "How to terminate the debug session"
date: "2023-10-31"
permalink: "/forums/topic/how-to-terminate-the-debug-session/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Schmill** · October 31, 2023 at 12:03 am

Hello there,
I have a running session with elements that have red icon and they have state, but in the debug window there is nothing, it is blank.
I used to have a window that I can’t remember the name of, where I could right click a node in a tree and terminate the session in which the component is running.

Thank you.

---

**cort** · October 31, 2023 at 7:56 am

Could you post a screen shot?

---

**Schmill** · October 31, 2023 at 9:05 am

Here it is:
[![](https://i.ibb.co/KKrnJ6g/Screenshot-2023-10-31-160204.png)](https://ibb.co/LNZK3Sy)

Thank you.

---

**Schmill** · November 1, 2023 at 9:22 am

I think I found the error:
I had a disabled breakpoint for action/state that no longer exists. once removed, the verifier now works as expected.
