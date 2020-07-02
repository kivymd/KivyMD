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
    FloatLayout:

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
                            text="CANCEL", text_color=self.theme_cls.primary_color
                        ),
                        MDFlatButton(
                            text="DISCARD", text_color=self.theme_cls.primary_color
                        ),
                    ],
                )
            self.dialog.open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/alert-dialog.png
    :align: center
"""

__all__ = ("MDDialog",)

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.modalview import ModalView

from kivymd.material_resources import DEVICE_TYPE
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import BaseButton
from kivymd.uix.card import MDSeparator
from kivymd.uix.list import BaseListItem

Builder.load_string(
    """
#:import images_path kivymd.images_path


<BaseDialog>
    background: '{}/transparent.png'.format(images_path)


<MDDialog>

    MDCard:
        id: container
        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height
        elevation: 12
        md_bg_color: 0, 0, 0, 0
        padding: "24dp", "24dp", "8dp", "8dp"

        canvas:
            Color:
                rgba: root.theme_cls.bg_dark
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: root.radius

        MDLabel:
            id: title
            text: root.title
            font_style: "H6"
            bold: True
            markup: True
            size_hint_y: None
            height: self.texture_size[1]
            valign: "top"

        BoxLayout:
            id: spacer_top_box
            size_hint_y: None
            height: root._spacer_top

        MDLabel:
            id: text
            text: root.text
            font_style: "Body1"
            theme_text_color: "Custom"
            text_color: root.theme_cls.disabled_hint_text_color
            size_hint_y: None
            height: self.texture_size[1]
            markup: True

        ScrollView:
            id: scroll
            size_hint_y: None
            height: root._scroll_height

            MDGridLayout:
                id: box_items
                adaptive_height: True
                cols: 1

        BoxLayout:
            id: spacer_bottom_box
            size_hint_y: None
            height: self.minimum_height

        AnchorLayout:
            id: root_button_box
            size_hint_y: None
            height: "52dp"
            anchor_x: "right"

            MDBoxLayout:
                id: button_box
                adaptive_size: True
                spacing: "8dp"
"""
)


class BaseDialog(ThemableBehavior, ModalView):
    pass


class MDDialog(BaseDialog):
    title = StringProperty()
    """
    Title dialog.

    .. code-block:: python

        self.dialog = MDDialog(
            title="Reset settings?",
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color
                ),
                MDFlatButton(
                    text="ACCEPT", text_color=self.theme_cls.primary_color
                ),
            ],
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-title.png
        :align: center

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    text = StringProperty()
    """
    Text dialog.

    .. code-block:: python

        self.dialog = MDDialog(
            title="Reset settings?",
            text="This will reset your device to its default factory settings.",
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color
                ),
                MDFlatButton(
                    text="ACCEPT", text_color=self.theme_cls.primary_color
                ),
            ],
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-text.png
        :align: center

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    radius = ListProperty([7, 7, 7, 7])
    """
    Dialog corners rounding value.

    .. code-block:: python

        self.dialog = MDDialog(
            text="Oops! Something seems to have gone wrong!",
            radius=[20, 7, 20, 7],
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dialog-radius.png
        :align: center

    :attr:`radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[7, 7, 7, 7]`.
    """

    buttons = ListProperty()
    """
    List of button objects for dialog.
    Objects must be inherited from :class:`~kivymd.uix.button.BaseButton` class.

    .. code-block:: python

        self.dialog = MDDialog(
            text="Discard draft?",
            buttons=[
                MDFlatButton(text="CANCEL"), MDRaisedButton(text="DISCARD"),
            ],
        )

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
    -----------------

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


        FloatLayout:

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
    -----------------------

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


        FloatLayout:

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
                                text="CANCEL", text_color=self.theme_cls.primary_color
                            ),
                            MDFlatButton(
                                text="OK", text_color=self.theme_cls.primary_color
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

    .. code-block::

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


        FloatLayout:

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
                                text="CANCEL", text_color=self.theme_cls.primary_color
                            ),
                            MDFlatButton(
                                text="OK", text_color=self.theme_cls.primary_color
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

    _scroll_height = NumericProperty("28dp")
    _spacer_top = NumericProperty("24dp")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if self.size_hint == [1, 1] and DEVICE_TYPE == "mobile":
            self.size_hint = (None, None)
            self.width = dp(280)
        elif self.size_hint == [1, 1] and DEVICE_TYPE == "desktop":
            self.size_hint = (None, None)
            self.width = dp(560)

        if not self.title:
            self._spacer_top = 0

        if not self.buttons:
            self.ids.root_button_box.height = 0
        else:
            self.create_buttons()

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
                self._spacer_top = self.content_cls.height + dp(24)
                self.ids.spacer_top_box.padding = (0, "24dp", "16dp", 0)
        if self.type == "alert":
            self.ids.scroll.bar_width = 0

    def on_open(self):
        # TODO: Add scrolling text.
        self.height = self.ids.container.height

    def set_normal_height(self):
        self.size_hint_y = 0.8

    def get_normal_height(self):
        return (
            (Window.height * 80 / 100)
            - self._spacer_top
            - dp(52)
            - self.ids.container.padding[1]
            - self.ids.container.padding[-1]
            - 100
        )

    def edit_padding_for_item(self, instance_item):
        instance_item.ids._left_container.x = 0
        instance_item._txt_left_pad = "56dp"

    def create_items(self):
        self.ids.container.remove_widget(self.ids.text)
        height = 0

        for item in self.items:
            if issubclass(item.__class__, BaseListItem):
                height += item.height  # calculate height contents
                self.edit_padding_for_item(item)
                self.ids.box_items.add_widget(item)

        if height > Window.height:
            self.set_normal_height()
            self.ids.scroll.height = self.get_normal_height()
        else:
            self.ids.scroll.height = height

    def create_buttons(self):
        for button in self.buttons:
            if issubclass(button.__class__, BaseButton):
                self.ids.button_box.add_widget(button)
