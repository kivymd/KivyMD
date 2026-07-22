from kivy.lang import Builder

from examples.common_app import CommonApp
from kivymd.app import MDApp

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: dp(12)
        icon: "menu"

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDBoxLayout:
                    spacing: "24dp"
                    pos_hint: {"center_x": .5, "center_y": .7}
                    adaptive_size: True

                    MDButton:
                        on_release: app.open_sheet(sheet, "standard")

                        MDButtonText:
                            text: "Open standard sheet"

                    MDButton:
                        on_release: app.open_sheet(sheet, "modal")

                        MDButtonText:
                            text: "Open modal sheet"

        MDBottomSheet:
            id: sheet
            size_hint_y: None
            height: "320dp"
            background_color: self.theme_cls.surfaceColor
            drawer_type: "standard"

            MDBottomSheetDragHandle:

                MDBottomSheetDragHandleTitle:
                    text: "MDBottomSheet"
                    adaptive_height: True
                    pos_hint: {"center_y": .5}

                MDBottomSheetDragHandleButton:
                    icon: "close"
                    on_release: sheet.set_state("toggle")

            BoxLayout:
                orientation: "vertical"

                Widget:
"""


class Example(MDApp, CommonApp):
    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)

    def open_sheet(self, sheet, drawer_type):
        sheet.drawer_type = drawer_type
        sheet.set_state("toggle")

    def disabled_widgets(self): ...


Example().run()
