---
redirect_from:
  - "/community/topic/what-does-nothing-to-verify-mean/"

layout: "topic"
title: "What does \"Nothing to verify.\" mean?"
date: "2015-05-14"
permalink: "/forums/topic/what-does-nothing-to-verify-mean/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Lee Riemenschneider** · May 14, 2015 at 1:59 am

Encountered this when running some test models tonight. The models had some errors, which I thought was the problem, but it turns out that fixing those errors didn’t solve the problem. The problem turned out to be that the packages containing the classes weren’t contained inside a component. Lesson learned.

---

**Bob Mulvey** · May 14, 2015 at 2:37 pm

Hi Lee,

The common things that come to mind for me are:
– the selected element is not being parsed (perhaps an error in the OAL),
– there is no OAL in the launch configuration being made,
– there is some other error in the selected launch configuration.

---

**Lee Riemenschneider** · May 14, 2015 at 3:24 pm

As my post stated, the solution was to put the packages in a component, if this isn’t the expected behavior, then I need to issue a bug report. Also if the Verifier was expected to launch, then the start of this test sequence doesn’t make sense.

Launch verifier
Open root Package ‘model’
select all packages on the canvas
Mouse action \> Cut
Draw new Component on the same canvas
Name it “Comp”
Open “Comp” component diagram
Mouse action \> Paste (previously cut packages)
Select “Comp” in model explorer
Mouse action \> Launch Verifier
Execute Functions Package::test

---

**Lee Riemenschneider** · May 14, 2015 at 3:27 pm

BTW, the model I’m referencing is the InstanceReferenceArray model in the models repository under the test directory.

---

**Bob Mulvey** · May 14, 2015 at 5:15 pm

Thanks Lee. I raised issue [https://support.onefact.net/redmine/issues/7668](https://support.onefact.net/redmine/issues/7668) to have this information put in the FAQ ([https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/FAQ.md](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/FAQ.md)), and I went ahead and did it. There is a pull request open now so it will be there soon.

- This reply was modified 10 years, 9 months ago by [![](https://secure.gravatar.com/avatar/ea6d2e68d9e24480faf46673da88124c2c221ff2d8107d66a7a34d3548928a08?s=14&amp;d=mm&amp;r=g)Bob Mulvey]({{ '/user/rmulvey/' | relative_url }}).

---

**Travis London** · May 14, 2015 at 5:18 pm

The FAQ document has been updated to include a verifier section. The changes include information that guides in what to look for when you hit this problem.

---

**JamesB007** · June 24, 2016 at 10:09 pm

Is it usual to get this message in debug for an executable that runs successfully in the system editor? That’s what I’m getting.

I run the executable but just when it gets interesting the console closes and I can’t see what the last things that happened were.

So then I try to run it in debug and get the “Nothing to Verify” message. I’m confused as to why it should be able to run in one but not the other. I would have expected that if I’m getting this message it’s because the code can’t run and that it would run in neither. Is this because I’m not understanding the difference between running a program in the system editor and in debug?

I’d like to see what’s happening at the end of my executable code before the console gets taken away. What can I do?

---

**keithbrown** · June 28, 2016 at 1:14 pm

There is a bug in Verifier that manifests as sporadic “Nothing to verify” messages when launching an application model. It seems to be related to incomplete cleanup of a previous execution.

Oftentimes launching a different model will clear it up, or restarting BridgePoint.

In any case, you should be able to set a breakpoint in the model being executed to inspect data at any point you wish.

---

**JamesB007** · June 28, 2016 at 2:40 pm

I’m still getting the “Nothing to Verify” message as soon as I try to run the model in debug mode so I don’t see anything being executed. When I run the executable in the system editor, it only runs up to the point where declarations and assignments are made (in the equivalent of the “defineOven” function). Anything I’ve written into the equivalent of “TestSequences” isn’t showing in the console, although it was a few days ago and all I’ve been working on changing was the “ARCH shutdown” procedure.

My classes are all declared in a package that is inside a component.

- This reply was modified 9 years, 7 months ago by [![](https://secure.gravatar.com/avatar/7cec857bd3f60c7a46298fa12b953743b118dc7f10b79aacb45a622d2468b9bc?s=14&amp;d=mm&amp;r=g)JamesB007]({{ '/user/jamesb007/' | relative_url }}).

---

**JamesB007** · June 29, 2016 at 11:14 am

I tried to edit my previous message but maybe writing this new one is more helpful as it will bounce the thread.

I have a model which compiles without errors and which executes in the system editor. It completes but, after execution of the very last lines, the console closes and I can’t see all of the output in one single view.

I try to execute the model using verifier and I get the message, “Nothing to Verify”.

Whether this is an error in my model or a bug in verifier, I need a way to see the full output of the execution. I don’t know why I’m getting the “Nothing to Verity” message and I don’t know how to cause either a pause in the execution or to make the console remain active after execution has finished or to redirect the system editor output to a file.

Could you tell me what I need to do to make any of these things happen so that I can see the output of the execution of my model, either in system output or the verifier?

---

**keithbrown** · July 1, 2016 at 4:11 am

To see the output when running the compiled executable, just open a command prompt/terminal window, navigate to the folder that contains the executable and run it there.

To pause execution in Verifier, set a breakpoint on any line of OAL.

I cannot say why you are getting “Nothing to verify”. Can you share the model?

Can you create the example MicrowaveOven and run it in Verifier?

---

**JamesB007** · July 1, 2016 at 2:23 pm

I can run the example Microwave Oven in Verifier (Does it ever run test sequence 2 or only test sequence 1?

I’m surprised that I can run my own project’s executable from a console but can’t run it in verifier. What is verifier meant to be doing? I presumed there was a direct relation between projects that would run in both verifier and as an exe (or wouldn’t run in either).

I will seek permission to share the model with you. In advance, can you tell me how I would do that?
THank you for the instruction on running the .exe from the command prompt. I at least got one of the things I really needed by doing that.

- This reply was modified 9 years, 7 months ago by [![](https://secure.gravatar.com/avatar/7cec857bd3f60c7a46298fa12b953743b118dc7f10b79aacb45a622d2468b9bc?s=14&amp;d=mm&amp;r=g)JamesB007]({{ '/user/jamesb007/' | relative_url }}).

---

**cort** · July 1, 2016 at 4:21 pm

@JamesB, Do this:
from the ‘xtUML Debugging’ perspective
Run -\> Debug Configurations…
double-click ‘xtUML Execute Application’
In the Models pane select the correct component (or component reference)
Check ‘Log model execution activity’
Check ‘Run deterministicly’
Press ‘Debug’

Let me know if this works.

---

**JamesB007** · July 8, 2016 at 10:14 am

[@Cort]({{ '/user/cort/' | relative_url }}), I tried that. It was what I was doing anyway but I still get the same “Nothing to verify” message. I’m still asking for permission to share the model.

I’m also still awaiting instructions from anyone on the forum who can tell me how I share the model.

---

**Lee Riemenschneider** · July 8, 2016 at 11:36 am

To share the model, select the project and File-\>Export, choose xtUML Model, make sure right model is selected, give it a destination name and select Finish.

---

**keithbrown** · January 14, 2019 at 10:15 pm

I was hitting this dialog continually on some new models and what I believe finally did the trick to get my past it was to open the Debug configuration for my model, expand the model tree to the point where I could see the components, then check and uncheck each component, hit the Apply button, then run the debug.
