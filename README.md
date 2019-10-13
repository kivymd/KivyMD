KivyMD
======

<img align="left" height="256" src="https://github.com/HeaTTheatR/KivyMD/raw/master/kivymd/images/kivy-logo-white-512.png"/>

KivyMD is a collection of Material Design compliant widgets for use with [Kivy](http://kivy.org), a framework for cross-platform, touch-enabled graphical applications.

The project's goal is to approximate Google's [Material Design spec](https://www.google.com/design/spec/material-design/introduction.html) as close as possible without sacrificing ease of use or application performance.

This library is a fork of the [KivyMD project](https://gitlab.com/kivymd/KivyMD) the author of which stopped supporting this project three years ago. We found the strength and brought this project to a new level.

Currently we're in **alpha** status, so things are changing all the time and we cannot promise any kind of API stability. However it is safe to vendor now and make use of what's currently available.

Join the project! Just fork the project, branch out and submit a pull request when your patch is ready. If any changes are necessary, we'll guide you through the steps that need to be done via PR comments or access to your for may be requested to outright submit them.

If you wish to become a project developer (permission to create branches on the project without forking for easier collaboration), have at least one PR approved and ask for it. If you contribute regularly to the project the role may be offered to you without asking too.

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI version](https://badge.fury.io/py/kivymd.svg)](https://badge.fury.io/py/kivymd)


Documentation
=============

Full documentation yet. Some examples of using KivyMD widgets can be found in our [Wiki](https://github.com/HeaTTheatR/KivyMD/wiki) and in the code of the [demo applications](https://github.com/HeaTTheatR/KivyMD/tree/master/demos/kitchen_sink/demo_apps)


KivyMD Tutorials
================
[Tutorials](https://www.youtube.com/watch?v=kRWtSkIYPFI&list=PLy5hjmUzdc0nMkzhphsqgPCX62NFhkell&index=1)


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

* Kivy >= 1.10.1
* PIL
* Python 3 *(Python 2 not supported)*

#### How to install

To install KivyMD, clone the project and run the setup.py script. The following line works on Linux and Mac OS, other OSes not tested:
  ```bash
  sudo python ./setup.py install
  ```
  or
  ```bash
  sudo pip3 install kivymd
  ```
#### How to use with Buildozer

If you want to use KivyMD with buildozer, in your buildozer.spec's requirements line you should add the full git HTTPS address, like this example:
  ```text
  requirements = kivy==master, kivymd
  ```


Running on Android
==================

Android 6.0 and higher [kitchen_sink-0.98.4-x86.apk](https://github.com/HeaTTheatR/KivyMD-data/tree/master/bin/x86) or [kitchen_sink-0.98.4-armeabi-v7a.apk](https://github.com/HeaTTheatR/KivyMD-data/tree/master/bin/armeabi-v7a)


Building
========

<a href="https://xubuntu.org/release/18-04/">
  <img align="left" height="140" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/XUBUNTU.png">
</a>

Packages for Android are built according to the following instructions:
* Download [XUbuntu 18.04](https://xubuntu.org/release/18-04/)
* Create a new virtual machine based on the downloaded image of XUbuntu
* Start the XUbuntu virtual machine, open the browser and download [this bash script](https://github.com/HeaTTheatR/KivyMD-data/blob/master/install-kivy-buildozer-dependencies.sh):

  Add execution permissions:
  ```bash
  chmod +x install-kivy-buildozer-dependencies.sh
  ```
  ...and run script:
  ```bash
  ./install-kivy-buildozer-dependencies.sh
  ```

* Run the script - it will install all the necessary libraries and tools for creating packages for Android
* Done! Now you have a virtual machine for building Kivy application packages!

Or see the instructions [here](https://github.com/zaemiel/kivy-buildozer-installer).


What's new in version 0.101.5:
============================

[CHANGELOG.md](CHANGELOG.md)


API Breaking changes:
=====================

* All classes with the `Behavior` prefix are now placed in the `kivymd/behaviors` directory
* All uix modules moved to kivymd.uix module.
* All widgets that usually used in kv-lang are automatically added to Factory.
You don't need to #:import them. Remove all your imports.
* Changed font styles:

| Old      | New       |
|----------|-----------|
| Icon     | Icon      |
| -        | Overline  |
| Caption  | Caption   |
| Button   | Button    |
| Body2    | Body2     |
| Body1    | Body1     |
| -        | Subtitle2 |
| Subhead  | Subtitle1 |
| Title    | H6        |
| Headline | H5        |
| Display1 | H4        |
| Display2 | H3        |
| Display3 | H2        |
| Display4 | H1        |

* Colors `BlueGrey` and `Grey` renamed to `BlueGray` and `Gray` (for better fit MD spec)


Video previous
==============

<p align="center">
  <a href="https://www.youtube.com/watch?v=oOTdQ-FHeSw">
    <img src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/prevideo.png">
  </a>
</p>


Image previous
==============

<p align="center">
  <img src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/previous.png">
</p>


Sister project:
==============

[Creator Kivy Project](https://github.com/HeaTTheatR/CreatorKivyProject) - Wizard for creating a new project for applications written using the Kivy framework


License
=======

[MIT License](LICENSE), same as Kivy.

Roboto font is licensed and distributed under the terms of the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Icons by the [Material Design Icons](https://materialdesignicons.com/) community covered by [SIL Open Font License 1.1](http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web)
