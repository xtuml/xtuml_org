---
redirect_from:
  - "/community/topic/model-snippet-of-the-day/"

layout: "topic"
title: "Model Snippet of the Day"
date: "2014-12-01"
permalink: "/forums/topic/model-snippet-of-the-day/"
forum: "Executable UML and xtUML Methodology"
forum_slug: "executable-uml-and-xtuml-methodology"
forum_url: "/forums/executable-uml-and-xtuml-methodology/"
---

**cort** · December 1, 2014 at 5:22 pm

[![]({{ '/assets/uploads/2014/12/BPcuff_paper.png' | relative_url }})]({{ '/assets/uploads/2014/12/BPcuff_paper.png' | relative_url }})

We teach Executable UML Modeling. We teach engineers and computer scientists, but we also teach managers, accountants, teachers and even nurses. In fact, it was a high school aged nurse-to-be that modeled the blood pressure cuff shown above on paper. The next day in class we entered the model into BridgePoint as shown below.

It is really fun to see someone grasp the concept of abstraction. Some people have knack for it and quickly learn to capture and communicate ideas with models. The nurse who built this model really disliked computer science and was mildly annoyed that she was so good at modeling!

Notice the “Class Blitz” list in upper left corner to assist in her brain-storming.

Look for another “model snippet of the day” like this in future posts.

\[originally posted at [http://onefact.net/blood-pressure-cuff/%5D](http://onefact.net/blood-pressure-cuff/%5D)
[![]({{ '/assets/uploads/2014/12/BPcuff_BP.png' | relative_url }})]({{ '/assets/uploads/2014/12/BPcuff_BP.png' | relative_url }})

- This topic was modified 11 years, 2 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).
- This topic was modified 11 years, 2 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).

---

**cort** · December 9, 2014 at 4:36 pm

[![]({{ '/assets/uploads/2014/12/brake_model.png' | relative_url }})]({{ '/assets/uploads/2014/12/brake_model.png' | relative_url }})
In today’s model snippet of the day I post a first draft class diagram of an electric parking brake. The classes are *rotor*, *caliper*, *gear box* and *motor*. Attributes are placed such that the *rotor* has a *diameter*. The *caliper* is in a *current_position*. The *gear box* must have gears that provide a *reduction*. The *motor* has a *power* rating and generates a quantity of *torque*.

Although not shown, the *motor* and *caliper* have lifecycles defined by state machines. You can tell this because of the state machine glyph on the classes. The associations labeled *R1*, *R2* and *R3* relate instances of the classes together.

When the brake *motor* is activated it drives the *gear box* providing mechanical advantage through its *reduction*. The *gear box* *closes* the *caliper* changing its *current_position*. The *caliper* *squeezes* the *rotor* providing frictional forces to prevent the *rotor* from turning, and thus keeping the car in its parking space. Note that we can read the associations in the opposite direction and state that the *rotor* *is squeezed by* the *caliper* which *is closed by* the *gear box* which *is driven by* the *motor*.
[![]({{ '/assets/uploads/2014/12/brake.jpg' | relative_url }})]({{ '/assets/uploads/2014/12/brake.jpg' | relative_url }})

- This reply was modified 11 years, 2 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).

---

**Dan George** · December 9, 2014 at 11:49 pm

Thanks, Cort. I hope we get to see the revised draft to get a sense of how models evolve incrementally.

Something I find challenging is coming up with asymmetric verb phrases. Lahman provides paid by/hires in contrast to employed by/employs. Another example can be taken from Balcer, Mellor, page 90. I think Lahman would have used one association with is rented by/lives in and then realized the need for a second association (for the reasons stated in the related text). Above, I wonder if

> drags surface of/wears down

,

> applies force to/is closed by

,

> drives/multiplies torque of

would be appropriate and useful. I tried to think of phrased more pertinent that mechanical connectivity. I don’t intend any criticism; just looking to expand on the simple example. Thoughts?

