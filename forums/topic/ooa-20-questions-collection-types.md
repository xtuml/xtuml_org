---
redirect_from:
  - "/community/topic/ooa-20-questions-collection-types/"

layout: "topic"
title: "OOA '20 Questions: Collection types"
date: "2019-09-26"
permalink: "/forums/topic/ooa-20-questions-collection-types/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**Lee Riemenschneider** · September 26, 2019 at 3:07 pm

# Method: Type System

### Collection types

Is the existing Type System (of classes,
user data types, enumerations and
structures) sufficient?

Are collection types (arrays, sequences,
bags, sets, dictionaries) missing from the
Method?

---

**Sean Kavanagh** · September 26, 2019 at 4:15 pm

I don’t think the introduction of traditional collection types would help people decompose their subject matters sufficiently.
I think what is missing is an external type that is mapped to data in another domain. The data would still need to be atomic in original domain but the service domain could define collection like accessors and mutators which could return primitive values or changed versions of the same type back to client domain.

---

**Lee Riemenschneider** · September 27, 2019 at 6:19 pm

What is the “existing Type System”? The one in the Mellor-Balcer book? Or (since you included structures) the one currently in BridgePoint?
I agree with Sean, but I need some clarification on the external type suggestion. If we go by the Mellor-Balcer types, then we have ordinals and collections (IIRC). The [Data Types in OOA paper]({{ '/assets/uploads/2015/10/Data-Types-in-OOA.pdf' | relative_url }}) has some discussion on ordinal, but doesn’t include collections. Would an external type for an ordinal have accessible elements if the type was known in the original domain or must it always be atomic? Collections should always be atomic.

---

**Nils** · February 17, 2020 at 1:00 pm

Since xtUML uses relational theory, which is based on set theory, we allready have all the collections we need via our set operators (select .. where …). Yes I know there are some operators missing (and highly anticipated) but lets just ignore that for the puprose of the discussion ;-).

/Nils

---

**Nils** · February 17, 2020 at 1:02 pm

Since xtUML uses relational theory, which is based on set theory, we allready have all the collections we need via our set operators (select .. where …). Yes I know there are some operators missing in Bridgepoint (and highly desired) but lets just ignore that for the puprose of the discussion ;-).

/Nils

- This reply was modified 5 years, 12 months ago by [![](https://secure.gravatar.com/avatar/fbfa4355e6d4aabc5918f55562a1246db838ff2c01ee3289ee24d56d8b0a5bfd?s=14&amp;d=mm&amp;r=g)Nils]({{ '/user/nils/' | relative_url }}).
