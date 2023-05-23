"""
Components/Snackbar
===================

.. seealso::

    `Material Design spec, Snackbars <https://m3.material.io/components/snackbar/overview>`_

.. rubric:: Snackbars provide brief messages about app processes at the bottom
    of the screen.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar.png
    :align: center

Usage
-----

.. code-block:: python

    MDSnackbar(
        MDLabel(
            text="First string",
            theme_text_color="Custom",
            text_color="#393231",
        ),
    ).open()

Example
-------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel
    from kivymd.uix.snackbar import MDSnackbar


    KV = '''
    MDScreen:

        MDRaisedButton:
            text: "Create simple snackbar"
            on_release: app.open_snackbar()
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Example(MDApp):
        def open_snackbar(self):
            MDSnackbar(
                MDLabel(
                    text="First string",
                ),
            ).open()

        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-simple.gif
    :align: center

Control width and pos
---------------------

.. code-block:: python

    MDSnackbar(
        MDLabel(
            text="First string",
        ),
        pos=(dp(24), dp(56)),
        size_hint_x=0.5,
    ).open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-widith-and-pos.gif
    :align: center

On mobile, use up to two lines of text to communicate the snackbar message:

.. code-block:: python

    MDSnackbar(
        MDLabel(
            text="First string",
            theme_text_color="Custom",
            text_color="#393231",
        ),
        MDLabel(
            text="Second string",
            theme_text_color="Custom",
            text_color="#393231",
        ),
        y=dp(24),
        pos_hint={"center_x": 0.5},
        size_hint_x=0.5,
        md_bg_color="#E8D8D7",
    ).open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-two-line.gif
    :align: center

Usage action button
-------------------

A snackbar can contain a single action. "Dismiss" or "cancel" actions are
optional:

.. code-block:: python

    MDSnackbar(
        MDLabel(
            text="First string",
            theme_text_color="Custom",
            text_color="#393231",
        ),
        MDSnackbarActionButton(
            text="Done",
            theme_text_color="Custom",
            text_color="#8E353C",
        ),
        y=dp(24),
        pos_hint={"center_x": 0.5},
        size_hint_x=0.5,
        md_bg_color="#E8D8D7",
    ).open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-action-button.gif
    :align: center

Callback action button
----------------------

.. code-block:: python

    def snackbar_action_button_callback(self, *args):
        print("Snackbar callback action button")

    def open_snackbar(self):
        self.snackbar = MDSnackbar(
            MDLabel(
                text="First string",
                theme_text_color="Custom",
                text_color="#393231",
            ),
            MDSnackbarActionButton(
                text="Done",
                theme_text_color="Custom",
                text_color="#8E353C",
                _no_ripple_effect=True,
                on_release=self.snackbar_action_button_callback,
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            md_bg_color="#E8D8D7",
        )
        self.snackbar.open()

If an action is long, it can be displayed on a third line:

.. code-block:: python

    MDSnackbar(
        MDLabel(
            text="If an action is long, it can be displayed",
            theme_text_color="Custom",
            text_color="#393231",
        ),
        MDLabel(
            text="on a third line.",
            theme_text_color="Custom",
            text_color="#393231",
        ),
        MDLabel(
            text=" ",
        ),
        MDSnackbarActionButton(
            text="Action button",
            theme_text_color="Custom",
            text_color="#8E353C",
            y=dp(8),
            _no_ripple_effect=True,
        ),
        y=dp(24),
        pos_hint={"center_x": 0.5},
        size_hint_x=0.5,
        md_bg_color="#E8D8D7",
    ).open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-action-button-on-thrid-line.gif
    :align: center

Icon (optional close affordance):

.. code-block:: python

    def snackbar_close(self, *args):
        self.snackbar.dismiss()

    def open_snackbar(self):
        self.snackbar = MDSnackbar(
            MDLabel(
                text="Icon (optional close affordance)",
                theme_text_color="Custom",
                text_color="#393231",
            ),
            MDSnackbarActionButton(
                text="Action button",
                theme_text_color="Custom",
                text_color="#8E353C",
                _no_ripple_effect=True,
            ),
            MDSnackbarCloseButton(
                icon="close",
                theme_text_color="Custom",
                text_color="#8E353C",
                _no_ripple_effect=True,
                on_release=self.snackbar_close,
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            md_bg_color="#E8D8D7",
        )
        self.snackbar.open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar-optional-close-affordance.gif
    :align: center

API break
=========

1.1.1 version
-------------

.. code-block:: python

    snackbar = Snackbar(
        text="First string",
        snackbar_x="10dp",
        snackbar_y="24dp",
    )
    snackbar.size_hint_x = (
        Window.width - (snackbar.snackbar_x * 2)
    ) / Window.width
    snackbar.buttons = [
        MDFlatButton(
            text="Done",
            theme_text_color="Custom",
            text_color="#8E353C",
            on_release=snackbar.dismiss,
        ),
    ]
    snackbar.open()

1.2.0 version
-------------

.. code-block:: python

    MDSnackbar(
        MDLabel(
            text="First string",
        ),
        MDSnackbarActionButton(
            text="Done",
            theme_text_color="Custom",
            text_color="#8E353C",
        ),
        y=dp(24),
        pos_hint={"center_x": 0.5},
        size_hint_x=0.5,
        md_bg_color="#E8D8D7",
    ).open()
"""

