from kivy.lang import Builder
from kivy.utils import get_hex_from_color

from kivymd.app import MDApp
from kivymd.color_definitions import colors
from kivymd.uix.button import (
    MDRoundFlatButton,
    MDIconButton,
    MDFloatingActionButton,
    MDFlatButton,
    MDRaisedButton,
    MDRectangleFlatButton,
    MDRectangleFlatIconButton,
    MDRoundFlatIconButton,
    MDFillRoundFlatButton,
    MDFillRoundFlatIconButton,
    MDTextButton,
)

KV = """
MDScreen:

    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: "10dp"

        ScrollView:
    
            MDBoxLayout:
                orientation: "vertical"
                padding: 20
                spacing: "10dp"
                adaptive_height: True
    
                # MDIconButton
    
                MDLabel:
                    text: "MDIconButton from KV"
                    adaptive_height: True
                    halign: "center"
                    font_style: "H6"
    
                MDSeparator:
        
                MDBoxLayout:
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True
        
                    MDIconButton:
                        id: btn_1
                        icon: "android"
                        user_font_size: "24sp"
        
                    MDIconButton:
                        id: btn_2
                        icon: "android"
                        user_font_size: "36sp"
        
                    MDIconButton:
                        id: btn_3
                        icon: "android"
                        user_font_size: "48sp"
        
                    MDIconButton:
                        icon: "android"
                        user_font_size: "56sp"
                        disabled: True

                MDBoxLayout:
                    adaptive_size: True

                    MDFlatButton:
                        text: "SET ICON COLOR"
                        on_release:
                            btn_1.theme_text_color = "Custom"
                            btn_1.text_color = (0, 0, 1, 1)
                            btn_2.theme_text_color = "Custom"
                            btn_2.text_color = (0, 0, 1, 1)
                            btn_3.theme_text_color = "Custom"
                            btn_3.text_color = (0, 0, 1, 1)
        
                    MDFlatButton:
                        text: "DISABLED"
                        on_release:
                            btn_1.disabled = True
                            btn_2.disabled = True
                            btn_3.disabled = True
        
                    MDFlatButton:
                        text: "UNDISABLED"
                        on_release:
                            btn_1.disabled = False
                            btn_2.disabled = False
                            btn_3.disabled = False

                    MDFlatButton:
                        text: "SET BG COLOR"
                        on_release:
                            btn_1.md_bg_color = (0, 1, 0, 1)
                            btn_2.md_bg_color = (1, 1, 0, 1)
                            btn_3.md_bg_color = (1, 0, 0, 1)

                    MDFlatButton:
                        text: "SET STYLE"
                        on_release:
                            app.theme_cls.theme_style = "Dark" \
                            if app.theme_cls.theme_style == "Light" \
                            else "Light"

                    MDFlatButton:
                        text: "SET PALETTE"
                        on_release:
                            app.theme_cls.primary_palette = "Green"

                MDBoxLayout:
                    orientation: "vertical"
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True
                    md_bg_color: 0, 0, 0, .2

                    MDLabel:
                        text: "MDIconButton from Python"
                        adaptive_height: True
                        halign: "center"
                        font_style: "H6"
            
                    MDBoxLayout:
                        id: python_box
                        padding: 20
                        spacing: "10dp"
                        adaptive_height: True

                MDSeparator:

                # MDFloatingActionButton

                MDLabel:
                    text: "MDFloatingActionButton from KV"
                    adaptive_height: True
                    halign: "center"
                    font_style: "H6"
            
                MDBoxLayout:
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True
        
                    MDFloatingActionButton:
                        id: btn_4
                        icon: "git"
        
                    MDFloatingActionButton:
                        id: btn_5
                        icon: "android"
        
                    MDFloatingActionButton:
                        id: btn_6
                        icon: "android"
        
                    MDFloatingActionButton:
                        icon: "android"
                        disabled: True
        
                MDBoxLayout:
                    adaptive_size: True

                    MDFlatButton:
                        text: "SET ICON COLOR"
                        on_release:
                            btn_4.theme_text_color = "Custom"
                            btn_4.text_color = (1, 0, 1, 1)
                            btn_5.theme_text_color = "Custom"
                            btn_5.text_color = (0, 1, 1, 1)
                            btn_6.theme_text_color = "Custom"
                            btn_6.text_color = (1, 0, 0, 1)
        
                    MDFlatButton:
                        text: "DISABLED"
                        on_release:
                            btn_4.disabled = True
                            btn_5.disabled = True
                            btn_6.disabled = True
        
                    MDFlatButton:
                        text: "UNDISABLED"
                        on_release:
                            btn_4.disabled = False
                            btn_5.disabled = False
                            btn_6.disabled = False

                    MDFlatButton:
                        text: "SET BG COLOR"
                        on_release:
                            btn_4.md_bg_color = (0, 1, 0, 1)
                            btn_5.md_bg_color = (1, 1, 0, 1)
                            btn_6.md_bg_color = (1, 0, 0, 1)

                    MDFlatButton:
                        text: "SET STYLE"
                        on_release:
                            app.theme_cls.theme_style = "Dark" \
                            if app.theme_cls.theme_style == "Light" \
                            else "Light"

                    MDFlatButton:
                        text: "SET PALETTE"
                        on_release: app.theme_cls.primary_palette = "Yellow"

                MDBoxLayout:
                    orientation: "vertical"
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True
                    md_bg_color: 0, 0, 0, .2
        
                    MDLabel:
                        text: "MDFloatingActionButton from Python"
                        adaptive_height: True
                        halign: "center"
                        font_style: "H6"
            
                    MDBoxLayout:
                        id: python_box_2
                        padding: 20
                        spacing: "10dp"
                        adaptive_height: True

                # MDFlatButton

                MDSeparator:

                MDLabel:
                    text: "MDFlatButton from KV"
                    adaptive_height: True
                    halign: "center"
                    font_style: "H6"
            
                MDBoxLayout:
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True

                    MDFlatButton:
                        id: btn_7
                        text: "MDFlatButton"

                    MDFlatButton:
                        id: btn_8
                        text: "MDFlatButton"
                        font_style: "H5"
        
                    MDFlatButton:
                        text: "MDFlatButton"
                        disabled: True
        
                MDBoxLayout:
                    adaptive_size: True

                    MDFlatButton:
                        text: "SET TEXT COLOR"
                        on_release:
                            btn_7.theme_text_color = "Custom"
                            btn_7.text_color = (0, 0, 1, 1)
                            btn_8.theme_text_color = "Custom"
                            btn_8.text_color = (0, 0, 1, 1)
        
                    MDFlatButton:
                        text: "DISABLED"
                        on_release:
                            btn_7.disabled = True
                            btn_8.disabled = True
        
                    MDFlatButton:
                        text: "UNDISABLED"
                        on_release:
                            btn_7.disabled = False
                            btn_8.disabled = False

                    MDFlatButton:
                        text: "SET STYLE"
                        on_release:
                            app.theme_cls.theme_style = "Dark" \
                            if app.theme_cls.theme_style == "Light" \
                            else "Light"

                MDBoxLayout:
                    orientation: "vertical"
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True
                    md_bg_color: 0, 0, 0, .2

                    MDLabel:
                        text: "MDFlatButton from Python"
                        adaptive_height: True
                        halign: "center"
                        font_style: "H6"

                    MDBoxLayout:
                        id: python_box_3
                        padding: 20
                        spacing: "10dp"
                        adaptive_height: True

                # MDRaisedButton

                MDSeparator:

                MDLabel:
                    text: "MDRaisedButton from KV"
                    adaptive_height: True
                    halign: "center"
                    font_style: "H6"
            
                MDBoxLayout:
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True

                    MDRaisedButton:
                        id: btn_9
                        text: "MDRaisedButton"

                    MDRaisedButton:
                        id: btn_10
                        text: "MDRaisedButton"
                        font_style: "H5"
        
                    MDRaisedButton:
                        text: "MDRaisedButton"
                        disabled: True
        
                MDBoxLayout:
                    adaptive_size: True

                    MDFlatButton:
                        text: "SET TEXT COLOR"
                        on_release:
                            btn_9.theme_text_color = "Custom"
                            btn_9.text_color = (1, 0, 1, 1)
                            btn_10.theme_text_color = "Custom"
                            btn_10.text_color = (0, 0, 1, 1)

                    MDFlatButton:
                        text: "SET BG COLOR"
                        on_release:
                            app.theme_cls.primary_palette = "Yellow"
                            #btn_9.md_bg_color = (0, 0, 1, 1)
                            #btn_10.md_bg_color = (1, 0, 1, 1)
        
                    MDFlatButton:
                        text: "DISABLED"
                        on_release:
                            btn_9.disabled = True
                            btn_10.disabled = True
        
                    MDFlatButton:
                        text: "UNDISABLED"
                        on_release:
                            btn_9.disabled = False
                            btn_10.disabled = False

                    MDFlatButton:
                        text: "SET STYLE"
                        on_release:
                            app.theme_cls.theme_style = "Dark" \
                            if app.theme_cls.theme_style == "Light" \
                            else "Light"

                MDBoxLayout:
                    orientation: "vertical"
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True
                    md_bg_color: 0, 0, 0, .2

                    MDLabel:
                        text: "MDFlatButton from Python"
                        adaptive_height: True
                        halign: "center"
                        font_style: "H6"

                    MDBoxLayout:
                        id: python_box_4
                        padding: 20
                        spacing: "10dp"
                        adaptive_height: True

                # MDRectangleFlatButton

                MDSeparator:

                MDLabel:
                    text: "MDRectangleFlatButton from KV"
                    adaptive_height: True
                    halign: "center"
                    font_style: "H6"
            
                MDBoxLayout:
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True

                    MDRectangleFlatButton:
                        id: btn_11
                        text: "MDRectangleFlatButton"

                    MDRectangleFlatButton:
                        id: btn_12
                        text: "MDRectangleFlatButton"
                        font_style: "H5"
        
                    MDRectangleFlatButton:
                        text: "MDRectangleFlatButton"
                        disabled: True
        
                MDBoxLayout:
                    adaptive_size: True

                    MDFlatButton:
                        text: "SET TEXT COLOR"
                        on_release:
                            btn_11.theme_text_color = "Custom"
                            btn_11.text_color = (1, 0, 1, 1)
                            btn_12.theme_text_color = "Custom"
                            btn_12.text_color = (0, 0, 1, 1)

                    MDFlatButton:
                        text: "SET LINE COLOR"
                        on_release:
                            btn_11.line_color = (0, 0, 1, 1)
                            btn_12.line_color = (1, 0, 1, 1)
        
                    MDFlatButton:
                        text: "DISABLED"
                        on_release:
                            btn_11.disabled = True
                            btn_12.disabled = True
        
                    MDFlatButton:
                        text: "UNDISABLED"
                        on_release:
                            btn_11.disabled = False
                            btn_12.disabled = False

                    MDFlatButton:
                        text: "SET STYLE"
                        on_release:
                            app.theme_cls.theme_style = "Dark" \
                            if app.theme_cls.theme_style == "Light" \
                            else "Light"

                    MDFlatButton:
                        text: "SET PALETTE"
                        on_release:
                            app.theme_cls.primary_palette = "Yellow"

                MDBoxLayout:
                    orientation: "vertical"
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True
                    md_bg_color: 0, 0, 0, .2

                    MDLabel:
                        text: "MDRectangleFlatButton from Python"
                        adaptive_height: True
                        halign: "center"
                        font_style: "H6"

                    MDBoxLayout:
                        id: python_box_5
                        padding: 20
                        spacing: "10dp"
                        adaptive_height: True

                # MDRectangleFlatIconButton

                MDSeparator:

                MDLabel:
                    text: "MDRectangleFlatIconButton from KV"
                    adaptive_height: True
                    halign: "center"
                    font_style: "H6"
            
                MDBoxLayout:
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True

                    MDRectangleFlatIconButton:
                        id: btn_13
                        text: "MDRectangleFlatIconButton"

                    MDRectangleFlatIconButton:
                        id: btn_14
                        text: "MDRectangleFlatIconButton"
                        font_style: "H5"
        
                    MDRectangleFlatIconButton:
                        text: "MDRectangleFlatIconButton"
                        disabled: True
        
                MDBoxLayout:
                    adaptive_size: True

                    MDFlatButton:
                        text: "SET TEXT COLOR"
                        on_release:
                            btn_13.theme_text_color = "Custom"
                            btn_13.text_color = (1, 0, 1, 1)
                            btn_14.theme_text_color = "Custom"
                            btn_14.text_color = (0, 0, 1, 1)

                    MDFlatButton:
                        text: "SET ICON COLOR"
                        on_release:
                            btn_13.icon_color = (0, 0, 1, 1)
                            btn_14.icon_color = (1, 0, 1, 1)

                    MDFlatButton:
                        text: "SET LINE COLOR"
                        on_release:
                            btn_13.line_color = (1, 0, 1, 1)
                            btn_14.line_color = (0, 0, 1, 1)
        
                    MDFlatButton:
                        text: "DISABLED"
                        on_release:
                            btn_13.disabled = True
                            btn_14.disabled = True
        
                    MDFlatButton:
                        text: "UNDISABLED"
                        on_release:
                            btn_13.disabled = False
                            btn_14.disabled = False

                    MDFlatButton:
                        text: "SET STYLE"
                        on_release:
                            app.theme_cls.theme_style = "Dark" \
                            if app.theme_cls.theme_style == "Light" \
                            else "Light"

                    MDFlatButton:
                        text: "SET PALETTE"
                        on_release:
                            app.theme_cls.primary_palette = "Yellow"

                MDBoxLayout:
                    orientation: "vertical"
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True
                    md_bg_color: 0, 0, 0, .2

                    MDLabel:
                        text: "MDRectangleFlatIconButton from Python"
                        adaptive_height: True
                        halign: "center"
                        font_style: "H6"

                    MDBoxLayout:
                        id: python_box_6
                        padding: 20
                        spacing: "10dp"
                        adaptive_height: True

                # MDRoundFlatButton

                MDSeparator:

                MDLabel:
                    text: "MDRoundFlatButton from KV"
                    adaptive_height: True
                    halign: "center"
                    font_style: "H6"
            
                MDBoxLayout:
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True

                    MDRoundFlatButton:
                        id: btn_15
                        text: "MDRoundFlatButton"

                    MDRoundFlatButton:
                        id: btn_16
                        text: "MDRoundFlatButton"
                        font_style: "H5"
        
                    MDRoundFlatButton:
                        text: "MDRoundFlatButton"
                        disabled: True
        
                MDBoxLayout:
                    adaptive_size: True

                    MDFlatButton:
                        text: "SET TEXT COLOR"
                        on_release:
                            btn_15.theme_text_color = "Custom"
                            btn_15.text_color = (1, 0, 1, 1)
                            btn_16.theme_text_color = "Custom"
                            btn_16.text_color = (0, 0, 1, 1)

                    MDFlatButton:
                        text: "SET LINE COLOR"
                        on_release:
                            btn_15.line_color = (1, 0, 1, 1)
                            btn_16.line_color = (0, 0, 1, 1)
        
                    MDFlatButton:
                        text: "DISABLED"
                        on_release:
                            btn_15.disabled = True
                            btn_16.disabled = True
        
                    MDFlatButton:
                        text: "UNDISABLED"
                        on_release:
                            btn_15.disabled = False
                            btn_16.disabled = False

                    MDFlatButton:
                        text: "SET STYLE"
                        on_release:
                            app.theme_cls.theme_style = "Dark" \
                            if app.theme_cls.theme_style == "Light" \
                            else "Light"

                    MDFlatButton:
                        text: "SET PALETTE"
                        on_release: app.theme_cls.primary_palette = "Yellow"

                MDBoxLayout:
                    orientation: "vertical"
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True
                    md_bg_color: 0, 0, 0, .2

                    MDLabel:
                        text: "MDRoundFlatButton from Python"
                        adaptive_height: True
                        halign: "center"
                        font_style: "H6"

                    MDBoxLayout:
                        id: python_box_7
                        padding: 20
                        spacing: "10dp"
                        adaptive_height: True

                # MDRoundFlatIconButton

                MDSeparator:

                MDLabel:
                    text: "MDRoundFlatIconButton from KV"
                    adaptive_height: True
                    halign: "center"
                    font_style: "H6"
            
                MDBoxLayout:
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True

                    MDRoundFlatIconButton:
                        id: btn_17
                        text: "MDRoundFlatIconButton"

                    MDRoundFlatIconButton:
                        id: btn_18
                        text: "MDRoundFlatIconButton"
                        font_style: "H5"
        
                    MDRoundFlatIconButton:
                        text: "MDRoundFlatIconButton"
                        disabled: True
        
                MDBoxLayout:
                    adaptive_size: True

                    MDFlatButton:
                        text: "SET TEXT COLOR"
                        on_release:
                            btn_17.theme_text_color = "Custom"
                            btn_17.text_color = (1, 0, 1, 1)
                            btn_18.theme_text_color = "Custom"
                            btn_18.text_color = (0, 0, 1, 1)

                    MDFlatButton:
                        text: "SET LINE COLOR"
                        on_release:
                            btn_17.line_color = (1, 0, 1, 1)
                            btn_18.line_color = (1, 0, 0, 1)

                    MDFlatButton:
                        text: "SET ICON COLOR"
                        on_release:
                            btn_17.icon_color = (0, 0, 1, 1)
                            btn_18.icon_color = (1, 0, 1, 1)
        
                    MDFlatButton:
                        text: "DISABLED"
                        on_release:
                            btn_17.disabled = True
                            btn_18.disabled = True
        
                    MDFlatButton:
                        text: "UNDISABLED"
                        on_release:
                            btn_17.disabled = False
                            btn_18.disabled = False

                    MDFlatButton:
                        text: "SET STYLE"
                        on_release:
                            app.theme_cls.theme_style = "Dark" \
                            if app.theme_cls.theme_style == "Light" \
                            else "Light"

                    MDFlatButton:
                        text: "SET PALETTE"
                        on_release: app.theme_cls.primary_palette = "Yellow"

                MDBoxLayout:
                    orientation: "vertical"
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True
                    md_bg_color: 0, 0, 0, .2

                    MDLabel:
                        text: "MDRoundFlatButton from Python"
                        adaptive_height: True
                        halign: "center"
                        font_style: "H6"

                    MDBoxLayout:
                        id: python_box_8
                        padding: 20
                        spacing: "10dp"
                        adaptive_height: True

                # MDFillRoundFlatButton

                MDSeparator:

                MDLabel:
                    text: "MDFillRoundFlatButton from KV"
                    adaptive_height: True
                    halign: "center"
                    font_style: "H6"
            
                MDBoxLayout:
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True

                    MDFillRoundFlatButton:
                        id: btn_19
                        text: "MDFillRoundFlatButton"

                    MDFillRoundFlatButton:
                        id: btn_20
                        text: "MDFillRoundFlatButton"
                        font_style: "H5"
        
                    MDFillRoundFlatButton:
                        text: "MDFillRoundFlatButton"
                        disabled: True
        
                MDBoxLayout:
                    adaptive_size: True

                    MDFlatButton:
                        text: "SET TEXT COLOR"
                        on_release:
                            btn_19.theme_text_color = "Custom"
                            btn_19.text_color = (1, 0, 1, 1)
                            btn_20.theme_text_color = "Custom"
                            btn_20.text_color = (0, 0, 1, 1)

                    MDFlatButton:
                        text: "SET PALETTE"
                        on_release:
                            app.theme_cls.primary_palette = "Yellow"

                    MDFlatButton:
                        text: "SET BG COLOR"
                        on_release:
                            btn_19.md_bg_color = (0, 0, 1, 1)
                            btn_20.md_bg_color = (1, 0, 0, 1)
        
                    MDFlatButton:
                        text: "DISABLED"
                        on_release:
                            btn_19.disabled = True
                            btn_20.disabled = True
        
                    MDFlatButton:
                        text: "UNDISABLED"
                        on_release:
                            btn_19.disabled = False
                            btn_20.disabled = False

                    MDFlatButton:
                        text: "SET STYLE"
                        on_release:
                            app.theme_cls.theme_style = "Dark" \
                            if app.theme_cls.theme_style == "Light" \
                            else "Light"

                MDBoxLayout:
                    orientation: "vertical"
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True
                    md_bg_color: 0, 0, 0, .2

                    MDLabel:
                        text: "MDFillRoundFlatButton from Python"
                        adaptive_height: True
                        halign: "center"
                        font_style: "H6"

                    MDBoxLayout:
                        id: python_box_9
                        padding: 20
                        spacing: "10dp"
                        adaptive_height: True

                # MDFillRoundFlatIconButton

                MDSeparator:

                MDLabel:
                    text: "MDFillRoundFlatIconButton from KV"
                    adaptive_height: True
                    halign: "center"
                    font_style: "H6"
            
                MDBoxLayout:
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True

                    MDFillRoundFlatIconButton:
                        id: btn_21
                        text: "MDFillRoundFlatIconButton"

                    MDFillRoundFlatIconButton:
                        id: btn_22
                        text: "MDFillRoundFlatIconButton"
                        font_style: "H5"
        
                    MDFillRoundFlatIconButton:
                        text: "MDFillRoundFlatIconButton 333"
                        disabled: True
        
                MDBoxLayout:
                    adaptive_size: True

                    MDFlatButton:
                        text: "SET TEXT COLOR"
                        on_release:
                            btn_21.theme_text_color = "Custom"
                            btn_21.text_color = (1, 0, 1, 1)
                            btn_22.theme_text_color = "Custom"
                            btn_22.text_color = (0, 0, 1, 1)

                    MDFlatButton:
                        text: "SET ICON COLOR"
                        on_release:
                            btn_21.icon_color = (1, 0, 1, 1)
                            btn_22.icon_color = (0, 1, 0, 1)

                    MDFlatButton:
                        text: "SET BG COLOR"
                        on_release:
                            btn_21.md_bg_color = (0, 0, 1, 1)
                            btn_22.md_bg_color = (1, 0, 0, 1)
        
                    MDFlatButton:
                        text: "DISABLED"
                        on_release:
                            btn_21.disabled = True
                            btn_22.disabled = True
        
                    MDFlatButton:
                        text: "UNDISABLED"
                        on_release:
                            btn_21.disabled = False
                            btn_22.disabled = False

                    MDFlatButton:
                        text: "SET STYLE"
                        on_release:
                            app.theme_cls.theme_style = "Dark" \
                            if app.theme_cls.theme_style == "Light" \
                            else "Light"

                    MDFlatButton:
                        text: "SET PALETTE"
                        on_release:
                            app.theme_cls.primary_palette = "Yellow"

                MDBoxLayout:
                    orientation: "vertical"
                    padding: 20
                    spacing: "10dp"
                    adaptive_height: True
                    md_bg_color: 0, 0, 0, .2

                    MDLabel:
                        text: "MDFillRoundFlatIconButton from Python"
                        adaptive_height: True
                        halign: "center"
                        font_style: "H6"

                    MDBoxLayout:
                        id: python_box_10
                        padding: 20
                        spacing: "10dp"
                        adaptive_height: True
"""


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        # MDIconButton
        self.root.ids.python_box.add_widget(
            MDIconButton(
                icon="language-python",
                user_font_size="24sp",
            )
        )
        self.root.ids.python_box.add_widget(
            MDIconButton(
                icon="language-python",
                user_font_size="36sp",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                md_bg_color=(1, 0, 1, 1),
            )
        )
        self.root.ids.python_box.add_widget(
            MDIconButton(
                icon="language-python",
                user_font_size="48sp",
                theme_text_color="Custom",
                text_color=(0, 0, 1, 1),
            )
        )
        self.root.ids.python_box.add_widget(
            MDIconButton(
                icon="language-python",
                user_font_size="56sp",
                disabled=True,
            )
        )
        # MDFloatingActionButton
        self.root.ids.python_box_2.add_widget(
            MDFloatingActionButton(icon="language-python")
        )
        self.root.ids.python_box_2.add_widget(
            MDFloatingActionButton(
                icon="language-python",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                md_bg_color=(1, 0, 1, 1),
            )
        )
        self.root.ids.python_box_2.add_widget(
            MDFloatingActionButton(
                icon="language-python",
                theme_text_color="Custom",
                text_color=(0, 0, 1, 1),
            )
        )
        self.root.ids.python_box_2.add_widget(
            MDFloatingActionButton(
                icon="language-python",
                disabled=True,
            )
        )
        # MDFlatButton
        self.root.ids.python_box_3.add_widget(MDFlatButton(text="MDFlatButton"))
        self.root.ids.python_box_3.add_widget(
            MDFlatButton(
                text="MDFlatButton",
                theme_text_color="Custom",
                text_color=(0, 1, 0, 1),
                font_style="H5",
            )
        )
        self.root.ids.python_box_3.add_widget(
            MDFlatButton(
                text="MDFlatButton",
                disabled=True,
            )
        )
        # MDRaisedButton
        self.root.ids.python_box_4.add_widget(
            MDRaisedButton(text="MDRaisedButton")
        )
        self.root.ids.python_box_4.add_widget(
            MDRaisedButton(
                text="MDFlatButton",
                md_bg_color=(0, 0, 1, 1),
                font_style="H5",
            )
        )
        self.root.ids.python_box_4.add_widget(
            MDRaisedButton(
                text="MDFlatButton",
                disabled=True,
            )
        )
        # MDRectangleFlatButton
        self.root.ids.python_box_5.add_widget(
            MDRectangleFlatButton(text="MDRectangleFlatButton")
        )
        self.root.ids.python_box_5.add_widget(
            MDRectangleFlatButton(
                text="MDRectangleFlatButton",
                line_color=(0, 0, 1, 1),
                theme_text_color="Custom",
                text_color=(1, 0, 1, 1),
                font_style="H5",
            )
        )
        self.root.ids.python_box_5.add_widget(
            MDRectangleFlatButton(
                text="MDRectangleFlatButton",
                disabled=True,
            )
        )
        # MDRectangleFlatIconButton
        self.root.ids.python_box_6.add_widget(
            MDRectangleFlatIconButton(
                icon="language-python",
                text="MDRectangleFlatIconButton",
            )
        )
        self.root.ids.python_box_6.add_widget(
            MDRectangleFlatIconButton(
                icon="language-python",
                text="MDRectangleFlatIconButton",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style="H5",
                line_color=(0, 0, 1, 1),
                icon_color=(1, 1, 0, 1),
            )
        )
        self.root.ids.python_box_6.add_widget(
            MDRectangleFlatIconButton(
                icon="language-python",
                text="MDRectangleFlatIconButton",
                disabled=True,
            )
        )
        # MDRoundFlatButton
        self.root.ids.python_box_7.add_widget(
            MDRoundFlatButton(
                text="MDRoundFlatButton",
            )
        )
        self.root.ids.python_box_7.add_widget(
            MDRoundFlatButton(
                text="MDRoundFlatButton",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                line_color=(0, 0, 1, 1),
                font_style="H5",
            )
        )
        self.root.ids.python_box_7.add_widget(
            MDRoundFlatButton(
                text="MDRoundFlatButton",
                disabled=True,
            )
        )
        # MDRoundFlatIconButton
        self.root.ids.python_box_8.add_widget(
            MDRoundFlatIconButton(
                icon="language-python",
                text="MDRoundFlatIconButton",
            )
        )
        self.root.ids.python_box_8.add_widget(
            MDRoundFlatIconButton(
                icon="language-python",
                text="MDRoundFlatIconButton",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                line_color=(1, 0, 1, 1),
                icon_color=(0, 0, 1, 1),
                font_style="H5",
            )
        )
        self.root.ids.python_box_8.add_widget(
            MDRoundFlatIconButton(
                icon="language-python",
                text="MDRoundFlatIconButton",
                disabled=True,
            )
        )
        # MDFillRoundFlatButton
        self.root.ids.python_box_9.add_widget(
            MDFillRoundFlatButton(
                text="MDFillRoundFlatButton",
            )
        )
        self.root.ids.python_box_9.add_widget(
            MDFillRoundFlatButton(
                text="MDFillRoundFlatButton",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                md_bg_color=(1, 0, 1, 1),
                font_style="H5",
            )
        )
        self.root.ids.python_box_9.add_widget(
            MDFillRoundFlatButton(
                text="MDFillRoundFlatButton",
                disabled=True,
            )
        )
        # MDFillRoundFlatIconButton
        self.root.ids.python_box_10.add_widget(
            MDFillRoundFlatIconButton(
                text="MDFillRoundFlatIconButton",
            )
        )
        self.root.ids.python_box_10.add_widget(
            MDFillRoundFlatIconButton(
                text="MDFillRoundFlatIconButton",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                md_bg_color=(1, 0, 1, 1),
                icon_color=(0, 0, 1, 1),
                font_style="H5",
            )
        )
        self.root.ids.python_box_10.add_widget(
            MDFillRoundFlatIconButton(
                text="MDFillRoundFlatIconButton",
                disabled=True,
            )
        )


Test().run()
