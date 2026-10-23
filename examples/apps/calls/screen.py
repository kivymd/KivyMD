from faker import Faker
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.utils import get_color_from_hex, platform

from examples.apps.calls.components import (  # NOQA
    CallsTile,
    DropDownLeftMenu,
    DropDownRightMenu,
    TabBarHorizontal,
    TextFieldSearch,
)
from kivymd.uix.behaviors import IOSLiquidDropdownContainer
from kivymd.uix.boxlayout import IOSBoxLayout
from kivymd.uix.screen import MDScreen

fake = Faker("en_US")

Builder.load_string("""
<CallsScreen>
    md_bg_color: self.theme_cls.backgroundColor

    MDBoxLayout:
        orientation: "vertical"
        padding: ["16dp", 0, "16dp", 0]

        MDRecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'
            bar_width: 0

            MDRecycleBoxLayout:
                orientation: "vertical"
                spacing: dp(10)
                padding: dp(10), tabs_top.height + dp(10), 0, dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height

    IOSButton:
        id: trigger_btn_left
        adaptive_width: True
        size_hint_y: None
        height: tabs_top.height
        border_radius: [dp(28)] * 4
        target_background: rv
        x: dp(12)
        y: root.height - (self.height + dp(12) + root.ios_pad)

        IOSButtonText:
            text: "  Edit  "
            theme_text_color: "Custom"
            text_color: "white"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

    TabBarHorizontal:
        id: tabs_top
        target_background: rv
        items_data: [("", "All"), ("", "Missed")]
        display_mode: "text"
        y: root.height - (self.height + dp(12) + root.ios_pad)
        pos_hint: {"center_x": 0.5}

    IOSButton:
        id: trigger_btn_right
        size_hint: None, None
        size: tabs_top.height, tabs_top.height
        border_radius: [tabs_top.height] * 4
        target_background: rv
        x: root.width - (self.width + dp(12))
        y: root.height - (self.height + dp(12) + root.ios_pad)

        IOSIconButton:
            icon: "filter-variant"
            theme_icon_color: "Custom"
            icon_color: "white"
            padding: dp(-2), 0, 0, 0

    TabBarHorizontal:
        id: tabs_bottom
        glass_color: [1.0, 1.0, 1.0, 0.35]
        target_background: rv
        items_data:
            [ \
            ("star", "Favorites"), \
            ("clock-time-three-outline", "Recent"), \
            ("bell", "Contacts"), \
            ("account-supervisor-circle-outline", "Account") \
            ]
        display_mode: "both"
        y: dp(12)
        pos_hint: {"center_x": 0.5}
""")


class CallsScreen(MDScreen):
    ios_pad = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if platform == "ios":
            self.ios_pad = dp(24)

        self.ids.rv.data.append(
            {
                "viewclass": "MDLabel",
                "text": "Recent",
                "padding": [0, dp(18), 0, 0],
                "adaptive_height": True,
                "bold": True,
                "font_style": "Title",
            }
        )
        self.ids.rv.data.append(
            {
                "viewclass": "TextFieldSearch",
                "target_background": self,
                "hint_text": "Search",
            }
        )

        for i in range(1, 20):
            kind = fake.random_element(elements=("person", "phone", "company"))
            color = fake.random_element(elements=("red", "white"))

            if kind == "person":
                title = fake.name()
                text = fake.random_element(elements=("Mobile", "Phone"))
                icon = "account"
            elif kind == "phone":
                title = fake.phone_number()
                text = fake.random_element(elements=("Mobile", "Phone"))
                icon = "phone"
            else:  # company
                title = fake.company()
                text = "Company"
                icon = "domain"

            self.ids.rv.data.append(
                {
                    "viewclass": "CallsTile",
                    "icon": icon,
                    "trailing_icon": "information-outline",
                    "title": title,
                    "text": text,
                    "color": color,
                    "divider": True,
                }
            )

        Clock.schedule_once(
            lambda dt: self._setup_dropdown(
                trigger_id="trigger_btn_left",
                menu_cls=DropDownLeftMenu,
                direction="bottom-right",
                menu_size=(dp(300), dp(130)),
            )
        )
        Clock.schedule_once(
            lambda dt: self._setup_dropdown(
                trigger_id="trigger_btn_right",
                menu_cls=DropDownRightMenu,
                direction="bottom-left",
                menu_size=(dp(280), dp(300)),
            )
        )

    def _setup_dropdown(self, trigger_id, menu_cls, direction, menu_size):
        trigger_btn = self.ids[trigger_id]

        dropdown_container = IOSLiquidDropdownContainer(
            direction=direction,
            glass_color=get_color_from_hex("#7EACF9")[:-1] + [0.3],
            spacing=dp(8),
        )

        menu = IOSBoxLayout(
            menu_cls(dropdown_container=dropdown_container),
            size_hint=[None, None],
            size=menu_size,
            orientation="vertical",
            padding=dp(8),
        )
        menu.border_radius = [dp(38)] * 4

        trigger_btn.bind(
            on_release=lambda x: dropdown_container.toggle_dropdown()
        )

        dropdown_container.widgets = [menu]
        dropdown_container.caller = trigger_btn
        dropdown_container.menu = menu

        self.add_widget(dropdown_container)
