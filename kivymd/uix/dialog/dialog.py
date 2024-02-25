"""
Components/Dialog
=================

.. seealso::

    `Material Design spec, Dialogs <https://m3.material.io/components/dialogs/overview>`_


.. rubric:: Dialogs provide important prompts in a user flow.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-preview.png
    :align: center

- Use dialogs to make sure users act on information
- Two types: basic and full-screen (full-screen not provided in KivyMD)
- Should be dedicated to completing a single task
- Can also display information relevant to the task
- Commonly used to confirm high-risk actions like deleting progress

Anatomy
=======

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-anatomy.png
    :align: center

Example
=======

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.widget import Widget

    from kivymd.app import MDApp
    from kivymd.uix.button import MDButton, MDButtonText
    from kivymd.uix.dialog import (
        MDDialog,
        MDDialogIcon,
        MDDialogHeadlineText,
        MDDialogSupportingText,
        MDDialogButtonContainer,
        MDDialogContentContainer,
    )
    from kivymd.uix.divider import MDDivider
    from kivymd.uix.list import (
        MDListItem,
        MDListItemLeadingIcon,
        MDListItemSupportingText,
    )

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDButton:
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_alert_dialog()

            MDButtonText:
                text: "Show dialog"
    '''


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def show_alert_dialog(self):
            MDDialog(
                # ----------------------------Icon-----------------------------
                MDDialogIcon(
                    icon="refresh",
                ),
                # -----------------------Headline text-------------------------
                MDDialogHeadlineText(
                    text="Reset settings?",
                ),
                # -----------------------Supporting text-----------------------
                MDDialogSupportingText(
                    text="This will reset your app preferences back to their "
                    "default settings. The following accounts will also "
                    "be signed out:",
                ),
                # -----------------------Custom content------------------------
                MDDialogContentContainer(
                    MDDivider(),
                    MDListItem(
                        MDListItemLeadingIcon(
                            icon="gmail",
                        ),
                        MDListItemSupportingText(
                            text="KivyMD-library@yandex.com",
                        ),
                        theme_bg_color="Custom",
                        md_bg_color=self.theme_cls.transparentColor,
                    ),
                    MDListItem(
                        MDListItemLeadingIcon(
                            icon="gmail",
                        ),
                        MDListItemSupportingText(
                            text="kivydevelopment@gmail.com",
                        ),
                        theme_bg_color="Custom",
                        md_bg_color=self.theme_cls.transparentColor,
                    ),
                    MDDivider(),
                    orientation="vertical",
                ),
                # ---------------------Button container------------------------
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="Cancel"),
                        style="text",
                    ),
                    MDButton(
                        MDButtonText(text="Accept"),
                        style="text",
                    ),
                    spacing="8dp",
                ),
                # -------------------------------------------------------------
            ).open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-example.gif
    :align: center

.. warning:: Do not try to use the MDDialog widget in KV files.

API break
=========

1.2.0 version
-------------

.. code-block:: python

    from kivy.uix.widget import Widget

    from kivymd.app import MDApp
    from kivymd.uix.button import MDFlatButton
    from kivymd.uix.dialog import MDDialog


    class Example(MDApp):
        def build(self):
            return Widget()

        def on_start(self):
            super().on_start()
            MDDialog(
                title="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            ).open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-api-break-1-2-0.png
    :align: center

.. code-block:: python

    from kivy.uix.widget import Widget

    from kivymd.app import MDApp
    from kivymd.uix.button import MDFlatButton
    from kivymd.uix.dialog import MDDialog


    class Example(MDApp):
        def build(self):
            return Widget()

        def on_start(self):
            super().on_start()
            MDDialog(
                title="Discard draft?",
                text="This will reset your device to its default factory settings.",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            ).open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/2-dialog-api-break-1-2-0.png
    :align: center

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty
    from kivy.uix.widget import Widget

    from kivymd import images_path
    from kivymd.app import MDApp
    from kivymd.uix.dialog import MDDialog
    from kivymd.uix.list import OneLineAvatarListItem

    KV = '''
    <Item>

        ImageLeftWidget:
            source: root.source
    '''


    class Item(OneLineAvatarListItem):
        divider = None
        source = StringProperty()


    class Example(MDApp):
        def build(self):
            Builder.load_string(KV)
            return Widget()

        def on_start(self):
            super().on_start()
            MDDialog(
                title="Set backup account",
                type="simple",
                items=[
                    Item(text="user01@gmail.com", source=f"{images_path}/logo/kivymd-icon-128.png"),
                    Item(text="user02@gmail.com", source="data/logo/kivy-icon-128.png"),
                ],
            ).open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/3-dialog-api-break-1-2-0.png
    :align: center

2.2.0 version
-------------

.. code-block:: python

    from kivy.uix.widget import Widget

    from kivymd.uix.widget import MDWidget
    from kivymd.app import MDApp
    from kivymd.uix.button import MDButton, MDButtonText
    from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer


    class Example(MDApp):
        def build(self):
            return MDWidget(md_bg_color=self.theme_cls.backgroundColor)

        def on_start(self):
            super().on_start()
            MDDialog(
                MDDialogHeadlineText(
                    text="Discard draft?",
                    halign="left",
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="Cancel"),
                        style="text",
                    ),
                    MDButton(
                        MDButtonText(text="Discard"),
                        style="text",
                    ),
                    spacing="8dp",
                ),
            ).open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-api-break-2-2-0.png
    :align: center

.. code-block:: python

    from kivy.uix.widget import Widget

    from kivymd.uix.widget import MDWidget
    from kivymd.app import MDApp
    from kivymd.uix.button import MDButton, MDButtonText
    from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer


    class Example(MDApp):
        def build(self):
            return MDWidget(md_bg_color=self.theme_cls.backgroundColor)

        def on_start(self):
            super().on_start()
            MDDialog(
                MDDialogHeadlineText(
                    text="Discard draft?",
                    halign="left",
                ),
                MDDialogSupportingText(
                    text="This will reset your device to its default factory settings.",
                    halign="left",
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="Cancel"),
                        style="text",
                    ),
                    MDButton(
                        MDButtonText(text="Discard"),
                        style="text",
                    ),
                    spacing="8dp",
                ),
            ).open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/2-dialog-api-break-2-2-0.png
    :align: center

.. code-block:: python

    from kivymd import images_path
    from kivymd.uix.widget import MDWidget
    from kivymd.app import MDApp
    from kivymd.uix.dialog import (
        MDDialog,
        MDDialogHeadlineText,
        MDDialogContentContainer,
    )
    from kivymd.uix.list import (
        MDListItem,
        MDListItemLeadingAvatar,
        MDListItemSupportingText,
    )


    class Example(MDApp):
        def build(self):
            return MDWidget(md_bg_color=self.theme_cls.backgroundColor)

        def on_start(self):
            super().on_start()
            MDDialog(
                MDDialogHeadlineText(
                    text="Set backup account",
                    halign="left",
                ),
                MDDialogContentContainer(
                    MDListItem(
                        MDListItemLeadingAvatar(
                            source=f"{images_path}/logo/kivymd-icon-128.png",
                        ),
                        MDListItemSupportingText(
                            text="user01@gmail.com",
                        ),
                        theme_bg_color="Custom",
                        md_bg_color=self.theme_cls.transparentColor,
                    ),
                    MDListItem(
                        MDListItemLeadingAvatar(
                            source="data/logo/kivy-icon-128.png",
                        ),
                        MDListItemSupportingText(
                            text="user01@gmail.com",
                        ),
                        theme_bg_color="Custom",
                        md_bg_color=self.theme_cls.transparentColor,
                    ),
                    orientation="vertical",
                ),
            ).open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/3-dialog-api-break-2-2-0.png
    :align: center

"""

