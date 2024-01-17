"""
Components/Swiper
=================

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/mdswiper-preview.gif
    :align: center

Usage
=====

.. code-block:: kv

    MDSwiper:

        MDSwiperItem:

        MDSwiperItem:

        MDSwiperItem:

Example
=======

.. code-block:: python

    from kivy.lang.builder import Builder

    from kivymd.app import MDApp

    kv = '''
    <MySwiper@MDSwiperItem>

        FitImage:
            source: "bg.jpg"
            radius: [dp(20),]


    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDSwiper:
            size_hint_y: None
            height: root.height - dp(40)
            y: root.height - self.height - dp(20)

            MySwiper:

            MySwiper:

            MySwiper:

            MySwiper:

            MySwiper:
    '''


    class Main(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(kv)


    Main().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/swiper-example.gif
    :align: center

.. warning::
    The width of :class:`MDSwiperItem` is adjusted automatically. Consider changing
    that by :attr:`~MDSwiperItem.width_mult`.

.. warning::
    The width of :class:`MDSwiper` is automatically adjusted according to the width of the window.

.. rubric:: :class:`~MDSwiper` provides the following events for use:

.. code-block:: python

    __events__ = (
        "on_swipe",
        "on_pre_swipe",
        "on_overswipe_right",
        "on_overswipe_left",
        "on_swipe_left",
        "on_swipe_right"
    )

.. code-block:: kv

    MDSwiper:
        on_swipe: print("on_swipe")
        on_pre_swipe: print("on_pre_swipe")
        on_overswipe_right: print("on_overswipe_right")
        on_overswipe_left: print("on_overswipe_left")
        on_swipe_left: print("on_swipe_left")
        on_swipe_right: print("on_swipe_right")
"""

