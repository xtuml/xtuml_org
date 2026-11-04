---
redirect_from:
  - "/community/topic/automatic-merging-of-xtuml-data-on-the-command-line-with-git/"

layout: "topic"
title: "Automatic merging of xtUML data on the command line with Git"
date: "2013-11-07"
permalink: "/forums/topic/automatic-merging-of-xtuml-data-on-the-command-line-with-git/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Travis London** · November 7, 2013 at 8:16 pm

The following instructions will allow one to configure automated merging on the command line using Git. The command line merge will automatically merge anything that does not have conflicts on a semantic level. Anytime a file and its modified versions are considered to be conflicting the merge will be aborted and the file will be left untouched.

The first part of work is to configure Git to use a custom merge driver. This is done in two parts.

1\. Modify the config file under the Git repository .git folder to have the following entry:

\[merge “xtUML”\]
name = xtUML Merger
driver = /eclipse/CLI.sh Merge -leftFile %A -rightFile %B -ancestorFile %O -outputFile %A

2\. Add this file under the .git folder, info/attributes, and include the following line:

\*.xtuml merge=xtUML

The second part of work is to assure you have a CLI.sh script (if in windows, it will exist in linux), and modify it to point at the proper workspace. Note that the workspace is only important if you want integrity reports after the merge. Here is example content for CLI.sh. If you are on windows just create a file with this contents at the expected location.

\#!/bin/bash
\# For windows use the following
\# BPHOMEDIR=”/c/xtUML/xtUMLEditor”
BPHOMEDIR=”\$HOME/xtUML/xtUMLEditor”
BP_VERSION=”4.1.0″
\# For windows use the following
\# WORKSPACE=”/c/path_to_workspace”
WORKSPACE=”\$HOME/workspace”

function die() {
echo -e \$@
exit 1
}

function displayHelp() {
echo -e “”
echo -e “Usage: ./CLI.sh ”
echo -e “”
echo -e “Example:”
echo -e ” ./CLI.sh Build -project MicrowaveOven -buildConfig Debug -cleanCLI”
echo -e “”
echo -e “To list complete usage information for a command:”
echo -e ” ./CLI.sh Build -help”
echo -e ” ./CLI.sh Import -help”
echo -e ” ./CLI.sh Execute -help”
echo -e ” ./CLI.sh Merge -help”
echo -e “”
echo -e “Note that you must edit the WORKSPACE variable inside this CLI.sh”
echo -e “to point at the appropriate workspace.”
echo -e “”
echo -e “For additional information, see the Command Line Interface ”
echo -e “documentation inside the Help system.”
echo -e “”
exit 2
}

\# Check that a valid argument is specified
if \[ “\$1” != “Build” \]; then
if \[ “\$1” != “Execute” \]; then
if \[ “\$1” != “Import” \]; then
if \[ “\$1” != “Merge” \]; then
displayHelp
fi
fi
fi
fi

if \[ “\${MGLS_LICENSE_FILE}” == “” \]; then
if \[ “\${LM_LICENSE_FILE}” == “” \]; then
\#
\# Since the license path is not already set, use the standard location. Users may
\# choose to set the value in the environment, or modify the following line to point to the correct
\# location (either local or remote).
\#
\# example configuration for a remote license server
\# export MGLS_LICENSE_FILE=1717@svr-taz-eng-05
\#
MGLS_LICENSE_FILE=”\$BPHOMEDIR/license/license.dat”
else
MGLS_LICENSE_FILE=\$LM_LICENSE_FILE
fi
fi
export MGLS_LICENSE_FILE

\[ \$MGLS_LICENSE_FILE \] \|\| die “No license is setup (missing \\LM_LICENSE_FILE)”

\#
\# DO NOT MODIFY ANY OF THE FOLLOWING LINES.
\#
export ORIGINAL_PATH=\$PATH
export PATH=\$PATH:\$BPHOMEDIR/tools/docgen/docbook
export MGC_EMBEDDED_HOME=\$BPHOMEDIR
export MGLS_DLL=
\#export MGLS_PKGINFO_FILE=
export MGC_HOME=
export MGLS_HOME=\$BPHOMEDIR/eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.core.linux.x86\_\$BP_VERSION/os/linux/x86
LAUNCHER=”\$BPHOMEDIR/eclipse/plugins/org.eclipse.equinox.launcher_1.2.0.v20110502.jar”
APPLICATION=”com.mentor.nucleus.bp.cli.\$1″

\$BPHOMEDIR/jre/bin/java -d32 -Xms256m -Xmx1g -XX:MaxPermSize=256m -jar \$LAUNCHER -clean -noSplash -product com.mentor.nucleus.bp.pkg.BridgePoint -data \$WORKSPACE -application \$APPLICATION \$2 “\$3” \$4 “\$5” \$6 “\$7” \$8 “\$9”

\# Restore the path
export PATH=\$ORIGINAL_PATH

exit 0

---

**Bob Mulvey** · November 8, 2013 at 5:55 pm

Be careful about trying to copy and paste the above test into CLI.sh. The double-qoutes are not being copied across correctly! They are not copied/pasted as simple ascii double quotes. It is safest to use the CLI.sh distributed with the linux version of the product and just add-in the settings for BPHOMEDIR, WORKSPACE, and MGLS_LICENSE_FILE at the top of the file.

---

**Bob Mulvey** · November 8, 2013 at 5:58 pm

Another thing to be careful of is use of Git Shell versus git in the cygwin shell (or linux). The path used in the example above comes from a Git Shell example. For cygwin this would likely need to be /cygdrive//, and of course in linux it would be something different depending on your installation.

---

**Bob Mulvey** · November 8, 2013 at 6:07 pm

In \#1 above, under “driver” in the “config” file, it reads:
driver = /eclipse/CLI.sh Merge -leftFile %A -rightFile %B -ancestorFile %O -outputFile %A

Note that you must put the path to you CLI.sh here. I suggest you simply put this next to the CLI.bat and Launch.bat files in your installation. If you do this, and you used the default installation path, and you are using Git Shell, then that setting will be:
/c/MentorGraphics/BridgePoint/eclipse/CLI.sh Merge -leftFile %A -rightFile %B -ancestorFile %O -outputFile %A
