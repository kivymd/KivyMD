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


    Screen:

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

Usage with padding
------------------

.. code-block:: python

    Snackbar(text="This is a snackbar!", padding="20dp").open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-padding.gif
    :align: center

Custom text color
-----------------

.. code-block:: python

    Snackbar(text="[color=#ddbb34]This is a snackbar![/color]", size_hint_x=.7, padding="20dp").open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-custom-color.png
    :align: center

Control width
-------------

.. code-block:: python

    Snackbar(text="This is a snackbar!", size_hint_x=.5).open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-percent-width.png
    :align: center

Usage with button
-----------------

.. code-block:: python

    snackbar = Snackbar(
        text="This is a snackbar!",
    )
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
-------------------------------

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
    Screen:

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
    from kivy.properties import StringProperty

    from kivymd.app import MDApp
    from kivymd.uix.button import MDFlatButton
    from kivymd.uix.snackbar import Snackbar

    KV = '''
    <-Snackbar>

        MDCard:
            id: box
            size_hint_y: None
            height: dp(58)
            spacing: dp(5)
            padding: dp(10)
            y: -self.height
            x: root.padding
            md_bg_color: get_color_from_hex('323232')
            radius: (5, 5, 5, 5) if root.padding else (0, 0, 0, 0)
            elevation: 11 if root.padding else 0

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
                text_color: get_color_from_hex('ffffff')
                shorten: True
                shorten_from: 'right'
                pos_hint: {'center_y': .5}


    Screen:

        MDRaisedButton:
            text: "SHOW"
            pos_hint: {"center_x": .5, "center_y": .45}
            on_press: app.show()
    '''


    class CustomSnackbar(Snackbar):
        icon = StringProperty()


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def show(self):
            CustomSnackbar(
                text="This is a snackbar!",
                icon="information",
                padding="20dp",
                buttons=[MDFlatButton(text="ACTION", text_color=(1, 1, 1, 1))]
            ).open()


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-custom.png
    :align: center
"""

__all__ = ("Snackbar",)

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
)

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import BaseButton

Builder.load_string(
    """
#:import get_color_from_hex kivy.utils.get_color_from_hex


<Snackbar>

    MDCard:
        id: box
        size_hint_y: None
        height: "58dp"
        spacing: "4dp"
        padding: "10dp", "10dp", "10dp", "10dp"
        y: -self.height
        x: root.padding[0]
        md_bg_color: get_color_from_hex("323232") if not root.bg_color else root.bg_color
        radius: root.radius if root.padding != [0, 0, 0, 0] else [0, 0, 0, 0]
        elevation: 11 if root.padding else 0

        canvas:
            Color:
                rgba: self.md_bg_color
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: self.radius

        MDLabel:
            id: text_bar
            size_hint_y: None
            height: self.texture_size[1]
            text: root.text
            font_size: root.font_size
            theme_text_color: "Custom"
            text_color: get_color_from_hex("ffffff")
            shorten: True
            shorten_from: "right"
            markup: True
            pos_hint: {"center_y": .5}
"""
)


class Snackbar(MDBoxLayout):
    """
    :Events:
        :attr:`on_open`
            Called when a dialog is opened.
        :attr:`on_dismiss`
            When the front layer rises.
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

    bg_color = ListProperty()
    """
    Snackbar background.

    :attr:`bg_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `'[]'`.
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

    _interval = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_dismiss")

    def dismiss(self, *args):
        """Dismiss the snackbar."""

        def dismiss(interval):
            anim = Animation(y=-self.ids.box.height, d=0.2)
            anim.bind(
                on_complete=lambda *args: Window.parent.remove_widget(self)
            )
            anim.start(self.ids.box)

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

        self.y = -self.ids.box.height - self.padding[0]
        Window.parent.add_widget(self)
        anim = Animation(y=self.padding[0], d=0.2)
        if self.auto_dismiss:
            anim.bind(
                on_complete=lambda *args: Clock.schedule_interval(
                    wait_interval, 0
                )
            )
        anim.start(self.ids.box)
        self.dispatch("on_open")

    def on_open(self, *args):
        """Called when a dialog is opened."""

    def on_dismiss(self, *args):
        """Called when the dialog is closed."""

    def on_buttons(self, instance, value):
        def on_buttons(interval):
            for button in value:
                if issubclass(button.__class__, (BaseButton,)):
                    self.ids.box.add_widget(button)
                else:
                    raise ValueError(
                        f"The {button} object must be inherited from the base class <BaseButton>"
                    )

        Clock.schedule_once(on_buttons)
