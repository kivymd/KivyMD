import os
from functools import partial

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    StringProperty,
    OptionProperty,
    NumericProperty,
    ListProperty,
    DictProperty,
)
from kivy.factory import Factory
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stencilview import StencilView

from kivymd import uix_path
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.carousel.carousel_strategy import AvaliableStrategies

with open(
    os.path.join(uix_path, "carousel", "carousel.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDCarouselImageItem(BoxLayout):
    pass


class MDCarousel(MDBoxLayout, StencilView):
    strategy = OptionProperty(
        "MultiBrowseCarouselStrategy", options=[AvaliableStrategies.avaliable]
    )
    is_horizontal = BooleanProperty(True)
    alignment = StringProperty("default")
    desired_item_size = NumericProperty(100)

    data = ListProperty([])
    viewclass = StringProperty("MDCarouselImageItem")

    _strategy = None
    _variable_item_size = dp(50)

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.bind(data=self.update_strategy)
        self.bind(strategy=self.update_strategy)
        self.bind(size=self.update_strategy)

    def on_data(self, instance, data):
        for widget_data in data:
            widget = Factory.get(
                self.viewclass
                if "viewclass" not in widget_data.keys()
                else widget_data["viewclass"]
            )(size_hint_x=None)
            for key, value in widget_data.items():
                setattr(widget, key, value)
            widget.width = 0
            self.ids._container.add_widget(widget)

    def update_strategy(self, *args):
        if self.width <= 0:
            Clock.schedule_once(self.update_strategy)
            return
        if self._strategy.__class__.__name__ != self.strategy:
            self._strategy = AvaliableStrategies.get(self.strategy, len(self.data))
        self._strategy.arrange(self.alignment, self.width, self.desired_item_size)
        Clock.schedule_once(partial(self._strategy.set_init_size, self.ids._container))
        return self._strategy

    def on_touch_move(self, touch):
        self._strategy.touch_move(self.ids._container, touch)
        super().on_touch_move(touch)
