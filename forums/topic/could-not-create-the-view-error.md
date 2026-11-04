---
redirect_from:
  - "/community/topic/could-not-create-the-view-error/"

layout: "topic"
title: "Could not create the view error"
date: "2013-02-06"
permalink: "/forums/topic/could-not-create-the-view-error/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**Domonkos Asztalos** · February 6, 2013 at 5:25 pm

I use Ubuntu 10.04
I can create a new project in an empty workspace, but when I want to use it next time I get the error:
Could not create the view: Plug-in com.mentor.nucleus.bp.ui.explorer was unable to load class com.mentor.nucleus.bp.ui.explorer.ExplorerView.
The first line of the details is:
org.eclipse.core.runtime.internal.adaptor.EclipseLazyStarter\$TerminatingClassNotFoundException: An error occurred while automatically activating bundle com.mentor.nucleus.bp.ui.explorer (692).
Any help?

---

**keithbrown** · February 7, 2013 at 2:59 pm

Domonkos,

Is this the sequence?:

\_- Start xtUML Editor on a fresh workspace
\_- Create a project
\_- Exit xtUML Editor
\_- Start xtUML Editor on the previous workspace
\_R ERROR: Model Explorer view doesn’t show, gives exception information where the view should be

I do not experience this problem on RedHat EL5. Have you tried the sequence on a different workspace? You can also provide more information by pasting the information from /.metadata/.log here.

---

**Lee Riemenschneider** · February 13, 2013 at 4:45 pm

Domankos,
Post which version of Java you are using as well. I’ll try to duplicate on my Ubuntu installation.

---

**Domonkos Asztalos** · February 14, 2013 at 4:01 pm

Yes, I tried it with several different workspaces.
The recent trial was the same, here is the Details(log):

org.eclipse.core.runtime.internal.adaptor.EclipseLazyStarter\$TerminatingClassNotFoundException: An error occurred while automatically activating bundle com.mentor.nucleus.bp.ui.explorer (692).
at org.eclipse.core.runtime.internal.adaptor.EclipseLazyStarter.postFindLocalClass(EclipseLazyStarter.java:125)
at org.eclipse.osgi.baseadaptor.loader.ClasspathManager.findLocalClass(ClasspathManager.java:449)
at org.eclipse.osgi.internal.baseadaptor.DefaultClassLoader.findLocalClass(DefaultClassLoader.java:211)
at org.eclipse.osgi.internal.loader.BundleLoader.findLocalClass(BundleLoader.java:376)
at org.eclipse.osgi.internal.loader.BundleLoader.findClassInternal(BundleLoader.java:452)
at org.eclipse.osgi.internal.loader.BundleLoader.findClass(BundleLoader.java:405)
at org.eclipse.osgi.internal.loader.BundleLoader.findClass(BundleLoader.java:393)
at org.eclipse.osgi.internal.baseadaptor.DefaultClassLoader.loadClass(DefaultClassLoader.java:105)
at java.lang.ClassLoader.loadClass(ClassLoader.java:252)
at org.eclipse.osgi.internal.loader.BundleLoader.loadClass(BundleLoader.java:321)
at org.eclipse.osgi.framework.internal.core.BundleHost.loadClass(BundleHost.java:231)
at org.eclipse.osgi.framework.internal.core.AbstractBundle.loadClass(AbstractBundle.java:1193)
at org.eclipse.core.internal.registry.osgi.RegistryStrategyOSGI.createExecutableExtension(RegistryStrategyOSGI.java:160)
at org.eclipse.core.internal.registry.ExtensionRegistry.createExecutableExtension(ExtensionRegistry.java:874)
at org.eclipse.core.internal.registry.ConfigurationElement.createExecutableExtension(ConfigurationElement.java:243)
at org.eclipse.core.internal.registry.ConfigurationElementHandle.createExecutableExtension(ConfigurationElementHandle.java:51)
at org.eclipse.ui.internal.WorkbenchPlugin\$1.run(WorkbenchPlugin.java:267)
at org.eclipse.swt.custom.BusyIndicator.showWhile(BusyIndicator.java:70)
at org.eclipse.ui.internal.WorkbenchPlugin.createExtension(WorkbenchPlugin.java:263)
at org.eclipse.ui.internal.registry.ViewDescriptor.createView(ViewDescriptor.java:63)
at org.eclipse.ui.internal.ViewReference.createPartHelper(ViewReference.java:324)
at org.eclipse.ui.internal.ViewReference.createPart(ViewReference.java:226)
at org.eclipse.ui.internal.WorkbenchPartReference.getPart(WorkbenchPartReference.java:595)
at org.eclipse.ui.internal.WorkbenchPage\$ActivationList.setActive(WorkbenchPage.java:4212)
at org.eclipse.ui.internal.WorkbenchPage\$18.runWithException(WorkbenchPage.java:3271)
at org.eclipse.ui.internal.StartupThreading\$StartupRunnable.run(StartupThreading.java:31)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:134)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:3468)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3115)
at org.eclipse.ui.application.WorkbenchAdvisor.openWindows(WorkbenchAdvisor.java:803)
at org.eclipse.ui.internal.Workbench\$28.runWithException(Workbench.java:1384)
at org.eclipse.ui.internal.StartupThreading\$StartupRunnable.run(StartupThreading.java:31)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:134)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:3468)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3115)
at org.eclipse.ui.internal.Workbench.runUI(Workbench.java:2316)
at org.eclipse.ui.internal.Workbench.access\$4(Workbench.java:2221)
at org.eclipse.ui.internal.Workbench\$5.run(Workbench.java:500)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:493)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:149)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:113)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:194)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:368)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:179)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
at java.lang.reflect.Method.invoke(Method.java:597)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:559)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:514)
at org.eclipse.equinox.launcher.Main.run(Main.java:1311)
Caused by: org.osgi.framework.BundleException: Exception in com.mentor.nucleus.bp.ui.explorer.ExplorerPlugin.start() of bundle com.mentor.nucleus.bp.ui.explorer.
at org.eclipse.osgi.framework.internal.core.BundleContextImpl.startActivator(BundleContextImpl.java:805)
at org.eclipse.osgi.framework.internal.core.BundleContextImpl.start(BundleContextImpl.java:754)
at org.eclipse.osgi.framework.internal.core.BundleHost.startWorker(BundleHost.java:352)
at org.eclipse.osgi.framework.internal.core.AbstractBundle.start(AbstractBundle.java:280)
at org.eclipse.osgi.framework.util.SecureAction.start(SecureAction.java:408)
at org.eclipse.core.runtime.internal.adaptor.EclipseLazyStarter.postFindLocalClass(EclipseLazyStarter.java:111)
… 55 more
Caused by: java.lang.NoClassDefFoundError: Could not initialize class com.mentor.jeda.comps.JetInitHeap
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.initConnection(BridgePointLicenseManager.java:120)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.getLicenseInternal(BridgePointLicenseManager.java:155)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.isEditorLicensed(BridgePointLicenseManager.java:305)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.isEditorLicensed(BridgePointLicenseManager.java:292)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.processStatement(ImportModelComponent.java:1517)
at com.mentor.nucleus.bp.io.core.SqlParser.insert_statement(SqlParser.java:134)
at com.mentor.nucleus.bp.io.core.SqlParser.sql_file(SqlParser.java:74)
at com.mentor.nucleus.bp.io.core.CoreImport.doLoadSql(CoreImport.java:262)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.run(ImportModelComponent.java:151)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:662)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:618)
at com.mentor.nucleus.bp.core.Package_c.PackageInstance(Package_c.java:2861)
at com.mentor.nucleus.bp.core.Package_c.PackageInstance(Package_c.java:2890)
at com.mentor.nucleus.bp.ui.canvas.Cl_c.Getinstancefromooa_id(Cl_c.java:496)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.finishComponentLoad(ImportModelComponent.java:575)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:671)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:618)
at com.mentor.nucleus.bp.core.common.PersistenceManager.initialize(PersistenceManager.java:465)
at com.mentor.nucleus.bp.core.common.PersistenceManager.getDefaultInstance(PersistenceManager.java:72)
at com.mentor.nucleus.bp.ui.explorer.ExplorerPlugin.start(Unknown Source)
at org.eclipse.osgi.framework.internal.core.BundleContextImpl\$1.run(BundleContextImpl.java:782)
at java.security.AccessController.doPrivileged(Native Method)
at org.eclipse.osgi.framework.internal.core.BundleContextImpl.startActivator(BundleContextImpl.java:773)
… 60 more

