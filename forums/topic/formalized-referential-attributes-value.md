---
redirect_from:
  - "/community/topic/formalized-referential-attributes-value/"

layout: "topic"
title: "Formalized referential attributes value"
date: "2023-09-08"
permalink: "/forums/topic/formalized-referential-attributes-value/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Schmill** · September 8, 2023 at 9:11 pm

Hi there, I’m facing a behavior I cannot understand.
Under certain configuration, when relating one element to another trough a formalized association, the referential attributes do not update.
When I tested this in a small model the behavior was not observed. therefore, I believe that this is something specific to my model that may be broken.
Is this the expected behavior? what am I doing wrong? is there any known work around?

Thank you.

---

**Schmill** · September 8, 2023 at 10:38 pm

Correction, instead of element I meant ‘object’ where the OAL of the relation is:

`create object instance prop of PR;`
`prop.Name = param.property;`
`relate prop to self across R4.'owned by';`

---

**cort** · September 9, 2023 at 8:32 am

What is your execution context? Verifier? MC-3020?

I believe both Verifier and MC-3020 will propagate the values to the referentials.

I will state that some modelers consider it dubious to read referential attribute values and insist that you navigate to the source class and read the identifier there.

My use of referential attributes is strictly for when they constrain an association. …but I digress.

---

**Schmill** · September 9, 2023 at 8:39 pm

Okay I think I understand, this is a big one for me.
Thank you.
