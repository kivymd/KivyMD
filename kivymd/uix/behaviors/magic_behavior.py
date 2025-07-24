"""
Behaviors/Magic
===============

.. rubric:: Magical effects for buttons.

.. warning:: Magic effects do not work correctly with `KivyMD` buttons!

To apply magic effects, you must create a new class that is inherited from the
widget to which you apply the effect and from the :attr:`MagicBehavior` class.

.. code-block:: python

    class MagicButton(MagicBehavior, MDButton):
        ...

.. rubric:: The :attr:`MagicBehavior` class provides five effects:

- :attr:`MagicBehavior.wobble`
- :attr:`MagicBehavior.grow`
- :attr:`MagicBehavior.shake`
- :attr:`MagicBehavior.twist`
- :attr:`MagicBehavior.shrink`

Example
=======

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import StringProperty

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import MagicBehavior
            from kivymd.uix.button import MDButton, MDButtonText

            KV = '''
            MDScreen:
                md_bg_color: app.theme_cls.backgroundColor

                MagicButtonGrowEffect:
                    on_release: self.grow()
                    pos_hint: {"center_x": .5, "center_y": .4}

                MagicButtonShakeEffect:
                    on_release: self.shake()
                    pos_hint: {"center_x": .5, "center_y": .5}

                MagicButtonTwistEffect:
                    on_release: self.twist()
                    pos_hint: {"center_x": .5, "center_y": .6}

                MagicButtonShrinkEffect:
                    on_release: self.shrink()
                    pos_hint: {"center_x": .5, "center_y": .7}

                MagicButtonWobbleEffect:
                    on_release: self.wobble()
                    pos_hint: {"center_x": .5, "center_y": .8}
            '''


            class BaseMagicButton(MDButton):
                '''
                A base button class with customizable text and outlined style.

                This class serves as a foundation for creating magic-effect buttons
                (like grow, shake, twist) with predefined styling and structure.
                It automatically initializes a button with MDButtonText as its child widget.
                '''

                text = StringProperty()
                style = "outlined"

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.widgets = [
                        MDButtonText(
                            text=self.text
                        )
                    ]
                    super().__init__(*args, **kwargs)


            class MagicButtonGrowEffect(MagicBehavior, BaseMagicButton):
                scale_value = 1.03
                text = "Grow Effect"


            class MagicButtonShakeEffect(MagicBehavior, BaseMagicButton):
                translate_value = 15
                text = "Shake Effect"


            class MagicButtonTwistEffect(MagicBehavior, BaseMagicButton):
                rotate_value = 6
                text = "Twist Effect"


            class MagicButtonShrinkEffect(MagicBehavior, BaseMagicButton):
                scale_value = 0.95
                text = "Shrink Effect"


            class MagicButtonWobbleEffect(MagicBehavior, BaseMagicButton):
                scale_value = 0.95
                text = "Wobble Effect"


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.clock import Clock
            from kivy.properties import StringProperty

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import MagicBehavior
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.screen import MDScreen


            class BaseMagicButton(MDButton):
                '''
                A base button class with customizable text and outlined style.

                This class serves as a foundation for creating magic-effect buttons
                (like grow, shake, twist) with predefined styling and structure.
                It automatically initializes a button with MDButtonText as its child widget.
                '''

                text = StringProperty()
                style = "outlined"

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    Clock.schedule_once(self.add_text)

                def add_text(self, *args) -> None:
                    self.widgets = [
                        MDButtonText(
                            text=self.text,
                            pos_hint={"center_x": .5, "center_y": .5}
                        )
                    ]

                def on_release(self, *args) -> None:
                    super().on_release(args)
                    {
                        "Grow": self.grow,
                        "Shake": self.shake,
                        "Twist": self.twist,
                        "Shrink": self.shrink,
                        "Wobble": self.wobble,
                    }.get(self.text.split()[0], "Grow")()


            class MagicButtonGrowEffect(MagicBehavior, BaseMagicButton):
                scale_value = 1.03
                text = "Grow Effect"


            class MagicButtonShakeEffect(MagicBehavior, BaseMagicButton):
                translate_value = 15
                text = "Shake Effect"


            class MagicButtonTwistEffect(MagicBehavior, BaseMagicButton):
                rotate_value = 6
                text = "Twist Effect"


            class MagicButtonShrinkEffect(MagicBehavior, BaseMagicButton):
                scale_value = 0.95
                text = "Shrink Effect"


            class MagicButtonWobbleEffect(MagicBehavior, BaseMagicButton):
                scale_value = 0.95
                text = "Wobble Effect"


            class Example(MDApp):
                def build(self):
                    return (
                        MDScreen(
                            MDBoxLayout(
                                MagicButtonGrowEffect(
                                ),
                                MagicButtonShakeEffect(
                                ),
                                MagicButtonTwistEffect(
                                ),
                                MagicButtonShrinkEffect(
                                ),
                                MagicButtonWobbleEffect(
                                ),
                                spacing="24dp",
                                orientation="vertical",
                                adaptive_size=True,
                                pos_hint={"center_x": .5, "center_y": .5}
                            ),
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/magic-button-3.gif
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
            # origin: self.center
            angle: self.rotate or 0
        Scale:
            # origin: self.center
            x: self.scale_x or 1
            y: self.scale_y or 1
    canvas.after:
        PopMatrix
"""
)


