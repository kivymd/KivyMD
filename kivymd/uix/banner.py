"""
Banner
======

Tooltips display informative text when users hover over, focus on,
or tap an element.

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Menus <https://material.io/components/banners>`_

Example
-------

from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.app import MDApp

Builder.load_string('''
<ExampleBanner@Screen>

    MDBanner:
        id: banner
        over_widget: scroll


    MDToolbar:
        id: toolbar
        title: "Example Banners"
        md_bg_color: app.theme_cls.primary_color
        elevation: 10
        left_action_items: [['dots-vertical', lambda x: None]]
        pos_hint: {'top': 1}

    ScrollView:
        id: scroll
        size_hint_y: None
        height: Window.height - toolbar.height

        GridLayout:
            id: box
            size_hint_y: None
            height: self.minimum_height
            cols: 1
            padding: "10dp"
            spacing: "10dp"

            OneLineListItem:
                text: "ThreeLineBanner"
                on_release:
                    banner.type = "three-line"
                    banner.text = \
                    [\
                    "Three line string text example with two actions.", \
                    "This is the second line of the banner message,", \
                    "and this is the third line of the banner message.",
                    ]
                    banner.left_action = ["CANCEL", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "TwoLineBanner"
                on_release:
                    banner.type = "two-line"
                    banner.text = \
                    [\
                    "One line string text example with two actions.", \
                    "This is the second line of the banner message.", \
                    ]
                    banner.left_action = ["CANCEL", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "OneLineBanner"
                on_release:
                    banner.type = "one-line"
                    banner.text = ["One line string text example with two actions."]
                    banner.left_action = ["CANCEL", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "ThreeLineIconBanner"
                on_release:
                    banner.type = "three-line-icon"
                    banner.text = \
                    [\
                    "Three line string text example with two actions.", \
                    "This is the second line of the banner message,", \
                    "and this is the third line of the banner message.",
                    ]
                    banner.left_action = ["CANCEL", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "TwoLineIconBanner"
                on_release:
                    banner.type = "two-line-icon"
                    banner.text = \
                    [\
                    "One line string text example with two actions.", \
                    "This is the second line of the banner message.", \
                    ]
                    banner.left_action = ["CANCEL", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "OneLineIconBanner"
                on_release:
                    banner.type = "one-line-icon"
                    banner.text = ["One line string text example with two actions."]
                    banner.left_action = ["CANCEL", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "Banner without actions"
                on_release:
                    banner.type = "one-line-icon"
                    banner.text = ["One line string text example without actions."]
                    banner.left_action = []
                    banner.right_action = []
                    banner.show()

            OneLineListItem:
                text: "Banner with one actions"
                on_release:
                    banner.type = "one-line-icon"
                    banner.text = ["One line string text example without actions."]
                    banner.left_action = []
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()
''')


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "DeepPurple"

    def build(self):
        return Factory.ExampleBanner()


Test().run()
"""

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ObjectProperty,
    ListProperty,
    StringProperty,
    OptionProperty,
)

from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.list import (
    ThreeLineAvatarListItem,
    TwoLineAvatarListItem,
    OneLineAvatarListItem,
    ThreeLineListItem,
    TwoLineListItem,
    OneLineListItem,
)

Builder.load_string(
    """
#:import Window kivy.core.window.Window
#:import Clock kivy.clock.Clock


<ThreeLineIconBanner>
    text: root.text_message[0]
    secondary_text: root.text_message[1]
    tertiary_text: root.text_message[2]
    divider: None
    _no_ripple_effect: True

    ImageLeftWidget:
        source: root.icon


<TwoLineIconBanner>
    text: root.text_message[0]
    secondary_text: root.text_message[1]
    divider: None
    _no_ripple_effect: True

    ImageLeftWidget:
        source: root.icon


<OneLineIconBanner>
    text: root.text_message[0]
    divider: None
    _no_ripple_effect: True

    ImageLeftWidget:
        source: root.icon


<ThreeLineBanner>
    text: root.text_message[0]
    secondary_text: root.text_message[1]
    tertiary_text: root.text_message[2]
    divider: None
    _no_ripple_effect: True


<TwoLineBanner>
    text: root.text_message[0]
    secondary_text: root.text_message[1]
    divider: None
    _no_ripple_effect: True


<OneLineBanner>
    text: root.text_message[0]
    divider: None
    _no_ripple_effect: True


<MDBanner>
    size_hint_y: None
    height: self.minimum_height
    banner_y: 0
    orientation: "vertical"
    y: Window.height - self.banner_y

    canvas:
        Color:
            rgba: 0, 0, 0, 0
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        id: container_message
        size_hint_y: None
        height: self.minimum_height

    BoxLayout:
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {"right": 1}
        padding: 0, 0, "8dp", "8dp"
        spacing: "8dp"

        BoxLayout:
            id: left_action_box
            size_hint: None, None
            size: self.minimum_size
    
        BoxLayout:
            id: right_action_box
            size_hint: None, None
            size: self.minimum_size
"""
)


