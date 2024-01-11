"""
Behaviors/Stencil
=================

.. versionadded:: 1.1.0

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
    from kivymd.uix.behaviors import StencilBehavior
    from kivymd.uix.fitimage import FitImage

    KV = '''
    #:import os os
    #:import images_path kivymd.images_path


    Carousel:

        StencilImage:
            size_hint: .9, .8
            pos_hint: {"center_x": .5, "center_y": .5}
            source: os.path.join(images_path, "logo", "kivymd-icon-512.png")
    '''


    class StencilImage(FitImage, StencilBehavior):
        pass


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()
"""

__all__ = ("StencilBehavior",)

from kivy.lang import Builder
from kivy.properties import VariableListProperty

Builder.load_string(
    """
<StencilBehavior>
    canvas.before:
        StencilPush
        RoundedRectangle:
            pos: root.pos
            size: root.size
            # FIXME: Sometimes the radius has the value [], which get a
            #  `GraphicException: Invalid radius value, must be list of tuples/numerics` error
            radius: root.radius if root.radius else [0, 0, 0, 0]
        StencilUse
    canvas.after:
        StencilUnUse
        RoundedRectangle:
            pos: root.pos
            size: root.size
            # FIXME: Sometimes the radius has the value [], which get a
            #  `GraphicException: Invalid radius value, must be list of tuples/numerics` error
            radius: root.radius if root.radius else [0, 0, 0, 0]
        StencilPop
"""
)


class StencilBehavior:
    """Base class for controlling the stencil instructions of the widget."""

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