---

**Domonkos Asztalos** · February 14, 2013 at 4:04 pm

I use the Java 1.6
All the problems are reproduced with Ububtu 12.04

---

**Lee Riemenschneider** · February 14, 2013 at 4:16 pm

Open Java or Sun (Oracle) Java?

---

**Domonkos Asztalos** · February 14, 2013 at 4:19 pm

More points:
when I open a new workspace and select the Quick Start option from the Welcome menu and I click one of the Example Applications (like microwave oven) then also something goes wrong:
In the Model Explorer one can see only the one project item and clicking on it you get:
An error has occurred. See error log for more details.
Could not initialize class com.mentor.jeda.comps.JetInitHeap

Details from the error log are:
!SESSION 2013-02-14 17:11:15.422 ———————————————–
eclipse.buildId=I20090611-1540
java.version=1.6.0_14
java.vendor=Sun Microsystems Inc.
BootLoader constants: OS=linux, ARCH=x86, WS=gtk, NL=hu_HU
Framework arguments: -product com.mentor.nucleus.bp.pkg.BridgePoint
Command-line arguments: -os linux -ws gtk -arch x86 -product com.mentor.nucleus.bp.pkg.BridgePoint

!ENTRY org.eclipse.equinox.p2.repository 4 0 2013-02-14 17:11:16.275
!MESSAGE ProvisioningEventBus could not be obtained. Metadata caches may not be cleaned up properly.

!ENTRY org.eclipse.ui.intro 4 0 2013-02-14 17:11:32.686
!MESSAGE Could not load SWT style: css/root_swt.properties
!STACK 0
java.net.MalformedURLException: no protocol: css/root_swt.properties
at java.net.URL.(URL.java:567)
at java.net.URL.(URL.java:464)
at java.net.URL.(URL.java:413)
at org.eclipse.ui.internal.intro.impl.swt.SharedStyleManager.load(SharedStyleManager.java:66)
at org.eclipse.ui.internal.intro.impl.swt.PageStyleManager.(PageStyleManager.java:66)
at org.eclipse.ui.internal.intro.impl.swt.RootPageForm.createPartControl(RootPageForm.java:177)
at org.eclipse.ui.internal.intro.impl.presentations.FormIntroPartImplementation.createMainPageBook(FormIntroPartImplementation.java:168)
at org.eclipse.ui.internal.intro.impl.presentations.FormIntroPartImplementation.dynamicCreatePartControl(FormIntroPartImplementation.java:137)
at org.eclipse.ui.internal.intro.impl.presentations.FormIntroPartImplementation.createPartControl(FormIntroPartImplementation.java:99)
at org.eclipse.ui.internal.intro.impl.model.IntroPartPresentation.createPartControl(IntroPartPresentation.java:268)
at org.eclipse.ui.intro.config.CustomizableIntroPart.createPartControl(CustomizableIntroPart.java:204)
at org.eclipse.ui.internal.ViewIntroAdapterPart.createPartControl(ViewIntroAdapterPart.java:98)
at org.eclipse.ui.internal.ViewReference.createPartHelper(ViewReference.java:367)
at org.eclipse.ui.internal.ViewReference.createPart(ViewReference.java:226)
at org.eclipse.ui.internal.WorkbenchPartReference.getPart(WorkbenchPartReference.java:595)
at org.eclipse.ui.internal.Perspective.showView(Perspective.java:2228)
at org.eclipse.ui.internal.WorkbenchPage.busyShowView(WorkbenchPage.java:1067)
at org.eclipse.ui.internal.WorkbenchPage\$20.run(WorkbenchPage.java:3816)
at org.eclipse.swt.custom.BusyIndicator.showWhile(BusyIndicator.java:70)
at org.eclipse.ui.internal.WorkbenchPage.showView(WorkbenchPage.java:3813)
at org.eclipse.ui.internal.WorkbenchPage.showView(WorkbenchPage.java:3789)
at org.eclipse.ui.internal.WorkbenchIntroManager.createIntro(WorkbenchIntroManager.java:173)
at org.eclipse.ui.internal.WorkbenchIntroManager.showIntro(WorkbenchIntroManager.java:120)
at org.eclipse.ui.application.WorkbenchWindowAdvisor.openIntro(WorkbenchWindowAdvisor.java:177)
at org.eclipse.ui.internal.ide.application.IDEWorkbenchWindowAdvisor.openIntro(IDEWorkbenchWindowAdvisor.java:467)
at org.eclipse.ui.internal.WorkbenchWindow.open(WorkbenchWindow.java:778)
at org.eclipse.ui.internal.Workbench\$22.runWithException(Workbench.java:1059)
at org.eclipse.ui.internal.StartupThreading\$StartupRunnable.run(StartupThreading.java:31)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:134)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:3468)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3115)
at org.eclipse.ui.application.WorkbenchAdvisor.openWindows(WorkbenchAdvisor.java:803)
at org.eclipse.ui.internal.Workbench\$28.runWithException(Workbench.java:1384)
at org.eclipse.ui.internal.StartupThreading\$StartupRunnable.run(StartupThreading.java:31)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:134)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:3468)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3115)
at org.eclipse.ui.internal.Workbench.runUI(Workbench.java:2316)
at org.eclipse.ui.internal.Workbench.access\$4(Workbench.java:2221)
at org.eclipse.ui.internal.Workbench\$5.run(Workbench.java:500)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:493)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:149)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:113)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:194)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:368)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:179)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
at java.lang.reflect.Method.invoke(Method.java:597)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:559)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:514)
at org.eclipse.equinox.launcher.Main.run(Main.java:1311)

