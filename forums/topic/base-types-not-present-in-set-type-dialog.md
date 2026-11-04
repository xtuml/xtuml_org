---
redirect_from:
  - "/community/topic/base-types-not-present-in-set-type-dialog/"

layout: "topic"
title: "Base Types not present in Set Type dialog"
date: "2018-05-09"
permalink: "/forums/topic/base-types-not-present-in-set-type-dialog/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**Dennis Tubbs** · May 9, 2018 at 8:59 pm

I have one project that only shows the inst_ref and enumeration types in the Set Type dialog box. None of the base types, e.g. Int, Void, Real, String appear in the list. It appears to be a project level issue but I cannot find a setting.

Am I missing a setting or have a corrupt project? Any ideas on how I might fix it?

Thanks,
Dennis

---

**keithbrown** · May 10, 2018 at 2:25 am

That definitely sounds like a corrupt project to me. I suggest you create a new xtUML project, do a quick test (say add a package and a function and then run Set Return Type…) and make sure the type picker shows all the core types. If it does, then export your model from the first project and import it into the new project.

---

**Dennis Tubbs** · May 10, 2018 at 2:12 pm

Thanks Keith, that fixed it.

---

**cort** · May 14, 2018 at 7:31 pm

If anyone else sees similar behavior, it will be good to capture the scenario leading up to the problem. Maybe there is a bug to be removed. :)
