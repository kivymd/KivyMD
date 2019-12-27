"""
MDToolbar
=======

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, App bars: top <https://material.io/design/components/app-bars-top.html>`_

Example
-------

from kivy.factory import Factory

from kivymd.app import MDApp
from kivy.lang import Builder


Builder.load_string('''
<StyleLabel@MDLabel>:
    size_hint_y: None
    height: self.texture_size[1]


<StyleItemCheck@BoxLayout>:
    group: ""
    text: ""
    active: False
    size_hint_y: None
    height: self.minimum_height

    MDCheckbox:
        group: root.group
        active: root.active
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {"center_y": .5}
        on_active: app.callback(root.text, self.active)

    StyleLabel:
        text: root.text
        pos_hint: {"center_y": .5}


<BottomAppBar@Screen>
    name: 'bottom app bar'

    BoxLayout:
        spacing: dp(10)
        orientation: 'vertical'

        MDToolbar:
            title: "Title"
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['menu', lambda x: x]]

        ScrollView:

            GridLayout:
                size_hint_y: None
                height: self.minimum_height
                cols: 1
                padding: "10dp"
                spacing: "10dp"

                MDSeparator:

                StyleLabel:
                    text: "Notch"

                StyleItemCheck:
                    group: 'notch'
                    text: "On"
                    active: True

                StyleItemCheck:
                    group: 'notch'
                    text: "Off"

                MDSeparator:

                StyleLabel:
                    text: "Position"

                StyleItemCheck:
                    group: 'pos'
                    text: "Attached - Center"
                    active: True

                StyleItemCheck:
                    group: 'pos'
                    text: "Attached - End"

                StyleItemCheck:
                    group: 'pos'
                    text: "Free - Center"

                StyleItemCheck:
                    group: 'pos'
                    text: "Free - End"

        MDBottomAppBar

            MDToolbar:
                id: toolbar
                title: "Title"
                icon: "git"
                type: "bottom"
                on_action_button: print("on_action_button")
                left_action_items: [["menu", lambda x: x]]
'''
)


class BottomAppBarTest(MDApp):
    def callback(self, text, value):
        if value and self.root:
            if text == "Off":
                self.root.ids.toolbar.remove_notch()
            elif text == "On":
                self.root.ids.toolbar.set_notch()
            elif text == "Attached - End":
                self.root.ids.toolbar.mode = "end"
            elif text == "Attached - Center":
                self.root.ids.toolbar.mode = "center"
            elif text == "Free - End":
                self.root.ids.toolbar.mode = "free-end"
            elif text == "Free - Center":
                self.root.ids.toolbar.mode = "free-center"

    def build(self):
        return Factory.BottomAppBar()


BottomAppBarTest().run()
"""
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ListProperty,
    StringProperty,
    NumericProperty,
    OptionProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

from kivymd.uix.button import MDIconButton, MDFloatingActionButton
from kivymd.uix.behaviors import (
    SpecificBackgroundColorBehavior,
    RectangularElevationBehavior,
)
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
#:import m_res kivymd.material_resources


<MDActionBottomAppBarButton>:
    canvas.before:
        PushMatrix
        Scale:
            origin: self.center
            x: root._scale_x
            y: root._scale_y
    canvas.after:
        PopMatrix


