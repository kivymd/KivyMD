from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.behaviors import (
    M3RectangularRippleBehavior,
    M3CircularRippleBehavior,
)
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, MDListItem, MDListItemHeadlineText, MDListItemSupportingText
from kivymd.uix.scrollview import MDScrollView

KV = """
MDScreen:
    md_bg_color: app.theme_cls.surfaceContainerColor

    MDBoxLayout:
        orientation: "vertical"
        spacing: "20dp"
        padding: "20dp"

        MDBoxLayout:
            adaptive_height: True
            spacing:dp(20)

            MDIconButton:
                icon: "menu"
                on_release: app.open_menu(self)
                pos_hint: {"center_y": .5}

            MDLabel:
                text: "Material 3 Ripple"
                theme_font_style: "Headline"
                adaptive_height: True
        Widget:

        MDScrollView:
            do_scroll_x: False
            bar_width: "4dp"

            MDList:
                adaptive_height: True
                spacing: "16dp"
                padding: "0dp", "0dp", "0dp", "20dp"

                M3RippleBox:
                    size_hint_x: 1
                    height: "120dp"
                    md_bg_color: app.theme_cls.surfaceContainerHighestColor
                    radius: "16dp"

                    MDLabel:
                        text: "Click Me"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1

                M3RippleBox:
                    size_hint_x: 1
                    height: "120dp"
                    md_bg_color: app.theme_cls.secondaryContainerColor
                    ripple_color:"#8dffff"
                    radius: [dp(60), dp(0), dp(60), 0]
                    ripple_alpha: 0.7

                    MDLabel:
                        text: "Custom Alpha Ripple"
                        halign: "center"

                M3RippleCircle:
                    size_hint: None, None
                    size: [dp(200)]*2
                    pos_hint: {"center_x": .5}
                    ripple_color:app.theme_cls.primaryColor
                    ripple_alpha: 0.7
                    radius:[self.height/2]*4

                    MDLabel:
                        text: "Circle"
                        halign: "center"

                MDListItem:
                    size_hint_x: 1
                    height: "72dp"
                    md_bg_color: app.theme_cls.surfaceContainerLowColor

                    MDListItemHeadlineText:
                        text: "Scrollable list item"

                    MDListItemSupportingText:
                        text: "Ripple inside a scroll view"

                MDListItem:
                    size_hint_x: 1
                    height: "72dp"
                    md_bg_color: app.theme_cls.surfaceContainerLowColor

                    MDListItemHeadlineText:
                        text: "Another item"

                    MDListItemSupportingText:
                        text: "Use this to verify nested coordinates"


        Widget:
"""


class M3RippleBox(
    M3RectangularRippleBehavior,
    MDBoxLayout,
):
    pass


class M3RippleCircle(
    M3CircularRippleBehavior,
    MDBoxLayout,
):
    pass


class Example(MDApp, CommonApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()
