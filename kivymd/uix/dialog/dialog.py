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

.. tabs::

    .. tab:: Declarative python style with KV

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

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.dialog import (
                MDDialog,
                MDDialogIcon,
                MDDialogHeadlineText,
                MDDialogSupportingText,
                MDDialogContentContainer,
                MDDialogButtonContainer,
            )
            from kivymd.uix.divider import MDDivider
            from kivymd.uix.list import (
                MDListItem, MDListItemSupportingText, MDListItemLeadingIcon
            )
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.widget import MDWidget


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return (
                        MDScreen(
                            MDButton(
                                MDButtonText(
                                    text="Show dialog"
                                ),
                                id="button",
                                pos_hint={'center_x': .5, 'center_y': 0.5},
                                on_release=self.show_alert_dialog,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )

                def show_alert_dialog(self, *args):
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
                            MDWidget(),
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

iOS liquid glass dialog
=======================

.. tabs::

    .. tab:: Imperative Python Style

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import StringProperty, ColorProperty

            from kivymd.app import MDApp
            from kivymd.uix.dialog import (
                IOSDialog,
                IOSDialogButtonContainer,
                IOSDialogMessage,
                IOSDialogTitle,
                IOSDialogButton,
            )


            KV = '''
            <CommonIOSDialogButton>

                IOSDialogButtonText:
                    text: root.text
                    theme_text_color: "Custom"
                    text_color: root.color


            MDScreen:

                FitImage:
                    id: bg_image
                    source: "https://picsum.photos/800/600?random=2"

                IOSButton:
                    target_background: bg_image
                    pos_hint: {"center_x": .5, "center_y": .5}
                    border_radius: [dp(22)] * 4
                    on_release: app.show_dialog()

                    IOSButtonText:
                        text: "Open iOS Dialog"
            '''


            class CommonIOSDialogButton(IOSDialogButton):
                text = StringProperty()
                color = ColorProperty("white")


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)

                def show_dialog(self, *args):
                    dialog = IOSDialog(target_background=self.root)
                    dialog.add_widget(IOSDialogTitle(text="Delete application?", bold=True))
                    dialog.add_widget(
                        IOSDialogMessage(
                            text=(
                                "This will also result in the deletion of all data "
                                "associated with it."
                            )
                        )
                    )

                    button_container = IOSDialogButtonContainer(orientation="vertical")

                    cancel_btn = CommonIOSDialogButton(text="Cancel")
                    cancel_btn.bind(on_release=lambda x: dialog.dismiss())

                    delete_btn = CommonIOSDialogButton(text="Delete", color="red")
                    delete_btn.bind(on_release=lambda x: dialog.dismiss())

                    button_container.add_widget(cancel_btn)
                    button_container.add_widget(delete_btn)

                    dialog.add_widget(button_container)
                    dialog.open()


            if __name__ == "__main__":
                Example().run()

    .. tab:: Declarative Python Style

        .. code-block:: python

            from kivy.metrics import dp
            from kivy.properties import StringProperty, ColorProperty

            from kivymd.app import MDApp
            from kivymd.uix.button import IOSButton, IOSButtonText
            from kivymd.uix.dialog import (
                IOSDialog,
                IOSDialogButtonContainer,
                IOSDialogMessage,
                IOSDialogTitle,
                IOSDialogButton,
                IOSDialogButtonText,
            )
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.screen import MDScreen

            class CommonIOSDialogButton(IOSDialogButton):
                text = StringProperty()
                color = ColorProperty("white")

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.widgets = [
                        IOSDialogButtonText(
                            text=self.text,
                            theme_text_color="Custom",
                            text_color=self.color,
                        )
                    ]


            class Example(MDApp):
                dialog = IOSDialog

                def build(self):
                    image = FitImage(source="https://picsum.photos/800/600?random=2")

                    return (
                        MDScreen(
                            image,
                            IOSButton(
                                IOSButtonText(
                                    text="Open iOS Dialog",
                                ),
                                target_background=image,
                                pos_hint={"center_x": .5, "center_y": .5},
                                border_radius=[dp(22)] * 4,
                                on_release=lambda x: self.show_dialog(),
                            )
                        )
                    )

                def dialog_dismiss(self, *args):
                    self.dialog.dismiss()

                def show_dialog(self, *args):
                    self.dialog = IOSDialog(
                        IOSDialogTitle(
                            text="Delete application?",
                            bold=True,
                        ),
                        IOSDialogMessage(
                            text=(
                                "This will also result in the deletion of all data "
                                "associated with it."
                            )
                        ),
                        IOSDialogButtonContainer(
                            CommonIOSDialogButton(
                                text="Cancel",
                                on_release=lambda x: self.dialog_dismiss(),
                            ),
                            CommonIOSDialogButton(
                                text="Delete",
                                color="red",
                                on_release=lambda x: self.dialog_dismiss(),
                            ),
                            orientation="vertical",
                        ),
                        target_background=self.root,
                    )
                    self.dialog.open()


            if __name__ == "__main__":
                Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-dialog-example.gif
    :align: center

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

2.0.0 version
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
    # MD
    "MDDialog",
    "MDDialogIcon",
    "MDDialogHeadlineText",
    "MDDialogSupportingText",
    "MDDialogContentContainer",
    "MDDialogButtonContainer",
    # IOS
    "IOSDialog",
    "IOSDialogButton",
    "IOSDialogButtonText",
    "IOSDialogTitle",
    "IOSDialogMessage",
    "IOSDialogContentContainer",
    "IOSDialogButtonContainer",
]

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.uix.behaviors import (
    DeclarativeBehavior,
    IOSButtonBehavior,
    IOSGlassBehavior,
    MotionDialogBehavior,
    ScaleBehavior,
    StencilBehavior,
)
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDIcon, MDLabel

