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

from kivy.app import App
from kivy.lang import Builder

from kivymd.theming import ThemeManager
from kivymd.toast import toast
from kivymd.toolbar import MDBottomAppBar

kv = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDLabel kivymd.label.MDLabel


BoxLayout:
    spacing: dp(10)
    orientation: 'vertical'

    AnchorLayout:
        anchor_y: 'center'
        anchor_x: 'center'

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)

            MDRaisedButton:
                text: 'Anchor center'
                pos_hint: {'center_x': .5}
                on_release:
                    app.md_app_bar.set_pos_action_button('center')
                    app.move_item_menu('center')

            MDRaisedButton:
                text: 'Anchor right'
                pos_hint: {'center_x': .5}
                on_release:
                    app.md_app_bar.set_pos_action_button('right')
                    app.move_item_menu('right')
'''


class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    md_app_bar = None

    def build(self):
        root = Builder.load_string(kv)
        self.md_app_bar = MDBottomAppBar(
            md_bg_color=self.theme_cls.primary_color,
            left_action_items=[
                ['menu', lambda x: x],
                ['clock', lambda x: x],
                ['dots-vertical', lambda x: x]],
            anchor='right',
            callback=self.press_button)
        root.add_widget(self.md_app_bar)
        return root

    def move_item_menu(self, anchor):
        md_app_bar = self.md_app_bar
        if md_app_bar.anchor != anchor:
            if len(md_app_bar.right_action_items):
                md_app_bar.left_action_items.append(
                    md_app_bar.right_action_items[0])
                md_app_bar.right_action_items = []
            else:
                left_action_items = md_app_bar.left_action_items
                action_items = left_action_items[0:2]
                md_app_bar.right_action_items = [left_action_items[-1]]
                md_app_bar.left_action_items = action_items

    def press_button(self, instance):
        toast('Press Button')


MyApp().run()
"""

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.core.window import Window

from kivymd.backgroundcolorbehavior import SpecificBackgroundColorBehavior
from kivymd.button import MDIconButton, MDFloatingActionButton
from kivymd.theming import ThemableBehavior
from kivymd.elevation import RectangularElevationBehavior

Builder.load_string(
    """
#:import m_res kivymd.material_resources
#:import MDFloatingActionButton kivymd.button.MDFloatingActionButton


<AppBarActionButton>
    size: 0, 0
    opacity: 0
    md_bg_color: root.action_button_color


<MDBottomAppBar>

    MDToolbar:
        id: toolbar
        left_action_items: root.left_action_items
        right_action_items: root.right_action_items
        md_bg_color: root.md_bg_color


<MDToolbar>
    size_hint_y: None
    height: root.theme_cls.standard_increment
    padding: [root.theme_cls.horizontal_margins - dp(12), 0]
    opposite_colors: True
    elevation: 6

    BoxLayout:
        id: left_actions
        orientation: 'horizontal'
        size_hint_x: None
        padding: [0, (self.height - dp(48))/2]

    BoxLayout:
        padding: dp(12), 0

        MDLabel:
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
        padding: [0, (self.height - dp(48))/2]
"""
)


class MDToolbar(
    ThemableBehavior,
    RectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
    BoxLayout,
):
    left_action_items = ListProperty()
    """The icons on the left of the MDToolbar.
    To add one, append a list like the following:
        ['icon_name', callback]
    where 'icon_name' is a string that corresponds to an icon definition and
     callback is the function called on a touch release event.
    """

    right_action_items = ListProperty()
    """The icons on the left of the MDToolbar.
    Works the same way as :attr:`left_action_items`
    """

    title = StringProperty()
    """The text displayed on the MDToolbar."""

    md_bg_color = ListProperty([0, 0, 0, 1])

    anchor_title = StringProperty("left")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(specific_text_color=self.update_action_bar_text_colors)
        Clock.schedule_once(
            lambda x: self.on_left_action_items(0, self.left_action_items)
        )
        Clock.schedule_once(
            lambda x: self.on_right_action_items(0, self.right_action_items)
        )

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


class MDBottomAppBar(FloatLayout):
    left_action_items = ListProperty()
    right_action_items = ListProperty()
    md_bg_color = ListProperty([0, 0, 0, 1])
    action_button_color = ListProperty([1, 0.7568627450980392, 0.027450980392156862, 1])
    anchor = StringProperty("right")
    callback = ObjectProperty(lambda x: None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Default action Button.
        x = (
            Window.width - dp(56) - dp(20)
            if self.anchor == "right"
            else Window.width // 2 - dp(56) // 2
            if self.anchor == "center"
            else dp(20)
        )
        self.action_button = AppBarActionButton(
            y=self.ids.toolbar.height // 2,
            x=x,
            opacity=1,
            size=(dp(56), dp(56)),
            on_release=self.callback,
            action_button_color=self.action_button_color,
        )
        self.add_widget(self.action_button)

    def set_pos_action_button(self, anchor):
        def _set_pos_action_button(*args):
            if anchor == "center":
                x = self.width // 2 - dp(56) // 2
            elif anchor == "right":
                x = self.width - dp(56) - dp(20)
            else:
                return

            self.remove_widget(self.action_button)
            self.action_button = AppBarActionButton(
                y=self.ids.toolbar.height // 2,
                x=x,
                on_release=self.callback,
                action_button_color=self.action_button_color,
            )
            self.add_widget(self.action_button)
            Animation(size=(dp(56), dp(56)), opacity=1, d=0.2).start(self.action_button)
            self.anchor = anchor

        if self.anchor != anchor:
            anim = Animation(size=(0, 0), opacity=0, d=0.2)
            anim.bind(on_complete=_set_pos_action_button)
            anim.start(self.action_button)


class AppBarActionButton(MDFloatingActionButton):
    action_button_color = ListProperty([1, 0.7568627450980392, 0.027450980392156862, 1])
