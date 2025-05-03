import os

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

import kivymd
from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.transition import MDSharedAxisTransition

KV = """
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, 1
    width:self.height

<SettingsItem@ButtonBehavior+BoxLayout>:
    icon:"wifi"
    text:"Network & Internet"
    subtext:"Network settings"
    size_hint_y:None
    height:dp(70)
    padding:dp(10)
    spacing:dp(10)
    on_release:
        app.root.get_screen("battery").ids.main_icon.icon = self.icon
        app.root.get_screen("battery").ids.main_text.text = self.text
        app.root.transition.opposite = False
        app.root.current = "battery"
    MDIconButton:
        style: "tonal"
        size_hint:None, 1
        width:self.height
        icon:root.icon
    BoxLayout:
        orientation:"vertical"
        MDLabel:
            text:root.text
            font_style:"Title"
            role:"medium"
        MDLabel:
            text:root.subtext
            font_style:"Label"
            role:"large"
            text_color:app.theme_cls.onSurfaceVariantColor

<SettingsScreen@MDScreen>:
    name:"main"
    md_bg_color:app.theme_cls.surfaceContainerLowColor
    MDBoxLayout:
        padding:[dp(10), 0]
        orientation:"vertical"
        BoxLayout:
            size_hint_y:None
            height:dp(70)
            padding:[0, dp(10)]
            MDIconButton:
                size_hint:None, None
                size:[dp(50)] * 2
                on_release: app.open_menu(self)
                icon: "menu"
            Widget:
            MDIconButton:
                size_hint:None, None
                size:[dp(50)] * 2
                on_release: app.open_menu(self)
                icon: "magnify"
            MDIconButton:
                size_hint:None, None
                size:[dp(50)] * 2
                on_release: app.open_menu(self)
                icon: "dots-vertical"
        MDLabel:
            text:"Settings"
            halign:"center"
            theme_font_size:"Custom"
            font_size:"30sp"
            style:"bold"
            size_hint_y:None
            height:dp(70)
        MDBoxLayout:
            md_bg_color:app.theme_cls.surfaceContainerHighColor
            padding:[dp(10), 0]
            radius:[self.height / 2]*4
            size_hint_y:None
            height:dp(60)
            padding:[dp(10), dp(10)]
            spacing:dp(10)
            MDIconButton:
                size_hint_y:1
                icon:"magnify"
                size_hint_x:None
                width:self.height
            MDLabel:
                text:"Search in settings"
                font_style:"Body"
                role:"large"
                theme_text_color:"Custom"
                text_color:app.theme_cls.onSurfaceVariantColor
            Image:
                size_hint_y:1
                source:app.image_path
                size_hint_x:None
                width:self.height
        BoxLayout:
            size_hint_y:None
            height:dp(20)
        MDBoxLayout:
            md_bg_color:app.theme_cls.surfaceContainerHighColor
            radius:[dp(25)] * 4
            size_hint_y:None
            height:self.minimum_height
            orientation:"vertical"
            SettingsItem:
                icon:"wifi"
            SettingsItem:
                icon:"battery-90"
                text:"Battery & Power"
                subtext:"42% - About 14hr left"
            SettingsItem:
                icon:"palette-outline"
                text:"Wallpaper & Style"
                subtext:"Colors, theme style"
            SettingsItem:
                icon:"android"
                text:"System Info"
                subtext:"About system"
        BoxLayout:
            size_hint_y:None
            height:dp(70)
            padding:[(self.width - dp(50)*6), dp(25)]
            spacing:dp(10)
            Check:
                active:True
                on_active:
                    setattr(app.transition, "transition_axis", "x") if self.active else app
            MDLabel:
                size_hint_x:None
                width:dp(50)
                text:"X"
            Check:
                on_active:
                    setattr(app.transition, "transition_axis", "y") if self.active else app
            MDLabel:
                size_hint_x:None
                width:dp(50)
                text:"Y"
            Check:
                on_active:
                    setattr(app.transition, "transition_axis", "z") if self.active else app
            MDLabel:
                size_hint_x:None
                width:dp(50)
                text:"Z"
        BoxLayout:
            size_hint_y:None
            height:dp(100)
            orientation:"vertical"
            MDLabel:
                id:duration
                text:"Duration: 0.2"
                adaptive_height:True
                halign:"center"
            MDSlider:
                size_hint_y:None
                height:dp(50)
                step: 10
                value: 10
                on_value:
                    duration.text = "Duration: " + str(self.value / 50)
                    app.transition.duration = self.value/50
                MDSliderHandle:
        Widget:

<BatteryScreen@MDScreen>:
    name:"battery"
    md_bg_color:app.theme_cls.surfaceContainerLowColor
    MDLabel:
        id:main_text
        text:"Battery"
        halign:"center"
        theme_font_size:"Custom"
        font_size:"30sp"
        style:"bold"
        size_hint_y:None
        height:dp(100)
        pos_hint:{"center_y":0.8}
    MDIconButton:
        id:main_icon
        icon:"wifi"
        style:"tonal"
        pos_hint:{"center_y":0.7, "center_x":0.5}
    MDButton:
        pos_hint:{"center_x":0.5, "center_y":0.5}
        style: "filled"
        on_release:
            app.root.transition.opposite = True
            app.root.current = "main"
        MDButtonText:
            text: "Go Back"

MDScreenManager:
    id:s_m
    md_bg_color:app.theme_cls.surfaceContainerLowColor
    transition:app.transition
    SettingsScreen:
    BatteryScreen:
"""


class ExampleApp(MDApp, CommonApp):
    image_path = os.path.join(
        kivymd.__path__[0], "images", "logo", "kivymd-icon-256.png"
    )

    def build(self):
        self.transition = MDSharedAxisTransition()
        return Builder.load_string(KV)


ExampleApp().run()
