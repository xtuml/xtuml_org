---
redirect_from:
  - "/community/topic/using-deferred-operations-in-the-model-verifier/"

layout: "topic"
title: "Using deferred operations in the Model Verifier"
date: "2021-12-06"
permalink: "/forums/topic/using-deferred-operations-in-the-model-verifier/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**ablair** · December 6, 2021 at 11:27 am

Does the Model Verifier (latest version of BP as of end Nov 2021) support “deferred operations”?
I have found a mechanism in the BP menu system to define a “deferred operation”, and I appear to have found, within one of the BP guides, a description of the use of Properties to differentiate deferred operations at supertype and subtype levels using Action Language Dialects (specifically None & MASL). But I’ve yet to figure out how to actually use a “deferred operation” with the Model Verifier. Any help from a BP/Model Verifier user would be much appreciated.

---

**cort** · December 6, 2021 at 3:40 pm

The Model Verifier does not (yet) support deferred operations.
The editor does support them.
The Ciera model compiler supports them.

This issue in the issue tracker was raised about a year ago to track support of deferred operations for Verifier:
[https://support.onefact.net/issues/10129](https://support.onefact.net/issues/10129)

It is a nice feature; it just needs a bit of time and resource to complete.
