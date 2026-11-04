---
redirect_from:
  - "/community/topic/trouble-activating-bp-on-big-sur-again/"

layout: "topic"
title: "Trouble activating BP on Big Sur - Again!!"
date: "2021-06-09"
permalink: "/forums/topic/trouble-activating-bp-on-big-sur-again/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Clive** · June 9, 2021 at 7:03 am

A few months ago the solution for overcoming the dreaded message -“Bridgepoint.app” is damaged and can’t be opened. You should move to to the Bin – I had to always activate it from the command line, making sure that the JAVA_HOME environment variable was set. I have another Mac running Big Sur 11.4 onto which I migrated a working version of BP 7. Making sure that the bridgepoint.ini file was the same and that JAVA_HOME was set, I tried to activate BP but received the dreaded message above.
In frustration I downloaded the latest version of BP 7, and installed it (using command line instructions) but nothing changed. The dreaded message was again displayed.
I had BP 7 working on both Big Sur 11.2.3 and Mojave 10.14.
Any clues?

---

**cort** · June 9, 2021 at 7:44 am

This article looks promising. Updating your mac and the xattr change seem like maybe a fit.

> [How to Fix App “is damaged and can’t be opened. You should move it to the Trash” Error on Mac](https://osxdaily.com/2019/02/13/fix-app-damaged-cant-be-opened-trash-error-mac/)

---

**Clive** · June 10, 2021 at 1:07 am

Thank you for the tip Cort,
Before trying out the xattr command I spent some undesired effort discovering a problem with the ‘export’ command in zsh on Big Sur 11.4 when setting environment variables What happens is that while a terminal is open (using zsh) the ‘export’ command seems to work because after doing an export if you echo the environment variable or simply type ‘env’ the appropriate values are reflected. However, if you open a new terminal window or tab and type ‘env’ nothing of the environment variable(s) set in the earlier window exists. If you close the window where the environment variable(s) were set those settings are lost. This doesn’t seem to happen for bash and it doesn’t seem to happen on at least Big Sur 11.2.3.

So a couple of hours were spent with Apple Support ‘proving’ that I was right. Their recommendation to do a restoration installation didn’t change the situation.

Thus I am now using only bash for terminal instances, but whilst I can set up (say) JAVA_HOME OK and have the value remain live between terminal sessions, it seems that setting the PATH variable is problematic.

Anyway, I did (finally) tryout the xattr -cr option (and also looked at one or two other of it’s options. After running it and then activating BP-7 from a bash terminal everything started up OK. However the following message did pop up:

SLF4J: Failed to load class “org.slf4j.impl.StaticLoggerBinder”.
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See [http://www.slf4j.org/codes.html#StaticLoggerBinder](http://www.slf4j.org/codes.html#StaticLoggerBinder) for further details.

I haven’t looked into this yet, but you are very likely to be able to decipher the implications more readily.

Thanks again!

Clive.

---

**cort** · June 10, 2021 at 8:00 am

Hi Clive,

‘export’ should behave the same between bash and zsh. In both cases it will not persist. Environment variables exist in your shell and any child shells. Once the parent goes away, so do the env vars.
You need to edit .bashrc or .zshrc and set them there. These files initialize the shell when the shell opens.

The error messages you see when BridgePoint starts are benign and come from the underlying Eclipse logging facility.

Cheers,
Cort

---

**Clive** · June 10, 2021 at 7:52 pm

Of course you are right – it’s in the Unix manual (which I hadn’t checked before I contacted Apple)! Odd that they didn’t point out the ‘proper ‘behaviour of ‘export’!?
However, undergoing the same procedure for setting up a set of terminals in bash and zsh, I can consistently obtain the result I mentioned. Whether I am doing something strange, or whether bash and zsh exhibit different properties in MacOS to other implementations or indeed whether it’s down to Terminal preferences, is not clear to me.
Over the years of using MacOS, I have never found this problem of ‘forgetting’ environment variables – thus I have been lulled into thinking it’s the norm. Maybe this is a result of rarely turning off my computer and also setting restoration of apps etc. to restart when there is a crash/shutdown.
Anyway, it seems that one way or another there is an inconsistency in behavior between bash and zsh in Big Sur.

So far BP is operating quite well on the Big Sur platform!

Regards.

Clive.
