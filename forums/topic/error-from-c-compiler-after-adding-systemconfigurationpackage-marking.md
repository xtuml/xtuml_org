---
redirect_from:
  - "/community/topic/error-from-c-compiler-after-adding-systemconfigurationpackage-marking/"

layout: "topic"
title: "Error from C++ compiler after adding SystemConfigurationPackage marking"
date: "2015-08-30"
permalink: "/forums/topic/error-from-c-compiler-after-adding-systemconfigurationpackage-marking/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**sm4rpq** · August 30, 2015 at 9:17 pm

Hello!

I’m testing out the new free bridgepoint version. Lots of new things to discover and play with. Have been a BP user at work for around 10 years but the last few years have not offered any projects so my latest contact was with 1.5.2 and MC-2020.

Made a small model to check out some integration stuff without much luck. And while actually reading the documentation I saw that some markings should be added. But after adding

.invoke MarkSystemConfigurationPackage( “System” )

To system.mark I get a lot of error messages from the model compiler. Seems there are some bug in there. First one is a complaint about R4707 which I have checked and it does not exist in the metamodel. For complete listing of error messages see below.

Would I be better off trying to fetch a newer version from github?

I do need C++. Using the C model compiler is not an option. I will be doing some extensions and dynamic binding will be needed. I just have to re-learn everything as this is MC3020 and every change I have done previously was in MC2020 which looks quite different.

q.component.arc: 520: ERROR: Related Object Pair ‘CL_IIR’ and ‘CL_POR’ is not specified properly – either ‘R4707’ is not a relationship or the direction is incorrectly specified.
q.component.arc: 528: ERROR: Unable to find ‘cl_ic_provider’ on stack.
q.component.arc: 528: ERROR: NOT_EMPTY operator expects INST_REF or INST_REF_SET rvalue.
q.component.arc: 528: ERROR: Invalid operation.
q.component.arc: 417: ERROR: Attribute of selected object does not exist.
q.component.arc: 420: ERROR: Instance Reference Variable for Object ‘C_PO’ has cardinality 0.
q.component.arc: 420: ERROR: Object Attribute ‘Id’ Undefined.
q.component.arc: 279: ERROR: Instance Reference Variable for Object ‘TE_PO’ has cardinality 0.
q.component.arc: 279: ERROR: Attribute Not a valid attribute of object.
q.component.arc: 279: ERROR: First operand has invalid type.
q.component.arc: 279: ERROR: Invalid operation.
q.component.arc: 520: ERROR: Related Object Pair ‘CL_IIR’ and ‘CL_POR’ is not specified properly – either ‘R4707’ is not a relationship or the direction is incorrectly specified.
q.component.arc: 528: ERROR: Unable to find ‘cl_ic_provider’ on stack.
q.component.arc: 528: ERROR: NOT_EMPTY operator expects INST_REF or INST_REF_SET rvalue.
q.component.arc: 528: ERROR: Invalid operation.
q.component.arc: 417: ERROR: Attribute of selected object does not exist.
q.component.arc: 420: ERROR: Instance Reference Variable for Object ‘C_PO’ has cardinality 0.
q.component.arc: 420: ERROR: Object Attribute ‘Id’ Undefined.
q.component.arc: 279: ERROR: Instance Reference Variable for Object ‘TE_PO’ has cardinality 0.
q.component.arc: 279: ERROR: Attribute Not a valid attribute of object.
q.component.arc: 279: ERROR: First operand has invalid type.
q.component.arc: 279: ERROR: Invalid operation.
q.component.arc: 520: ERROR: Related Object Pair ‘CL_IIR’ and ‘CL_POR’ is not specified properly – either ‘R4707’ is not a relationship or the direction is incorrectly specified.
q.component.arc: 528: ERROR: Unable to find ‘cl_ic_provider’ on stack.
q.component.arc: 528: ERROR: NOT_EMPTY operator expects INST_REF or INST_REF_SET rvalue.
q.component.arc: 528: ERROR: Invalid operation.
q.component.arc: 520: ERROR: Related Object Pair ‘CL_IIR’ and ‘CL_POR’ is not specified properly – either ‘R4707’ is not a relationship or the direction is incorrectly specified.
q.component.arc: 528: ERROR: Unable to find ‘cl_ic_provider’ on stack.
q.component.arc: 528: ERROR: NOT_EMPTY operator expects INST_REF or INST_REF_SET rvalue.
q.component.arc: 528: ERROR: Invalid operation.
q.component.arc: 417: ERROR: Attribute of selected object does not exist.
q.component.arc: 420: ERROR: Instance Reference Variable for Object ‘C_PO’ has cardinality 0.
q.component.arc: 420: ERROR: Object Attribute ‘Id’ Undefined.
q.component.arc: 279: ERROR: Instance Reference Variable for Object ‘TE_PO’ has cardinality 0.
q.component.arc: 279: ERROR: Attribute Not a valid attribute of object.
q.component.arc: 279: ERROR: First operand has invalid type.
q.component.arc: 279: ERROR: Invalid operation.

---

**cort** · August 31, 2015 at 1:07 am

Dear sm4rpq,

Thank you for the post.

Even though C is not an option, I suggest getting started with it. The C model compiler seems to always be ahead of the C++ MC. Get some code that compiles with your model.

Once you have “gotten back into the swing of xtUML”, then fire up the C++ MC. We will help you get it going.

Kind Regards,
Cort

---

**sm4rpq** · September 19, 2015 at 6:29 am

There are so many things to discover and understand. At first I did have a hard time accepting the new component modeling and unified packages but resistance was futile, I have been assimilated.

I still have a lot to re-learn so working without a model compiler is good enough for now. Thanks for the offer. I have looked around on Github but can’t seem to find the archetypes for C++. Maybe I have not looked hard enough.

I have however noted that on modern hardware they seem to be a lot faster than I remember which is really appreciated.

---

**keithbrown** · September 19, 2015 at 10:41 pm

As of BridgePoint 5, the source archetypes for the model compilers are included in the installation. For example, the C++ arcs are found in /eclipse/plugins/org.xtuml.bp.mc.cpp.source_5.1.0/mc3020/arc

On github, the c++ specific arcs are “shared” with the SystemC arcs. The output differences are determined by markings. It is important to note that the C and C++ arcs share a lot of common functionality. Thus, when you look at [https://github.com/xtuml/mc/tree/master/arc](https://github.com/xtuml/mc/tree/master/arc) you see all the common/shared archetypes. The ones that are specific to each model compiler are then found in the c/ and sysc/ subdirs.

Cheers,
Keith
