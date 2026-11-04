---
redirect_from:
  - "/community/topic/attention-model-compiler-writers-r4700-removed/"

layout: "topic"
title: "Attention Model Compiler Writers - R4700 removed"
date: "2015-05-18"
permalink: "/forums/topic/attention-model-compiler-writers-r4700-removed/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**keithbrown** · May 18, 2015 at 1:25 pm

To model compiler writers,

In BridgePoint 5.0 we added a new feature to show port names under component references, instead of simply interface names. In order to support this feature, we added a new class to the OOAofOOA named “Port Reference” (keyletters CL_POR) and modified the relationships between “Component Reference” (CL_IC) and “Imported Reference” (CL_IIR).

\[code title=””\]orig: CL_IC\[R4201\]-\>CL_IIR\[R4700\]
new: CL_IC\[R4201\]-\>CL_POR\[R4707\]-\>CL_IIR\[R4708\]\[/code\]

The end result is that any model compiler archetypes which use R4700 must be changed to use the new traversal. This change should have been noted in the Release Notes for BridgePoint 5.0 and was inadvertently left out.

- This topic was modified 10 years, 9 months ago by [![](https://secure.gravatar.com/avatar/ea6d2e68d9e24480faf46673da88124c2c221ff2d8107d66a7a34d3548928a08?s=14&amp;d=mm&amp;r=g)Bob Mulvey]({{ '/user/rmulvey/' | relative_url }}).