class MagicBehavior:
    """
    A mixin class that provides animated visual effects for Kivy/KivyMD widgets.

    `MagicBehavior` adds interactive animation effects that enhance user interface
    feedback and engagement. These animations include:

    - `grow()`: Expands the widget slightly and returns to its original size.
    - `shake()`: Shakes the widget horizontally.
    - `wobble()`: Squashes and stretches the widget briefly.
    - `twist()`: Rotates the widget and resets its angle.
    - `shrink()`: Shrinks the widget temporarily and restores it.
    """

    scale_value = NumericProperty(1)
    """
    Scale factor for animation effects.

    .. versionadded:: 2.0.0

    :attr:`scale_value` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    translate_value = NumericProperty(1)
    """
    Translation distance for animation effects.

    .. versionadded:: 2.0.0

    :attr:`translate_value` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    rotate_value = NumericProperty(25)
    """
    Rotation angle in degrees for animation effects.

    .. versionadded:: 2.0.0

    :attr:`rotate_value` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `25`.
    """

    magic_speed = NumericProperty(1)
    """
    Animation playback speed.

    :attr:`magic_speed` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    def grow(self) -> None:
        """Grow effect animation."""

        (
            Animation(
                scale_x=self.scale_value,
                scale_y=self.scale_value,
                t="out_quad",
                d=0.03 / self.magic_speed,
            )
            + Animation(
                scale_x=1, scale_y=1, t="out_elastic", d=0.4 / self.magic_speed
            )
        ).start(self)

    def shake(self) -> None:
        """Shake effect animation."""

        (
            Animation(
                translate_x=self.translate_value,
                t="out_quad",
                d=0.02 / self.magic_speed,
            )
            + Animation(
                translate_x=0, t="out_elastic", d=0.5 / self.magic_speed
            )
        ).start(self)

    def wobble(self) -> None:
        """Wobble effect animation."""

        (
            (
                Animation(scale_y=0.1, t="out_quad", d=0.03 / self.magic_speed)
                & Animation(
                    scale_x=0.2, t="out_quad", d=0.03 / self.magic_speed
                )
            )
            + (
                Animation(scale_y=1, t="out_elastic", d=0.5 / self.magic_speed)
                & Animation(
                    scale_x=1, t="out_elastic", d=0.4 / self.magic_speed
                )
            )
        ).start(self)

    def twist(self) -> None:
        """Twist effect animation."""

        (
            Animation(
                rotate=self.rotate_value,
                t="out_quad",
                d=0.05 / self.magic_speed,
            )
            + Animation(rotate=0, t="out_elastic", d=0.5 / self.magic_speed)
        ).start(self)

    def shrink(self) -> None:
        """Shrink effect animation."""

        (
            Animation(
                scale_x=self.scale_value,
                scale_y=self.scale_value,
                t="out_quad",
                d=0.1 / self.magic_speed,
            )
            + Animation(
                scale_x=1, scale_y=1, t="out_elastic", d=0.5 / self.magic_speed
            )
        ).start(self)

    def on_touch_up(self, *args):
        Animation.stop_all(self)
        return super().on_touch_up(*args)
