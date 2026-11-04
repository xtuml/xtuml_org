---
redirect_from:
  - "/community/topic/persistent-crash-on-macos/"

layout: "topic"
title: "Persistent crash on MacOS"
date: "2018-05-17"
permalink: "/forums/topic/persistent-crash-on-macos/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**bgat** · May 17, 2018 at 3:43 pm

Guys:

Bridgepoint is aborting on MacOS whenever I do a second build of a project. The first build attempt always seems to go fine, but when I do a subsequent clean/build, I get the following crash report. The problem is repeatable with the GPS watch example. Suggestions welcome!

Process: bridgepoint \[6463\]
Path: /private/var/folders/\*/BridgePoint.app/Contents/MacOS/bridgepoint
Identifier: org.xtuml.bp.product
Version: 6.13.0 (6.13.0.201805112044)
Code Type: X86-64 (Native)
Parent Process: ??? \[1\]
Responsible: bridgepoint \[6463\]
User ID: 501

Date/Time: 2018-05-17 10:28:42.446 -0500
OS Version: Mac OS X 10.13.4 (17E202)
Report Version: 12
Bridge OS Version: 3.0 (14Y664)
Anonymous UUID: BD071D08-481B-89DF-D2EB-CCE5AEA5A43B

Time Awake Since Boot: 59000 seconds

System Integrity Protection: enabled

Notes: Translocated Process

Crashed Thread: 0 Dispatch queue: com.apple.main-thread

Exception Type: EXC_BAD_ACCESS (SIGABRT)
Exception Codes: KERN_INVALID_ADDRESS at 0x000000015098cd78
Exception Note: EXC_CORPSE_NOTIFY

VM Regions Near 0x15098cd78:
mapped file 000000014944e000-0000000149918000 \[ 4904K\] r–/r-x SM=ALI
–\>
VM_ALLOCATE 00000006c0000000-00000006c7c00000 \[124.0M\] rw-/rwx SM=PRV

Application Specific Information:
CGBlt_copyBytes: buffer check:

abort() called

Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0 libsystem_kernel.dylib 0x00007fff79391b6e \_\_pthread_kill + 10
1 libsystem_pthread.dylib 0x00007fff7955c080 pthread_kill + 333
2 libsystem_c.dylib 0x00007fff792ed1ae abort + 127
3 libjvm.dylib 0x0000000108cd629f os::abort(bool) + 25
4 libjvm.dylib 0x0000000108dfd3de VMError::report_and_die() + 2304
5 libjvm.dylib 0x0000000108cd7eca JVM_handle_bsd_signal + 1131
6 libjvm.dylib 0x0000000108cd412f signalHandler(int, \_\_siginfo\*, void\*) + 47
7 libsystem_platform.dylib 0x00007fff7954ff5a \_sigtramp + 26
8 ??? 0x00000001007040e0 0 + 4302323936
9 com.apple.CoreGraphics 0x00007fff5136df15 CGBlt_copyBytes + 101
10 com.apple.CoreGraphics 0x00007fff5136f7fb argb32_image + 4999
11 com.apple.CoreGraphics 0x00007fff516da901 ripl_Mark + 22
12 com.apple.CoreGraphics 0x00007fff516d6d11 RIPLayerBltImage + 1035
13 com.apple.CoreGraphics 0x00007fff514400c7 ripc_RenderImage + 228
14 com.apple.CoreGraphics 0x00007fff514416eb ripc_DrawImage + 856
15 com.apple.CoreGraphics 0x00007fff513aa400 CGContextDelegateDrawImage + 41
16 com.apple.AppKit 0x00007fff4e656f43 \_\_backing_store_DrawImage_block_invoke + 70
17 com.apple.AppKit 0x00007fff4e653275 backing_store_delegate + 962
18 com.apple.AppKit 0x00007fff4e94d6aa backing_store_DrawImage.llvm.2667B97D + 514
19 com.apple.CoreGraphics 0x00007fff513aa400 CGContextDelegateDrawImage + 41
20 com.apple.AppKit 0x00007fff4e94e544 backing_store_DrawWindowContents.llvm.2667B97D + 1197
21 com.apple.CoreGraphics 0x00007fff513b3b1d CGContextDelegateDrawWindowContents + 59
22 com.apple.SkyLight 0x00007fff732539b4 SLContextCopyWindowContentsToRect + 178
23 com.apple.AppKit 0x00007fff4e82e987 \_NSRenderImageFromWindow + 1454
24 com.apple.AppKit 0x00007fff4e82e3b9 \_NXScroll + 451
25 com.apple.AppKit 0x00007fff4eddc7ba NSCopyBitsFromGraphicsContext + 312
26 com.apple.AppKit 0x00007fff4eddc67c NSCopyBits + 58
27 libswt-pi-cocoa-4530.jnilib 0x0000000127fa7ed9 Java_org_eclipse_swt_internal_cocoa_OS_NSCopyBits + 187
28 ??? 0x00000001098099f4 0 + 4454390260
29 ??? 0x000000010c572e54 0 + 4502007380
30 ??? 0x00000001097fa2bd 0 + 4454326973
31 ??? 0x00000001097fa2bd 0 + 4454326973
32 ??? 0x00000001097fa302 0 + 4454327042
33 ??? 0x00000001097fa2bd 0 + 4454326973
34 ??? 0x000000010aa7fc24 0 + 4473748516
35 ??? 0x000000010c580174 0 + 4502061428