!ENTRY org.eclipse.ui.intro 4 0 2013-02-14 17:11:32.753
!MESSAGE Could not load SWT style: css/root_swt.properties
!STACK 0
java.net.MalformedURLException: no protocol: css/root_swt.properties
at java.net.URL.(URL.java:567)
at java.net.URL.(URL.java:464)
at java.net.URL.(URL.java:413)
at org.eclipse.ui.internal.intro.impl.swt.SharedStyleManager.load(SharedStyleManager.java:66)
at org.eclipse.ui.internal.intro.impl.swt.PageStyleManager.(PageStyleManager.java:66)
at org.eclipse.ui.internal.intro.impl.swt.PageFormWithNavigation.createPartControl(PageFormWithNavigation.java:63)
at org.eclipse.ui.internal.intro.impl.presentations.FormIntroPartImplementation.createMainPageBook(FormIntroPartImplementation.java:179)
at org.eclipse.ui.internal.intro.impl.presentations.FormIntroPartImplementation.dynamicCreatePartControl(FormIntroPartImplementation.java:137)
at org.eclipse.ui.internal.intro.impl.presentations.FormIntroPartImplementation.createPartControl(FormIntroPartImplementation.java:99)
at org.eclipse.ui.internal.intro.impl.model.IntroPartPresentation.createPartControl(IntroPartPresentation.java:268)
at org.eclipse.ui.intro.config.CustomizableIntroPart.createPartControl(CustomizableIntroPart.java:204)
at org.eclipse.ui.internal.ViewIntroAdapterPart.createPartControl(ViewIntroAdapterPart.java:98)
at org.eclipse.ui.internal.ViewReference.createPartHelper(ViewReference.java:367)
at org.eclipse.ui.internal.ViewReference.createPart(ViewReference.java:226)
at org.eclipse.ui.internal.WorkbenchPartReference.getPart(WorkbenchPartReference.java:595)
at org.eclipse.ui.internal.Perspective.showView(Perspective.java:2228)
at org.eclipse.ui.internal.WorkbenchPage.busyShowView(WorkbenchPage.java:1067)
at org.eclipse.ui.internal.WorkbenchPage\$20.run(WorkbenchPage.java:3816)
at org.eclipse.swt.custom.BusyIndicator.showWhile(BusyIndicator.java:70)
at org.eclipse.ui.internal.WorkbenchPage.showView(WorkbenchPage.java:3813)
at org.eclipse.ui.internal.WorkbenchPage.showView(WorkbenchPage.java:3789)
at org.eclipse.ui.internal.WorkbenchIntroManager.createIntro(WorkbenchIntroManager.java:173)
at org.eclipse.ui.internal.WorkbenchIntroManager.showIntro(WorkbenchIntroManager.java:120)
at org.eclipse.ui.application.WorkbenchWindowAdvisor.openIntro(WorkbenchWindowAdvisor.java:177)
at org.eclipse.ui.internal.ide.application.IDEWorkbenchWindowAdvisor.openIntro(IDEWorkbenchWindowAdvisor.java:467)
at org.eclipse.ui.internal.WorkbenchWindow.open(WorkbenchWindow.java:778)
at org.eclipse.ui.internal.Workbench\$22.runWithException(Workbench.java:1059)
at org.eclipse.ui.internal.StartupThreading\$StartupRunnable.run(StartupThreading.java:31)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:134)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:3468)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3115)
at org.eclipse.ui.application.WorkbenchAdvisor.openWindows(WorkbenchAdvisor.java:803)
at org.eclipse.ui.internal.Workbench\$28.runWithException(Workbench.java:1384)
at org.eclipse.ui.internal.StartupThreading\$StartupRunnable.run(StartupThreading.java:31)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:134)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:3468)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3115)
at org.eclipse.ui.internal.Workbench.runUI(Workbench.java:2316)
at org.eclipse.ui.internal.Workbench.access\$4(Workbench.java:2221)
at org.eclipse.ui.internal.Workbench\$5.run(Workbench.java:500)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:493)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:149)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:113)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:194)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:368)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:179)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
at java.lang.reflect.Method.invoke(Method.java:597)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:559)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:514)
at org.eclipse.equinox.launcher.Main.run(Main.java:1311)

