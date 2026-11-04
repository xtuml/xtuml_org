---
redirect_from:
  - "/community/topic/initial-state/"

layout: "topic"
title: "Initial state"
date: "2017-06-02"
permalink: "/forums/topic/initial-state/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**micke.x** · June 2, 2017 at 9:56 am

Which is the initial state of a state machine in xtUML?

Inspecting the behaviour in Model Verifier, it seems that the property State Number is used to govern this?

Is this intended or in line with xtUML semantics?
I have not been able to find where this is specified.

It also seems like the Creation Transition does not have any effect on the start transition, unless a specific event is received (i.e. there does not seem to be an implicit (or explicit) “start event” in xtUML state machines).

The semantics of the Creation Transitions seems a bit unclear to me.
Is it useful?

Regarding state numbers, xtUML book says that the numbering is arbitrary and does not imply any sequencing, so I guess this behaviour is a deviation in BP.

To me it seems fragile and a bit arbitrary to use State Number for this purpose.
Do code generators use this scheme also, or can this be realized with a different semantics compared to the Model Verifier behaviour?

---

**Levi** · June 2, 2017 at 1:28 pm

In xtUML, there is a rule that a class created by the “create” statement is initialized in the lowest numbered state (usually state 1). It is correct that the rest of the numbers have no bearing on ordering. Verifier and the C model compiler both adhere to this rule.

Creation transitions can be used to initialize an instance into any state. For example, a state machine for “class1” with 5 states could have a creation transition to state 2 assigned event “foo” and another creation transition to state 4 assigned to event “bar”. If the event “foo” is generated to “class1 creator”, the event dispatcher will create the instance and transition to state 2. Likewise if “bar” is generated, the instance will be created and immediately transition to state 4. Only for synchronous creation using the “create” statement is the lowest numbered state rule applied.

It should also be noted that with the “create” statement, the activity body of the lowest numbered state is not executed. Common patterns are to have an empty “initial” state for state 1, or to have a transition to self in state 1 that gets the lifecycle started.

We’ve actually had some good discussion recently on the xtUML community chat (“Community Chat!” link above) about this. Both of the patterns I described above are distasteful to me as they don’t seem to capture the essence of the model. I think it would be great if instead of using the “lowest number” rule, the semantics of the “create” statement are that the instance is created in an architecturally provided initial state similar to the non existent start state that is used for creation transitions. I think this would allow the model to be captured more accurately and still provide synchronous creation of instances.
