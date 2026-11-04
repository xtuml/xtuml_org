---
redirect_from:
  - "/community/topic/import-export-project/"

layout: "topic"
title: "Import / Export project"
date: "2023-09-23"
permalink: "/forums/topic/import-export-project/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Schmill** · September 23, 2023 at 10:35 pm

Hi there,
1) I’m trying to copy the models directory and the .project from directory A to new directory B.
2) in the new workspace I open the project in directory B using the ‘Open Projects from file system’
3) Only parts of the model elements are imported. many classes are missing.
4) I clicked all the BP tools referential integrity and it added some but still many are missing.

Alternatively I tried use the export wizard, but then import wizard won’t provide any option to complete the import when I reference the exported file (the list is blank).

Thank you.

---

**John Wolfe** · September 23, 2023 at 11:35 pm

From within BridgePoint, use File \> Export \> General \> Archive File.
Then select the projects you want to export, and select the .project file.
After successfully exporting to an archive file (zip or tar), you can then import one or more projects from that file into another (perhaps newly created) workspace using File \> Import \> General \> Existing Projects into Workspace.
Select “Select archive file” and navigate to the archive you exported earlier.
Select the projects you want to import, and hit “Finish”. The selected projects will be imported into the workspace.

---

**Schmill** · September 24, 2023 at 7:55 am

Perfect,
Thank you
