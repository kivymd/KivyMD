"""
Components/Snackbar
===================

.. seealso::

    `Material Design spec, Snackbars <https://material.io/components/snackbars>`_

.. rubric:: Snackbars provide brief messages about app processes at the bottom
    of the screen.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar.png
    :align: center

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    #:import Snackbar kivymd.uix.snackbar.Snackbar


    MDScreen:

        MDRaisedButton:
            text: "Create simple snackbar"
            on_release: Snackbar(text="This is a snackbar!").open()
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-simple.gif
    :align: center

Usage with snackbar_x, snackbar_y
---------------------------------

.. code-block:: python

    Snackbar(
        text="This is a snackbar!",
        snackbar_x="10dp",
        snackbar_y="10dp",
        size_hint_x=(
            Window.width - (dp(10) * 2)
        ) / Window.width
    ).open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-padding.gif
    :align: center

Control width
-------------

.. code-block:: python

    Snackbar(
        text="This is a snackbar!",
        snackbar_x="10dp",
        snackbar_y="10dp",
        size_hint_x=.5
    ).open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-percent-width.png
    :align: center

Custom text color
-----------------

.. code-block:: python

    Snackbar(
        text="[color=#ddbb34]This is a snackbar![/color]",
        snackbar_y="10dp",
        snackbar_y="10dp",
        size_hint_x=.7
    ).open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-custom-color.png
    :align: center

Usage with button
-----------------

.. code-block:: python

    snackbar = Snackbar(
        text="This is a snackbar!",
        snackbar_x="10dp",
        snackbar_y="10dp",
    )
    snackbar.size_hint_x = (
        Window.width - (snackbar.snackbar_x * 2)
    ) / Window.width
    snackbar.buttons = [
        MDFlatButton(
            text="UPDATE",
            text_color=(1, 1, 1, 1),
            on_release=snackbar.dismiss,
        ),
        MDFlatButton(
            text="CANCEL",
            text_color=(1, 1, 1, 1),
            on_release=snackbar.dismiss,
        ),
    ]
    snackbar.open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-button.png
    :align: center

Using a button with custom color
--------------------------------

.. code-block:: python

    Snackbar(
        ...
        bg_color=(0, 0, 1, 1),
    ).open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-button-custom-color.png
    :align: center

Custom usage
------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.animation import Animation
    from kivy.clock import Clock
    from kivy.metrics import dp

    from kivymd.app import MDApp
    from kivymd.uix.snackbar import Snackbar


    KV = '''
    MDScreen:

        MDFloatingActionButton:
            id: button
            x: root.width - self.width - dp(10)
            y: dp(10)
            on_release: app.snackbar_show()
    '''


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            self.snackbar = None
            self._interval = 0

        def build(self):
            return self.screen

        def wait_interval(self, interval):
            self._interval += interval
            if self._interval > self.snackbar.duration + 0.5:
                anim = Animation(y=dp(10), d=.2)
                anim.start(self.screen.ids.button)
                Clock.unschedule(self.wait_interval)
                self._interval = 0
                self.snackbar = None

        def snackbar_show(self):
            if not self.snackbar:
                self.snackbar = Snackbar(text="This is a snackbar!")
                self.snackbar.open()
                anim = Animation(y=dp(72), d=.2)
                anim.bind(on_complete=lambda *args: Clock.schedule_interval(
                    self.wait_interval, 0))
                anim.start(self.screen.ids.button)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-custom-usage.gif
    :align: center

Custom Snackbar
---------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.core.window import Window
    from kivy.properties import StringProperty, NumericProperty

    from kivymd.app import MDApp
    from kivymd.uix.button import MDFlatButton
    from kivymd.uix.snackbar import BaseSnackbar

    KV = '''
    <CustomSnackbar>

        MDIconButton:
            pos_hint: {'center_y': .5}
            icon: root.icon
            opposite_colors: True

        MDLabel:
            id: text_bar
            size_hint_y: None
            height: self.texture_size[1]
            text: root.text
            font_size: root.font_size
            theme_text_color: 'Custom'
            text_color: 'ffffff'
            shorten: True
            shorten_from: 'right'
            pos_hint: {'center_y': .5}


    MDScreen:

        MDRaisedButton:
            text: "SHOW"
            pos_hint: {"center_x": .5, "center_y": .45}
            on_press: app.show()
    '''


    class CustomSnackbar(BaseSnackbar):
        text = StringProperty(None)
        icon = StringProperty(None)
        font_size = NumericProperty("15sp")


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def show(self):
            snackbar = CustomSnackbar(
                text="This is a snackbar!",
                icon="information",
                snackbar_x="10dp",
                snackbar_y="10dp",
                buttons=[MDFlatButton(text="ACTION", text_color=(1, 1, 1, 1))]
            )
            snackbar.size_hint_x = (
                Window.width - (snackbar.snackbar_x * 2)
            ) / Window.width
            snackbar.open()


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-custom.png
    :align: center
"""

