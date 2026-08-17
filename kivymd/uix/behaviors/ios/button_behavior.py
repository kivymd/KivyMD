"""
Behaviors/iOS Button
====================

.. versionadded:: 2.0.1

.. rubric:: A behavior that implements an iOS-style interactive button.

The :class:`~IOSButtonBehavior` class provides a touch-responsive button
behavior inspired by the interaction of buttons in iOS. When the user
presses the widget, it smoothly scales up and activates the corresponding
glass/touch response. When the touch is released, the widget smoothly
returns to its original scale.

The behavior can be combined with other widgets or behaviors to create
custom interactive components.

Example
-------

.. tabs::

    .. tab:: Imperative Python style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.behaviors import IOSGlassBehavior, IOSButtonBehavior
            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                FitImage:
                    id: bg_image
                    source: "https://picsum.photos/800/600?random=2"

                GlassContainer:
                    target_background: bg_image
                    border_radius: [dp(26), dp(26), dp(26), dp(26)]
                    glass_color: [1.0, 1.0, 1.0, 0.18]
                    blur_amount: 10.0
                    size_hint: None, None
                    size: "400dp", "200dp"
                    pos_hint: {"center_x": .5, "center_y": .5}
            '''


            class GlassContainer(IOSGlassBehavior, IOSButtonBehavior, MDBoxLayout):
                pass


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import IOSGlassBehavior, IOSButtonBehavior
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.screen import MDScreen


            class MyScreen(MDScreen):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                    bg_image = FitImage(source="https://picsum.photos/800/600?random=2")
                    self.widgets = [
                        bg_image,
                        GlassContainer(
                            target_background=bg_image,
                            border_radius=[dp(26), dp(26), dp(26), dp(26)],
                            glass_color=[1.0, 1.0, 1.0, 0.18],
                            blur_amount=10.0,
                            size_hint=(None, None),
                            size=("400dp", "200dp"),
                            pos_hint={"center_x": .5, "center_y": .5},
                        ),
                    ]


            class GlassContainer(IOSGlassBehavior, IOSButtonBehavior, MDBoxLayout):
                pass


            class Example(MDApp):
                def build(self):
                    return MyScreen()


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-button-behavior-example.gif
    :align: center

.. Note::
    Use the :class:`~kivy.uix.behaviors.ButtonBehavior` class only in
    conjunction with the :class:`~kivy.uix.behaviors.IOSGlassBehavior` class.

    Right
    -----

    .. code-block:: python

        class GlassContainer(IOSGlassBehavior, IOSButtonBehavior, MDBoxLayout):
            ...

    Wrong
    -----

    .. code-block:: python

        class GlassContainer(IOSButtonBehavior, MDBoxLayout):
            ...
"""

__all__ = ("IOSButtonBehavior",)

from kivy.animation import Animation
from kivy.graphics import PopMatrix, PushMatrix, Scale
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior


class IOSButtonBehavior(ButtonBehavior):
    """
    Implements iOS-style interactive button behaviors.

    Provides touch-responsive feedback by applying smooth scaling animations
    and tracking touch positions for glass glare effects. On press, the widget
    scales up to 110% and updates press intensity factors. On release, it
    returns to its original scale with a spring-back transition.

    For more information, see in the
    :class:`~kivy.uix.behaviors.ButtonBehavior`
    class documentation.
    """

    press_scale_transition = StringProperty("easing_accelerated")
    """
    The type of transition for the scale-up animation on touch down.

    .. code-block:: python

        GlassContainer(
            press_scale_transition="out_elastic",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-button-behavior-press-scale-transition.gif
        :align: center

    :attr:`press_scale_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'easing_accelerated'`.
    """

    press_scale_duration = NumericProperty(0.14)
    """
    The duration of the scale-up animation on touch down in seconds.

    .. code-block:: python

        GlassContainer(
            press_scale_duration=2,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-button-behavior-press-scale-duration.gif
        :align: center

    :attr:`press_scale_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.14`.
    """

    release_scale_transition = StringProperty("out_back")
    """
    The type of transition for returning to original scale on touch up.

    .. code-block:: python

        GlassContainer(
            release_scale_transition="out_elastic",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-button-behavior-release-scale-transition.gif
        :align: center

    :attr:`release_scale_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_back'`.
    """

    release_scale_duration = NumericProperty(0.22)
    """
    The duration of returning to original scale animation on touch up in seconds.

    .. code-block:: python

        GlassContainer(
            release_scale_duration=2,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-button-behavior-release-scale-duration.gif
        :align: center

    :attr:`release_scale_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.22`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._scale_instr = Scale(1, 1, 1, origin=self.center)

        self.canvas.before.insert(0, self._scale_instr)
        self.canvas.before.insert(0, PushMatrix())
        self.canvas.after.add(PopMatrix())

        self.bind(
            center=self._update_scale_origin,
            _scale_factor=self._update_scale,
        )

    def _update_scale_origin(self, *args):
        self._scale_instr.origin = self.center

    def _update_scale(self, instance, value):
        self._scale_instr.x = value
        self._scale_instr.y = value

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self._touch_pos = list(touch.pos)

            Animation.cancel_all(self, "_press_factor", "_scale_factor")

            # Glint from a finger touch animation.
            anim_press = Animation(
                _press_factor=1.0,
                d=0.14,
                t="easing_decelerated",
            )
            # Container scaling animation.
            anim_scale = Animation(
                _scale_factor=1.1,
                d=self.press_scale_duration,
                t=self.press_scale_transition,
            )

            anim_press.start(self)
            anim_scale.start(self)

        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self._touch_pos = list(touch.pos)

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        Animation.cancel_all(self, "_press_factor", "_scale_factor")

        # Glint from a finger touch animation.
        anim_release = Animation(
            _press_factor=0.0,
            d=0.2,
            t="out_quad",
        )
        # Container scaling animation.
        anim_scale_back = Animation(
            _scale_factor=1.0,
            d=self.release_scale_duration,
            t=self.release_scale_transition,
        )

        anim_release.start(self)
        anim_scale_back.start(self)

        return super().on_touch_up(touch)
