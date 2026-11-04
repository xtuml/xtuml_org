---
redirect_from:
  - "/community/topic/can-i-force-a-project-to-be-read-only/"

layout: "topic"
title: "Can I force a project to be read-only?"
date: "2013-07-10"
permalink: "/forums/topic/can-i-force-a-project-to-be-read-only/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**rrice** · July 10, 2013 at 3:13 pm

I have a project that I’d like to share with other team members, but I only want to give them read access and not allow them to modify the model. Is there any way that I can create a read-only project to share with my team? Or is there a special “viewer” mode I can use for the xtUML Editor?

---

**cort** · July 12, 2013 at 1:03 am

One good approach is to keep your project in configuration management (git, Subversion, ClearCase, etc.). The xtUML Editor integrates nicely with these systems. You can then allow read-only checkout (no “push” authority).

Another possibility is to allow a user to access a project (Import the project) from a file system to which they do not have write access. (For example, allowing them to import a project that exists in your home directory (on Unix) where they have only read access. This works, too.

Note that there is no specific “view-only” mode for the xtUML Editor. It might be a nice feature to add some day.

:)
