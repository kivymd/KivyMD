KivyMD [v0.102.1 - *Alpha*](https://github.com/HeaTTheatR/KivyMD/blob/master/CHANGELOG.md)
======

<img align="left" width="256" src="https://github.com/HeaTTheatR/KivyMD/raw/master/kivymd/images/kivy-logo-white-512.png"/>

KivyMD is a collection of Material Design compliant widgets for use with [Kivy](http://kivy.org), a framework for cross-platform, touch-enabled graphical applications.

The project's goal is to approximate Google's [Material Design spec](https://material.io/design/introduction/) as close as possible without sacrificing ease of use or application performance.

This library is a fork of the [KivyMD project](https://gitlab.com/kivymd/KivyMD) the author of which stopped supporting this project three years ago. We found the strength and brought this project to a new level.

Currently we're in **alpha** status, so things are changing all the time and we cannot promise any kind of API stability. However it is safe to vendor now and make use of what's currently available.

Join the project! Just fork the project, branch out and submit a pull request when your patch is ready. If any changes are necessary, we'll guide you through the steps that need to be done via PR comments or access to your for may be requested to outright submit them.

If you wish to become a project developer (permission to create branches on the project without forking for easier collaboration), have at least one PR approved and ask for it. If you contribute regularly to the project the role may be offered to you without asking too.

[![Latest version on PyPI](https://img.shields.io/pypi/v/kivymd.svg)](https://pypi.org/project/kivymd)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/kivymd.svg)](#Installation)
[![Downloads](https://pepy.tech/badge/kivymd)](https://pepy.tech/project/kivymd)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Build status](https://travis-ci.org/HeaTTheatR/KivyMD.svg?branch=master)](https://travis-ci.org/HeaTTheatR/KivyMD)
[![Discord server](https://img.shields.io/discord/566880874789076992?logo=discord)](https://discord.gg/wu3qBST)

Documentation
=============

#### Wiki

No complete documentation yet. Our [Wiki](https://github.com/HeaTTheatR/KivyMD/wiki) contains some examples of using KivyMD widgets.

#### Demos

<p align="center">
  <a href="https://www.youtube.com/watch?v=qU6C_Icp6TM">
    <img width="400" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/prevideo-run-in-desktop.png" title='Click to watch "How to run the KivyMD demo on desktop?" on YouTube'>
  </a>
</p>

[Kitchen sink](https://github.com/HeaTTheatR/KivyMD/tree/master/demos/kitchen_sink) app demonstrates every KivyMD widget. You can see how to use widget in code of app. You can download apk for your smartphone (Android 6.0 and higher):  [kitchen_sink-0.98.4-x86.apk](https://github.com/HeaTTheatR/KivyMD-data/tree/master/bin/x86) or [kitchen_sink-0.98.4-armeabi-v7a.apk](https://github.com/HeaTTheatR/KivyMD-data/tree/master/bin/armeabi-v7a).

[Another demo applications](https://github.com/HeaTTheatR/KivyMD/tree/master/demos/kitchen_sink/demo_apps) contain some useful GUI examples.

#### Tutorials on YouTube

<p align="center">
  <a href="https://www.youtube.com/watch?v=kRWtSkIYPFI&list=PLy5hjmUzdc0nMkzhphsqgPCX62NFhkell&index=1">
    <img width="400" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/tutorial.png" title="Click to watch KivyMD Tutorials on YouTube">
  </a>
</p>

[Tutorials](https://www.youtube.com/watch?v=kRWtSkIYPFI&list=PLy5hjmUzdc0nMkzhphsqgPCX62NFhkell&index=1) by [Erik Sandberg](https://github.com/Dirk-Sandberg) show you how to create application with KivyMD and use its widgets.


Support
=======

If you need assistance or you have a question, you can ask for help on our mailing list:

* **Discord server (priority):** https://discord.gg/wu3qBST (English #support, Russian #ru-support)
* VK group: https://vk.com/kivy_development (Russian)
* Google group: https://groups.google.com/forum/#!categories/kivymd-users-support (English)
* Email: kivydevelopment@gmail.com


Installation
============

#### Dependencies:

* [Kivy](https://github.com/kivy/kivy) >= 1.10.1 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
* [PIL](https://github.com/python-pillow/Pillow) ([Installation](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation))
* [Python 3.6+](https://www.python.org/) *(Python 2 not supported)*

#### How to install

You can install latest release version of KivyMD from [PyPI](https://pypi.org/project/kivymd):
```bash
python3 -m pip install kivymd
```
If you want to install development version from [master](https://github.com/HeaTTheatR/KivyMD/tree/master/) branch, you should specify git HTTPS address:
```bash
# Master branch:
python3 -m pip install git+https://github.com/HeaTTheatR/KivyMD.git
# Specific branch:
python3 -m pip install git+https://github.com/HeaTTheatR/KivyMD.git@stable
# Specific tag:
python3 -m pip install git+https://github.com/HeaTTheatR/KivyMD.git@0.100.2
# Specific commit:
python3 -m pip install git+https://github.com/HeaTTheatR/KivyMD.git@f80d9c8b812d54a724db7eda30c4211d0ba764c2

# If you already has installed KivyMD
python3 -m pip install --force-reinstall git+https://github.com/HeaTTheatR/KivyMD.git
```
Also you can install manually from sources. Just clone the project and run the setup.py script:
```bash
python3 ./setup.py install
```

#### How to use with [Buildozer](https://github.com/kivy/buildozer)

```text
requirements = kivy==1.11.1, kivymd
```
This will download latest release version from PyPI. If you want to use master branch, you should write the full git HTTPS address, like this example:
```text
# Master branch:
requirements = kivy==1.11.1, git+https://github.com/HeaTTheatR/KivyMD.git
# Specific branch:
requirements = kivy==1.11.1, git+https://github.com/HeaTTheatR/KivyMD.git@master
# Specific tag:
requirements = kivy==1.11.1, git+https://github.com/HeaTTheatR/KivyMD.git@0.100.2
# Specific commit:
requirements = kivy==1.11.1, git+https://github.com/HeaTTheatR/KivyMD.git@f80d9c8b812d54a724db7eda30c4211d0ba764c2
```
Do not forget to remove `buildozer` directory before building if version was updated (Buildozer doesn't update already downloaded packages).


Building with VM
================

<a href="https://xubuntu.org/release/18-04/">
  <img align="left" width="300" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/XUBUNTU.png" title="Click to download XUbuntu 18.04">
</a>

Packages for Android are built according to the following instructions:
* Download [XUbuntu 18.04](https://xubuntu.org/release/18-04/)
* Create a new virtual machine based on the downloaded image of XUbuntu
* Start the XUbuntu virtual machine, download [this bash script](https://github.com/HeaTTheatR/KivyMD-data/blob/master/install-kivy-buildozer-dependencies.sh), add execution permissions and run script:
```bash
wget https://github.com/HeaTTheatR/KivyMD-data/raw/master/install-kivy-buildozer-dependencies.sh
chmod +x install-kivy-buildozer-dependencies.sh

./install-kivy-buildozer-dependencies.sh
```
* Script will install all the necessary libraries and tools for creating packages for Android
* Done! Now you have a virtual machine for building Kivy application packages!

> Or see the instructions [here](https://github.com/zaemiel/kivy-buildozer-installer).

Settings
========

#### [Syntax highlighting and auto-completion for Kivy/KivyMD .kv files in PyCharm/Intellij IDEA](https://github.com/noembryo/KV4Jetbrains)




API Breaking changes
====================

* App object should be inherited from `kivymd.app.MDApp`. See wiki for example
and more information:
[Material App on KivyMD wiki](https://github.com/HeaTTheatR/KivyMD/wiki/Modules-Material-App).
* All classes with the Behavior prefix moved to `kivymd.uix.behaviors` module.
* All uix modules moved to `kivymd.uix` module.
* All widgets that usually used in kv-lang are automatically added to Factory.
You don't need to `#:import` them. Remove all your imports from kv files.
* Replaced `MDAccordion` and `MDAccordionListItem` with `MDExpansionPanel`.
* Changed font styles:

| Old      | New       |
|----------|-----------|
| Icon     | Icon      |
| -        | Overline  |
| -        | Subtitle2 |
| Subhead  | Subtitle1 |
| Title    | H6        |
| Headline | H5        |
| Display1 | H4        |
| Display2 | H3        |
| Display3 | H2        |
| Display4 | H1        |

* Colors `BlueGrey` and `Grey` renamed to `BlueGray` and `Gray`

Video preview
=============

<p align="center">
  <a href="https://www.youtube.com/watch?v=oOTdQ-FHeSw">
    <img src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/prevideo.png" title='Click to watch video on YouTube'>
  </a>
</p>


Image preview
=============

<p align="center">
  <img src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/previous.png">
</p>


Contributing
============

We always welcome your [Bug reports](https://github.com/HeaTTheatR/KivyMD/issues/new?template=bug_report.md),
[Feature requests](https://github.com/HeaTTheatR/KivyMD/issues/new?template=feature_request.md)
and [Pull requests](https://github.com/HeaTTheatR/KivyMD/pulls)!
Check out [CONTRIBUTING.md](https://github.com/HeaTTheatR/KivyMD/blob/master/.github/CONTRIBUTING.md)
and feel free to improve KivyMD.


Sister projects
===============

* [Creator Kivy Project](https://github.com/HeaTTheatR/CreatorKivyProject) - Wizard for creating a new project for applications written using the Kivy framework


License
=======

KivyMD is released under the terms of the [MIT License](https://github.com/HeaTTheatR/KivyMD/blob/master/LICENSE), same as [Kivy](https://github.com/kivy/kivy/blob/master/LICENSE).

[Roboto font](https://fonts.google.com/specimen/Roboto) is licensed and distributed under the terms of the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

[Iconic font](https://github.com/Templarian/MaterialDesign-Webfont) by the [Material Design Icons](https://materialdesignicons.com/) community covered by [SIL Open Font License 1.1](http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web)
