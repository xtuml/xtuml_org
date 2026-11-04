---
redirect_from:
  - "/community/topic/bp-4-2-0-for-linux-unable-to-translate/"

layout: "topic"
title: "BP 4.2.0 for linux: Unable to translate"
date: "2014-12-09"
permalink: "/forums/topic/bp-4-2-0-for-linux-unable-to-translate/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**cley95** · December 9, 2014 at 2:35 am

Hello, I’m new to BP and encountered a problem when compiling the models.

The BP version is the latest 4.2.0 for Linux.,OS is Ubuntu 12.04 LTD, and the project is the demo MicrowaveOven.

When i use ‘build project’ to generate the c codes, following error occurred.

xtumlmc_build -home /home/cley/MentorGraphics/BridgePoint-420/eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.mc.c.binary_4.2.0/ -l3b -e -d code_generation -O ../../src/
Upgrading translation workspace: code_generation
/home/cley/MentorGraphics/BridgePoint-420/eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.mc.c.binary_4.2.0//mc3020/bin/mcmc: 1: /home/cley/MentorGraphics/BridgePoint-420/eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.mc.c.binary_4.2.0//mc3020/bin/mcmc: Syntax error: “(” unexpected
NOTE: Domain code 0 allocated for this import.
NOTE: The domain code you have entered has already been used/allocated, but will allow this import to proceed normally.
sys.arc: 1: INFO: starting Tue Dec 9 03:20:13 2014
sys.arc: 10: INFO: No data found. The exported model file appears to be empty.
\sys.arc: 11: ERROR: Exit with exit code = 100 as result of .EXIT Statement.\</span\>
Code generation complete.

Does anyone know this problem? Many thanks.

---

**keithbrown** · December 9, 2014 at 4:47 pm

Code translation & compilation is working OK for me on Ubuntu 14.04 LTS. Perhaps this is a configuration issue.

Make sure you’ve ran:
\$ sudo apt-get install libstdc++5
\$ sudo apt-get install g++

Also, open the directory where mcmc lives and run ls -al. Let us know if anything differs from mine:
\[code title=””\]
kbrown@XPS-L322X:/opt/xtuml/BP420/eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.mc.c.binary_4.2.0/mc3020/bin\$ ls -al
total 16760
drwxr-xr-x 2 kbrown kbrown 4096 Nov 21 10:54 .
drwxr-xr-x 4 kbrown kbrown 4096 Nov 21 10:54 ..
-rwxr-xr-x 1 kbrown kbrown 2068480 Nov 13 18:38 gen_erate.exe
-rwxr-xr-x 1 kbrown kbrown 45056 Nov 13 18:38 libTRANS.dll
-rwxr-xr-x 1 kbrown kbrown 1386475 Nov 13 18:38 mcmc
-rwxr-xr-x 1 kbrown kbrown 1240702 Nov 13 18:38 mcmc.exe
-rw-rw-r– 1 kbrown kbrown 1499756 Nov 21 10:54 mgc.pkginfo
-rw-rw-r– 1 kbrown kbrown 1811840 Nov 21 10:54 MGLS.DLL
-rw-rw-r– 1 kbrown kbrown 57344 Nov 21 10:54 msvcirt.dll
-rw-rw-r– 1 kbrown kbrown 413696 Nov 21 10:54 msvcp60.dll
-rwxr-xr-x 1 kbrown kbrown 343040 Nov 21 10:54 msvcrt.dll
-rwxr-xr-x 1 kbrown kbrown 214 Nov 13 18:38 README.md
-rwxr-xr-x 1 kbrown kbrown 3303936 Nov 13 18:38 vgal8c.dll
-rwxr-xr-x 1 kbrown kbrown 486010 Nov 13 18:38 vgalaxy8.vr
-rwxr-xr-x 1 kbrown kbrown 54981 Nov 13 18:38 xtumlmc_build
-rwxrwxr-x 1 kbrown kbrown 53413 Nov 21 10:54 xtumlmc_build.exe
-rw-rw-r– 1 kbrown kbrown 4365720 Nov 21 10:54 xtumlmc_build.exe.win
\[/code\]

Keith

---

**cley95** · December 10, 2014 at 6:37 am

Hello, Thanks for the reply.
I already installed the libstdc++5 and g++. And below is the list of my directory. I can’t see any difference.
\[code title=”list”\]
cd /home/cley/MentorGraphics/BridgePoint-420/eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.mc.c.binary_4.2.0/mc3020/bin/
ls -al

total 16764
drwxr-xr-x 2 cley cley 4096 Dec 10 07:28 .
drwxr-xr-x 4 cley cley 4096 Dec 9 02:53 ..
-rw-rw-r– 1 cley cley 1153 Dec 10 07:28 1.txt
-rwxr-xr-x 1 cley cley 2068480 Nov 14 00:38 gen_erate.exe
-rwxr-xr-x 1 cley cley 45056 Nov 14 00:38 libTRANS.dll
-rwxr-xr-x 1 cley cley 1386475 Nov 14 00:38 mcmc
-rwxr-xr-x 1 cley cley 1240702 Nov 14 00:38 mcmc.exe
-rw-rw-r– 1 cley cley 1499756 Dec 9 02:54 mgc.pkginfo
-rw-rw-r– 1 cley cley 1811840 Dec 9 02:54 MGLS.DLL
-rw-rw-r– 1 cley cley 57344 Dec 9 02:54 msvcirt.dll
-rw-rw-r– 1 cley cley 413696 Dec 9 02:54 msvcp60.dll
-rwxr-xr-x 1 cley cley 343040 Dec 9 02:54 msvcrt.dll
-rwxr-xr-x 1 cley cley 214 Nov 14 00:38 README.md
-rwxr-xr-x 1 cley cley 3303936 Nov 14 00:38 vgal8c.dll
-rwxr-xr-x 1 cley cley 486010 Nov 14 00:38 vgalaxy8.vr
-rwxr-xr-x 1 cley cley 54981 Nov 14 00:38 xtumlmc_build
-rwxrwxr-x 1 cley cley 53413 Dec 9 02:54 xtumlmc_build.exe
-rw-rw-r– 1 cley cley 4365720 Dec 9 02:54 xtumlmc_build.exe.win

