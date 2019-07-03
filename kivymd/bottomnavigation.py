"""
BottomNavigation
================

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Tabs <https://material.io/design/components/tabs.html>`_
"""

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.metrics import dp, sp
from kivy.properties import (
    StringProperty,
    ListProperty,
    ObjectProperty,
    BoundedNumericProperty,
    NumericProperty,
    BooleanProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

from kivymd.backgroundcolorbehavior import (
    BackgroundColorBehavior,
    SpecificBackgroundColorBehavior,
)
from kivymd.button import BaseFlatButton, BasePressedButton
from kivymd.elevation import RectangularElevationBehavior
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
#:import sm kivy.uix.screenmanager
#:import Window kivy.core.window.Window


<MDBottomNavigation>
    id: panel
    orientation: 'vertical'
    height: dp(56)  # Spec

    ScreenManager:
        id: tab_manager
        transition: sm.FadeTransition(duration=.2)
        current: root.current
        screens: root.tabs

    MDBottomNavigationBar:
        size_hint_y: None
        height: dp(56)  # Spec
        md_bg_color: root.theme_cls.bg_dark

        BoxLayout:
            pos_hint: {'center_x': .5, 'center_y': .5}
            id: tab_bar
            height: dp(56)
            pos: self.pos
            size_hint_x: None
            size_hint: None, None


<MDBottomNavigationHeader>
    canvas:
        Color:
            rgba: self.panel.theme_cls.bg_dark
        Rectangle:
            size: self.size
            pos: self.pos

    width:
        root.panel.width / len(root.panel.ids.tab_manager.screens)\
        if len(root.panel.ids.tab_manager.screens) != 0 else root.panel.width
    padding: (dp(12), dp(12))
    on_press:
        self.tab.dispatch('on_tab_press')
    on_release: self.tab.dispatch('on_tab_release')
    on_touch_down: self.tab.dispatch('on_tab_touch_down',*args)
    on_touch_move: self.tab.dispatch('on_tab_touch_move',*args)
    on_touch_up: self.tab.dispatch('on_tab_touch_up',*args)

    FloatLayout:

        MDIcon:
            id: _label_icon
            icon: root.tab.icon
            size_hint_x: None
            text_size: (None, root.height)
            height: self.texture_size[1]
            theme_text_color: 'Custom'
            text_color: root._current_color
            valign: 'middle'
            halign: 'center'
            opposite_colors: root.opposite_colors
            pos: [self.pos[0], self.pos[1]]
            font_size: dp(24)
            pos_hint: {'center_x': .5, 'center_y': .7}

        MDLabel:
            id: _label
            text: root.tab.text
            font_style: 'Button'
            size_hint_x: None
            text_size: (None, root.height)
            height: self.texture_size[1]
            theme_text_color: 'Custom'
            text_color: root._current_color
            valign: 'bottom'
            halign: 'center'
            opposite_colors: root.opposite_colors
            font_size: root._label_font_size
            pos_hint: {'center_x': .5, 'center_y': .6}


<MDTab>
    canvas:
        Color:
            rgba: root.theme_cls.bg_normal
        Rectangle:
            size: root.size
"""
)


class MDBottomNavigationBar(
    ThemableBehavior, BackgroundColorBehavior, FloatLayout, RectangularElevationBehavior
):
    pass


class MDBottomNavigationErrorCache:
    last_size_warning = 0


def small_error_warn(x):
    if dp(x) <= dp(80):
        if MDBottomNavigationErrorCache.last_size_warning != x:
            MDBottomNavigationErrorCache.last_size_warning = x
            Logger.warning(
                f"MDBottomNavigation: {x}dp is less than the minimum size "
                f"of 80dp for a MDBottomNavigationItem. "
                f"We must now expand to 168dp."
            )
            # Did you come here to find out what the bug is?
            # The bug is that on startup, this function returning dp(80)
            # breaks the way it displays until you resize
            # I don't know why, this may or may not get fixed in the future
    return dp(168)


class MDBottomNavigationHeader(BaseFlatButton, BasePressedButton):
    width = BoundedNumericProperty(
        dp(0), min=dp(80), max=dp(168), errorhandler=lambda x: small_error_warn(x)
    )
    tab = ObjectProperty(None)
    panel = ObjectProperty(None)
    _label = ObjectProperty()
    _label_font_size = NumericProperty(sp(12))
    _current_color = ListProperty([0.0, 0.0, 0.0, 0.0])
    text = StringProperty("")
    _capitalized_text = StringProperty("")
    active = BooleanProperty(False)

    def on_text(self, instance, value):
        self._capitalized_text = value.upper()

    def __init__(self, panel, height, tab):
        self.panel = panel
        self.height = height
        self.tab = tab
        super().__init__()
        self._current_color = self.theme_cls.disabled_hint_text_color
        self._label = self.ids._label
        self._label_font_size = sp(12)
        self.theme_cls.bind(
            primary_color=self._update_theme_color,
            disabled_hint_text_color=self._update_theme_style,
        )
        self.active = False

    def on_press(self):
        Animation(_label_font_size=sp(14), d=0.1).start(self)
        Animation(_current_color=self.theme_cls.primary_color, d=0.1).start(self)

    def _update_theme_color(self, instance, color):
        if self.active:
            self._current_color = self.theme_cls.primary_color

    def _update_theme_style(self, instance, color):
        if not self.active:
            self._current_color = self.theme_cls.disabled_hint_text_color


class MDTab(Screen, ThemableBehavior):
    """ A tab is simply a screen with meta information
        that defines the content that goes in the tab header.
    """

    __events__ = (
        "on_tab_touch_down",
        "on_tab_touch_move",
        "on_tab_touch_up",
        "on_tab_press",
        "on_tab_release",
    )

    # Tab header text
    text = StringProperty()

    # Tab header icon
    icon = StringProperty("checkbox-blank-circle")

    # Tab dropdown menu items
    menu_items = ListProperty()

    # Tab dropdown menu (if you want to customize it)
    menu = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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

    def on_tab_press(self, *args):
        par = self.parent_widget
        par.ids.tab_manager.current = self.name
        if par.previous_tab is not self:
            Animation(_label_font_size=sp(12), d=0.1).start(par.previous_tab.header)
            Animation(
                _current_color=par.previous_tab.header.theme_cls.disabled_hint_text_color,
                d=0.1,
            ).start(par.previous_tab.header)
            par.previous_tab.header.active = False
            self.header.active = True
        par.previous_tab = self

    def on_leave(self, *args):
        pass


class TabbedPanelBase(ThemableBehavior, SpecificBackgroundColorBehavior, BoxLayout):
    """
    A class that contains all variables a TabPannel must have
    It is here so I (zingballyhoo) don't get mad about
    the TabbedPannels not being DRY
    """

    tabs = ListProperty([])

    # Current tab name
    current = StringProperty(None)

    previous_tab = ObjectProperty(None)


class MDBottomNavigation(TabbedPanelBase):
    """ A bottom navigation that is implemented by delegating
    all items to a ScreenManager."""

    first_widget = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.previous_tab = None
        self.widget_index = 0
        self._refresh_tabs()
        Window.bind(on_resize=self.on_resize)
        Clock.schedule_once(lambda x: self.on_resize(), 2)

    def _refresh_tabs(self):
        """ Refresh all tabs """

        if not self.ids:
            return
        tab_bar = self.ids.tab_bar
        tab_bar.clear_widgets()
        tab_manager = self.ids.tab_manager
        for tab in tab_manager.screens:
            tab_header = MDBottomNavigationHeader(
                tab=tab, panel=self, height=tab_bar.height
            )
            tab.header = tab_header
            tab_bar.add_widget(tab_header)
            if tab is self.first_widget:
                tab_header._current_color = self.theme_cls.primary_color
                tab_header._label_font_size = sp(14)
                tab_header.active = True
            else:
                tab_header._label_font_size = sp(12)
        self.on_resize()

    def on_resize(self, instance=None, width=None, do_again=True):
        full_width = 0
        for tab in self.ids.tab_manager.screens:
            full_width += tab.header.width
        self.ids.tab_bar.width = full_width
        if do_again:
            Clock.schedule_once(lambda x: self.on_resize(do_again=False), 0.01)

    def add_widget(self, widget, **kwargs):
        """ Add tabs to the screen or the layout.
        :param widget: The widget to add.
        """

        if isinstance(widget, MDBottomNavigationItem):
            self.widget_index += 1
            widget.index = self.widget_index
            widget.parent_widget = self
            tab_header = MDBottomNavigationHeader(
                tab=widget, panel=self, height=widget.height
            )
            self.ids.tab_bar.add_widget(tab_header)
            widget.header = tab_header
            self.ids.tab_manager.add_widget(widget)
            if self.widget_index == 1:
                self.previous_tab = widget
                tab_header._current_color = self.theme_cls.primary_color
                tab_header._label_font_size = sp(14)
                tab_header.active = True
                self.first_widget = widget
            else:
                tab_header._label_font_size = sp(12)

            self._refresh_tabs()
        else:
            super().add_widget(widget)

    def remove_widget(self, widget):
        """ Remove tabs from the screen or the layout.
        :param widget: The widget to remove.
        """

        if isinstance(widget, MDBottomNavigationItem):
            self.ids.tab_manager.remove_widget(widget)
            self._refresh_tabs()
        else:
            super().remove_widget(widget)


if __name__ == "__main__":
    from kivy.app import App
    from kivymd.theming import ThemeManager

    class TabsApp(App):
        theme_cls = ThemeManager()

        def build(self):
            from kivy.core.window import Window

            Window.size = (540, 720)

            return Builder.load_string(
                """
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import MDRaisedButton kivymd.button.MDRaisedButton


BoxLayout:
    orientation:'vertical'

    MDToolbar:
        id: toolbar
        title: 'Page title'
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: '']]

    MDBottomNavigation:

        MDBottomNavigationItem:
            name: 'files1'
            text: 'Python'
            icon: 'language-python'
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: 'I love Python'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'files2'
            text: 'C++'
            icon: 'language-cpp'
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: 'I programming of C++'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'files3'
            text: 'JS'
            icon: 'language-javascript'
            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: 'Oh god JS again'
                halign: 'center'
"""
            )

    TabsApp().run()
