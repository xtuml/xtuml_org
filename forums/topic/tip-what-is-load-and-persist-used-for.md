---
redirect_from:
  - "/community/topic/tip-what-is-load-and-persist-used-for/"

layout: "topic"
title: "TIP: What is \"Load and Persist\" used for?"
date: "2014-03-13"
permalink: "/forums/topic/tip-what-is-load-and-persist-used-for/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Bob Mulvey** · March 13, 2014 at 7:28 pm

Load and Persist is not really required but it can potentially speed model load time. During load, xtUML Editor performs needed conversions to account for meta-model changes that may have happened between versions. xtUML Editor makes these changes to the model that is loaded in memory, but it does not persist the changes until the model is modified. This is done so that when you launch the tool with a new version it doesn’t check out and dirty files for what would appear to be no apparent reason. What “Load and Persist” does is to force the entire model to load and then forces it all to be written to disk, thus dirtying all the model files. This persists any model changes that were done in memory only. This can potentially speed model load a bit in some cases (because during load the conversions don’t needed to be).

---

**cort** · March 13, 2014 at 7:55 pm

“Load and Persist” is found on the xtUML Editor project context menu. It loads a project and persists the model data to the latest (and greatest) version/format.
