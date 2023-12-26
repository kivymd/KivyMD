"""
Components/Snackbar
===================

.. seealso::

    `Material Design spec, Snackbars <https://m3.material.io/components/snackbar/overview>`_

.. rubric:: Snackbars provide brief messages about app processes at the bottom
    of the screen.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snackbar.png
    :align: center

- Snackbars shouldn’t interrupt the user’s experience
- Usually appear at the bottom of the UI
- Can disappear on their own or remain on screen until the user takes action

Usage
-----

.. code-block:: python

    MDSnackbar(
        MDSnackbarText(
            text="Text",
        ),
        y=dp(24),
        pos_hint={"center_x": 0.5},
        size_hint_x=0.5,
    ).open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snakbar-anatomy-detail.png
    :align: center

1. Container
2. Supporting text
3. Action (optional)
4. Icon (optional close affordance)

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snakbar-anatomy.png
    :align: center

Configurations
==============

1. Single line
--------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snakbar-configurations-single-line.png
    :align: center

.. code-block:: python

    MDSnackbar(
        MDSnackbarText(
            text="Single-line snackbar",
        ),
        y=dp(24),
        pos_hint={"center_x": 0.5},
        size_hint_x=0.5,
    ).open()


2. Single-line snackbar with action
-----------------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snakbar-configurations-single-line-with-action.png
    :align: center

.. code-block:: python

    MDSnackbar(
        MDSnackbarSupportingText(
            text="Single-line snackbar with action",
        ),
        MDSnackbarButtonContainer(
            MDSnackbarActionButton(
                MDSnackbarActionButtonText(
                    text="Action button"
                ),
            ),
            pos_hint={"center_y": 0.5}
        ),
        y=dp(24),
        orientation="horizontal",
        pos_hint={"center_x": 0.5},
        size_hint_x=0.5,
    ).open()

3. Single-line snackbar with action and close buttons
-----------------------------------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snakbar-configurations-single-line-with-action-and-close-buttons.png
    :align: center

.. code-block:: python

    MDSnackbar(
        MDSnackbarSupportingText(
            text="Single-line snackbar with action and close buttons",
        ),
        MDSnackbarButtonContainer(
            MDSnackbarActionButton(
                MDSnackbarActionButtonText(
                    text="Action button"
                ),
            ),
            MDSnackbarCloseButton(
                icon="close",
            ),
            pos_hint={"center_y": 0.5}
        ),
        y=dp(24),
        orientation="horizontal",
        pos_hint={"center_x": 0.5},
        size_hint_x=0.5,
    ).open()

4. Two-line snackbar with action and close buttons
--------------------------------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snakbar-configurations-two-line-with-action-and-close-buttons.png
    :align: center

.. code-block:: python

    MDSnackbar(
        MDSnackbarText(
            text="Single-line snackbar",
        ),
        MDSnackbarSupportingText(
            text="with action and close buttons",
        ),
        MDSnackbarButtonContainer(
            MDSnackbarActionButton(
                MDSnackbarActionButtonText(
                    text="Action button"
                ),
            ),
            MDSnackbarCloseButton(
                icon="close",
            ),
            pos_hint={"center_y": 0.5}
        ),
        y=dp(24),
        orientation="horizontal",
        pos_hint={"center_x": 0.5},
        size_hint_x=0.5,
    ).open()

5. Two-line snackbar with action and close buttons at the bottom
----------------------------------------------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/snakbar-configurations-two-line-with-action-and-close-buttons-bottom.png
    :align: center

.. code-block:: python

    MDSnackbar(
        MDSnackbarText(
            text="Single-line snackbar with action",
        ),
        MDSnackbarSupportingText(
            text="and close buttons at the bottom",
            padding=[0, 0, 0, dp(56)],
        ),
        MDSnackbarButtonContainer(
            Widget(),
            MDSnackbarActionButton(
                MDSnackbarActionButtonText(
                    text="Action button"
                ),
            ),
            MDSnackbarCloseButton(
                icon="close",
            ),
        ),
        y=dp(124),
        pos_hint={"center_x": 0.5},
        size_hint_x=0.5,
        padding=[0, 0, "8dp", "8dp"],
    ).open()

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

2.0.0 version
-------------

.. code-block:: python

    MDSnackbar(
        MDSnackbarSupportingText(
            text="Single-line snackbar with action",
        ),
        MDSnackbarButtonContainer(
            MDSnackbarActionButton(
                MDSnackbarActionButtonText(
                    text="Action button"
                ),
            ),
            pos_hint={"center_y": 0.5}
        ),
        y=dp(24),
        orientation="horizontal",
        pos_hint={"center_x": 0.5},
        size_hint_x=0.5,
        background_color=self.theme_cls.onPrimaryContainerColor,
    ).open()
"""

