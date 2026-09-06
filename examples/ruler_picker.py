from kivy.metrics import dp

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import IOSRulerPicker, IOSRulerPickerLabel
from kivymd.uix.screen import MDScreen


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        menu = MDIconButton(
            pos_hint={"top": 0.98},
            x="12dp",
            icon="menu",
        )
        menu.bind(on_release=lambda x: MDApp.get_running_app().open_menu(menu))

        self.widgets = [
            MDBoxLayout(
                MDLabel(
                    text="With label and step 20",
                    adaptive_size=True,
                    bold=True,
                ),
                IOSRulerPicker(
                    IOSRulerPickerLabel(),
                    min=100,
                    max=250,
                    value=175,
                    size_hint_y=None,
                    height=dp(56),
                    label_step=10,
                ),
                MDLabel(
                    text="With label and step 50",
                    adaptive_size=True,
                    bold=True,
                ),
                IOSRulerPicker(
                    IOSRulerPickerLabel(),
                    min=100,
                    max=500,
                    value=250,
                    size_hint_y=None,
                    height=dp(56),
                    label_step=50,
                ),
                MDLabel(
                    text="With custom color",
                    adaptive_size=True,
                    bold=True,
                ),
                IOSRulerPicker(
                    IOSRulerPickerLabel(),
                    min=100,
                    max=250,
                    value=150,
                    size_hint_y=None,
                    height=dp(100),
                    label_step=10,
                    indicator_color="olive",
                    primary_tick_color="teal",
                    secondary_tick_color="red",
                ),
                orientation="vertical",
                spacing=dp(12),
                padding=dp(48),
                md_bg_color=self.theme_cls.backgroundColor,
                adaptive_height=True,
                pos_hint={"center_y": 0.5},
            ),
            menu,
        ]


class RulerPickerApp(MDApp, CommonApp):
    def build(self):
        return MainScreen(md_bg_color=self.theme_cls.backgroundColor)


if __name__ == "__main__":
    RulerPickerApp().run()
