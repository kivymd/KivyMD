"""
KivyMD
======

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/previous.png

Is a collection of Material Design compliant widgets for use with,
`Kivy cross-platform graphical framework <http://kivy.org/#home>`_
a framework for cross-platform, touch-enabled graphical applications.
The project's goal is to approximate Google's `Material Design spec
<https://material.io/design/introduction>`_ as close as possible without
sacrificing ease of use.

This library is a fork of the `KivyMD project
<https://gitlab.com/kivymd/KivyMD>`_. We found the strength and brought this
project to a new level.

If you wish to become a project developer (permission to create branches on the
project without forking for easier collaboration), have at least one PR
approved and ask for it. If you contribute regularly to the project the role
may be offered to you without asking too.
"""

import os

import kivy
from kivy.logger import Logger

__version__ = "1.1.0.dev0"
"""KivyMD version."""

release = False
kivy.require("2.0.0")

try:
    from kivymd._version import __date__, __hash__, __short_hash__
except ImportError:
    __hash__ = __short_hash__ = __date__ = ""

path = os.path.dirname(__file__)
"""Path to KivyMD package directory."""

fonts_path = os.path.join(path, f"fonts{os.sep}")
"""Path to fonts directory."""

images_path = os.path.join(path, f"images{os.sep}")
"""Path to images directory."""

uix_path = os.path.join(path, "uix")
"""Path to uix directory."""

glsl_path = os.path.join(path, "data", "glsl")
"""Path to glsl directory."""

_log_message = (
    "KivyMD:"
    + (" Release" if release else "")
    + f" {__version__}"
    + (f", git-{__short_hash__}" if __short_hash__ else "")
    + (f", {__date__}" if __date__ else "")
    + f' (installed at "{__file__}")'
)
Logger.info(_log_message)

import kivymd.factory_registers  # NOQA
import kivymd.font_definitions  # NOQA
from kivymd.tools.packaging.pyinstaller import hooks_path  # NOQA
