---
redirect_from:
  - "/community/topic/verifier-ee-external-method-not-found/"

layout: "topic"
title: "Verifier EE external method not found"
date: "2015-08-12"
permalink: "/forums/topic/verifier-ee-external-method-not-found/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**benjo123** · August 12, 2015 at 5:42 pm

Dear All,

I have created a Realized Component according to the instructions written in the Help:

– in the model the realized component is connected through an interface to the ‘normal’ component, the bindings are correct.
– the core.jar is added to the path of the realized component (in the Properties view).

– added the interfaces with methods (ICommunicationToProvider.java, ICommunicationFromProvider.java) to the correct package (relative to the root of the Project, inside the source folder).
– the headers of the methods are correct: first parameter is the ComponentInstance_c, the others are the same as in the model’s interface defintion; the return type is correct as well.
– added the realized component’s class at the correct place.
– implemented the realized component correctly: constructor with one parameter (ICommunicationFromProvider), the class implements the ICommunicationToProvider interface, all the methods of the interface are implemented by the class.

When I run the system in the Verifier, and I call an operation (initialize) through that interface from the model to the realized component, the following Exceptions are thrown:

\[3 times:\]
Verifier EE external method setSection( org.xtuml.bp.core.ComponentInstance_c, int, java.lang.Boolean ) not found
java.lang.NoSuchMethodException: setSection
at org.xtuml.bp.core.Vm_c.Execute(Vm_c.java:469)
at org.xtuml.bp.debug.java.access.VerifierInvocationHandler.executeRealizedCode(VerifierInvocationHandler.java:989)
at org.xtuml.bp.debug.ui.model.BPThread\$1.run(BPThread.java:119)
at java.lang.Thread.run(Unknown Source)

\[Once:\]
Verifier EE external method initialize( org.xtuml.bp.core.ComponentInstance_c, int ) not found
java.lang.NoSuchMethodException: initialize
at org.xtuml.bp.core.Vm_c.Execute(Vm_c.java:469)
at org.xtuml.bp.debug.java.access.VerifierInvocationHandler.executeRealizedCode(VerifierInvocationHandler.java:989)
at org.xtuml.bp.debug.ui.model.BPThread\$1.run(BPThread.java:119)
at java.lang.Thread.run(Unknown Source)

The ICommunicationToProvider interface contains these methods:

public void setSection(ComponentInstance_c senderReceiver, int sectionId,
Boolean isEnabled);
public void initialize(ComponentInstance_c senderReceiver, int turnoutId);

The direction of the setSection and initialize are ToProvider (where the provider is the realized component). The initialize is an operation, setSection is a signal.

Java codes are compiled correctly, no reference errors.

What may cause the Exceptions, and how can I correct the error?

Thank you for the help in advance.

Best regards,
Ben

---

**Bob Mulvey** · August 13, 2015 at 12:47 am

Hi Ben, I do not know why you are seeing this. However, I will tell you what I would do to track down a problem like this. I would follow the instructions in the developers getting started guide found here: [https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/Developer%20Getting%20Started%20Guide.md](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/Developer%20Getting%20Started%20Guide.md)

That allows you to debug and make changes to BridgePoint!

After getting a good build I would then launch the tool in a debug session. I would then set a breakpoint perhaps on the line called out by your call stack here: “at org.xtuml.bp.core.Vm_c.Execute(Vm_c.java:469)”

I would then execute the procedure to reproduce the problem, hit the breakpoint and go from there to see why it happened.
