"""
Navigation Drawer
=================

Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Navigation drawer <https://material.io/design/components/navigation-drawer.html>`

Example
-------

from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.uix.list import OneLineAvatarListItem

KV = '''
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:import images_path kivymd.images_path


<NavigationItem>
    theme_text_color: 'Custom'
    divider: None

    IconLeftWidget:
        icon: root.icon


<ContentNavigationDrawer>

    BoxLayout:
        orientation: 'vertical'

        FloatLayout:
            size_hint_y: None
            height: "200dp"

            canvas:
                Color:
                    rgba: app.theme_cls.primary_color
                Rectangle:
                    pos: self.pos
                    size: self.size

            BoxLayout:
                id: top_box
                size_hint_y: None
                height: "200dp"
                #padding: "10dp"
                x: root.parent.x
                pos_hint: {"top": 1}

                FitImage:
                    source: f"{images_path}kivymd_alpha.png"

            MDIconButton:
                icon: "close"
                x: root.parent.x + dp(10)
                pos_hint: {"top": 1}
                on_release: root.parent.toggle_nav_drawer()

            MDLabel:
                markup: True
                text: "[b]KivyMD[/b]\\nVersion: 0.102.1"
                #pos_hint: {'center_y': .5}
                x: root.parent.x + dp(10)
                y: root.height - top_box.height + dp(10)
                size_hint_y: None
                height: self.texture_size[1]

        ScrollView:
            pos_hint: {"top": 1}

            GridLayout:
                id: box_item
                cols: 1
                size_hint_y: None
                height: self.minimum_height


Screen:

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"
                        md_bg_color: app.theme_cls.primary_color
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

'''


class ContentNavigationDrawer(BoxLayout):
    pass


class NavigationItem(OneLineAvatarListItem):
    icon = StringProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for items in {
            "home-circle-outline": "Home",
            "update": "Check for Update",
            "settings-outline": "Settings",
            "exit-to-app": "Exit",
        }.items():
            self.root.ids.content_drawer.ids.box_item.add_widget(
                NavigationItem(
                    text=items[1],
                    icon=items[0],
                )
            )


TestNavigationDrawer().run()

"""

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager

from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDToolbar

Builder.load_string(
    """
#:import Window kivy.core.window.Window


<MDNavigationDrawer>
    size_hint: None, None
    width: root.side_panel_width
    height: Window.height
    drawer_x: 0
    elevation: 10
    x: self.drawer_x - self.width
"""
)


class NavigationDrawerContentError(Exception):
    pass


class NavigationLayout(FloatLayout):
    _cache = []
    _color = None
    _rectangle = None

    def add_canvas(self, widget):
        with widget.canvas.after:
            self._color = Color(rgba=[0, 0, 0, 0])
            self._rectangle = Rectangle(pos=widget.pos, size=widget.size)
            widget.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self._rectangle.pos = self.pos
        self._rectangle.size = self.size

    def add_widget(self, widget, index=0, canvas=None):
        """Only two layouts are allowed:
        ScreenManager and MDNavigationDrawer.

        """

        if (
            widget.__class__ is MDNavigationDrawer
            or widget.__class__ is ScreenManager
            or widget.__class__ is MDToolbar
        ):
            if widget.__class__ is ScreenManager:
                self.add_canvas(widget)
            self._cache.append(widget)
            if len(self._cache) > 3:
                raise NavigationDrawerContentError(
                    "The NavigationLayoutNew should contain "
                    "only MDNavigationDrawer class and only ScreenManager class"
                )
            return super().add_widget(widget)


class MDNavigationDrawer(MDCard):
    side_panel_width = (
        (dp(320) * 80) // 100 if dp(320) >= Window.width else dp(320)
    )
    """The width of the hidden side panel. Defaults to the minimum of
    320dp or half the NavigationDrawer width."""

    anim_time = NumericProperty(0.2)
    """The time taken for the panel to slide to the open/closed state when
    released or manually animated with anim_to_state."""

    opening_transition = StringProperty("out_cubic")
    """The name of the animation transition type to use when animating to
    an open state. Defaults to 'out_cubic'."""

    closing_transition = StringProperty("out_sine")
    """The name of the animation transition type to use when animating to
    a closed state. Defaults to 'out_sine'."""

    swipe_distance = NumericProperty(10)
    """The size of the area with which the movement of navigation drawer begins."""

    state = StringProperty("close")
    """Closed or open panel."""

    _count_distance = False
    _direction = "unknown"
    __state = "close"

    def _on_touch_move(self, touch):
        if touch.dx > 0:
            if self.drawer_x < self.width:
                self._direction = "right"
                if self.drawer_x < self.width:
                    self.drawer_x += abs(touch.dx)
        else:
            if self.drawer_x > 0:
                self._direction = "left"
                self.drawer_x -= abs(touch.dx)

    def on_touch_move(self, touch):
        if self.__state == "close":
            if self.swipe_distance > touch.x or self._count_distance is True:
                self._count_distance = True
                self._on_touch_move(touch)
        else:
            self._on_touch_move(touch)
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self._direction == "right":
            self.animation_open()
        elif self._direction == "left":
            self.animation_close()
        self._direction = "unknown"
        self._count_distance = False
        return super().on_touch_up(touch)

    def animation_open(self):
        anim = Animation(
            drawer_x=self.side_panel_width,
            d=self.anim_time,
            t=self.opening_transition,
        )
        anim.bind(on_progress=self._on_progress_open)
        anim.start(self)
        self.__state = "open"
        self.state = self.__state

    def animation_close(self):
        anim = Animation(
            drawer_x=0, d=self.anim_time, t=self.closing_transition
        )
        anim.bind(on_progress=self._on_progress_close)
        anim.start(self)
        self.__state = "close"
        self.state = self.__state

    def toggle_nav_drawer(self):
        if self.__state == "open":
            self.animation_close()
        elif self.__state == "close":
            self.animation_open()

    def _on_progress_open(self, animation, widget, progress):
        self.parent._color.rgba = [0, 0, 0, progress / 2]

    def _on_progress_close(self, animation, widget, progress):
        self.parent._color.rgba = [0, 0, 0, 0.5 - progress]
