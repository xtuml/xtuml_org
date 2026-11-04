---
redirect_from:
  - "/community/topic/how-to-read-model-from-eclipse-builder/"

layout: "topic"
title: "How to read model from Eclipse builder?"
date: "2014-04-29"
permalink: "/forums/topic/how-to-read-model-from-eclipse-builder/"
forum: "BridgePoint/xtUML Usage and Training"
forum_slug: "xtuml-forum"
forum_url: "/forums/xtuml-forum/"
---

**sfinnie** · April 29, 2014 at 7:25 am

I’m trying to read a model from an eclipse builder – but not getting anything returned. Am using the API docs as posted on [this thread]({{ '/forums/topic/model-extraction-from-xtuml-editor/' | relative_url }}) (thanks Campbell). Is there something I need to do to initialise/access the model first? Builder code as follows:

\[code\]
protected IProject\[\] build(int kind, Map args, IProgressMonitor monitor)
throws CoreException {
MessageConsole console = getMessageConsole();
MessageConsoleStream out = console.newMessageStream();

out.println(“Builder called for project ” + getProject().getName());
//try approach from LoadAndPersistaction.java
ArrayList fElements = new ArrayList();
Iterator iter = fElements.iterator();
while (iter.hasNext()) {
NonRootModelElement nrme = iter.next();
out.println(“\tNon-root model element: ” + nrme.Get_name());
}

//try the API directly
Package_c start = null;

PackageableElement_c\[\] pes = PackageableElement_c.getManyPE_PEsOnR8000(start);
for(PackageableElement_c p:pes) {
out.println(“\tProcessing PackageableElement ” + p.Get_name());
}
out.println(“Builder completed for project ” + getProject().getName());
return null;
}

\[/code\]

The builder is being called OK – start & finish messages are being logged. However, neither approach to reading model contents yields any results.

So: given I have the project instance, is there something else I need to do before accessing the model contents?

Thanks,
Scott.

---

**Travis London** · April 30, 2014 at 4:21 pm

To get all the root packages you need to use association R1401:

Package_c\[\] pkgs = Package_c.getManyEP_PKGsOnR1401(system);

To get a system you can do this:

SystemModel_c system = SystemModel_c.SystemModelInstance(Ooaofooa.getDefaultInstance(), new ClassQueryInterface_c() {

@Override
public boolean evaluate(Object candidate) {
return ((SystemModel_c) candidate).getName().equals(projectName);
}
});

Then you can get the root packages from that system.

To get nested packages you do this:

Package_c\[\] childPkgs = Package_c.getManyEP_PKGsOnR8000(PackageableElement_c.getManyPE_PEsOnR8000(pkg));

---

**sfinnie** · May 1, 2014 at 9:20 pm

Hi Travis, thanks for the response. I can now get to the Packages for the system; however trying to print the name of each results in an empty string (they are named in the model). I’m obviously missing something – but not sure what?

Builder code now as follows:

\[code title=””\] protected IProject\[\] build(int kind, Map args, IProgressMonitor monitor)
throws CoreException {
MessageConsoleStream out = getConsole();

out.println(“Builder called for project ” + getProject().getName());
SystemModel_c sysmdl = getSystemModel(getProject());
if (sysmdl == null) {
out.println(“System model is null”);
} else {
out.println(“System model name: ‘” + sysmdl.Get_name() + “‘”);
for (Package_c pkg: getModelPackages(sysmdl)) {
out.println(“\tPackage name: ‘” + pkg.Get_name() + “‘”);
}
}

out.println(“Builder completed for project ” + getProject().getName());
return null;
}

SystemModel_c getSystemModel(IProject project) {
final String projectName = project.getName();
getConsole().println(“Is Ooa \_full\_ model loaded? ” + Ooaofooa.getDefaultInstance().isFullModelLoaded());
SystemModel_c sysmdl = SystemModel_c.SystemModelInstance(Ooaofooa.getDefaultInstance(), new ClassQueryInterface_c() {
@Override
public boolean evaluate(Object candidate) {
return ((SystemModel_c) candidate).getName().equals(projectName);
}
});
if (sysmdl == null) {
getConsole().println(“System Model is null”);
}
return sysmdl;
}

Package_c\[\] getModelPackages(SystemModel_c sysmdl) {
Package_c\[\] pkgs = Package_c.getManyEP_PKGsOnR1401(sysmdl);
if (pkgs == null) {
getConsole().println(“Package list is null”);
} else {
getConsole().println(“System contains ” + pkgs.length + ” packages”);
}
return pkgs;
}
\[/code\]

which produces the following output:

\[code\]
Builder called for project GO
Is Ooa \_full\_ model loaded? true
System model name: ”
System contains 4 packages
Package name: ”
Package name: ”
Package name: ”
Package name: ”
Builder completed for project GO
\[/code\]

Is it anything to do with the ‘model loaded’ flags? I notice that isModelLoaded() returns ‘false’even when isFullModelLoaded() returns true. If so is there any way to force model load from the builder?

Thanks,
Scott.

---

**sfinnie** · May 1, 2014 at 9:31 pm

Answering my own question: I should have used ‘getName()’ not ‘Get_Name()’. Works now. (Although a bit confused by why both methods exist?).

And still interested to know if there’s a way to ensure the model is loaded as the first step of running the builder. I’m currently opening model diagrams in the editor before running builder; if I don’t then the model objects return null.

Thanks.

---

**Travis London** · May 2, 2014 at 1:13 pm

Some elements do not have a Name attribute. In these cases the views expect a get_name operation to be present. The NonRootModelElement class is a supertype to all model elements. The getName() pattern is for convenience only, the metamodel should be referenced for proper name access.

\[code title=”getName”\] /\*\*
\* This method will be implemented by the subtype. If not it will call
\* the Get_name method that will also be implemented by the subtype
\* returning an empty string if neither method was implemented.
\*/
public String getName() {
return Get_name();
}
public String Get_name() {
return “”;
}
\[/code\]

Regarding model load it should occur for you. The BridgePoint tool supports lazy loading. I suspect you are missing one key call. PersistenceManager.getDefaultInstance(); This will initialize the loading infrastructure and allow for lazy loading to occur. Let me know if this solves the issue for you.

---

**sfinnie** · May 6, 2014 at 8:58 am

Thanks for the explanation Travis. And calling ‘PersistenceManager.getDefaultInstance()’ does seem to be the missing link for model load; working fine now.

---

**BrotherHok** · July 22, 2014 at 5:02 am

Hello .
Shikarnenko here. I liked it!
Keep up the good work! :)
