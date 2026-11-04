---
redirect_from:
  - "/community/topic/eclipse-mars-tips/"

layout: "topic"
title: "Eclipse Mars Tips"
date: "2015-12-09"
permalink: "/forums/topic/eclipse-mars-tips/"
forum: "Miscellaneous"
forum_slug: "miscellaneous"
forum_url: "/forums/miscellaneous/"
---

**Lee Riemenschneider** · December 9, 2015 at 12:29 pm

I thought I’d start this topic, because I had some trouble with the Oomph Preference Recorder, that has been popping up every time you change a preference in eclipse.

The Preference Recorder will apply the preference change to all usage (all present and new workspaces) of eclipse if you click OK. Not only that, but it will not pop-up for that preference again. (OK is now the default and all future changes to the preference get propagated everywhere.)

If you click Cancel, the preference will only be applied to your current workspace.

If you click OK and later want to undo this change, you have to do the following from the toolbar: Navigate \> Open Setup \> Open User \> User Preferences \> UserPreferences, then find the key for the preference and delete it. There is also another key under the plugin folder at the same level as the UserPreferences drop down list. You can delete this one too.

The UserPreferences key is the recorder selection key. Clearing the value, “record”, will also stop the recorder. The other key is the value key. If the recorder key is deleted or cleared, the value key no longer gets updated.

You can also turn off the recorder in the pop-up dialog (so you don’t see the pop-ups any more) or in Window \> Preference \> Oomph \> Preference Recorder.
