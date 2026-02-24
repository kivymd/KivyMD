"""
Components/Splitter
===================

.. versionadded:: 2.0.0

The MDSplitter widget is a container that allows its children to be resized
by dragging a separator line.
"""

__all__ = ("MDSplitter", "MDSplitterStrip")

import os

from kivy.lang import Builder
from kivy.uix.splitter import Splitter, SplitterStrip

from kivymd import uix_path
from kivymd.theming import ThemableBehavior

with open(
    os.path.join(uix_path, "splitter", "splitter.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSplitterStrip(ThemableBehavior, SplitterStrip):
    """
    A custom splitter strip for MDSplitter.
    """


class MDSplitter(ThemableBehavior, Splitter):
    """
    A material design splitter.
    """
