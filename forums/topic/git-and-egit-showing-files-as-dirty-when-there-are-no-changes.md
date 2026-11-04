---
redirect_from:
  - "/community/topic/git-and-egit-showing-files-as-dirty-when-there-are-no-changes/"

layout: "topic"
title: "Git (and egit) showing files as dirty when there are no changes"
date: "2015-07-15"
permalink: "/forums/topic/git-and-egit-showing-files-as-dirty-when-there-are-no-changes/"
forum: "Miscellaneous"
forum_slug: "miscellaneous"
forum_url: "/forums/miscellaneous/"
---

**Bob Mulvey** · July 15, 2015 at 8:25 pm

This problem has been driving me crazy for quite a while. IT happens to me infrequently enough that I never spent time to look for what exactly was going on. In my case I am using a Ubunutu VM on a MAC. I have my repo(s) checked out such that I can share them across VMs (and the MAC OS iteself). I don’t tend to attenot to do cross-platform things though. For example, my git repos folders are named for the OS I use them in so I explicitly try to assure I do not hit cross platform persistence issues.

I found a thread that has an explanation for what is going on (explanation at the end of the thread), enjoy :) : [http://stackoverflow.com/questions/26542226/git-showing-identical-files-as-changed](http://stackoverflow.com/questions/26542226/git-showing-identical-files-as-changed)

---

**Travis London** · July 22, 2015 at 2:36 pm

Here is some github documentation for the issue:

[https://help.github.com/articles/dealing-with-line-endings/](https://help.github.com/articles/dealing-with-line-endings/)

There are multiple options, which can be per repository or global. They can also be configured such that all repositories cloned share the same settings.

---

**Bob Mulvey** · July 30, 2015 at 4:30 pm

I really think the proper thing to do is to put a .gitattibutes in place as called out in the article I linked to. Following those directions and doing a hard reset should change the CRLF to LF and then keep them that way from this point forward regardless of the environment being used.

---

**Bob Mulvey** · July 30, 2015 at 4:45 pm

This issue just bit me really hard AGAIN. I should have raised an issue earlier and did not. It is now issue [https://support.onefact.net/redmine/issues/7820](https://support.onefact.net/redmine/issues/7820)
