---
redirect_from:
  - "/community/topic/activity-diagrams/"

layout: "topic"
title: "Activity Diagrams"
date: "2019-04-28"
permalink: "/forums/topic/activity-diagrams/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Rob** · April 28, 2019 at 3:11 am

I have not seen much in the tutorials about the activity diagrams but they are in the xtUML perspective. Are there ways to make the models executable utilizing the activity diagrams? Can the activity diagrams contain OAL? If not, what is the purpose of the activity diagram with xtUML? Do they just provide amplifying information?

---

**cort** · April 29, 2019 at 12:38 am

Rob,

In the long-time past, BridgePoint supported only class diagrams, state machines and a bit of packaging. OAL was supported in the state machines and later in domain functions. This was the original base of Shlaer-Mellor modeling.

Enter UML. UML supports many diagrams. So these diagrams were added to BridgePoint. Use Case, Sequence, Activity and Communication diagrams were added. These are useful to define/describe individual scenarios of an application. They are not part of the solution but part of description of the solution.

The components, class diagrams and state machines represent the executable portion of the solution.

Note, there is a way to connect (“formalize”) the elements in the Use Case, Activity, et al to the executable elements. Let me know if you are interested.

Note, there is a way to configure the user interface of BridgePoint to support only the diagram and element types that you want to use in your work.

Regards,
Cort

---

**Rob** · April 29, 2019 at 11:04 pm

Cort,

Yes, I am interested in the way to connect (“formalize”) the elements in the Use Case, Activity, et al to the executable elements.

Thanks,
Rob

---

**cort** · April 30, 2019 at 12:40 am

When you have a class, component, message or other element in some informal (non-executable) diagram, you can right-click on the element and select ‘Formalize’ from the context menu. You can then select an element from the executable specification model. This presses you to treat elements in the informal diagrams more carefully. It causes you to consider carefully elements you may have in these diagrams that have no counterpart in the executable solution model.
