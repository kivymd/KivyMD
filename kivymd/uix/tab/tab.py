"""
Components/Tabs
===============

.. seealso::

    `Material Design spec, Tabs <https://m3.material.io/components/tabs/overview>`_

.. rubric:: Tabs organize content across different screens, data sets,
    and other interactions.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tab-preview.png
    :align: center

- Use tabs to group content into helpful categories
- Two types: primary and secondary
- Tabs can horizontally scroll, so a UI can have as many tabs as needed
- Place tabs next to each other as peers

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tab-types.png
    :align: center

1. Primary tabs
2. Secondary tabs

Usage primary tabs
------------------

Primary tabs should be used when just one set of tabs are needed.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.tab import (
        MDTabsItem,
        MDTabsItemIcon,
        MDTabsItemText,
        MDTabsBadge,
    )

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDTabsPrimary:
            id: tabs
            pos_hint: {"center_x": .5, "center_y": .5}

            MDDivider:
    '''


    class Example(MDApp):
        def on_start(self):
            for tab_icon, tab_name in {
                "airplane": "Flights",
                "treasure-chest": "Trips",
                "compass-outline": "Explore",
            }.items():
                if tab_icon == "treasure-chest":
                    self.root.ids.tabs.add_widget(
                        MDTabsItem(
                            MDTabsItemIcon(
                                MDTabsBadge(
                                    text="99",
                                ),
                                icon=tab_icon,
                            ),
                            MDTabsItemText(
                                text=tab_name,
                            ),
                        )
                    )
                else:
                    self.root.ids.tabs.add_widget(
                        MDTabsItem(
                            MDTabsItemIcon(
                                icon=tab_icon,
                            ),
                            MDTabsItemText(
                                text=tab_name,
                            ),
                        )
                    )
                self.root.ids.tabs.switch_tab(icon="airplane")

        def build(self):
            self.theme_cls.primary_palette = "Olive"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tab-primary-usage.png
    :align: center

Anatomy primary tabs
--------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tab-primary-anatomy.png
    :align: center

Usage secondary tabs
--------------------

Secondary tabs are necessary when a screen requires more than one level of
tabs. These tabs use a simpler style of indicator, but their function is
identical to primary tabs.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.tab import (
        MDTabsItemIcon,
        MDTabsItemText,
        MDTabsBadge, MDTabsItemSecondary,
    )

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDTabsSecondary:
            id: tabs
            pos_hint: {"center_x": .5, "center_y": .5}

            MDDivider:
    '''


    class Example(MDApp):
        def on_start(self):
            for tab_icon, tab_name in {
                "airplane": "Flights",
                "treasure-chest": "Trips",
                "compass-outline": "Explore",
            }.items():
                if tab_icon == "treasure-chest":
                    self.root.ids.tabs.add_widget(
                        MDTabsItemSecondary(
                            MDTabsItemIcon(
                                icon=tab_icon,
                            ),
                            MDTabsItemText(
                                text=tab_name,
                            ),
                            MDTabsBadge(
                                text="5",
                            ),
                        )
                    )
                else:
                    self.root.ids.tabs.add_widget(
                        MDTabsItemSecondary(
                            MDTabsItemIcon(
                                icon=tab_icon,
                            ),
                            MDTabsItemText(
                                text=tab_name,
                            ),
                        )
                    )
            self.root.ids.tabs.switch_tab(icon="airplane")

        def build(self):
            self.theme_cls.primary_palette = "Olive"
            return Builder.load_string(KV)


    Example().run()

Anatomy secondary tabs
----------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tab-secondary-anatomy.png
    :align: center

Related content
---------------

Use tabs to group related content, not sequential content.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel
    from kivymd.uix.tab import (
        MDTabsItemIcon,
        MDTabsItemText,
        MDTabsItem,
    )

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDTabsPrimary:
            id: tabs
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint_x: .6

            MDDivider:

            MDTabsCarousel:
                id: related_content_container
                size_hint_y: None
                height: dp(320)
    '''


    class Example(MDApp):
        def on_start(self):
            for tab_icon, tab_name in {
                "airplane": "Flights",
                "treasure-chest": "Trips",
                "compass-outline": "Explore",
            }.items():
                self.root.ids.tabs.add_widget(
                    MDTabsItem(
                        MDTabsItemIcon(
                            icon=tab_icon,
                        ),
                        MDTabsItemText(
                            text=tab_name,
                        ),
                    )
                )
                self.root.ids.related_content_container.add_widget(
                    MDLabel(
                        text=tab_name,
                        halign="center",
                    )
                )
                self.root.ids.tabs.switch_tab(icon="airplane")

        def build(self):
            self.theme_cls.primary_palette = "Olive"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tab-primary-related-content.gif
    :align: center

Behaviors
=========

Scrollable tabs
---------------

When a set of tabs cannot fit on screen, use scrollable tabs. Scrollable tabs
can use longer text labels and a larger number of tabs. They are best used for
browsing on touch interfaces.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.tab import MDTabsItemText, MDTabsItem

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDTabsPrimary:
            id: tabs
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint_x: .6
            allow_stretch: False
            label_only: True

            MDDivider:
    '''


    class Example(MDApp):
        def on_start(self):
            for tab_name in [
                "Moscow",
                "Saint Petersburg",
                "Novosibirsk",
                "Yekaterinburg",
                "Kazan",
                "Nizhny Novgorod",
                "Chelyabinsk",
            ]:
                self.root.ids.tabs.add_widget(
                    MDTabsItem(
                        MDTabsItemText(
                            text=tab_name,
                        ),
                    )
                )
            self.root.ids.tabs.switch_tab(text="Moscow")

        def build(self):
            self.theme_cls.primary_palette = "Olive"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tab-primary-scrollable-behavior.gif
    :align: center

Fixed tabs
==========

Fixed tabs display all tabs in a set simultaneously. They are best for
switching between related content quickly, such as between transportation
methods in a map. To navigate between fixed tabs, tap an individual tab, or
swipe left or right in the content area.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.tab import MDTabsItemText, MDTabsItem

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDTabsPrimary:
            id: tabs
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint_x: .6
            allow_stretch: True
            label_only: True

            MDDivider:
    '''


    class Example(MDApp):
        def on_start(self):
            for tab_name in [
                "Moscow", "Saint Petersburg", "Novosibirsk"
            ]:
                self.root.ids.tabs.add_widget(
                    MDTabsItem(
                        MDTabsItemText(
                            text=tab_name,
                        ),
                    )
                )
            self.root.ids.tabs.switch_tab(text="Moscow")

        def build(self):
            self.theme_cls.primary_palette = "Olive"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tab-primary-fixed-behavior.png
    :align: center

Tap a tab
---------

Navigate to a tab by tapping on it.


.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tab-primary-tap-a-tab-behavior.gif
    :align: center

Swipe within the content area
-----------------------------

To navigate between tabs, users can swipe left or right within the content
area.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tab-primary-swipe-within-content-area-behavior.gif
    :align: center

Switching tab
=============

You can switch tabs by icon name, by tab name, and by tab objects:

.. code-block:: python

    instance_tabs.switch_tab(icon="airplane")

.. code-block:: python

    instance_tabs.switch_tab(text="Airplane")

.. code-block:: python

    instance_tabs.switch_tab(
        instance=instance_tabs_item  # MDTabsItem
    )

API break
=========

1.2.0 version
-------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.floatlayout import MDFloatLayout
    from kivymd.uix.tab import MDTabsBase
    from kivymd.icon_definitions import md_icons

    KV = '''
    MDBoxLayout:

        MDTabs:
            id: tabs
            on_ref_press: app.on_ref_press(*args)


    <Tab>

        MDIconButton:
            id: icon
            icon: app.icons[0]
            icon_size: "48sp"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Tab(MDFloatLayout, MDTabsBase):
        '''Class implementing content for a tab.'''


    class Example(MDApp):
        icons = list(md_icons.keys())[15:30]

        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for name_tab in self.icons:
                self.root.ids.tabs.add_widget(
                    Tab(title=name_tab, icon=name_tab)
                )


    Example().run()

2.0.0 version
-------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.icon_definitions import md_icons
    from kivymd.uix.label import MDIcon
    from kivymd.uix.tab import MDTabsItem, MDTabsItemIcon
    from kivymd.uix.tab.tab import MDTabsItemText

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDTabsPrimary:
            id: tabs
            allow_stretch: False
            pos_hint: {"center_x": .5, "center_y": .5}

            MDDivider:

            MDTabsCarousel:
                id: related_content
                size_hint_y: None
                height: root.height - tabs.ids.tab_scroll.height
    '''


    class Example(MDApp):
        def on_start(self):
            for name_tab in list(md_icons.keys())[15:30]:
                self.root.ids.tabs.add_widget(
                    MDTabsItem(
                        MDTabsItemIcon(
                            icon=name_tab,
                        ),
                        MDTabsItemText(
                            text=name_tab,
                        ),
                    )
                )
                self.root.ids.related_content.add_widget(
                    MDIcon(
                        icon=name_tab,
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                    )
                )
                self.root.ids.tabs.switch_tab(icon="airplane")

        def build(self):
            return Builder.load_string(KV)


    Example().run()
"""