!ENTRY org.eclipse.ui.intro 4 0 2013-02-14 17:11:32.779
!MESSAGE Could not load SWT style: css/root_swt.properties
!STACK 0
java.net.MalformedURLException: no protocol: css/root_swt.properties
at java.net.URL.(URL.java:567)
at java.net.URL.(URL.java:464)
at java.net.URL.(URL.java:413)
at org.eclipse.ui.internal.intro.impl.swt.SharedStyleManager.load(SharedStyleManager.java:66)
at org.eclipse.ui.internal.intro.impl.swt.PageStyleManager.(PageStyleManager.java:66)
at org.eclipse.ui.internal.intro.impl.presentations.FormIntroPartImplementation.createMainPageBook(FormIntroPartImplementation.java:191)
at org.eclipse.ui.internal.intro.impl.presentations.FormIntroPartImplementation.dynamicCreatePartControl(FormIntroPartImplementation.java:137)
at org.eclipse.ui.internal.intro.impl.presentations.FormIntroPartImplementation.createPartControl(FormIntroPartImplementation.java:99)
at org.eclipse.ui.internal.intro.impl.model.IntroPartPresentation.createPartControl(IntroPartPresentation.java:268)
at org.eclipse.ui.intro.config.CustomizableIntroPart.createPartControl(CustomizableIntroPart.java:204)
at org.eclipse.ui.internal.ViewIntroAdapterPart.createPartControl(ViewIntroAdapterPart.java:98)
at org.eclipse.ui.internal.ViewReference.createPartHelper(ViewReference.java:367)
at org.eclipse.ui.internal.ViewReference.createPart(ViewReference.java:226)
at org.eclipse.ui.internal.WorkbenchPartReference.getPart(WorkbenchPartReference.java:595)
at org.eclipse.ui.internal.Perspective.showView(Perspective.java:2228)
at org.eclipse.ui.internal.WorkbenchPage.busyShowView(WorkbenchPage.java:1067)
at org.eclipse.ui.internal.WorkbenchPage\$20.run(WorkbenchPage.java:3816)
at org.eclipse.swt.custom.BusyIndicator.showWhile(BusyIndicator.java:70)
at org.eclipse.ui.internal.WorkbenchPage.showView(WorkbenchPage.java:3813)
at org.eclipse.ui.internal.WorkbenchPage.showView(WorkbenchPage.java:3789)
at org.eclipse.ui.internal.WorkbenchIntroManager.createIntro(WorkbenchIntroManager.java:173)
at org.eclipse.ui.internal.WorkbenchIntroManager.showIntro(WorkbenchIntroManager.java:120)
at org.eclipse.ui.application.WorkbenchWindowAdvisor.openIntro(WorkbenchWindowAdvisor.java:177)
at org.eclipse.ui.internal.ide.application.IDEWorkbenchWindowAdvisor.openIntro(IDEWorkbenchWindowAdvisor.java:467)
at org.eclipse.ui.internal.WorkbenchWindow.open(WorkbenchWindow.java:778)
at org.eclipse.ui.internal.Workbench\$22.runWithException(Workbench.java:1059)
at org.eclipse.ui.internal.StartupThreading\$StartupRunnable.run(StartupThreading.java:31)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:134)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:3468)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3115)
at org.eclipse.ui.application.WorkbenchAdvisor.openWindows(WorkbenchAdvisor.java:803)
at org.eclipse.ui.internal.Workbench\$28.runWithException(Workbench.java:1384)
at org.eclipse.ui.internal.StartupThreading\$StartupRunnable.run(StartupThreading.java:31)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:134)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:3468)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3115)
at org.eclipse.ui.internal.Workbench.runUI(Workbench.java:2316)
at org.eclipse.ui.internal.Workbench.access\$4(Workbench.java:2221)
at org.eclipse.ui.internal.Workbench\$5.run(Workbench.java:500)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:493)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:149)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:113)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:194)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:368)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:179)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
at java.lang.reflect.Method.invoke(Method.java:597)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:559)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:514)
at org.eclipse.equinox.launcher.Main.run(Main.java:1311)

