---
redirect_from:
  - "/community/topic/status-of-egit-integration/"

layout: "topic"
title: "Status of EGit integration"
date: "2017-02-15"
permalink: "/forums/topic/status-of-egit-integration/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**micke.x** · February 15, 2017 at 10:28 am

Hi,

is the Egit integration working as it is supposed to?

I have problems using Git in BP 5.5.
I try to use it in the same way that worked reasonable in BP 5.1, but I get problems when trying to set up CM for a project.
Eclipse 4.5.2
BP 5.5.0 8321_Model_Element_Move
EGit 4.1.1.201511131810-r

The problem I get is the following:
– for a Project, I select Team/Share…
– select Git
– Create…
After entering a location for the new repository, I get an error message:
“Unhandled event loop exception
Should not get here”

Proceeding after this results in another error message dialog that disappears quickly.

The error log is listed below.

The state after the command is that
– the files seem to be copied to the new git repository OK
– label decorations are not shown for workspace items as expected

Trying Team / Synchronize Workspace and switching to Git Perspective gives another error log message:
!ENTRY org.eclipse.ui.navigator.resources 4 0 2017-02-15 10:46:07.426
!MESSAGE Could not acquire INavigatorContentService: Project Explorer not found.

Does anyone recognize this problem?

/Michael

error log after create Git repository:
——————————————————————
!ENTRY org.eclipse.ui 4 0 2017-02-15 10:42:51.501
!MESSAGE Unhandled event loop exception
!STACK 0
java.lang.InternalError: Should not get here
at sun.nio.fs.WindowsNativeDispatcher.CreateSymbolicLink0(Native Method)
at sun.nio.fs.WindowsNativeDispatcher.CreateSymbolicLink(Unknown Source)
at sun.nio.fs.WindowsFileSystemProvider.createSymbolicLink(Unknown Source)
at java.nio.file.Files.createSymbolicLink(Unknown Source)
at org.eclipse.jgit.util.FileUtils.createSymLink(FileUtils.java:415)
at org.eclipse.jgit.util.FS.createSymLink(FS.java:704)
at org.eclipse.jgit.util.FS_Win32.detectSymlinkSupport(FS_Win32.java:171)
at org.eclipse.jgit.util.FS_Win32.supportsSymlinks(FS_Win32.java:162)
at org.eclipse.jgit.internal.storage.file.FileRepository.create(FileRepository.java:306)
at org.eclipse.jgit.api.InitCommand.call(InitCommand.java:115)
at org.eclipse.egit.ui.internal.repository.NewRepositoryWizard.performFinish(NewRepositoryWizard.java:77)
at org.eclipse.jface.wizard.WizardDialog.finishPressed(WizardDialog.java:799)
at org.eclipse.jface.wizard.WizardDialog.buttonPressed(WizardDialog.java:429)
at org.eclipse.jface.dialogs.Dialog\$2.widgetSelected(Dialog.java:619)
at org.eclipse.swt.widgets.TypedListener.handleEvent(TypedListener.java:248)
at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
at org.eclipse.swt.widgets.Display.sendEvent(Display.java:4362)
at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1113)
at org.eclipse.swt.widgets.Display.runDeferredEvents(Display.java:4180)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3769)
at org.eclipse.jface.window.Window.runEventLoop(Window.java:827)
at org.eclipse.jface.window.Window.open(Window.java:803)
at org.eclipse.egit.ui.internal.sharing.ExistingOrNewPage\$3.widgetSelected(ExistingOrNewPage.java:186)
at org.eclipse.swt.widgets.TypedListener.handleEvent(TypedListener.java:248)
at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
at org.eclipse.swt.widgets.Display.sendEvent(Display.java:4362)
at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1113)
at org.eclipse.swt.widgets.Display.runDeferredEvents(Display.java:4180)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3769)
at org.eclipse.jface.window.Window.runEventLoop(Window.java:827)
at org.eclipse.jface.window.Window.open(Window.java:803)
at org.eclipse.team.internal.ui.wizards.ConfigureProjectWizard.openWizard(ConfigureProjectWizard.java:224)
at org.eclipse.team.internal.ui.wizards.ConfigureProjectWizard.shareProjects(ConfigureProjectWizard.java:124)
at org.eclipse.team.internal.ui.actions.ConfigureProjectAction\$1.run(ConfigureProjectAction.java:39)
at org.eclipse.team.internal.ui.actions.TeamAction\$3.run(TeamAction.java:266)
at org.eclipse.swt.custom.BusyIndicator.showWhile(BusyIndicator.java:70)
at org.eclipse.team.internal.ui.actions.TeamAction.run(TeamAction.java:263)
at org.eclipse.team.internal.ui.actions.ConfigureProjectAction.execute(ConfigureProjectAction.java:33)
at org.eclipse.team.internal.ui.actions.TeamAction.run(TeamAction.java:515)
at org.eclipse.team.internal.ui.actions.TeamAction.runWithEvent(TeamAction.java:549)
at org.eclipse.ui.internal.PluginAction.runWithEvent(PluginAction.java:237)
at org.eclipse.jface.action.ActionContributionItem.handleWidgetSelection(ActionContributionItem.java:595)
at org.eclipse.jface.action.ActionContributionItem.access\$2(ActionContributionItem.java:511)
at org.eclipse.jface.action.ActionContributionItem\$5.handleEvent(ActionContributionItem.java:420)
at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
at org.eclipse.swt.widgets.Display.sendEvent(Display.java:4362)
at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1113)
at org.eclipse.swt.widgets.Display.runDeferredEvents(Display.java:4180)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3769)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine\$4.run(PartRenderingEngine.java:1127)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:337)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine.run(PartRenderingEngine.java:1018)
at org.eclipse.e4.ui.internal.workbench.E4Workbench.createAndRunUI(E4Workbench.java:156)
at org.eclipse.ui.internal.Workbench\$5.run(Workbench.java:694)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:337)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:606)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:150)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:139)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:134)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:104)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:380)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:235)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
at java.lang.reflect.Method.invoke(Unknown Source)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:669)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:608)
at org.eclipse.equinox.launcher.Main.run(Main.java:1515)

