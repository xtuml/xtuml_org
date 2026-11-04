---
redirect_from:
  - "/community/topic/auto-generation-of-test-case-class-from-sequence-diagram/"

layout: "topic"
title: "Auto generation of test case class from sequence diagram"
date: "2014-12-11"
permalink: "/forums/topic/auto-generation-of-test-case-class-from-sequence-diagram/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dan George** · December 11, 2014 at 4:29 am

I just viewed Module 17, “Model Based Testing.”

AWESOME! I knew this kind of thing could be done but I’ve never been able to convince my co-workers and management to invest in it. But now I’m getting the this-is-too-good-to-be-true feeling. I’ll get over it.

Speaking of tgtbt, auto generating the test cases from sequence diagrams seems like an obvious great idea. Are there complications that don’t reveal themselves in the video?

Come to think of it, I haven’t seen any mention of model-to-model translation. In this case, I’d be generating more of a model from itself. The sequence diagram would depict the expect sequence using real components. In this case, the UI component and the rest. The compiler would generate the corresponding test case and add it to the UItb component.

---

**cort** · December 14, 2014 at 9:51 pm

People/companies are using this (or similar) test harnessing in real projects.

The primary point of model-based testing is to gain the stated benefits of modeling (abstraction and thus productivity) when testing.

This harness is nothing near ideal, but it works and provides a solid first step.

Hmm, sequence diagrams. It is not difficult to use sequence diagrams as input stimulus to testing. It is not difficult to use sequence diagrams as expected results of testing. I am not aware of automated paths to do this with BridgePoint.

Cort
