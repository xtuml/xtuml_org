---
redirect_from:
  - "/community/topic/how-to-run-rule-files-from-the-command-line/"

layout: "topic"
title: "How to run rule files from the command line?"
date: "2014-04-16"
permalink: "/forums/topic/how-to-run-rule-files-from-the-command-line/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**sfinnie** · April 16, 2014 at 12:27 pm

I’m using the xtuml editor (not BP,so no verifier / model compiler). I’ve written some some rules files that I want to run over my models, however I can’t get it to work. Would appreciate any suggestions.

What I’m doing:

1\. Export model from the editor – produces file ‘go.xtuml’. Seems fine
2. Run a .cmd file with the following contents:

\[code title=””\]
set PATH=%PATH%;C:\sf\bin\xtUMLEditor\eclipse_extensions\BridgePoint\eclipse\plugins\com.mentor.nucleus.bp.core.win32.x86_4.1.2\os\win32\x86\lib
set PATH=%PATH%;C:\sf\bin\xtUMLEditor\eclipse_extensions\BridgePoint\eclipse\plugins\com.mentor.nucleus.bp.core.win32.x86_4.1.2\bridgepoint\win32\client\bin
call xtumlmc_gen_erate.cmd -arch ooa2rdb.rule -d 1 -import go.xtuml -e foo -nopersist -v STMT
\[/code\]

It fails with a pop up dialogue saying “Failed to load required MGLS dll”. OK’ing that pops up another that says:

“gen_erate

The system could not find the environment option that was entered
(
C:\sf\bin\xtUMLEditor\eclipse_extensions\BridgePoint\eclipse\plugins\com.mentor.nucleus.bp.core.win32.x86_4.1.2\bridgepoint\win32\client\bin
)

Thanks for any pointers.

– Scott.

PS: the ‘-e foo’ argument is only there because the help files say it has to be present but the value doesn’t matter.

---

**sfinnie** · April 16, 2014 at 2:28 pm

EDIT: I changed tack to use pt_gen_import/pt_gen_file:

\[code title=””\]@echo off
set PATH=%PATH%;C:\sf\bin\xtUMLEditor\eclipse_extensions\BridgePoint\eclipse\plugins\com.mentor.nucleus.bp.core.win32.x86_4.1.2\os\win32\x86\lib
set PATH=%PATH%;C:\sf\bin\xtUMLEditor\eclipse_extensions\BridgePoint\eclipse\plugins\com.mentor.nucleus.bp.core.win32.x86_4.1.2\bridgepoint\win32\client\bin
set OOASCHEMA=C:\sf\bin\xtUMLEditor\eclipse_extensions\BridgePoint\eclipse\plugins\com.mentor.nucleus.bp.dap.pkg_4.1.2\bridgepoint\xtumlmc_schema.sql
set TDB=go.tdb

REM call xtumlmc_gen_erate.cmd -arch ooa2rdb.rule -d 1 -import go.xtuml -e foo -nopersist -v STMT

del %TDB%
REM Load XTUML schema (1)
call pt_gen_import %TDB% %OOASCHEMA%
REM load the model (2)
call pt_gen_import %TDB% go.xtuml
REM call pt_gen_file %TDB% ooa2rdb.rule\[/code\]

The binaries execute properly and the schema loads fine (1). However loading the model (2) fails because the schema doesn’t include tables for the graphical data. Not sure how to resolve this? can’t find another schema file that includes graphics tables; and can’t see a way to export model from the modeller without the graphical data.

Any pointers?

Thanks.

---

**cort** · April 22, 2014 at 1:20 pm

Hi Scott,
You are attempting to run the “generator” (model compiler) which is not technically part of the xtUML Editor (even though some of the files may be present). You will need the (licensed) BridgePoint tool to accomplish your task.
Regards,
Cort

---

**sfinnie** · April 22, 2014 at 2:12 pm

Hi Cort, thanks for the reply.

In that case I’d like to investigate the Java API you mention [here]({{ '/forums/topic/how-to-get-model-data-from-and-xtuml-model/' | relative_url }}) . Can you point to any documentation? Thanks.

– Scott.

PS: Just noticed [another post asking the same question]({{ '/forums/topic/model-extraction-from-xtuml-editor/' | relative_url }}). I’ll track that question so you don’t need to answer twice.
