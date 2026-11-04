---
redirect_from:
  - "/community/topic/right-click-menus-decreasing-number-of-clicks/"

layout: "topic"
title: "Right Click Menus, Decreasing Number of Clicks"
date: "2016-02-01"
permalink: "/forums/topic/right-click-menus-decreasing-number-of-clicks/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**poj** · February 1, 2016 at 9:26 pm

In the current tool design, some things are most easily done from a context menu choice that starts a wizard with a single page containing just a single drop-down list of choices. The number of possible choices is quite limited, and are more reasonable choice would actually be just a sub-menu (no wizard) where you can choose directly. For a sub-menu to be useable, the number of choices must be limited, and there should be no need for the user to filter the results. The dialog used to select a new datatype is an excellent choice where a sub-menu solution would be bad for the user experience.

The two main cases I’ve found where a sub-menu implementation would result in significantly fewer clicks is the handling of attributes in identifiers, and the assigning of events to transitions in state machines.

The identifier case is most likely simpler to implement, since the number of possible choices is currently static, and the same for all attributes. The current implementation uses a separate wizard for “Add to Identifier” and “Remove from Identifier”, but in a sub-menu solution a single sub-menu “Part of Identifier” with three choices “\*1” “\*2” and “\*3”, preceded with a check mark if the attribute is part of the identifier is another possible solution.

The assignment of states to transitions is a bit more complex, since the choices available is dynamic, and must be populated on the fly. Here it looks like Eclipse Mars might actually have some issues with dynamically populated sub-menus.

So what is the opinion on changing the editor UI in these areas?
