"""
Components/BottomNavigation
===========================

.. seealso::

    `Material Design 2 spec, Bottom navigation <https://material.io/components/bottom-navigation>`_ and
    `Material Design 3 spec, Bottom navigation <https://m3.material.io/components/navigation-bar/overview>`_

.. rubric:: Bottom navigation bars allow movement between primary destinations in an app:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-navigation.png
    :align: center

Usage
-----

.. code-block:: kv

    <Root>

        MDBottomNavigation:

            MDBottomNavigationItem:
                name: "screen 1"

                YourContent:

            MDBottomNavigationItem:
                name: "screen 2"

                YourContent:

            MDBottomNavigationItem:
                name: "screen 3"

                YourContent:

For ease of understanding, this code works like this:

.. code-block:: kv

    <Root>

        ScreenManager:

            Screen:
                name: "screen 1"

                YourContent:

            Screen:
                name: "screen 2"

                YourContent:

            Screen:
                name: "screen 3"

                YourContent:

Example
-------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp


            class Test(MDApp):

                def build(self):
                    self.theme_cls.material_style = "M3"
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(
                        '''
            MDScreen:

                MDBottomNavigation:
                    #panel_color: "#eeeaea"
                    selected_color_background: "orange"
                    text_color_active: "lightgrey"

                    MDBottomNavigationItem:
                        name: 'screen 1'
                        text: 'Mail'
                        icon: 'gmail'
                        badge_icon: "numeric-10"

                        MDLabel:
                            text: 'Mail'
                            halign: 'center'

                    MDBottomNavigationItem:
                        name: 'screen 2'
                        text: 'Twitter'
                        icon: 'twitter'
                        badge_icon: "numeric-5"

                        MDLabel:
                            text: 'Twitter'
                            halign: 'center'

                    MDBottomNavigationItem:
                        name: 'screen 3'
                        text: 'LinkedIN'
                        icon: 'linkedin'

                        MDLabel:
                            text: 'LinkedIN'
                            halign: 'center'
            '''
                    )


            Test().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen


            class Test(MDApp):
                def build(self):
                    self.theme_cls.material_style = "M3"
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDBottomNavigation(
                                MDBottomNavigationItem(
                                    MDLabel(
                                        text='Mail',
                                        halign='center',
                                    ),
                                    name='screen 1',
                                    text='Mail',
                                    icon='gmail',
                                    badge_icon="numeric-10",
                                ),
                                MDBottomNavigationItem(
                                    MDLabel(
                                        text='Twitter',
                                        halign='center',
                                    ),
                                    name='screen 1',
                                    text='Twitter',
                                    icon='twitter',
                                    badge_icon="numeric-10",
                                ),
                                MDBottomNavigationItem(
                                    MDLabel(
                                        text='LinkedIN',
                                        halign='center',
                                    ),
                                    name='screen 1',
                                    text='LinkedIN',
                                    icon='linkedin',
                                    badge_icon="numeric-10",
                                ),
                                selected_color_background="orange",
                                text_color_active="lightgrey",
                            )
                        )
                    )


            Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-navigation.gif
    :align: center

.. rubric:: :class:`~MDBottomNavigationItem` provides the following events for use:

.. code-block:: python

    __events__ = (
        "on_tab_touch_down",
        "on_tab_touch_move",
        "on_tab_touch_up",
        "on_tab_press",
        "on_tab_release",
    )

.. code-block:: kv

    Root:

        MDBottomNavigation:

            MDBottomNavigationItem:
                on_tab_touch_down: print("on_tab_touch_down")
                on_tab_touch_move: print("on_tab_touch_move")
                on_tab_touch_up: print("on_tab_touch_up")
                on_tab_press: print("on_tab_press")
                on_tab_release: print("on_tab_release")

                YourContent:

How to automatically switch a tab?
----------------------------------

Use method :attr:`~MDBottomNavigation.switch_tab` which takes as argument
the name of the tab you want to switch to.

Use custom icon
---------------

.. code-block:: kv

    MDBottomNavigation:

        MDBottomNavigationItem:
            icon: "icon.png"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-navigation-custom-icon.png
    :align: center
"""

