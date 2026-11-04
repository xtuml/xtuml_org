---
redirect_from:
  - "/community/topic/routing-graphic-information-of-association-are-lost-by-importing-project/"

layout: "topic"
title: "Routing graphic information of association are lost by importing project"
date: "2024-10-10"
permalink: "/forums/topic/routing-graphic-information-of-association-are-lost-by-importing-project/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**kae-made** · October 10, 2024 at 12:29 am

When I import a project, the graphic information for the lines in the relationship in the class diagram is missing.
I tried the following three import methods, but all of them didn’t work,
1. Copy the project folder to another location and import the folder
2. Create ZIP file of the project folder and import the archived file
3. Pull the project folder and contents from github repository and import that.

I’ve published a project on github that causes the problem so I want you to give it a try.
[https://github.com/kae-made/HealthcareCasestudy](https://github.com/kae-made/HealthcareCasestudy)

---

**cort** · October 10, 2024 at 9:21 am

Hello Kae-Made,

I looked at the model in the repository. It seems to be a “single-file” model (from a previous export).

To import this model try the following steps:
1) Create a new xtUML Project
2) Select the new project, right click and ‘Import’
3) Select xtuml -\> xtUML Model

Tell me if it works.

Cort
