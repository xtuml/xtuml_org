---
redirect_from:
  - "/community/topic/component-data-type-conversion-in-inteface/"

layout: "topic"
title: "Component Data Type Conversion In Inteface"
date: "2013-10-31"
permalink: "/forums/topic/component-data-type-conversion-in-inteface/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dennis Tubbs** · October 31, 2013 at 2:07 pm

Hi,

I am wondering what the best practice is for converting data specific to one component to the data used by another component, which is interfaced to it, without compromising the re-usability of the components. For example, consider a generic IO component that performs operations like Set(PortA, Pin7, True) and another application component interfaced to the IO component performing operations like Enable(MicrowaveLight). Does the mapping from {MicrowaveLight} to {PortA, Pin7} occur within the interface operations and signals, thus making the interface custom for each interface formalization? Or, would you wrap the IO component within another application specific component (maybe called Microwave_IO) and put the conversion code within that component? Or is there another better way?

Thanks,
Dennis

---

**Martin** · November 1, 2013 at 2:34 pm

Hi,

My thoughts and how we work is that you need another component (a bridging domain) that is the bridge between the components (the domains). I think this is one conceptual way of still thinking domains and bridges and using the components and interfaces defined by BridgePoint xtUML.
Traditional the bridging domain was not visible at the system level and only implemented in source code, or maybe in marking. I think this is a good way of making them more visible at the complete system level.
Further it is possible to also in the bridging domain split one signal/operation/message/bridge being sent to many receivers.

---

**Lee Riemenschneider** · November 6, 2013 at 2:28 pm

[@DTubbs]({{ '/user/dtubbs/' | relative_url }}) I have usually handled these cases by custom (hand-coded) bridge logic for each implementation. You can then manage these custom bridges via your configuration management scheme, so you can still build your old system when you change to a new processor.

[@Martin]({{ '/user/martin/' | relative_url }}) “Bridging Domain” sounds like an oxymoron. Bridges are visible on the system model, and they should be able to be connected to multiple domains.

I have noticed some issues with xtUML Editor’s use of interfaces, which make them less usable than the previous way of handling bridges. Maybe this is bringing up issues to handling [@DTubbs]({{ '/user/dtubbs/' | relative_url }}) concerns and why [@Martin]({{ '/user/martin/' | relative_url }}) is proposing bridges as components. ???
