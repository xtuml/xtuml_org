---
redirect_from:
  - "/community/topic/why-does-bridgepoint-grammar-allow-as-rval/"

layout: "topic"
title: "Why does BridgePoint grammar allow ? as rval"
date: "2015-09-30"
permalink: "/forums/topic/why-does-bridgepoint-grammar-allow-as-rval/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Bob Mulvey** · September 30, 2015 at 4:32 pm

In discussion today, the BP oal grammar was discussed (QMARK in [https://github.com/xtuml/bridgepoint/blob/master/src/org.xtuml.bp.als.oal/bnf/oal.bnf](https://github.com/xtuml/bridgepoint/blob/master/src/org.xtuml.bp.als.oal/bnf/oal.bnf) ). Specifically, there is support for an rval of ? (qmark in oal.bnf). Looking at the current implementation for this token I see no valid use case. Furthermore, there is inconsistency between the parser and verifier here (parser allows something that the verifier does not support).

Consider:

Example 1 (this IS currently valid syntax AND executes):
test=1;
test=?;
LOG::LogInteger(message:test);
// This displays the value 1

Example 2 (this is valid syntax, but execution fails on the first assignment because there is no type defined type in BPValue::getValueString):
test=?;
test=1;

I could see where example 2 could be useful to allow syntax where there was an unknown value or even unknown type that was initialized later, for example:

example 3 (not supported by the parser):
test=?
if (test==?)
test=1;
else
test=”string”; // parser error, type already defined
end if;

Does anyone understand the history of why this rval “?” is present?

---

**Lee Riemenschneider** · May 17, 2017 at 3:41 pm

In [this discussion]({{ '/forums/topic/creating-structured-data-types-in-oal/' | relative_url }}), a workaround was shown for how to create an out-of-scope unassigned inst_ref variable. The QMARK seems to be what was put into OAL for this purpose with any type of data variable.

The problem with inst_ref is the QMARK variable can’t be used inside a select, so a workaround must still be used.
ref = ?;
if (true)
select object instance foo of BAR;
ref = foo;
end if;
if (empty ref)
end if;

Verifier should probably support the QMARK. MC-3020 seemed to handle it OK in an experiment I ran.

In a discussion yesterday, Levi and I surmised that the proper handling of no assignment should be a default value for the type.
e.g.,
ref = ?;
if (false)
select object instance foo of BAR;
ref = foo;
end if;
ref will be empty here due to no assignment.

- This reply was modified 8 years, 9 months ago by [![](https://secure.gravatar.com/avatar/2beeed50ad01495a2bb8456ccfd23100a3ae303e29fc1a90ee450c7cf5e79641?s=14&amp;d=mm&amp;r=g)Lee Riemenschneider]({{ '/user/lwriemen/' | relative_url }}).
