---
redirect_from:
  - "/community/topic/accessing-operations-from-a-passed-inst_ref/"

layout: "topic"
title: "Accessing operations from a passed inst_ref"
date: "2015-06-24"
permalink: "/forums/topic/accessing-operations-from-a-passed-inst_ref/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Bob Mulvey** · June 24, 2015 at 4:58 pm

There was a good Q/A in the modeling chat about accessing operations from an instance passed as inst_ref. I think it is worth capturing here in the forums so it can be easily found by users who may search xtuml-org.hustlefish-sites.com. Here it is:

dave2: Hi I have a question. If i pass an object to a function using the inst_ref, I am then able to access the attributes of the object by param.. but how do I access its operations/memeber functions?(7:23AM 23rd Jun)
dave2: For instance, I have an object called card of the Class Cards. I call the function by ::myFunction(card:card); and in the function i am able to access the attributes by x = param.card.m_myAttribute; But its memeberfunctions/operations I am unable to reach. I have a function called toString in Cards which returns a string. When I try to use it by, str = param.card.toString(); Bridgepoint complains about unexpected token ‘(‘ and that ‘(‘ is not an attribute of Class Cards.(7:27AM 23rd Jun)
dave2: toString has no parameters(7:28AM 23rd Jun)
Me: Does operation toString () have a return type of string?(7:33AM 23rd Jun)
dave2: yes it does(7:37AM 23rd Jun)
cort: Is the operation toString “instance-based” or “class-based”?(8:19AM 23rd Jun)
cort: I ask this, because “instance-based” operations are accessed through inst_ref. But “class-based” operations are access by name :: .(8:23AM 23rd Jun)
dave2: It is instance based(9:38AM 23rd Jun)
dave2: I am able to access the operations where I have created the objects(9:40AM 23rd Jun)
dave2: using the same method, str = card.toString(); and the same when accessing attributes. Also able to access the attributes in the function but not the operations(9:41AM 23rd Jun)
dave2: I dont understand why I am able to access attributes but not operations(9:43AM 23rd Jun)
cort: This could be a bug.(9:44AM 23rd Jun)
cort: Are you seeing this while running Verifier?(9:45AM 23rd Jun)
dave2: Yes(9:45AM 23rd Jun)
dave2: Or wait, I can double check that(9:45AM 23rd Jun)
cort: O.K. Try something for me (a workaround).(9:45AM 23rd Jun)
cort: Do this:
card = param.card;
str = card.toString();(9:46AM 23rd Jun)
cort: I have seen situation where:
param.card.toString() may have trouble. But assigning to a temporary variable worked around it. Let me know what you see.(9:47AM 23rd Jun)
dave2: Well it actually worked with your workaround(9:48AM 23rd Jun)
dave2: It work as expected(9:48AM 23rd Jun)
dave2: I also get a warning, “Warning: access made to unwritten array element. Using default value at proj::.(..)”(9:50AM 23rd Jun)
dave2: Thank you for the help, I’ll use this workaround for now(9:50AM 23rd Jun)

---

**Erik Wedin** · June 24, 2015 at 10:12 pm

Good post! I was not even aware of that it was possible to invoke operations based on an instance reference parameter.
