---
redirect_from:
  - "/community/topic/bridgepoint-project-configuration-managment/"

layout: "topic"
title: "BridgePoint project configuration managment"
date: "2016-06-02"
permalink: "/forums/topic/bridgepoint-project-configuration-managment/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**keithbrown** · June 2, 2016 at 2:13 am

A new BridgePoint user raised the following questions:

> A question on config control… if we use git to hold the xtuml source for our MASL domains and MASL projects, are there any restrictions on how we split/combine them between repositories? I.e. Could we have each MASL domain and MASL project in a separate repository? Can we combine related MASL domains and MASL projects into a single repository? If a MASL domain is common to a number of projects in different repositories, how is that handled?

Each user will have their own eclipse workspace(s) on their local machine. On disk, a workspace is simply a directory that also contains some eclipse configuration data. Inside the eclipse/BridgePoint UI, a workspace is container of one-to-many eclipse projects. Note the terminology overlap here. An eclipse project is not equal to a MASL project.

Eclipse projects may live on disk either inside the workspace directory, or they may live outside the workspace directory and be imported into the workspace. Inside the UI there is no visible difference to the user where the eclipse projects live on disk.

Inside the eclipse UI, the user can create connections to one or more repositories. These repository connections are saved in the workspace configuration data.

The practical upshot of this is that a user may import eclipse projects into their workspace from many different repositories. They can mix and match eclipse projects in their workspace identically or completely differently from other users. Once the eclipse project is imported into the workspace and has BridgePoint inter-project references turned on it can see all the other projects in the workspace.

The modeler must be careful when creating inter-project references so that other modelers know those dependencies exist. For example, if you have an eclipse xtUML project that contains a shared datatype package in repository A, and another eclipse xtUML project that contains a MASL domain in repository B that has a class attribute that references a type from the shared type package, then every user who imports the domain-containing project into their workspace will also need to import the shared type package-containing project. The eclipse workspace/project mechanism does provide the ability for Users Jack and Jill to each have their own MASL project (which will be inside an eclipse xtUML project) stored in different repositories that both reuse the domain and types.

If you want to look for more information the vast majority of what I’ve described is core eclipse functionality and not BridgePoint specific, so there is lots of information about this in books and on-line (including the xtUML Modeling on-line video course on xtuml-org.hustlefish-sites.com).

A final note: when cloning a git repository to your local machine, **NEVER** clone it to a directory under an eclipse workspace. Git repos should be cloned to their own working areas, inside eclipse you add a link to the local repository and import the projects into the workspace.

Cheers,
Keith