__all__ = [
    "MDDialog",
    "MDDialogIcon",
    "MDDialogHeadlineText",
    "MDDialogSupportingText",
    "MDDialogContentContainer",
    "MDDialogButtonContainer",
]

import os

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    VariableListProperty,
    NumericProperty,
    ColorProperty,
    ObjectProperty,
    BooleanProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivymd.uix.card import MDCard
from kivymd.uix.label import MDIcon, MDLabel
from kivymd import uix_path
from kivymd.material_resources import DEVICE_TYPE
from kivymd.uix.behaviors import MotionDialogBehavior, DeclarativeBehavior

with open(
    os.path.join(uix_path, "dialog", "dialog.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDDialog(MDCard, MotionDialogBehavior):
    """
    Dialog class.

    For more information, see in the
    :class:`~kivymd.uix.card.card.MDCard` and
    :class:`~kivymd.uix.behaviors.motion_behavior.MotionDialogBehavior`
    classes documentation.

    :Events:
        `on_pre_open`:
            Fired before the MDDialog is opened. When this event is fired
            MDDialog is not yet added to window.
        `on_open`:
            Fired when the MDDialog is opened.
        `on_pre_dismiss`:
            Fired before the MDDialog is closed.
        `on_dismiss`:
            Fired when the MDDialog is closed. If the callback returns True,
            the dismiss will be canceled.
    """

    width_offset = NumericProperty(dp(48))
    """
    Dialog offset from device width.

    :attr:`width_offset` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(48)`.
    """

    radius = VariableListProperty(dp(28), lenght=4)
    """
    Dialog corners rounding value.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(28), dp(28), dp(28), dp(28)]`.
    """

    scrim_color = ColorProperty([0, 0, 0, 0.5])
    """
    Color for scrim in (r, g, b, a) or string format.

    :attr:`scrim_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.5]`.
    """

    auto_dismiss = BooleanProperty(True)
    """
    This property determines if the dialog is automatically
    dismissed when the user clicks outside it.

    ..versionadded:: 2.0.0

    :attr:`auto_dismiss` is a :class:`~kivy.properties.BooleanProperty` and
    defaults to True.
    """

    _scrim = ObjectProperty()  # kivymd.uix.dialog.dialog.MDDialogScrim object
    _is_open = False  # is the dialog currently open or closed.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_pre_open")
        self.register_event_type("on_dismiss")
        self.register_event_type("on_pre_dismiss")
        self.opacity = 0
        Window.bind(on_resize=self.update_width)

    def update_width(self, *args) -> None:
        self.size_hint_max_x = max(
            self.width_offset,
            min(
                dp(560) if DEVICE_TYPE != "mobile" else dp(280),
                Window.width - self.width_offset,
            ),
        )

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDDialogIcon):
            self.ids.icon_container.add_widget(widget)
        elif isinstance(widget, MDDialogHeadlineText):
            self.ids.headline_container.add_widget(widget)
        elif isinstance(widget, MDDialogSupportingText):
            self.ids.supporting_text_container.add_widget(widget)
        elif isinstance(widget, MDDialogContentContainer):
            self.ids.content_container.add_widget(widget)
        elif isinstance(widget, MDDialogButtonContainer):
            self.ids.button_container.add_widget(widget)
        else:
            return super().add_widget(widget)

    def open(self) -> None:
        """Show the dialog."""

        if self._is_open:
            return

        self.dispatch("on_pre_open")
        self._is_open = True

        if not self._scrim:
            self._scrim = MDDialogScrim(color=self.scrim_color)

        Window.add_widget(self._scrim)
        Window.add_widget(self)
        super().on_open()
        self.dispatch("on_open")

    def on_pre_open(self, *args) -> None:
        """Fired when a dialog pre opened."""

    def on_open(self, *args) -> None:
        """Fired when a dialog opened."""

    def on_dismiss(self, *args) -> None:
        """Fired when a dialog dismiss."""

    def on_pre_dismiss(self, *args) -> None:
        """Fired when a dialog pre-dismiss."""

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos) and self.auto_dismiss:
            self.dismiss()
            return True
        super().on_touch_down(touch)
        return True

    def dismiss(self, *args) -> None:
        """Closes the dialog."""

        self.dispatch("on_pre_dismiss")
        super().on_dismiss()
        self._is_open = False
        self.dispatch("on_dismiss")


class MDDialogIcon(MDIcon):
    """
    The class implements an icon.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDIcon` class documentation.
    """


class MDDialogHeadlineText(MDLabel):
    """
    The class implements the headline text.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """


class MDDialogSupportingText(MDLabel):
    """
    The class implements the supporting text.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """


class MDDialogContentContainer(DeclarativeBehavior, BoxLayout):
    """
    The class implements the container for custom widgets.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout` classes documentation.
    """


class MDDialogButtonContainer(DeclarativeBehavior, BoxLayout):
    """
    The class implements a container for placing dialog buttons.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout` classes documentation.
    """


class MDDialogScrim(Widget):
    color = ColorProperty(None)
    alpha = NumericProperty(0)