with open(
    os.path.join(uix_path, "dialog", "dialog.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class BaseDialog:
    def on_pre_open(self, *args) -> None:
        """Fired when a dialog pre opened."""

    def on_open(self, *args) -> None:
        """Fired when a dialog opened."""

    def on_dismiss(self, *args) -> None:
        """Fired when a dialog dismiss."""

    def on_pre_dismiss(self, *args) -> None:
        """Fired when a dialog pre-dismiss."""


# ----------------------------------- MD ----------------------------------


class MDDialog(MDCard, MotionDialogBehavior, BaseDialog):
    """
    Dialog class.

    For more information, see in the
    :class:`~kivymd.uix.card.card.MDCard` and
    :class:`~kivymd.uix.behaviors.motion_behavior.MotionDialogBehavior`
    :class:`~BaseDialog`
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

    .. versionadded:: 2.0.0

    :attr:`auto_dismiss` is a :class:`~kivy.properties.BooleanProperty` and
    defaults to True.
    """

    _scrim = ObjectProperty()  # kivymd.uix.dialog.dialog.MDDialogScrim object
    _is_open = False  # is the dialog currently open or closed.

    __events__ = ("on_open", "on_pre_open", "on_dismiss", "on_pre_dismiss")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.opacity = 0
        self.update_width()
        Window.bind(on_resize=self.update_width)

    def update_width(self, *args) -> None:
        """Fired when the application window is resized."""

        side_padding = dp(24)
        ideal_width = dp(560)
        min_width = dp(240)
        max_width = Window.width - side_padding * 2

        if max_width < min_width:
            self.width = min_width
            return

        self.width = min(ideal_width, max_width)

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

    def set_properties_widget(self) -> None:
        """Fired `on_release/on_press/on_enter/on_leave` events."""

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


class MDDialogSpacer(Widget):
    pass


# ---------------------------------- IOS ----------------------------------


class IOSDialog(
    DeclarativeBehavior,
    IOSGlassBehavior,
    IOSButtonBehavior,
    ScaleBehavior,
    StencilBehavior,
    BaseDialog,
    FloatLayout,
):
    """
    iOS style dialog class.

    .. versionadded:: 2.0.1

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and,
    :class:`~kivymd.uix.behaviors.ios.glass_behavior.IOSGlassBehavior` and,
    :class:`~kivymd.uix.behaviors.ios.button_behavior.IOSButtonBehavior` and,
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and,
    :class:`~kivymd.uix.behaviors.stencil_behavior.StencilBehavior` and,
    :class:`~BaseDialog`, and
    :class:`~kivy.uix.floatlayout.FloatLayout`
    classes documentation.

    :Events:
        `on_pre_open`:
            Fired before the IOSDialog is opened. When this event is fired
            IOSDialog is not yet added to window.
        `on_open`:
            Fired when the IOSDialog is opened.
        `on_pre_dismiss`:
            Fired before the IOSDialog is closed.
        `on_dismiss`:
            Fired when the IOSDialog is closed. If the callback returns True,
            the dismiss will be canceled.
    """

    radius = VariableListProperty([dp(18)] * 4)
    """
    Dialog corners rounding value.

    :attr:`radius` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(18), dp(18), dp(18), dp(18)]`.
    """

    scrim_color = ColorProperty([0, 0, 0, 0.4])
    """
    Color for scrim in (r, g, b, a) format.

    :attr:`scrim_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.4]`.
    """

    auto_dismiss = BooleanProperty(True)
    """
    This property determines if the dialog is automatically
    dismissed when the user clicks outside it.

    :attr:`auto_dismiss` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    show_transition = StringProperty("easing_standard")
    """
    Animation transition type for dialog open.

    :attr:`show_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'easing_standard'`.
    """

    show_duration = NumericProperty(0.2)
    """
    Animation duration for dialog open in seconds.

    :attr:`show_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    hide_transition = StringProperty("easing_accelerated")
    """
    Animation transition type for dialog close.

    :attr:`hide_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'easing_accelerated'`.
    """

    hide_duration = NumericProperty(0.15)
    """
    Animation duration for dialog close in seconds.

    :attr:`hide_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.15`.
    """

    lens_power = NumericProperty(0.01)
    """
    Magnification power at the center of the lens.

    :attr:`lens_power` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.08`.
    """

    bevel_power = NumericProperty(0.05)
    """
    Light refraction power at the bevel/edges.

    :attr:`bevel_power` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.15`.
    """

    _scrim = ObjectProperty(None)
    _is_open = BooleanProperty(False)
    __events__ = ("on_open", "on_pre_open", "on_dismiss", "on_pre_dismiss")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.opacity = 0
        self.pos_hint = {}
        self.bind(size=self._recenter)
        Window.bind(size=self._on_window_resize)

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, IOSDialogTitle):
            self.ids.title_container.add_widget(widget)
        elif isinstance(widget, IOSDialogMessage):
            self.ids.message_container.add_widget(widget)
        elif isinstance(widget, IOSDialogContentContainer):
            self.ids.custom_content_container.add_widget(widget)
        elif isinstance(widget, IOSDialogButtonContainer):
            self.ids.button_container.add_widget(widget)
        elif isinstance(widget, IOSDialogButton):
            self.ids.button_container.add_widget(widget)
        else:
            super().add_widget(widget, *args, **kwargs)

    def open(self) -> None:
        """Show the dialog."""

        if self._is_open:
            return

        self.dispatch("on_pre_open")
        self._is_open = True

        if not self._scrim:
            self._scrim = IOSDialogScrim(color=self.scrim_color)

        if self.parent:
            self.parent.remove_widget(self)

        Window.add_widget(self._scrim)
        Window.add_widget(self)

        Clock.unschedule(self._setup_glass_fbo)
        self._setup_glass_fbo()

        self.opacity = 0
        self.scale_value_y = 0.85
        self.scale_value_x = 0.85

        Clock.schedule_once(self._start_open_animation, 0)
        self.dispatch("on_open")

    def dismiss(self, *args) -> None:
        """Closes the dialog."""

        if not self._is_open:
            return

        self.dispatch("on_pre_dismiss")

        def remove_dialog(*args):
            Window.unbind(size=self._on_window_resize)
            Window.remove_widget(self)

            if self._scrim and self._scrim.parent:
                Window.remove_widget(self._scrim)

        if self._scrim:
            Animation(alpha=0, d=self.hide_duration).start(self._scrim)

        anim = Animation(
            opacity=0,
            scale_value_y=0.85,
            scale_value_x=0.85,
            t=self.hide_transition,
            d=self.hide_duration,
        )
        anim.bind(on_complete=remove_dialog)
        anim.start(self)

        self._is_open = False
        self.dispatch("on_dismiss")

    def on_touch_down(self, touch):
        if not self._is_open:
            return super().on_touch_down(touch)

        if self.collide_point(*touch.pos):
            super().on_touch_down(touch)

            return True

        if self.auto_dismiss:
            self.dismiss()

        return True

    def on_touch_move(self, touch):
        if self._is_open:
            super().on_touch_move(touch)

            return True

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self._is_open:
            super().on_touch_up(touch)

            return True

        return super().on_touch_up(touch)

    def _start_open_animation(self, dt):
        if hasattr(self, "_setup_glass_fbo"):
            self._setup_glass_fbo()

        anim = Animation(
            opacity=1,
            scale_value_y=1,
            scale_value_x=1,
            t=self.show_transition,
            d=self.show_duration,
        )
        anim.start(self)

        if self._scrim:
            Animation(alpha=1, d=self.show_duration).start(self._scrim)

    def _recenter(self, *args):
        self.pos_hint = {}
        self.pos = (
            round((Window.width - self.width) / 2),
            round((Window.height - self.height) / 2),
        )
        self.scale_value_center = self.center

    def _on_window_resize(self, *args):
        if self._scrim:
            self._scrim.size = Window.size
        self._recenter()


class IOSDialogScrim(Widget):
    """
    iOS dialog scrim class.

    .. versionadded:: 2.0.1

    For more information, see in the
    :class:`~kivy.uix.widget.Widget` class documentation.
    """

    color = ColorProperty([0, 0, 0, 0.4])
    """
    Color for scrim in (r, g, b, a) format.

    :attr:`color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.4]`.
    """

    alpha = NumericProperty(1)
    """
    Scrim transparency value.

    :attr:`alpha` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """


class IOSDialogTitle(MDLabel):
    """
    iOS dialog title class.

    .. versionadded:: 2.0.1

    For more information, see in the
    :class:`~kivymd.uix.label.MDLabel` class documentation.
    """


class IOSDialogMessage(MDLabel):
    """
    iOS dialog message class.

    .. versionadded:: 2.0.1

    For more information, see in the
    :class:`~kivymd.uix.label.MDLabel` class documentation.
    """


class IOSDialogContentContainer(DeclarativeBehavior, BoxLayout):
    """
    iOS custom content container.

    .. versionadded:: 2.0.1

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout` classes documentation.
    """


class IOSDialogButtonContainer(DeclarativeBehavior, BoxLayout):
    """
    iOS custom button container class.

    .. versionadded:: 2.0.1

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout` classes documentation.
    """


class IOSDialogButton(MDButton):
    """
    iOS dialog button class.

    .. versionadded:: 2.0.1

    For more information, see in the
    :class:`~kivymd.uix.button.MDButton` class documentation.
    """


class IOSDialogButtonText(MDButtonText):
    """
    iOS dialog button text class.

    .. versionadded:: 2.0.1

    For more information, see in the
    :class:`~kivymd.uix.button.MDButtonText` class documentation.
    """
