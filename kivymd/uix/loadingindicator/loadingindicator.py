"""
Components/LoadingIndicator
===========================

.. seealso::

    `Material Design spec, Loading indicator <https://m3.material.io/components/loading-indicator/overview>`_
    `Shapes preview <https://github.com/T-Dynamos/materialshapes-python/tree/c48e367bd9e7ef3db95ea68bd2e3f8fd1fc976cb?tab=readme-ov-file#preview>`_

.. rubric:: Loading indicators display the status of a process using continuous or sequential shape animations.

- Used to represent indeterminate operations (no fixed end).
- Each shape is based on Material 3 geometry guidelines.
- Animations can cycle between multiple predefined shapes.


Usage
-----

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            from kivy.clock import Clock
            from kivy.lang import Builder
            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: app.theme_cls.surfaceColor
                MDLoadingIndicator:
                    id: indicator
                    shape_size: dp(100)
            '''


            class ExampleApp(MDApp):

                def build(self):
                    return Builder.load_string(KV)

                def on_start(self):
                    # start the morphing animation
                    self.root.ids.indicator.start()

                    # print available shape names
                    print(self.root.ids.indicator.get_shape_names())

                    # optionally stop animation after 5 seconds
                    # Clock.schedule_once(self.root.ids.indicator.stop, 5)


            ExampleApp().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.loadingindicator import MDLoadingIndicator

            class ExampleApp(MDApp):
                def build(self):
                    return MDScreen(
                        MDLoadingIndicator(
                            id="indicator",
                            shape_size="100dp",
                        ),
                        md_bg_color=self.theme_cls.surfaceColor,
                    )

                def on_start(self):
                    # start the morphing animation
                    self.root.children[0].start()

                    # print available shape names
                    print(self.root.children[0].get_shape_names())

                    # optionally stop animation after 5 seconds
                    # Clock.schedule_once(self.root.ids.indicator.stop, 5)

            ExampleApp().run()


.. image:: https://github.com/user-attachments/assets/1a24f741-a710-4271-993b-5a335a284787
    :align: center
"""


import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
)
from kivy.uix.anchorlayout import AnchorLayout

from materialshapes.kivy_widget import MaterialShape
from kivymd import uix_path
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.behaviors import RotateBehavior

with open(
    os.path.join(uix_path, "loadingindicator", "loadingindicator.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDLoadingIndicator(DeclarativeBehavior, AnchorLayout, RotateBehavior):
    """
    Implementation of a morphing and rotating loading indicator.

    For more information, see the
    :class:`~kivy.uix.anchorlayout.AnchorLayout` and
    :class:`~kivymd.uix.behaviors.RotateBehavior`
    classes documentation.
    """

    shape = StringProperty("cookie12Sided")
    """
    Current shape name displayed by the loading indicator.

    The shape corresponds to one of the predefined shapes available
    in the :class:`~materialshapes.kivy_widget.MaterialShape` library.

    You can view all available shape names using
    :meth:`get_shape_names`.

    :attr:`shape` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'cookie12Sided'`.
    """

    shape_sequence = ListProperty(
        [
            "cookie12Sided",
            "pentagon",
            "pill",
            "verySunny",
            "cookie4Sided",
            "oval",
            "flower",
            "softBoom",
        ]
    )
    """
    Sequence of shape names through which the indicator cycles.

    Each shape in the list is morphed into the next one over time,
    looping continuously while the indicator is active.

    :attr:`shape_sequence` is a :class:`~kivy.properties.ListProperty`
    and defaults to::

        [
            "cookie12Sided",
            "pentagon",
            "pill",
            "verySunny",
            "cookie4Sided",
            "oval",
            "flower",
            "softBoom",
        ]
    """

    shape_size = NumericProperty(dp(48))
    """
    Size of the loading indicator.

    :attr:`shape_size` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(48)`.
    """

    duration = NumericProperty(0.65)
    """
    Duration of one morph-and-rotate cycle in seconds.

    This value controls the overall speed of the loading indicator.

    :attr:`duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.65`.
    """

    active_indicator_color = ColorProperty([0,0,0,0])
    """
    Color of the active (foreground) loading shape.

    :attr:`active_indicator_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    container_color = ColorProperty([0,0,0,0])
    """
    Background container color of the indicator.

    :attr:`container_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    shape_index = NumericProperty(0)
    """
    Current index in the :attr:`shape_sequence`.

    :attr:`shape_index` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    _intrvl = None

    def start(self, *args):
        """
        Start the loading animation.

        Initiates the shape morphing and rotation cycle.
        The indicator continuously transitions between the shapes defined in
        :attr:`shape_sequence` while rotating at regular intervals.

        If already active, the animation sequence is reset.
        """
        self._run_cycle()
        self.stop()
        self._intrvl = Clock.schedule_interval(self._run_cycle, self.duration)

    def stop(self, *args):
        """
        Stop the loading animation.
        """
        if self._intrvl is not None:
            self._intrvl.cancel()
        self._intrvl = None

    def _run_cycle(self, *args):
        """
        Internal method for executing one morph-and-rotate cycle.

        Each cycle performs two actions:

        1. Morphs the current shape into the next in :attr:`shape_sequence`.
        2. Rotates the entire indicator by 90 degrees using an 'out_cubic'
           easing function.

        This method is called automatically at regular intervals
        determined by :attr:`duration`.
        """
        shape = self.shape_sequence[self.shape_index % len(self.shape_sequence)]
        self.ids.material_shape.morph_to(shape, d=self.duration * 0.9)

        Animation(
            rotate_value_angle=(self.shape_index + 1) * 90,
            duration=self.duration * 0.8,
            t="out_cubic",
        ).start(self)

        self.shape_index += 1


    def get_shape_names(self):
        """
        Return all available material shape names.
        """
        return list(self.ids.material_shape.material_shapes.all.keys())
