---
redirect_from:
  - "/community/topic/japanese-characters-is-garbled-on-windows/"

layout: "topic"
title: "Japanese characters is garbled on Windows."
date: "2022-06-02"
permalink: "/forums/topic/japanese-characters-is-garbled-on-windows/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**kae-made** · June 2, 2022 at 10:01 pm

Hi BridgePoint developers,
Please let me know how to resolve UNICODE character garbling problem.
I use BridgePoint on Windows 11. I can write Japanese sentence in text editor but the sentence at the moment of saving becomes garbled.
The xtuml file seems to be saved as not UTF8 but ANSI.
I also tried BridgePoint run on WSL2 but I was unable to input or copy & paste Japanse characters.

---

**cort** · June 3, 2022 at 10:55 am

Navigate to Eclipse-\>Preferences-\>Workspace

You will see a place to set the default encoding. Set it to UTF-8.

---

**Shin Kuboaki** · June 3, 2022 at 2:07 pm

I set the following on BridgePoint for Windows:

Eclipse-\> Preferences-\> Workspace
Then default encoding. Set it to UTF-8.

With this setting, I entered the class description using Japanese. When saved, the encoding of the’.xtuml’ file is MS932 (default encoding of Japanese Windows).
From this, it looks like BridgePoint or Eclipse is not saving in UTF-8 when saving to a file. (Or when reading?)

Next, I tried using Japanese for the class name.
In this case, a folder with the Japanese class name was created in the folder of the class diagram package.
After restarting BridgePoint with this setting, it appears as a blank class in the class diagram and Model Explore no longer shows this class in that package.

---

**Shin Kuboaki** · June 6, 2022 at 12:01 pm

Ohta-san edited the source code of BridgePoint and built it to solve this issue, but it seems that the following error has occurred.

> Hi, I’m trying to build BridgePoint.
> I tried Debian 11.3, Ubuntu 20.04.4 LTS, and Ubuntu 18.04.6 LTS, but a build error happened at org.xtuml.bp.als.
> I also tried Ubuntu 20.04 environment in a Docker container and I confirmed that the same build error happens.
>
> \[ERROR\] Failed to execute goal org.apache.maven.plugins:maven-antrun-plugin:1.8:run (generate-ant) on project org.xtuml.bp.als: An Ant BuildException has occured: The following error occurred while executing this line:
> \[ERROR\] /root/git/bridgepoint/src/org.xtuml.bp.als/generate.xml:202: Warning: Could not find file /root/git/bridgepoint/src/org.xtuml.bp.als/gen/code_generation/ooaofooa.sql to copy.
> \[ERROR\] around Ant part …\<ant antfile=”/root/git/bridgepoint/src/org.xtuml.bp.als/generate.xml” target=”nb_all”/\>… @ 12:91 in /root/git/bridgepoint/src/org.xtuml.bp.als/target/antrun/build-main.xml
>
> I share my docker image as kaemade/bp-build-ubuntu:1.0.0 .
> Please try to solve the error by running it.
>
> \$ sudo docker run –name test -it kaemade/bp-build-ubuntu:1.0.0
> \# ~/git/bridgepoint/utilities/build/build_and_test_bpsh
>
> I also share my Dockerfile at [https://github.com/kae-made/bridgepoint/blob/master/utilities/docker-for-build/Dockerfile](https://github.com/kae-made/bridgepoint/blob/master/utilities/docker-for-build/Dockerfile)
> You can create Docker image by yourself.
>
> \$ sudo docker build -t bp-build-ubuntu -f Dockerfile .
>
> If there are some mistakes in the build environment setup, please let me know.

---

**kae-made** · June 6, 2022 at 7:18 pm

Hi, kae-made is Hiroshi Ota’s account.
My all build activities are done on Windows for Linux and Windows docker envrironment.
I suspect that there are some version inconsistency associated with updating the library using.
I don’t have Mac PC so I have no way to check if it works properly on Mac. Please try to build on latest Mac environment.

---

**Shin Kuboaki** · June 7, 2022 at 12:26 am

Trying to build on Intel Mac, I got the following error message:

> Failed to execute goal org.apache.maven.plugins:maven-antrun-plugin:1.8:run (generate-ant) on project org.xtuml.bp.als: An Ant BuildException has occured: The following error occurred while executing this line:
> \[ERROR\] /Users/kuboaki/git/bridgepoint/src/org.xtuml.bp.als/generate.xml:256: Unable to determine generated class
> \[ERROR\] around Ant part …\<ant antfile=”/Users/kuboaki/git/bridgepoint/src/org.xtuml.bp.als/generate.xml” target=”nb_all”/\>… @ 12:100 in /Users/kuboaki/git/bridgepoint/src/org.xtuml.bp.als/target/antrun/build-main.xml

---

**kae-made** · July 11, 2022 at 10:11 pm

Hi, I resolved this problem.
By the following setting for environment variables in control pannel, Japanese characters can be saved.
JAVA_TOOL_OPTIONS
-Dfile.encoding=”UTF-8″

Even if I don’t set this Japanese characters can be used for names of class, attribute, operation or phrase of relationship. Only the description text editor has this problem.
It seems that both saving are done by bridgepoint/src/org.xtuml.canvas.language.parent/org.xtuml.canvas.language.ui/src/org/xtuml/canvas/language/io/CanvasWriter.ja
I don’t know why only previous items work correctly.

---

**cort** · July 12, 2022 at 8:06 am

This is good news! Thank you, kae-made.
