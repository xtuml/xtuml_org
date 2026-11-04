---
redirect_from:
  - "/community/topic/building-a-simulatable-model/"

layout: "topic"
title: "Building a simulatable model?"
date: "2014-11-27"
permalink: "/forums/topic/building-a-simulatable-model/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**sfinnie** · November 27, 2014 at 1:00 pm

Hi all,

Are there instructions anywhere for how to create a simulatable model?

By ‘simulatable’, I mean one that can be run in verifier but that doesn’t need to be translated using a model compiler. I tried the following but am getting an error:

1\. Create new xtuml project
2. Select ‘None’ in the “select model compiler” step
3. Finish creation wizard
4. In Model Explorer, right click on project & select “new package”, create package “foo”
5. Repeat above to create package “test foo”
6. Create simple class diagram for “foo” (Dog-Ownership-Person)
7. Create single class in “test foo” named “Test_Foo”.
8. Add state diagram to Test_Foo that tests the domain model in Foo (create instances of model, assert results as expected).
9. Add function in “test foo” package to instantiate Test_Foo class and send it the ‘setup’ event
10. Right click on project in model explorer & select “Launch Verifier”

At this point the xtUML Debugging perspective opens, but then a dialogue with the following content appears:

“Nothing to Verify. Open the Debug dialog and check the configuration for this session”

Not sure what this means? The only ‘Debug Dialog’ I can find is under Preferences (Window-\>Preferences-\>Run/Debug) but there’s nothing obvious in there.

I can successfully run the Microwave example as above (right click on project, select “launch verifier”).

So that suggests it’s something about my model. The only obvious difference I can see is that the MW model includes a Component whereas mine doesn’t.

I tried setting the MW model compiler to “None” (Right click project-\>Bridgepoint utilities-\>Set Model Compiler) and it still works fine, which further suggests something about my model.

Thanks for any guidance.

-Scott.

PS: Great news on the open source announcement btw. Best wishes to all at OneFact.

---

**poj** · November 28, 2014 at 6:10 am

Putting things inside a component gives you a model you can simulate using Verifier.

---

**sfinnie** · November 28, 2014 at 12:36 pm

@poi thanks, that did indeed solve it.

---

**Lee Riemenschneider** · November 30, 2014 at 9:56 pm

So…which is the error? Requiring a component to run a model simulation, or allowing a class model to be built without a component? If components are considered domains in this BridgePoint incarnation, then you probably shouldn’t be allowed to build a class model without a domain.

---

**cort** · December 1, 2014 at 5:14 pm

BridgePoint plans to allow class diagrams to be modeled outside of components and then “imported” to the internal behavior of components. This will allow reuse of classes and class diagrams.

In the mean time, we have the above mentioned “one or the other but not both”.

Cort