__all__ = ("Snackbar", "BaseSnackbar")

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
    StringProperty,
)

from kivymd import uix_path
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.button import BaseButton
from kivymd.uix.card import MDCard

with open(
    os.path.join(uix_path, "snackbar", "snackbar.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class BaseSnackbar(MDCard, FakeRectangularElevationBehavior):
    """
    :Events:
        :attr:`on_open`
            Called when a dialog is opened.
        :attr:`on_dismiss`
            When the front layer rises.

    Abstract base class for all Snackbars.
    This class handles sizing, positioning, shape and events for Snackbars

    All Snackbars will be made off of this `BaseSnackbar`.

    `BaseSnackbar` will always try to fill the remainder of the screen with
    your Snackbar.

    To make your Snackbar dynamic and symetric with snackbar_x.

    Set size_hint_x like below:

    .. code-block:: python

        size_hint_z = (
            Window.width - (snackbar_x * 2)
        ) / Window.width
    """

    duration = NumericProperty(3)
    """
    The amount of time that the snackbar will stay on screen for.

    :attr:`duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `3`.
    """

    auto_dismiss = BooleanProperty(True)
    """
    Whether to use automatic closing of the snackbar or not.

    :attr:`auto_dismiss` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `'True'`.
    """

    bg_color = ColorProperty(None)
    """
    Snackbar background.

    :attr:`bg_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    buttons = ListProperty()
    """
    Snackbar buttons.

    :attr:`buttons` is a :class:`~kivy.properties.ListProperty`
    and defaults to `'[]'`
    """

    radius = ListProperty([5, 5, 5, 5])
    """
    Snackbar radius.

    :attr:`radius` is a :class:`~kivy.properties.ListProperty`
    and defaults to `'[5, 5, 5, 5]'`
    """

    snackbar_animation_dir = OptionProperty(
        "Bottom",
        options=["Top", "Bottom", "Left", "Right"],
    )
    """
    Snackbar animation direction.

    Available options are: `"Top"`, `"Bottom"`, `"Left"`, `"Right"`

    :attr:`snackbar_animation_dir` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Bottom'`.
    """

    snackbar_x = NumericProperty("0dp")
    """
    The snackbar x position in the screen

    :attr:`snackbar_x` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0dp`.
    """

    snackbar_y = NumericProperty("0dp")
    """
    The snackbar x position in the screen

    :attr:`snackbar_y` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0dp`.
    """

    _interval = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_dismiss")

    def dismiss(self, *args):
        """Dismiss the snackbar."""

        def dismiss(interval):
            if self.snackbar_animation_dir == "Top":
                anim = Animation(y=(Window.height + self.height), d=0.2)
            elif self.snackbar_animation_dir == "Left":
                anim = Animation(x=-self.width, d=0.2)
            elif self.snackbar_animation_dir == "Right":
                anim = Animation(x=Window.width, d=0.2)
            else:
                anim = Animation(y=-self.height, d=0.2)

            anim.bind(
                on_complete=lambda *args: Window.parent.remove_widget(self)
            )
            anim.start(self)

        Clock.schedule_once(dismiss, 0.5)
        self.dispatch("on_dismiss")

    def open(self):
        """Show the snackbar."""

        def wait_interval(interval):
            self._interval += interval
            if self._interval > self.duration:
                self.dismiss()
                Clock.unschedule(wait_interval)
                self._interval = 0

        for c in Window.parent.children:
            if isinstance(c, BaseSnackbar):
                return

        if self.snackbar_y > (Window.height - self.height):
            self.snackbar_y = Window.height - self.height

        self._calc_radius()

        if self.size_hint_x == 1:
            self.size_hint_x = (Window.width - self.snackbar_x) / Window.width

        if (
            self.snackbar_animation_dir == "Top"
            or self.snackbar_animation_dir == "Bottom"
        ):
            self.x = self.snackbar_x

            if self.snackbar_animation_dir == "Top":
                self.y = Window.height + self.height
            else:
                self.y = -self.height

            Window.parent.add_widget(self)

            if self.snackbar_animation_dir == "Top":
                anim = Animation(
                    y=self.snackbar_y
                    if self.snackbar_y != 0
                    else Window.height - self.height,
                    d=0.2,
                )
            else:
                anim = Animation(
                    y=self.snackbar_y if self.snackbar_y != 0 else 0, d=0.2
                )

        elif (
            self.snackbar_animation_dir == "Left"
            or self.snackbar_animation_dir == "Right"
        ):
            self.y = self.snackbar_y

            if self.snackbar_animation_dir == "Left":
                self.x = -Window.width
            else:
                self.x = Window.width

            Window.parent.add_widget(self)
            anim = Animation(
                x=self.snackbar_x if self.snackbar_x != 0 else 0, d=0.2
            )

        if self.auto_dismiss:
            anim.bind(
                on_complete=lambda *args: Clock.schedule_interval(
                    wait_interval, 0
                )
            )
        anim.start(self)
        self.dispatch("on_open")

    def on_open(self, *args):
        """Called when a dialog is opened."""

    def on_dismiss(self, *args):
        """Called when the dialog is closed."""

    def on_buttons(self, instance, value):
        def on_buttons(interval):
            for button in value:
                if issubclass(button.__class__, (BaseButton,)):
                    self.add_widget(button)
                else:
                    raise ValueError(
                        f"The {button} object must be inherited from the base class <BaseButton>"
                    )

        Clock.schedule_once(on_buttons)

    def _calc_radius(self):
        if (
            self.snackbar_animation_dir == "Top"
            or self.snackbar_animation_dir == "Bottom"
        ):

            if self.snackbar_y == 0 and self.snackbar_x == 0:

                if self.size_hint_x == 1:
                    self.radius = [0, 0, 0, 0]
                else:
                    if self.snackbar_animation_dir == "Top":
                        self.radius = [0, 0, self.radius[2], 0]
                    else:
                        self.radius = [0, self.radius[1], 0, 0]

            elif self.snackbar_y != 0 and self.snackbar_x == 0:

                if self.size_hint_x == 1:
                    self.radius = [0, 0, 0, 0]
                else:
                    if self.snackbar_y >= Window.height - self.height:
                        self.radius = [0, 0, self.radius[2], 0]
                    else:
                        self.radius = [0, self.radius[1], self.radius[2], 0]

            elif self.snackbar_y == 0 and self.snackbar_x != 0:

                if self.size_hint_x == 1:
                    if self.snackbar_animation_dir == "Top":
                        self.radius = [0, 0, 0, self.radius[3]]
                    else:
                        self.radius = [self.radius[0], 0, 0, 0]
                else:
                    if self.snackbar_animation_dir == "Top":
                        self.radius = [0, 0, self.radius[2], self.radius[3]]
                    else:
                        self.radius = [self.radius[0], self.radius[1], 0, 0]

            else:  # self.snackbar_y != 0 and self.snackbar_x != 0

                if self.size_hint_x == 1:
                    self.radius = [self.radius[0], 0, 0, self.radius[3]]
                elif self.snackbar_y >= Window.height - self.height:
                    self.radius = [0, 0, self.radius[2], self.radius[3]]

        elif (
            self.snackbar_animation_dir == "Left"
            or self.snackbar_animation_dir == "Right"
        ):

            if self.snackbar_y == 0 and self.snackbar_x == 0:

                if self.size_hint_x == 1:
                    self.radius = [0, 0, 0, 0]
                else:
                    self.radius = [0, self.radius[1], 0, 0]

            elif self.snackbar_y != 0 and self.snackbar_x == 0:

                if self.size_hint_x == 1:
                    self.radius = [0, 0, 0, 0]
                else:
                    self.radius = [0, self.radius[1], self.radius[2], 0]

            elif self.snackbar_y == 0 and self.snackbar_x != 0:

                if self.size_hint_x == 1:
                    self.radius = [self.radius[0], 0, 0, 0]
                else:
                    self.radius = [self.radius[0], self.radius[1], 0, 0]

            else:  # self.snackbar_y != 0 and self.snackbar_x != 0

                if self.size_hint_x == 1:
                    if self.snackbar_y >= Window.height - self.height:
                        self.radius = [0, 0, 0, self.radius[3]]
                    else:
                        self.radius = [self.radius[0], 0, 0, self.radius[3]]
                elif self.snackbar_y >= Window.height - self.height:
                    self.radius = [0, 0, self.radius[2], self.radius[3]]


class Snackbar(BaseSnackbar):
    """
    Snackbar inherits all its functionality from `BaseSnackbar`
    """

    text = StringProperty()
    """
    The text that will appear in the snackbar.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    font_size = NumericProperty("15sp")
    """
    The font size of the text that will appear in the snackbar.

    :attr:`font_size` is a :class:`~kivy.properties.NumericProperty` and
    defaults to `'15sp'`.
    """
