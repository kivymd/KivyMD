"""
Components/Widget
=================

:class:`~kivy.uix.widget.Widget` class equivalent. Simplifies working
with some widget properties. For example:

Widget
------

.. code-block::

    Widget:
        size_hint: .5, None
        height: self.width

        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [self.height / 2,]

MDWidget
--------

.. code-block::

    MDWidget:
        size_hint: .5, None
        height: self.width
        radius: self.height / 2
        md_bg_color: app.theme_cls.primary_color
"""

from kivymd.uix import MDAdaptiveWidget


class MDWidget(MDAdaptiveWidget):
    """
    See :class:`~kivy.uix.Widget` class documentation for more information.

    .. versionadded:: 1.0.0
    """
