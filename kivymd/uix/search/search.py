from __future__ import annotations

__all__ = (
    "MDSearchView",
    "MDSearchBar",
    "MDSearchTrailingIcon",
    "MDSearchTrailingAvatar",
)

import os

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView

from kivymd import uix_path
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton

with open(
    os.path.join(uix_path, "search", "search.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSearchTrailingAvatar(ButtonBehavior, Image):
    pass


class MDSearchTrailingIcon(MDIconButton):
    pass

class MDSearchView(ModalView):

    _header_height = dp(70)
    def __init__(self, search_bar, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_bar = search_bar
        
    def open_view(self):
        self.ids.root_container.width = self.search_bar.width
        self.ids.root_container.pos = [
            self.search_bar.pos[0],
            self.search_bar.pos[1] - self.ids.root_container.height + self.search_bar.height
        ]
        # TODO: make it like animating from that view
        self.open()

    def close_view(self):
        self.dismiss()


class MDSearchBar(ButtonBehavior, MDBoxLayout):

    leading_icon = StringProperty("magnify")
    supporting_text = StringProperty("Hinted search text")

    # internal
    _supporting_text_padding = ListProperty([0, 0, dp(30), 0])
    _search_view = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_leading_icon_release")
        self.register_event_type("on_leading_icon_press")
        self._search_view = MDSearchView(self)

    def on_leading_icon_release(self):
        pass

    def on_leading_icon_press(self):
        pass

    def on_release(self):
        pass
