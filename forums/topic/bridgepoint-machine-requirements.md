---
redirect_from:
  - "/community/topic/bridgepoint-machine-requirements/"

layout: "topic"
title: "BridgePoint machine requirements"
date: "2015-06-10"
permalink: "/forums/topic/bridgepoint-machine-requirements/"
forum: "Miscellaneous"
forum_slug: "miscellaneous"
forum_url: "/forums/miscellaneous/"
---

**Bob Mulvey** · June 10, 2015 at 9:05 pm

I have been asked to comment about BridgePoint machine requirements. I am inclined to add the following to the FAQ. Please tell me what you think about this and help improve this:

General machine guidelines for working with BridgePoint

Since BridgePoint runs under Eclipse, machine configuration requirements come largely from Eclipse. However, as of this writing, there are no published requirements or recommendations for running with Eclipse. The reason for this is of course that Eclipse is an open development platform that can be used to run many plugins. Which plugins are being used will determine system requirements. That said, for BridgePoint, any reasonable standard engineering development workstation will do. As with any machine, the more resources, the better the performance. However, the only BridgePoint requirement is that for those using model compilers a minimum of 8gb of ram is required. Experience has shown that engineers running under Windows prefer at least 16gb of RAM.

---

**Travis London** · June 10, 2015 at 10:36 pm

The following comments are related to machines used to build BridgePoint. For building user models I think I would suggest 4GB as the minimum.

I prefer 16GB, using 8GB for the eclipse executable. However, this is not necessary for normal BP development. You can also only use ~4GB if running with the current product (32-bit limitations). If you have many build iterations and many test iterations you will likely hit an OutOfMemory error, causing you to restart. With the 8GB memory setting for java you rarely need to restart eclipse. As for processor, I do not think we have any requirements. But of course as Bob stated the bigger the better :).

Also note that the work to move BridgePoint to eclispe 4.4 has shown that a requirement is to have java 1.7. There is also another plug-in that requires java 1.8. Given this, soon one requirement will be to have at least java 1.7. Also note that the 1.7 requirement we likely be for building user models as well.

Regards,
Travis

---

**Travis London** · June 10, 2015 at 10:44 pm

Another semi-requirement would be to use ubuntu or windows. Again this is to build BridgePoint itself. I have successfully built it on both openSUSE and debian, but our instructions work much better with ubuntu.

For user models any linux variant should work without issue. There are requirements to have wine and some other libraries installed though. You can reference the documentation to figure out what is required.

---

**Lee Riemenschneider** · June 11, 2015 at 3:14 am

Shouldn’t this be in the usage forum?

---

**Lee Riemenschneider** · June 11, 2015 at 3:32 am

As Travis said, 32-bit means 4 GB per process, but a 64-bit machine could run parallel processes. I was doing model compilation just fine with 4GB on Ubuntu with an i7 quad core processor.
