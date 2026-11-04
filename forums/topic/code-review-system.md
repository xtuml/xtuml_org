---
redirect_from:
  - "/community/topic/code-review-system/"

layout: "topic"
title: "Code review system"
date: "2015-05-22"
permalink: "/forums/topic/code-review-system/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**Travis London** · May 22, 2015 at 2:38 pm

I think it may be helpful to integrate with the Gerrit review system. I believe the latest eGit supports gerrit. If there are other code review tools that any of you know of it would be nice to hear. The one thing about Gerrit is that it is based on git.

---

**Bob Mulvey** · May 22, 2015 at 4:15 pm

How would this work in our process flow?

---

**Travis London** · May 22, 2015 at 4:35 pm

-ant
-dnt
-int
-post on gerrit that an issue is ready to be promoted
-tests pass
-reviewers (recommend at least two) check the changes
-issue is promoted by one of the reviewers

I do not know too much about Gerrit yet, but what I have seen follows this flow (aside from the documentation). Egit uses Gerrit, and I have followed a few issues. The system will not allow a promotion to master unless all reviewers agree and the tests have passed. You can also post reasons for a non-pass of review, then reset the state to require re-review.

---

**Travis London** · May 22, 2015 at 5:02 pm

I must add some comment to enable follow-up replies so here it is :)

---

**Erik Wedin** · May 24, 2015 at 7:17 am

Support for Gerrit sounds good. We are using it for source code in another project.
