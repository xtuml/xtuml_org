---
redirect_from:
  - "/community/topic/how-to-sort-schemas-for-compare-and-merge/"

layout: "topic"
title: "How to sort schemas for compare and merge"
date: "2015-09-01"
permalink: "/forums/topic/how-to-sort-schemas-for-compare-and-merge/"
forum: "Miscellaneous"
forum_slug: "miscellaneous"
forum_url: "/forums/miscellaneous/"
---

**Bob Mulvey** · September 1, 2015 at 11:25 pm

Here is a tip that someone may come looking for some day that I hope is as useful for you as it was for me. In making some changes to the BridgePoint metamodel recently I found myself in need of a way to easily compare copies of the ooaofooa schema before and after changes. In this case, the schema was produced by tool in the bridgepoint build chain, so the format was what you see in the example below. The problem was that the copies I had were in different order which made it very hard to diff. In case you do not know what I mean by schema, what I mean is the file being specified to xtumlmc_gen_erate’s -import option to create schema elements. The commands in the schema file are “create ROP …” and “create TABLE …”. Examples from the ooaofooa schema are:
CREATE TABLE S_SYS (
Sys_ID UNIQUE_ID,
Name STRING,
useGlobals INTEGER );

CREATE ROP REF_ID R1405 FROM MC EP_PKG ( Direct_Sys_ID )
TO 1 S_SYS ( Sys_ID );

Here are the ilnux commands I used to sort the schema files. Thank you to Cort Starrett for providing this!
\$ cat after.sql \| grep -v ‘\\\\‘ \| tr -d ‘\015’ \| tr -d ‘\n’ \| sed ‘s/;/;\n/g’ \| sort \> a1.sql
\$ cat before.sql \| grep -v ‘\\\\‘ \| tr -d ‘\015’ \| tr -d ‘\n’ \| sed ‘s/;/;\n/g’ \| sort \> b1.sql

After sorting you can easily then use your favorite diff tool to clearly see changes.

---

**john** · September 8, 2015 at 10:12 pm

Optionally, you can also use pyxtuml, which sorts the schema by key letter and association id, and works without the prebuilder:

To install:
pip install ply –user
pip install pyxtuml –user

Example usage on ooaofooa (which takes a few seconds to parse):

python -m bridgepoint.gen_sql_schema \\
-o ooaofooa.schema.sql \\
org.xtuml.bp.core/models/org.xtuml.bp.core/ooaofooa

**Note**: the schema generator in pyxtuml ignores the “export directives” encoded in descriptions on classes and so on, so the resulting sql file may differ from other schema generators.