Thanks again, Dan

---

**Lee Riemenschneider** · December 10, 2014 at 3:13 am

I added a wrong comment on the One Fact blog, so if you go over there, ignore it. I plead temporary insanity. :-)

+Dan one thing you don’t need to do is model every thing that is occuring in the system, only the things you want to control. The caliper wearing down the rotor is irrelevant to control of the brakes.

If there was a way to dynamically check the thickness of the rotor, then a minimum thickness attribute would probably exist in the model (most likely in a specification class for the rotor rather than the Rotor class. A sensor would also have to be added. If this dynamic sensing isn’t in the system, then the minimum thickness would not be needed in the model, so it would better reside in a service manual.

I’m not sure all of your verb phrases were targeted at additional relationships. The “drives/multiplies torque of” might be considered a better verb phrase for R3, because it helps to illustrate the need for the reduction and torque attributes.

For R2, “closes” is more descriptive than “applies force to”, because “applies force to” doesn’t give a reason. As an additional relationship, it would be redundant.

---

**Dan George** · December 10, 2014 at 6:18 pm

Thanks, Lee. Ya, I was making things up with my examples trying to think of reverse roles. The R3 asymmetric phrases was the only one that didn’t feel forced.

I’m a little bugged about including both phrases when they are symmetric. On the plus side, you don’t have to wonder if the omitted one was an oversight or intentionally implied symmetric. On the down side, it clutters the model and violates, ironically, one fact, one place.

Another thing that I run into is not knowing how to say what’s in or out of scope for the model. IOW, just by looking at a model, how can I tell some aspect has been overlooked or if it is intentionally left out? My guess is that the domain diagram and descriptions resolve this issue.

Thanks again, Cort, for providing an example for us to discuss and learn from. I suspect that there are more would-be-xtUML users that struggle to learn because of isolation and lack of mentors.

---

**cort** · December 11, 2014 at 1:36 pm

Good thoughts on symmetric versus asymmetric verb phrases. You can get yourself into trouble getting too creative trying to come up with the “other direction verb phrase”. In this particular model, I think it may be cleaner to leave some of the verb phrases off. Choose the direction of traversal and provide that verb phrase only.

My favorite example of multiple verb phrases deals with the relationship(s) between “car” and “person”. A rel-phrase combination “owns”/”transports” is just such a problem. I own the car in my garage, but my rental transports me. So, there would be 2 separate associations to link 2 separate instances of “car”.

---

**Domonkos Asztalos** · December 11, 2014 at 7:46 pm

Dan, one must have a bunch of requiremnets specifying the scope of the model.

---

**Dan George** · December 11, 2014 at 9:02 pm

Domonkos, well, at least some requirements, anyway :). Remember that Stephen Mellor is an original signatory of the Agile Manifesto for Software Development.

He expressed disappointment that the industry focused on 3GL Agile instead of Model Driven Agile here: [http://www.softed.com/resources/docs/stephen%20mellor%20agile%20manifesto%2010%20years%20on.pdf](http://www.softed.com/resources/docs/stephen%20mellor%20agile%20manifesto%2010%20years%20on.pdf)

I suppose the answer to my question is “it depends” and you really cannot validate a model just by looking at it. You have to know the context and the purpose of the model. The insight can be gained face-to-face, from model notes, requirements, etc.

Cort, it would be great if you could give us a little blurb on the purpose of a particular snippet in future postings. It will help me learn how to do that for my own models.

---

**poj** · December 11, 2014 at 9:16 pm

When it comes to asymmetrical phrases on relations, many of the best examples are just a tiny bit asymmetrical.
A Waypoint is first in a Route, but a Route starts with a Waypoint.

Remember to keep your phrases in the domain you’re modelling. Cort’s example of “owns”/”transports” somewhat mixes two things into the same relation. The ownership of a car is one kind of a relation to a Person, the actual ongoing transportation of Persons are another thing.

When trying to decide if phrases are correctly paired, I try to read it in one direction and then in the other and see if the statements contradict, have nothing to do with each other, or if they supports each other. Non-supporting phrases is an indication of domain mixup in the relation.

---

**Lee Riemenschneider** · January 2, 2015 at 4:29 pm

Domain mixup or an unspecified relationship within the domain. In either case, there’s an indication that the model needs to be revisited.

---

**Lee Riemenschneider** · January 2, 2015 at 4:51 pm

On requirements and Agile: One of the discussions I’ve frequently had with co-workers concerns invariants in the system and known requirements. Most people could probably tell you a number of requirements for a (e.g.) radio off the top of their head, but I’ve heard developers claim those requirements don’t exist until a systems engineer writes them down. Not only that, but those known requirements are often not viewed as invariants that can be modeled and reused in every radio under development. The major problems with requirements change is the lack of recognition and capture of the invariants in the system and poor separation of concerns.

---

**Travis London** · January 24, 2015 at 3:51 pm

Father’s Day

Just thinking about how may day goes, and figured I would have some state machine fun :).

