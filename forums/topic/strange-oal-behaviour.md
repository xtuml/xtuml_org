---
redirect_from:
  - "/community/topic/strange-oal-behaviour/"

layout: "topic"
title: "Strange OAL behaviour"
date: "2019-09-19"
permalink: "/forums/topic/strange-oal-behaviour/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Clive** · September 19, 2019 at 9:29 am

The following class function works (as expected according to OAL web manual). This function creates an instance.
——————————————————–
// Create a new staff member.
// First check that Staff Member does not already exist.

select any StaffMem from instances of SM where selected.First_Name == param.First_Name AND selected.Last_Name == param.Last_Name AND selected.Birth_Date == param.DoB;

if empty StaffMem //If the Staff Mmember doesn’t already exist then create a new instance and send success message.
create object instance new_SM of SM;
assign new_SM.First_Name = param.First_Name;
assign new_SM.Middle_Name = param.Middle_Name;
assign new_SM.Last_Name = param.Last_Name;
assign new_SM.Birth_Date = param.DoB;
assign new_SM.Honorific = param.Title;
assign new_SM.Mobile_Phone = param.Mobile_Number;
return “New Staff Member has been Added Successfully!”;
else //If the Staff Member does already exist then send message to indicate that fact.
return “Staff Member Already Exists”;
end if;
———————————————————————-

The following, similar OAL structure of a class function that deletes an instance shows errors. Interestingly, the error indicates that a ‘return’ statement is NOT necessary in a CLASS function. Unless I haven’t cleaned my specs properly, the OAL web manual indicates that I can only use the ‘return’ statement in a CLASS function. So why does the former (creation) function show no errors (and work as required) but the (deletion) function below show errors and won’t work unless I remove the ‘return’ statements.
—————————————————————————

// Remove a staff member.

// First choose the staff member to remove

select any existing_SM from instances of SM where selected.First_Name == param.First_Name AND selected.Middle_Name == param.Middle_Name AND selected.Last_Name == param.Last_Name AND selected.Birth_Date == param.DoB;

if not empty existing_SM //If the specific staff member exists then remove him/her.
delete object instance existing_SM;
message = “Staff member has been removed”;
//return “Staff member has been removed”;
else
message = “This particular staff member does not exist! Please check that you have entered the correct details.”;
//return message;
end if;

return message;

———————————————————-
The lines in the latter function showing ‘//return’ indicate other attempts to get the function to parse. This particular version faults on the last line with the comment I mentioned above of the ‘return’ statement not being necessary.

---

**Clive** · September 19, 2019 at 11:46 am

What a dill! I thought my return type for the function was correct (i.e. – string) but on further examination it was actually set to ‘void’. Silly, not to have checked all angles before reporting on this one. However, from another viewpoint it’s an opportunity to re-iterate the message of ‘strong typing’ in languages.

Although, I really should have picked this one up earlier, I have to say that the message associated with the error was somewhat misleading in suggesting that a return statement is not necessary in a class-based function.

The discussions had at xtUML Days 2019 surrounding MASL and strongly typed languages should be followed up closely – especially as there’s significantly greater opportunity to identify and label errors more meaningfully.

On this occasion it was/is the ‘typing’ that was picked up, but reported obscurely.
