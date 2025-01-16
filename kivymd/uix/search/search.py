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
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.behaviors import StencilBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDIcon

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


class MDSearchViewContainer(StencilBehavior, BoxLayout):
    pass


class MDSearchWidget(RelativeLayout):

    _font_style = theme_font_styles["Title"]["medium"]
    _duration = 0.4
    _transition = "in_out_circ"
    state = "closed"

    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root

    def update_pos(self, *args):
        self.ids.root_container.pos = self.root.pos

    def update_size(self, *args):
        self.ids.root_container.size = self.root.size
        self.ids.root_container.radius = dp(28)

    def _delayed_run(self, delay, func, *args):
        Clock.schedule_once(lambda dt: func(*args), delay)

    def _open(self, d, t, opacity_down, opacity_up, docked):
        self.root._view_container.size_hint_y = 1
        self.root._view_container.opacity = 0
        self.ids.root_container.add_widget(self.root._view_container, index=1)
        self._delayed_run(d / 4, opacity_up.start, self.root._view_container)
        Animation(size=self.size, pos=self.pos, radius=[0] * 4, t=t, d=d).start(
            self.ids.root_container
        )
        Animation(height=dp(70), t=t, d=d).start(self.ids.header)
        opacity_down.start(self.root._bar_trailing_container)
        opacity_down.start(self.root._bar_leading_container)
        self.root._view_leading_container.opacity = 0
        self.root._view_trailing_container.opacity = 0
        self._delayed_run(d / 2, self.update_state_opened)
        self._delayed_run(
            d / 2, opacity_up.start, self.root._view_trailing_container
        )
        self._delayed_run(
            d / 2, opacity_up.start, self.root._view_leading_container
        )

    def _close(self, d, t, opacity_down, opacity_up, docked):
        self.root._view_container.size_hint_y = None
        self.root._view_container.opacity = 1
        opacity_down.start(self.root._view_container)
        if self.root._view_container in self.ids.root_container.children:
            self._delayed_run(
                d / 2,
                self.ids.root_container.remove_widget,
                self.root._view_container,
            )
        self._delayed_run(
            d, setattr, self.root._view_container, "height", dp(55)
        )
        Animation(
            size=[self.root.width, dp(56)],
            pos=self.root.pos,
            radius=[dp(28)] * 4,
            t=t,
            d=d,
        ).start(self.ids.root_container)
        Animation(height=dp(56), t=t, d=d).start(self.ids.header)
        opacity_down.start(self.root._view_trailing_container)
        opacity_down.start(self.root._view_leading_container)
        self.root._bar_leading_container.opacity = 0
        self.root._bar_trailing_container.opacity = 0
        self._delayed_run(d / 2, self.update_state_closed)
        self._delayed_run(
            d / 2, opacity_up.start, self.root._bar_trailing_container
        )
        self._delayed_run(
            d / 2, opacity_up.start, self.root._bar_leading_container
        )

    switching_state = False

    def switch_state(self, new_state):
        if self.switching_state or new_state == self.state:
            return
        self.switching_state = True
        docked = False
        opacity_down = Animation(
            opacity=0, t=self._transition, d=self._duration / 2
        )
        opacity_up = Animation(
            opacity=1, t=self._transition, d=self._duration / 2
        )

        getattr(self, "_" + new_state)(
            self._duration, self._transition, opacity_down, opacity_up, docked
        )
        Clock.schedule_once(
            lambda dt: setattr(self, "switching_state", False), self._duration
        )

    def init_state(self):
        self.clean_header()

    def clean_header(self):
        for child in self.ids.header.children:
            if child.__class__.__name__ != "TextInput":
                self.ids.header.remove_widget(child)

    def init_state(self):
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
        self.bind(pos=self._search_widget.update_pos)
        self.bind(size=self._search_widget.update_size)

    def on_supporting_text(self, instance, text):
        self._search_widget.ids.text_input.hint_text = text

    def on_view_root(self, *args):
        if self._search_widget.parent:
            self._search_widget.parent.remove_widget(self._search_widget)
        self.view_root.add_widget(self._search_widget)
        self._search_widget.init_state()

    def add_widget(self, widget):
        if widget.__class__.__name__ in self._view_map.keys():
            setattr(self, self._view_map[widget.__class__.__name__], widget)

    def close_view(self):
        self._search_widget.switch_state("close")

    def open_view(self):
        self._search_widget.switch_state("open")
