---
redirect_from:
  - "/community/topic/selecting-a-subtype-instance-in-oal/"

layout: "topic"
title: "Selecting a subtype instance in OAL"
date: "2017-12-13"
permalink: "/forums/topic/selecting-a-subtype-instance-in-oal/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**xthunderheartx** · December 13, 2017 at 4:29 pm

So if I have an instance handle to some supertype and I want a handle to it’s associated the subtype it seems like I should be able to get that via the relationship between the 2 right? The following seems to suggest that:

select one \<instance handle\> related by \<start\> -\> \<relationship link\> -\> … \<relationship link\>;

In this case \<start\> is the supertype, \<instance handle\> should be the returned subtype handle, and \<relationship link\> is the subtype/Supertype relationship number.

Shouldn’t I be able to do something along these lines:

select any dl_inst from instances of Datalink where selected.LinkType == protocol::J1939;
select one dl_subtype_inst related by dl_inst-\>R1;

What am I missing?

---

**Levi** · December 13, 2017 at 4:49 pm

In OAL, you must specify key letters in all association traversals. So in your case:

select one dl_subtype_inst related by dl_inst-\>SUBTYPE_KL\[R1\];

Unfortunately, OAL doesn’t support selecting a generic subtype as it appears you may be trying to do. The typical pattern used here would be something like:

select one dl_subtype_inst related by dl_inst-\>SUBTYPE1_KL\[R1\];
if ( empty dl_subtype_inst )
select one dl_subtype_inst related by dl_inst-\>SUBTYPE2_KL\[R1\];
if ( empty dl_subtype_inst )
select one dl_subtype_inst related by dl_inst-\>SUBTYPE3_KL\[R1\];
if ( empty dl_subtype_inst )
// …. etc ….
end if;
end if;
end if;

Depending on what you are attempting to do with the generic subtype, there is some support. xtUML and OAL support polymorphic event handling, i.e. events can be generated to a supertype instance and each of the subtype instance can handle them in their own state machines.

Another feature that I have personally been wanting for a long time is deferred (abstract) operations. An operation could be defined on a supertype class and in each of its subtype classes. If invoked on an instance of the supertype, the related subtype operation would get invoked. This is not currently supported, but it would be interesting to hear if there are other people that have been wanting it!

Levi

---

**Dennis Tubbs** · December 13, 2017 at 5:58 pm

I would be in favor of deferred (abstract) operations. Polymorphic events are a great way to delegate events to a subtype to handle, when the event is part of the subtype’s natural life-cycle. But it has always bothered me when I have to create a state model for a class that has nothing to do with the state behavior of the class. Why should a class have a state model if it does not have any interesting behavior?

---

**xthunderheartx** · December 13, 2017 at 6:57 pm

This is precisely the issue. I have action associated with an incoming signal that needs to select a subtype instance based on one of the incoming parameters and then invoke an operation in the subtype. The subtypes don’t really have interesting lifecyles so I guess they will all have to get boring little state-machines … lame.

Thx all

---

**Lee Riemenschneider** · December 13, 2017 at 7:32 pm

You can invoke operations without a state machine. I take it you’re looking for some kind of overloading. ???

Subtype selection in BridgePoint is tedious, but there are workarounds. e.g., have a type attribute and select instances based on it.

---

**Lee Riemenschneider** · December 13, 2017 at 7:51 pm

Actually type attribute is a bad answer, because it’s pretty much the same if-then-else if-… selection mechanism.

---

**Lee Riemenschneider** · December 13, 2017 at 7:58 pm

I’m a little confused, because it sounds like you know the subtype class that you want to operate upon, so why do you need to send initiate the operation at the supertype?

---

**xthunderheartx** · December 13, 2017 at 8:48 pm

I have a supertype, Say ‘Animal’. There are 3 subtypes ‘Cat’, ‘Dog’, ‘Mon-Keigh’. Signal arrives over interface Port2::petAnimal which carries a parameter, say PetType which specifies the subtype. Maybe 0 = Cat, 1 = Dog, 2 = Mon Keigh. The super/sub is formalized over R1 with attribute AnimalType. Since every instance of Animal literally ‘is a’ Cat, Dog or Mon Keigh, and every instance of Cat, Dog or Mon Keigh ‘is a’ instance of Animal, if I have an instance handle of Animal, I should by the definition of ‘is a’ have a handle to the other Cat, Dog or Mon Keigh. The super and sub are literally the same instance. So if I select an instance myLittleBuddy of Animal where AnimalType == param.petType and then myLittleBuddy.stroke(); I should get the right mammal. Or at least it seems like it should work that way. But the OAL can’t see ‘stroke()’ because it isn’t defined in Animal, only Cat, Dog and Mon Keigh.

Now since stroking your kitty Cat is different than stroking your Mon Keigh the behavior should be different in each case.

Obviously, it can be done with Polymorphic Events, which I use elsewhere. But stroking the Mon Keigh isn’t very interesting and has no true dynamic nature so it doesn’t need a state machine. Just an operation with different processing than Cat or Dog.

I could be in the weeds of course. It happens at my age … now where did I put my glasses?

---

**Lee Riemenschneider** · December 13, 2017 at 9:39 pm

select any \[petType instance name\] of \[petType Keyletters\] where selected.id == \[Animal handle\].id;
\[petType instance name\].stroke();

This is different than the scenario where you want to stroke all the animals without selecting instances of each subtype.

Examples aside, I know this discussion has cropped up before. It’d be nice to have polymorphic operations.

---

**Lee Riemenschneider** · December 13, 2017 at 9:55 pm

Even nicer would be to have the metamodel recognize that the instances are the same in such a way the you could even assign a subtype attribute. i.e., \[supertype handle\].\[subtype attribute\] = x;

OTOH, if you know the subtype why not just get it’s handle? The polymorphic events are a nicety to the OAL coder, but require extra work in state modeling. The question is does it also result in more efficient compiled output, and if so, is this a flaw in the model compiler?

Can it be mitigated through a rework of the metamodel? In [this metamodel](https://github.com/lwriemen/shlaer-mellor-metamodel), I worked to get generalization right (I hope), but it doesn’t have any supporting tooling to verify that it makes things better. Maybe I’ll get the tooling done when I retire. Maybe BridgePoint can benefit from the lessons I’ve learned in making it.

---

**xthunderheartx** · December 14, 2017 at 1:44 am

Hmmmmmm ….