<MDToolbar>
    size_hint_y: None
    height: root.theme_cls.standard_increment
    padding: [root.theme_cls.horizontal_margins - dp(12), 0]
    opposite_colors: True
    elevation: 6

    canvas:
        Color:
            rgba: root.theme_cls.primary_color
        RoundedRectangle:
            pos:
                self.pos \
                if root.mode == "center" else \
                (self.width - root.action_button.width + dp(6), self.y)
            size:
                (((self.width - root.action_button.width) / 2 - dp(6), self.height) \
                if root.mode == "center" else \
                (root.action_button.width - dp(6), self.height)) if root.type == "bottom" else self.pos
            radius:
                (0, root.round, 0, 0) if root.mode == "center" else (root.round, 0, 0, 0)
        Rectangle:
            pos:
                ((self.width / 2 - root.action_button.width / 2) - dp(6), self.y - root._shift) \
                if root.mode == "center" else \
                (self.width - root.action_button.width * 2 - dp(6), self.y - root._shift)
            size:
                (root.action_button.width + dp(6) * 2, self.height - root._shift * 2) \
                if root.type == "bottom" else (0, 0)
        RoundedRectangle:
            pos:
                ((self.width + root.action_button.width) / 2 + dp(6), self.y) \
                if root.mode == "center" else self.pos
            size:
                (((self.width - root.action_button.width) / 2 + dp(6), self.height) \
                if root.mode == "center" else \
                ((self.width - root.action_button.width * 2 - dp(6)), self.height)) \
                if root.type == "bottom" else (0, 0)
            radius: (root.round, 0, 0, 0) if root.mode == "center" else (0, root.round, 0, 0)
        Color:
            rgba: 1, 1, 1, 1
        Ellipse:
            pos:
                (self.center[0] - root.action_button.width / 2 - dp(6), self.center[1] - root._shift * 2) \
                if root.mode == "center" else \
                (self.width - root.action_button.width * 2 - dp(6), self.center[1] - root._shift * 2)
            size:
                (root.action_button.width + dp(6) * 2, root.action_button.width) \
                if root.type == "bottom" else (0, 0)
            angle_start: root._angle_start
            angle_end: root._angle_end

    BoxLayout:
        id: left_actions
        orientation: 'horizontal'
        size_hint_x: None
        padding: [0, (self.height - dp(48))/2]

    BoxLayout:
        padding: dp(12), 0

        MDLabel:
            id: label_title
            font_style: 'H6'
            opposite_colors: root.opposite_colors
            theme_text_color: 'Custom'
            text_color: root.specific_text_color
            text: root.title
            shorten: True
            shorten_from: 'right'
            halign: root.anchor_title

    BoxLayout:
        id: right_actions
        orientation: 'horizontal'
        size_hint_x: None
        padding: [0, (self.height - dp(48)) / 2]