!ENTRY org.eclipse.jface 4 0 2013-02-14 17:14:53.346
!MESSAGE Unhandled event loop exception during blocked modal context.
!STACK 0
org.eclipse.swt.SWTException: Failed to execute runnable (java.lang.UnsatisfiedLinkError: /home/asztalos/MentorGraphics/xtUMLEditor/eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.core.linux.x86_3.6.4/os/linux/x86/libJetInitHeap.so: libstdc++.so.5: nem nyitható meg a megosztott objektumfájl: Nincs ilyen fájl vagy könyvtár)
at org.eclipse.swt.SWT.error(SWT.java:3884)
at org.eclipse.swt.SWT.error(SWT.java:3799)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:137)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:3468)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3115)
at org.eclipse.jface.operation.ModalContext\$ModalContextThread.block(ModalContext.java:173)
at org.eclipse.jface.operation.ModalContext.run(ModalContext.java:388)
at org.eclipse.jface.wizard.WizardDialog.run(WizardDialog.java:944)
at org.eclipse.ui.internal.wizards.datatransfer.WizardProjectsImportPage.createProjects(WizardProjectsImportPage.java:1258)
at org.eclipse.ui.wizards.datatransfer.ExternalProjectImportWizard.performFinish(ExternalProjectImportWizard.java:113)
at com.mentor.nucleus.bp.utilities.ui.ProjectUtilities\$3.run(ProjectUtilities.java:352)
at com.mentor.nucleus.bp.utilities.ui.ProjectUtilities\$4.run(ProjectUtilities.java:366)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:134)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:3468)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3115)
at org.eclipse.jface.window.Window.runEventLoop(Window.java:825)
at org.eclipse.jface.window.Window.open(Window.java:801)
at com.mentor.nucleus.bp.utilities.ui.ProjectUtilities.importExistingProject(ProjectUtilities.java:371)
at com.mentor.nucleus.bp.utilities.ui.ProjectUtilities.importExistingProject(ProjectUtilities.java:318)
at com.mentor.nucleus.bp.welcome.gettingstarted.SampleProjectGettingStartedAction.setupProject(SampleProjectGettingStartedAction.java:147)
at com.mentor.nucleus.bp.welcome.gettingstarted.SampleProjectGettingStartedAction.setup(SampleProjectGettingStartedAction.java:81)
at com.mentor.nucleus.bp.welcome.gettingstarted.SampleProjectGettingStartedAction.run(SampleProjectGettingStartedAction.java:75)
at org.eclipse.ui.internal.intro.impl.model.url.IntroURL.runAction(IntroURL.java:282)
at org.eclipse.ui.internal.intro.impl.model.url.IntroURL.doExecute(IntroURL.java:193)
at org.eclipse.ui.internal.intro.impl.model.url.IntroURL\$1.run(IntroURL.java:144)
at org.eclipse.swt.custom.BusyIndicator.showWhile(BusyIndicator.java:70)
at org.eclipse.ui.internal.intro.impl.model.url.IntroURL.execute(IntroURL.java:141)
at org.eclipse.ui.internal.intro.impl.swt.PageWidgetFactory\$1.linkActivated(PageWidgetFactory.java:63)
at org.eclipse.ui.forms.widgets.AbstractHyperlink.handleActivate(AbstractHyperlink.java:233)
at org.eclipse.ui.forms.widgets.AbstractHyperlink.handleMouseUp(AbstractHyperlink.java:327)
at org.eclipse.ui.forms.widgets.AbstractHyperlink.access\$2(AbstractHyperlink.java:311)
at org.eclipse.ui.forms.widgets.AbstractHyperlink\$4.handleEvent(AbstractHyperlink.java:125)
at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1176)
at org.eclipse.swt.widgets.Display.runDeferredEvents(Display.java:3493)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3112)
at org.eclipse.ui.internal.Workbench.runEventLoop(Workbench.java:2405)
at org.eclipse.ui.internal.Workbench.runUI(Workbench.java:2369)
at org.eclipse.ui.internal.Workbench.access\$4(Workbench.java:2221)
at org.eclipse.ui.internal.Workbench\$5.run(Workbench.java:500)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:493)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:149)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:113)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:194)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:368)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:179)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
at java.lang.reflect.Method.invoke(Method.java:597)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:559)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:514)
at org.eclipse.equinox.launcher.Main.run(Main.java:1311)
Caused by: java.lang.UnsatisfiedLinkError: /home/asztalos/MentorGraphics/xtUMLEditor/eclipse_extensions/BridgePoint/eclipse/plugins/com.mentor.nucleus.bp.core.linux.x86_3.6.4/os/linux/x86/libJetInitHeap.so: libstdc++.so.5: nem nyitható meg a megosztott objektumfájl: Nincs ilyen fájl vagy könyvtár
at java.lang.ClassLoader\$NativeLibrary.load(Native Method)
at java.lang.ClassLoader.loadLibrary0(ClassLoader.java:1778)
at java.lang.ClassLoader.loadLibrary(ClassLoader.java:1687)
at java.lang.Runtime.loadLibrary0(Runtime.java:823)
at java.lang.System.loadLibrary(System.java:1028)
at com.mentor.jeda.comps.JetInitHeap.(JetInitHeap.java:28)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.initConnection(BridgePointLicenseManager.java:120)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.getLicenseInternal(BridgePointLicenseManager.java:155)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.isEditorLicensed(BridgePointLicenseManager.java:305)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.isEditorLicensed(BridgePointLicenseManager.java:292)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.processStatement(ImportModelComponent.java:1517)
at com.mentor.nucleus.bp.io.core.SqlParser.insert_statement(SqlParser.java:134)
at com.mentor.nucleus.bp.io.core.SqlParser.sql_file(SqlParser.java:74)
at com.mentor.nucleus.bp.io.core.CoreImport.doLoadSql(CoreImport.java:262)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.run(ImportModelComponent.java:151)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:662)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:618)
at com.mentor.nucleus.bp.core.Package_c.PackageInstance(Package_c.java:2861)
at com.mentor.nucleus.bp.core.Package_c.PackageInstance(Package_c.java:2890)
at com.mentor.nucleus.bp.ui.canvas.Cl_c.Getinstancefromooa_id(Cl_c.java:496)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.finishComponentLoad(ImportModelComponent.java:575)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:671)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:618)
at com.mentor.nucleus.bp.core.common.PersistenceManager.ensureAllInstancesLoaded(PersistenceManager.java:754)
at com.mentor.nucleus.bp.core.SystemModel_c.SystemModelInstances(SystemModel_c.java:3242)
at com.mentor.nucleus.bp.core.SystemModel_c.SystemModelInstances(SystemModel_c.java:3268)
at com.mentor.nucleus.bp.ui.explorer.adapters.RootAdapter.getChildren(Unknown Source)
at com.mentor.nucleus.bp.ui.explorer.ModelContentProvider.getChildren(Unknown Source)
at com.mentor.nucleus.bp.ui.explorer.ModelContentProvider.getElements(Unknown Source)
at org.eclipse.jface.viewers.StructuredViewer.getRawChildren(StructuredViewer.java:959)
at org.eclipse.jface.viewers.ColumnViewer.getRawChildren(ColumnViewer.java:703)
at org.eclipse.jface.viewers.AbstractTreeViewer.getRawChildren(AbstractTreeViewer.java:1330)
at org.eclipse.jface.viewers.TreeViewer.getRawChildren(TreeViewer.java:390)
at org.eclipse.jface.viewers.AbstractTreeViewer.getFilteredChildren(AbstractTreeViewer.java:636)
at org.eclipse.jface.viewers.AbstractTreeViewer.getSortedChildren(AbstractTreeViewer.java:602)
at org.eclipse.jface.viewers.AbstractTreeViewer.updateChildren(AbstractTreeViewer.java:2578)
at org.eclipse.jface.viewers.AbstractTreeViewer.internalRefreshStruct(AbstractTreeViewer.java:1863)
at org.eclipse.jface.viewers.TreeViewer.internalRefreshStruct(TreeViewer.java:716)
at org.eclipse.jface.viewers.AbstractTreeViewer.internalRefresh(AbstractTreeViewer.java:1838)
at org.eclipse.jface.viewers.AbstractTreeViewer.internalRefresh(AbstractTreeViewer.java:1794)
at org.eclipse.jface.viewers.AbstractTreeViewer.internalRefresh(AbstractTreeViewer.java:1780)
at org.eclipse.jface.viewers.StructuredViewer\$7.run(StructuredViewer.java:1457)
at org.eclipse.jface.viewers.StructuredViewer.preservingSelection(StructuredViewer.java:1392)
at org.eclipse.jface.viewers.TreeViewer.preservingSelection(TreeViewer.java:402)
at org.eclipse.jface.viewers.StructuredViewer.preservingSelection(StructuredViewer.java:1353)
at org.eclipse.jface.viewers.StructuredViewer.refresh(StructuredViewer.java:1455)
at org.eclipse.jface.viewers.ColumnViewer.refresh(ColumnViewer.java:537)
at org.eclipse.jface.viewers.StructuredViewer.refresh(StructuredViewer.java:1414)
at com.mentor.nucleus.bp.core.util.UIUtil.refresh(UIUtil.java:179)
at com.mentor.nucleus.bp.core.util.UIUtil.access\$100(UIUtil.java:55)
at com.mentor.nucleus.bp.core.util.UIUtil\$2.run(UIUtil.java:157)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:134)
… 54 more

!ENTRY org.eclipse.ui 4 0 2013-02-14 17:14:53.570
!MESSAGE Unhandled event loop exception
!STACK 0
java.lang.NoClassDefFoundError: Could not initialize class com.mentor.jeda.comps.JetInitHeap
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.initConnection(BridgePointLicenseManager.java:120)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.testLicense(BridgePointLicenseManager.java:370)
at com.mentor.nucleus.bp.mc.mc3020.MCBuilderArgumentHandler.getLicenseString(MCBuilderArgumentHandler.java:214)
at com.mentor.nucleus.bp.mc.mc3020.MCBuilderArgumentHandler.setArguments(MCBuilderArgumentHandler.java:58)
at com.mentor.nucleus.bp.welcome.gettingstarted.SampleProjectGettingStartedAction.setupProject(SampleProjectGettingStartedAction.java:153)
at com.mentor.nucleus.bp.welcome.gettingstarted.SampleProjectGettingStartedAction.setup(SampleProjectGettingStartedAction.java:81)
at com.mentor.nucleus.bp.welcome.gettingstarted.SampleProjectGettingStartedAction.run(SampleProjectGettingStartedAction.java:75)
at org.eclipse.ui.internal.intro.impl.model.url.IntroURL.runAction(IntroURL.java:282)
at org.eclipse.ui.internal.intro.impl.model.url.IntroURL.doExecute(IntroURL.java:193)
at org.eclipse.ui.internal.intro.impl.model.url.IntroURL\$1.run(IntroURL.java:144)
at org.eclipse.swt.custom.BusyIndicator.showWhile(BusyIndicator.java:70)
at org.eclipse.ui.internal.intro.impl.model.url.IntroURL.execute(IntroURL.java:141)
at org.eclipse.ui.internal.intro.impl.swt.PageWidgetFactory\$1.linkActivated(PageWidgetFactory.java:63)
at org.eclipse.ui.forms.widgets.AbstractHyperlink.handleActivate(AbstractHyperlink.java:233)
at org.eclipse.ui.forms.widgets.AbstractHyperlink.handleMouseUp(AbstractHyperlink.java:327)
at org.eclipse.ui.forms.widgets.AbstractHyperlink.access\$2(AbstractHyperlink.java:311)
at org.eclipse.ui.forms.widgets.AbstractHyperlink\$4.handleEvent(AbstractHyperlink.java:125)
at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1176)
at org.eclipse.swt.widgets.Display.runDeferredEvents(Display.java:3493)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3112)
at org.eclipse.ui.internal.Workbench.runEventLoop(Workbench.java:2405)
at org.eclipse.ui.internal.Workbench.runUI(Workbench.java:2369)
at org.eclipse.ui.internal.Workbench.access\$4(Workbench.java:2221)
at org.eclipse.ui.internal.Workbench\$5.run(Workbench.java:500)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:493)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:149)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:113)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:194)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:368)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:179)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
at java.lang.reflect.Method.invoke(Method.java:597)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:559)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:514)
at org.eclipse.equinox.launcher.Main.run(Main.java:1311)

