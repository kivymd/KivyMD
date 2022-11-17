from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class TestLabelDefaultThemeTextColor(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color_data = {
            "Secondary": getattr(self.theme_cls, "secondary_text_color"),
            "Hint": getattr(self.theme_cls, "disabled_hint_text_color"),
            "Error": getattr(self.theme_cls, "error_color"),
        }

    def build(self):
        return MDScreen()

    def on_start(self):
        def check_color():
            assert label.color == self.color_data[name_color]

        for name_color in self.color_data.keys():
            label = MDLabel(text="MDLabel", theme_text_color=name_color)
            self.root.add_widget(label)
            check_color()

        self.stop()


TestLabelDefaultThemeTextColor().run()
