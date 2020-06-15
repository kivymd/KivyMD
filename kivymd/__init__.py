"""
KivyMD
======

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/previous.png

Is a collection of Material Design compliant widgets for use with,
`Kivy cross-platform graphical framework <http://kivy.org/#home>`_
a framework for cross-platform, touch-enabled graphical applications.
The project's goal is to approximate Google's `Material Design spec
<https://material.io/design/introduction>`_ as close as possible without
sacrificing ease of use or application performance.

This library is a fork of the `KivyMD project
<https://gitlab.com/kivymd/KivyMD>`_ the author of which stopped supporting
this project three years ago. We found the strength and brought this project
to a new level. Currently we're in **alpha** status, so things are changing
all the time and we cannot promise any kind of API stability.
However it is safe to vendor now and make use of what's currently available.

Join the project! Just fork the project, branch out and submit a pull request
when your patch is ready. If any changes are necessary, we'll guide you
through the steps that need to be done via PR comments or access to your for
may be requested to outright submit them. If you wish to become a project
developer (permission to create branches on the project without forking for
easier collaboration), have at least one PR approved and ask for it.
If you contribute regularly to the project the role may be offered to you
without asking too.
"""

import os

from kivy.logger import Logger

__version__ = "0.104.1"
"""KivyMD version."""

path = os.path.dirname(__file__)
"""Path to KivyMD package directory."""

fonts_path = os.path.join(path, f"fonts{os.sep}")
"""Path to fonts directory."""

images_path = os.path.join(path, f"images{os.sep}")
"""Path to images directory."""

Logger.info(f"KivyMD: v{__version__}")

import kivymd.factory_registers  # NOQA
import kivymd.font_definitions  # NOQA
from kivymd.tools.packaging.pyinstaller import hooks_path  # NOQA
