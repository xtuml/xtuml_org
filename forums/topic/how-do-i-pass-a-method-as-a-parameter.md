---
redirect_from:
  - "/community/topic/how-do-i-pass-a-method-as-a-parameter/"

layout: "topic"
title: "How do I pass a method as a parameter."
date: "2024-04-03"
permalink: "/forums/topic/how-do-i-pass-a-method-as-a-parameter/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**OlleCarlberg** · April 3, 2024 at 4:07 am

Hi!
All feedback is welcome.

I have class A with method “run and class B with methods “method1” and “method2”.

I want to call a function from B from class A.

In class A I have a “run” method that should be able to execute both “method1” and “method2” from class B.
Option 1:
The method that should be executed should be sent as a parameter. (Don’t know if this is possible).

Option 2:
Create an object of Class x to run the method. Then I need to pass the Class name and the method name to be avle to create the object inside the run method.

Option 3:
As described by Kent Beck in ‘Test-Driven Development’ he uses the following python code which we want to mimic:
Def run(self):
method = getattr(self, self.name)
method()

Some background:
I am aiming to create a Unit Testing Framework. In the beggining I am using Kent Becks xUnit example from the book ‘Test-Driven Development’

Thanks!

---

**John Wolfe** · April 4, 2024 at 5:31 pm

While passing a method as a parameter is not directly supported by the language, there may be a few ways to achieve a similar effect. The language supports deferred (polymorphic) operations, and polymorphic events. It also supports passing of instance references and event instances as parameters.
Separately, a testing framework exists here: [https://github.com/MaileTechnical/TestFramework](https://github.com/MaileTechnical/TestFramework)

---

**OlleCarlberg** · April 5, 2024 at 9:41 am

Thanks!

Another question :)

I have a superclass and a subclass. I have created an instance of the subclass and want to call a operation from the superclass.
I saw there was a button in BridgePoint that said “defer operation” so I tried it with the relation to the subclass and noticed the superclass operation was also created in the subclass (Because I checked the “required” checkbox).

I tried running it in the Model Verifier by calling the function but since I don’t want to implement the behavior inside the subclass operation and instead use the superclass operation it did not work since I believe it used the empty operation from the subclass.
I read from an older post that the Model Verifier did not support deferred operations (yet). This post was from 2021 so I’m not sure if it has updated or if still does not work.

---

**cort** · April 5, 2024 at 9:45 am

It is still unsupported in Verifier.
It is supported in the MASL C++ and Ciera (OAL) model compiler.

---

**John Wolfe** · April 5, 2024 at 2:10 pm

Deferred operations are supported in Verifier. When you check the “required” box, it forces you to implement the method in the subtype. If that is not what you want, then uncheck that box, and it should work as you expect.
