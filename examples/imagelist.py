from kivy.lang import Builder
from kivy.properties import VariableListProperty

from kivymd.app import MDApp
from kivymd.uix.imagelist import MDSmartTile

from examples.common_app import CommonApp

KV = """
<SmartTile>
    size_hint: None, None
    size: "320dp", "320dp"

    MDSmartTileImage:
        source: "bg.jpg"
        radius: root.image_radius

    MDSmartTileOverlayContainer:
        md_bg_color: 0, 0, 0, .5
        adaptive_height: True
        padding: "8dp"
        spacing: "8dp"
        radius: root.container_radius

        MDIconButton:
            icon: "heart-outline"
            pos_hint: {"center_y": .5}
            on_release:
                self.icon = "heart" \\
                if self.icon == "heart-outline" else \\
                "heart-outline"

        MDLabel:
            text: "Ibanez GRG121DX-BKF"
            theme_text_color: "Custom"
            text_color: "white"


MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: "12dp"
        icon: "menu"

    MDBoxLayout:
        adaptive_size: True
        spacing: "24dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        SmartTile:
            overlap: True
            image_radius: [dp(24), ]
            container_radius: [0, 0, dp(24), dp(24)]

        SmartTile:
            overlap: False
            image_radius: [dp(24), dp(24), 0, 0]
            container_radius: [0, 0, dp(24), dp(24)]
"""


class SmartTile(MDSmartTile):
    image_radius = VariableListProperty([0], length=4)
    container_radius = VariableListProperty([0], length=4)


class Example(MDApp, CommonApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def disabled_widgets(self):
        ...


Example().run()
