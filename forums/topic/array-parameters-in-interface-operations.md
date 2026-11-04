---
redirect_from:
  - "/community/topic/array-parameters-in-interface-operations/"

layout: "topic"
title: "Array Parameters in Interface Operations"
date: "2017-09-21"
permalink: "/forums/topic/array-parameters-in-interface-operations/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dennis Tubbs** · September 21, 2017 at 3:57 pm

Do interface operations support array parameters?

Thanks,
Dennis

---

**keithbrown** · September 21, 2017 at 6:18 pm

This is a known defect: [https://support.onefact.net/issues/9575](https://support.onefact.net/issues/9575)

There was a change a while back that disallowed changes (like rename and delete) inside interface references, requiring the change to be made inside the interface itself. I think it’s possible that the logic in that change isn’t quite right and had the adverse effect you are seeing.

---

**keithbrown** · September 21, 2017 at 6:19 pm

This is a known defect: [https://support.onefact.net/issues/9575](https://support.onefact.net/issues/9575)

There was a change a while back that disallowed changes (like rename and delete) inside interface references, requiring the change to be made inside the interface itself. I think it’s possible that the logic in that change isn’t quite right and had the adverse effect you are seeing.

---

**keithbrown** · September 21, 2017 at 6:19 pm

This is a known defect: [https://support.onefact.net/issues/9575](https://support.onefact.net/issues/9575)

There was a change a while back that disallowed changes (like rename and delete) inside interface references, requiring the change to be made inside the interface itself. I think it’s possible that the logic in that change isn’t quite right and had the adverse effect you are seeing.
