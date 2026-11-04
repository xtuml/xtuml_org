---
redirect_from:
  - "/community/topic/arch-shutdown-problem/"

layout: "topic"
title: "ARCH Shutdown problem"
date: "2016-06-23"
permalink: "/forums/topic/arch-shutdown-problem/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**JamesB007** · June 23, 2016 at 3:49 pm

I’ve used the Microwave Oven sample project (version 4.2) as a template for another project also in 4.2 with binary ‘C’ compiler.

I get a warning – implicit declaration of function ‘ARCH_Shutdown’ – which is coming from a line of OAL in one of my state machines for test sequences.

I’ve used the same as in the microwave oven code, i.e.
//For code generation: terminate system once complete
Bridge ARCH::shutdown();

and I’ve used “Add Built-in External Entities” to create the entities, Architecture, Logging and Time

Is there something else I need to do or am I using the wrong syntax/commands to perform the shutdown?

---

**keithbrown** · June 23, 2016 at 5:51 pm

Does your src/ folder include ARCH_bridge.\[c\|h\]?

Does the file that has the generated call have \#include “ARCH_bridge.h” at the top?

You wrote ‘ARCH_Shutdown()’, but the generated call for that bridge OAL line should be ‘ARCH_shutdown()’? Is that a typo or an error?

---

**JamesB007** · June 24, 2016 at 9:22 am

In my modeling perspective, I have a top level component called Machine which contains the external entities. So, the generated .h and .c files are called Machine_ARCH_Bridge.\[c\|h\]
They are both in the src/ folder.

The generated call is ARCH_shutdown() inside a generated procedure in the .c file called Machine_ARCH_shutdown() which is declared as void in the .h file

The .c file has the line \#include “Machine_ARCH_bridge.h” at the top.

In the microwave oven sample project, the generated MicrowaveOven_ARCH_bridge.c code doesn’t call ARCH_shutdown() in the MicrowaveOven_ARCH_shutdown() procedure. It just has the return command.

I’m wondering why there is this difference? Do I need to mark something so that my project compiles differently?

---

**keithbrown** · June 24, 2016 at 4:13 pm

OK. I see what you mean.

The short answer is, remove the “control stop;” OAL from inside the ARCH::shutdown EE bridge. It isn’t needed and is causing the extra code to be generated into the C function \_after\_ the return statement.

The normal use case for an EE is to translate the model to get (for example Machine_ARCH_Bridge.c), then copy Machine_ARCH_Bridge.c to your project’s gen/ folder and edit the C functions to perform whatever code actions you want, then next time you translate, your Machine_ARCH_Bridge.c will be copied into the src/ folder and compiled with the rest of the generated application.

I’ve opened a bug ([https://support.onefact.net/issues/8543](https://support.onefact.net/issues/8543)) to capture the original issue you raised.

---

**JamesB007** · June 24, 2016 at 8:42 pm

I’ve removed the OAL code “control stop” from the shutdown bridge but I’m still getting this line of code generated in the Machine_ARCH_bridge.c file

void
Machine_ARCH_shutdown()
{
Escher_run_flag = false; /\* default automatic action for this bridge \*/
return;
/\* Replace/Insert your implementation code here… \*/
/\* CONTROL \*/
XTUML_OAL_STMT_TRACE( 1, “CONTROL” );
ARCH_shutdown();
}

Is there anything else I can do to make sure that the program will stop. I can run it in the system editor warning even with the warning but after the initialization assignments, the program hangs and I have to break out manually.

---

**keithbrown** · June 28, 2016 at 1:27 pm

It sure looks like that file did not get regenerated. The 3 lines starting with /\* CONTROL \*/ are the generated code for the “control stop” OAL.

The prior line to set the run flag to false will cause the application to stop. That flag controls the event processing loop (just grep the code to see where it is used). When it goes false, event processing will stop and the application will exit.

---

**JamesB007** · June 28, 2016 at 2:35 pm

I’ve come back to this today, after shutting down my machine over the weekend, and the file has successfully regenerated without the extra three lines of code. I can only put that down it working because I turned it off and on again.
The model compiles with no errors or warnings and will run in the system editor, but hangs half way through execution. I think this is for an unrelated reason and I have addressed this in the “Nothing to Verify” thread.
