---
redirect_from:
  - "/community/topic/git-best-practices/"

layout: "topic"
title: "Git best practices"
date: "2013-08-07"
permalink: "/forums/topic/git-best-practices/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Bob Mulvey** · August 7, 2013 at 7:13 pm

git merge (egit vs git):
As someone who prefers GUIs to command-line in most cases, I tend to use egit over git. While I do still go to the command-line on occasion, I have found that most things I do can be done with egit. However, git merge is something I prefer to do from the command line. After a pull request is issued for a branch our process requires that the branch be merged and tested by someone other then the engineer that did the work. The github review and merge feature allows an issue to be quckly and easily merged and promoted when there are no conflicts, but it does NOT allow the change to be built and tested prior to the promotion, therefore process prevents it from being used in most cases. Instead, the promoter must merge the changes into their local repository, build, test, and then push the merged branch. In taking this approach, I would love to use egit to perform the merge. However, a needed feature seems to be missing. The feature is the ability to provide a message (a comment) with the merge. For this reason, I prefer to go to the command-line to perform the merge. Here are the steps I am taking:
\_- checkout master from github
(Git Repositories View \> Switch To \> branch)
or
git checkout
\_- merge the branch into master: git merge -m ” \# ”
The above causes the merge to be associated with the git issue tracking the change. The -m is what egit does not seem to allow.
\_- build and test the changes
\_- If the test passes then push the changes to github. If the test fails you can restore your local repository as follows: git reset —hard origin/master

---

**Bob Mulvey** · August 9, 2013 at 2:22 pm

Sharing your branch changes with colleagues:

To a quick code review and/or get input from colleagues you can take advantage of the pull request’s ability to show changes:
\_- Submit a pull request for your branch
If the branch is not really ready to be pulled, just put that information in the pull comment.
\_- Capture the link to the changed files (this is found in “Files Changed” tab of the pull request).
\_- Send the link to colleagues as needed
\_- When done, close the pull request
(Go to the bottom of the pull request page and select close)

- This reply was modified 12 years, 6 months ago by [![](https://secure.gravatar.com/avatar/ea6d2e68d9e24480faf46673da88124c2c221ff2d8107d66a7a34d3548928a08?s=14&amp;d=mm&amp;r=g)Bob Mulvey]({{ '/user/rmulvey/' | relative_url }}).
- This reply was modified 12 years, 6 months ago by [![](https://secure.gravatar.com/avatar/ea6d2e68d9e24480faf46673da88124c2c221ff2d8107d66a7a34d3548928a08?s=14&amp;d=mm&amp;r=g)Bob Mulvey]({{ '/user/rmulvey/' | relative_url }}).

---

**Bob Mulvey** · August 9, 2013 at 2:26 pm

Get a list of the file changed in your branch:

Our process requires that the list of files changed be included in a particular required process document. In other RCS system a utility was created to capture this information. In git you can do this:
\_- check out you branch
\_- \$ git diff –name-only origin/master

---

**Lee Riemenschneider** · August 13, 2013 at 2:56 am

I’ve been trying out R4E at work for reviews. It works pretty good for associating reviews with specific versions of code and tying them to a task. We’re using it with Subclipse, but it works with git (egit) as well.
