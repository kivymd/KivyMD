from kivy.lang import Builder

from kivymd.app import MDApp

from examples.common_app import CommonApp

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: "12dp"
        icon: "menu"

    MDBoxLayout:
        orientation: "vertical"
        padding: "32dp", "72dp", "32dp", "32dp"
        spacing: "24dp"

        MDLabel:
            adaptive_height: True
            text: "Segmented button"

        MDSegmentedButton:
            id: segmented_button
    
            MDSegmentedButtonItem:
                
                MDSegmentButtonIcon:
                    icon: "language-python"
    
                MDSegmentButtonLabel:
                    text: "Python"
    
            MDSegmentedButtonItem:
                
                MDSegmentButtonIcon:
                    icon: "language-javascript"
    
                MDSegmentButtonLabel:
                    text: "Java-Script"

        MDLabel:
            adaptive_height: True
            text: "Custom Segmented button"

        MDSegmentedButton:
            id: segmented_button_custom
            selected_icon_color: "red"
    
            MDSegmentedButtonItem:
                theme_line_color: "Custom"
                line_color: "red"
                selected_color: "#a655f240"
                
                MDSegmentButtonIcon:
                    icon: "language-python"
                    theme_icon_color: "Custom"
                    icon_color: "red"
    
                MDSegmentButtonLabel:
                    text: "Python"
                    theme_text_color: "Custom"
                    text_color: "red"
    
            MDSegmentedButtonItem:
                theme_line_color: "Custom"
                line_color: "red"
                selected_color: "#a655f240"
                
                MDSegmentButtonIcon:
                    icon: "language-javascript"
                    theme_icon_color: "Custom"
                    icon_color: "red"
    
                MDSegmentButtonLabel:
                    text: "Java-Script"
                    theme_text_color: "Custom"
                    text_color: "red"

        MDWidget:
"""


class Example(MDApp, CommonApp):
    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)

    def disabled_widgets(self):
        for item in (
            self.root.ids.segmented_button.get_items()
            + self.root.ids.segmented_button_custom.get_items()
        ):
            item.disabled = not item.disabled


Example().run()