---

**keithbrown** · May 17, 2018 at 4:08 pm

Hello.

I just did a lot of builds in a row. I saw the issue happen one time near the beginning. After the crash I restarted BP, deleted all the “Debug\*” folders from under the project, and built OK. I then did the same delete and re-build with out error several times. Then I stopped deleting Debug/ and rebuilt several times without issue.

Can you try deleting Debug\*/ and rebuild and see if that helps you?

Your stack trace looks like what I saw. Though not particularly helpful I’m afraid.

regards,
Keith

---

**bgat** · May 17, 2018 at 5:42 pm

That does seem to stop the crashing. Thanks!

---

**bgat** · May 17, 2018 at 9:16 pm

Correction: it stopped the crashes for just one build/clean/build cycle.

So, the problem is still there… Any other ideas?

---

**keithbrown** · May 18, 2018 at 2:41 pm

I don’t have any more ideas at this time. When I deleted Debug/ every time before a build and never crashed it made me think the CDT for some reason didn’t like the old .o files sitting around.

If any new ideas come to mind I will let you know.

---

**cort** · May 18, 2018 at 4:43 pm

I would experiment with separating the model compiler build and the CDT build.

Turn off the CDT build and just generate the code. (right-click Properties -\> Builders) If there is no crash, then it would point to the CDT. Also, you can build from the MacOS command line.

Assuming you narrow the problem down to the CDT, you can begin changing some of the build parameters in CDT. For example, build a Release build rather than a Debug build.

---

**Lee Riemenschneider** · May 18, 2018 at 5:34 pm

This might be related to some of the eclipse Mars issues.
[https://bugs.eclipse.org/bugs/show_bug.cgi?id=527171](https://bugs.eclipse.org/bugs/show_bug.cgi?id=527171)

---

**Lee Riemenschneider** · May 18, 2018 at 5:48 pm

You might also try increasing the JVM memory. At my work, we had to change the heap settings to:
-Xms512m
-Xmx2048m
in eclipse.ini on a CDT project. Eclipse was catching and reporting this to us on Windows.

I had BridgePoint crash on me this morning with an out of stack issue after a lot of cut and pasting on Linux. (I think it was stack and not heap.) I seem to remember someone also talking about setting -Xss1m (-Xss512k is the default) for either BridgePoint or our work eclipse.

---

**bgat** · May 21, 2018 at 9:45 pm

Yep, that bug \#527171 looks just like me. :-(

But if I’m reading this properties pane right, I’m running a version of Eclipse that has the fix.

What version of Eclipse is shipping with the daily Bridgepoint builds?

---

**bgat** · May 21, 2018 at 10:09 pm

On second glance, looks like Bridgepoint ships with Eclipse 4.5, which might still be affected by that bug.

How do I update to the latest Eclipse?

---

**keithbrown** · May 22, 2018 at 2:40 am

Yes, BridgePoint ships with Eclipse Mars (4.5). The development team has considered a move to Eclipse Oxygen (along with a simultaneous update to Java 9), but that is not an official project yet. From a high level, the project will include building the BP plugins in an Oxygen development environment, rinse and repeat until the build is clean. Then run all Junit tests and fix problems until those are clean again. Then update the build packaging so that it packages Oxygen instead of Mars. And run testing on Mac, Linux, and Windows.

When we’ve made an eclipse migration in the past, it has not been terribly challenging, but it does take some time and of course we don’t want to have degraded functionality in the process, so we must test thoroughly.

---

**keithbrown** · May 22, 2018 at 2:52 am

As far as workarounds go:

1\) I would not recommend dumping the org.xtuml.\* features and plugins into an Oxygen installation. I cannot say what level of functionality you would get. It may kind of work, but the behavior is completely undefined.

2\) The problem seems to be localized to CDT and the core platform CDT integration. You could work around by not using CDT in Eclipse Mars. This is not an ideal solution, but you could have one workspace that you run Eclipse Mars (BridgePoint) against. This is where you do your modeling. On the project builders, just run Pre-build and Model Compiler, but \_do not\_ run the C builder or Scanner Config builder. Then have an Eclipse Oxygen with CDT but no BP. Have another workspace and import the same project. Thus, both projects point to the same files on disk. After you run the BP build chain, you switch over to the Oxygen workspace, refresh the project to pick up changes, and build and edit the C files.

---

**cort** · May 29, 2018 at 7:26 pm

Is there an update on this?
Did any work-arounds succeed?
I am especially curious to know whether a later version of CDT worked correctly.
Cort

---

**bgat** · May 29, 2018 at 7:35 pm

My “workaround” was to switch to running Bridgepoint on Linux, which seems to be working ok for now.

I didn’t try a later version of the CDT, because I’m barely an Eclipse \*user\*. Hacking around under the hood is way beyond my skillset right now.