__all__ = (
    "MDSnackbar",
    "MDSnackbarText",
    "MDSnackbarSupportingText",
    "MDSnackbarButtonContainer",
    "MDSnackbarActionButton",
    "MDSnackbarActionButtonText",
    "MDSnackbarCloseButton",
)

import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    ColorProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.uix.behaviors import MotionShackBehavior, DeclarativeBehavior
from kivymd.uix.button import MDButton, MDIconButton, MDButtonText
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

with open(
    os.path.join(uix_path, "snackbar", "snackbar.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSnackbarButtonContainer(DeclarativeBehavior, BoxLayout):
    """
    The class implements a container for placing snackbar buttons.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout` classes documentation.
    """

    def add_widget(self, widget, *args, **kwargs):
        def set_container_width(w):
            self.parent.width += w.width

        if isinstance(
            widget, (MDSnackbarActionButton, MDSnackbarCloseButton, Widget)
        ):
            Clock.schedule_once(lambda x: set_container_width(widget), 0.2)

        return super().add_widget(widget)


class MDSnackbarCloseButton(MDIconButton):
    """
    Snackbar closed button class.

    For more information, see in the
    :class:`~kivymd.uix.button.button.MDIconButton` class documentation.
    """


class MDSnackbarActionButtonText(MDButtonText):
    """
    The class implements the text for the :class:`~MDSnackbarActionButton`
    class.

    .. versionchanged:: 2.2.0

    For more information, see in the
    :class:`~kivymd.uix.button.button.MDButtonText` class documentation.
    """


class MDSnackbarActionButton(MDButton):
    """
    Snackbar action button class.

    For more information, see in the
    :class:`~kivymd.uix.button.button.MDButton` class documentation.
    """


class MDSnackbar(MotionShackBehavior, MDCard):
    """
    Snackbar class.

    .. versionchanged:: 1.2.0
        Rename `BaseSnackbar` to `MDSnackbar` class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.motion_behavior.MotionShackBehavior` and
    :class:`~kivymd.uix.card.card.MDCard` and
    class documentation.

    :Events:
        :attr:`on_open`
            Fired when a snackbar opened.
        :attr:`on_dismiss`
            Fired when a snackbar closes.
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

    radius = ListProperty([dp(4), dp(4), dp(4), dp(4)])
    """
    Snackbar radius.

    :attr:`radius` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(4), dp(4), dp(4), dp(4)]`
    """

    background_color = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the snackbar.

    :attr:`background_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
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

        Window.add_widget(self)
        super().on_open()

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, (MDSnackbarText, MDSnackbarSupportingText)):
            self.ids.label_container.add_widget(widget)
        elif isinstance(widget, MDSnackbarButtonContainer):
            self.ids.button_container.size_hint_x = (
                1 if self.orientation == "vertical" else None
            )
            self.ids.button_container.add_widget(widget)
        else:
            return super().add_widget(widget)

    def on_open(self, *args) -> None:
        """Fired when a snackbar opened."""

    def on_dismiss(self, *args) -> None:
        """Fired when a snackbar closed."""


class MDSnackbarText(MDLabel):
    """
    The class implements the text.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """


class MDSnackbarSupportingText(MDLabel):
    """
    The class implements the supporting text.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """
