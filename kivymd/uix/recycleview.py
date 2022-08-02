"""
Components/RecycleView
======================

.. versionadded:: 1.0.0

:class:`~kivy.uix.recycleview.RecycleView` class equivalent. Simplifies working
with some widget properties. For example:

RecycleView
-----------

.. code-block:: kv

    RecycleView:

        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

MDRecycleView
-------------

.. code-block:: kv

    MDRecycleView:
        md_bg_color: app.theme_cls.primary_color
"""

__all__ = ("MDRecycleView",)

from kivy.uix.recycleview import RecycleView

from kivymd.uix.behaviors import DeclarativeBehavior


class MDRecycleView(DeclarativeBehavior, RecycleView):
    """
    Recycle view class. For more information, see in the
    :class:`~kivy.uix.recycleview.RecycleView` class documentation.
    """
