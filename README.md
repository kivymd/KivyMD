KivyMD
======

<img align="left" height="256" src="https://raw.githubusercontent.com/kivymd/KivyMD/master/assets/kivymd_logo.png"/>

KivyMD is a collection of Material Design compliant widgets for use with [Kivy](http://kivy.org), a framework for cross-platform, touch-enabled graphical applications.

The project's goal is to approximate Google's [Material Design spec](https://www.google.com/design/spec/material-design/introduction.html) as close as possible without sacrificing ease of use or application performance.

Currently we're in **alpha** status, so things are changing all the time and we cannot promise any kind of API stability. However it is safe to vendor now and make use of what's currently available; giving you freedom to upgrade when you're ready to do the necessary refactoring.

Roadmap is available on [the project's wiki](https://gitlab.com/kivymd/KivyMD/wikis/Roadmap).

If you wish to contribute, [the project's coding style](https://gitlab.com/kivymd/KivyMD/wikis/Coding-style) is available there as well. Just fork the project, branch out and submit a pull request when your patch is ready. If any changes are necessary, we'll guide you through the steps that need to be done via PR comments or access to your for may be requested to outright submit them.

If you wish to become a project developer (permission to create branches on the project without forking for easier collaboration), have at least one PR approved and ask for it. If you contribute regularly to the project the role may be offered to you without asking too.

Documentation
=============

Some very early documentation can be found at our project's website, other than that we recommend checking the [demos/kitchen_sink/main.py](https://gitlab.com/kivymd/KivyMD/blob/master/demos/kitchen_sink/main.py) file for examples.

Installation and use with Buildozer
===================================

#### Dependencies:
* Kivy 1.9.2-dev0 or Kivy 1.9.2 (When released)

#### How to install

To install KivyMD, clone the project and run the setup.py script. The following line works on Linux, other OSes not tested:

    sudo python ./setup.py install

Replace "python" with the Python interpreter you want to install KivyMD on (Python 3 is supported)


#### How to use with Buildozer

If you want to use KivyMD with buildozer, in your buildozer.spec's requirements line you should add the full git HTTPS address, like this example:

    requirements = kivy==master,git+https://gitlab.com/kivymd/KivyMD.git

License
=======

MIT, same as Kivy.

[Material Design Iconic Font](https://github.com/zavoloklom/material-design-iconic-font) by [Sergey Kupletsky](https://twitter.com/zavoloklom) covered by the licenses described at https://zavoloklom.github.io/material-design-iconic-font/license.html.

Icons by the materialdesignicons.com community covered by SIL OFL 1.1
