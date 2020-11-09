import ast
import os
import sys
from pathlib import Path

from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.loader import Loader
from libs.baseclass.dialog_change_theme import (
    KitchenSinkDialogChangeTheme,
    KitchenSinkUsageCode,
)
from libs.baseclass.expansionpanel import KitchenSinkExpansionPanelContent
from libs.baseclass.list_items import (  # NOQA: F401
    KitchenSinkOneLineLeftIconItem,
)

from kivymd import images_path
from kivymd.app import MDApp
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine

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
            f"{os.environ['KITCHEN_SINK_ROOT']}/libs/kv/list_items.kv"
        )
        return Builder.load_file(
            f"{os.environ['KITCHEN_SINK_ROOT']}/libs/kv/start_screen.kv"
        )

    def show_dialog_change_theme(self):
        if not self.dialog_change_theme:
            self.dialog_change_theme = KitchenSinkDialogChangeTheme()
            self.dialog_change_theme.set_list_colors_themes()
        self.dialog_change_theme.open()

    def on_start(self):
        """Creates a list of items with examples on start screen."""
        Builder.load_file(
            f"{os.environ['KITCHEN_SINK_ROOT']}/libs/kv/dialog_change_theme.kv",
        )
        Builder.load_file(
            f"{os.environ['KITCHEN_SINK_ROOT']}/libs/kv/base_content.kv",
        )

        with open(
            f"{os.environ['KITCHEN_SINK_ROOT']}/screens_data.json"
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
                f"{os.environ['KITCHEN_SINK_ROOT']}/libs/kv/{name_kv_file}.kv",
            )
            if "Import" in self.data_screens[name_screen]:
                exec(self.data_screens[name_screen]["Import"])
            screen_object = eval(self.data_screens[name_screen]["Factory"])
            self.data_screens[name_screen]["object"] = screen_object
            if "toolbar" in screen_object.ids:
                screen_object.ids.toolbar.title = name_screen
            manager.add_widget(screen_object)
        code_file = f"{os.environ['KITCHEN_SINK_ROOT']}/assets/md/{self.data_screens[name_screen]['source_code']}"
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

    def callback_for_menu_items(self, *args):
        from kivymd.toast import toast

        toast(args[0])

    def show_code(self):
        if self.theme_cls.device_orientation == "landscape":
            code = KitchenSinkUsageCode(
                code=self.sample_code,
                title=self.screen_name,
                website=self.website,
            )
            code.open()

    def show_demo_shrine(self, instance):
        """
        :type instance <Screen name='shrine demo'> object

        """

        def add_screen_shrine(MDShrine):
            def remove_box(*args):
                instance.remove_widget(box)

            from kivy.animation import Animation

            md_shrine = MDShrine()
            md_shrine.opacity = 0
            instance.add_widget(md_shrine)

            anim = Animation(opacity=0, d=0.5)
            anim.bind(on_complete=remove_box)
            anim.start(box)
            Animation(opacity=2, d=0.5).start(md_shrine)
            self.theme_cls.primary_palette = "Red"

        def show_demo_shrine(interval):
            from kivy.animation import Animation
            from studies.shrine.shrine import MDShrine

            anim = Animation(
                size_hint=(0.2, 0.2), pos_hint={"center_y": 0.7}, d=0.5
            )
            anim.bind(on_complete=lambda *x: add_screen_shrine(MDShrine))
            anim.start(box)

        from kivy.clock import Clock
        from kivy.metrics import dp
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.image import Image

        self.theme_cls.theme_style = "Light"
        box = BoxLayout(
            orientation="vertical",
            size_hint=(0.4, 0.6),
            spacing=dp(10),
            pos_hint={"center_x": 0.5, "center_y": 0.6},
        )
        path_to_logo = (
            f"{os.environ['KITCHEN_SINK_ROOT']}/studies/shrine/data/images/shrine-white.png"
            if self.theme_cls.theme_style == "Dark"
            else f"{os.environ['KITCHEN_SINK_ROOT']}/studies/shrine/data/images/shrine-dark.png"
        )
        logo = Image(
            source=path_to_logo, size_hint_x=0.8, pos_hint={"center_x": 0.5}
        )
        box.add_widget(logo)
        box.add_widget(Factory.ShrinePresplashTile(text="SHRINE"))
        instance.add_widget(box)
        Clock.schedule_once(show_demo_shrine, 1)

    def add_expansion_panel(self, card):
        content = KitchenSinkExpansionPanelContent()
        card.add_widget(
            MDExpansionPanel(
                icon=f"{os.environ['KITCHEN_SINK_ASSETS']}avatar.png",
                content=content,
                panel_cls=MDExpansionPanelOneLine(text="KivyMD 0.104.1"),
            )
        )


KitchenSinkApp().run()
