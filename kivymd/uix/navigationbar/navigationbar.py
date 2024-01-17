"""
Components/Navigation bar
=========================

.. seealso::

    `Material Design 3 spec, Navigation bar <https://m3.material.io/components/navigation-bar/overview>`_

.. rubric:: Bottom navigation bars allow movement between primary destinations in an app:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-navigation.png
    :align: center

Usage
-----

.. code-block:: kv

    <Root>

        MDNavigationBar:

            MDNavigationItem:

                MDNavigationItemIcon:

                MDNavigationItemLabel:

            [...]

Anatomy
=======

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigationbar-item-anatomy.png
    :align: center

Example
-------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import StringProperty

            from kivymd.app import MDApp
            from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
            from kivymd.uix.screen import MDScreen


            class BaseMDNavigationItem(MDNavigationItem):
                icon = StringProperty()
                text = StringProperty()


            class BaseScreen(MDScreen):
                image_size = StringProperty()


            KV = '''
            <BaseMDNavigationItem>

                MDNavigationItemIcon:
                    icon: root.icon

                MDNavigationItemLabel:
                    text: root.text


            <BaseScreen>

                FitImage:
                    source: f"https://picsum.photos/{root.image_size}/{root.image_size}"
                    size_hint: .9, .9
                    pos_hint: {"center_x": .5, "center_y": .5}
                    radius: dp(24)


            MDBoxLayout:
                orientation: "vertical"
                md_bg_color: self.theme_cls.backgroundColor

                MDScreenManager:
                    id: screen_manager

                    BaseScreen:
                        name: "Screen 1"
                        image_size: "1024"

                    BaseScreen:
                        name: "Screen 2"
                        image_size: "800"

                    BaseScreen:
                        name: "Screen 3"
                        image_size: "600"


                MDNavigationBar:
                    on_switch_tabs: app.on_switch_tabs(*args)

                    BaseMDNavigationItem
                        icon: "gmail"
                        text: "Screen 1"
                        active: True

                    BaseMDNavigationItem
                        icon: "twitter"
                        text: "Screen 2"

                    BaseMDNavigationItem
                        icon: "linkedin"
                        text: "Screen 3"
            '''


            class Example(MDApp):
                def on_switch_tabs(
                    self,
                    bar: MDNavigationBar,
                    item: MDNavigationItem,
                    item_icon: str,
                    item_text: str,
                ):
                    self.root.ids.screen_manager.current = item_text

                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.metrics import dp
            from kivy.properties import StringProperty

            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.screenmanager import MDScreenManager
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.navigationbar import (
                MDNavigationBar,
                MDNavigationItem,
                MDNavigationItemLabel,
                MDNavigationItemIcon,
            )
            from kivymd.app import MDApp


            class BaseMDNavigationItem(MDNavigationItem):
                icon = StringProperty()
                text = StringProperty()

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.add_widget(MDNavigationItemIcon(icon=self.icon))
                    self.add_widget(MDNavigationItemLabel(text=self.text))


            class BaseScreen(MDScreen):
                image_size = StringProperty()

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.add_widget(
                        FitImage(
                            source=f"https://picsum.photos/{self.image_size}/{self.image_size}",
                            size_hint=(0.9, 0.9),
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                            radius=dp(24),
                        ),
                    )


            class Example(MDApp):
                def on_switch_tabs(
                    self,
                    bar: MDNavigationBar,
                    item: MDNavigationItem,
                    item_icon: str,
                    item_text: str,
                ):
                    self.root.get_ids().screen_manager.current = item_text

                def build(self):
                    return MDBoxLayout(
                        MDScreenManager(
                            BaseScreen(
                                name="Screen 1",
                                image_size="1024",
                            ),
                            BaseScreen(
                                name="Screen 2",
                                image_size="800",
                            ),
                            BaseScreen(
                                name="Screen 3",
                                image_size="600",
                            ),
                            id="screen_manager",
                        ),
                        MDNavigationBar(
                            BaseMDNavigationItem(
                                icon="gmail",
                                text="Screen 1",
                                active=True,
                            ),
                            BaseMDNavigationItem(
                                icon="twitter",
                                text="Screen 2",
                            ),
                            BaseMDNavigationItem(
                                icon="linkedin",
                                text="Screen 3",
                            ),
                            on_switch_tabs=self.on_switch_tabs,
                        ),
                        orientation="vertical",
                        md_bg_color=self.theme_cls.backgroundColor,
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigationbar-usage.gif
    :align: center

API break
=========

1.2.0 version
-------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp


    class Example(MDApp):
        def build(self):
            return Builder.load_string(
                '''
    MDScreen:

        MDBottomNavigation:

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Mail'
                icon: 'gmail'
                badge_icon: "numeric-10"

                MDLabel:
                    text: 'Screen 1'
                    halign: 'center'

            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Twitter'
                icon: 'twitter'

                MDLabel:
                    text: 'Screen 2'
                    halign: 'center'
    '''
            )


    Example().run()

2.0.0 version
-------------

MDNavigationBar in version 2.0.0 no longer provides a screen manager for
content placement. You have to implement it yourself. This is due to the fact
that when using MDNavigationBar and MDTabs widgets at the same time, there
were conflicts between their screen managers.

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty

    from kivymd.app import MDApp
    from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
    from kivymd.uix.screen import MDScreen


    class BaseMDNavigationItem(MDNavigationItem):
        icon = StringProperty()
        text = StringProperty()


    class BaseScreen(MDScreen):
        ...


    KV = '''
    <BaseMDNavigationItem>

        MDNavigationItemIcon:
            icon: root.icon

        MDNavigationItemLabel:
            text: root.text


    <BaseScreen>

        MDLabel:
            text: root.name
            halign: "center"


    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: self.theme_cls.backgroundColor

        MDScreenManager:
            id: screen_manager

            BaseScreen:
                name: "Screen 1"

            BaseScreen:
                name: "Screen 2"


        MDNavigationBar:
            on_switch_tabs: app.on_switch_tabs(*args)

            BaseMDNavigationItem
                icon: "gmail"
                text: "Screen 1"
                active: True

            BaseMDNavigationItem
                icon: "twitter"
                text: "Screen 2"
    '''


    class Example(MDApp):
        def on_switch_tabs(
            self,
            bar: MDNavigationBar,
            item: MDNavigationItem,
            item_icon: str,
            item_text: str,
        ):
            self.root.ids.screen_manager.current = item_text

        def build(self):
            return Builder.load_string(KV)


    Example().run()
"""