Maybe I could extend on this a build a robot to help out.

Enjoy,
Travis

[![]({{ '/assets/uploads/2015/01/FathersDay.png' | relative_url }})]({{ '/assets/uploads/2015/01/FathersDay.png' | relative_url }})

---

**cort** · May 15, 2015 at 6:23 pm

See Revision Control model snippet here: [http://onefact.net/revision-control/](http://onefact.net/revision-control/)

[![]({{ '/assets/uploads/2015/05/RevControl.png' | relative_url }})]({{ '/assets/uploads/2015/05/RevControl.png' | relative_url }})

- This reply was modified 10 years, 9 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).

---

**Bob Mulvey** · May 22, 2015 at 2:12 pm

Thanks Cort!

---

**cort** · May 25, 2015 at 2:12 pm

Happy Memorial Day (in the USA) and may freedom be enjoyed were you live.

[![]({{ '/assets/uploads/2015/05/MemorialDay.png' | relative_url }})]({{ '/assets/uploads/2015/05/MemorialDay.png' | relative_url }})

---

**cort** · July 21, 2015 at 8:42 pm

[![]({{ '/assets/uploads/2015/07/car_one_row.png' | relative_url }})]({{ '/assets/uploads/2015/07/car_one_row.png' | relative_url }})

An autosampler is a robot used in a laboratory to collect or dispense fluid from a vial. Chemistry, biology and medical labs use these devices. They save time and can be more accurate than non-automated sampling processes.

[![](http://roxsoftware.com/ug/as2class.png)](http://roxsoftware.com/ug/as2class.png)

The model above has classes carousel, row, sampling_probe and probe_assignment. The carousel ‘contains’ row, while the row ‘is rotated by’ the carousel. A sampling_probe ‘is assigned to’ a row.

State machines (not shown) govern the behavior of the class instances. Actions in the states perform the necessary processing for each state of the state machines.

This model *mostly* supports the concept of multiple sampling probes and multiple rows in a carousel. Although to support multiple rows this model would need to change the cardinality on an association. Can you identify which one?

This UML model is the “source code” of an autosampler in field use since the late 1990s. It is a long-standing example of *xtUML Inside*!

[![]({{ '/assets/uploads/2015/07/car_many_rows.png' | relative_url }})]({{ '/assets/uploads/2015/07/car_many_rows.png' | relative_url }})

- This reply was modified 10 years, 6 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}). Reason: added note about device in field

---

**cort** · August 7, 2015 at 10:23 am

The Model Snippet of the Day is a fragment of the xtUML metamodel. A Function defines zero to many Function Parameters (R24). Each Function Parameter precedes and/or succeeds another Function Parameter (R54).
[![]({{ '/assets/uploads/2015/08/function_parameter-300x144.png' | relative_url }})]({{ '/assets/uploads/2015/08/function_parameter-300x144.png' | relative_url }})