__all__ = ("MDSwiperItem", "MDSwiper")

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.effects.dampedscroll import DampedScrollEffect
from kivy.lang.builder import Builder
from kivy.properties import (
    BooleanProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.utils import platform

from kivymd import uix_path
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView

with open(
    os.path.join(uix_path, "swiper", "swiper.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


# TODO: Redesign this module according to the specification -
#  https://m3.material.io/components/carousel/overview
class _ScrollViewHardStop(DampedScrollEffect):
    def stop(self, val, t=None):
        return super().stop(val, t=0.01)


class _ItemsBox(AnchorLayout):
    _root = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._update)
        Window.bind(on_resize=self._set_size)

    def _update(self, *args):
        self._set_size()

    def _set_size(self, *args):
        window_size = Window.size
        self.size = [
            window_size[0]
            - self._root.items_spacing * self._root.width_mult * 2,
            self._root.height,
        ]


class MDSwiperItem(MDBoxLayout):
    """
    Swiper item class.

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` class documentation.
    """

    _root = ObjectProperty()
    _selected = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self._set_size)
        Window.bind(on_resize=self._set_size)

    def _set_size(self, *args):
        Clock.schedule_once(lambda x: self._root._reset_size())
        if self._selected:
            self._selected_size()
        else:
            self._dismiss_size()

    def _selected_size(self):
        size = [
            Window.size[0]
            - self._root.items_spacing * self._root.width_mult * 2,
            self._root.height,
        ]
        anim = Animation(
            size=size, d=self._root.size_duration, t=self._root.size_transition
        )
        anim.start(self)

    def _dismiss_size(self):
        size = [
            Window.size[0]
            - self._root.items_spacing * (1 + self._root.width_mult) * 2,
            self._root.height - self._root.items_spacing * 2,
        ]
        anim = Animation(
            size=size, d=self._root.size_duration, t=self._root.size_transition
        )
        anim.start(self)


class MDSwiper(MDScrollView):
    """
    Swiper class.

    For more information, see in the
    :class:`~kivymd.uix.scrollview.MDScrollView` class documentation.
    """

    items_spacing = NumericProperty("20dp")
    """
    The space between each :class:`MDSwiperItem`.

    :attr:`items_spacing` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `20dp`.
    """

    transition_duration = NumericProperty(0.2)
    """
    Duration of switching between :class:`MDSwiperItem`.

    :attr:`transition_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    size_duration = NumericProperty(0.2)
    """
    Duration of changing the size of :class:`MDSwiperItem`.

    :attr:`transition_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    size_transition = StringProperty("out_quad")
    """
    The type of animation used for changing the size of :class:`MDSwiperItem`.

    :attr:`size_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `out_quad`.
    """

    swipe_transition = StringProperty("out_quad")
    """
    The type of animation used for swiping.

    :attr:`swipe_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `out_quad`.
    """

    swipe_distance = NumericProperty("70dp")
    """
    Distance to move before swiping the :class:`MDSwiperItem`.

    :attr:`swipe_distance` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `70dp`.
    """

    width_mult = NumericProperty(3)
    """
    This number is multiplied by :attr:`items_spacing` x2 and
    then subtracted from the width of window to specify the width of
    :class:`MDSwiperItem`. So by decreasing the :attr:`width_mult` the width
    of :class:`MDSwiperItem` increases and vice versa.

    :attr:`width_mult` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `3`.
    """

    swipe_on_scroll = BooleanProperty(True)
    """
    Wheter to swipe on mouse wheel scrolling or not.

    :attr:`swipe_on_scroll` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    _selected = 0
    _start_touch_x = None

    __events__ = (
        "on_swipe",
        "on_pre_swipe",
        "on_overswipe_right",
        "on_overswipe_left",
        "on_swipe_left",
        "on_swipe_right",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_swipe")
        self.register_event_type("on_pre_swipe")
        self.register_event_type("on_overswipe_right")
        self.register_event_type("on_overswipe_left")
        self.register_event_type("on_swipe_left")
        self.register_event_type("on_swipe_right")

        self.effect_cls = _ScrollViewHardStop

    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, MDSwiperItem):
            widget._root = self
            items_box = _ItemsBox(_root=self)
            items_box.add_widget(widget)
            self.ids.anchor_scroll.add_widget(items_box)
            return
        else:
            return super().add_widget(widget, index=index)

    def remove_widget(self, widget):
        if not issubclass(widget.__class__, MDSwiperItem):
            return

        for item_box in self.ids.anchor_scroll.children:
            if widget in item_box.children:
                return self.ids.anchor_scroll.remove_widget(item_box)

    def set_current(self, index):
        """Switch to given :class:`MDSwiperItem` index."""

        self._selected = index
        self.dispatch("on_pre_swipe")
        self._reset_size()
        self.dispatch("on_swipe")

    def get_current_index(self):
        """Returns the current :class:`MDSwiperItem` index."""

        return self._selected

    def get_current_item(self):
        """Returns the current :class:`MDSwiperItem` instance."""

        return list(reversed(self.ids.anchor_scroll.children))[
            self._selected
        ].children[0]

    def get_items(self):
        """Returns the list of :class:`MDSwiperItem` children.

        .. note::

            Use `get_items()` to get the list of children instead of
            `MDSwiper.children`.

        """

        children = list(reversed(self.ids.anchor_scroll.children))
        items = [item.children[0] for item in children]
        return items

    def _reset_size(self, *args):
        children = list(reversed(self.ids.anchor_scroll.children))
        if not children:
            return

        child = children[self._selected]
        total_width = self.ids.anchor_scroll.width - Window.width

        if self.get_current_index() == 0:
            view_x = child.x - self.items_spacing
        elif self.get_current_index() == len(children) - 1:
            view_x = (
                child.x
                - self.items_spacing * self.width_mult
                - self.items_spacing * 2
            )
        else:
            view_x = child.x - self.items_spacing * self.width_mult

        anim = Animation(
            scroll_x=view_x / total_width,
            d=self.transition_duration,
            t=self.swipe_transition,
        )
        anim.start(self)

        for widget in children:
            widget.children[0]._dismiss_size()
            widget.children[0]._selected = False

        child.children[0]._selected_size()
        child.children[0]._selected = True

    def on_swipe(self):
        pass

    def on_pre_swipe(self):
        pass

    def on_overswipe_right(self):
        pass

    def on_overswipe_left(self):
        pass

    def on_swipe_left(self):
        pass

    def on_swipe_right(self):
        pass

    def swipe_left(self):
        previous_index = self._selected - 1
        if previous_index == -1:
            self.set_current(0)
            self.dispatch("on_overswipe_left")
        else:
            self.set_current(previous_index)
            self.dispatch("on_swipe_left")

    def swipe_right(self):
        next_index = self._selected + 1
        last_index = len(self.ids.anchor_scroll.children) - 1
        if next_index == last_index + 1:
            self.set_current(last_index)
            self.dispatch("on_overswipe_right")
        else:
            self.set_current(next_index)
            self.dispatch("on_swipe_right")

    def on_scroll_start(self, touch, check_children=True):
        if platform in ["ios", "android"]:
            return super().on_scroll_start(touch)

        # on touch pad events
        if touch.button == "scrollright":
            self.swipe_left()
        elif touch.button == "scrollleft":
            self.swipe_right()
        return super().on_scroll_start(touch)

    def on_touch_down(self, touch):
        super().on_touch_down(touch)

        if not self.collide_point(touch.pos[0], touch.pos[1]):
            return

        if platform not in ["ios", "android"] and self.swipe_on_scroll:
            if touch.button == "scrolldown":
                self.swipe_right()
            elif touch.button == "scrollup":
                self.swipe_left()
            else:
                self._start_touch_x = touch.pos[0]
        else:
            self._start_touch_x = touch.pos[0]

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        if not self._start_touch_x:
            return

        if self._start_touch_x:
            touch_x_diff = abs(self._start_touch_x - touch.pos[0])
        else:
            return

        if touch_x_diff <= self.swipe_distance:
            if touch_x_diff == 0:
                return
            self._reset_size()
            return

        # swipe to left
        if self._start_touch_x < touch.pos[0]:
            self.swipe_left()
        # swipe to right
        else:
            self.swipe_right()

        self._start_touch_x = None
        return
