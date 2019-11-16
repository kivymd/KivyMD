"""
Chips
=====

Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Chips <https://material.io/design/components/chips.html>`_

Example
-------

from kivymd.app import MDApp
from kivy.lang import Builder

from kivymd.theming import ThemeManager

kv = '''
BoxLayout:
    orientation: 'vertical'
    spacing: dp(10)

    MDToolbar:
        title: 'Example Chips'
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: x]]
        background_palette: 'Primary'

    ScrollView:

        GridLayout:
            padding: dp(10)
            spacing: dp(10)
            cols: 1
            size_hint_y: None
            height: self.minimum_height

            MDLabel:
                text: 'Chips with color:'

            MDSeparator:

            StackLayout:
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(5)

                MDChip:
                    label: 'Coffee'
                    color: .4470588235294118, .19607843137254902, 0, 1
                    icon: 'coffee'
                    callback: app.callback

                MDChip:
                    label: 'Duck'
                    color: .9215686274509803, 0, 0, 1
                    icon: 'duck'
                    callback: app.callback

                MDChip:
                    label: 'Earth'
                    color: .21176470588235294, .09803921568627451, 1, 1
                    icon: 'earth'
                    callback: app.callback

                MDChip:
                    label: 'Face'
                    color: .20392156865098, .48235294117606, .43529411764705883, 1
                    icon: 'face'
                    callback: app.callback

                MDChip:
                    label: 'Facebook'
                    color: .5607843137254902, .48235294164706, .435294117705883, 1
                    icon: 'facebook'
                    callback: app.callback

            Widget:
                size_hint_y: None
                height: dp(5)

            MDLabel:
                text: 'Chip without icon:'

            MDSeparator:

            StackLayout:
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(5)

                MDChip:
                    label: 'Without icon'
                    icon: ''
                    callback: app.callback

            Widget:
                size_hint_y: None
                height: dp(5)

            MDLabel:
                text: 'Chips with check:'

            MDSeparator:

            StackLayout:
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(5)

                MDChip:
                    label: 'Check'
                    icon: ''
                    check: True
                    callback: app.callback

                MDChip:
                    label: 'Check with icon'
                    icon: 'city'
                    check: True
                    callback: app.callback
            Widget:
                size_hint_y: None
                height: dp(5)

            MDLabel:
                text: 'Choose chip:'

            MDSeparator:

            MDChooseChip:

                MDChip:
                    label: 'Earth'
                    icon: 'earth'
                    callback: app.callback

                MDChip:
                    label: 'Face'
                    icon: 'face'
                    callback: app.callback

                MDChip:
                    label: 'Facebook'
                    icon: 'facebook'
                    callback: app.callback
'''


class MyApp(MDApp):

    def callback(self, name_chip):
        pass

    def build(self):
        return Builder.load_string(kv)


MyApp().run()
"""

from kivy.metrics import dp
from kivy.properties import (
    StringProperty,
    ListProperty,
    ObjectProperty,
    BooleanProperty,
    NumericProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout

from kivymd.uix.button import MDIconButton
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
#:import DEVICE_TYPE kivymd.material_resources.DEVICE_TYPE


<MDChooseChip>
    size_hint_y: None
    height: self.minimum_height
    spacing: "5dp"


<MDChip>
    size_hint: None,  None
    height: "26dp"
    padding: 0, 0, "5dp", 0
    width:
        self.minimum_width - (dp(10) if DEVICE_TYPE == "desktop" else dp(20)) if root.icon != 'checkbox-blank-circle'\
        else self.minimum_width

    canvas:
        Color:
            rgba: root.color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [root.radius]

    BoxLayout:
        id: box_check
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_y': .5}

    BoxLayout:
        size_hint_x: None
        width: self.minimum_width
        padding: dp(10)

        Label:
            id: label
            text: root.label
            size_hint_x: None
            width: self.texture_size[0]

    MDIconButton:
        id: icon
        icon: root.icon
        size_hint_y: None
        height: "20dp"
        pos_hint: {"center_y": .5}
        user_font_size: "20dp"
        disabled: True
"""
)


class MDChip(BoxLayout, ThemableBehavior):
    label = StringProperty()
    """`MDChip` text."""

    icon = StringProperty("checkbox-blank-circle")
    """`MDChip` icon."""

    color = ListProperty([0.4, 0.4, 0.4, 1])
    """`MDChip` color."""

    check = BooleanProperty(False)
    """If True, a checkmark is added to the left when touch to the chip."""

    callback = ObjectProperty(lambda x: None)
    """Custom method."""

    radius = NumericProperty(dp(12))
    """Corner radius values."""

    def on_icon(self, instance, value):
        if value == "":
            self.icon = "checkbox-blank-circle"
            self.remove_widget(self.ids.icon)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.callback(self.label)
            md_choose_chip = self.parent
            if md_choose_chip.__class__ is MDChooseChip:
                if md_choose_chip.selected_chip:
                    md_choose_chip.selected_chip.color = (
                        md_choose_chip.selected_chip_color
                    )
                md_choose_chip.selected_chip = self
                md_choose_chip.selected_chip_color = self.color
                self.color = self.theme_cls.primary_color
            if self.check:
                if not len(self.ids.box_check.children):
                    self.ids.box_check.add_widget(
                        MDIconButton(
                            icon="check",
                            size_hint_y=None,
                            height=dp(20),
                            disabled=True,
                            user_font_size=dp(20),
                            pos_hint={"center_y": 0.5},
                        )
                    )
                else:
                    check = self.ids.box_check.children[0]
                    self.ids.box_check.remove_widget(check)


class MDChooseChip(StackLayout):
    selected_chip = None
    """The `MDChi`p object that is currently selected."""

    selected_chip_color = None
    """The color of the chip that is currently selected."""
