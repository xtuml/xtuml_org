---
redirect_from:
  - "/community/topic/ooa-20-questions-inter-domain-messages/"

layout: "topic"
title: "OOA '20 Questions: (Inter-domain) Messages"
date: "2019-09-26"
permalink: "/forums/topic/ooa-20-questions-inter-domain-messages/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · September 26, 2019 at 1:45 pm

# Method: System Modeling

## (Inter-domain) Messages

synchronous and asynchronous
Should there be a distinction between synchronous and asynchronous messages between domains? If so, what are the semantic differences?

synchronous
Should senders block on transmission of synchronous inter-domain messages returning no data (void)?

\[Scenario\] Consider domains ‘navigation’ and ‘braking’. A statement within the
the interior of a state action of an instance state machine in ‘navigation’ sends
the ‘apply friction’ message (invokes a terminator service) on ‘braking’.
See Action Semantics for the UML for discussion on intra-domain messaging
semantics.

---

**Lee Riemenschneider** · September 27, 2019 at 4:04 pm

Let’s start with some definitions:
**Synchronous messaging** – call and wait until completion
**Asynchronous messaging** – call and continue

If we can agree on these, then there is a very definite advantage in the analyst knowing which kind of messaging is being performed, so there should be a designation applied for all accessors (bridges, events, class operations) that can support either type of messaging.
“void” is just an indication of no return value, and if used to imply a messaging type, then another term would need to be invented for no return value.
As the block on transmission is implied by the definition of a synchronous message, it should be expected when the analyst chooses to call a synchronous bridge. However, it is possible to override this behavior in the architecture for specific platforms. This would need to be done with caution, as the model is obviously intending something to be completed.
