---
redirect_from:
  - "/community/topic/verifier-handling-of-reflexive-relationship-with-associative-object/"

layout: "topic"
title: "Verifier Handling of Reflexive Relationship with Associative Object"
date: "2017-09-20"
permalink: "/forums/topic/verifier-handling-of-reflexive-relationship-with-associative-object/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dennis Tubbs** · September 20, 2017 at 3:31 pm

I have a reflexive relationship in my model (1c:1c) on both ends. I created an associative object and formalized the relationship, assigning prefix ‘Next\_’ and ‘Prev\_’ for the instances. My associative object contains two attributes from the formalization ‘Next_Id’ and ‘Prev_Id’.

My initialization code creates two instances of the reflexive object (A) and one instance of the associative object (B). These instances I am calling a1, a2 and b1 respectively and unique identifiers are assigned to the identifying attribute ‘Id’ in each instance.

The instances are related with the following OAL:
relate a1 to a2 across R1.’prev’ using b1;

When I run this in the Verifier I end up with the following attributes in object b1 after executing the relate statement:
b1.Next_Id : a1.Id
b1.Prev_Id : a1.Id

b1.Next_Id should not be equal to b1.Prev_Id

Am I missing something?

Thanks,
Dennis

---

**Lee Riemenschneider** · September 20, 2017 at 4:55 pm

I just tried this in a test model and couldn’t reproduce it. I’m using BridgePoint version 6.4.3.201708292034.

---

**Dennis Tubbs** · September 20, 2017 at 6:44 pm

Hi Lee,

I installed v6.4.3 and got the same results I had before. So I created a test model as you did and that worked. I then went back to my original model, deleted and recreated the classes and relationships in question. It still did not work. Any idea on how I can resolve this without having to recreate the model from scratch?

Thanks,
Dennis

---

**Dennis Tubbs** · September 21, 2017 at 2:23 pm

I have resolved this issue, although I do not know exactly what was wrong. I created replacement classes as I did before but this time I did it with many intermediate steps, each time verifying the relationship was still correct.

---

**keithbrown** · September 21, 2017 at 3:58 pm

Hi Dennis,

In the case where it worked you said you used “many intermediate steps”. Can you explain what this means? Were you using copy/paste previously as an alternate method of class creation?

Keith

---

**Dennis Tubbs** · September 21, 2017 at 4:11 pm

Hi Keith,

In both cases I created new classes, copy and paste was not used. The first time after I created the new classes I immediately deleted the old relationships and classes, then I renamed the new classes to the old names and recreated the relationships. If I had to guess, I think I fooled BridgePoint into thinking I hadn’t made any changes through the renaming process. The files are not in source control.

The second time I did the same thing but broke it down into a couple of dozen steps. After each small change I checked that the relationship was correct in the Verifier before proceeding.

Thanks,
Dennis
