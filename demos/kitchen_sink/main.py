import ast
import os
import sys
from pathlib import Path

from kivy.core.window import Window
from kivy.factory import Factory  # NOQA: F401
from kivy.lang import Builder
from kivy.loader import Loader
from libs.baseclass.dialog_change_theme import (
    KitchenSinkDialogChangeTheme,
    KitchenSinkUsageCode,
)
from libs.baseclass.list_items import (  # NOQA: F401
    KitchenSinkOneLineLeftIconItem,
)

from kivymd import images_path
from kivymd.app import MDApp

os.environ["KIVY_PROFILE_LANG"] = "1"

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["KITCHEN_SINK_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ["KITCHEN_SINK_ROOT"] = str(Path(__file__).parent)
    # os.environ["KITCHEN_SINK_ROOT"] = os.path.dirname(os.path.abspath(__file__))
os.environ["KITCHEN_SINK_ASSETS"] = os.path.join(
    os.environ["KITCHEN_SINK_ROOT"], f"assets{os.sep}"
)
Window.softinput_mode = "below_target"


class KitchenSinkApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"
        self.dialog_change_theme = None
        self.toolbar = None
        self.data_screens = {}
        Loader.loading_image = f"{images_path}transparent.png"

    def build(self):
        Builder.load_file(
            os.path.join(
                os.environ["KITCHEN_SINK_ROOT"], "libs", "kv", "list_items.kv"
            )
        )
        return Builder.load_file(
            os.path.join(
                os.environ["KITCHEN_SINK_ROOT"], "libs", "kv", "start_screen.kv"
            )
        )

    def show_dialog_change_theme(self):
        if not self.dialog_change_theme:
            self.dialog_change_theme = KitchenSinkDialogChangeTheme()
            self.dialog_change_theme.set_list_colors_themes()
        self.dialog_change_theme.open()

    def on_start(self):
        """Creates a list of items with examples on start screen."""

        Builder.load_file(
            os.path.join(
                os.environ["KITCHEN_SINK_ROOT"],
                "libs",
                "kv",
                "dialog_change_theme.kv",
            )
        )

        with open(
            os.path.join(os.environ["KITCHEN_SINK_ROOT"], "screens_data.json")
        ) as read_file:
            self.data_screens = ast.literal_eval(read_file.read())
            data_screens = list(self.data_screens.keys())
            data_screens.sort()
        for name_item_example in data_screens:
            self.root.ids.backdrop_front_layer.data.append(
                {
                    "viewclass": "KitchenSinkOneLineLeftIconItem",
                    "text": name_item_example,
                    "icon": self.data_screens[name_item_example]["icon"],
                    "on_release": lambda x=name_item_example: self.set_example_screen(
                        x
                    ),
                }
            )

    def set_example_screen(self, name_screen):
        manager = self.root.ids.screen_manager
        if not manager.has_screen(
            self.data_screens[name_screen]["name_screen"]
        ):
            name_kv_file = self.data_screens[name_screen]["kv_string"]
            Builder.load_file(
                os.path.join(
                    os.environ["KITCHEN_SINK_ROOT"],
                    "libs",
                    "kv",
                    f"{name_kv_file}.kv",
                )
            )
            if "Import" in self.data_screens[name_screen]:
                exec(self.data_screens[name_screen]["Import"])
            screen_object = eval(self.data_screens[name_screen]["Factory"])
            self.data_screens[name_screen]["object"] = screen_object
            if "toolbar" in screen_object.ids:
                screen_object.ids.toolbar.title = name_screen
            manager.add_widget(screen_object)
        code_file = os.path.join(
            os.environ["KITCHEN_SINK_ROOT"],
            "assets",
            "usage",
            self.data_screens[name_screen]["source_code"],
        )
        with open(code_file, "r") as f:
            self.sample_code = f.read()
            self.screen_name = name_screen
            self.website = self.data_screens[name_screen]["more_info"]
        manager.current = self.data_screens[name_screen]["name_screen"]

    def back_to_home_screen(self):
        self.root.ids.screen_manager.current = "home"

    def switch_theme_style(self):
        self.theme_cls.theme_style = (
            "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        )
        self.root.ids.backdrop.ids._front_layer.md_bg_color = [0, 0, 0, 0]

    def show_code(self):
        if self.theme_cls.device_orientation == "landscape":
            code = KitchenSinkUsageCode(
                code=self.sample_code,
                title=self.screen_name,
                website=self.website,
            )
            code.open()


KitchenSinkApp().run()
