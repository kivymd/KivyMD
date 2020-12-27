import os

from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from libs.baseclass.list_items import KitchenSinkOneLineLeftAvatarItem

from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem


class KitchenSinkDialogsCustomContent(BoxLayout):
    pass


class KitchenSinkItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False


class KitchenSinkDialogs(ThemableBehavior, Screen):
    app = ObjectProperty()
    simple_dialog = None
    alert_dialog = None
    custom_dialog = None
    confirmation_dialog = None

    def show_example_confirmation_dialog(self):
        if not self.confirmation_dialog:
            self.confirmation_dialog = MDDialog(
                title="Phone ringtone",
                type="confirmation",
                items=[
                    KitchenSinkItemConfirm(text=i)
                    for i in [
                        "Callisto",
                        "Luna",
                        "Night",
                        "Solo",
                        "Phobos",
                        "Diamond",
                        "Sirena",
                        "Red music",
                        "Allergio",
                        "Magic",
                        "Tic-tac",
                    ]
                ],
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        text_color=self.app.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.app.theme_cls.primary_color
                    ),
                ],
            )
        self.confirmation_dialog.md_bg_color = self.theme_cls.bg_dark
        self.confirmation_dialog.open()

    def show_example_simple_dialog(self):
        if not self.simple_dialog:
            self.simple_dialog = MDDialog(
                title="Set backup account",
                type="simple",
                items=[
                    KitchenSinkOneLineLeftAvatarItem(
                        text="user01@gmail.com",
                        source=f"{os.environ['KITCHEN_SINK_ASSETS']}heattheatr.png",
                    ),
                    KitchenSinkOneLineLeftAvatarItem(
                        text="user02@gmail.com",
                        source=f"{os.environ['KITCHEN_SINK_ASSETS']}artemsbulgakov.png",
                    ),
                    KitchenSinkOneLineLeftAvatarItem(
                        text="Add account",
                        source=f"{os.environ['KITCHEN_SINK_ASSETS']}twitter-round.png",
                    ),
                ],
            )
        self.simple_dialog.md_bg_color = self.theme_cls.bg_dark
        self.simple_dialog.open()

    def show_example_custom_dialog(self):
        if not self.custom_dialog:
            self.custom_dialog = MDDialog(
                title="Address:",
                type="custom",
                content_cls=KitchenSinkDialogsCustomContent(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        text_color=self.app.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.app.theme_cls.primary_color
                    ),
                ],
            )
        self.custom_dialog.md_bg_color = self.theme_cls.bg_dark
        self.custom_dialog.open()

    def show_example_alert_dialog(self):
        if not self.alert_dialog:
            self.alert_dialog = MDDialog(
                title="Reset settings?",
                text="This will reset your device to its default factory settings.",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        text_color=self.app.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="ACCEPT",
                        text_color=self.app.theme_cls.primary_color,
                    ),
                ],
            )
        self.alert_dialog.md_bg_color = self.theme_cls.bg_dark
        self.alert_dialog.open()
