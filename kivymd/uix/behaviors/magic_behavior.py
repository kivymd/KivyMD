"""
Behaviors/Magic
===============

.. rubric:: Magical effects for buttons.

.. warning:: Magic effects do not work correctly with `KivyMD` buttons!

To apply magic effects, you must create a new class that is inherited from the
widget to which you apply the effect and from the :attr:`MagicBehavior` class.

In `KV file`:

.. code-block:: kv

    <MagicButton@MagicBehavior+MDRectangleFlatButton>

In `python file`:

.. code-block:: python

    class MagicButton(MagicBehavior, MDRectangleFlatButton):
        pass

.. rubric:: The :attr:`MagicBehavior` class provides five effects:

- :attr:`MagicBehavior.wobble`
- :attr:`MagicBehavior.grow`
- :attr:`MagicBehavior.shake`
- :attr:`MagicBehavior.twist`
- :attr:`MagicBehavior.shrink`

Example:

.. code-block:: python

    from kivymd.app import MDApp
    from kivy.lang import Builder

    KV = '''
    #:import MagicBehavior kivymd.uix.behaviors.MagicBehavior


    <MagicButton@MagicBehavior+MDRectangleFlatButton>


    FloatLayout:

        MagicButton:
            text: "WOBBLE EFFECT"
            on_release: self.wobble()
            pos_hint: {"center_x": .5, "center_y": .3}

        MagicButton:
            text: "GROW EFFECT"
            on_release: self.grow()
            pos_hint: {"center_x": .5, "center_y": .4}

        MagicButton:
            text: "SHAKE EFFECT"
            on_release: self.shake()
            pos_hint: {"center_x": .5, "center_y": .5}

        MagicButton:
            text: "TWIST EFFECT"
            on_release: self.twist()
            pos_hint: {"center_x": .5, "center_y": .6}

        MagicButton:
            text: "SHRINK EFFECT"
            on_release: self.shrink()
            pos_hint: {"center_x": .5, "center_y": .7}
    '''


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()


.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/magic-button.gif
   :width: 250 px
   :align: center
"""

__all__ = ("MagicBehavior",)

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import NumericProperty

Builder.load_string(
    """
<MagicBehavior>
    translate_x: 0
    translate_y: 0
    scale_x: 1
    scale_y: 1
    rotate: 0

    canvas.before:
        PushMatrix
        Translate:
            x: self.translate_x or 0
            y: self.translate_y or 0
        Rotate:
            origin: self.center
            angle: self.rotate or 0
        Scale:
            origin: self.center
            x: self.scale_x or 1
            y: self.scale_y or 1
    canvas.after:
        PopMatrix
"""
)


class MagicBehavior:

    magic_speed = NumericProperty(1)
    """
    Animation playback speed.

    :attr:`magic_speed` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    def grow(self):
        """Grow effect animation."""

        (
            Animation(
                scale_x=1.2,
                scale_y=1.2,
                t="out_quad",
                d=0.03 / self.magic_speed,
            )
            + Animation(
                scale_x=1, scale_y=1, t="out_elastic", d=0.4 / self.magic_speed
            )
        ).start(self)

    def shake(self):
        """Shake effect animation."""

        (
            Animation(translate_x=50, t="out_quad", d=0.02 / self.magic_speed)
            + Animation(
                translate_x=0, t="out_elastic", d=0.5 / self.magic_speed
            )
        ).start(self)

    def wobble(self):
        """Wobble effect animation."""

        (
            (
                Animation(scale_y=0.7, t="out_quad", d=0.03 / self.magic_speed)
                & Animation(
                    scale_x=1.4, t="out_quad", d=0.03 / self.magic_speed
                )
            )
            + (
                Animation(scale_y=1, t="out_elastic", d=0.5 / self.magic_speed)
                & Animation(
                    scale_x=1, t="out_elastic", d=0.4 / self.magic_speed
                )
            )
        ).start(self)

    def twist(self):
        """Twist effect animation."""

        (
            Animation(rotate=25, t="out_quad", d=0.05 / self.magic_speed)
            + Animation(rotate=0, t="out_elastic", d=0.5 / self.magic_speed)
        ).start(self)

    def shrink(self):
        """Shrink effect animation."""

        Animation(
            scale_x=0.95, scale_y=0.95, t="out_quad", d=0.1 / self.magic_speed
        ).start(self)

    def on_touch_up(self, *args):
        Animation.stop_all(self)
        return super().on_touch_up(*args)