__all__ = (
    "MDSnackbar",
    "MDSnackbarActionButton",
    "MDSnackbarCloseButton",
)

import os

from kivy import Logger
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
from kivymd.uix.behaviors import MotionShackBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout

with open(
    os.path.join(uix_path, "snackbar", "snackbar.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class SnackbarLabelContainer(MDBoxLayout):
    """Container for placing snackbar text."""


class SnackbarActionButtonContainer(MDRelativeLayout):
    """Container for placing snackbar action button."""


class SnackbarCloseButtonContainer(MDRelativeLayout):
    """Container for placing snackbar close button."""


class MDSnackbarCloseButton(MDIconButton):
    """
    Snackbar closed button class.

    For more information, see in the
    :class:`~kivymd.uix.button.MDIconButton` class documentation.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.y and not self.pos_hint:
            self.pos_hint = {"center_y": 0.5}


class MDSnackbarActionButton(MDFlatButton):
    """
    Snackbar action button class.

    For more information, see in the
    :class:`~kivymd.uix.button.MDFlatButton` class documentation.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.y and not self.pos_hint:
            self.pos_hint = {"center_y": 0.5}


class MDSnackbar(MotionShackBehavior, MDCard):
    """
    Snackbar class.

    .. versionchanged:: 1.2.0
        Rename `BaseSnackbar` to `MDSnackbar` class.

    For more information, see in the
    :class:`~kivymd.uix.card.MDCard` and
    :class:`~kivymd.uix.behaviors.StencilBehavior`
    class documentation.

    :Events:
        :attr:`on_open`
            Called when a snackbar opened.
        :attr:`on_dismiss`
            Called when a snackbar closes.
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
    and defaults to `True`.
    """

    radius = ListProperty([5, 5, 5, 5])
    """
    Snackbar radius.

    :attr:`radius` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[5, 5, 5, 5]`
    """

    bg_color = ColorProperty(None, deprecated=True)
    """
    Snackbar background color in (r, g, b, a) or string format.

    .. deprecated:: 1.2.0
        Use 'md_bg_color` instead.

    :attr:`bg_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    buttons = ListProperty(deprecated=True)
    """
    Snackbar buttons.

    .. deprecated:: 1.2.0

    :attr:`buttons` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`
    """

    snackbar_animation_dir = OptionProperty(
        "Bottom",
        options=["Top", "Bottom", "Left", "Right"],
        deprecated=True,
    )
    """
    Snackbar animation direction.
    Available options are: `'Top'`, `'Bottom'`, `'Left'`, `'Right'`.

    .. deprecated:: 1.2.0

    :attr:`snackbar_animation_dir` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Bottom'`.
    """

    snackbar_x = NumericProperty(0, deprecated=True)
    """
    The snackbar x position in the screen

    .. deprecated:: 1.2.0

    :attr:`snackbar_x` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    snackbar_y = NumericProperty(0, deprecated=True)
    """
    The snackbar x position in the screen

    .. deprecated:: 1.2.0

    :attr:`snackbar_y` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_dismiss")
        self.opacity = 0

    def dismiss(self, *args) -> None:
        """Dismiss the snackbar."""

        super().on_dismiss()

    def open(self) -> None:
        """Show the snackbar."""

        for widget in Window.parent.children:
            if widget.__class__ is MDSnackbar:
                return

        Window.parent.add_widget(self)
        super().on_open()

    def add_widget(self, widget, *args, **kwargs):
        def check_color(color):
            if not widget.text_color:
                widget.theme_text_color = "Custom"
                widget.text_color = color

        if isinstance(widget, MDSnackbarCloseButton):
            widget.icon_size = "20sp"
            check_color("white")
            self.ids.close_container.add_widget(widget)
            if len(self.ids.close_container.children) >= 2:
                Logger.warning(
                    "KivyMD: "
                    "Do not use more than one button to close the snackbar. "
                    "This is contrary to the material design rules "
                    "of version 3"
                )
        if isinstance(widget, MDSnackbarActionButton):
            self.ids.action_container.add_widget(widget)
            check_color(self.theme_cls.primary_color)
            if len(self.ids.action_container.children) >= 2:
                Logger.warning(
                    "KivyMD: "
                    "Do not use more than one action button. "
                    "This is contrary to the material design rules "
                    "of version 3"
                )
        if isinstance(widget, MDLabel):
            widget.adaptive_height = True
            widget.pos_hint = {"center_y": 0.5}
            check_color("white")
            self.ids.label_container.add_widget(widget)
            if len(self.ids.label_container.children) >= 4:
                Logger.warning(
                    "KivyMD: "
                    "Do not use more than three lines in the snackbar. "
                    "This is contrary to the material design rules "
                    "of version 3"
                )
        elif isinstance(
            widget,
            (
                SnackbarLabelContainer,
                SnackbarActionButtonContainer,
                SnackbarCloseButtonContainer,
            ),
        ):
            return super().add_widget(widget)

    def on_open(self, *args) -> None:
        """Called when a snackbar opened."""

    def on_dismiss(self, *args) -> None:
        """Called when a snackbar closed."""


class Snackbar(MDSnackbar):
    """
    .. deprecated:: 1.2.0
        Use :class:`~kivymd.uix.snackbar.MDSnackbar`
        class instead.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Logger.warning(
            "KivyMD: "
            "The `Snackbar` class has been deprecated. "
            "Use the `MDSnackbar` class instead."
        )