file \*

gen_erate.exe: PE32 executable (console) Intel 80386, for MS Windows
libTRANS.dll: PE32 executable (DLL) (GUI) Intel 80386, for MS Windows
mcmc: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.9, not stripped
mcmc.exe: PE32 executable (console) Intel 80386, for MS Windows
mgc.pkginfo: data
MGLS.DLL: PE32 executable (DLL) (GUI) Intel 80386, for MS Windows
msvcirt.dll: PE32 executable (DLL) (console) Intel 80386, for MS Windows
msvcp60.dll: PE32 executable (DLL) (GUI) Intel 80386, for MS Windows
msvcrt.dll: PE32 executable (DLL) (GUI) Intel 80386, for MS Windows
README.md: ASCII English text
vgal8c.dll: PE32 executable (DLL) (GUI) Intel 80386, for MS Windows
vgalaxy8.vr: data
xtumlmc_build: a /usr/bin/perl15 script, ASCII text executable, with CRLF line terminators
xtumlmc_build.exe: a /usr/bin/perl script, ASCII text executable
xtumlmc_build.exe.win: PE32 executable (console) Intel 80386 (stripped to external PDB), for MS Windows

\[/code\]

I also notice that the xtumlmc_build is with dos ending format and tried to convert it to unix format. The translation error still exists.
Any idea?

---

**keithbrown** · December 10, 2014 at 2:23 pm

– Open the folder ~/mgc/install.ixl/LOGS, ls -al to look at the dates, open the file that corresponds to the time when you installed BridgePoint 4.2.0. Then go down to the “Starting post-install” section and see if there are any errors reported.

– Create a new xtUML project with some simple internals: add a package with a component inside. Add a package inside the component, and a class inside the inner package. Add an operation with simply OAL that just increments a transient variable. Build the new project. Does it experience the same problem?

---

**cley95** · December 11, 2014 at 2:57 am

There is no error in the post-install section of log file.

I tried creating a simple xtUML project as you described. There is still the problem.
\[code title=””\]home/cley/MentorGraphics/BridgePoint-420/eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.mc.c.binary_4.2.0//mc3020/bin/mcmc: 1: /home/cley/MentorGraphics/BridgePoint-420/eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.mc.c.binary_4.2.0//mc3020/bin/mcmc: Syntax error: “(” unexpected
\[/code\]
It seems the problem comes from the executable mcmc.

After checking again, now I probably know where the problem is, but haven’t verified my thought yet.
From my previous post,
\[code title=””\]mcmc: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.9, not stripped \[/code\]
The mcmc is a 64-bit executable. But my OS is a 32-bit Ubuntu (Sorry for forgetting to state this in my inital post). That may be the syntax error came from.

I download the installation package from [BridgePoint for Liunx](https://s3.amazonaws.com/xtuml-installers/BridgePoint_v4.2.0.ixl). There is no any clue of that it is for 32 or 64-bit system. :(

- This reply was modified 11 years, 2 months ago by [![](https://secure.gravatar.com/avatar/195e2ddd047695325d913f4b4e217b5e518f966f024d1f42d3e879a0eccc5c37?s=14&amp;d=mm&amp;r=g)cley95]({{ '/user/cley95/' | relative_url }}).

---

**cley95** · December 12, 2014 at 8:25 am

Update.

When I tried to install the bp4.2 in a 64-bit Ubuntu, I suddenly found the installer `BridgPoint_v4.2.0.ixl` itself is a ELF 32-bit LSB executable. So it should be targeted for 32-bit system.

But why is the file `eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.mc.c.binary_4.2.0//mc3020/bin/mcmc` a 64-bit executable? Right now I’m confused.

Does anyone know the root cause of my failure?

---

**keithbrown** · December 12, 2014 at 4:56 pm

The BridgePoint installers and the eclipse they include have been historically distributed as 32 bit applications in an attempt to provide the widest capability of usage. It appears that the mcmc was built without specifing the 32 bit flag to gcc.

However, the vast majority of users run 64 bit systems, so they never saw an error. It appears that you are the first to try to run on a 32 bit linux OS. At least, you are the first to report the problem.

Are you able to run a build successfully on your 64 bit Ubuntu? Do you intend to stick with it or do you want to go back to 32 bit Ubuntu?

---

**cort** · December 14, 2014 at 10:05 pm

Dear cley95,
I will plan to compile mcmc as a 32-bit executable and post a link to it. It may be a day or two before I can do this.
Thank you for the feedback.
Note, you can raise issues in the BridgePoint issue tracker. You can find a link to the issue tracker on the developer page ([developers]({{ '/participate/developers/' | relative_url }})). \[Note, to raise an issue requires you create an ID on the issue tracking system.\]
Regards,
Cort

---

**cley95** · December 15, 2014 at 4:39 am

Thank you very much.
I would still prefer to use my original 32 bit OS. So I’m glad to hear that a 32-bit mcmc would be provided. Looking forward the update.
Best regards.

---

**cort** · April 7, 2015 at 4:37 pm

The updated MC is available… including 32-bit mcmc.

See here: [download]({{ '/download/' | relative_url }})
