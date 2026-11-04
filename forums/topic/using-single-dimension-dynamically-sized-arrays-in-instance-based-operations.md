---
redirect_from:
  - "/community/topic/using-single-dimension-dynamically-sized-arrays-in-instance-based-operations/"

layout: "topic"
title: "Using single-dimension, dynamically-sized arrays in instance-based operations"
date: "2022-11-17"
permalink: "/forums/topic/using-single-dimension-dynamically-sized-arrays-in-instance-based-operations/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**ablair** · November 17, 2022 at 4:06 pm

Hi, I’m struggling with BP. I want to create an instance-based operation with no parameters that returns a single-dimension array of integers … but I don’t know in advance the size of the array.
Via the Properties view, I’ve declared that the Return Array Dimension for the operation is \[\]
I’m using OAL to define the operation. Can someone please illustrate how I might capture integral values as array elements in the body of the operation, and then return the array of values? I’m lost!
TIA.
\[Once I understand how to return 1D arrays of values from an operation, I’m assuming that I can use this mechanism within the Model Verifier(?)\]

---

**Bob Mulvey** · November 17, 2022 at 4:34 pm

Hi Alasdar,

I hope I am not leading you down a rabbit hole. It has been a long time since I have look at this. However, when looking for examples I think about the BridgePoint unit tests and manual test cases. I see this issue which describes array annual tests:
[https://support.onefact.net/issues/1995](https://support.onefact.net/issues/1995)

Notes in that issue read there is a test model.issue, but it may be worth looking at.

I do recall development notes written about this too, but searching quickly I am not seeing them.

Bob

---

**cort** · November 17, 2022 at 4:36 pm

…at the moment, I do not have time to look at an example model, but I can make a couple of comments.

1\) There are setting in the BridgePoint preferences to enable/disable fixed and dynamic arrays.
2) Array support came in BridgePoint relatively late in the game, and support is mixed, but I am pretty sure that Verifier supports anything that the editor supports.
3) You may have better luck passing a reference parameter rather than trying to return an array. This is what I wanted to check on.

---

**ablair** · November 17, 2022 at 7:06 pm

Thanks Bob, Cort. I’ll look into your suggestions.

---

**John Wolfe** · November 18, 2022 at 1:00 am

Verifier supports arrays, including variable-length ones. But, at the moment, I cannot remember the magic for declaring a variable-length array as a temporary variable. I think I’ve done it in the past, so let me know if it matters to you, and I’ll try to recall how to do it.
In any case, here is an example of an instance-based operation returning a variable-length array of integers. It uses an attribute declared as a variable-length array to collect the values and then returns the value of that attribute.
[https://github.com/johnrwolfe/ArrayReturn](https://github.com/johnrwolfe/ArrayReturn)

---

**ablair** · November 18, 2022 at 5:50 am

Many thanks, John. The syntax needed is clear from your example … and I think I can live without the variable-length array as a temp variable.
Thanks all!
