---
redirect_from:
  - "/community/topic/xtumlbridgepoint-workflow/"

layout: "topic"
title: "xtuml/BridgePoint Workflow"
date: "2015-06-02"
permalink: "/forums/topic/xtumlbridgepoint-workflow/"
forum: "Miscellaneous"
forum_slug: "miscellaneous"
forum_url: "/forums/miscellaneous/"
---

**Bob Mulvey** · June 2, 2015 at 3:36 pm

This topic came up in the miscellanous chat room. I wanted to capture in a spot that is easy to find.

MeHeba, you had a question about “workflow” ?10:52am
..
back to workflow :)10:56am
how would things go around10:57am
MeSmile BTW, Keith the new forum is there now.10:57am
In the developer’s getting started guide, [https://github.com/xtu…de.md](https://github.com/xtu…de.md) , you will see that you must create a fork11:01am
Your work will now always be done in your own fork11:02am
We still suggest you use branches within your fork, so that you can easily have multiple projects going on, as you did when we working in branches against master. However, the branches are now in your fork11:03am
Other than that, process is quite similar to what it was when the team was with Mentor Graphics.11:04am
You pick an issue, or are assigned one (in your case)11:05am
make sure your fork is up to date with master11:05am
create a new branch \_11:06am
Write the appropriate development note and investigate11:06am
Review the note with us11:06am
compete the work in your fork11:06am
review again as needed (depending on issue size)11:07am
run tests11:07am
when ready for promotion you will create a pull request on your fork11:07am
Someone with permission to service that pull request will review and promote.11:08am
BTW, the issues status should be changed to “in progress” when you start working on it11:08am
When you issue the pull request, the status need to be changed to “resolved” to indicate that the issue is resolved, but not yet in master11:09am
The person that performs the final review/promotion will close the issue when they promote it11:09am
I think that is all. Did I leave anything out11:09am
?11:09am
HebaNope11:16am

---

**Bob Mulvey** · June 2, 2015 at 4:05 pm

When a commit message is made in git we use the following format:
job:#

There is a cron job that looks for the “job:#” in a message and, when found, sends the comment to the specified issue number in the issue tracking system. This serves as a means of requirements tracing. The issue in the issue tracking system ends-up holding links to every individual change that was made (and the comment associated with the change).

---

**Bob Mulvey** · June 2, 2015 at 4:09 pm

I must note here that the cron job only runs against the repositories git origin. This means, you will not see all your comments go into the issue until your fork’s branch is promoted.
