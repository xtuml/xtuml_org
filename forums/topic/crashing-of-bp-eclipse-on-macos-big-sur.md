---
redirect_from:
  - "/community/topic/crashing-of-bp-eclipse-on-macos-big-sur/"

layout: "topic"
title: "Crashing of BP/Eclipse on MacOS Big Sur"
date: "2021-07-07"
permalink: "/forums/topic/crashing-of-bp-eclipse-on-macos-big-sur/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Clive** · July 7, 2021 at 2:30 am

On odd occasions when using BP 7.1 (in the git perspective) my iMac crashes resulting in the black screen of oblivion. It takes a couple of minutes to restart. BP is not restarted after the reboot.
So I open a terminal and type in the command to start BP. Following is the text that appears in a separate terminal after restarting BP:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
cliveboughton@iMac Project_Monitor % eval “\$(ssh-agent -s)”
Agent pid 23427
cliveboughton@iMac Project_Monitor % less ~/.ssh/config
cliveboughton@iMac Project_Monitor % ssh-keygen -t ed25519 -C “clive@softimp.com.au”
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/cliveboughton/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/cliveboughton/.ssh/id_ed25519.
Your public key has been saved in /Users/cliveboughton/.ssh/id_ed25519.pub.
The key fingerprint is:
SHA256:C+Dg998rYWP8sbfD30Nle3h7ympidMrKC4sZp05BOqI [clive@softimp.com.au](mailto:clive@softimp.com.au)
The key’s randomart image is:
+–\[ED25519 256\]–+
\| \|
\| \|
\| . o \|
\| . = . o\|
\|. + + ..S oo\|
\|.. o o .\*.o . .oo\|
\|E o +o.\* \* ..o\|
\| . \* =..B =. +.\|
\| .= . ==o=o=+.+\|
+—-\[SHA256\]—–+
cliveboughton@iMac Project_Monitor % eval “\$(ssh-agent -s)”
Agent pid 23461
cliveboughton@iMac Project_Monitor % open ~/.ssh/config
cliveboughton@iMac Project_Monitor % ssh-add -K ~/.ssh/id_ed25519
Enter passphrase for /Users/cliveboughton/.ssh/id_ed25519:
Identity added: /Users/cliveboughton/.ssh/id_ed25519 (clive@softimp.com.au)
cliveboughton@iMac Project_Monitor % pbcopy \< ~/.ssh/id_ed25519.pub
cliveboughton@iMac Project_Monitor % pbcopy \< ~/.ssh/id_ed25519.pubpwd
zsh: no such file or directory: /Users/cliveboughton/.ssh/id_ed25519.pubpwd
cliveboughton@iMac Project_Monitor % pwd
/Users/cliveboughton/git/Project_Monitor
cliveboughton@iMac Project_Monitor % git status
On branch master
nothing to commit, working tree clean
cliveboughton@iMac Project_Monitor %
\[Restored 22 Jun 2021 at 10:32:52 am\]
Last login: Tue Jun 22 10:32:52 on ttys000
cliveboughton@iMac Project_Monitor %
\[Restored 6 Jul 2021 at 5:19:37 pm\]
Last login: Tue Jul 6 17:19:37 on ttys000
cliveboughton@iMac Project_Monitor % ls -al ~/.ssh/id_ed25519
-rw——- 1 cliveboughton staff 464 21 Jun 14:31 /Users/cliveboughton/.ssh/id_ed25519
cliveboughton@iMac Project_Monitor % ls -al ~/.ssh/id_ed25519
\[Restored 7 Jul 2021 at 4:09:56 pm\]
Last login: Wed Jul 7 16:09:56 on ttys001
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Previously I had manually generated an ssh-key for my github repository that used pretty much the same set of commands, except for the pbcopy to a a file with a .pubpwd extension. So, I suspect what’s going on is in addition to what I needed to do regarding an ssh-key for the github repository. Any advice or known fixes would be welcome.

In addition to the ssh-key generation, the dates & times of previous crashes can be seen at lines starting with \[Restored ………\]. So, what is shown looks like the contents of a log file for crashes.

I presume that what I’ve described may be down to Eclipse behaviour. However, (so far) it only happens when I’m perusing stuff in the Eclipse git (EGit) perspective within BP 7.1.

---

**Clive** · July 11, 2021 at 9:57 pm

Following on from the issue I first posted as “Crashing of BP/Eclipse on MacOS Big Sur”.
I did some further investigation by generating ssh keys manually (using the github instructions) and from BP/Eclipse. I only generated keys of type ‘id_rsa’ because Eclipse doesn’t seem to be able to generate keys of type ‘ed_25519’.

Both alternatives (of course) created a public and private key file with permissions 644 (-rw-r–r–). These permissions are the default (it seems) for all OSes (including MacOS Big Sur).

After copying the public key to my github repo (and adding a passphrase), I then used the command “ssh -T [git@github.com](mailto:git@github.com)” to test whether the ssh connection worked. It didn’t! The same sort of messages that I posted previously appeared again. The messages only disappeared once I set the permissions on the private key file to 400 (-r——–). It was only then that I was asked to enter the ssh passphrase that I created – which also worked OK.

The requirement to reduce permissions on the generated private key file is relevant to at least MacOS Big Sur and perhaps Catalina. This requirement was unnecessary for Mojave and its predecessors. It also seems unnecessary for the latest Linux, Unix and Windows systems.

I have not investigated whether there’s a way to provide specific permissions when using the ssh -keygen command or any other ssh command. At first glance there doesn’t seem to be such an option. Perhaps someone else more familiar with SSH can provide some advice. In the meantime, simply resetting the permissions on the private key file using chmod seems to work OK.

PS: Given the severity of the ‘crash’ it seems to me that Apple should be doing something quite different in the treatment of such exceptions. I will report this issue to them, but I doubt there’ll be any immediate response.