from __future__ import annotations

__all__ = (
    "MDTabsPrimary",
    "MDTabsSecondary",
    "MDTabsItem",
    "MDTabsItemSecondary",
    "MDTabsItemIcon",
    "MDTabsItemText",
    "MDTabsCarousel",
    "MDTabsBadge",
)

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.utils import boundary

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.badge import MDBadge
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    DeclarativeBehavior,
    RectangularRippleBehavior,
)
from kivymd.uix.behaviors.state_layer_behavior import StateLayerBehavior
from kivymd.uix.label import MDIcon, MDLabel

with open(os.path.join(uix_path, "tab", "tab.kv"), encoding="utf-8") as kv_file:
    Builder.load_string(kv_file.read())


###############################################################################
#
#                               COMMON CLASSES
#
###############################################################################


class MDTabsBadge(MDBadge):
    """
    Implements an badge for secondary tabs.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.badge.badge.MDBadge` class documentation.
    """


class MDTabsCarousel(Carousel):
    """
    Implements a carousel for user-generated content.

    For more information, see in the
    :class:`~kivy.uix.carousel.Carousel` class documentation.
    """

    lock_swiping = BooleanProperty(False)
    """
    If True - disable switching tabs by swipe.

    :attr:`lock_swiping` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _tabs = ObjectProperty()  # MDTabsPrimary/MDTabsSecondary object

    def on_touch_move(self, touch) -> str | bool | None:
        if self.lock_swiping:  # lock a swiping
            return
        if not self.touch_mode_change:
            if self.ignore_perpendicular_swipes and self.direction in (
                "top",
                "bottom",
            ):
                if abs(touch.oy - touch.y) < self.scroll_distance:
                    if abs(touch.ox - touch.x) > self.scroll_distance:
                        self._change_touch_mode()
                        self.touch_mode_change = True
            elif self.ignore_perpendicular_swipes and self.direction in (
                "right",
                "left",
            ):
                if abs(touch.ox - touch.x) < self.scroll_distance:
                    if abs(touch.oy - touch.y) > self.scroll_distance:
                        self._change_touch_mode()
                        self.touch_mode_change = True

        if self._get_uid("cavoid") in touch.ud:
            return
        if self._touch is not touch:
            super().on_touch_move(touch)
            return self._get_uid() in touch.ud
        if touch.grab_current is not self:
            return True

        ud = touch.ud[self._get_uid()]
        direction = self.direction[0]

        if ud["mode"] == "unknown":
            if direction in "rl":
                distance = abs(touch.ox - touch.x)
            else:
                distance = abs(touch.oy - touch.y)
            if distance > self.scroll_distance:
                ev = self._change_touch_mode_ev
                if ev is not None:
                    ev.cancel()
                ud["mode"] = "scroll"
        else:
            if direction in "rl":
                self._offset += touch.dx
            if direction in "tb":
                self._offset += touch.dy
        return True

    def add_widget(self, widget, *args, **kwargs):
        super().add_widget(widget, *args, **kwargs)
        if hasattr(self, "_tabs") and self._tabs:
            index = len(self.slides) - 1
            tabs_items = self._tabs.ids.container.children[::-1]
            if index < len(tabs_items):
                tab_item = tabs_items[index]
                tab_item._tab_content = widget
                widget.tab_item = tab_item


class MDTabsScrollView(BackgroundColorBehavior, ScrollView):
    """
    Implements a scrollable list of tabs.
    This class hacked version to fix scroll_x manual setting.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.scrollview.ScrollView`
    classes documentation.
    """

    def goto(self, scroll_x: float | None, scroll_y: float | None) -> None:
        """Update event value along with scroll_*."""

        def _update(e, x):
            if e:
                e.value = (e.max + e.min) * x

        if not (scroll_x is None):
            self.scroll_x = scroll_x
            _update(self.effect_x, scroll_x)

        if not (scroll_y is None):
            self.scroll_y = scroll_y
            _update(self.effect_y, scroll_y)


class MDTabsItemText(MDLabel):
    """
    Implements an label for the :class:`~MDTabsItem` class.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.

    .. versionadded:: 2.0.0
    """

    _active = BooleanProperty(False)


class MDTabsItemIcon(MDIcon):
    """
    Implements an icon for the :class:`~MDTabsItem` class.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDIcon` class documentation.

    .. versionadded:: 2.0.0
    """


class MDTabsItemBase(
    DeclarativeBehavior,
    BackgroundColorBehavior,
    RectangularRippleBehavior,
    ButtonBehavior,
    ThemableBehavior,
    StateLayerBehavior,
):
    """
    Implements a base item with an icon and text.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivymd.uix.behaviors.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.theming.ThemableBehavior`
    classes documentation.
    """

    active = BooleanProperty(False)
    """
    Is the tab active.

    :attr:`active` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _tabs = ObjectProperty()  # MDTabsPrimary/MDTabsSecondary object
    _tab_content = ObjectProperty()  # Carousel slide (related content) object

    def on_release(self, *args) -> None:
        """
        Fired when the button is released
        (i.e. the touch/click that pressed the button goes away).
        """

        if self._tab_content:
            self._tabs._tabs_carousel.load_slide(self._tab_content)

        self._tabs.update_indicator(instance=self)
        self._tabs.dispatch("on_tab_switch", self, self._tab_content)
        self._tabs._current_tab = self
        self._tabs._current_related_content = self._tab_content


class MDTabsItem(MDTabsItemBase, BoxLayout):
    """
    Implements a item with an icon and text for :class:`~MDTabsPrimary` class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~MDTabsItemBase` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.
    """

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, (MDTabsItemText, MDTabsItemIcon)):
            if len(self.children) <= 1:
                Clock.schedule_once(lambda x: self._set_width(widget))

    def _set_width(self, widget):
        def set_width(*args):
            self.width = widget.texture_size[0] + widget.padding[0] + 2

        if not self._tabs.allow_stretch and isinstance(widget, MDTabsItemText):
            Clock.schedule_once(set_width)

        super().add_widget(widget)


###############################################################################
#
#                               PRIMARY CLASSES
#
###############################################################################


class MDTabsPrimary(DeclarativeBehavior, ThemableBehavior, BoxLayout):
    """
    Tabs primary class.

    .. versionchanged:: 2.0.0

        Rename from `MDTabs` to `MDTabsPrimary` class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.

    :Events:
        `on_tab_switch`
            Fired when switching tabs.
    """

    md_bg_color = ColorProperty(None)
    """
    The background color of the widget.

    :attr:`md_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    label_only = BooleanProperty(False)
    """
    Tabs with a label only or with an icon and a label.

    .. versionadded:: 2.0.0

    :attr:`label_only` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    allow_stretch = BooleanProperty(True)
    """
    Whether to stretch tabs to the width of the panel.

    :attr:`allow_stretch` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    lock_swiping = BooleanProperty(False)
    """
    If True - disable switching tabs by swipe.

    :attr:`lock_swiping` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    anim_duration = NumericProperty(0.2)
    """
    Duration of the slide animation.

    :attr:`anim_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    indicator_anim = BooleanProperty(True)
    """
    Tab indicator animation. If you want use animation set it to ``True``.

    .. versionchanged:: 2.0.0

        Rename from `tab_indicator_anim` to `indicator_anim` attribute.

    :attr:`indicator_anim` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    indicator_radius = VariableListProperty([dp(2), dp(2), 0, 0], lenght=4)
    """
    Radius of the tab indicator.

    .. versionadded:: 2.0.0

    :attr:`indicator_radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(2), dp(2), 0, 0]`.
    """

    indicator_height = NumericProperty("4dp")
    """
    Height of the tab indicator.

    .. versionchanged:: 2.0.0

        Rename from `tab_indicator_height` to `indicator_height` attribute.

    :attr:`indicator_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'4dp'`.
    """

    indicator_duration = NumericProperty(0.5)
    """
    The duration of the animation of the indicator movement when switching
    tabs.

    .. versionadded:: 2.0.0

    :attr:`indicator_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.5`.
    """

    indicator_transition = StringProperty("out_expo")
    """
    The transition name of animation of the indicator movement when switching
    tabs.

    .. versionadded:: 2.0.0

    :attr:`indicator_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'out_expo'.
    """

    def get_last_scroll_x(self):
        return self.ids.tab_scroll.scroll_x

    last_scroll_x = AliasProperty(
        get_last_scroll_x, bind=("target",), cache=True
    )
    """
    Is the carousel reference of the next tab/slide.
    When you go from `'Tab A'` to `'Tab B'`, `'Tab B'` will be the
    target tab/slide of the carousel.

    :attr:`last_scroll_x` is an :class:`~kivy.properties.AliasProperty`.
    """

    target = ObjectProperty(None, allownone=True)
    """
    It is the carousel reference of the next tab / slide.
    When you go from `'Tab A'` to `'Tab B'`, `'Tab B'` will be the
    target tab / slide of the carousel.

    :attr:`target` is an :class:`~kivy.properties.ObjectProperty`
    and default to `None`.
    """

    def get_rect_instruction(self):
        canvas_instructions = self.ids.container.canvas.before.get_group(
            "md-tabs-rounded-rectangle"
        )
        return canvas_instructions[0]

    indicator = AliasProperty(get_rect_instruction, cache=True)
    """
    It is the :class:`~kivy.graphics.vertex_instructions.SmoothRoundedRectangle`
    instruction reference of the tab indicator.

    :attr:`indicator` is an :class:`~kivy.properties.AliasProperty`.
    """

    _tabs_carousel = ObjectProperty()  # MDTabsCarousel object
    _current_tab = None  # MDTabsItem object
    _current_related_content = None  # Carousel slide (related content) object
    _do_releasing = True

    __events__ = ("on_tab_switch", "on_slide_progress")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self._check_panel_height)

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDTabsCarousel):
            self._tabs_carousel = widget
            widget._tabs = self
            widget.bind(
                _offset=self.android_animation, index=self.on_carousel_index
            )
            return super().add_widget(widget)
        elif isinstance(widget, MDTabsItem) or (
            isinstance(self, MDTabsSecondary)
            and isinstance(widget, MDTabsItemSecondary)
        ):
            widget._tabs = self
            widget.bind(on_release=self.set_active_item)
            self.ids.container.add_widget(widget)
            Clock.schedule_once(lambda x: self.recalculate_tab_widths(), 0)
        else:
            return super().add_widget(widget)

    def do_autoscroll_tabs(self, instance: MDTabsItem, value: float) -> None:
        """
        Automatically scrolls the list of tabs when swiping the carousel
        slide (related content).

        .. versionchanged:: 2.0.0

            Rename from `tab_bar_autoscroll` to `do_autoscroll_tabs` method.
        """

        bound_left = self.center_x - self.x
        bound_right = self.ids.container.width - bound_left
        dt = instance.center_x - bound_left
        sx, sy = self.ids.tab_scroll.convert_distance_to_scroll(dt, 0)
        lsx = self.last_scroll_x  # ast scroll x of the tab bar
        scroll_is_late = lsx < sx  # determine scroll direction
        dst = abs(lsx - sx) * value  # distance to run)

        if not dst:
            return
        if scroll_is_late and instance.center_x > bound_left:
            x = lsx + dst
        elif not scroll_is_late and instance.center_x < bound_right:
            x = lsx - dst
        else:
            return

        x = boundary(x, 0.0, 1.0)
        self.ids.tab_scroll.goto(x, None)

    def android_animation(
        self, instance: MDTabsCarousel, offset: float
    ) -> None:
        """Fired when swiping a carousel slide (related content)."""

        self.dispatch("on_slide_progress", instance, offset)

        # Try to reproduce the android animation effect.
        if offset != 0 and abs(offset) < instance.width:
            forward = offset < 0
            offset = abs(offset)
            step = offset / float(instance.width)

            skip_slide = (
                instance.slides[instance._skip_slide]
                if instance._skip_slide is not None
                else None
            )
            next_slide = (
                instance.next_slide if forward else instance.previous_slide
            )
            self.target = skip_slide if skip_slide else next_slide

            if not self.target:
                return

            a = instance.current_slide.tab_item
            b = self.target.tab_item
            self.do_autoscroll_tabs(b, step)
            item_text_object = self._get_tab_item_text_icon_object()

            if item_text_object:
                if self.__class__.__name__ == "MDTabsSecondary":
                    tab_text_width = a.width
                else:
                    tab_text_width = item_text_object.texture_size[0]

                if self.indicator_anim is False:
                    return

                gap_x = abs(a.x - b.x)
                if forward:
                    x_step = (
                        a.x
                        + (a.width / 2 - tab_text_width / 2)
                        + dp(4)
                        + (gap_x * step)
                    )
                else:
                    x_step = (
                        a.x
                        + (a.width / 2 - tab_text_width / 2)
                        + dp(4)
                        - gap_x * step
                    )

                w_step = tab_text_width - (
                    dp(8) if self.__class__.__name__ == "MDTabsPrimary" else 0
                )
                self.update_indicator(x_step, w_step)

    def update_indicator(
        self, x: float = 0.0, w: float = 0.0, instance: MDTabsItem = None
    ) -> None:
        """Update position and size of the indicator."""

        def update_indicator(*args):
            indicator_pos = (0, 0)
            indicator_size = (0, 0)

            if self.__class__.__name__ == "MDTabsPrimary":
                item_text_object = self._get_tab_item_text_icon_object()

                if item_text_object:
                    tab_text_width = item_text_object.texture_size[0]
                    indicator_pos = (
                        instance.x
                        + (instance.width / 2 - tab_text_width / 2)
                        + dp(4),
                        (
                            self.indicator.pos[1]
                            if not self._tabs_carousel
                            else self._tabs_carousel.height
                        ),
                    )
                    indicator_size = (
                        tab_text_width - dp(8),
                        self.indicator_height,
                    )
            elif self.__class__.__name__ == "MDTabsSecondary":
                indicator_pos = (instance.x, self.indicator.pos[1])
                indicator_size = (instance.width, self.indicator_height)

            Animation(
                pos=indicator_pos,
                size=indicator_size,
                d=0 if not self.indicator_anim else self.indicator_duration,
                t=self.indicator_transition,
            ).start(self.indicator)

        if not instance:
            self.indicator.pos = (x, self.indicator.pos[1])
            self.indicator.size = (w, self.indicator_height)
        else:
            Clock.schedule_once(update_indicator)

    def switch_tab(
        self, instance: MDTabsItem = None, text: str = "", icon: str = ""
    ) -> None:
        """Switches tabs by tab object/tab text/tab icon name."""

        Clock.schedule_once(
            lambda x: self._switch_tab(instance, text, icon), 0.8
        )

    def set_active_item(self, item: MDTabsItem) -> None:
        """Sets the active tab item."""

        for widget in self.ids.container.children:
            if item is widget:
                # Trying to switch an already active tab.
                if widget.active and item.active:
                    break

                widget.active = not widget.active

                for widget_item in item.children:
                    if isinstance(widget_item, MDTabsItemText):
                        widget_item._active = widget.active
                        Animation(
                            text_color=(
                                self.theme_cls.primaryColor
                                if widget.active
                                else self.theme_cls.onSurfaceVariantColor
                            ),
                            d=0.2,
                        ).start(widget_item)
                    if isinstance(widget_item, MDTabsItemIcon):
                        widget_item._active = widget.active
                        Animation(
                            icon_color=(
                                self.theme_cls.primaryColor
                                if widget.active
                                else self.theme_cls.onSurfaceVariantColor
                            ),
                            d=0.2,
                        ).start(widget_item)
            else:
                widget.active = False
                for widget_item in widget.children:
                    widget_item._active = widget.active
                    if isinstance(widget_item, MDTabsItemText):
                        Animation(
                            text_color=self.theme_cls.onSurfaceVariantColor,
                            d=0.2,
                        ).start(widget_item)
                    if isinstance(widget_item, MDTabsItemIcon):
                        Animation(
                            icon_color=self.theme_cls.onSurfaceVariantColor,
                            d=0.2,
                        ).start(widget_item)

    def get_tabs_list(self) -> list:
        """
        Returns a list of :class:`~MDTabsItem` objects.

        .. versionchanged:: 2.0.0

            Rename from `get_tab_list` to `get_tabs_list` method.
        """

        return self.ids.container.children

    def get_slides_list(self) -> list:
        """
        Returns a list of user tab objects.

        .. versionchanged:: 2.0.0

            Rename from `get_slides` to `get_slides_list` method.
        """

        if self._tabs_carousel:
            return self._tabs_carousel.slides

    def get_current_tab(self) -> MDTabsItem:
        """
        Returns current tab object.

        .. versionadded:: 1.0.0
        """

        return self._current_tab

    def get_current_related_content(self) -> Widget:
        """
        Returns the carousel slide object (related content).

        .. versionadded:: 2.0.0
        """

        return self._current_related_content

    def on_tab_switch(self, *args) -> None:
        """This event is launched every time the current tab is changed."""

    def on_slide_progress(self, *args) -> None:
        """
        This event is deployed every available frame while the tab is
        scrolling.
        """

    def on_carousel_index(self, instance: MDTabsCarousel, value: int) -> None:
        """
        Fired when the Tab index have changed.
        This event is deployed by the builtin carousel of the class.
        """

        # When the index of the carousel change, update tab indicator,
        # select the current tab and reset threshold data.
        if instance.current_slide and hasattr(
            instance.current_slide, "tab_item"
        ):
            Clock.schedule_once(
                lambda x: instance.current_slide.tab_item.dispatch("on_release")
            )

    def on_size(self, instance, size) -> None:
        """Fired when the application screen size changes."""

        width, height = size
        number_tabs = len(self.ids.container.children)

        if self.allow_stretch:
            for tab in self.ids.container.children:
                tab.width = width / number_tabs

        if self._tabs_carousel:
            Clock.schedule_once(
                lambda x: self._tabs_carousel.current_slide.tab_item.dispatch(
                    "on_release"
                )
            )

    def recalculate_tab_widths(self) -> None:
        """
        Recalculates and updates the width of each tab in the tab bar.

        This method ensures that all tabs are evenly distributed across the
        available horizontal space when `allow_stretch` is enabled. It is
        automatically called after a new tab is added.

        If no tabs are present, the method exits without making changes.
        """

        number_tabs = len(self.ids.container.children)
        if number_tabs == 0:
            return

        width = self.width
        if self.allow_stretch:
            for tab in self.ids.container.children:
                tab.width = width / number_tabs

    def _switch_tab(
        self, instance: MDTabsItem = None, text: str = "", icon: str = ""
    ):
        def get_match(widget_to_compare, widget_to_compare_with, value, attr):
            if isinstance(widget_to_compare, widget_to_compare_with):
                if getattr(widget_to_compare, attr) == value:
                    return True

        def switch_by(by_attr, attr):
            for tab_item in self.ids.container.children:
                for child in tab_item.children:
                    if isinstance(child, MDTabsItemSecondaryContainer):
                        for w in child.children:
                            if get_match(
                                w,
                                (
                                    MDTabsItemText
                                    if by_attr == "text"
                                    else MDTabsItemIcon
                                ),
                                attr,
                                by_attr,
                            ):
                                tab_item.dispatch("on_release")
                                break
                    else:
                        if get_match(
                            child,
                            (
                                MDTabsItemText
                                if by_attr == "text"
                                else MDTabsItemIcon
                            ),
                            attr,
                            by_attr,
                        ):
                            tab_item.dispatch("on_release")
                            break

        if instance and isinstance(instance, MDTabsItem):
            instance.dispatch("on_release")
        elif text:
            switch_by("text", text)
        elif icon:
            switch_by("icon", icon)

    def _get_tab_item_text_icon_object(
        self, get_type="text"
    ) -> MDTabsItemText | MDTabsItemIcon | None:
        item_text_object = None

        for tab_item in self.ids.container.children:
            if tab_item.active:
                for child in tab_item.children:
                    if isinstance(child, MDTabsItemSecondaryContainer):
                        for w in child.children:
                            if isinstance(
                                w,
                                (
                                    MDTabsItemText
                                    if get_type == "text"
                                    else MDTabsItemIcon
                                ),
                            ):
                                item_text_object = w
                                break
                    else:
                        if isinstance(
                            child,
                            (
                                MDTabsItemText
                                if get_type == "text"
                                else MDTabsItemIcon
                            ),
                        ):
                            item_text_object = child
                            break
        return item_text_object

    def _check_panel_height(self, *args):
        if self.label_only:
            self.ids.tab_scroll.height = dp(48)
        else:
            self.ids.tab_scroll.height = dp(64)


###############################################################################
#
#                              SECONDARY CLASSES
#
###############################################################################


class MDTabsItemSecondaryContainer(BoxLayout):
    """
    Implements a container for placing widgets for the
    :class:`~MDTabsItemSecondary` class.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """


class MDTabsItemSecondary(MDTabsItemBase, AnchorLayout):
    """
    Implements a item with an icon and text for :class:`~MDTabsSecondary`
    class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~MDTabsItemBase` and
    :class:`~kivy.uix.anchorlayout.AnchorLayout`
    classes documentation.
    """

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, (MDTabsItemText, MDTabsItemIcon, MDTabsBadge)):
            Clock.schedule_once(
                lambda x: self.ids.box_container.add_widget(widget)
            )
        else:
            return super().add_widget(widget)


class MDTabsSecondary(MDTabsPrimary):
    """
    Tabs secondary class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~MDTabsPrimary` class documentation.
    """

    indicator_radius = VariableListProperty(0, lenght=4)
    """
    Radius of the tab indicator.

    :attr:`indicator_radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    indicator_height = NumericProperty("2dp")
    """
    Height of the tab indicator.

    :attr:`indicator_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'2dp'`.
    """

    def _check_panel_height(self, *args):
        self.ids.tab_scroll.height = dp(48)
