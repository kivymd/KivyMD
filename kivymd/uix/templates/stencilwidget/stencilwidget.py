"""
Templates/StencilWidget
=======================

.. versionadded:: 1.0.0

Base class for controlling the stencil instructions of the widget.

.. note:: See `Stencil instructions
    <https://kivy.org/doc/stable/api-kivy.graphics.stencil_instructions.html>`_
    for more information.

Kivy
----

.. code-block:: python

    from kivy.lang import Builder
    from kivy.app import App

    KV = '''
    Carousel:

        Button:
            size_hint: .9, .8
            pos_hint: {"center_x": .5, "center_y": .5}

            canvas.before:
                StencilPush
                RoundedRectangle:
                    pos: root.pos
                    size: root.size
                StencilUse
            canvas.after:
                StencilUnUse
                RoundedRectangle:
                    pos: root.pos
                    size: root.size
                StencilPop
    '''


    class Test(App):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

KivyMD
------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.templates import StencilWidget
    from kivymd.utils.fitimage import FitImage

    KV = '''
    MDCarousel:

        StencilImage:
            size_hint: .9, .8
            pos_hint: {"center_x": .5, "center_y": .5}
            source: "image.png"
    '''


    class StencilImage(FitImage, StencilWidget):
        pass


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()
"""

__all__ = ("StencilWidget",)

import os

from kivy.lang import Builder
from kivy.properties import VariableListProperty

from kivymd import uix_path

with open(
    os.path.join(uix_path, "templates", "stencilwidget", "stencilwidget.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class StencilWidget:
    """Base class for controlling the stencil instructions of the widget"""

    radius = VariableListProperty([0], length=4)
    """
    Canvas radius.

    .. versionadded:: 1.0.0

    .. code-block:: python

        # Top left corner slice.
        MDWidget:
            radius: [25, 0, 0, 0]

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """
