# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.properties import OptionProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
from kivy.utils import get_color_from_hex
from kivymd.backgroundcolorbehavior import SpecificBackgroundColorBehavior
from kivymd.button import MDIconButton
from kivymd.color_definitions import colors
from kivymd.elevationbehavior import RectangularElevationBehavior
from kivymd.theming import ThemableBehavior

Builder.load_string("""
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
<ColorSelector>:
    size: dp(40), dp(40)
    pos: self.pos
    size_hint: (None, None)
    canvas:
        Color:
            rgba: root.rgb_hex(root.color_name)
        Ellipse:
            size: self.size
            pos: self.pos

<AccentColorSelector@ColorSelector>:
    on_release: app.theme_cls.accent_palette = root.color_name

<PrimaryColorSelector@ColorSelector>:
    on_release: app.theme_cls.primary_palette = root.color_name

<MDThemePicker>:
    size_hint: (None, None)
    size: dp(284), dp(120)+dp(290)
    pos_hint: {'center_x': .5, 'center_y': .5}
    canvas:
        Color:
            rgb: app.theme_cls.primary_color
        Rectangle:
            size: self.width, dp(120)
            pos: root.pos[0], root.pos[1] + root.height-dp(120)
        Color:
            rgb: app.theme_cls.bg_normal
        Rectangle:
            size: self.width, dp(290)
            pos: root.pos[0], root.pos[1] + root.height-(dp(120)+dp(290))

    MDFlatButton:
        pos: root.pos[0]+root.size[0]-self.width-dp(10), root.pos[1] + dp(10)
        text: "Close"
        on_release: root.dismiss()
    MDLabel:
        font_style: "Headline"
        text: "Change theme"
        size_hint: (None, None)
        size: dp(160), dp(50)
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        theme_text_color: 'Custom'
        text_color: root.specific_text_color
    MDTabbedPanel:
        size_hint: (None, None)
        size: root.width, root.height-dp(135)
        pos_hint: {'center_x': 0.5, 'center_y': 0.475}
        id: tab_panel
        tab_display_mode:'text'

        MDTab:
            name: 'color'
            text: "Theme Color"
            BoxLayout:
                spacing: dp(4)
                size_hint: (None, None)
                size: dp(270), root.height  # -dp(120)
                pos_hint: {'center_x': 0.532, 'center_y': 0.89}
                orientation: 'vertical'
                BoxLayout:
                    size_hint: (None, None)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size: dp(230), dp(40)
                    pos: self.pos
                    halign: 'center'
                    orientation: 'horizontal'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Red'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Pink'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Purple'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'DeepPurple'
                BoxLayout:
                    size_hint: (None, None)
                    pos_hint: {'center_x': .5, 'center_y': 0.5}
                    size: dp(230), dp(40)
                    pos: self.pos
                    halign: 'center'
                    orientation: 'horizontal'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Indigo'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Blue'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'LightBlue'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Cyan'
                BoxLayout:
                    size_hint: (None, None)
                    pos_hint: {'center_x': .5, 'center_y': 0.5}
                    size: dp(230), dp(40)
                    pos: self.pos
                    halign: 'center'
                    orientation: 'horizontal'
                    padding: 0, 0, 0, dp(1)
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Teal'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Green'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'LightGreen'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Lime'
                BoxLayout:
                    size_hint: (None, None)
                    pos_hint: {'center_x': .5, 'center_y': 0.5}
                    size: dp(230), dp(40)
                    pos: self.pos
                    orientation: 'horizontal'
                    halign: 'center'
                    padding: 0, 0, 0, dp(1)
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Yellow'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Amber'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Orange'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'DeepOrange'
                BoxLayout:
                    size_hint: (None, None)
                    pos_hint: {'center_x': .5, 'center_y': 0.5}
                    size: dp(230), dp(40)
                    #pos: self.pos
                    orientation: 'horizontal'
                    padding: 0, 0, 0, dp(1)
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Brown'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'Grey'
                    BoxLayout:
                        PrimaryColorSelector:
                            color_name: 'BlueGrey'
                    BoxLayout:
                        MDIconButton:
                            size: dp(40), dp(40)
                            size_hint: (None, None)
                            canvas:
                                Color:
                                    rgba: app.theme_cls.bg_normal
                                Ellipse:
                                    size: self.size
                                    pos: self.pos
                            disabled: True

        MDTab:
            name: 'accent_color'
            text: "Accent Color"
            BoxLayout:
                spacing: dp(4)
                size_hint: (None, None)
                size: dp(270), root.height  # -dp(120)
                pos_hint: {'center_x': 0.532, 'center_y': 0.89}
                orientation: 'vertical'
                BoxLayout:
                    size_hint: (None, None)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size: dp(230), dp(40)
                    pos: self.pos
                    halign: 'center'
                    orientation: 'horizontal'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Red'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Pink'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Purple'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'DeepPurple'
                BoxLayout:
                    size_hint: (None, None)
                    pos_hint: {'center_x': .5, 'center_y': 0.5}
                    size: dp(230), dp(40)
                    pos: self.pos
                    halign: 'center'
                    orientation: 'horizontal'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Indigo'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Blue'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'LightBlue'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Cyan'
                BoxLayout:
                    size_hint: (None, None)
                    pos_hint: {'center_x': .5, 'center_y': 0.5}
                    size: dp(230), dp(40)
                    pos: self.pos
                    halign: 'center'
                    orientation: 'horizontal'
                    padding: 0, 0, 0, dp(1)
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Teal'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Green'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'LightGreen'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Lime'
                BoxLayout:
                    size_hint: (None, None)
                    pos_hint: {'center_x': .5, 'center_y': 0.5}
                    size: dp(230), dp(40)
                    pos: self.pos
                    orientation: 'horizontal'
                    halign: 'center'
                    padding: 0, 0, 0, dp(1)
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Yellow'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Amber'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Orange'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'DeepOrange'
                BoxLayout:
                    size_hint: (None, None)
                    pos_hint: {'center_x': .5, 'center_y': 0.5}
                    size: dp(230), dp(40)
                    #pos: self.pos
                    orientation: 'horizontal'
                    padding: 0, 0, 0, dp(1)
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Brown'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'Grey'
                    BoxLayout:
                        AccentColorSelector:
                            color_name: 'BlueGrey'
                    BoxLayout:
                        MDIconButton:
                            size: dp(40), dp(40)
                            size_hint: (None, None)
                            canvas:
                                Color:
                                    rgba: app.theme_cls.bg_normal
                                Ellipse:
                                    size: self.size
                                    pos: self.pos
                            disabled: True

        MDTab:
            name: 'style'
            text: "Theme Style"
            FloatLayout:
                size: self.size
                pos: self.pos
                BoxLayout:
                    size_hint: (None, None)
                    pos_hint: {'center_x': .5, 'center_y': .6}
                    halign: 'center'
                    valign: 'center'
                    spacing: dp(10)
                    width: dp(210)
                    height: dp(100)
                    MDIconButton:
                        size: dp(100), dp(100)
                        size_hint: (None, None)
                        canvas:
                            Color:
                                rgba: 1, 1, 1, 1
                            Ellipse:
                                size: self.size
                                pos: self.pos
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 1.
                                circle: (self.center_x, self.center_y, dp(50))
                        on_release: app.theme_cls.theme_style = 'Light'
                    MDIconButton:
                        size: dp(100), dp(100)
                        pos: self.pos
                        size_hint: (None, None)
                        canvas:
                            Color:
                                rgba: 0, 0, 0, 1
                            Ellipse:
                                size: self.size
                                pos: self.pos
                        on_release: app.theme_cls.theme_style = 'Dark'
""")


class ColorSelector(MDIconButton):
    color_name = OptionProperty(
            'Indigo',
            options=['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue',
                     'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
                     'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange',
                     'Brown', 'Grey', 'BlueGrey'])

    def rgb_hex(self, col):
        return get_color_from_hex(colors[col][self.theme_cls.accent_hue])


class MDThemePicker(ThemableBehavior, FloatLayout, ModalView,
                    SpecificBackgroundColorBehavior,
                    RectangularElevationBehavior):
    pass


if __name__ == "__main__":
    from kivy.app import App
    from kivymd.theming import ThemeManager

    class ThemePickerApp(App):
        theme_cls = ThemeManager()

        def build(self):
            main_widget = Builder.load_string("""
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
FloatLayout:
    MDRaisedButton:
        size_hint: None, None
        pos_hint: {'center_x': .5, 'center_y': .5}
        size: 3 * dp(48), dp(48)
        center_x: self.parent.center_x
        text: 'Open theme picker'
        on_release: MDThemePicker().open()
        opposite_colors: True
""")
            return main_widget

    ThemePickerApp().run()
