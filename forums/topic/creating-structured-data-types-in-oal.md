---
redirect_from:
  - "/community/topic/creating-structured-data-types-in-oal/"

layout: "topic"
title: "Creating Structured Data Types in OAL"
date: "2016-01-11"
permalink: "/forums/topic/creating-structured-data-types-in-oal/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dennis Tubbs** · January 11, 2016 at 7:37 pm

I have created a structured data type and assigned the return value of a class operation to this type. How do I create an instance of the type in the OAL so I can assign values to the members and return it? I cannot find the documentation for this syntax and am not having any success with the trial and error method.

---

**poj** · January 11, 2016 at 8:12 pm

As far as I know, the only way to create a value of a structured data type is to have something that is already of that data type, and copying it.
The easiest way to create a value of a structured data type is to have an attribute of a class, and then reading that attribute.

---

**Dennis Tubbs** · January 11, 2016 at 9:12 pm

Should I write this up as a defect? It seems to me the structured data type is not treated consistent with the other data types.

---

**poj** · January 11, 2016 at 10:29 pm

Actually it is at least partially consistent, however it is strange.

Look at the case where you want to create a local variable in OAL:
\[code title=””\]
Var_A = \<expression\>
\[/code\]
the type of Var_A is derived from the type of the right hand expression. However, there are no “primitive” expression that can have a structure type.

For arrays in OAL, you can actually create an array in action code by assigning to the last item in the array:
\[code title=””\]
Var_B\[17\] = \<expression\>;
\[/code\]
Var_B is now an array of 18 elements, accessed from 0 to 17, however the “type” of Var_B can be seen as an anonymous type that is an array of the type of the expression. Looking at the meta-model, xtUML is actually lacking named types with dimensions. Only specific objects of a data type may have dimensions. In most cases this does not lead to any problems, but there are cases when mapping towards legacy code that is hard to handle without specific model compiler extensions.

It would be nice to have support for declaring the type of a variable properly. That would require adding constructs to OAL. One quick idea would be to fomulate that as
\[code title=””\]
declare Var_A as Type_Name;
declare Var_B as instance reference of Key_Letters
declare Var_C as instance reference set of Key_Letters
\[/code\]
The last variant is perhaps not so useful, since instance sets are lacking useful operations for modifying them.
The last two are used when needing to bring a variable name into a scope, and for the model interpretation and model compiler we use at work, we have defined that Var_B case is written as
\[code title=””\]
select any Var_B from instances of Key_Letters where (False);
\[/code\]
Literal false where clauses on select from instances of are special cased, and only results in bringing the variable into the correct scope.

---

**Lee Riemenschneider** · January 12, 2016 at 12:26 am

In the Var_B example, why the where clause? An assignment is made, but does that matter?

As far as structured datatypes go, as an xtUML purist, they should only be allowed for copy and compare operations with no internal access or assignments. If you need access/assignment, then they should be defined as a class in the domain.

---

**Dennis Tubbs** · January 12, 2016 at 2:35 am

This all makes sense. In my case I am not translating but documenting a Python program with a class diagram. I didn’t want to create a new class because the program will be using a Python data structure, so it seemed more appropriate to use a structured data type.

---

**poj** · January 12, 2016 at 6:56 am

The use of the where clause in the Var_B example becomes clearer in a longer segment of code.
\[code title=””\]
//Cs is a set of instances of class Class_C
select any Var_B from instances of Class_B where (False);
for each C in Cs
if (C.Foo)
select any Var_B related by C-\>Class_B\[R47\];
end if;
end for;
\[/code\]
This segment can be seen as a select from instances of Class_B with a where clause acting on a related class. Without the where-clause, the value of Var_B would be something unreasonable after the for-loop.

Actually, there is nothing in xtUML that says that an assignment is done at that point. By analyzing the body, a model compiler can easily remove an unnecessary assignment.

But back to the original question. In most cases, you should avoid structured data types, but when interfacing the outside world it is sometimes useful to be able to create values of a structured data type easily. For example when doing tests on your modeled domain, and you want to create a small model of the surrounding world that returns a value to your main concern.

---

**Lee Riemenschneider** · January 12, 2016 at 4:28 pm

An empty Var_B after the loop (assuming no C.Foo). Nice tip.

---

**john** · January 12, 2016 at 7:25 pm

One might also imagine an action language that support some kind of data type constructors, e.g:

\[code\]
my_variable = My_Structure_Type();
\[/code\]

Or to be more OAL like:
\[code\]
create transient variable my_variable of My_Structure_Type;
\[/code\]

Come to think of it, the later should probably be quite easy to add to the current OAL grammar.

---

**Lee Riemenschneider** · January 13, 2016 at 7:05 pm

Why not just make the structures invisible classes and use the OAL for class accesses.

create a structure data type: user_structured_DT_t;

create object instance of struct_var of user_structured_DT_t;
struct_var.member_1 = 10;
struct_var.member_2 = “string”;

Of course if you wanted to allow them to be class members with accessible members, you’d have to allow: instance.struct.member notations.

This would all have to be added to the “Invisible” OOAofOOA subsystem. :-J

---

**Lee Riemenschneider** · May 17, 2017 at 3:34 pm

Recent discussion found the QMARK in OAL syntax, where assignment of QMARK creates an out of scope variable placeholder. This doesn’t allow the variable to be conditionally assigned a type, and it doesn’t let it be assigned via a select statement.

Using the above example:
//Cs is a set of instances of class Class_C
Var_B = ?;
for each C in Cs
if (C.Foo)
select any B related by C-\>Class_B\[R47\];
Var_B = B; \<--- workaround for lack of select usage end if; end for; if (empty Var_B) end if; More discussion [here]({{ '/forums/topic/why-does-bridgepoint-grammar-allow-as-rval/' | relative_url }}).

---

**Lee Riemenschneider** · May 17, 2017 at 3:51 pm

The other discussion I referenced shows that Verifier doesn’t work properly with the QMARK, so you might not want to use it.