---

**cort** · August 17, 2015 at 1:16 pm

[![]({{ '/assets/uploads/2015/08/testing_states.png' | relative_url }})]({{ '/assets/uploads/2015/08/testing_states.png' | relative_url }})
This Model Snippet shows a small state model that sequences test case execution for a model-based testing harness.

---

**cort** · August 19, 2015 at 2:19 am

Yesterday we looked at a state machine traversing the stages of a test case. Here is another view of a system containing that exact model. This system shows a component called ‘ec’ (electrochemical detector) configured together with an ectb (electrochemical testbench) and a test runner. The test case state machine lives in a class inside the ‘ectb’ component. The test case state machine is driving stimulation of the electrochemical detector component and verifying proper response to that stimulation.
Note that this is not a pedagogical example; this is production material for an electrochemistry instrumentation supplier.
\[The boxes are UML components. The connections are UML interfaces (provided with ball-end, required with cup end).\]
[![]({{ '/assets/uploads/2015/08/ectb.png' | relative_url }})]({{ '/assets/uploads/2015/08/ectb.png' | relative_url }})

- This reply was modified 10 years, 6 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).

---

**cort** · September 2, 2015 at 3:46 pm

Here is a model of a weather station (Stevenson Screen). It is likely that there will be more of this coming in the future.