!ENTRY org.eclipse.cdt.core 1 0 2013-02-14 17:14:56.259
!MESSAGE Indexed ‘MicrowaveOven’ (13 sources, 108 headers) in 1,63 sec: 3 309 declarations; 7 717 references; 3 unresolved inclusions; 0 syntax errors; 13 unresolved names (0,12%)

!ENTRY org.eclipse.ui.workbench 4 2 2013-02-14 17:14:58.660
!MESSAGE Problems occurred when invoking code from plug-in: “org.eclipse.ui.workbench”.
!STACK 0
java.lang.NoClassDefFoundError: Could not initialize class com.mentor.jeda.comps.JetInitHeap
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.initConnection(BridgePointLicenseManager.java:120)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.getLicenseInternal(BridgePointLicenseManager.java:155)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.isEditorLicensed(BridgePointLicenseManager.java:305)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.isEditorLicensed(BridgePointLicenseManager.java:292)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.processStatement(ImportModelComponent.java:1517)
at com.mentor.nucleus.bp.io.core.SqlParser.insert_statement(SqlParser.java:134)
at com.mentor.nucleus.bp.io.core.SqlParser.sql_file(SqlParser.java:74)
at com.mentor.nucleus.bp.io.core.CoreImport.doLoadSql(CoreImport.java:262)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.run(ImportModelComponent.java:151)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:662)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:618)
at com.mentor.nucleus.bp.core.common.PersistenceManager.ensureAllInstancesLoaded(PersistenceManager.java:754)
at com.mentor.nucleus.bp.core.Package_c.getManyEP_PKGsOnR1405(Package_c.java:978)
at com.mentor.nucleus.bp.core.Package_c.getManyEP_PKGsOnR1405(Package_c.java:967)
at com.mentor.nucleus.bp.core.Package_c.getManyEP_PKGsOnR1405(Package_c.java:957)
at com.mentor.nucleus.bp.core.SystemModel_c.Collectreferencesforsynchronization(SystemModel_c.java:6039)
at com.mentor.nucleus.bp.ui.explorer.decorators.SynchronizationDecorator.childrenAreSynchronized(Unknown Source)
at com.mentor.nucleus.bp.ui.explorer.decorators.SynchronizationDecorator.isSynchronized(Unknown Source)
at com.mentor.nucleus.bp.ui.explorer.decorators.SynchronizationDecorator.decorate(Unknown Source)
at org.eclipse.ui.internal.decorators.LightweightDecoratorDefinition.decorate(LightweightDecoratorDefinition.java:269)
at org.eclipse.ui.internal.decorators.LightweightDecoratorManager\$LightweightRunnable.run(LightweightDecoratorManager.java:81)
at org.eclipse.core.runtime.SafeRunner.run(SafeRunner.java:42)
at org.eclipse.ui.internal.decorators.LightweightDecoratorManager.decorate(LightweightDecoratorManager.java:365)
at org.eclipse.ui.internal.decorators.LightweightDecoratorManager.getDecorations(LightweightDecoratorManager.java:347)
at org.eclipse.ui.internal.decorators.DecorationScheduler\$1.ensureResultCached(DecorationScheduler.java:371)
at org.eclipse.ui.internal.decorators.DecorationScheduler\$1.run(DecorationScheduler.java:331)
at org.eclipse.core.internal.jobs.Worker.run(Worker.java:55)

!ENTRY org.eclipse.ui 4 4 2013-02-14 17:14:58.675
!MESSAGE Exception in Decorator. The ‘BridgePoint Synchronization Decorator’ decorator will be disabled.

!ENTRY org.eclipse.ui 4 4 2013-02-14 17:14:58.675
!MESSAGE Could not initialize class com.mentor.jeda.comps.JetInitHeap
!STACK 0
java.lang.NoClassDefFoundError: Could not initialize class com.mentor.jeda.comps.JetInitHeap
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.initConnection(BridgePointLicenseManager.java:120)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.getLicenseInternal(BridgePointLicenseManager.java:155)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.isEditorLicensed(BridgePointLicenseManager.java:305)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.isEditorLicensed(BridgePointLicenseManager.java:292)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.processStatement(ImportModelComponent.java:1517)
at com.mentor.nucleus.bp.io.core.SqlParser.insert_statement(SqlParser.java:134)
at com.mentor.nucleus.bp.io.core.SqlParser.sql_file(SqlParser.java:74)
at com.mentor.nucleus.bp.io.core.CoreImport.doLoadSql(CoreImport.java:262)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.run(ImportModelComponent.java:151)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:662)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:618)
at com.mentor.nucleus.bp.core.common.PersistenceManager.ensureAllInstancesLoaded(PersistenceManager.java:754)
at com.mentor.nucleus.bp.core.Package_c.getManyEP_PKGsOnR1405(Package_c.java:978)
at com.mentor.nucleus.bp.core.Package_c.getManyEP_PKGsOnR1405(Package_c.java:967)
at com.mentor.nucleus.bp.core.Package_c.getManyEP_PKGsOnR1405(Package_c.java:957)
at com.mentor.nucleus.bp.core.SystemModel_c.Collectreferencesforsynchronization(SystemModel_c.java:6039)
at com.mentor.nucleus.bp.ui.explorer.decorators.SynchronizationDecorator.childrenAreSynchronized(Unknown Source)
at com.mentor.nucleus.bp.ui.explorer.decorators.SynchronizationDecorator.isSynchronized(Unknown Source)
at com.mentor.nucleus.bp.ui.explorer.decorators.SynchronizationDecorator.decorate(Unknown Source)
at org.eclipse.ui.internal.decorators.LightweightDecoratorDefinition.decorate(LightweightDecoratorDefinition.java:269)
at org.eclipse.ui.internal.decorators.LightweightDecoratorManager\$LightweightRunnable.run(LightweightDecoratorManager.java:81)
at org.eclipse.core.runtime.SafeRunner.run(SafeRunner.java:42)
at org.eclipse.ui.internal.decorators.LightweightDecoratorManager.decorate(LightweightDecoratorManager.java:365)
at org.eclipse.ui.internal.decorators.LightweightDecoratorManager.getDecorations(LightweightDecoratorManager.java:347)
at org.eclipse.ui.internal.decorators.DecorationScheduler\$1.ensureResultCached(DecorationScheduler.java:371)
at org.eclipse.ui.internal.decorators.DecorationScheduler\$1.run(DecorationScheduler.java:331)
at org.eclipse.core.internal.jobs.Worker.run(Worker.java:55)

