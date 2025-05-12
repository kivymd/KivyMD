import time

from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import (
    MDTimePickerDialHorizontal,
    MDTimePickerDialVertical,
    MDTimePickerInput,
)

KV = """
<SelectedItem>
    adaptive_size: True
    spacing: "12dp"

    MDCheckbox:
        group: root.group
        on_active: root.dispatch("on_active", self.active)
        active: root.active

    MDLabel:
        text: root.text
        theme_line_height: "Custom"
        adaptive_size: True
        pos_hint: {'center_y': .5}
        line_height: 1


MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: dp(12)
        icon: "menu"

    MDBoxLayout:
        orientation: "vertical"
        pos_hint: {'center_x': .5}
        size_hint_x: .5
        padding: "24dp"
        spacing: "24dp"

        Widget:

        MDLabel:
            text: "Properties"
            adaptive_height: True
            pos_hint: {'center_y': .5}

        SelectedItem:
            text: "Current time"
            group: "range"
            on_active: app.set_current_time(*args)

        MDBoxLayout:
            adaptive_size: True
            spacing: "12dp"

            SelectedItem:
                text: "AM"
                group: "AMPM"
                active: True
                on_active: app.set_am_pm("am")

            SelectedItem:
                text: "PM"
                group: "AMPM"
                on_active: app.set_am_pm("pm")

        MDLabel:
            text: "Type"
            adaptive_height: True
            pos_hint: {'center_y': .5}

        MDBoxLayout:
            adaptive_height: True
            spacing: "12dp"

            SelectedItem:
                text: "Vertical"
                active: True
                on_active: app.set_type_dialog(*args, "Vertical")

            SelectedItem:
                text: "Horizontal"
                on_active: app.set_type_dialog(*args, "Horizontal")

            SelectedItem:
                text: "Input"
                on_active: app.set_type_dialog(*args, "Input")

    MDButton:
        pos_hint: {'center_x': .5, 'center_y': .7}
        on_release: app.open_time_picker()

        MDButtonText:
            text: "Open time picker"
"""


class SelectedItem(MDBoxLayout):
    active = BooleanProperty(False)
    text = StringProperty()
    group = StringProperty("type")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_active")

    def on_active(self, *args): ...


class Example(MDApp, CommonApp):
    type_dialog = "Vertical"
    time_picker = None
    current_time = False
    am_pm = "am"

    def build(self):
        self.theme_cls.primary_palette = "Olive"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def set_am_pm(self, time_mode):
        self.am_pm = time_mode

    def set_current_time(self, instance_check, active):
        if active:
            self.current_time = True
        else:
            self.current_time = False

    def set_type_dialog(self, instance_check, active, type_dialog):
        if active:
            self.type_dialog = type_dialog

    def on_ok(self, *args):
        print(self.time_picker.time)
        self.on_cancel()

    def on_cancel(self, *args):
        if self.time_picker:
            self.time_picker.dismiss()

    def open_time_picker(self, dialog=None):
        if self.type_dialog == "Vertical":
            dialog = MDTimePickerDialVertical
        elif self.type_dialog == "Input":
            dialog = MDTimePickerInput
        elif self.type_dialog == "Horizontal":
            dialog = MDTimePickerDialHorizontal

        if dialog:
            self.time_picker = dialog(
                am_pm=self.am_pm,
                hour=time.strftime("%H") if self.current_time else "12",
                minute=time.strftime("%M") if self.current_time else "0",
            )
            self.time_picker.bind(
                on_ok=self.on_ok,
                on_cancel=self.on_cancel,
            )
            self.time_picker.open()

    def disabled_widgets(self): ...


Example().run()