!ENTRY org.eclipse.egit.core 4 0 2017-02-15 10:43:12.093
!MESSAGE Remove repository mapping of Git mapped resource for which project or mapped git repository has disappeared: ‘RepositoryMapping\[\<empty\> -\> ‘../../.git’, absolute path: ‘C:/Users/eeiilnc/git5/.git’ \]’
!STACK 0
java.io.FileNotFoundException:
at org.eclipse.egit.core.project.GitProjectData.logAndUnmapGoneMappedResource(GitProjectData.java:544)
at org.eclipse.egit.core.project.GitProjectData.map(GitProjectData.java:510)
at org.eclipse.egit.core.project.GitProjectData.remapAll(GitProjectData.java:479)
at org.eclipse.egit.core.project.GitProjectData.setRepositoryMappings(GitProjectData.java:321)
at org.eclipse.egit.core.op.ConnectProviderOperation.connectProject(ConnectProviderOperation.java:154)
at org.eclipse.egit.core.op.ConnectProviderOperation.execute(ConnectProviderOperation.java:105)
at org.eclipse.egit.ui.internal.sharing.SharingWizard\$1.run(SharingWizard.java:113)
at org.eclipse.jface.operation.ModalContext\$ModalContextThread.run(ModalContext.java:119)

!ENTRY org.eclipse.egit.core 4 0 2017-02-15 10:43:12.146
!MESSAGE Unmapping gone mapped resource {0} failed
!STACK 1
org.eclipse.team.core.TeamException: No provider registered for MicrowaveOven.
at org.eclipse.team.internal.core.TeamPlugin.wrapException(TeamPlugin.java:142)
at org.eclipse.team.core.RepositoryProvider.unmap(RepositoryProvider.java:289)
at org.eclipse.egit.core.project.GitProjectData\$UnmapJob.run(GitProjectData.java:580)
at org.eclipse.core.internal.jobs.Worker.run(Worker.java:55)
Caused by: org.eclipse.team.core.TeamException: No provider registered for MicrowaveOven.
at org.eclipse.team.core.RepositoryProvider.unmap(RepositoryProvider.java:256)
… 2 more
!SUBENTRY 1 org.eclipse.team.core 4 0 2017-02-15 10:43:12.147
!MESSAGE No provider registered for MicrowaveOven.
!STACK 1
org.eclipse.team.core.TeamException: No provider registered for MicrowaveOven.
at org.eclipse.team.core.RepositoryProvider.unmap(RepositoryProvider.java:256)
at org.eclipse.egit.core.project.GitProjectData\$UnmapJob.run(GitProjectData.java:580)
at org.eclipse.core.internal.jobs.Worker.run(Worker.java:55)
!SUBENTRY 2 org.eclipse.team.core 4 0 2017-02-15 10:43:12.147
!MESSAGE No provider registered for MicrowaveOven.

---

**cort** · February 15, 2017 at 12:31 pm

My team is using EGit every day. We sometimes hit an EGit bug, but it mostly works fine.

Did you add your local clones as local git repositories (from the Git perspective)?

---

**micke.x** · February 15, 2017 at 12:46 pm

Hi,
thank you for your feedback.

I do not understand
“Did you add your local clones as local git repositories (from the Git perspective)”.

My scenario is that I have a non-versioned model in BP.
I want to be able to share it with others, so I choose Team/Share…

I have no clones or no central repository.
It is just the local repository I want to create and work with for the time being, exploring the model based compare/merge functionality of BP.
I am using only local branches.

regards
Michael

- This reply was modified 9 years ago by [![](https://secure.gravatar.com/avatar/b701ff482b4e987013c98935ef4f510fe8db42f26a11191f2e382ab039bb0013?s=14&amp;d=mm&amp;r=g)micke.x]({{ '/user/micke-x/' | relative_url }}).

---

**micke.x** · February 15, 2017 at 2:02 pm

Some more information.

After the “Share” operation, that partly failed,
I can “sort of” work with Git and the model, but they are not tightly connected, i.e.:
– there are no Git label decorations on the entities in the model view structure
– there are no Git commands available for model entities using pop-up / Team
– Git views (staging etc.) are not automatically kept in sync (I have to manually refresh)
– the Compare views (after choosing Merge Tool for a conflict after merging two branches) seems even less useful (compared to 5.1) – I cannot push/accept changes from right-to-left, for example (could perhaps be a consequence of the previous problem)

regards
Michael

---

**micke.x** · February 17, 2017 at 10:07 am

It seems like the problem was related to the versions of the different components.
Somehow the Eclipse and EGit was updated to 4.5.2 and 4.1.1…
Re-installing BP, and using the bundled Eclipse 4.5.1 and EGit 4.0.3, Egit works as expected…
