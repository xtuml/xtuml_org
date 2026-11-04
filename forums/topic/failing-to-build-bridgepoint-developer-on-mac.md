---
redirect_from:
  - "/community/topic/failing-to-build-bridgepoint-developer-on-mac/"

layout: "topic"
title: "Failing to build BridgePoint Developer on Mac"
date: "2019-09-26"
permalink: "/forums/topic/failing-to-build-bridgepoint-developer-on-mac/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**Sean Kavanagh** · September 26, 2019 at 3:23 pm

Hi All,

I’m having a problem getting BridgePoint Developer setup on my Mac,
I’ve been following the user guide closely but i’m stuck with the following problem:

\[ERROR\] Failed to execute goal org.apache.maven.plugins:maven-antrun-plugin:1.8:run (generate-ant) on project org.xtuml.bp.als: An Ant BuildException has occured: The following error occurred while executing this line:
\[ERROR\] /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.als/generate.xml:256: Unable to determine generated class
\[ERROR\] around Ant part …\<ant antfile=”/Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.als/generate.xml” target=”nb_all”/\>… @ 12:144 in /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.als/target/antrun/build-main.xml

Any help would be appreciated.

Regards, Sean.

The full log after a second run is included below:

\$ \$ ~/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/utilities/build/build_and_test_bp.sh
Starting CLI Build
Performing the build of project: org.xtuml.bp.core
Starting CLI Build
Performing the build of project: org.xtuml.bp.als
Starting CLI Build
Performing the build of project: org.xtuml.bp.ui.canvas
\[INFO\] Scanning for projects…
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.als.oal:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.als.oal/pom.xml
\[INFO\] Fetching p2.index from [http://download.eclipse.org/releases/oxygen/](http://download.eclipse.org/releases/oxygen/)
\[INFO\] Adding repository [http://download.eclipse.org/releases/oxygen](http://download.eclipse.org/releases/oxygen)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/technology/epp/packages/oxygen/](http://download.eclipse.org/technology/epp/packages/oxygen/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/technology/epp/packages/oxygen/](http://download.eclipse.org/technology/epp/packages/oxygen/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/releases/oxygen/201804111000/](http://download.eclipse.org/releases/oxygen/201804111000/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/releases/oxygen/201804111000/](http://download.eclipse.org/releases/oxygen/201804111000/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/releases/oxygen/201803211000/](http://download.eclipse.org/releases/oxygen/201803211000/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/releases/oxygen/201803211000/](http://download.eclipse.org/releases/oxygen/201803211000/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/releases/oxygen/201712201001/](http://download.eclipse.org/releases/oxygen/201712201001/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/releases/oxygen/201712201001/](http://download.eclipse.org/releases/oxygen/201712201001/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/](http://download.eclipse.org/eclipse/updates/4.7/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/](http://download.eclipse.org/eclipse/updates/4.7/)
\[INFO\] Adding repository [http://download.eclipse.org/eclipse/updates/4.7](http://download.eclipse.org/eclipse/updates/4.7)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/R-4.7-201706120950/](http://download.eclipse.org/eclipse/updates/4.7/R-4.7-201706120950/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/R-4.7-201706120950/](http://download.eclipse.org/eclipse/updates/4.7/R-4.7-201706120950/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/R-4.7.1-201709061700/](http://download.eclipse.org/eclipse/updates/4.7/R-4.7.1-201709061700/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/R-4.7.1-201709061700/](http://download.eclipse.org/eclipse/updates/4.7/R-4.7.1-201709061700/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/R-4.7.1a-201710090410/](http://download.eclipse.org/eclipse/updates/4.7/R-4.7.1a-201710090410/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/R-4.7.1a-201710090410/](http://download.eclipse.org/eclipse/updates/4.7/R-4.7.1a-201710090410/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/R-4.7.2-201711300510/](http://download.eclipse.org/eclipse/updates/4.7/R-4.7.2-201711300510/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/R-4.7.2-201711300510/](http://download.eclipse.org/eclipse/updates/4.7/R-4.7.2-201711300510/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/R-4.7.3-201803010715/](http://download.eclipse.org/eclipse/updates/4.7/R-4.7.3-201803010715/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/R-4.7.3-201803010715/](http://download.eclipse.org/eclipse/updates/4.7/R-4.7.3-201803010715/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/R-4.7.3a-201803300640/](http://download.eclipse.org/eclipse/updates/4.7/R-4.7.3a-201803300640/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/eclipse/updates/4.7/R-4.7.3a-201803300640/](http://download.eclipse.org/eclipse/updates/4.7/R-4.7.3a-201803300640/)
\[INFO\] Adding repository [https://s3.amazonaws.com/1f-outgoing/antlr_upsite](https://s3.amazonaws.com/1f-outgoing/antlr_upsite)
\[INFO\] Adding repository [http://download.eclipse.org/tools/cdt/releases/8.8.1](http://download.eclipse.org/tools/cdt/releases/8.8.1)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/tools/cdt/releases/8.8.1/r/](http://download.eclipse.org/tools/cdt/releases/8.8.1/r/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/tools/cdt/releases/8.8.1/r/](http://download.eclipse.org/tools/cdt/releases/8.8.1/r/)
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.als.oal:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.als.oal/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.als.oal:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.als.oal/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.cli:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.cli/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.cli:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.cli/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.cli:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.cli/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.debug.ui:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.debug.ui/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.debug.ui:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.debug.ui/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.debug.ui:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.debug.ui/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.doc:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.doc/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.doc:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.doc/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.doc:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.doc/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.mc.docgen:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc.docgen/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.mc.docgen:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc.docgen/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.mc.docgen:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc.docgen/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.integrity:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.integrity/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.integrity:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.integrity/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.integrity:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.integrity/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.internal.tools:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.internal.tools/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.internal.tools:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.internal.tools/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.internal.tools:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.internal.tools/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.io.image:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.io.image/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.io.image:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.io.image/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.io.image:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.io.image/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.x2m:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.x2m/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.x2m:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.x2m/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.x2m:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.x2m/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.mc:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.mc:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.mc:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.mc.masl:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc.masl/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.mc.masl:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc.masl/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.mc.masl:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc.masl/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.mc.mc3020:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc.mc3020/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.mc.mc3020:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc.mc3020/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.mc.mc3020:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc.mc3020/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.mc.java:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc.java/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.mc.java:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc.java/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.mc.java:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.mc.java/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.pkg:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.pkg/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.pkg:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.pkg/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.pkg:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.pkg/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.pkg.feature:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.pkg-feature/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.pkg.feature:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.pkg-feature/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.pkg.feature:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.pkg-feature/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.search:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.search/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.search:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.search/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.search:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.search/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.ui.graphics:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.graphics/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.graphics:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.graphics/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.graphics:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.graphics/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.ui.search:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.search/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.search:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.search/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.search:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.search/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.ui.sem:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.sem/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.sem:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.sem/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.sem:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.sem/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.core.editors:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.core.editors/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.core.editors:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.core.editors/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.core.editors:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.core.editors/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.ui.marking:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.marking/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.marking:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.marking/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.marking:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.marking/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.utilities:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.utilities/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.utilities:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.utilities/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.utilities:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.utilities/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.welcome:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.welcome/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.welcome:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.welcome/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.welcome:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.welcome/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.help.bp.mc:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.help.bp.mc/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.help.bp.mc:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.help.bp.mc/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.help.bp.mc:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.help.bp.mc/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.releng.p2:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.releng.p2/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.releng.p2:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.releng.p2/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.releng.p2:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.releng.p2/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.compare:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.compare/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.compare:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.compare/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.compare:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.compare/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.core:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.core/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.core:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.core/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.core:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.core/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.io.core:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.io.core/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.io.core:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.io.core/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.io.core:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.io.core/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.io.mdl:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.io.mdl/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.io.mdl:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.io.mdl/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.io.mdl:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.io.mdl/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.model.compare:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.model.compare/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.model.compare:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.model.compare/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.model.compare:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.model.compare/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.ui.canvas:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.canvas/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.canvas:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.canvas/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.canvas:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.canvas/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.ui.explorer:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.explorer/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.explorer:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.explorer/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.explorer:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.explorer/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.ui.properties:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.properties/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.properties:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.properties/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.properties:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.properties/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.ui.session:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.session/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.session:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.session/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.session:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.session/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.ui.text:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.text/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.text:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.text/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.ui.text:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.ui.text/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.generator:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.generator/pom.xml
\[INFO\] Fetching p2.index from [http://download.eclipse.org/releases/mars/201506241002/](http://download.eclipse.org/releases/mars/201506241002/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/releases/mars/201506241002/](http://download.eclipse.org/releases/mars/201506241002/)
\[INFO\] Adding repository [http://download.eclipse.org/releases/mars/201506241002](http://download.eclipse.org/releases/mars/201506241002)
\[INFO\] Adding repository [http://download.eclipse.org/modeling/emft/mwe/updates/releases/2.8.1](http://download.eclipse.org/modeling/emft/mwe/updates/releases/2.8.1)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/modeling/tmf/xtext/updates/releases/2.9.2/](http://download.eclipse.org/modeling/tmf/xtext/updates/releases/2.9.2/)
\[INFO\] Fetching p2.index from [http://download.eclipse.org/modeling/tmf/xtext/updates/releases/2.9.2/](http://download.eclipse.org/modeling/tmf/xtext/updates/releases/2.9.2/)
\[INFO\] Adding repository [http://download.eclipse.org/modeling/tmf/xtext/updates/releases/2.9.2](http://download.eclipse.org/modeling/tmf/xtext/updates/releases/2.9.2)
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.generator:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.generator/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.generator:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.generator/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl.ide:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl.ide/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl.ide:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl.ide/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl.ide:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl.ide/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl.ui:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl.ui/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl.ui:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl.ui/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl.ui:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl.ui/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl.feature:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl.feature/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl.feature:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl.feature/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl.feature:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl.feature/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl.updatesite:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl.updatesite/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl.updatesite:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl.updatesite/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp.xtext.masl:org.xtuml.bp.xtext.masl.updatesite:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.xtext.masl.parent/org.xtuml.bp.xtext.masl.updatesite/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.releng.parent.product:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.releng.parent.product/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.releng.parent.product:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.releng.parent.product/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.releng.parent.product:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.releng.parent.product/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.releng.parent.product-dev:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.releng.parent.product-dev/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.releng.parent.product-dev:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.releng.parent.product-dev/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.releng.parent.product-dev:6.19.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.releng.parent.product-dev/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.mctools:1.0.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.mctools/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.mctools:1.0.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.mctools/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.mctools:1.0.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.mctools/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.jre:1.0.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/packaging/features/org.xtuml.bp.jre/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.jre:1.0.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/packaging/features/org.xtuml.bp.jre/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.jre:1.0.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/packaging/features/org.xtuml.bp.jre/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.docgen:1.0.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/packaging/features/org.xtuml.bp.docgen/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.docgen:1.0.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/packaging/features/org.xtuml.bp.docgen/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.docgen:1.0.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/packaging/features/org.xtuml.bp.docgen/pom.xml
\[INFO\] Computing target platform for MavenProject: org.xtuml.bp:org.xtuml.bp.MinGW:1.0.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/packaging/features/org.xtuml.bp.MinGW/pom.xml
\[INFO\] Resolving dependencies of MavenProject: org.xtuml.bp:org.xtuml.bp.MinGW:1.0.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/packaging/features/org.xtuml.bp.MinGW/pom.xml
\[INFO\] Resolving class path of MavenProject: org.xtuml.bp:org.xtuml.bp.MinGW:1.0.0-SNAPSHOT @ /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/packaging/features/org.xtuml.bp.MinGW/pom.xml
\[INFO\] ————————————————————————
\[INFO\] Reactor Build Order:
\[INFO\]
\[INFO\] org.xtuml.bp.releng.parent \[pom\]
\[INFO\] org.xtuml.bp.als \[pom\]
\[INFO\] org.xtuml.bp.releng.parent.generation \[pom\]
\[INFO\] org.xtuml.bp.core \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.als.oal \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.ui.text \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.ui.properties \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.ui.explorer \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.ui.canvas \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.ui.session \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.ui.graphics \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.io.core \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.debug.ui \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.io.mdl \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.utilities \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.model.compare \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.mc \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.mc.java \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.cli \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.doc \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.io.image \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.mc.docgen \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.integrity \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.internal.tools \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.x2m \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.mc.masl \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.mc.mc3020 \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.pkg \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.compare \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.search \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.ui.search \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.ui.sem \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.ui.marking \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.welcome \[eclipse-plugin\]
\[INFO\] org.xtuml.help.bp.mc \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.core.editors \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.pkg.feature \[eclipse-feature\]
\[INFO\] org.xtuml.bp.releng.p2 \[eclipse-repository\]
\[INFO\] org.xtuml.bp.xtext.masl.parent \[pom\]
\[INFO\] org.xtuml.bp.xtext.generator \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.xtext.masl \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.xtext.masl.ide \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.xtext.masl.ui \[eclipse-plugin\]
\[INFO\] org.xtuml.bp.xtext.masl.target \[eclipse-target-definition\]
\[INFO\] org.xtuml.bp.xtext.masl.feature \[eclipse-feature\]
\[INFO\] org.xtuml.bp.xtext.masl.updatesite \[eclipse-repository\]
\[INFO\] org.xtuml.bp.jre.parent \[pom\]
\[INFO\] org.xtuml.bp.jre \[eclipse-feature\]
\[INFO\] org.xtuml.bp.MinGW.parent \[pom\]
\[INFO\] org.xtuml.bp.MinGW \[eclipse-feature\]
\[INFO\] org.xtuml.bp.docgen.parent \[pom\]
\[INFO\] org.xtuml.bp.docgen \[eclipse-feature\]
\[INFO\] org.xtuml.bp.mctools.parent \[pom\]
\[INFO\] org.xtuml.bp.mctools \[eclipse-feature\]
\[INFO\] org.xtuml.bp.releng.parent.product \[eclipse-repository\]
\[INFO\] org.xtuml.bp.releng.parent.product-dev \[eclipse-repository\]
\[INFO\]
\[INFO\] ————–\< org.xtuml.bp:org.xtuml.bp.releng.parent \>—————
\[INFO\] Building org.xtuml.bp.releng.parent 6.19.0-SNAPSHOT \[1/56\]
\[INFO\] ——————————–\[ pom \]———————————
\[INFO\]
\[INFO\] — maven-install-plugin:2.4:install (default-install) @ org.xtuml.bp.releng.parent —
\[INFO\] Installing /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/releng/org.xtuml.bp.releng.parent/pom.xml to /Users/seankavanagh/.m2/repository/org/xtuml/bp/org.xtuml.bp.releng.parent/6.19.0-SNAPSHOT/org.xtuml.bp.releng.parent-6.19.0-SNAPSHOT.pom
\[INFO\]
\[INFO\] ——————-\< org.xtuml.bp:org.xtuml.bp.als \>——————–
\[INFO\] Building org.xtuml.bp.als 6.19.0-SNAPSHOT \[2/56\]
\[INFO\] ——————————–\[ pom \]———————————
\[INFO\]
\[INFO\] — maven-antrun-plugin:1.8:run (generate-ant) @ org.xtuml.bp.als —
\[WARNING\] Parameter tasks is deprecated, use target instead
\[INFO\] Executing tasks

main:

sql.depends:

sql:

schema.depends:

schema:

grammar.depends:

grammar:
\[echo\] Generating sql/oal_grammar.sql …
\[echo\] NOTE: This file has termporarily been changed to be hand-edited. See [https://support.onefact.net/issues/10322](https://support.onefact.net/issues/10322)

validate.depends:

validate:

ooa_functions.depends:

ooa_functions:
\[echo\] Collecting available OOA parser functions…
\[exec\] dyld: Library not loaded: /usr/local/opt/libffi/lib/libffi.6.dylib
\[exec\] Referenced from: /usr/local/Cellar/pypy/7.1.1_1/libexec/lib/libpypy-c.dylib
\[exec\] Reason: image not found

content_assist.depends:

content_assist:
\[echo\] Adding content assist hooks…
\[exec\] dyld: Library not loaded: /usr/local/opt/libffi/lib/libffi.6.dylib
\[exec\] Referenced from: /usr/local/Cellar/pypy/7.1.1_1/libexec/lib/libpypy-c.dylib
\[exec\] Reason: image not found

grammar_enhancer.depends:

grammar_enhancer:

compile_grammar:
\[INFO\] ————————————————————————
\[INFO\] Reactor Summary:
\[INFO\]
\[INFO\] org.xtuml.bp.releng.parent 6.19.0-SNAPSHOT ……… SUCCESS \[ 0.116 s\]
\[INFO\] org.xtuml.bp.als …………………………….. FAILURE \[ 0.524 s\]
\[INFO\] org.xtuml.bp.releng.parent.generation ………….. SKIPPED
\[INFO\] org.xtuml.bp.core ……………………………. SKIPPED
\[INFO\] org.xtuml.bp.als.oal …………………………. SKIPPED
\[INFO\] org.xtuml.bp.ui.text …………………………. SKIPPED
\[INFO\] org.xtuml.bp.ui.properties ……………………. SKIPPED
\[INFO\] org.xtuml.bp.ui.explorer ……………………… SKIPPED
\[INFO\] org.xtuml.bp.ui.canvas ……………………….. SKIPPED
\[INFO\] org.xtuml.bp.ui.session ………………………. SKIPPED
\[INFO\] org.xtuml.bp.ui.graphics ……………………… SKIPPED
\[INFO\] org.xtuml.bp.io.core …………………………. SKIPPED
\[INFO\] org.xtuml.bp.debug.ui ………………………… SKIPPED
\[INFO\] org.xtuml.bp.io.mdl ………………………….. SKIPPED
\[INFO\] org.xtuml.bp.utilities ……………………….. SKIPPED
\[INFO\] org.xtuml.bp.model.compare ……………………. SKIPPED
\[INFO\] org.xtuml.bp.mc ……………………………… SKIPPED
\[INFO\] org.xtuml.bp.mc.java …………………………. SKIPPED
\[INFO\] org.xtuml.bp.cli …………………………….. SKIPPED
\[INFO\] org.xtuml.bp.doc …………………………….. SKIPPED
\[INFO\] org.xtuml.bp.io.image ………………………… SKIPPED
\[INFO\] org.xtuml.bp.mc.docgen ……………………….. SKIPPED
\[INFO\] org.xtuml.bp.integrity ……………………….. SKIPPED
\[INFO\] org.xtuml.bp.internal.tools …………………… SKIPPED
\[INFO\] org.xtuml.bp.x2m …………………………….. SKIPPED
\[INFO\] org.xtuml.bp.mc.masl …………………………. SKIPPED
\[INFO\] org.xtuml.bp.mc.mc3020 ……………………….. SKIPPED
\[INFO\] org.xtuml.bp.pkg …………………………….. SKIPPED
\[INFO\] org.xtuml.bp.compare …………………………. SKIPPED
\[INFO\] org.xtuml.bp.search ………………………….. SKIPPED
\[INFO\] org.xtuml.bp.ui.search ……………………….. SKIPPED
\[INFO\] org.xtuml.bp.ui.sem ………………………….. SKIPPED
\[INFO\] org.xtuml.bp.ui.marking ………………………. SKIPPED
\[INFO\] org.xtuml.bp.welcome …………………………. SKIPPED
\[INFO\] org.xtuml.help.bp.mc …………………………. SKIPPED
\[INFO\] org.xtuml.bp.core.editors …………………….. SKIPPED
\[INFO\] org.xtuml.bp.pkg.feature ……………………… SKIPPED
\[INFO\] org.xtuml.bp.releng.p2 ……………………….. SKIPPED
\[INFO\] org.xtuml.bp.xtext.masl.parent ………………… SKIPPED
\[INFO\] org.xtuml.bp.xtext.generator ………………….. SKIPPED
\[INFO\] org.xtuml.bp.xtext.masl ………………………. SKIPPED
\[INFO\] org.xtuml.bp.xtext.masl.ide …………………… SKIPPED
\[INFO\] org.xtuml.bp.xtext.masl.ui ……………………. SKIPPED
\[INFO\] org.xtuml.bp.xtext.masl.target ………………… SKIPPED
\[INFO\] org.xtuml.bp.xtext.masl.feature ……………….. SKIPPED
\[INFO\] org.xtuml.bp.xtext.masl.updatesite …………….. SKIPPED
\[INFO\] org.xtuml.bp.jre.parent 0.0.1-SNAPSHOT …………. SKIPPED
\[INFO\] org.xtuml.bp.jre 1.0.0-SNAPSHOT ……………….. SKIPPED
\[INFO\] org.xtuml.bp.MinGW.parent 0.0.1-SNAPSHOT ……….. SKIPPED
\[INFO\] org.xtuml.bp.MinGW 1.0.0-SNAPSHOT ……………… SKIPPED
\[INFO\] org.xtuml.bp.docgen.parent 0.0.1-SNAPSHOT ………. SKIPPED
\[INFO\] org.xtuml.bp.docgen 1.0.0-SNAPSHOT …………….. SKIPPED
\[INFO\] org.xtuml.bp.mctools.parent 0.0.1-SNAPSHOT ……… SKIPPED
\[INFO\] org.xtuml.bp.mctools 1.0.0-SNAPSHOT ……………. SKIPPED
\[INFO\] org.xtuml.bp.releng.parent.product …………….. SKIPPED
\[INFO\] org.xtuml.bp.releng.parent.product-dev 6.19.0-SNAPSHOT SKIPPED
\[INFO\] ————————————————————————
\[INFO\] BUILD FAILURE
\[INFO\] ————————————————————————
\[INFO\] Total time: 02:00 min
\[INFO\] Finished at: 2019-09-26T15:56:05+01:00
\[INFO\] ————————————————————————
\[ERROR\] Failed to execute goal org.apache.maven.plugins:maven-antrun-plugin:1.8:run (generate-ant) on project org.xtuml.bp.als: An Ant BuildException has occured: The following error occurred while executing this line:
\[ERROR\] /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.als/generate.xml:256: Unable to determine generated class
\[ERROR\] around Ant part …\<ant antfile=”/Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.als/generate.xml” target=”nb_all”/\>… @ 12:144 in /Users/seankavanagh/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/src/org.xtuml.bp.als/target/antrun/build-main.xml
\[ERROR\] -\> \[Help 1\]
\[ERROR\]
\[ERROR\] To see the full stack trace of the errors, re-run Maven with the -e switch.
\[ERROR\] Re-run Maven using the -X switch to enable full debug logging.
\[ERROR\]
\[ERROR\] For more information about the errors and possible solutions, please read the following articles:
\[ERROR\] \[Help 1\] [http://cwiki.apache.org/confluence/display/MAVEN/MojoExecutionException](http://cwiki.apache.org/confluence/display/MAVEN/MojoExecutionException)
\[ERROR\]
\[ERROR\] After correcting the problems, you can resume the build with the command
\[ERROR\] mvn \<goals\> -rf :org.xtuml.bp.als

---

**Sean Kavanagh** · September 27, 2019 at 2:59 pm

After looking at FAQ ([https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/FAQ.md](https://github.com/xtuml/bridgepoint/blob/master/doc-bridgepoint/process/FAQ.md))
I tried deleting git/bridgepoint/src/org.xtuml.bp.als/sql/oal_grammar.sql,
and touching git/bridgepoint/src/org.xtuml.bp.als.oal/bnf/oal.bnf
and then rebuilding using build_and_test_bp.sh but I get exactly the same error.

Instead of rerunning build script, the FAQ actually suggested:
Right click on org.xtuml.bp.als/generate.xml and choose Run As… \> Ant Build…
but i don’t get any such options when I run the Developer app.

Regards, Sean.

---

**Lee Riemenschneider** · September 28, 2019 at 2:56 am

Hmmm…I’m seeing deviations between your build output and mine in this area:

main:

sql.depends:

sql:
\[echo\] Generating grammar_model.sql …
\[echo\] Using: /home/lee/devBridgePoint/tools/mc/bin/xtumlmc_build …
\[copy\] Copying 1 file to /home/lee/git/bridgepoint/src/org.xtuml.bp.als/models/org.xtuml.bp.als/grammar
\[delete\] Deleting: /home/lee/git/bridgepoint/src/org.xtuml.bp.als/models/org.xtuml.bp.als/grammar/Globals.xtuml

schema.depends:

schema:
\[echo\] Generating grammar_schema.sql …

generate.schema:

mcj_path_type:

generate.schema.absolute:

generate.schema.relative:
\[exec\] schema_gen.arc: 415: INFO: File ‘grammar_schema.sql’ CREATED

grammar.depends:

grammar:
\[echo\] Generating sql/oal_grammar.sql …
\[echo\] NOTE: This file has termporarily been changed to be hand-edited. See [https://support.onefact.net/issues/10322](https://support.onefact.net/issues/10322)

validate.depends:

validate:
\[echo\] Generating ../org.xtuml.bp.als.oal/src/org/xtuml/bp/als/oal/Oal_validate.java …
\[copy\] Copying 1 file to /home/lee/git/bridgepoint/src/org.xtuml.bp.als/gen/code_generation
\[delete\] Deleting: /home/lee/git/bridgepoint/src/org.xtuml.bp.als/gen/code_generation/ooaofooa.xtuml
\[exec\] translate_oal.inc: 40: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate literal booleans \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 42: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate literal integers \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 44: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate literal reals \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 46: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate literal strings \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 48: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate literal enums \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 50: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate attribute values \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 52: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate transient values \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 54: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate inst_ref values \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 56: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate selection values \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 58: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate inst_ref sets \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 60: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate event values \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 62: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate parameter values \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 64: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate binary operation values \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 66: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate unary operation values \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 68: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate bridge return values \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 70: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate operation return values \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 72: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate function return values \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 74: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate array element reference values \*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 80: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate if statements \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 82: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate else statements \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 84: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate for statements \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 86: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate while statements \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 88: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate else if statements \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 96: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate assignments \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 98: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate creates \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 100: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\*\* generate deletes \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 102: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate event creates \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 104: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate relates \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 106: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate unrelates \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 108: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate select from instances \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 110: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate select from instances where \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 112: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate select rel \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 114: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate select rel where \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 116: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate relate using \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 118: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate unrelate using \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 120: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate ism events \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 122: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate csm events \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 124: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate operations \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 126: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate bridges \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 128: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate functions \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 130: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate returns \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 132: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate arch controls \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 134: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate breaks \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] translate_oal.inc: 136: INFO: \*\*\*\*\*\*\*\*\*\*\*\*\* generate continues \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\[exec\] validate_gen.arc: 182: INFO: File ‘../org.xtuml.bp.als.oal/src/org/xtuml/bp/als/oal/Oal_validate.java’ CREATED

ooa_functions.depends:

ooa_functions:
\[echo\] Collecting available OOA parser functions…
\[exec\] ooa_functions.arc: 6: INFO: File ‘sql/ooa_functions.sql’ CREATED

content_assist.depends:

content_assist:
\[echo\] Adding content assist hooks…
\[exec\] content_assist.arc: 138: INFO: File ‘sql/content_assist.sql’ CREATED

grammar_enhancer.depends:

---

**Lee Riemenschneider** · September 28, 2019 at 3:00 am

I’m building on Ubuntu Linux, but I’m wondering if these lines in your output are a clue:
\[exec\] dyld: Library not loaded: /usr/local/opt/libffi/lib/libffi.6.dylib
\[exec\] Referenced from: /usr/local/Cellar/pypy/7.1.1_1/libexec/lib/libpypy-c.dylib
\[exec\] Reason: image not found

Maybe pypy isn’t installed properly?

---

**Lee Riemenschneider** · September 28, 2019 at 3:05 am

Searching on “dyld: Library not loaded: /usr/local/opt/libffi/lib/libffi.6.dylib” uncovered many discussions like [this one](https://github.com/platformio/platform-lattice_ice40/issues/7) for Mac installs.

---

**Sean Kavanagh** · September 30, 2019 at 7:47 am

Thanks Lee. I will investigate this library and if i can resolve, will rerun.

---

**Sean Kavanagh** · October 1, 2019 at 1:36 pm

Success!

I performed the following:

\$ brew install libffi
\$ brew reinstall pypy

\$ cd ~/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/
\$ git clean -fdx -e build_configuration.sh
\$ cd ~/Workspaces/HackDayProjects/BridgePoint/git/bptest/
\$ git clean -fdx

\$ ~/Workspaces/HackDayProjects/BridgePoint/git/bridgepoint/utilities/build/build_and_test_bp.sh

And after 48 mins, the build completed! :D

Many thanks, Sean.

---

**John Wolfe** · April 28, 2023 at 5:21 pm

I saw the same failure on Ubuntu 20. Updating pyenv (\$ pyenv update) solved the problem. Details follow.
During the 7.4 release, a .python-version file specifying pypy3 was added to the bridgepoint repository. I was building master, which contained this file, and the version of pyenv installed on my machine predated the version that supports fuzzy matching of python versions, so even though pypy3.9-7.3.9 was installed on my machine, pyenv would report that pypy3 was not installed.
Pyenv 2.3.6 includes the ability for pyenv to recognize that a requirement for pypy3 can be satisfied by any pypy3.\* version. I was running pyenv 2.3.0, which does not have this feature. Updating pyenv solved the problem.
