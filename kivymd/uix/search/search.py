from __future__ import annotations

__all__ = (
    "MDSearchBar",
    "MDSearchTrailingAvatar",
    "MDSearchTrailingIcon",
    "MDSearchLeadingIcon",
    "MDSearchViewContainer",
    "MDSearchBarLeadingContainer",
    "MDSearchBarTrailingContainer",
    "MDSearchViewLeadingContainer",
    "MDSearchViewTrailingContainer",
)

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
    BooleanProperty
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDIcon
from kivymd.utils import next_frame

with open(
    os.path.join(uix_path, "search", "search.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSearchTrailingAvatar(ButtonBehavior, Image):
    pass


class MDSearchLeadingIcon(ButtonBehavior, MDIcon):
    pass


class MDSearchTrailingIcon(ButtonBehavior, MDIcon):
    pass


class MDSearchBarTrailingContainer(BoxLayout):
    pass


class MDSearchBarLeadingContainer(BoxLayout):
    pass


class MDSearchViewTrailingContainer(BoxLayout):
    pass


class MDSearchViewLeadingContainer(BoxLayout):
    pass


class MDSearchViewContainer(BoxLayout):
    pass


class MDSearchWidget(RelativeLayout):

    _font_style = theme_font_styles["Title"]["medium"]
    _d = 0.4
    _t = "in_out_circ"
    state = "close"

    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root

    def update_bar(self, *args):
        if self.state == "close":
            self.ids.root_container.size = self.root.size
            self.ids.root_container.radius = dp(28)
            self.ids.root_container.pos = self.root.pos
        else:
            if self.root.docked:
                self.ids.root_container.radius = [dp(28)] * 4
                docked_size = self.root.width, dp(56) + self.root.docked_height
                self.ids.root_container.pos = [
                    self.root.pos[0], self.root.pos[1] - docked_size[1] + dp(56)
                ]
            else:
                self.ids.root_container.radius = [0] * 4
                self.ids.root_container.pos = [0,0]
                self.ids.root_container.size = self.size

    def _docked_open(self, opacity_down, opacity_up):
        docked_size = self.root.width, dp(56) + self.root.docked_height
        Animation(
            size=docked_size,
            pos=[self.root.pos[0], self.root.pos[1] - docked_size[1] + dp(56)],
            radius=[dp(28)] * 4,
            t=self._t,
            d=self._d,
        ).start(self.ids.root_container)
        self.root._view_container.size_hint_y = 1
        self.root._view_container.opacity = 0
        self.root._view_container.padding = [0, 0, 0, dp(16)]
        next_frame(
            self.ids.root_container.add_widget,
            self.root._view_container,
            index=0,
        )
        next_frame(opacity_up.start, self.root._view_container, t=self._d)
        self.icons_open(opacity_up, opacity_down, self._d / 2)

    def _docked_close(self, opacity_down, opacity_up):
        self._close(opacity_down, opacity_up)

    def _open(self, opacity_down, opacity_up):
        h_d = self._d / 2

        # container
        self.root._view_container.size_hint_y = 1
        self.root._view_container.opacity = 0
        self.root._view_container.padding = [0] * 4
        self.ids.root_container.add_widget(self.root._view_container, index=0)
        next_frame(opacity_up.start, self.root._view_container, t=h_d / 1.5)
        Animation(
            size=self.size, pos=self.pos, radius=[0] * 4, t=self._t, d=self._d
        ).start(self.ids.root_container)

        # header
        Animation(height=dp(70), t=self._t, d=self._d).start(self.ids.header)
        self.icons_open(opacity_up, opacity_down, h_d)

    def _close(self, opacity_down, opacity_up):
        h_d = self._d / 2
        # container
        self.root._view_container.size_hint_y = 1
        self.root._view_container.opacity = 1
        opacity_down.start(self.root._view_container)
        if self.root._view_container in self.ids.root_container.children:
            next_frame(
                self.ids.root_container.remove_widget,
                self.root._view_container,
                t=self._d,
            )
        next_frame(setattr, self.root._view_container, "height", dp(55), t=h_d)
        Animation(
            size=[self.root.width, dp(56)],
            pos=self.root.pos,
            radius=[dp(28)] * 4,
            t=self._t,
            d=self._d,
        ).start(self.ids.root_container)

        # header
        Animation(height=dp(56), t=self._t, d=self._d).start(self.ids.header)
        self.icons_close(opacity_up, opacity_down, h_d)

    def icons_close(self, opacity_up, opacity_down, h_d):
        opacity_down.start(self.root._view_trailing_container)
        opacity_down.start(self.root._view_leading_container)
        self.root._bar_leading_container.opacity = 0
        self.root._bar_trailing_container.opacity = 0
        next_frame(self.update_state_closed, t=h_d)
        next_frame(opacity_up.start, self.root._bar_trailing_container, t=h_d)
        next_frame(opacity_up.start, self.root._bar_leading_container, t=h_d)

    def icons_open(self, opacity_up, opacity_down, h_d):
        opacity_down.start(self.root._bar_trailing_container)
        opacity_down.start(self.root._bar_leading_container)
        self.root._view_leading_container.opacity = 0
        self.root._view_trailing_container.opacity = 0
        next_frame(self.update_state_opened, t=h_d)
        next_frame(opacity_up.start, self.root._view_trailing_container, t=h_d)
        next_frame(opacity_up.start, self.root._view_leading_container, t=h_d)

    switching_state = False

    def switch_state(self, new_state):
        if self.switching_state or new_state == self.state:
            return
        self.switching_state = True

        opacity_down = Animation(opacity=0, d=self._d / 2)
        opacity_up = Animation(opacity=1, d=self._d / 2)

        if self.root.docked:
            self.root.width = self.root.docked_width
            self.ids.root_container.width = self.root.docked_width
            getattr(self, "_docked_" + new_state)(opacity_down, opacity_up)
        else:
            getattr(self, "_" + new_state)(opacity_down, opacity_up)

        if new_state == "close":
            self.ids.text_input.focus = False

        self.state = new_state
        Clock.schedule_once(
            lambda dt: setattr(self, "switching_state", False), self._d
        )

    def init_state(self):
        self.clean_header()

    def clean_header(self):
        for child in self.ids.header.children:
            if child.__class__.__name__ != "TextInput":
                self.ids.header.remove_widget(child)

    def init_state(self):
        if self.root.docked:
            self.root.size_hint_x = None
            self.root.width = self.root.docked_width
        else:
            self.root.size_hint_x = 1
        self.ids.root_container.size = [self.root.width, dp(56)]
        self.update_state_closed()

    def update_state_opened(self, *args):
        self.clean_header()
        self.ids.header.add_widget(self.root._view_leading_container, index=2)
        self.ids.header.add_widget(self.root._view_trailing_container, index=0)

    def update_state_closed(self, *args):
        self.clean_header()
        self.ids.header.add_widget(self.root._bar_leading_container, index=2)
        self.ids.header.add_widget(self.root._bar_trailing_container, index=0)


class MDSearchBar(Widget):

    leading_icon = StringProperty("magnify")
    supporting_text = StringProperty("Hinted search text")
    view_root = ObjectProperty(None)
    docked_width = NumericProperty(dp(360))
    docked_height = NumericProperty(dp(240))
    docked = BooleanProperty(False)

    # internal props
    _search_widget = None
    _bar_leading_container = None
    _bar_trailing_container = None
    _view_leading_container = None
    _view_trailing_container = None
    _view_container = None
    _view_map = {
        "MDSearchBarLeadingContainer": "_bar_leading_container",
        "MDSearchBarTrailingContainer": "_bar_trailing_container",
        "MDSearchViewLeadingContainer": "_view_leading_container",
        "MDSearchViewTrailingContainer": "_view_trailing_container",
        "MDSearchViewContainer": "_view_container",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._search_widget = MDSearchWidget(self)
        self.bind(pos=self._search_widget.update_bar)
        self.bind(size=self._search_widget.update_bar)
        self.on_docked(self, self.docked)

    def on_docked(self, instance, docked):
        if docked:
            self.size_hint_x = None
            self.width = self.docked_width
        else:
            self.size_hint_x = 1

    def on_supporting_text(self, instance, text):
        self._search_widget.ids.text_input.hint_text = text

    def on_view_root(self, *args):
        if self._search_widget.parent:
            self._search_widget.parent.remove_widget(self._search_widget)
        self.view_root.add_widget(self._search_widget)
        self._search_widget.init_state()
        self._search_widget.update_bar()
        self.view_root.bind(size=self._search_widget.update_bar)

    def add_widget(self, widget):
        if widget.__class__.__name__ in self._view_map.keys():
            setattr(self, self._view_map[widget.__class__.__name__], widget)

    def close_view(self):
        self._search_widget.switch_state("close")

    def open_view(self):
        self._search_widget.switch_state("open")
