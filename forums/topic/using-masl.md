---
redirect_from:
  - "/community/topic/using-masl/"

layout: "topic"
title: "Using MASL"
date: "2019-07-25"
permalink: "/forums/topic/using-masl/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Clive** · July 25, 2019 at 3:22 am

I’ve been trying to use MASL as the default action language in BridgePoint. And I’m getting very frustrated because I don’t seem to be able to create a new instance of anything – basic interactive message is that the particular class/object I’m trying to create an instance of is ‘unresolved’. This seems very odd because the name given to the service is ‘quite’ resolved. Declarations of other basic types seems OK, but then when I activate the verifier and run the function containing the action I’m informed that there’s ‘no statements to execute’.
I’ve checked that the default language is MASL in the BP preferences – which strangely doesn’t seem to gravitate to the information in the properties of the function (where OAL is the default). I make sure that I am opening the function file with the MASL editor, too!
I’ve read a lot of the manual, and also watched several of the videos and everything there seems consistent.
So! What on earth have I missed? Can anyone provide a tip/clue?

---

**John Wolfe** · July 25, 2019 at 3:51 am

Clive, I think, though I have not verified, that MASL is not yet supported by Verifier or the C model compiler (MC-3020).

---

**Lee Riemenschneider** · July 25, 2019 at 11:23 am

Clive, I can’t verify what John said either, but one of the recent changes to BridgePoint requires you to explicitly set your model compiler. This affect projects made before this change, and unfortunately the upgrade of the projects isn’t automated. The fix however is easy:

For older projects:
1. Choose Project -\> Properties -\> Builders
2. Remove any “Missing builder … ” entries
3. Remove “Model Compiler” entry if present
4. Follow the newer project steps

For newer projects:
1. Choose BridgePoint Utilities from the Project context menu (right mouse button click on project)
2. Choose Set Model Compilers
3. In the pop-up window choose the model compiler you want. In your case this would be only MASL Exporter.
4. Select Finish (if you choose MC-3020, you’ll get a Next button to choose C, C++, or SystemC

For creating new projects:
1. New -\> xtUML Project
2. After entering the project name, make sure you choose Next
3. The model compiler pop-up window is presented.
4. If you click Finish instead of next, your project will have no model compiler set up, and you’ll have to do the “For newer projects step” to compile and build.

John might still be right with what he wrote. I don’t work with MASL much.

---

**Levi** · July 25, 2019 at 11:46 am

I can verify what John said — MASL is not supported in BridgePoint Verifier or MC-3020.

If you want to get started using MASL, I recommend checking out the GPS Watch (MASL) project from the Welcome page (Click Help \> Welcome). A couple things to note if you do decide to go that way:

– The MASL architecture is only supported on Linux. I have successfully gotten it running on Ubuntu 18.04, but I did have some dependency issues with the current version of the model compiler. I would recommend Ubuntu 16.04 LTS as the easiest to get going. I cannot speak for other Linux distros.
– You must build and install the MASL compiler from source before it can be used to build xtUML projects. The git repo is here: [https://github.com/xtuml/masl](https://github.com/xtuml/masl). There are instructions in the README to get started.

---

**Clive** · July 26, 2019 at 12:48 am

Levi, Lee, John,
Thank you very much for the information/clarification and potential solutions. I guess what I’ve experienced exposes an issue of the tool seeming to allow functionality that is not apparently fully supported. From my position of getting very excited about the possibility of using MASL in my model (because I could select that option) there was nothing in the tool interface that suggested that I shouldn’t really choose the option without doing some more analysis/reading, or (if you like) ring alarm bells suggesting that what I was attempting required a particular consideration. Of course, my lack of deep analysis didn’t help the situation.
Nonetheless, the full inclusion of MASL for general modelling seems to be a very reasonable goal. On the other hand whilst ‘behaviour’ has to be defined and adequately specified for model execution, the language should not be so ‘powerful’ as to reduce the effort required to specify the data and state models (and their connection).
Because of my current pressing requirements to create a somewhat intricate model, I will put MASL aside for the moment and go back to good old OAL (in its

> latest

form).
