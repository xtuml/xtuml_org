---
redirect_from:
  - "/community/topic/how-to-get-model-data-from-and-xtuml-model/"

layout: "topic"
title: "How to get model data from and xtuml model?"
date: "2014-03-12"
permalink: "/forums/topic/how-to-get-model-data-from-and-xtuml-model/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Dan George** · March 12, 2014 at 7:25 pm

I already asked this quesiton but perhaps with too much distracting text. I can see that as I build a model, ~/workspace/Gps Watch/models/Gps Watch/…/\*.xtuml files change. Unfortunately, I’m unable to decypher the contents of those files. Any pointers for me?

Thanks,
Dan

---

**cort** · March 13, 2014 at 12:25 pm

The xtUML Editor stores model data in text files with file name/extension \*.xtuml.

The contents of the model are stored in multiple files divided by package. (This is done for scalability to make it easier for large teams to concurrently work on the same model and minimize conflicts.)

Inside the files you will see SQL INSERT statements. During load, the model data is inserted and related in-memory.

The schema for this in-memory “data base” (actually linked java classes in the plugins) is the xtUML meta-model (OOA of OOA in days of yore). The meta-model and schema are open source and published in various places. In the xtUML Editor you can find the meta-model as an example project. (Hmmm, the editor is delivered with a model of itself.)

Using Export from the project menu you can export the entire model to a single file.

A programmer can also access the model data through a java API (which is generated from the meta-model)

---

**Bob Mulvey** · March 13, 2014 at 12:40 pm

Hi Dan,

Actually, the \*.xtuml files do not change when a model is built. The \*.xtuml files hold the model data. The build process does not modify that model data. The build process in eclipse runs the build tool chain associated with the project. To see this tool chain you can right-right the project from Project Explorer and select Properties \> Builders. The 2 builders associated with xtUML are the first 2 in the list, “Model Compiler Pre-build”, and “Model Compiler”. Here is roughly what they do:
1) Model Compiler Pre-build
a) The model is parsed
b) During this step you may see files in the following folder get modified: /.externalToolBuilders. The reason for this is that this
pre-builder step is preparing for model translation. To this this is must set the home folder of the model. You will see this location in the
the ATTR_LOCATION attribute in the file /.externalToolBuilders/Model Compiler.launch
c) This step produces a file named /gen/code_generation/.sql. This “.sql” file is a single-file representation of your model (in this case GPS Watch), that includes the executable instance data created by the parser. If you are looking through the “.sql” file you can see this data in instances that start with this like insert into {“V\_\*” \| “ACT\_\*”}
2) Model Compiler
a) This step runs the model compiler to translate the model
b) The /gen/code_generation/.sql file created by the Mode Compiler Prebuilder is “pre-processesed” to prepare for the model compiler to run. This pre-processing is done by a perl script named xtumlmc_build. In fact, if you look at the first line of the console output in eclipse when you build, you will see the xtumlmc_build command-line. It looks something like this:
xtumlmc_build -home C:/git/repos/internal/src/com.mentor.nucleus.bp.mc.c.binary/ -l3b -e -d code_generation -O ../../src/
c) The xtumlmc_build command in the previous statement creates a copy of the file /gen/code_generation/.sql that has been pre-processed to be ready for model translation. This file is named: /gen/code_generation/\_system.sql
d) At this point xtumlmc_build starts the model translation by calling gen_erate.exe which loads the xtUML meta-model, loads the model to be translated, and then executes the model compiler archetypes that cause the translation.
e) The files created are placed under the /gen/code_generation folder
f) Once the Model Compiler has finished, the source files are copied into the /src folder so the remaining tools in the build chain can access them.

3\) The other builders in the tool chain run next to compiler the translated source files produced by the model compiler.

Of course that explanation does not really answer your question :). To decipher the contents of an xtUML file you must understand the xtUML Meta Model. What you see in each of the \*.xtuml files are instances of the classes defined in the xtUML meta-model. This meta-model is distributed as one of the sample projects. You can create this project and look at it in the same way you created GPS Watch. Help \> Welcome \> Documentation Project – xtUML MetaModel. Now let’s look at one of the elements in one of the GPS Watch \*.xtuml files. I will pick one at random:
1) Open GPS Watch/models/GPS Watch/Activities/Activities.xtuml
2) This is the first element in this “.xtuml” file:
INSERT INTO EP_PKG
VALUES (“c4db7d83-7a88-46de-81dd-7d9c8a3c56fa”,
“36a41cf7-d411-488d-99fc-74866d4fea39”,
“36a41cf7-d411-488d-99fc-74866d4fea39″,
‘Activities’,
”,
0);
3) Open the xtUML_MetaModel project provided in Help \> Welcome \> Documentation Project – xtUML MetaModel
4) Go to the xtUML Model perspective
5) In the Model Explorer view navigate to :
ooaofooa \> Element Packaging \> Package
6) Look at the properties view for this class named “Package”
7) Note that it’s key letters are EP_PKG! This is the instance from the GPS watch model. This happens to be a “Package”, and it’s name in the GPS Watch model is “Activities”.

You can find every instance in every “.xtuml” file in this way (they are all instances of meta-model classes). I hope gives you a start! Of course I simply randomly picked an element. To learn about the meta-model elements you can examine the provided model, and you can look in the documentation at the Metamodel Reference.

/Bob

---

**Dan George** · March 13, 2014 at 6:10 pm

The OOA of OOA model is awesome! It will take me quite some time just to get an handle on just any one domain. Lots to learn.

Great work, guys, and thank you for the pointers.

Dan

---

**cort** · March 13, 2014 at 7:43 pm

Start in the package called “Subsystem” at “Model Class (O_OBJ)” and work out from there.
