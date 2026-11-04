---
redirect_from:
  - "/community/topic/printing-to-standard-output-from-java-code/"

layout: "topic"
title: "Printing to standard output from Java code"
date: "2015-08-09"
permalink: "/forums/topic/printing-to-standard-output-from-java-code/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**benjo123** · August 9, 2015 at 9:03 am

Dear All,

Is it possible to print to the standard output (System.out.println) without using CorePlugin.out.println?

I ask it, because I have written Java codes to the model in a Realized Component, and I deploy those codes in a single jar. I forward the method-calls to the jar in the realized component. I would like to deploy only a single jar, that contains all the dependant ones, which include the core.jar that is quite large (12 MBs).

Is it possible to include only those components from the core.jar that are responsible for printing to the standard output?

Thank you for the help.

Best regards,
Ben

---

**keithbrown** · August 10, 2015 at 1:38 pm

Hello Ben,

Yes, it is possible to call System.out.println from your realized java class. I don’t quite follow the issue you are facing.

The topic of using Realized classes is covered in Module 18 of the Modeling with xtUML course here on xtuml-org.hustlefish-sites.com ([on line courses]({{ '/learn/on-line-courses/' | relative_url }})), perhaps that will help you as well.

Cheers,
Keith

---

**benjo123** · August 10, 2015 at 2:26 pm

Dear Keith,

Thank you for the answer. In the previous versions of BridgePoint I faced with a problem, that I could only print to the standard output, through CorePlugin.out.println, that’s why I thought I shall use that method.

In the built-in examples still the CorePlugin.out.println is written in the Help chapter for the Realized classes.

Best regards,
Ben
