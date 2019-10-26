import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex
from kivy.animation import Animation

from kivymd.color_definitions import colors
from kivymd.theming import ThemableBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.behaviors import MagicBehavior
from kivymd.utils.cropimage import crop_image


PATH_TO_IMAGES = f"{os.environ['KITCHEN_SINK_ROOT']}/studies/shrine/data/images"


class MoreInformation(ThemableBehavior, BoxLayout):
    pass


class PlanItem(ThemableBehavior, MagicBehavior, BoxLayout):
    text_item = StringProperty()
    border = StringProperty()
    color_select = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color_select = self.theme_cls.disabled_hint_text_color
        self.primary = get_color_from_hex(colors["BlueGray"]["500"])

    def press_on_plan(self, instance_plan):
        for widget in self.parent.parent.children[0].children:
            if widget.color_select == self.primary:
                widget.color_select = self.color_select
                self.grow()
                break
        instance_plan.color_select = self.primary


class ProductScreen(ThemableBehavior, Screen):
    has_already_opened = False

    # FIXME: Some kind of dirty hack - after opening the `md_expansion_panel`,
    #  the `content_for_panel` height is 1900 pixels.
    def on_panel_open(self, instance_md_expansion_panel):
        Animation(height=dp(450), d=0.2).start(self.ids.expansion_panel_box)

    def on_panel_close(self, instance_md_expansion_panel):
        Animation(height=dp(65), d=0.2).start(self.ids.expansion_panel_box)

    def show_product_screen(self):
        Animation(y=0, opacity=1, d=0.3).start(self)

    def hide_product_screen(self):
        Animation(y=-self.height, opacity=0, d=0.3).start(self)

    def on_enter(self):
        if self.has_already_opened:
            return
        else:
            self.has_already_opened = True

        content_for_panel = MoreInformation()
        md_expansion_panel = MDExpansionPanel(
            content=content_for_panel,
            icon=f"{PATH_TO_IMAGES}/information.png",
            title="More information",
        )
        md_expansion_panel.bind(on_open=self.on_panel_open)
        md_expansion_panel.bind(on_close=self.on_panel_close)
        self.ids.expansion_panel_box.add_widget(md_expansion_panel)

        path = f"{PATH_TO_IMAGES}/previous_crop.jpg"
        if not os.path.exists(path):
            crop_image(
                (Window.width, int(dp(Window.height * 35 // 100))),
                f"{PATH_TO_IMAGES}/previous.jpg",
                path,
            )
        Clock.schedule_once(lambda x: self.set_path_toImage_product(path), 0.2)

    def set_path_toImage_product(self, path, interval=0):
        self.ids.previous_image.source = path
