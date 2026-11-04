---
layout: "page"
title: "Release Notes – BridgePoint 5.0"
permalink: "/release-notes-bridgepoint-5-0/"
---

# BridgePoint xtUML Release Notes

Release 5.0

## 1. License

BridgePoint is licensed under the [Apache 2.0 License Agreement](http://www.apache.org/licenses/LICENSE-2.0).

## 2. System Requirements

|                           |                                      |
|---------------------------|--------------------------------------|
| Operating System          | Windows 7, Windows 8, Linux variants |
| \*Eclipse                 | Version 3.7.2                        |
| \*Java Virtual Machine    | Version 1.6 or later                 |
| \*(supplied by installer) |                                      |

 

## 3. General Notes

- A summary of the release highlights and new functionality is available on the [What’s New]({{ '/whats-new-bridgepoint-5-0/' | relative_url }}) page.
- **IMPORTANT:** BridgePoint 5.0 is a completely open source version of the software. Please see [xtUML.org]({{ '/' | relative_url }}) and [onefact.net](http://onefact.net/) for ongoing development and support of BridgePoint.
- BridgePoint is simplified to ship as a zip file similar to standard eclipse packages. Users who wish to create desktop shortcuts to start BridgePoint should set the shortcut to start in \<install dir\>/eclipse/

## 4. Interoperability with Previous Releases

- BridgePoint 5.0 is compatible with workspaces and projects created with BridgePoint 4.2.
- When opening workspaces created with previous versions, the xtUML Modeling perspective will not show properly the first time. Close and re-open this perspective.
- Any existing projects that reference core.jar must be modified to point at the file in its new home under \<install dir\>/eclipse/plugins/org.xtuml.bp.core_5.0.x/core.jar

## 5. Issues and Feature Requests

The BridgePoint support system is hosted at [support.onefact.net](https://support.onefact.net/). Please check here for known issues and to submit bug reports and requests for new features.

## 6. Closed Issues

The full [“v5.0 – Closed Issues”](https://support.onefact.net/redmine/issues?query_id=15) list is available in the One Fact Support system.
