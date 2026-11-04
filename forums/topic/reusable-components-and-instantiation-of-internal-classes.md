---
redirect_from:
  - "/community/topic/reusable-components-and-instantiation-of-internal-classes/"

layout: "topic"
title: "Reusable Components and Instantiation of Internal Classes"
date: "2014-01-09"
permalink: "/forums/topic/reusable-components-and-instantiation-of-internal-classes/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dennis Tubbs** · January 9, 2014 at 3:50 pm

Is there a good method to instantiate the classes within a reusable component? I would like to be able to have some simple OAL within the component, or at least scoped to be within the component, like the following:
create object instance
relate object instance
etc.

However, once this OAL is placed within the component the component is no longer reusable in a different application. For example, a component that handles IO. One option is to copy and paste but I do not consider that reuse. Another option would be to create an interface and serialize the commands to instantiate the class diagram for any particular use, but this seems cumbersome.

Has anyone considered this and found a good solution? Are components really reusable?

Thanks,
Dennis

---

**Dennis Tubbs** · January 10, 2014 at 7:43 pm

I found the answer in the “BridgePoint Model Compiler – User’s Guide”.

---

**cort** · February 11, 2014 at 7:09 pm

Dear Dennis,

Sorry for not responding to this post right away. Hopefully, what you found in the manual is sufficient. But here are some additional thoughts.

The manual describes an “initialization function”. Such a function can be marked to run at system start. Your model can contain more than one initialization function. Different markings can enable/disable the various initialization sequences. This allows the same model to be used in various configurations.

Another option is to use messaging. You can have “start” messages that are received by the component from another component responsible for sequencing initialization. To reuse initialization functions, the message can invoke your initialization functions.

Just some options.

Regards,
Cort
