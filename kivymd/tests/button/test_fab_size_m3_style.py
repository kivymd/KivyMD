from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton

KV = """
MDScreen:
    md_bg_color: "#f7f2fa"

    MDBoxLayout:
        id: box
        spacing: "56dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class TestFabSizeM3Style(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def check_size_button(self, *args):
        data = {
            "large": [96.0, 96.0],
            "small": [40.0, 40.0],
            "standard": [56.0, 56.0],
        }
        for button in self.root.ids.box.children:
            assert button.size == data[button.type]

        self.stop()

    def on_start(self):
        data = {
            "standard": {"md_bg_color": "#fefbff", "text_color": "#6851a5"},
            "small": {"md_bg_color": "#e9dff7", "text_color": "#211c29"},
            "large": {"md_bg_color": "#f8d7e3", "text_color": "#311021"},
        }
        for type_button in data.keys():
            self.root.ids.box.add_widget(
                MDFloatingActionButton(
                    icon="pencil",
                    type=type_button,
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    icon_color=data[type_button]["text_color"],
                )
            )

        Clock.schedule_once(self.check_size_button, 1.2)


TestFabSizeM3Style().run()
