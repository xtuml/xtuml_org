---
redirect_from:
  - "/community/topic/component-referencing-not-working/"

layout: "topic"
title: "Component Referencing not working"
date: "2019-09-06"
permalink: "/forums/topic/component-referencing-not-working/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Clive** · September 6, 2019 at 7:54 am

I seem to be having trouble creating component references. I’ve created several components (some to be realised). I’ve created provided and required interfaces (the circles and cups) on various components. No problems!
I then created a separate package and went through the process of creating component references and assigning them to the existing components. The components (as usual) are selectable from a list that appears, and when selected the corresponding component name appears in the drawn component reference box, but none of the interface connectors appear – not a one!
This all seemed to be working OK earlier, but then I rearranged the model – not in any arbitrary way but rather changed high level components (containing sub-components) into packages (containing the sub-components).

I then decided to create an interface, and ‘formalise it’ to a connection between two components. That all went fine, all the operations I’d assigned to the port showed up in the correct places in the hierarchy of the Model Explorer. I then checked whether a class operation that ‘called’ one of the interface operations actually worked. Initially it did using the construct of \<interface_name\>::\<interface_operation\>. The OAL parsed OK. I then started to do some exploring:
Firstly I disconnected the formalised interface on the component diagram – that didn’t seem to change anything in parsing the OAL.
Secondly, I unformalised one side of the previously ‘connected’ interface. The OAL then did not parse.
Thirdly, I tried to re-formalise the interface. The OAL did not parse.
Fourthly, I completely deleted the ports (in the hierarchy) corresponding to the relevant interface connectors on each component, and recreated them, and re-formalised the whole connection. The OAL still didn’t parse.
Fifthly, I checked why the OAL didn’t parse. The error (apparently) is caused because I didn’t refer to the ‘port’, and that I couldn’t use the interface name to qualify the operation I wanted to call (i.e. using the construct mentioned above).
All I could say then was Huh! What the heck is going on here? Why did this all work to begin with and now it doesn’t together with a somewhat curious error statement. Why name an interface and attach operations/signals to it when I’m apparently supposed to use a port to access the interface. Further to that, I have not found a way to refer to a port from OAL. Then I checked OAL preferences and found that the box for using interface names for inter-component messaging was turned off. Turning it back on resolved the OAL issue (at least). Why it became swithed off, I have no idea.

Then I went back to creating the component references I had started out to do. Well! Things improved slightly. Any formalised, connected arrangements I had created within my original (real) component diagram showed up, disconnected, on the diagram on which I assigned them as component references. More curiousness!

Unless, I’ve missed something, I don’t believe this is the way that component referencing is supposed to work. I believe I am supposed to be able to create more than one ‘configuration’ showing different component connection arrangements. This at least implies that all given provided and required interfaces should show up on the ‘configuration’ diagram in order to be ‘configured’! They certainly seem to do so in the tutorials I’ve watched.

Have I missed a preference setting?

---

**cort** · September 6, 2019 at 1:45 pm

It sounds like you are doing mostly the right things. There is a lot in this post, so allow me to simply make some recommendations.

1\) In OAL, always refer to the port (rather than the interface) when sending messages. UML allows the use of the interface name, and thus OAL was designed to support that idiom. However, it brings a couple of problems. Firstly, you then cannot formalize an interface onto the same component twice. Also, the reason for ports is so that there is an “internal view” of the interface named in the vocabulary of the domain embodied by the component.

2\) There is a bug in the OAL parser that will get confused if you name a port the same as an interface. Avoid this by naming ports differently from interfaces. Again, choose a name that makes sense to component/domain that is sending/receiving messages.

3\) I think you are doing this, but we often recommend having a package of components with interfaces formalized but not connected. Build your configurations from component references only.

4\) Nesting components is complex. Take care when choosing to configure a system this way. Unless your system truly requires component nesting, try to simpler approaches… at least while beginning to use BridgePoint.

---

**Clive** · September 6, 2019 at 10:56 pm

Thank you for the input. As you point out, I think I’m doing (roughly) the right things – at least I believe what I’m doing is ‘logical’ :-)

I will do a little more research based on your input. BTW, I did name ports differently to interfaces. I have now discovered why I didn’t get it to work – I hadn’t changed the BP Preferences for OAL back to the default of not using the interface name for component communication. The references to the keyword ‘send’ lead me astray too!

Actually, it’s a backward compatibility issue that is driving the use of interface naming. At least for now!