class BaseBanner:
    text_message = ListProperty(["", "", ""])
    icon = StringProperty()


class ThreeLineIconBanner(ThreeLineAvatarListItem, BaseBanner):
    pass


class TwoLineIconBanner(TwoLineAvatarListItem, BaseBanner):
    pass


class OneLineIconBanner(OneLineAvatarListItem, BaseBanner):
    pass


class ThreeLineBanner(ThreeLineListItem, BaseBanner):
    pass


class TwoLineBanner(TwoLineListItem, BaseBanner):
    pass


class OneLineBanner(OneLineListItem, BaseBanner):
    pass


class MDBanner(MDCard):
    icon = StringProperty("data/logo/kivy-icon-128.png")
    """Icon banner."""

    over_widget = ObjectProperty()
    """
    The widget that is under the banner.
    It will be shifted down to the height of the banner.
    """

    text = ListProperty()
    """The action of banner.

    List of lines for banner text. Must contain no more than three lines for a
    `one-line`, `two-line` and `three-line` banner, respectively.
    """

    left_action = ListProperty()
    """The action of banner.

    To add one action, append a list like the following:
        ["name_action", callback]
    where `name_action` is a string that corresponds to an action name and
    `callback` is the function called on a touch release event.
    """

    right_action = ListProperty()
    """Works the same way as :attr:`left_action`."""

    type = OptionProperty(
        None,
        options=[
            "one-line",
            "two-line",
            "three-line",
            "one-line-icon",
            "two-line-icon",
            "three-line-icon",
        ],
        allownone=True,
    )
    """Banner type."""

    _type_message = None
    _progress = False

    def add_actions_buttons(self, box, data):
        if data:
            name_action_button, function_action_button = data
            action_button = MDFlatButton(
                text=f"[b]{name_action_button}[/b]",
                theme_text_color="Custom",
                text_color=self.theme_cls.primary_color,
                on_release=function_action_button,
            )
            action_button.markup = True
            box.add_widget(action_button)

    def set_left_action(self):
        self.add_actions_buttons(self.ids.left_action_box, self.left_action)

    def set_right_action(self):
        self.add_actions_buttons(self.ids.right_action_box, self.right_action)

    def set_type_banner(self):
        self._type_message = {
            "three-line-icon": ThreeLineIconBanner,
            "two-line-icon": TwoLineIconBanner,
            "one-line-icon": OneLineIconBanner,
            "three-line": ThreeLineBanner,
            "two-line": TwoLineBanner,
            "one-line": OneLineBanner,
        }[self.type]

    def add_banner_to_container(self):
        self.ids.container_message.add_widget(
            self._type_message(text_message=self.text, icon=self.icon)
        )

    def show(self):
        def show(interval):
            self.set_type_banner()
            self.set_left_action()
            self.set_right_action()
            self.add_banner_to_container()
            Clock.schedule_once(self.animation_display_banner, 0.1)

        if self._progress:
            return
        self._progress = True
        if self.ids.container_message.children:
            self.hide()
        Clock.schedule_once(show, 0.7)

    def animation_display_banner(self, i):
        Animation(banner_y=self.height + dp(68), d=0.15, t="in_quad").start(
            self
        )
        anim = Animation(
            y=self.over_widget.y - self.height, d=0.15, t="in_quad"
        )
        anim.bind(on_complete=self._reset_progress)
        anim.start(self.over_widget)

    def hide(self):
        def hide(interval):
            anim = Animation(banner_y=0, d=0.15)
            anim.bind(on_complete=self._remove_banner)
            anim.start(self)
            Animation(y=self.over_widget.y + self.height, d=0.15).start(
                self.over_widget
            )

        Clock.schedule_once(hide, 0.5)

    def _remove_banner(self, *args):
        self.ids.container_message.clear_widgets()
        self.ids.left_action_box.clear_widgets()
        self.ids.right_action_box.clear_widgets()

    def _reset_progress(self, *args):
        self._progress = False
