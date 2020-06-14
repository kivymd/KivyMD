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
            on_release: Snackbar(text="This is a snackbar!").show()
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

    Snackbar(text="This is a snackbar!", padding="20dp").show()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-padding.gif
    :align: center

Usage with button
-----------------

.. code-block:: python

    Snackbar(
        text="This is a snackbar",
        button_text="BUTTON",
        button_callback=app.callback
    ).show()

.. code-block:: python
    def callback(self, instance):
        from kivymd.toast import toast

        toast(instance.text)

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-button.gif
    :align: center

Using a button with custom color
-------------------------------

.. code-block:: python

    Snackbar(
        text="This is a snackbar!",
        padding="20dp",
        button_text="ACTION",
        button_color=(1, 0, 1, 1)
    ).show()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-button-custom-color.gif
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
            if self._interval > self.snackbar.duration:
                anim = Animation(y=dp(10), d=.2)
                anim.start(self.screen.ids.button)
                Clock.unschedule(self.wait_interval)
                self._interval = 0
                self.snackbar = None

        def snackbar_show(self):
            if not self.snackbar:
                self.snackbar = Snackbar(text="This is a snackbar!")
                self.snackbar.show()
                anim = Animation(y=dp(72), d=.2)
                anim.bind(on_complete=lambda *args: Clock.schedule_interval(
                    self.wait_interval, 0))
                anim.start(self.screen.ids.button)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-custom-usage.gif
    :align: center
"""

__all__ = ("Snackbar",)

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ListProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)

from kivymd.uix.button import MDFlatButton
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_string(
    """
#:import get_color_from_hex kivy.utils.get_color_from_hex


<Snackbar>

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
"""
)


class Snackbar(MDFloatLayout):
    text = StringProperty()
    """The text that will appear in the snackbar.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    font_size = NumericProperty("15sp")
    """The font size of the text that will appear in the snackbar.

    :attr:`font_size` is a :class:`~kivy.properties.NumericProperty` and
    defaults to `'15sp'`.
    """

    button_text = StringProperty()
    """The text that will appear in the snackbar's button.

    .. Note::
        If this variable is None, the snackbar will have no button.

    :attr:`button_text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    button_callback = ObjectProperty()
    """The callback that will be triggered when the snackbar's
    button is pressed.

    .. Note::
        If this variable is None, the snackbar will have no button.

    :attr:`button_callback` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    button_color = ListProperty()
    """Button color.

    :attr:`button_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    duration = NumericProperty(3)
    """The amount of time that the snackbar will stay on screen for.

    :attr:`duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `3`.
    """

    padding = NumericProperty("0dp")
    """Snackbar padding.

    :attr:`padding` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `'0dp'`.
    """

    _interval = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.button_text != "":
            button = MDFlatButton(text=self.button_text)
            button.text_color = (
                (1, 1, 1, 1) if not self.button_color else self.button_color
            )
            self.ids.box.add_widget(button)
            if self.button_callback:
                button.bind(on_release=self.button_callback)

    def show(self):
        """Show the snackbar."""

        def wait_interval(interval):
            self._interval += interval
            if self._interval > self.duration:
                anim = Animation(y=-self.ids.box.height, d=0.2)
                anim.bind(
                    on_complete=lambda *args: Window.parent.remove_widget(self)
                )
                anim.start(self.ids.box)
                Clock.unschedule(wait_interval)
                self._interval = 0

        self.size_hint_x = None
        self.width = Window.width - dp(self.padding) * 2
        Window.parent.add_widget(self)
        anim = Animation(y=self.padding, d=0.2)
        anim.bind(
            on_complete=lambda *args: Clock.schedule_interval(wait_interval, 0)
        )
        anim.start(self.ids.box)
