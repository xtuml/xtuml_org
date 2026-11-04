---
redirect_from:
  - "/community/topic/how-to-use-the-component_ref-base-type/"

layout: "topic"
title: "How to use the component_ref base type?"
date: "2015-08-31"
permalink: "/forums/topic/how-to-use-the-component_ref-base-type/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Domonkos Asztalos** · August 31, 2015 at 11:20 am

Are there any documentation, tutorial where this item is described?
Can anybody provide some hints on the use of this type?

---

**keithbrown** · August 31, 2015 at 2:37 pm

Hello Domonkos,

In the BridgePoint help see: BridgePoint UML Suite Help \> Reference \> Using BridgePoint \> xtUML Modeling Perspective \> Model Elements \> Data Types

I did a quick search in the public [https://github.com/xtuml/models](https://github.com/xtuml/models) repository for the word “sender”. Then browsed to find “.xtuml” files in the search results. I see at least the VerifierMessageTestGlobals and ComponentSyntaxTest models both contain uses of “sender” and the component_ref data type. I suggest you import the ComponentSyntaxTest model and see how it uses “sender”.

Best,
Keith

---

**John Wolfe** · September 1, 2015 at 5:35 pm

Domi:

You may recall that we used this capability on the DIAMETER project. The model in question had a single server component sprouting a provided interface which was then connected to three different client components, each sprouting a required interface connected to the same provided interface on the server component.
The server component contained at least one class (call it Request) with an attribute (call it Requester_ID) of type component_ref. When the server received a request from a client, it would create an instance of Request and set the value of Requester_ID to the value of the ‘sender’ keyword. Later, when the server needed to reply to a client, it would then use the value of Request.Requester_ID as the target in a ‘send’ statement, enabling the server to send interface messages through a single port to a specific component instance among several connected to that port.
To summarize, the data type in question (component_ref) should be used carefully, and only in situations in which you anticipate the need to connect multiple component instances to a single port and require the ability to direct interface message to a specific component instance connected to that port.

–JRW
