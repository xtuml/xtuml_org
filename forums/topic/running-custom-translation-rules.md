---
redirect_from:
  - "/community/topic/running-custom-translation-rules/"

layout: "topic"
title: "running custom translation rules?"
date: "2014-11-27"
permalink: "/forums/topic/running-custom-translation-rules/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**sfinnie** · November 27, 2014 at 1:57 pm

Just like buses, 2 posts in one day :).

I’m trying to run some custom archectypes over a model. xtumlmc_gen_erate is failing, I expect bwcause I don’t have the correct db structure. Steps as follows:

1\. Export model from BP (right click project, select “Export…”, xtUML model), choose model, finish.
2. Run the script below.

Result is lots of errors like:

    foo.xtuml: 1577:  ERROR:  Object 'S_SYS_PROXY' Unknown.
    foo.xtuml: 1577:  ERROR:  Aborting commitment of ALL SQL statements.

Batch file used to run it as follows:

    @echo off
    set PATH=%PATH%;C:\sf\bin\xtuml-full-4.2\eclipse_extensions\BridgePoint\eclipse\plugins\com.mentor.nucleus.bp.core.win32.x86_4.2.0\os\win32\x86\lib
    set PATH=%PATH%;C:\sf\bin\xtuml-full-4.2\eclipse_extensions\BridgePoint\eclipse\plugins\com.mentor.nucleus.bp.core.win32.x86_4.2.0\bridgepoint\win32\client\bin
    REM set OOASCHEMA=C:\sf\bin\xtuml-full-4.2\eclipse_extensions\BridgePoint\eclipse\plugins\com.mentor.nucleus.bp.dap.pkg_4.2.0\bridgepoint\xtumlmc_schema.sql
    set OOASCHEMA=C:\sf\bin\xtuml-full-4.2\eclipse_extensions\BridgePoint\eclipse\plugins\com.mentor.nucleus.bp.mc.c.source_4.2.0\mc3020\schema\sql\xtumlmc_schema.sql
    REM set MGLS_LICENSE_FILE=%~d0\sf\bin\xtuml-full-4.2\license\license.dat
    set TDB=foo.tdb

    call xtumlmc_gen_erate.cmd -arch ooa2rdb.rule -d 1 -import foo.xtuml -e foo -nopersist -v STMT

    del %TDB%

Thanks for any suggestions.

- This topic was modified 10 years, 9 months ago by [![](https://secure.gravatar.com/avatar/ea6d2e68d9e24480faf46673da88124c2c221ff2d8107d66a7a34d3548928a08?s=14&amp;d=mm&amp;r=g)Bob Mulvey]({{ '/user/rmulvey/' | relative_url }}).

---

**cort** · December 1, 2014 at 5:18 pm

You can run your model compiler from within BridgePoint. Here is how: [https://www.youtube.com/watch?v=EonNPFltfAI](https://www.youtube.com/watch?v=EonNPFltfAI)

A short-cut of playing with model compilers is shown at about 10 minutes into this video. You can write RSL (archetype language) directly inside of a marking file to go really quick-and-easy.

Cort