!ENTRY org.eclipse.ui 4 0 2013-02-14 17:15:03.770
!MESSAGE Unhandled event loop exception
!STACK 0
java.lang.NoClassDefFoundError: Could not initialize class com.mentor.jeda.comps.JetInitHeap
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.initConnection(BridgePointLicenseManager.java:120)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.getLicenseInternal(BridgePointLicenseManager.java:155)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.isEditorLicensed(BridgePointLicenseManager.java:305)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.isEditorLicensed(BridgePointLicenseManager.java:292)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.processStatement(ImportModelComponent.java:1517)
at com.mentor.nucleus.bp.io.core.SqlParser.insert_statement(SqlParser.java:134)
at com.mentor.nucleus.bp.io.core.SqlParser.sql_file(SqlParser.java:74)
at com.mentor.nucleus.bp.io.core.CoreImport.doLoadSql(CoreImport.java:262)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.run(ImportModelComponent.java:151)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:662)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:618)
at com.mentor.nucleus.bp.core.common.PersistenceManager.ensureAllChildInstancesLoaded(PersistenceManager.java:822)
at com.mentor.nucleus.bp.core.common.PersistenceManager.ensureAllChildInstancesLoaded(PersistenceManager.java:809)
at com.mentor.nucleus.bp.core.Package_c.getManyEP_PKGsOnR1401(Package_c.java:721)
at com.mentor.nucleus.bp.core.Package_c.getManyEP_PKGsOnR1401(Package_c.java:710)
at com.mentor.nucleus.bp.core.Package_c.getManyEP_PKGsOnR1401(Package_c.java:700)
at com.mentor.nucleus.bp.ui.explorer.adapters.SystemAdapter.getChildren(Unknown Source)
at com.mentor.nucleus.bp.ui.explorer.ModelContentProvider.getChildren(Unknown Source)
at org.eclipse.jface.viewers.AbstractTreeViewer.getRawChildren(AbstractTreeViewer.java:1352)
at org.eclipse.jface.viewers.TreeViewer.getRawChildren(TreeViewer.java:390)
at org.eclipse.jface.viewers.AbstractTreeViewer.getFilteredChildren(AbstractTreeViewer.java:636)
at org.eclipse.jface.viewers.AbstractTreeViewer.getSortedChildren(AbstractTreeViewer.java:602)
at org.eclipse.jface.viewers.AbstractTreeViewer\$1.run(AbstractTreeViewer.java:799)
at org.eclipse.swt.custom.BusyIndicator.showWhile(BusyIndicator.java:70)
at org.eclipse.jface.viewers.AbstractTreeViewer.createChildren(AbstractTreeViewer.java:776)
at org.eclipse.jface.viewers.TreeViewer.createChildren(TreeViewer.java:639)
at org.eclipse.jface.viewers.AbstractTreeViewer.handleTreeExpand(AbstractTreeViewer.java:1442)
at org.eclipse.jface.viewers.TreeViewer.handleTreeExpand(TreeViewer.java:937)
at org.eclipse.jface.viewers.AbstractTreeViewer\$4.treeExpanded(AbstractTreeViewer.java:1453)
at org.eclipse.swt.widgets.TypedListener.handleEvent(TypedListener.java:126)
at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1176)
at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1200)
at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1185)
at org.eclipse.swt.widgets.Tree.gtk_test_expand_row(Tree.java:2062)
at org.eclipse.swt.widgets.Widget.windowProc(Widget.java:1601)
at org.eclipse.swt.widgets.Display.windowProc(Display.java:4197)
at org.eclipse.swt.internal.gtk.OS.\_gtk_main_do_event(Native Method)
at org.eclipse.swt.internal.gtk.OS.gtk_main_do_event(OS.java:7586)
at org.eclipse.swt.widgets.Display.eventProc(Display.java:1185)
at org.eclipse.swt.internal.gtk.OS.\_g_main_context_iteration(Native Method)
at org.eclipse.swt.internal.gtk.OS.g_main_context_iteration(OS.java:1858)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3110)
at org.eclipse.ui.internal.Workbench.runEventLoop(Workbench.java:2405)
at org.eclipse.ui.internal.Workbench.runUI(Workbench.java:2369)
at org.eclipse.ui.internal.Workbench.access\$4(Workbench.java:2221)
at org.eclipse.ui.internal.Workbench\$5.run(Workbench.java:500)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:493)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:149)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:113)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:194)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:368)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:179)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
at java.lang.reflect.Method.invoke(Method.java:597)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:559)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:514)
at org.eclipse.equinox.launcher.Main.run(Main.java:1311)

