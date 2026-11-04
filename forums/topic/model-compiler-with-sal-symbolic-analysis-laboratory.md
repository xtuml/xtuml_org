---
redirect_from:
  - "/community/topic/model-compiler-with-sal-symbolic-analysis-laboratory/"

layout: "topic"
title: "Model Compiler with SAL (Symbolic Analysis Laboratory)"
date: "2015-08-12"
permalink: "/forums/topic/model-compiler-with-sal-symbolic-analysis-laboratory/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**moerafaat** · August 12, 2015 at 5:16 pm

Dear All,
Our team is working on developing a model compiler for [SAL (Symbolic Analysis Laboratory)](http://sal.csl.sri.com/). We have followed the video tutorial series available on the website as well as the documentation available for BridgePoint and the Object Action Language. We have managed to create a relatively detailed system model featuring an Elevator system. We have also gone through the verification and testing process. Now we want to implement the model compiler for SAL. SAL is a very powerful verification tool that is used to check the correctness and completeness of a system by validating the predefined theorems for the model. Adding this feature to BridgePoint is going to be very beneficial since it will allow the users to not only compile to a language of their preference, but will now allow them to compile to a language that can automatically verify the correctness of their models without going through the hassle of write detailed test benches for the system and validating them manually. All they need to do is provide the theorems upon which the model will be evaluated. We are looking for a good start point from which we can acquire enough knowledge to implement the custom model compiler. Any ideas?

---

**benjo123** · August 12, 2015 at 5:49 pm

Hi,

Have you seen video on YouTube about Customizing a Model Compiler ([https://www.youtube.com/watch?v=EonNPFltfAI](https://www.youtube.com/watch?v=EonNPFltfAI))?

In the Help Contents of BridgePoint there is a book called BridgePoint Model Compiler – User’s Guide, that may contain useful information.

Kind regards,
Ben

---

**keithbrown** · August 12, 2015 at 8:18 pm

Hello moerafaat,

This sounds like an interesting project you are working on. The video and documentation that Ben pointed to are very useful starting points.

Now for some technical details….

a\) I will point out that the source code for the BridgePoint model compilers is now open source and is included with BridgePoint 5 Community Edition. You will find it under the various model compiler plug-ins in the mc3020/arc/ folders. So, for example, the source code for the C model compiler is under /BridgePoint/eclipse/plugins/org.xtuml.bp.mc.c.source_5./mc3020/arc/. When the build process begins, the specialized/sys.arc is processed first.

b\) Regarding that demo video, the spirit is correct but some of the details have changed in the 2+ years since the video was created. Instead of putting archetype code directly into system.mark, I would now recommend doing this:
1) Create a new file: /BridgePoint/eclipse/plugins/org.xtuml.bp.mc.c.source_5./mc3020/arc/specialized/myexample.arc , populate it with the archetype code from the examples, or with your own modifications
2) Edit sys.arc in the same folder, find “.include “\${arc_path}/t.smt.arc”” (around line 76). Insert a line after that includes your new file: .include “\${arc_path}/myexample.arc”
3) Modify your project to use the C source model compiler. Right-click on the project, then choose “BridgePoint Utilities \> Set Model Compiler”, use the wizard to choose the C Source MC.
4) Now when you build your project, the code in myexample.arc will be executed.

I think you will find that custom model compilers are awesome and extremely powerful! However, that also means they are non-trivial. Good luck!

Best,
Keith

---

**cort** · August 12, 2015 at 9:07 pm

\<commercial offering\>

If you need more help than can be provided in forums and live chat, One Fact offers training on building and modifying model compilers.

:)

\</commercial offering\>

- This reply was modified 10 years, 6 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).
- This reply was modified 10 years, 6 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).
- This reply was modified 10 years, 6 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).
- This reply was modified 10 years, 6 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).

---

**Ahmedagiza** · August 17, 2015 at 9:53 am

Hello,

I am working with moerafaat in the team, I have some inquires:

1- I have followed Keith’s instructions but it seems to ignore the source files, do I need to re-compile the model compiler first or it is compiled on the run? If yes, are there specific compilation instructions?

2- Do I have to modify the C Compiler? Can’t I have an entry for the new compiler instead of ruining an existing one?

3- Is there anything that describes the translation flow inside the files? I mean, I know the abstract steps, and I know that it starts in sys.arc, but I am asking about a guide of where the components are queried, the OAL is translated, the templates are used..etc?

Any other references, guides, tips are highly appreciated.

---

**cort** · August 17, 2015 at 12:40 pm

Dear Ahmedagiza,

Hello. Thank you for posting your questions.

1\. Let us trace this one down.
a) Be sure you are running the \_source\_ model compiler and not the binary model compiler. Do this by checking the top line of the model compiler console output.
b) Once you are sure you are running the source MC, modify sys.arc to do some print statements right at the beginning. Be sure you see the print statements.
c) Make sure you renamed mc3020/bin/mcmc (and mcmc.exe) so that mcmc is not running.

2\. You can easily change the C compiler settings. This is a CDT (Eclipse C Development Tools). It is not specific to BridgePoint. Start in the ‘Builders’ section under the project properties.

3\. There is a lot of information in the MC-3020 User Guide. After that, I recommend looking at the meta-model extensions (TE\_\* classes). After reviewing sys.arc, look at q.sys_populate.arc; it does most of the M2M transformations.

Kind Regards,
Cort

---

**Ahmedagiza** · August 18, 2015 at 10:05 am

Thanks for the usefule information!

But would you please elaborate what **mcmc** and **mcmc.exe** files are? I tried to remove them while building but it drained the memory and I got the following message (I have 8GB Memory):
\An error has occurred. The following chain of information is available:
error 1: /Memory/Alloc/
errno: 12: Not enough space
requested size: 409710931\</span\>

Also, can you please explain what is **Action Block Anchor** and what does the function **TE_ABA_rollup** do?

*Btw, we can point out the vague/difficult part of the tutorials/guide after we finish the project since we have been learning through tutorials from scratch, if that will be helpful for you and the community.*

Thanks again.

---

**keithbrown** · August 18, 2015 at 4:11 pm

mcmc (linux version) and mcmc.exe (windows version) is a tool that performs a first pass over the action language in the model and translates the OAL to C. Then, during a second pass the structural parts (components, classes, etc) of the model are translated. Using mcmc speeds up the translation process and reduces memory consumption of gen_erate.exe which is used during translation, but only if you are intending to translate to C.

If you look at the model compiler metamodel (available in the xtuml/mc repository on github) you’ll see that TE_ABA is related to all the action homes. TE_ABA_rollup takes all the translated instance data for a particular action and saves into the string “code” of TE_ABA. Once we translate the OAL to code and save it to this string, we can get rid of the instance data for that action as it is no longer needed.

Can you provide more information about the model you are using and how you have implemented your model compiler customizations?
