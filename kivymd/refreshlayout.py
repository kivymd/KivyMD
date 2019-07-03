"""
ScrollView Refresh Layout
=========================

Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

Example
-------

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty

from kivymd.button import MDIconButton
from kivymd.icon_definitions import md_icons
from kivymd.list import ILeftBodyTouch, OneLineIconListItem
from kivymd.theming import ThemeManager
from kivymd.utils import asynckivy

Builder.load_string('''
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import MDScrollViewRefreshLayout kivymd.refreshlayout.MDScrollViewRefreshLayout


<ItemForList>
    text: root.text

    IconLeftSampleWidget:
        icon: root.icon


<Example@FloatLayout>

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: app.title
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            elevation: 10
            left_action_items: [['menu', lambda x: x]]

        MDScrollViewRefreshLayout:
            id: refresh_layout
            refresh_callback: app.refresh_callback
            root_layout: root

            GridLayout:
                id: box
                size_hint_y: None
                height: self.minimum_height
                cols: 1
''')


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class ItemForList(OneLineIconListItem):
    icon = StringProperty()


class Example(App):
    title = 'Example Refresh Layout'
    theme_cls = ThemeManager()
    screen = None
    x = 0
    y = 15

    def build(self):
        self.screen = Factory.Example()
        self.set_list()

        return self.screen

    def set_list(self):
        async def set_list():
            names_icons_list = list(md_icons.keys())[self.x:self.y]
            for name_icon in names_icons_list:
                await asynckivy.sleep(0)
                self.screen.ids.box.add_widget(
                    ItemForList(icon=name_icon, text=name_icon))
        asynckivy.start(set_list())

    def refresh_callback(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.screen.ids.box.clear_widgets()
            if self.x == 0:
                self.x, self.y = 15, 30
            else:
                self.x, self.y = 0, 15
            self.set_list()
            self.screen.ids.refresh_layout.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)


Example().run()

"""

from kivy.animation import Animation
from kivy.effects.dampedscroll import DampedScrollEffect
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty, ObjectProperty, ListProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
#:import Window kivy.core.window.Window
#:import MDSpinner kivymd.spinner.MDSpinner


<RefreshSpinner>

    AnchorLayout:
        id: body_spinner
        size_hint: None, None
        size: dp(46), dp(46)
        y: Window.height
        pos_hint: {'center_x': .5}
        anchor_x: 'center'
        anchor_y: 'center'

        canvas:
            Clear
            Color:
                rgba: root.theme_cls.primary_dark
            Ellipse:
                pos: self.pos
                size: self.size

        MDSpinner:
            id: spinner
            size_hint: None, None
            size: dp(30), dp(30)
            color: 1, 1, 1, 1
"""
)


class _RefreshScrollEffect(DampedScrollEffect):
    """This class is simply based on DampedScrollEffect.
    If you need any documentation please look at kivy.effects.dampedscrolleffect.
    """

    min_scroll_to_reload = NumericProperty(-dp(100))
    """Minimum overscroll value to reload."""

    def on_overscroll(self, scrollview, overscroll):
        if overscroll < self.min_scroll_to_reload:
            scroll_view = self.target_widget.parent
            scroll_view._did_overscroll = True
            return True
        else:
            return False


class MDScrollViewRefreshLayout(ScrollView):
    root_layout = ObjectProperty()
    """The spinner will be attached to this layout."""

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.effect_cls = _RefreshScrollEffect
        self._work_spinnrer = False
        self._did_overscroll = False
        self.refresh_spinner = None

    def on_touch_up(self, *args):
        if self._did_overscroll and not self._work_spinnrer:
            if self.refresh_callback:
                self.refresh_callback()
            if not self.refresh_spinner:
                self.refresh_spinner = RefreshSpinner(_refresh_layout=self)
                self.root_layout.add_widget(self.refresh_spinner)
            self.refresh_spinner.start_anim_spinner()
            self._work_spinnrer = True
            self._did_overscroll = False
            return True

        return super().on_touch_up(*args)

    def refresh_done(self):
        if self.refresh_spinner:
            self.refresh_spinner.hide_anim_spinner()


class RefreshSpinner(ThemableBehavior, FloatLayout):
    spinner_color = ListProperty([1, 1, 1, 1])

    _refresh_layout = ObjectProperty()
    """kivymd.refreshlayout.MDScrollViewRefreshLayout object."""

    def start_anim_spinner(self):
        spinner = self.ids.body_spinner
        Animation(y=spinner.y - dp(76), d=0.8, t="out_elastic").start(spinner)

    def hide_anim_spinner(self):
        spinner = self.ids.body_spinner
        anim = Animation(y=Window.height, d=0.8, t="out_elastic")
        anim.bind(on_complete=self.set_spinner)
        anim.start(spinner)

    def set_spinner(self, *args):
        body_spinner = self.ids.body_spinner
        body_spinner.size = (dp(46), dp(46))
        body_spinner.y = Window.height
        body_spinner.opacity = 1
        spinner = self.ids.spinner
        spinner.size = (dp(30), dp(30))
        spinner.opacity = 1
        self._refresh_layout._work_spinnrer = False
        self._refresh_layout._did_overscroll = False
