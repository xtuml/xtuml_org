---
redirect_from:
  - "/community/topic/adding-members-to-mc-c-generated-structures/"

layout: "topic"
title: "Adding members to MC C generated structures."
date: "2023-11-13"
permalink: "/forums/topic/adding-members-to-mc-c-generated-structures/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Schmill** · November 13, 2023 at 9:49 am

Hello,
From MC perspective, is it safe and legitimate to add members to the generated structures of Classes?

In this example I add att3 to the generated struct:

`struct SomeDomain_RD`
`{`
`Escher_StateNumber_t current_state;`
`Escher_UniqueID_t ThingID;`
`i_t att1;`
`c_t att2[ESCHER_SYS_MAX_STRING_LEN];`
`struct some_type* att3; /* - can this be added to the gen? */`
`};`

Thank you.

---

**cort** · November 13, 2023 at 10:59 am

You simply add more attributes to the class in the data model.

Or are you wanting to modify the generated code?

---

**Schmill** · November 13, 2023 at 11:02 am

Correct, I would like to add pointers to structs that are not known to the data model. by modifying the generated code.

- This reply was modified 2 years, 3 months ago by [![](https://secure.gravatar.com/avatar/3040dde2b0b01d2ea433fda15866ec95296afd183c3e8807c9693f8e2edd2eab?s=14&amp;d=mm&amp;r=g)Schmill]({{ '/user/schmill/' | relative_url }}).

---

**cort** · November 13, 2023 at 11:06 am

There is documentation in the MC-3020 User Guide for doing this. But the summary is:

1\. Copy generated code from the /src folder to the /gen folder.
2. Edit the code in the /gen folder.
3. Now, each time you generate code, the edited file will get copied \_over\_ the generated file in the src folder.

If you modify the model behind the generated code, you may want to re-generate and re-edit.

---

**Schmill** · November 13, 2023 at 11:11 am

Very well, I have the documentation. just wanted to make sure I don’t do anything that is criminal to the Class structures ;)

---

**cort** · November 13, 2023 at 11:22 am

This is the start. Pretty soon you will be asking how to change the model compiler itself to add the various patterns you are applying to the classes. :)

---

**Schmill** · November 13, 2023 at 11:26 am

I’m still dealing with the very basics, but thank you so much)
