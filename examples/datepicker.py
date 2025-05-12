import datetime

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import BooleanProperty, StringProperty

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import (
    MDDockedDatePicker,
    MDModalDatePicker,
    MDModalInputDatePicker,
)

KV = """
<SelectedItem>
    adaptive_height: True
    spacing: "12dp"

    MDCheckbox:
        group: root.group
        on_active: root.dispatch("on_active", self.active)
        active: root.active

    MDLabel:
        text: root.text
        theme_line_height: "Custom"
        adaptive_height: True
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

        MDTextField:
            id: field
            mode: "outlined"
            on_focus: app.open_date_picker(self.focus)

            MDTextFieldHintText:
                id: field_hint
                text: "Modal data picker"

            MDTextFieldHelperText:
                text: "MM/DD/YYYY"
                mode: "persistent"

            MDTextFieldTrailingIcon:
                icon: "calendar"

        Widget:

        MDLabel:
            text: "Properties"
            adaptive_height: True
            pos_hint: {'center_y': .5}

        SelectedItem:
            text: "With range"
            group: "range"
            on_active: app.set_range(*args)

        MDLabel:
            text: "Type"
            adaptive_height: True
            pos_hint: {'center_y': .5}

        MDBoxLayout:
            adaptive_height: True
            spacing: "12dp"

            SelectedItem:
                text: "Modal"
                active: True
                on_active: app.set_type_dialog(*args, "Modal")

            SelectedItem:
                text: "Docked"
                on_active: app.set_type_dialog(*args, "Docked")

            SelectedItem:
                text: "Input"
                on_active: app.set_type_dialog(*args, "Input")
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
    type_dialog = "Modal"
    date_picker = None
    min_date = None
    max_date = None
    mode = "picker"
    mark_today = True

    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)

    def set_range(self, instance_check, active):
        if active:
            self.min_date = datetime.date.today()
            self.max_date = datetime.date(
                datetime.date.today().year,
                datetime.date.today().month,
                datetime.date.today().day + 4,
            )
            self.mode = "range"
            self.mark_today = False
        else:
            self.min_date = None
            self.max_date = None
            self.mode = "picker"
            self.mark_today = True

    def set_type_dialog(self, instance_check, active, type_dialog):
        if active:
            self.type_dialog = type_dialog
            self.root.ids.field_hint.text = f"{type_dialog} dara picker"

    def on_ok(self, *args):
        print(self.date_picker.get_date())
        self.on_cancel()

    def on_cancel(self, *args):
        if self.date_picker:
            self.date_picker.dismiss()

    def open_date_picker(self, focus, dialog=None):
        if not focus:
            return

        if self.type_dialog == "Modal":
            dialog = MDModalDatePicker
        elif self.type_dialog == "Input":
            dialog = MDModalInputDatePicker
        elif self.type_dialog == "Docked":
            dialog = MDDockedDatePicker

        if dialog:
            self.date_picker = dialog(
                min_date=self.min_date,
                max_date=self.max_date,
                mode=self.mode,
                mark_today=self.mark_today,
            )
            self.date_picker.bind(
                on_ok=self.on_ok,
                on_cancel=self.on_cancel,
            )
            self.date_picker.pos = [
                self.root.ids.field.center_x - self.date_picker.width / 2,
                self.root.ids.field.y - (self.date_picker.height + dp(32)),
            ]
            self.date_picker.open()

    def disabled_widgets(self): ...


Example().run()
