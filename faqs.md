---
layout: "page"
title: "FAQs"
permalink: "/faqs/"
---

[xtUML Profile](#profile)  \|  [xtUML Editor](#editor)

## xtUML Profile

1.  **What is xtUML?**
    xtUML is a UML profile that defines the constraints and extensions needed to make UML executable and translatable. xtUML transforms the UML language from a static picture drawing facility into a full-fledged solution for model-driven development. With xtUML, users don’t draw model pictures of their application at a moment of time. Instead, they create models that are the application.

2.  **What is the history of xtUML?\**
    The introduction of the Unified Modeling Language (UML) by the Object Management Group (OMG) in 1997 marked a turning point in the development of a mature process for systems and software engineers. The UML provides a standard notation for describing complex systems and offers a more effective communication and documentation mechanism. However, UML fails to prescribe a methodology that ensures high quality systems will emerge from these diagrams. This lack of a methodology inadvertently constrained the impact of UML diagrams on the systems design community.To correct this problem, the developers of xtUML combined the methodology of Model Driven Architecture (MDA) with the notation of UML. This combination provides a rigorous framework for raising the abstraction of systems design and automating the transformation from platform-independent models to platform-specific implementations. From this starting point, a user community and set of tools has emerged, and with the formation of xtuML.org, the ability to edit, execute, and translate xtUML models into target-domain solutions will continue to grow.

3.  **How is xtUML different from UML or SysML?**
    xtUML and SysML are both profiles of the UML. The SysML profile customizes UML for the broad, interdisciplinary, field of systems engineering. The xtUML profile customizes UML for software and hardware application development and system design.  There is roughly 70% overlap.

4.  **What is the xtUML Process?**
    The xtUML process defines a recommended methodology and style guide for doing model-driven development with a focus on early execution followed by translation of application models into design-level code.

5.  **What is Object Action Language?**
    The Object Action Language (OAL) is used to define the semantics for the processing that occurs in an action. An action can be associated with states, functions, and interface messages.OAL is used for:

    - data access
    - event generation
    - test
    - transformation
    - bridge and function
    - inter-component messaging

    It supports these through:

    - control logic
    - access to the data described by the class diagram
    - access to the data supplied by events initiating actions
    - the ability to generate events
    - access to timers and to the current time and date

    Using OAL allows the application developer to have the flexibility of a platform-independent model that is not tied to a specific target language or premature partitioning of the hardware and software components. This frees the developers from worrying about language-specific constructs and allows the model compiler to create efficient, retargetable, standards-compliant implementation code.

6.  **What is a Model Compiler?**
    A model compiler is a software tool that translates the data (components and classes), control (state machines and messages), and processing (OAL) defined in the application model into an implementation-specific runnable suitable for execution on the target. Model compilers perform rules-based code generation. Commercial model compilers are available that support C, C++, and SystemC.

7.  **Where can I get model execution and translation support?**
    The Verifier and model compilers are Open Source Software along with the Editor.

8.  **Where can I find out more about xtUML methodology and tools?**
    The [xtUML Index]({{ '/index/' | relative_url }} "Index") defines a list of terms with associated tutorial videos.

## xtUML Editor – General Questions

1.  **What are the capabilities of the xtUML Editor?**
    The Unified Modeling Language (UML) is used to graphically analyze and create software systems. The xtUML Editor is built upon the eclipse
    framework. It allows users to draw UML diagrams that:

    - explore how the various pieces of the system communicate
    - delimit how these pieces are packaged together
    - elaborate the underlying data within the system
    - specify flow of control
    - define the actions and processing

    There are many tools that exist that allow users to draw UML diagrams. The xtUML Editor enables the user to define the actions and processing within the model in a platform independent way. Before hardware decisions are made and implementation languages are chosen. This frees the system designer to worry about the domain-specific problems his application is solving rather than getting bogged down in implementation details.

    Platform-independent modeling achieves its full power and culminates in the “x” and “t” part of xtUML.  The “x” refers to model execution. The BridgePoint xtUML suite of tools provides a tool (called Verifier) to test and debug the models created in the xtUML. org editor. Verifier runs the application model in an environment similar to other language-specific debuggers in Eclipse–with stack tracing, variable views, stepping, and breakpoints, all done without any hardware or implementation languages. Verifier truly executes the model itself. This allows the system designers and application-domain experts to test and verify the functionality of the application, not the implementation (hardware issues and implementation language bugs). This increases reliability and reduces time to market.

    The “t” refers to model translation. When it comes time to make implementation decisions, BridgePoint provides model compilers that translate the model into a specific language (such as C or SystemC) while conforming to APIs and standards (such as IP-XACT, AUTOSAR, or MISRA-C). In the same way that C raised the level of abstraction over machine-specific assembler languages, xtUML Editor’s Object Action Language raises the level of abstraction over languages such as C and SystemC. This allows you to reuse and retarget pieces of the application model very easily. The BridgePoint model compilers provide all these benefits while giving the implementation experts control over the details of the target implementation and ability to customize the model compilers themselves.

2.  **How do I get started using xtUML Editor?**
    - [Link to Introduction to modeling doc]({{ '/assets/uploads/2012/12/xtUML-Quick-Start-Guide.pdf' | relative_url }})
    - When the application starts, the Welcome page is displayed.  Choose Quick Start, then select one of the sample model links to create the example project.

3.  **What sets the xtUML Editor apart from other UML editors?**
    Other UML editors are either just drawing tools or lock you into platform-specific constructs. The xtUML Editor is much more than just a drawing tool. It is the gateway to platform-independent modeling, model execution, and model translation.

4.  **Can I integrate my UML application with existing code or libraries?**
    Yes. xtUML provides modeling constructs that allow you to interface with existing code and libraries. This significantly decreases the barrier to entry because it allows you to try out xtUML by modeling a small piece of your application instead of having to try to model the entire application at once.

5.  **What are the licensing terms?**
    Please see the [Terms & Conditions]({{ '/about/terms-conditions/' | relative_url }} "Terms & Conditions").

 

## xtUML Editor – Runtime Questions

1.  **I’m having trouble installing or running xtUML Editor on Linux.  What is wrong?**
    Installing and running on Linux may require some additional system configuration.  There are existing [Forum discussions]({{ '/forums/xtuml-forum/' | relative_url }} "xtUML Forum") that may prove helpful.  If you are still having trouble after trying out those suggestions, create a new discussion which details your problem.
