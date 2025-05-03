from kivy.lang import Builder

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: "12dp"
        icon: "menu"

    MDRecycleView:
        id: rv
        key_viewclass: 'viewclass'
        key_size: 'height'
        size_hint_y: None
        height: root.height - dp(48)

        RecycleBoxLayout:
            padding: dp(18)
            spacing: dp(10)
            default_size: None, dp(48)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: "vertical"
"""


class Example(MDApp, CommonApp):
    _disabled = False

    def build(self):
        return Builder.load_string(KV)

    def disabled_widgets(self):
        self._disabled = not self._disabled
        self.create_widgets()

    def create_widgets(self):
        self.root.ids.rv.data = []
        for style in theme_font_styles:
            if style != "Icon":
                for role in theme_font_styles[style]:
                    font_size = int(theme_font_styles[style][role]["font-size"])
                    self.root.ids.rv.data.append(
                        {
                            "viewclass": "MDLabel",
                            "text": f"{style} {role} {font_size} sp",
                            "adaptive_height": "True",
                            "font_style": style,
                            "role": role,
                            "disabled": self._disabled,
                        }
                    )

    def on_start(self):
        self.create_widgets()


Example().run()
