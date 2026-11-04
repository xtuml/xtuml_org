---
redirect_from:
  - "/community/topic/xtuml-core-datatypes-udts-and-model-compilation/"

layout: "topic"
title: "xtUML core datatypes, UDTs and model compilation"
date: "2013-04-08"
permalink: "/forums/topic/xtuml-core-datatypes-udts-and-model-compilation/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dean** · April 8, 2013 at 7:14 pm

Recently I was asked by a new xtUML modeler, “In many programming languages like C++ and Java, or in hardware description languages like VHDL and Verilog, there are many variants of the fundamental numerical datatypes that developers use to optimize the final implementation. Why then in xtUML are there only two numerical core datatypes: integer and real?” Ironically, the answer is contained within the modeler’s question when they mentioned “to optimize the final implementation”. These variants of integer and real are in fact capturing Platform Specific Modeling (PSM) details, and in the xtUML methodology, PSM details are applied through a combination of entries in the marking files and capabilities in the model compiler. The Platform Independent model (PIM) in xtUML can then be annotated with descriptive User Defined Types (UDTs) and each UDT mapped to a target language datatype using the TagDataTypePrecision marking in the datatypes.mark file. The format of the TagDataTypePrecision marking is

.invoke TagDataTypePrecision( “MyDom”, “position”, “double”, “23.45” )

where the parameters are component, datatype name, PSM datatype name, and initial value.
Similarly, UDTs that are to be implemented as pointer based datatypes are also a PSM detail and can be called out to the model compiler by using the MapDataTypeAsPointer tag in the datatypes.mark file. The format of this marking tag is

.invoke MapDataTypeAsPointer( “MyDom”, “DataPacket”, “char”, “packet.h” )

where the parameters are component, datatype name, pointer type, and optional include file to declare this type as pointer.
