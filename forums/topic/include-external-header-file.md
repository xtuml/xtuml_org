---
redirect_from:
  - "/community/topic/include-external-header-file/"

layout: "topic"
title: "Include external header file"
date: "2018-02-22"
permalink: "/forums/topic/include-external-header-file/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**gkrister** · February 22, 2018 at 12:13 pm

Hi,

I’m a bit new to xtUML and Bridgepoint and have a question.
I use Bridgepoint to generate C++ code.
I would like in Bridgepoint (or rather in the transformation step I guess) include external header file(s), so the external header files are included into the transformed C++ files., how to do that ?
BR,
Krister

---

**cort** · February 22, 2018 at 1:49 pm

Hi Krister,

There is a simple way to add .c and .h files into your build. Just drop your file into the /gen folder of the project. It will automatically be copied into the /src folder during model translation. It is also possible to modify a generated file by copying a file from /src to /gen and editing it. The files in /gen are copied \_on top of\_ files in /src after all code is generated.

This process is also described in the BridgePoint Model Compiler Help topic in the tool.

Cort