[http://onefact.net/stevenson-screen-weather-station/](http://onefact.net/stevenson-screen-weather-station/)

[![]({{ '/assets/uploads/2015/09/wx_components.png' | relative_url }})]({{ '/assets/uploads/2015/09/wx_components.png' | relative_url }})

---

**cort** · September 3, 2015 at 7:02 pm

The BridgePoint model for the Stevenson Screen (weather station) can be found in the xtuml/models repository in github.
Here: [https://github.com/xtuml/models/tree/master/applications/wx](https://github.com/xtuml/models/tree/master/applications/wx)

---

**cort** · September 17, 2015 at 1:15 pm

Today’s model snippet describes the game of football (fútbol, soccer).

class model

[![]({{ '/assets/uploads/2015/09/futbol-300x189.png' | relative_url }})]({{ '/assets/uploads/2015/09/futbol-300x189.png' | relative_url }})

state model

[![]({{ '/assets/uploads/2015/09/ball_state_machine-300x174.png' | relative_url }})]({{ '/assets/uploads/2015/09/ball_state_machine-300x174.png' | relative_url }})

A bit more of a write-up is here: [http://onefact.net/football-futbol-soccer/](http://onefact.net/football-futbol-soccer/)

- This reply was modified 10 years, 5 months ago by [![](https://secure.gravatar.com/avatar/ca308d0579825a651fd9c17e27bb94d5ca63f6afd5132edc4321556ec82bd246?s=14&amp;d=mm&amp;r=g)cort]({{ '/user/cort/' | relative_url }}).

---

**Bob Mulvey** · September 17, 2015 at 11:18 pm

Looking at the class model, and I don’t quite follow. The importance of good relationship phrases is clear :). Each of the places where the relationship phrase is present, I clearly understand the selected cardinality and conditionality. In the places where relationship phrases are missing I don’t understand the selected cardinality and conditionality.

---

**cort** · September 18, 2015 at 4:54 am

Thanks for the comment, Bob.

Even though I have mostly taught people to always include phrases on both ends, many times it is redundant. Here is a list of the corresponding phrases for the model above:

R1: kicks, is kicked by
R2: bounds, is bound by
R3: coaches, is coached by
R4: penalizes, is penalized by

Keep in mind that an association has a *single* meaning. For example, an incorrect association between referee and player would include phrases.

R4: penalizes, yells at

The *penalize* association and the *yells* association are actually two different relationships.

The moral? Look closely at models and see if you are being good by placing phrases at both ends, but maybe you are mixing two different associations with one link… which leads to bugs!

---

**sm4rpq** · September 19, 2015 at 6:14 am

Maybe just a confusion due to me not being native english speaking and not fully understanding “in bounds”.

But the state machine for the ball has an “out-of-bounds” state from which it can go to various other states. And the class model specifies it to be unconditionally one in bounds of a field. So I would interpret it as when the ball is kicked out of the field it has to be deleted which is in conflict with the state model.

It may also be that I don’t understand the rules of soccer. A sport I would like to see much less of in the newspapers here in Sweden. Much much less.

---

**cort** · September 20, 2015 at 6:17 am

Ah, the amount of news will likely increase before it decreases!

I like your close examination of the model. And your perspective would work. However, in this case, I prefer the idea of having a field that is a preexisting instance that remains for the duration of the game. It is a bit disconcerting to think of the field being deleted.

Let me clarify my use of English in the state model and in the association text phrases.

In the state model I used “out-of-bounds” to mean “outside the lines marked on the field”.
Thus, a ball is out-of-bounds when it is beyond the marking lines on the field. So, the field itself actually includes (some) space outside the bounding lines.

On the class diagram I use “bounds” as a verb synonymous with “provides marking lines”.
A *field* *bounds* zero or one *ball*. In English bounds usually speaks of physically restraining, but here I stretch that meaning just a bit. :)

---

**cort** · October 15, 2015 at 1:38 am

[![]({{ '/assets/uploads/2015/10/experiment.png' | relative_url }})]({{ '/assets/uploads/2015/10/experiment.png' | relative_url }})

Today’s Model Snippet of the Day is Experiment.

[Experiment](http://onefact.net/experiment/)

---

**poj** · October 27, 2015 at 4:42 pm

I would argue that the phrases for R1 in that model is a little bit vague. The phrase ‘is going’ should really be ‘is going to’.

Also, in which contexts is it OK with a conference without attendees? A conference without attendees is a sad conference…

---

**cort** · October 27, 2015 at 5:45 pm

Agreed on all points. A conference with zero attendees is not even a conference at all…

‘is going’ was shorted from ‘is going to’ for social media posting reasons. “self … is going” sounded better than “self … is going to” :)

---

**Dan George** · October 27, 2015 at 6:29 pm

Well, doesn’t it depend on the state model? Surely it would not be a good idea to have a Conference in the Participants Mixing state with no Attendees. But, how does the first prospective Attendee find a conference?

---

**john** · October 27, 2015 at 7:45 pm

I tried to do it in python:
\[code title=”model_snippet.py”\]
from xtuml import relate
from xtuml import where_eq as where

from components import community

me = community.select_any(‘attendee’, where(name=’john’))
conf = community.select_any(‘conference’,
where(name=’xtUML 2015′,
date=’December 7 and 8′,
location=’Lafayette, IN’))

relate(me, conf, 1, ‘is going’)
\[/code\]

but I ran into some trouble:

\[code title=”stdout”\]
Traceback (most recent call last):
File “model_snippet.py”, line 12, in \<module\>
relate(me, conf, 1, ‘is going’)
ModelException: Unable to attend conference: its location is to far away.
\[/code\]

:)

---

**cort** · October 28, 2015 at 3:02 am

O.K. I need some input and plan to discuss this model leading up to a significant write-up. See if the following makes sense.

[![]({{ '/assets/uploads/2015/10/apmodtool.png' | relative_url }})]({{ '/assets/uploads/2015/10/apmodtool.png' | relative_url }})

model abstracts application
model conforms to method
method applies standard
tool enforces standard
tool manifests method
tool edit model

This is just a starting point.

---

**john** · October 28, 2015 at 6:44 am

I tend to see a tool as an automated process governed by user input, unless we are talking AI. So perhaps the tool itself does no do the manifestation, but a user, that uses a tool to automate some task in the methodology.

---

**cort** · October 28, 2015 at 12:43 pm

Thanks, John. Agreed.

A point that I want to make about modeling is the following:
– applications first
– then models (based on a method)
– then tools and standards

The application, the problem to be solved, is the basis.
Models represent captured IP and hold great value.

Everything else must follow as stewardship of the model-encoded applications.

Models are more important than tools.

Thoughts?

(…still interested

---

**cort** · January 6, 2016 at 2:44 pm

Happy New Year 2016!
May your labors in 2016 select many bright opportunities.
[![]({{ '/assets/uploads/2016/01/HappyNewYear2016.png' | relative_url }})]({{ '/assets/uploads/2016/01/HappyNewYear2016.png' | relative_url }})

---

**cort** · February 2, 2016 at 2:52 pm

When modeling an application, you may encounter subject matters that deal with the same information but addressing different requirements. When the requirements are varied enough, it may make sense to model parts of the application on separate class diagrams… each with its own view of the data.

For example, here is a model of the syntax of a language. This model focuses on the content, form and inter-relationships of the elements of the language.

[![]({{ '/assets/uploads/2016/02/modeling.png' | relative_url }})]({{ '/assets/uploads/2016/02/modeling.png' | relative_url }})

This language can be marked with options that affect its translation. Marking deals with the same information but is addressing a separate and substantially different requirement. So, a new view of the data is modeled that focuses on the requirements of providing the needed translation options. In xtUML, this is done with an imported class (or class reference) that is depicted on more than one class diagram.

[![]({{ '/assets/uploads/2016/02/marking.png' | relative_url }})]({{ '/assets/uploads/2016/02/marking.png' | relative_url }})

originally posted here: [http://onefact.net/2-views/](http://onefact.net/2-views/)

---

**cort** · February 10, 2016 at 4:30 pm

xtUML interfaces can be uni-directional or bi-directional. From this graphic you can see small arrows in the port boxes indicating whether the port contains messages that are inbound, outbound or both. The LocationProvider and LocationUtil interfaces are uni-directional and on the Tracking component the messages are all outbound. The UI and HeartRateProvider interfaces contain messages in both directions.
[![]({{ '/assets/uploads/2016/02/ifaces.png' | relative_url }})]({{ '/assets/uploads/2016/02/ifaces.png' | relative_url }})

---

**cort** · March 22, 2016 at 1:29 pm

Model Snippet of the Day: Graphics Elements

xtUML has a model of graphics. Here is a simplified version of it. This model abstracts out very far and distinguishes only diagram, widget, figure, connector and junction.

A diagram depicts widgets. A widget is either a figure (shape) or a coupler (connector). Couplers connect widgets together, meaning that a coupler can have junctions between figures and/or other couplers.

Example figures are class, component, state.
Example couplers are association and transition.

[![](https://scontent-ord1-1.xx.fbcdn.net/hphotos-xpf1/t31.0-8/12440604_598057850348706_3255780885061980589_o.png)](https://scontent-ord1-1.xx.fbcdn.net/hphotos-xpf1/t31.0-8/12440604_598057850348706_3255780885061980589_o.png)

---

**cort** · April 26, 2016 at 2:18 pm

Dog owner owns one to many dogs. Dog is owned by zero or one dog owner.

Relationships in xtUML are a first-class part of the language. Also called associations, these constructs are more than documentation. They are part of the language and constrain the population of instances of the various classes. Associations also allow for quick traversal from an instance of one class to the instances of related classes.

For example, if you know a particular dog owner, you can traverse across R1 to get the set of dogs owned by that dog owner.

Quiz question: Does the model depicted here support the concept of a ‘stray dog’?
[![](https://lh3.googleusercontent.com/-26lwKnQC19s/Vx90ThNf3tI/AAAAAAAABH0/SJm_MPseDAs62VTW6IERAINBmzbYyafzQCL0B/w908-h310-no/13095735_615734671914357_1988017581231378765_n.png)](https://lh3.googleusercontent.com/-26lwKnQC19s/Vx90ThNf3tI/AAAAAAAABH0/SJm_MPseDAs62VTW6IERAINBmzbYyafzQCL0B/w908-h310-no/13095735_615734671914357_1988017581231378765_n.png)

---

**cort** · April 28, 2016 at 1:52 pm

Conditionality and Multiplicity
The answer to the quiz question from yesterday is, “yes”. The model allows for a stray dog (a dog without an owner, poor thing).
The way that the model shows this is by the ‘conditionality’ of the association. On the dog owner end of the relationship ‘0..1’ is shown. This means that a ‘dog is owned by 0 to 1 dog owner’. A dog with zero owners is a stray dog. The relationship is said to be ‘conditional’ on this end.
Also encoded into the ‘0..1’ and ‘1..\*’ are the ‘multiplicities’ of this association. We can understand from the multiplicity that a dog owner can own more than one dog. A dog owner must own at least 1 dog. We can also tell that a dog cannot be owned by more than one dog owner.

---

**cort** · May 5, 2016 at 10:31 am

Modeling an Association

Look around the room you are in. You will see plugs and sockets. Some plugs are in service (plugged in to a socket) and some are not. Some sockets are being used (occupied by a plug) and some are not (except at the airport, where it seems \_all\_ of them are being used).

‘plug’ ‘is plugged in to’ zero-or-one ‘socket’. ‘socket’ ‘is occupied by’ zero-or-one ‘plug’.
This is a one-to-one bi-conditional association. For any instance of plug, we can find out if it is plugged in and to which instance of socket it is connected. If we have an instance of socket “in hand”, we can find the related plug if one is there. Association R1 gives us a lot information about the instance populations of ‘plug’ and ‘socket’.

Consider modeling current flow. In which class do we want to model the current flow?

[![](https://scontent-ord1-1.xx.fbcdn.net/v/t1.0-9/13151853_619085768245914_5865020400092504155_n.png?oh=aa9029574b45ee237b2132b16f66cc54&amp;oe=57A49EFF)](https://scontent-ord1-1.xx.fbcdn.net/v/t1.0-9/13151853_619085768245914_5865020400092504155_n.png?oh=aa9029574b45ee237b2132b16f66cc54&amp;oe=57A49EFF)

Associative Classes

Also called “ternary associations” and “link classes”, associative classes model relationships as data. Instead of just a line with role phrases, the full power of class, attributes and state modeling can be applied to clearly specify the relationship. Associative classes also can participate in other associations.

In our ‘plug’ and ‘socket’ model, we could have modeled ‘current_flow’ on either or both of ‘plug’ and ‘socket’, although it is more clear to model the flow of current through the connection since this flow is through both. ‘Resistance’ would not make sense on the ‘plug’ or the ‘socket’. The resistance to current flow is a function of a particular ‘plug’ being connected to a particular ‘socket’.

In complex systems, the relationships between resources in the system are often a focus on study. In such systems there are limited resources that must be allocated and shared. One object in a system will “want to be associated” with another object, but it is busy. Such patterns can leverage associative classes nicely.

[![](https://scontent-ord1-1.xx.fbcdn.net/v/t1.0-9/13100782_619143601573464_6094841091044809431_n.png?oh=e43a8f6739897369fc5afaea1278b5f6&amp;oe=579F4C11)](https://scontent-ord1-1.xx.fbcdn.net/v/t1.0-9/13100782_619143601573464_6094841091044809431_n.png?oh=e43a8f6739897369fc5afaea1278b5f6&amp;oe=579F4C11)

---

**cort** · January 3, 2017 at 6:15 pm

This is a model of “marking” (linking model compiler features to application model elements). Most development starts like this with a rough sketch on scrap paper and reviewed over soup and fries at lunchtime.

BTW, a marking editor is being added BridgePoint.

[![]({{ '/assets/uploads/2017/01/markingmodel.jpg' | relative_url }})]({{ '/assets/uploads/2017/01/markingmodel.jpg' | relative_url }})
