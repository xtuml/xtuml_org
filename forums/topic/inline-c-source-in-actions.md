---
redirect_from:
  - "/community/topic/inline-c-source-in-actions/"

layout: "topic"
title: "Inline C source in actions"
date: "2023-11-17"
permalink: "/forums/topic/inline-c-source-in-actions/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Schmill** · November 17, 2023 at 1:24 pm

The document\[1\] mention the ability to intermix target source code with action language with this example:
` /*#inline`
`// Don't Panic`
`int a = 42;`
`printf( "The answer is %d\n", a );`
`*/`
Unfortunately, adding these inline snippets does not produce anything in the generated source. I suspect that the document is out of date, but I desperately look for such functionality because my only working method now is to make changes to the model, and then build to generate the source and then overwrite the relevant file in **gen** from **src**. this is really tedious, especially when I make multiple changes to the model.

I Also tried to change the action dialect to C, but no luck there either, it does not produce any source.
What am I missing?
Many thanks!

\[1\] [https://xtuml.github.io/docs/mcug/ch02.html](https://xtuml.github.io/docs/mcug/ch02.html)

---

**cort** · November 17, 2023 at 5:16 pm

This feature was supported in the past. It is no longer supported in MC-3020.

---

**Schmill** · November 17, 2023 at 10:46 pm

Okay, thank you.
