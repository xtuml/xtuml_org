---
layout: unit
title: Exercise - Selections
permalink: /learn/courses/xtuml-editor-developer-training/exercise-selections/
module: Module 5
module_title: Understanding the OOAofOOA and Source Code Layout
unit: Unit 5
course_title: xtUML Editor Developer Training
course_url: /learn/courses/xtuml-editor-developer-training/
redirect_from:
- /module-5/exercise-selections/
prev: /learn/courses/xtuml-editor-developer-training/compare-and-contrast-select-statements-in-oal-and-java/
prev_title: Compare and contrast select statements in OAL and Java
next: /learn/courses/xtuml-editor-developer-training/exercise-inspect-data-via-context-menu-entry/
next_title: Exercise - Inspect data via context menu entry
---

Time for another exercise.

Your task:

- Add a new function `boolean isInPackage()` to `ModelClass_c.java`. The function shall return `true` if the parent of the class is a Package, otherwise it shall return `false`.
- Write the necessary OAL selection as a comment inside this operation, then write the actual implementation in Java.
- Call the new `isInPackage()` from `ModelClass_c.setKey_lett()`
- Build
- Run the xtUML Editor Application in debug mode. Show via breakpoint and stepping that the function successfully returns `true` for a class inside a package.