!ENTRY com.mentor.nucleus.bp.core 4 2 2013-02-14 17:16:23.198
!MESSAGE Problems occurred when invoking code from plug-in: “com.mentor.nucleus.bp.core”.
!STACK 0
java.lang.NoClassDefFoundError: Could not initialize class com.mentor.jeda.comps.JetInitHeap
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.initConnection(BridgePointLicenseManager.java:120)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.getLicenseInternal(BridgePointLicenseManager.java:155)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.isEditorLicensed(BridgePointLicenseManager.java:305)
at com.mentor.nucleus.bp.core.util.BridgePointLicenseManager.isEditorLicensed(BridgePointLicenseManager.java:292)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.processStatement(ImportModelComponent.java:1517)
at com.mentor.nucleus.bp.io.core.SqlParser.insert_statement(SqlParser.java:134)
at com.mentor.nucleus.bp.io.core.SqlParser.sql_file(SqlParser.java:74)
at com.mentor.nucleus.bp.io.core.CoreImport.doLoadSql(CoreImport.java:262)
at com.mentor.nucleus.bp.io.mdl.ImportModelComponent.run(ImportModelComponent.java:151)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:662)
at com.mentor.nucleus.bp.core.common.PersistableModelComponent.load(PersistableModelComponent.java:618)
at com.mentor.nucleus.bp.core.common.PersistenceManager.ensureAllChildInstancesLoaded(PersistenceManager.java:822)
at com.mentor.nucleus.bp.core.common.PersistenceManager.ensureAllChildInstancesLoaded(PersistenceManager.java:809)
at com.mentor.nucleus.bp.core.Package_c.getManyEP_PKGsOnR1401(Package_c.java:721)
at com.mentor.nucleus.bp.core.Package_c.getManyEP_PKGsOnR1401(Package_c.java:710)
at com.mentor.nucleus.bp.core.Package_c.getManyEP_PKGsOnR1401(Package_c.java:700)
at com.mentor.nucleus.bp.ui.properties.SystemS_SYSPropertySource.getPropertyDescriptors(SystemS_SYSPropertySource.java:146)
at org.eclipse.ui.views.properties.PropertySheetEntry.computeMergedPropertyDescriptors(PropertySheetEntry.java:167)
at org.eclipse.ui.views.properties.PropertySheetEntry.refreshChildEntries(PropertySheetEntry.java:530)
at org.eclipse.ui.views.properties.PropertySheetEntry.setValues(PropertySheetEntry.java:760)
at org.eclipse.ui.views.properties.PropertySheetViewer.setInput(PropertySheetViewer.java:973)
at org.eclipse.ui.views.properties.PropertySheetPage.selectionChanged(PropertySheetPage.java:510)
at org.eclipse.ui.views.properties.PropertySheet.selectionChanged(PropertySheet.java:344)
at org.eclipse.ui.internal.AbstractSelectionService.fireSelection(AbstractSelectionService.java:156)
at org.eclipse.ui.internal.AbstractSelectionService\$1.selectionChanged(AbstractSelectionService.java:62)
at com.mentor.nucleus.bp.core.ui.Selection\$2.run(Selection.java:226)
at org.eclipse.core.runtime.SafeRunner.run(SafeRunner.java:42)
at org.eclipse.core.runtime.Platform.run(Platform.java:888)
at com.mentor.nucleus.bp.core.ui.Selection.fireSelectionChanged(Selection.java:223)
at com.mentor.nucleus.bp.core.ui.Selection.setSelection(Selection.java:169)
at com.mentor.nucleus.bp.core.ui.Selection.setSelection(Selection.java:155)
at com.mentor.nucleus.bp.ui.explorer.ExplorerView\$3.selectionChanged(Unknown Source)
at org.eclipse.jface.viewers.Viewer\$2.run(Viewer.java:162)
at org.eclipse.core.runtime.SafeRunner.run(SafeRunner.java:42)
at org.eclipse.core.runtime.Platform.run(Platform.java:888)
at org.eclipse.ui.internal.JFaceUtil\$1.run(JFaceUtil.java:48)
at org.eclipse.jface.util.SafeRunnable.run(SafeRunnable.java:175)
at org.eclipse.jface.viewers.Viewer.fireSelectionChanged(Viewer.java:160)
at org.eclipse.jface.viewers.StructuredViewer.updateSelection(StructuredViewer.java:2132)
at org.eclipse.jface.viewers.StructuredViewer.handleSelect(StructuredViewer.java:1160)
at org.eclipse.jface.viewers.StructuredViewer\$4.widgetSelected(StructuredViewer.java:1190)
at org.eclipse.jface.util.OpenStrategy.fireSelectionEvent(OpenStrategy.java:228)
at org.eclipse.jface.util.OpenStrategy.access\$4(OpenStrategy.java:222)
at org.eclipse.jface.util.OpenStrategy\$1.handleEvent(OpenStrategy.java:389)
at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1176)
at org.eclipse.swt.widgets.Display.runDeferredEvents(Display.java:3493)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3112)
at org.eclipse.ui.internal.Workbench.runEventLoop(Workbench.java:2405)
at org.eclipse.ui.internal.Workbench.runUI(Workbench.java:2369)
at org.eclipse.ui.internal.Workbench.access\$4(Workbench.java:2221)
at org.eclipse.ui.internal.Workbench\$5.run(Workbench.java:500)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:493)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:149)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:113)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:194)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:368)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:179)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25)
at java.lang.reflect.Method.invoke(Method.java:597)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:559)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:514)
at org.eclipse.equinox.launcher.Main.run(Main.java:1311)

---

**Domonkos Asztalos** · February 14, 2013 at 10:43 pm

OpenJDK 6

---

**Lee Riemenschneider** · February 15, 2013 at 3:33 am

Domonkos,

I couldn’t repeat your errors on Ubuntu 12.10 64-bit. I tried both OpenJDK 6 & 7.

---

**keithbrown** · February 15, 2013 at 2:51 pm

Domonkos,

I am not duplicating the problem on an Ubuntu 11 (64-bit) installation. I will note that I did install the 32-bit compatibility libs with the command ‘sudo apt-get install ia32-libs’. I also have changed the /bin/sh symlink to point at bash instead of dash. After those changes, I ran the install under my user account and installed under my home directory (just to make sure I didn’t run into any write permissions issues).

Once installed, I start xtUML Editor. Choose Quick Start and created MicrowaveOven. It does pop up a “Can’t get code generation license” at this point, but that is not fatal. The project is created anyway. Then went through the same steps to create GPS Watch. I am able to browse both models.

I will point out that xtUML Editor includes and uses its own JVM (Oracle’s). It specifies to use this in the /eclipse/BridgePoint_Launcher.sh script. Are you using this script to start xtUML Editor?

---

**Lee Riemenschneider** · February 15, 2013 at 2:57 pm

One thing I noticed last night was that I installed without the dash to bash sh link change, so it might not be necessary on later versions (mine is 12.10) of Ubuntu.

- This reply was modified 13 years ago by [![](https://secure.gravatar.com/avatar/2beeed50ad01495a2bb8456ccfd23100a3ae303e29fc1a90ee450c7cf5e79641?s=14&amp;d=mm&amp;r=g)Lee Riemenschneider]({{ '/user/lwriemen/' | relative_url }}).

---

**Lee Riemenschneider** · February 15, 2013 at 3:02 pm

Domonkos,
Did you use the install with Eclipse or use your existing Eclipse?

---

**Domonkos Asztalos** · February 23, 2013 at 11:19 am

SOLVED:

in Ubuntu 12.10 and some earlier versions the package stdlibc++6 is installed, but the xtUMLEditor needs the stdlibc++5 package.
Having installed it:

sudo apt-get install libstdc++5

I can use the Editor.
