---
redirect_from:
  - "/community/topic/select-all-bodies-within-component/"

layout: "topic"
title: "Select all bodies within component"
date: "2015-10-18"
permalink: "/forums/topic/select-all-bodies-within-component/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**nukic** · October 18, 2015 at 2:55 pm

Hi guys
I want to select all the bodies within a component.
I found associative relation R694 from C_C to ACT_ACT via ACT_BIC (Body in Component) but selection seems to be empty each time. Any ideas why? I searched sql file from gen/code_generation folder, no inserts in ACT_BIC was found. I will temporarily use workaround and select each of the body types separately, but this shortcut would be nice to have. Can you help?
I am using BP 4.2.

Thanks!
/Neno

---

**Bob Mulvey** · October 19, 2015 at 2:39 pm

Hi Neno,

Good to hear from you, I hope you are doing well!
The reason that is empty is that it is ALMOST obsolete and can be removed from the meta-model. I actually dealt with this recently in the specialized package removal work that is in progress ([https://support.onefact.net/redmine/issues/7769](https://support.onefact.net/redmine/issues/7769)). With the introduction of generic packages this shortcut is replaced by R640. That relationship is only used by verifier and only for a single command (sender) (see Functions::OAL Validation Utility Functions::sender_validate). I believe it could actually be removed even for that case, and thus completely remove R694 from the meta-model, but I choose to leave it for now simply because keeping it for this single case is a bit safer then removing it at this time. I would prefer the task to remove it be done as a stand-alone project where the testing can be properly focused to assure it is done right and removal has not unexpected side effects.

The removal work for 7769 is done, but testing is not. The fork/branch is [https://github.com/rmulvey/bridgepoint/tree/7769_remove_sp](https://github.com/rmulvey/bridgepoint/tree/7769_remove_sp)
If you are able and interested in helping push this forward by helping with testing, let me know and I will get you started.

Kind Regards,

/Bob

---

**nukic** · October 19, 2015 at 2:50 pm

Hi Bob,

Thanks for the answer, I should have seen R640 relation, its right next to R694 :)

Regards,
Neno

---

**Martin** · October 23, 2015 at 5:16 am

Hi,

Keep in mind that also Body In Element is marked as a non persistence class. From an exported/pre_builder build sql file you will have no instance of Body In Element. In our model compilers we have always performed a first pass translation that for example creates the Body In Component / Body In Element instances. The associations makes it easier to perform other kind of navigations, without checking the Body “type” all the time.
It might be a good idea to remove the non persistence while the number of users increases.

/Martin

---

**nukic** · October 23, 2015 at 10:13 am

Hi Martin

If I understood you correctly, that explains why there are no inserts for “Body in Element” class in sql file, right?
But I should still be able to find bodies if I use relation R640?

I am asking because, I tried it briefly and it did not work from first try and since I had working workaround, I gave up.
So I am wondering, did I do something wrong or I was not supposed to not find those bodies anyway?

Thanks,
/Neno

---

**Martin** · November 15, 2015 at 9:17 am

You will not fond Body In Element in the sql. IF you run in eclipse-java you will have instances.
