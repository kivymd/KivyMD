import os

from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from libs.baseclass.list_items import KitchenSinkOneLineLeftIconItem

from kivymd.icon_definitions import md_icons
from kivymd.toast import toast
from kivymd.uix.bottomsheet import (
    MDCustomBottomSheet,
    MDGridBottomSheet,
    MDListBottomSheet,
)


class KitchenSinkBottomSheet(Screen):
    def show_example_bottom_sheet(self):

        bs_menu_1 = MDListBottomSheet()
        bs_menu_1.add_item(
            "Here's an item with text only",
            lambda x: self.callback_for_menu_items(
                "Here's an item with text only"
            ),
        )
        bs_menu_1.add_item(
            "Here's an item with an icon",
            lambda x: self.callback_for_menu_items(
                "Here's an item with an icon"
            ),
            icon="clipboard-account",
        )
        bs_menu_1.add_item(
            "Here's another!",
            lambda x: self.callback_for_menu_items("Here's another!"),
            icon="nfc",
        )
        bs_menu_1.open()

    def show_example_grid_bottom_sheet(self):

        bs_menu = MDGridBottomSheet()
        bs_menu.add_item(
            "Facebook",
            lambda x: self.callback_for_menu_items("Facebook"),
            icon_src=f"{os.environ['KITCHEN_SINK_ASSETS']}facebook-box.png",
        )
        bs_menu.add_item(
            "YouTube",
            lambda x: self.callback_for_menu_items("YouTube"),
            icon_src=f"{os.environ['KITCHEN_SINK_ASSETS']}youtube-play.png",
        )
        bs_menu.add_item(
            "Twitter",
            lambda x: self.callback_for_menu_items("Twitter"),
            icon_src=f"{os.environ['KITCHEN_SINK_ASSETS']}twitter.png",
        )
        bs_menu.add_item(
            "Da Cloud",
            lambda x: self.callback_for_menu_items("Da Cloud"),
            icon_src=f"{os.environ['KITCHEN_SINK_ASSETS']}cloud-upload.png",
        )
        bs_menu.add_item(
            "Camera",
            lambda x: self.callback_for_menu_items("Camera"),
            icon_src=f"{os.environ['KITCHEN_SINK_ASSETS']}camera.png",
        )
        bs_menu.open()

    def show_example_custom_bottom_sheet(
        self, type, corner=None, animation=True
    ):

        if type == "custom":
            custom_screen_for_bottom_sheet = Factory.KitchenSinkBaseContent()
            custom_screen_for_bottom_sheet.callback = (
                self.callback_for_menu_items
            )
        elif type == "list":
            custom_screen_for_bottom_sheet = (
                KitchenSinkBoxContentForBottomSheetCustomList()
            )

        MDCustomBottomSheet(
            screen=custom_screen_for_bottom_sheet,
            bg_color=[0.2, 0.2, 0.2, 1],
            animation=animation,
            radius_from=corner,
        ).open()

    def callback_for_menu_items(self, text):
        toast(text)


class KitchenSinkBoxContentForBottomSheetCustomList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        icons = list(md_icons.keys())[0:10]
        for i in range(10):
            self.ids.box.add_widget(
                KitchenSinkOneLineLeftIconItem(icon=icons[i], text=f"Item {i}")
            )