from __future__ import annotations

__all__ = (
    "MDNavigationItem",
    "MDNavigationBar",
    "MDNavigationItemLabel",
    "MDNavigationItemIcon",
)

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd import uix_path
from kivymd.uix.behaviors import (
    DeclarativeBehavior,
    CommonElevationBehavior,
    RectangularRippleBehavior,
)
from kivymd.utils.set_bars_colors import set_bars_colors

with open(
    os.path.join(uix_path, "navigationbar", "navigationbar.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDNavigationItemLabel(MDLabel):
    """
    Implements a text label for the :class:`~MDNavigationItem` class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """

    text_color_active = ColorProperty(None)
    """
    Item icon color in (r, g, b, a) or string format.

    :attr:`text_color_active` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_color_normal = ColorProperty(None)
    """
    Item icon color in (r, g, b, a) or string format.

    :attr:`text_color_normal` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """


class MDNavigationItemIcon(MDIcon):
    """
    Implements a icon for the :class:`~MDNavigationItem` class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDIcon` class documentation.
    """

    icon_color_active = ColorProperty(None)
    """
    Item icon color in (r, g, b, a) or string format.

    :attr:`icon_color_active` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color_normal = ColorProperty(None)
    """
    Item icon color in (r, g, b, a) or string format.

    :attr:`icon_color_normal` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """


class MDNavigationItem(
    DeclarativeBehavior,
    RectangularRippleBehavior,
    ButtonBehavior,
    RelativeLayout,
):
    """
    Bottom item class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivy.uix.anchorlayout.AnchorLayout` and
    :class:`~kivy.uix.behaviors.ButtonBehavior`
    classes documentation.

    .. versionchanged:: 2.0.0
        Rename class from `MDBottomNavigationItem` to `MDNavigationItem`.
    """

    active = BooleanProperty(False)
    """
    Indicates if the bar item is active or inactive.

    :attr:`active` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    indicator_color = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the highlighted
    item.

    .. versionadded:: 1.0.0

    .. versionchanged:: 2.0.0
        Rename property from `selected_color_background` to `indicator_color`.

    :attr:`indicator_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    indicator_transition = StringProperty("in_out_sine")
    """
    Animation type of the active element indicator.

    :attr:`indicator_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'in_out_sine'`.
    """

    indicator_duration = NumericProperty(0.1)
    """
    Duration of animation of the active element indicator.

    :attr:`indicator_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.1`.
    """

    _selected_region_width = NumericProperty(dp(0))

    def on_active(self, instance, value) -> None:
        """Fired when the values of :attr:`active` change."""

        def on_active(*args):
            Animation(
                _selected_region_width=dp(64) if value else 0,
                t=self.indicator_transition,
                d=self.indicator_duration,
            ).start(self)

        Clock.schedule_once(on_active)

    def on_release(self) -> None:
        """Fired when clicking on a panel item."""

        self.parent.set_active_item(self)

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDNavigationItemLabel):
            self.ids.label_container.add_widget(widget)
        elif isinstance(widget, MDNavigationItemIcon):
            self.ids.icon_container.add_widget(widget)
        elif isinstance(
            widget,
            (MDNavigationItemIconContainer, MDNavigationItemLabelContainer),
        ):
            return super().add_widget(widget)


class MDNavigationBar(CommonElevationBehavior, MDBoxLayout):
    """
    A navigation bar class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~kivymd.uix.boxlayout.MDBoxLayout`
    classes documentation.

    :Events:
        :attr:`on_switch_tabs`
            Fired when switching tabs.

        .. versionadded:: 1.0.0

    .. versionchanged:: 2.0.0
        Rename class from `MDBottomNavigation` to `MDNavigationBar`.
    """

    set_bars_color = BooleanProperty(False)
    """
    If `True` the background color of the navigation bar will be set
    automatically according to the current color of the toolbar.

    .. versionadded:: 1.0.0

    :attr:`set_bars_color` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    def __init__(self, *args, **kwargs):
        self.register_event_type("on_switch_tabs")
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.set_status_bar_color)

    def set_active_item(self, item: MDNavigationItem) -> None:
        """Sets the currently active element on the panel."""

        for widget in self.children:
            if item is widget:
                widget.active = True
                self.dispatch(
                    "on_switch_tabs",
                    widget,
                    widget.ids.icon_container.children[0].icon
                    if len(widget.ids.icon_container.children)
                    else "",
                    widget.ids.label_container.children[0].text
                    if len(widget.ids.label_container.children)
                    else "",
                )
            else:
                widget.active = False

    def set_status_bar_color(self, interval: int | float) -> None:
        """Sets the color of the lower system navigation bar."""

        if self.set_bars_color:
            set_bars_colors(self.md_bg_color, None, self.theme_cls.theme_style)

    def on_switch_tabs(
        self, item: MDNavigationItem, item_icon: str, item_text: str
    ) -> None:
        """Fired when switching tabs."""


class MDNavigationItemIconContainer(BoxLayout):
    pass


class MDNavigationItemLabelContainer(BoxLayout):
    pass
