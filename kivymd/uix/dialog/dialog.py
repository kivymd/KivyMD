"""
Components/Dialog
=================

.. seealso::

    `Material Design spec, Dialogs <https://material.io/components/dialogs>`_


.. rubric:: Dialogs inform users about a task and can contain critical
    information, require decisions, or involve multiple tasks.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialogs.png
    :align: center

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.button import MDFlatButton
    from kivymd.uix.dialog import MDDialog

    KV = '''
    MDFloatLayout:

        MDFlatButton:
            text: "ALERT DIALOG"
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_alert_dialog()
    '''


    class Example(MDApp):
        dialog = None

        def build(self):
            return Builder.load_string(KV)

        def show_alert_dialog(self):
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Discard draft?",
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
                )
            self.dialog.open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/alert-dialog.png
    :align: center
"""

__all__ = ("MDDialog", "BaseDialog")

import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.modalview import ModalView

from kivymd import uix_path
from kivymd.material_resources import DEVICE_TYPE
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import BaseButton
from kivymd.uix.card import MDSeparator
from kivymd.uix.list import BaseListItem

with open(
    os.path.join(uix_path, "dialog", "dialog.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class BaseDialog(ThemableBehavior, ModalView):
    radius = ListProperty([dp(7), dp(7), dp(7), dp(7)])
    """
    Dialog corners rounding value.

    .. code-block:: python

        [...]
            self.dialog = MDDialog(
                text="Oops! Something seems to have gone wrong!",
                radius=[20, 7, 20, 7],
            )
            [...]

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-radius.png
        :align: center

    :attr:`radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[7, 7, 7, 7]`.
    """

    _scale_x = NumericProperty(1)
    _scale_y = NumericProperty(1)


class MDDialog(BaseDialog):
    title = StringProperty()
    """
    Title dialog.

    .. code-block:: python

        [...]
            self.dialog = MDDialog(
                title="Reset settings?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="ACCEPT",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
            [...]

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-title.png
        :align: center

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    text = StringProperty()
    """
    Text dialog.

    .. code-block:: python

        [...]
            self.dialog = MDDialog(
                title="Reset settings?",
                text="This will reset your device to its default factory settings.",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="ACCEPT",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
            [...]

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-text.png
        :align: center

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    buttons = ListProperty()
    """
    List of button objects for dialog.
    Objects must be inherited from :class:`~kivymd.uix.button.BaseButton` class.

    .. code-block:: python

        [...]
            self.dialog = MDDialog(
                text="Discard draft?",
                buttons=[
                    MDFlatButton(text="CANCEL"), MDRaisedButton(text="DISCARD"),
                ],
            )
            [...]

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-buttons.png
        :align: center

    :attr:`buttons` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    items = ListProperty()
    """
    List of items objects for dialog.
    Objects must be inherited from :class:`~kivymd.uix.list.BaseListItem` class.

    With type 'simple'
    ~~~~~~~~~~~~~~~~~~

    .. code-block:: python

        from kivy.lang import Builder
        from kivy.properties import StringProperty

        from kivymd.app import MDApp
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.list import OneLineAvatarListItem

        KV = '''
        <Item>

            ImageLeftWidget:
                source: root.source


        MDFloatLayout:

            MDFlatButton:
                text: "ALERT DIALOG"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_simple_dialog()
        '''


        class Item(OneLineAvatarListItem):
            divider = None
            source = StringProperty()


        class Example(MDApp):
            dialog = None

            def build(self):
                return Builder.load_string(KV)

            def show_simple_dialog(self):
                if not self.dialog:
                    self.dialog = MDDialog(
                        title="Set backup account",
                        type="simple",
                        items=[
                            Item(text="user01@gmail.com", source="user-1.png"),
                            Item(text="user02@gmail.com", source="user-2.png"),
                            Item(text="Add account", source="add-icon.png"),
                        ],
                    )
                self.dialog.open()


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-items.png
        :align: center

    With type 'confirmation'
    ~~~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: python

        from kivy.lang import Builder

        from kivymd.app import MDApp
        from kivymd.uix.button import MDFlatButton
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.list import OneLineAvatarIconListItem

        KV = '''
        <ItemConfirm>
            on_release: root.set_icon(check)

            CheckboxLeftWidget:
                id: check
                group: "check"


        MDFloatLayout:

            MDFlatButton:
                text: "ALERT DIALOG"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_confirmation_dialog()
        '''


        class ItemConfirm(OneLineAvatarIconListItem):
            divider = None

            def set_icon(self, instance_check):
                instance_check.active = True
                check_list = instance_check.get_widgets(instance_check.group)
                for check in check_list:
                    if check != instance_check:
                        check.active = False


        class Example(MDApp):
            dialog = None

            def build(self):
                return Builder.load_string(KV)

            def show_confirmation_dialog(self):
                if not self.dialog:
                    self.dialog = MDDialog(
                        title="Phone ringtone",
                        type="confirmation",
                        items=[
                            ItemConfirm(text="Callisto"),
                            ItemConfirm(text="Luna"),
                            ItemConfirm(text="Night"),
                            ItemConfirm(text="Solo"),
                            ItemConfirm(text="Phobos"),
                            ItemConfirm(text="Diamond"),
                            ItemConfirm(text="Sirena"),
                            ItemConfirm(text="Red music"),
                            ItemConfirm(text="Allergio"),
                            ItemConfirm(text="Magic"),
                            ItemConfirm(text="Tic-tac"),
                        ],
                        buttons=[
                            MDFlatButton(
                                text="CANCEL",
                                theme_text_color="Custom",
                                text_color=self.theme_cls.primary_color,
                            ),
                            MDFlatButton(
                                text="OK",
                                theme_text_color="Custom",
                                text_color=self.theme_cls.primary_color,
                            ),
                        ],
                    )
                self.dialog.open()


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-confirmation.png
        :align: center

    :attr:`items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    width_offset = NumericProperty(dp(48))
    """
    Dialog offset from device width.

    :attr:`width_offset` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(48)`.
    """

    type = OptionProperty(
        "alert", options=["alert", "simple", "confirmation", "custom"]
    )
    """
    Dialog type.
    Available option are `'alert'`, `'simple'`, `'confirmation'`, `'custom'`.

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'alert'`.
    """

    content_cls = ObjectProperty()
    """
    Custom content class.

    .. code-block:: python

        from kivy.lang import Builder
        from kivy.uix.boxlayout import BoxLayout

        from kivymd.app import MDApp
        from kivymd.uix.button import MDFlatButton
        from kivymd.uix.dialog import MDDialog

        KV = '''
        <Content>
            orientation: "vertical"
            spacing: "12dp"
            size_hint_y: None
            height: "120dp"

            MDTextField:
                hint_text: "City"

            MDTextField:
                hint_text: "Street"


        MDFloatLayout:

            MDFlatButton:
                text: "ALERT DIALOG"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_confirmation_dialog()
        '''


        class Content(BoxLayout):
            pass


        class Example(MDApp):
            dialog = None

            def build(self):
                return Builder.load_string(KV)

            def show_confirmation_dialog(self):
                if not self.dialog:
                    self.dialog = MDDialog(
                        title="Address:",
                        type="custom",
                        content_cls=Content(),
                        buttons=[
                            MDFlatButton(
                                text="CANCEL",
                                theme_text_color="Custom",
                                text_color=self.theme_cls.primary_color,
                            ),
                            MDFlatButton(
                                text="OK",
                                theme_text_color="Custom",
                                text_color=self.theme_cls.primary_color,
                            ),
                        ],
                    )
                self.dialog.open()


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-custom.png
        :align: center

    :attr:`content_cls` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `'None'`.
    """

    md_bg_color = ColorProperty(None)
    """
    Background color in the format (r, g, b, a).

    :attr:`md_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _scroll_height = NumericProperty("28dp")
    _spacer_top = NumericProperty("24dp")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self.update_width)

        if self.size_hint == [1, 1] and (
            DEVICE_TYPE == "desktop" or DEVICE_TYPE == "tablet"
        ):
            self.size_hint = (None, None)
            self.width = min(dp(560), Window.width - self.width_offset)
        elif self.size_hint == [1, 1] and DEVICE_TYPE == "mobile":
            self.size_hint = (None, None)
            self.width = min(dp(280), Window.width - self.width_offset)

        if not self.title:
            self._spacer_top = 0

        if not self.buttons:
            self.ids.root_button_box.height = 0
        else:
            self.create_buttons()

        update_height = False
        if self.type in ("simple", "confirmation"):
            if self.type == "confirmation":
                self.ids.spacer_top_box.add_widget(MDSeparator())
                self.ids.spacer_bottom_box.add_widget(MDSeparator())
            self.create_items()
        if self.type == "custom":
            if self.content_cls:
                self.ids.container.remove_widget(self.ids.scroll)
                self.ids.container.remove_widget(self.ids.text)
                self.ids.spacer_top_box.add_widget(self.content_cls)
                self.ids.spacer_top_box.padding = (0, "24dp", "16dp", 0)
                update_height = True
        if self.type == "alert":
            self.ids.scroll.bar_width = 0

        if update_height:
            Clock.schedule_once(self.update_height)

    def update_width(self, *args) -> None:
        self.width = max(
            self.height + self.width_offset,
            min(
                dp(560) if DEVICE_TYPE != "mobile" else dp(280),
                Window.width - self.width_offset,
            ),
        )

    def update_height(self, *args) -> None:
        self._spacer_top = self.content_cls.height + dp(24)

    def update_items(self, items: list) -> None:
        self.ids.box_items.clear_widgets()
        self.items = items
        self.create_items()

    def on_open(self) -> None:
        # TODO: Add scrolling text.
        self.height = self.ids.container.height

    def get_normal_height(self) -> float:
        return (
            (Window.height * 80 / 100)
            - self._spacer_top
            - dp(52)
            - self.ids.container.padding[1]
            - self.ids.container.padding[-1]
            - 100
        )

    def edit_padding_for_item(self, instance_item) -> None:
        instance_item.ids._left_container.x = 0
        instance_item._txt_left_pad = "56dp"

    def create_items(self) -> None:
        if not self.text:
            self.ids.container.remove_widget(self.ids.text)
            height = 0
        else:
            height = self.ids.text.height

        for item in self.items:
            if issubclass(item.__class__, BaseListItem):
                height += item.height  # calculate height contents
                self.edit_padding_for_item(item)
                self.ids.box_items.add_widget(item)

        if height > Window.height:
            self.ids.scroll.height = self.get_normal_height()
        else:
            self.ids.scroll.height = height

    def create_buttons(self) -> None:
        for button in self.buttons:
            if issubclass(button.__class__, BaseButton):
                self.ids.button_box.add_widget(button)
