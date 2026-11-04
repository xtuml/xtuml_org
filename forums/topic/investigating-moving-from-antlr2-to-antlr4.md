---
redirect_from:
  - "/community/topic/investigating-moving-from-antlr2-to-antlr4/"

layout: "topic"
title: "Investigating moving from antlr2 to antlr4"
date: "2016-06-10"
permalink: "/forums/topic/investigating-moving-from-antlr2-to-antlr4/"
forum: "BridgePoint Development and Integrations"
forum_slug: "bridgepoint-development-and-integrations"
forum_url: "/forums/bridgepoint-development-and-integrations/"
---

**nehad** · June 10, 2016 at 10:01 pm

As part of moving BridgePoint code base under Eclipse management, it needed to move from Antlr2 to Antlr4

As Antlr2 open-source license is unclear and Eclipse could not include it, therefore the need to move antlr4 became necessary.

There are customization done to antlr2 -rename as pt_antlr- to fit BridgePoint needs,
We need to find all these customization, whether antlr4 supports what we need natively, and estimates how much work there is to go from 2.7 to 4.

- This topic was modified 9 years, 8 months ago by [![](https://secure.gravatar.com/avatar/caf2eaa23d362ed6faf5029f93a6daa2fa184875a5cf2bc4f1dfa5fd55cc8e13?s=14&amp;d=mm&amp;r=g)nehad]({{ '/user/nehad/' | relative_url }}).

---

**cort** · June 10, 2016 at 10:12 pm

What are the customizations for?
Do we need them?

---

**nehad** · June 11, 2016 at 7:09 pm

Here what I know so far.
Antlr – antlr4 at least- uses the input grammar to generate Lexar and Parser, with Listeners that notify user when token is recognized, and rule is parsed.

In pt_antlr, we turned off the generation of antlr parser/lexer, that is why we renamed the grammar file from .g to .bnf (I need to double check on this)

So we use antlr to create abstract syntax tree aka AST, and we modified antlr to create our own AST parser to output SQL that populate the model under als project

This SQL file is input for grammar_enhancer.arc that determine which rules needs validations by ! character (another change from antlr as this character has different purpose in antlr), and emit the rule definitions for each rule with the validation function
invocations invoked as needed.

Another archetype runs, this time to create db with these sql instances and all datatypes needed, these information is written in oal_functions.sql

the grammar enhancer generates oal.g which input to antlr to generate oalParser (this part I do not understand yet, why we make this workaround, and oal.g looks like a java class more than grammar syntax)

oal_lex.g is used by antlr to create oalLexer (the oal_lex.g is not generated file, I do not understand this yet, I was expecting to have single .g file used for both parser and lexer generation)

I still do not know why we made these changes yet, as I do not know what lacks in antlr2 causes this work.

I also do not understand why do we need the oal model, and why we generate sql out of AST

I read that there was intention to support another action language when this work is done, but I do not see still how this helps in that.

Regarding moving to in antlr4, I think we either gonna change it to output SQL that populate the oal model, or we will get rid of that if possible, and rely on the listener/visitor invocations to invoke the validation functions.

But we might have issue if we get rid of SQL part, as oal_validate archetype uses the output files from this process to create oal_validate.java

I will look into the build process, generate.xml file, and the named archetypes above so have better understanding how things work correctly and how they fit together.

If anyone has information helps in this investigation or correct wrong information I mentioned above, that would be wonderful :)

- This reply was modified 9 years, 8 months ago by [![](https://secure.gravatar.com/avatar/caf2eaa23d362ed6faf5029f93a6daa2fa184875a5cf2bc4f1dfa5fd55cc8e13?s=14&amp;d=mm&amp;r=g)nehad]({{ '/user/nehad/' | relative_url }}).

---

**nehad** · August 2, 2016 at 4:21 pm

The migration to antlr4 should not be an issue, we are not having a big change in antlr.
I checked the java generation for antlr2, and I could not find change we made there.

To test this, we just need to use Antlr4 to generate the lexer and parser from the two .g files in the oal.als project
My exceptation we will have same output
If that happens, that means the only change in antlr is the SQL conversion (parsing the AST to generate SQL instead of Java)
I know this while ago, but I could not test it out. So I thought to say it, until I do
