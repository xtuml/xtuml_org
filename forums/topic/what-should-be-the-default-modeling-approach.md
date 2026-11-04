---
redirect_from:
  - "/community/topic/what-should-be-the-default-modeling-approach/"

layout: "topic"
title: "What should be the default modeling approach?"
date: "2017-10-25"
permalink: "/forums/topic/what-should-be-the-default-modeling-approach/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Lee Riemenschneider** · October 25, 2017 at 12:09 pm

This topic stems from a recent discussion in a feature request I submitted (#9864).

In the discussion, package references were brought up as a way to model domains without components, which I had assumed, from the training videos on this site and much of the BridgePoint help documentation, was not a desired approach.

Since the issue discussion might lead to training/documentation changes, I thought maybe we needed to (re)define the default modeling approach. I attached the list below to the issue, but thought this might be a good place to elicit feedback from the BridgePoint user community. Please add your comments about your desired modeling approach.

Default modeling approaches:
1. Shlaer-Mellor/Executable UML book approach is:
\* Identify domains in system
\* Model domains in system
\* Combine domains (through largely unidentified means) to result in system

2\. xtUML training approach is:
\* One xtUML project (yes, IPR is covered, but mostly GPS Watch approach)
\* Library package with components representing domains
\* System package with component references
\* Run model compiler/project build to result in system

3\. What I would do in a large company/team development project:
\* Separate xtUML project for each domain
\* Separate xtUML project for each target system
\* Use components in domain projects was the default, but maybe now I’d use package references in the system project.

---

**Dennis Tubbs** · November 22, 2017 at 5:09 pm

Maybe the problem is in the way I think of partitioning a system, but I struggle with Components and the ability to re-use parts of the model.

For example, it seems natural to me to create an interface to a servo drive. A generic interface decouples the application logic from the drive logic and when a different hardware vendor is required the main application logic remains intact. As a bonus I can use the vendor specific drive component on any project where the hardware will include the drive.

But when I think about a machine that has 100 or more identical servo drives and all of the ports required to interface to them, I start wondering if a package of classes and relationships wouldn’t have been the better approach. The downside is the system becomes more tightly coupled and the ability to re-use the model decreases.

Maybe with the 3rd approach the modeler can choose the size of building block that best fits the task at hand, either a Component or a Package.

---

**Lee Riemenschneider** · November 23, 2017 at 3:23 am

I’m trying to impress that a package-as-a-domain and a component-as-a-domain are the same thing, so choosing one or the other based on size isn’t really a valid choice. By the same token, an EE and interface are the same at the analysis level.

I’m not sure I understand the servo example. It sounds like one Servo domain model bridged 100 times to another domain. This is multiple instantiations across the same interface. The instantiations can either be modeled with an identifier as a bridge parameter (class instances), or could be handled in the implementation (domain instances).

The included Time EE is maybe an illustration of this issue. Making it a component on the system diagram would produce a very messy picture.

---

**Dennis Tubbs** · November 27, 2017 at 1:43 pm

Poor choice of analogy and the word “size” on my part. What I meant was more in line with “pick the right tool for the job.” However, after reading your response I have a better understanding of your point, I think. A Component aligns with modeling method \#2, a package with modeling method \#1, and you are proposing to create a system out of either.

I am unclear as to how you can use a Package to build a system without some other code to create the interface. Maybe that is just the 3rd bullet in your method \#1.

Thanks for the pointer on my servo example. I think another level of training, beyond what is currently available on the website, is necessary. Having all the pieces doesn’t mean someone is qualified to put them together correctly. I have seen this more than once with programmers who use C++ or C# but are still writing functional programs because they are not using any of the OO features of the language.

---

**Lee Riemenschneider** · November 28, 2017 at 12:39 pm

Yes, “package as a domain” required some other external code to build a system in pre-component BridgePoint, and requires the use of “package references” in components in current BridgePoint.

One thing online self training misses is the ability to easily identify the gaps in the training. Classroom style training is still preferred. Having an online forum helps, but you also need the more structured walk through.

You also need a consistent approach, which is what I’m trying to nail down. I prefer domain modeling with packages, but that creates more work when integrating the domain into a system. Domain modeling with components requires more work on the domain modeling side, but everything is in place for system integration. Ideally, creating a component and interface structure from a package domain model could be automated, but is it worth the cost of the changes on the tool side?

Maybe a HOWTO of both approaches should be written. The documentation in the BridgePoint help needs updated anyway.

---

**Dan George** · November 29, 2017 at 12:17 am

FWIW, package reference is the way I’d choose (assuming it is not a PITA). IMHO, components are part of the model compiler domain. TBH, I was disappointed to find BP using components instead of packages as in SM-UML.

I’m not a BP users. Part of the reason for that is the lack of guidance for simple, practical issues like this. I felt that not only would I have to learn the ins-and-outs of MDD, I’d also have to figure out how to manage the artifacts, from scratch. Too daunting.

---

**Lee Riemenschneider** · November 29, 2017 at 12:23 pm

The only PITA in using package references is recreating your incoming and outgoing bridge definitions as Interface operations or signals. This is the part that I think could be automated.

Components aren’t really part of the model compiler domain. The model compiler is still working on a single domain at a time. In a multi-domain build, you could have multiple instances of the model compiler running in parallel. (NOTE: This might be more theoretical than how BridgePoint actually works right now. I’m going to be lazy and not look it up.) Combining the domains is a linker step. In eclipse (and most IDEs), a project build runs many different tools, so it looks seamless.

The component interfaces give you a place to put implementation specific code in your system model for a specific platform. Thus Dennis’ servo example could use some distribution middleware interface to remote servers on one platform and direct hardware port I/O calls on another. In the old BridgePoint EE skeleton generation paradigm, it was much harder to maintain this kind of reuse of the application domain. Even without different platform targets, test code in component interfaces is easier than test code in EE bridges.

This convenience outweighs the overhead of components in BridgePoint, but that doesn’t mean we shouldn’t be able to modify the tool to eliminate the overhead.

---

**cort** · December 6, 2017 at 6:09 pm

Good thinking, @Lee.

**Publish Interface**

One way of working with a Shlaer-Mellor domain is to create “public” domain functions that serve to receive invocations from outside the domain (modeled in a package-as-domain). Then, when deploying the domain, linking these domain functions to incoming messages from an interface. However as stated above, this process requires manually creating interfaces with messages that correspond to the public domain functions.
Maybe we could right click on a package and “publish” these domain functions by automatically creating an interface with messages having the same signatures as the domain functions… Hmmm.
It also makes me think of an enhancement to Verifier to automatically call a like-named domain function from an inbound port message that has no OAL… Hmmm.

---

**Clive** · May 28, 2019 at 9:59 am

I’ve perused this conversation because I was looking for guidance or an answer to the question of “What modelling technique should I use that corresponds best with the available model compiler.”
When reading the current doco surrounding the latest BP, it seems that the model compiler suits the OOA approach, but not the later UML 2.x approach. I’m not really bothered too much about which modelling approach to take, but I am concerned about choosing one that best matches the modelling.
So! Which combination of modelling approach and model compiler is deemed best?
Another part of my concern is the fact that I possess a model compiler for generating Ada95 that was constructed in 2006 using MC-2020. I would like to update it to be compatible with the current version of BP. And also to generate Ada 2012/SPARK 2014. Any advice or suggestions would be well received.

---

**Lee Riemenschneider** · May 28, 2019 at 1:25 pm

What do you mean by the UML 2.x approach? The OMG version of executable UML (fUML + Alf), or something else?

---

**cort** · May 28, 2019 at 2:32 pm

All BridgePoint model compilers translate models which adhere to the Shlaer-Mellor Method of Object Oriented Analysis (S-M OOA). MC-2020 and your Ada95 derivative will translate classes, state machines and action language according to the methodology. MC-3020 as bundled with the current BridgePoint is also an implementation of S-M OOA but does translate components and interfaces in addition to the original S-M artifacts.

Can you post your model compiler derivatives to one of the xtuml repositories? I am sure members of the community would enjoy helping you analyze the alternatives.

---

**Clive** · May 29, 2019 at 12:57 am

Sorry Lee! My language was rather loose wrt to using ‘approach’. However, the thought was brought on by a reference (somewhere) in the user manuals/guides about a distinction between xtUML and UML2. Rereading has now established that I was misinterpreting what had been written. Apologies.

Cort: Your summary comment has cleared up some of my fuzziness. I can certainly provide all the relevant pieces of information including the compiler we created. We used the compiler to develop an trial election system for the Australian Electoral Commission. The system was intended for the vision-impaired and blind and was used in the in the Australian Federal Election in 2007. The system worked perfectly and the election commission officers were very impressed with its stability and consistency. Unfortunately, the political will did then not exist to take the system further.

What do I need to do to include the information in the xtUML repository. Additionally is there a possibility of contracting a model compiler expert to guide us in upgrading the compiler for use with BP 3020? We do have some limited funding.

Regards.

Clive.

---

**cort** · May 29, 2019 at 1:50 am

[@Clive]({{ '/user/clive/' | relative_url }}), very good information.

You can do things the Modern Cool Nerd Way by creating an account on github.com, forking xtuml/models, cloning and submitting a pull request (PR). Or you can do things the Practical Way and email a zip file to me or someone on the BridgePoint team. :)

For that and for direct communication regarding a model compiler expert, send an email to cortland.starrett \[at\] onefact.net.
