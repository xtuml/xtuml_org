---
redirect_from:
  - "/community/topic/idiosyncratic-parsing/"

layout: "topic"
title: "Idiosyncratic parsing"
date: "2021-06-16"
permalink: "/forums/topic/idiosyncratic-parsing/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Clive** · June 16, 2021 at 3:00 am

Much of the time the automatic type-as-you-go parsing works quite well and is certainly a necessary and helpful tool. However, over the last few days, I’ve found the parsing process to be slow and because of that, somewhat misleading. In fact there’s been many occasions when the little white cross in the red circle does not disappear when the identified parsing errors are fixed. Sometimes going to the ‘project menu’ and choosing “Parse All Activities” helps by removing the stubborn error indicators, but sometimes I have to repeat “Parse All Activities” in order to be sure. It’s not a ‘biggy’ but it is (at times) a nuisance and tends to waste time when trying to put together a model.

I’m using BP 7.1 on MacOS Big Sur.

I got into a real bind when accidentally writing an invocation for an instance operation when it was actually a class operation. Easily fixed (I thought) but when I did fix the error, nothing indicating the error changed. I then selected “Parse All Activities” but the indicated errors still didn’t disappear. It took another few minutes before the error indicators disappeared of their own accord!?

---

**cort** · June 16, 2021 at 9:12 am

You are observing mostly normal behavior. Between the challenge of parsing larger bodies of OAL/model and the finicky Eclipse error marker mechanism, we get this difficulty.

Error markers are actually the facade of an error marker file that is persisted. Eclipse is not 100% reliable in removing these even after an error has been resolved.

You should have an Errors view, usually in the bottom pane of your perspective. You can manually delete the errors here. This is safe, because a re-parse will recreate any legitimate errors.

---

**Clive** · June 17, 2021 at 6:51 pm

Thanks Cort.
I certainly do keep the Errors view open. So, I guess you are implying that it is the Errors view that indicates fact (sometimes more than One Fact of course) :-). If there are no errors listed in the Errors view, even though there may be markers in the OAL Editor view, then I should ignore the markers!?

---

**Bob Mulvey** · June 17, 2021 at 7:05 pm

Here is what I tend to do…
1. Never use “build automatically”
2. If I see errors in error/problem view that do not seem right to me, manually delete them
3. Build manually ,or, touch the code to force a new parse.

Note that the above is what I have learned over time working with misc tools in Eclipse, not only BridgePoint. It resolves the issue for me and let’s me do my work. Hope it helps you!
