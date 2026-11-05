---
layout: unit
title: Setting up to run JUnits
permalink: /learn/courses/xtuml-editor-developer-training/setting-up-to-run-junits/
module: Module 7
module_title: JUnit Testing
unit: Unit 2
course_title: xtUML Editor Developer Training
course_url: /learn/courses/xtuml-editor-developer-training/
redirect_from:
- /module-7/setting-up-to-run-junits/
prev: /learn/courses/xtuml-editor-developer-training/tour-of-the-junit-plug-ins/
prev_title: Tour of the JUnit plug-ins
next: /learn/courses/xtuml-editor-developer-training/exercise-run-junit-tests/
next_title: Exercise - Run JUnit tests
---

The xtUML Editor JUnit test cases require some special configuration in order to run successfully. Due to the functionality of the screen manipulations and screen comparisons, some of the tests only run on Windows.

Some additional configuration of the development environment is necessary to run the JUnit tests.

- Open Git Repository Exploring perspective. Select the button to *Clone a Git Repository and add the clone to this view*.
  - Using the wizard as performed previously, clone `https://github.com/xtuml/models.git` to a local repository (*Example: c:/git/xtuml/models*).
- Open `c:/MentorGraphics/xtUMLEditor/eclipse/Launcher.bat` in a text editor.
  - After the `set BP_JVM=...` line add the following (adjusted for your previously chosen repository locations):

```
set XTUML_TEST_MODEL_REPOSITORY=C:/git/xtuml/models/test/
set XTUML_DEVELOPMENT_REPOSITORY=C:/git/xtum/editor
```

- Prepare to run unit tests (on MS Windows):
  - Exit xtUML Editor.
  - Configure Windows Vista or Windows 7 for unit test running.
    - Bring up the Windows Color and Appearance settings.
      - Right click on the desktop background and select Personalize.
        - In Vista select the Windows Color and Appearance hyperlink.
        - In Windows 7 select the Window Color hyperlink, then "Advanced appearance settings..."
      - In the dialog window that appears, change the following attributes:
        - Active Title Bar — Size: 25, Font: Trebuchet 10
        - Border Padding — Size: 0
        - Caption Buttons — Size: 25
        - Icon — Size: 32, Font: Tahoma 8
        - Inactive Title Bar — Size: 25, Font: Trebuchet 10
        - Menu — Size: 19, Font: Tahoma 8
        - Message Box — Font: Tahoma 8
        - Palette Title — Size: 17, Font: Tahoma 8
        - Selected Items — Size: 19, Font: Tahoma 8
        - Tooltip — Font: Tahoma 8
      - If you have a smaller screen or resolution potential you may need to configure the start menu to not always be on top, or set it to auto-hide.
      - Do not use the Windows setting that scales text to make it easier to see. In Windows 7 this is Personalization > Display > "Make it easier to read what is on your machine". This setting must be "smaller" 100%. If it is adjusted, graphical compare results will not match.
      - Save this modified theme to make it easier to switch back to at a later time.
- Launch xtUML Editor.
- Set the unit test history to assure the test summary tool captures all results.
  - Open the JUnit view.
  - Select the drop-down arrow in the upper-right of the view.
  - Select the History… option.
  - Set "Maximum count of remembered test runs" to 30.
