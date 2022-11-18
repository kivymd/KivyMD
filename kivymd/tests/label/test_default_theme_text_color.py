from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.utils import asynckivy


class TestDefaultThemeTextColor(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color_data = {
            "Secondary": getattr(self.theme_cls, "secondary_text_color"),
            "Hint": getattr(self.theme_cls, "disabled_hint_text_color"),
            "Error": getattr(self.theme_cls, "error_color"),
        }

    def build(self):
        return MDScreen()

    async def generate_labels(self):
        for name_color in self.color_data.keys():
            await asynckivy.sleep(0)
            label = MDLabel(text="MDLabel", theme_text_color=name_color)
            self.root.add_widget(label)
            assert label.color == self.color_data[name_color]
            self.root.clear_widgets()
        self.stop()

    def on_start(self):
        asynckivy.start(self.generate_labels())


TestDefaultThemeTextColor().run()
