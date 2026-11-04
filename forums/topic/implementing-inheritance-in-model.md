---
redirect_from:
  - "/community/topic/implementing-inheritance-in-model/"

layout: "topic"
title: "Implementing Inheritance in Model"
date: "2017-09-02"
permalink: "/forums/topic/implementing-inheritance-in-model/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Rob** · September 2, 2017 at 6:58 pm

Do you have examples how to setup inheritance in the model? I set up a basic scenario in which I setup an inheritance relationship between the super class and derived class. I had an attribute in the derive class. I instantiated the classes in OAL but i could not access the “inherited attribute” in the derived class. Any insight on setting up inheritance where i can inherit attributes?

Thanks,
Rob

---

**cort** · September 2, 2017 at 8:23 pm

In xtUML, traditional inheritance is not completely present. Here are some specifics.

– On state machines, event inheritance \_polymorphic events\_ are supported. Events to a supertype can be received at the subtype.
– In the MASL dialect of xtUML, operation inheritance (\_deferred operation\_) is supported.
– Attributes are instantiated in the instance of the class in which they are defined. In xtUML, the hierarchy of classes is instantiated as a \_related instance chain\_. Access to attributes in a supertype is via navigation.

Here is an example model showing a sub/super hierarchy: [https://github.com/xtuml/models/tree/master/VandMC_testing/mctest/subsuperchain](https://github.com/xtuml/models/tree/master/VandMC_testing/mctest/subsuperchain)

Here is a video on the various association types. Just after 1:30 a sub/super is diagrammed.

---

**Rob** · September 2, 2017 at 9:10 pm

For the 3rd case is the “\_related instance chain\_” the name of the associated link to navigate? Is “\_related instance chain\_” defined “automatically” when the super-type relation is “drawn”?

Thanks,
Rob

---

**cort** · September 2, 2017 at 9:28 pm

When you create the instances of the sub/supertype hierarchy (in OAL using *create*). You will also relate them (using the *relate* statement).

So, then when you access these instances, you can navigate across the association using the relationship number of that association (using the OAL *select … related by* statement).

The example model should demonstrate this. Let me know if you want pointers to other example models.
