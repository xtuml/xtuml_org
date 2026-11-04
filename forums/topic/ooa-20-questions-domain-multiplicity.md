---
redirect_from:
  - "/community/topic/ooa-20-questions-domain-multiplicity/"

layout: "topic"
title: "OOA '20 Questions: Domain Multiplicity"
date: "2019-09-26"
permalink: "/forums/topic/ooa-20-questions-domain-multiplicity/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · September 26, 2019 at 2:35 pm

# Method: System Modeling

## Domain Multiplicity

***“instances” of domains***

Can a domain be reused multiple times in the same
system? If so, how are messages directed to the correct
instance of the domain?

\[Scenario\] Consider domains ‘navigation’ and ‘braking’. A statement
within the the interior of a state action of an instance state machine in
‘navigation’ sends the ‘apply friction’ message to the “left rear
instance/instantiation” of the ‘braking’ domain.

---

**Lee Riemenschneider** · September 27, 2019 at 4:47 pm

Yes, multiple instances of a domain should be allowed. In the scenario, it states how this would be handled in the model; the navigation model would identify a “left rear braking” domain, and probably three other braking domains. The thing that the navigation model would not know is if the braking domains are all instantiations of the same domain.
Of course, this could also be handled by the navigation model defining a required service that included the target brake system as a parameter, which would then be distributed by the architecture to the correct domain instance.