__all__ = (
    "TabbedPanelBase",
    "MDBottomNavigationItem",
    "MDBottomNavigation",
    "MDTab",
)

import os
from typing import Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.window.window_sdl2 import WindowSDL
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import FadeTransition, ScreenManagerException

from kivymd import uix_path
from kivymd.material_resources import STANDARD_INCREMENT
from kivymd.theming import ThemableBehavior, ThemeManager
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.behaviors import CommonElevationBehavior, DeclarativeBehavior
from kivymd.uix.behaviors.backgroundcolor_behavior import (
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.utils.set_bars_colors import set_bars_colors

with open(
    os.path.join(uix_path, "bottomnavigation", "bottomnavigation.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDBottomNavigationHeader(ButtonBehavior, MDAnchorLayout):
    """
    Bottom navigation header class.

    For more information, see in the
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.anchorlayout.MDAnchorLayout`
    classes documentation.
    """

    panel_color = ColorProperty([1, 1, 1, 0])
    """
    Panel color of bottom navigation in (r, g, b, a) or string format.

    :attr:`panel_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 0]`.
    """

    tab = ObjectProperty()
    """
    :attr:`tab` is an :class:`~MDBottomNavigationItem`
    and defaults to `None`.
    """

    panel = ObjectProperty()
    """
    :attr:`panel` is an :class:`~MDBottomNavigation`
    and defaults to `None`.
    """

    active = BooleanProperty(False)

    text = StringProperty()
    """
    :attr:`text` is an :class:`~MDTab.text`
    and defaults to `''`.
    """

    text_color_normal = ColorProperty([1, 1, 1, 1])
    """
    Text color in (r, g, b, a) or string format of the label when it is not
    selected.

    :attr:`text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 1]`.
    """

    text_color_active = ColorProperty([1, 1, 1, 1])
    """
    Text color in (r, g, b, a) or string format of the label when it is selected.

    :attr:`text_color_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 1]`.
    """

    selected_color_background = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the highlighted
    item when using Material Design v3.

    .. versionadded:: 1.0.0

    :attr:`selected_color_background` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    opposite_colors = BooleanProperty(True)

    _label = ObjectProperty()
    _label_font_size = NumericProperty("12sp")
    _text_color_normal = ColorProperty([1, 1, 1, 1])
    _text_color_active = ColorProperty([1, 1, 1, 1])
    _selected_region_width = NumericProperty(dp(64))

    def __init__(self, panel, tab):
        self.panel = panel
        self.tab = tab
        super().__init__()
        self._text_color_normal = (
            self.theme_cls.disabled_hint_text_color
            if self.text_color_normal == [1, 1, 1, 1]
            else self.text_color_normal
        )
        self._label = self.ids._label
        self._label_font_size = sp(12)
        self.theme_cls.bind(disabled_hint_text_color=self._update_theme_style)
        self.active = False

    def on_press(self) -> None:
        """Called when clicking on a panel item."""

        if self.theme_cls.material_style == "M2":
            Animation(_label_font_size=sp(14), d=0.1).start(self)
        elif self.theme_cls.material_style == "M3":
            Animation(
                _selected_region_width=dp(64),
                t="in_out_sine",
                d=0,
            ).start(self)
        Animation(
            _text_color_normal=self.theme_cls.primary_color
            if self.text_color_active == [1, 1, 1, 1]
            else self.text_color_active,
            d=0.1,
        ).start(self)

    def _update_theme_style(
        self, instance_theme_manager: ThemeManager, color: list
    ):
        """Called when the application theme style changes (White/Black)."""

        if not self.active:
            self._text_color_normal = (
                color
                if self.text_color_normal == [1, 1, 1, 1]
                else self.text_color_normal
            )


class MDTab(MDScreen):
    """
    A tab is simply a screen with meta information that defines the content
    that goes in the tab header.

    For more information, see in the
    :class:`~kivymd.uix.screen.MDScreen` class documentation.
    """

    __events__ = (
        "on_tab_touch_down",
        "on_tab_touch_move",
        "on_tab_touch_up",
        "on_tab_press",
        "on_tab_release",
    )
    """Events provided."""

    text = StringProperty()
    """
    Tab header text.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon = StringProperty("checkbox-blank-circle")
    """
    Tab header icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle'`.
    """

    badge_icon = StringProperty()
    """
    Tab header badge icon.

    .. versionadded:: 1.0.0

    :attr:`badge_icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.index = 0
        self.parent_widget = None
        self.register_event_type("on_tab_touch_down")
        self.register_event_type("on_tab_touch_move")
        self.register_event_type("on_tab_touch_up")
        self.register_event_type("on_tab_press")
        self.register_event_type("on_tab_release")

    def on_tab_touch_down(self, *args):
        pass

    def on_tab_touch_move(self, *args):
        pass

    def on_tab_touch_up(self, *args):
        pass

    def on_tab_press(self, *args):
        par = self.parent_widget
        if par.previous_tab is not self:
            if par.previous_tab.index > self.index:
                par.ids.tab_manager.transition.direction = "right"
            elif par.previous_tab.index < self.index:
                par.ids.tab_manager.transition.direction = "left"
            par.ids.tab_manager.current = self.name
            par.previous_tab = self

    def on_tab_release(self, *args):
        pass

    def __repr__(self):
        return f"<MDTab name='{self.name}', text='{self.text}'>"


class MDBottomNavigationItem(MDTab):
    header = ObjectProperty()
    """
    :attr:`header` is an :class:`~MDBottomNavigationHeader`
    and defaults to `None`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def animate_header(
        self, bottom_navigation_object, bottom_navigation_header_object
    ) -> None:
        if bottom_navigation_object.use_text:
            Animation(_label_font_size=sp(12), d=0.1).start(
                bottom_navigation_object.previous_tab.header
            )
        Animation(
            _selected_region_width=0,
            t="in_out_sine",
            d=0,
        ).start(bottom_navigation_header_object)
        Animation(
            _text_color_normal=bottom_navigation_header_object.text_color_normal
            if bottom_navigation_object.previous_tab.header.text_color_normal
            != [1, 1, 1, 1]
            else self.theme_cls.disabled_hint_text_color,
            d=0.1,
        ).start(bottom_navigation_object.previous_tab.header)
        bottom_navigation_object.previous_tab.header.active = False
        self.header.active = True

    def on_tab_press(self, *args) -> None:
        """Called when clicking on a panel item."""

        bottom_navigation_object = self.parent_widget
        bottom_navigation_header_object = (
            bottom_navigation_object.previous_tab.header
        )

        if bottom_navigation_object.previous_tab is not self:
            self.animate_header(
                bottom_navigation_object, bottom_navigation_header_object
            )

        super().on_tab_press(*args)

    def on_disabled(
        self, instance_bottom_navigation_item, disabled_value: bool
    ) -> None:
        self.header.disabled = disabled_value

    def on_leave(self, *args):
        pass


class TabbedPanelBase(
    ThemableBehavior, SpecificBackgroundColorBehavior, BoxLayout
):
    """
    A class that contains all variables a :class:`~kivy.properties.TabPannel`
    must have. It is here so I (zingballyhoo) don't get mad about
    the :class:`~kivy.properties.TabbedPannels` not being DRY.

    For more information, see in the :class:`~kivymd.theming.ThemableBehavior`
    and :class:`~kivymd.uix.behaviors.SpecificBackgroundColorBehavior`
    and :class:`~kivy.uix.boxlayout.BoxLayout` classes documentation.
    """

    current = StringProperty(None)
    """
    Current tab name.

    :attr:`current` is an :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
    """

    previous_tab = ObjectProperty(None, aloownone=True)
    """
    :attr:`previous_tab` is an :class:`~MDTab` and defaults to `None`.
    """

    panel_color = ColorProperty(None)
    """
    Panel color of bottom navigation.

    :attr:`panel_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    tabs = ListProperty()


class MDBottomNavigation(DeclarativeBehavior, TabbedPanelBase):
    """
    A bottom navigation that is implemented by delegating all items to a
    :class:`~kivy.uix.screenmanager.ScreenManager`.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.DeclarativeBehavior` and
    :class:`~TabbedPanelBase` classes documentation.

    :Events:
        :attr:`on_switch_tabs`
            Called when switching tabs. Returns the object of the tab to be
            opened.

        .. versionadded:: 1.0.0
    """

    transition = ObjectProperty(FadeTransition)
    """
    Transition animation of bottom navigation screen manager.

    .. versionadded:: 1.1.0

    :attr:`transition` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `FadeTransition`.
    """

    transition_duration = NumericProperty(0.2)
    """
    Duration animation of bottom navigation screen manager.

    .. versionadded:: 1.1.0

    :attr:`transition_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    text_color_normal = ColorProperty([1, 1, 1, 1])
    """
    Text color of the label when it is not selected.

    .. code-block:: kv

        MDBottomNavigation:
            text_color_normal: 1, 0, 1, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-navigation-text_color_normal.png

    :attr:`text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 1]`.
    """

    text_color_active = ColorProperty([1, 1, 1, 1])
    """
    Text color of the label when it is selected.

    .. code-block:: kv

        MDBottomNavigation:
            text_color_active: 0, 0, 0, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-navigation-text_color_active.png

    :attr:`text_color_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 1]`.
    """

    use_text = BooleanProperty(True)
    """
    Use text for :class:`~MDBottomNavigationItem` or not.
    If ``True``, the :class:`~MDBottomNavigation` panel height will be reduced
    by the text height.

    .. versionadded:: 1.0.0

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-navigation-use-text.png
        :align: center

    :attr:`use_text` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    selected_color_background = ColorProperty(None)
    """
    The background color of the highlighted item when using Material Design v3.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDBottomNavigation:
            selected_color_background: 0, 0, 1, .4

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-navigation=selected-color-background.png

    :attr:`selected_color_background` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    font_name = StringProperty("Roboto")
    """
    Font name of the label.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDBottomNavigation:
            font_name: "path/to/font.ttf"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-navigation-font-name.png

    :attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Roboto'`.
    """

    first_widget = ObjectProperty()
    """
    :attr:`first_widget` is an :class:`~MDBottomNavigationItem`
    and defaults to `None`.
    """

    tab_header = ObjectProperty()
    """
    :attr:`tab_header` is an :class:`~MDBottomNavigationHeader`
    and defaults to `None`.
    """

    set_bars_color = BooleanProperty(False)
    """
    If `True` the background color of the navigation bar will be set
    automatically according to the current color of the toolbar.

    .. versionadded:: 1.0.0

    :attr:`set_bars_color` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    widget_index = NumericProperty(0)

    # Text active color if it is selected.
    _active_color = ColorProperty([1, 1, 1, 1])

    def __init__(self, *args, **kwargs):
        self.previous_tab = None
        self.register_event_type("on_switch_tabs")
        super().__init__(*args, **kwargs)
        self.theme_cls.bind(material_style=self.refresh_tabs)
        Window.bind(on_resize=self.on_resize)
        Clock.schedule_once(lambda x: self.on_resize())
        Clock.schedule_once(self.set_status_bar_color)

    def set_status_bar_color(self, interval: Union[int, float]) -> None:
        if self.set_bars_color:
            set_bars_colors(self.panel_color, None, self.theme_cls.theme_style)

    def switch_tab(self, name_tab) -> None:
        """Switching the tab by name."""

        if not self.ids.tab_manager.has_screen(name_tab):
            raise ScreenManagerException(f"No Screen with name '{name_tab}'.")
        self.ids.tab_manager.get_screen(name_tab).dispatch("on_tab_press")
        count_index_screen = [
            self.ids.tab_manager.screens.index(screen)
            for screen in self.ids.tab_manager.screens
            if screen.name == name_tab
        ][0]
        numbers_screens = list(range(len(self.ids.tab_manager.screens)))
        numbers_screens.reverse()
        self.ids.tab_bar.children[
            numbers_screens.index(count_index_screen)
        ].dispatch("on_press")

    def refresh_tabs(self, *args) -> None:
        """Refresh all tabs."""

        if self.ids:
            tab_bar = self.ids.tab_bar
            tab_bar.clear_widgets()
            tab_manager = self.ids.tab_manager
            self._active_color = self.theme_cls.primary_color

            if self.text_color_active != [1, 1, 1, 1]:
                self._active_color = self.text_color_active

            for tab in tab_manager.screens:
                self.tab_header = MDBottomNavigationHeader(tab=tab, panel=self)
                tab.header = self.tab_header
                tab_bar.add_widget(self.tab_header)

                if tab is self.first_widget:
                    self.tab_header._text_color_normal = self._active_color
                    self.tab_header._label_font_size = sp(14)
                    self.tab_header.active = True
                else:
                    self.tab_header.ids._label.font_size = sp(12)
                    self.tab_header._label_font_size = sp(12)

    def on_font_name(self, instance_bottom_navigation, font_name: str) -> None:
        for tab in self.ids.tab_bar.children:
            tab.ids._label.font_name = font_name

    def on_selected_color_background(
        self, instance_bottom_navigation, color: list
    ) -> None:
        def on_selected_color_background(*args):
            for tab in self.ids.tab_bar.children:
                tab.selected_color_background = color

        Clock.schedule_once(on_selected_color_background)

    def on_use_text(
        self, instance_bottom_navigation, use_text_value: bool
    ) -> None:
        if not use_text_value:
            for instance_bottom_navigation_header in self.ids.tab_bar.children:
                instance_bottom_navigation_header.ids.item_container.remove_widget(
                    instance_bottom_navigation_header.ids._label
                )
            if self.theme_cls.material_style == "M2":
                height = dp(42)
            else:
                height = dp(80)
            self.height = height
            self.ids.bottom_panel.height = height
            self.ids.tab_bar.height = height
        else:
            if self.theme_cls.material_style == "M2":
                height = STANDARD_INCREMENT
            else:
                height = dp(80)
            self.height = height
            self.ids.bottom_panel.height = height
            self.ids.tab_bar.height = height

    def on_text_color_normal(
        self, instance_bottom_navigation, color: list
    ) -> None:
        MDBottomNavigationHeader.text_color_normal = color
        for tab in self.ids.tab_bar.children:
            if not tab.active:
                tab._text_color_normal = color

    def on_text_color_active(
        self, instance_bottom_navigation, color: list
    ) -> None:
        def on_text_color_active(*args):
            MDBottomNavigationHeader.text_color_active = color
            self.text_color_active = color
            for tab in self.ids.tab_bar.children:
                tab.text_color_active = color
                if tab.active:
                    tab._text_color_normal = color

        Clock.schedule_once(on_text_color_active)

    def on_switch_tabs(self, bottom_navigation_item, name_tab: str) -> None:
        """
        Called when switching tabs. Returns the object of the tab to be opened.
        """

    def on_size(self, *args) -> None:
        self.on_resize()

    def on_resize(
        self,
        instance: Union[WindowSDL, None] = None,
        width: Union[int, None] = None,
        do_again: bool = True,
    ) -> None:
        """Called when the application window is resized."""

        full_width = 0
        for tab in self.ids.tab_manager.screens:
            full_width += tab.header.width
            tab.header.text_color_normal = self.text_color_normal
        self.ids.tab_bar.width = full_width
        if do_again:
            Clock.schedule_once(lambda x: self.on_resize(do_again=False), 0.1)

    def add_widget(self, widget, **kwargs):
        if isinstance(widget, MDBottomNavigationItem):
            self.widget_index += 1
            widget.index = self.widget_index
            widget.parent_widget = self
            self.ids.tab_manager.add_widget(widget)
            if self.widget_index == 1:
                self.previous_tab = widget
                self.first_widget = widget
            self.refresh_tabs()
        else:
            super().add_widget(widget)

    def remove_widget(self, widget):
        if isinstance(widget, MDBottomNavigationItem):
            self.ids.tab_manager.remove_widget(widget)
            self.refresh_tabs()
        else:
            super().remove_widget(widget)

    def _get_switchig_tab(self, name_tab: str) -> MDBottomNavigationItem:
        bottom_navigation_item = None
        for bottom_navigation_header_instance in self.ids.tab_bar.children:
            if bottom_navigation_header_instance.tab.name == name_tab:
                bottom_navigation_item = bottom_navigation_header_instance.tab
                break
        return bottom_navigation_item


class MDBottomNavigationBar(CommonElevationBehavior, MDFloatLayout):
    pass
