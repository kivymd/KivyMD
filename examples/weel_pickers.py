import calendar

from kivy.metrics import dp

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.pickers import (
    IOSWheelPicker,
    IOSWheelPickerLabel,
    IOSWheelPickerUnitLabel,
)
from kivymd.uix.screen import MDScreen


class ContentBox(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = dp(20)
        self.size_hint = (None, None)
        self.size = (dp(600), dp(450))
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        months = list(calendar.month_name)[1:]
        custom_cols_1 = [
            (1, 31, 20, "DAY"),
            (1900, 2026, 2020, "YEAR"),
            (months, "August", "Month"),
        ]
        custom_cols_2 = [
            (1, 31, 20),
            (1900, 2026, 2020),
            (months, "August"),
        ]

        self.widgets = [
            IOSWheelPicker(
                IOSWheelPickerLabel(
                    bold=True,
                ),
                IOSWheelPickerUnitLabel(
                    bold=True,
                ),
                columns=custom_cols_1,
                visible_count=5,
                picker_width=dp(600),
                curve_factor=dp(35),
                on_select=self.on_picker_select,
            ),
            IOSWheelPicker(
                IOSWheelPickerLabel(
                    bold=True,
                ),
                columns=custom_cols_2,
                visible_count=5,
                picker_width=dp(600),
                curve_factor=dp(35),
                on_select=self.on_picker_select,
            ),
        ]

    def on_picker_select(self, instance, values):
        print(instance, values)


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        menu = MDIconButton(
            pos_hint={"top": 0.98},
            x="12dp",
            icon="menu",
        )
        menu.bind(on_release=lambda x: MDApp.get_running_app().open_menu(menu))

        self.widgets = [
            ContentBox(),
            menu,
        ]


class TimePickerApp(MDApp, CommonApp):
    def build(self):
        return MainScreen(
            md_bg_color=self.theme_cls.backgroundColor,
        )


if __name__ == "__main__":
    TimePickerApp().run()
