"""
Components/ScrollView
=====================

.. versionadded:: 1.0.0

:class:`~kivy.uix.scrollview.ScrollView` class equivalent. Simplifies working
with some widget properties. For example:

ScrollView
----------

.. code-block::

    ScrollView:

        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

MDScrollView
------------

.. code-block::

    MDScrollView:
        md_bg_color: app.theme_cls.primary_color
"""

__all__ = ("MDScrollView",)

from kivy.uix.scrollview import ScrollView

from kivymd.uix.behaviors import DeclarativeBehavior


class MDScrollView(DeclarativeBehavior, ScrollView):
    pass
