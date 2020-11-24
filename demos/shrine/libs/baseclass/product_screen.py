import os

from kivy.animation import Animation
from kivy.properties import ListProperty, StringProperty
from kivy.utils import get_color_from_hex

from kivymd.color_definitions import colors
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import MagicBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.screen import MDScreen

PATH_TO_IMAGES = f"{os.environ['SHRINE_ROOT']}/assets/images"


class MoreInformation(ThemableBehavior, MDBoxLayout):
    pass


class PlanItem(ThemableBehavior, MagicBehavior, MDBoxLayout):
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


class ProductScreen(ThemableBehavior, MDScreen):
    has_already_opened = False

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
            panel_cls=MDExpansionPanelOneLine(text="More information"),
        )
        self.ids.expansion_panel_box.add_widget(md_expansion_panel)
        self.ids.previous_image.source = f"{PATH_TO_IMAGES}/previous.jpg"