"""
)


class MDActionBottomAppBarButton(MDFloatingActionButton):
    _scale_x = NumericProperty(1)
    _scale_y = NumericProperty(1)


class MDToolbar(
    ThemableBehavior,
    RectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
    BoxLayout,
):
    """
    :Events:
        `on_action_button`
            Method for the button used for the `MDBottomAppBar` class.
    """

    left_action_items = ListProperty()
    """The icons on the left of the `MDToolbar`.
    To add one, append a list like the following:
        ['icon_name', callback]
    where 'icon_name' is a string that corresponds to an icon definition and
     callback is the function called on a touch release event.
    """

    right_action_items = ListProperty()
    """The icons on the left of the `MDToolbar`.
    Works the same way as :attr:`left_action_items`
    """

    title = StringProperty()
    """The text displayed on the `MDToolbar`."""

    md_bg_color = ListProperty([0, 0, 0, 0])
    """Color for `MDToolbar`."""

    anchor_title = StringProperty("left")

    mode = OptionProperty(
        "center", options=["free-end", "free-center", "end", "center"]
    )
    """`MDBottomAppBar` button position."""

    round = NumericProperty(dp(10))
    """Rounding the corners at the notch for a button in `MDBottomAppBar`"""

    icon = StringProperty("android")
    """Icon action button."""

    icon_color = ListProperty()
    """Color action button."""

    type = OptionProperty("top", options=["top", "bottom"])
    """When using the `MDBottomAppBar` class,
    the parameter `type` must be set to `bottom`:
    
    Python:

        .. code-block:: python

            MDBottomAppBar:
                type: "bottom"
    """

    _shift = NumericProperty(dp(3.5))
    _angle_start = NumericProperty(90)
    _angle_end = NumericProperty(270)

    def __init__(self, **kwargs):
        self.action_button = MDActionBottomAppBarButton()
        super().__init__(**kwargs)
        self.register_event_type("on_action_button")
        self.action_button.bind(
            on_release=lambda x: self.dispatch("on_action_button")
        )
        self.action_button.x = Window.width / 2 - self.action_button.width / 2
        self.action_button.y = (
            (self.center[1] - self.height / 2)
            + self.theme_cls.standard_increment / 2
            + self._shift
        )
        if not self.icon_color:
            self.icon_color = self.theme_cls.primary_color
        Window.bind(on_resize=self._on_resize)
        self.bind(specific_text_color=self.update_action_bar_text_colors)
        Clock.schedule_once(
            lambda x: self.on_left_action_items(0, self.left_action_items)
        )
        Clock.schedule_once(
            lambda x: self.on_right_action_items(0, self.right_action_items)
        )

    def on_action_button(self, *args):
        pass

    def on_md_bg_color(self, instance, value):
        if type == "bottom":
            self.md_bg_color = [0, 0, 0, 0]

    def on_left_action_items(self, instance, value):
        self.update_action_bar(self.ids["left_actions"], value)

    def on_right_action_items(self, instance, value):
        self.update_action_bar(self.ids["right_actions"], value)

    def update_action_bar(self, action_bar, action_bar_items):
        action_bar.clear_widgets()
        new_width = 0
        for item in action_bar_items:
            new_width += dp(48)
            action_bar.add_widget(
                MDIconButton(
                    icon=item[0],
                    on_release=item[1],
                    opposite_colors=True,
                    text_color=self.specific_text_color,
                    theme_text_color="Custom",
                )
            )
        action_bar.width = new_width

    def update_action_bar_text_colors(self, instance, value):
        for child in self.ids["left_actions"].children:
            child.text_color = self.specific_text_color
        for child in self.ids["right_actions"].children:
            child.text_color = self.specific_text_color

    def _on_resize(self, instance, width, height):
        if self.mode == "center":
            self.action_button.x = width / 2 - self.action_button.width / 2
        else:
            self.action_button.x = width - self.action_button.width * 2

    def on_icon(self, instance, value):
        self.action_button.icon = value

    def on_icon_color(self, instance, value):
        self.action_button.md_bg_color = value

    def on_mode(self, instance, value):
        def set_button_pos(*args):
            self.action_button.x = x
            self.action_button.y = y
            self.action_button._hard_shadow_size = (0, 0)
            self.action_button._soft_shadow_size = (0, 0)
            anim = Animation(_scale_x=1, _scale_y=1, d=0.05)
            anim.bind(on_complete=self.set_shadow)
            anim.start(self.action_button)

        if value == "center":
            self.set_notch()
            x = Window.width / 2 - self.action_button.width / 2
            y = (
                (self.center[1] - self.height / 2)
                + self.theme_cls.standard_increment / 2
                + self._shift
            )
        elif value == "end":

            self.set_notch()
            x = Window.width - self.action_button.width * 2
            y = (
                (self.center[1] - self.height / 2)
                + self.theme_cls.standard_increment / 2
                + self._shift
            )
            self.right_action_items = []
        elif value == "free-end":
            self.remove_notch()
            x = Window.width - self.action_button.width - dp(10)
            y = self.action_button.height + self.action_button.height / 2
        elif value == "free-center":
            self.remove_notch()
            x = Window.width / 2 - self.action_button.width / 2
            y = self.action_button.height + self.action_button.height / 2
        self.remove_shadow()
        anim = Animation(_scale_x=0, _scale_y=0, d=0.05)
        anim.bind(on_complete=set_button_pos)
        anim.start(self.action_button)

    def remove_notch(self):
        self._angle_start = 0
        self._angle_end = 0
        self.round = 0
        self._shift = 0

    def set_notch(self):
        self._angle_start = 90
        self._angle_end = 270
        self.round = dp(10)
        self._shift = dp(3.5)

    def remove_shadow(self):
        self.action_button._hard_shadow_size = (0, 0)
        self.action_button._soft_shadow_size = (0, 0)

    def set_shadow(self, *args):
        self.action_button._hard_shadow_size = (dp(112), dp(112))
        self.action_button._soft_shadow_size = (dp(112), dp(112))


class MDBottomAppBar(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None

    def add_widget(self, widget, index=0, canvas=None):
        if widget.__class__ is MDToolbar:
            super().add_widget(widget)
            return super().add_widget(widget.action_button)
