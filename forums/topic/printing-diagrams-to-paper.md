---
redirect_from:
  - "/community/topic/printing-diagrams-to-paper/"

layout: "topic"
title: "Printing diagrams to paper"
date: "2017-11-01"
permalink: "/forums/topic/printing-diagrams-to-paper/"
forum: "Miscellaneous"
forum_slug: "miscellaneous"
forum_url: "/forums/miscellaneous/"
---

**xthunderheartx** · November 1, 2017 at 3:42 pm

Is there a simple way to tell eclipse to print all the diagrams in a project? Or maybe export them to PDF?

-Thx

P.S.: Bridgepoint and Shlaer-Mellor have \*really\* come a long way since the mid ’90s. All I can say is … thank you.

---

**Bob Mulvey** · November 1, 2017 at 4:03 pm

Hi!

There is no mechanism in place to print all diagrams.

Honestly, I think, if there was, it may not be very useful because of the variability of the diagram content and size. I can tell you what I do when I want a hard-copy for reference is I capture sections of the diagram as-needed based on what I am doing so that reasonable content is present. I then print these “logical pieces” to pdf naming them \_1, …\_2, etc. I can them lay-out the pieces of paper in front of me as needed. There are some diagrams that I refer to that tend to be fairly static. For these I keep the pdfs in folders so I can get them again as time passes.

I will also note that in many cases when I am thinking about wanting hard-copy to work from I may consider using the Eclipse “New Window” feature to allow me to show the diagram in question on a separate monitor while I work on the task at hand. This is actually my preferred approach, but I understand that indeed it is nice to have “hard copy” sometimes too.

That is what I tend to do when I want a hard-copy for reference while working.

---

**xthunderheartx** · November 1, 2017 at 4:17 pm

I need the images for an onsite project review with customers. Bunch of Army Guys. Their eyes will glaze over of course, but I gotta have something for the PowerPoint. Foils Dood! We need Foils!?? It ain’t a presentation without Foils …

---

**Lee Riemenschneider** · November 1, 2017 at 4:54 pm

You can use \[project\]-\>RMB-\>BridgePoint Utilities-\>Create Documentation in the xtUML Modeling view to get an html file generated. The html isn’t too pretty, but a doc/images directory gets generated in your project workspace. This directory has images you can use to place in your presentation, and they are named like: \[project\]-\[package\]-\[component\]-\[package\]-\[class\]-Instance State Machine.png.

- This reply was modified 8 years, 3 months ago by [![](https://secure.gravatar.com/avatar/2beeed50ad01495a2bb8456ccfd23100a3ae303e29fc1a90ee450c7cf5e79641?s=14&amp;d=mm&amp;r=g)Lee Riemenschneider]({{ '/user/lwriemen/' | relative_url }}).

---

**Bob Mulvey** · November 1, 2017 at 6:01 pm

Oh yeah, Document Generation (DocGen)! I forgot about DocGen :). Document Generation is perfect for this. Thanks Lee!

- This reply was modified 8 years, 3 months ago by [![](https://secure.gravatar.com/avatar/ea6d2e68d9e24480faf46673da88124c2c221ff2d8107d66a7a34d3548928a08?s=14&amp;d=mm&amp;r=g)Bob Mulvey]({{ '/user/rmulvey/' | relative_url }}).
- This reply was modified 8 years, 3 months ago by [![](https://secure.gravatar.com/avatar/ea6d2e68d9e24480faf46673da88124c2c221ff2d8107d66a7a34d3548928a08?s=14&amp;d=mm&amp;r=g)Bob Mulvey]({{ '/user/rmulvey/' | relative_url }}).

---

**xthunderheartx** · November 16, 2017 at 1:56 pm

Yeah I did a Doc Gen on the MO project. I wasn’t really that disappointed in it honestly. Plan to use the feature on my current project. Thanx for the help. Wonder why I didn’t get a notification when this thread updated …
