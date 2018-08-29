'''
Navigation Drawer
=================

`Material Design spec page <https://material.io/guidelines/patterns/navigation-drawer.html>`_

API
---
'''

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ListProperty, BooleanProperty,\
    OptionProperty, Clock
from kivy.uix.boxlayout import BoxLayout

from kivymd import images_path
from kivymd.elevationbehavior import RectangularElevationBehavior
from kivymd.icon_definitions import md_icons
from kivymd.label import MDLabel
from kivymd.list import BaseListItem, ILeftBody, OneLineListItem, OneLineIconListItem, IRightBody
from kivymd.theming import ThemableBehavior
from kivymd.toolbar import Toolbar
from kivymd.vendor.navigationdrawer import (NavigationDrawer as VendorNavigationDrawer)

Builder.load_string("""
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDList kivymd.list.MDList
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import colors kivymd.color_definitions.colors
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import ScrollView kivy.uix.scrollview.ScrollView
#:import Window kivy.core.window.Window

<NavigationDrawerToolbar>
    elevation: 0
    specific_text_color: root.theme_cls.secondary_text_color
    opposite_colors: False
    title_theme_color: 'Secondary'
    md_bg_color: root.theme_cls.bg_light
    canvas:
        Color:
            rgba: root.theme_cls.divider_color
        Line:
            points: self.x, self.y, self.x+self.width,self.y
<NavigationLayout>
<MDNavigationDrawer>:
    _list: list
    _header_container: _header_container
    canvas:
        Color:
            rgba: root.theme_cls.bg_light
        Rectangle:
            size: root.size
            pos: root.pos
    canvas.before:
        Color:
            rgba: root.shadow_color
        Rectangle:
            size: Window.size
            pos: 0, 0
    BoxLayout:
        id: _header_container
        size_hint_y: None
        height: _header_container.minimum_height
    ScrollView:
        do_scroll_x: False
        MDList:
            id: list

<NavigationDrawerIconButton>:
    theme_text_color: 'Primary' if not root._active else 'Custom' if root.use_active else 'Primary'
    text_color: root.theme_cls.secondary_text_color if not root._active else root.active_color if \
        root.active_color_type == "custom" else root._active_color if root.use_active else \
        root.theme_cls.secondary_text_color
    NDIconLabel:
        id: _icon
        font_style: 'Icon'
        theme_text_color: 'Secondary' if not root._active else 'Custom' if root.use_active else 'Custom'
        text_color: root.theme_cls.secondary_text_color if not root._active else root.active_color if \
            root.active_color_type == "custom" else root._active_color if root.use_active else \
            root.theme_cls.secondary_text_color
    BoxLayout:
        id: _right_container
        size_hint: None, None
        x: root.x + root.width - _badge.texture_size[0] - dp(25) #  - m_res.HORIZ_MARGINS
        y: root.y + root.height/2 - self.height/2
        size: dp(70), root.height
    NDBadgeLabel:
        id: _badge
        theme_text_color: 'Secondary' if not root._active else 'Custom' if root.use_active else 'Custom'
        text_color: root.theme_cls.secondary_text_color if not root._active else root.active_color if \
            root.active_color_type == "custom" else root._active_color if root.use_active else \
            root.theme_cls.secondary_text_color
        text: root.badge_text
        halign: 'right'


<NavigationDrawerDivider>:
    canvas:
        Color:
            rgba: self.theme_cls.divider_color
        Line:
            points: root.x ,root.y+dp(8), root.x+self.width, root.y+dp(8)
""")


class NDIconLabel(ILeftBody, MDLabel):
    pass


class NDBadgeLabel(IRightBody, MDLabel):
    pass


class NavigationDrawerHeaderBase:
    '''
    Tells the :class:`~MDNavigationDrawer` that this should be in the header area (above the
    :class:`~kivy.uix.scrollview.ScrollView`).
    '''

    pass


class NavigationDrawerToolbar(Toolbar, NavigationDrawerHeaderBase):
    def _update_specific_text_color(self, instance, value):
        pass


class NavigationDrawerIconButton(OneLineIconListItem):
    '''
    An item in the :class:`MDNavigationDrawer`.
    '''
    _active = BooleanProperty(False)
    _active_color = ListProperty()
    _icon = ObjectProperty()
    divider = None

    active_color = ListProperty()
    '''Custom active color.
    This option only takes effect when :attr:`active_color_type` = 'custom'.

    :attr:`active_color` is a :class:`~kivy.properties.ListProperty` and defaults to None.
    '''

    active_color_type = OptionProperty('primary', options=['primary', 'accent', 'custom'])
    '''Decides which color should be used for the active color.
    This option only takes effect when :attr:`use_active` = True.

    Options:
        primary: Active color will be the primary theme color.

        accent: Active color will be the theme's accent color.

        custom: Active color will be taken from the :attr:`active_color` attribute.

    :attr:`active_color_type` is a :class:`~kivy.properties.OptionProperty` and defaults to 'primary'.
    '''

    icon = StringProperty('checkbox-blank-circle')
    '''Icon that appears to the left of the widget.

    :attr:`icon` is a :class:`~kivy.properties.StringProperty` and defaults to 'checkbox-blank-circle'.
    '''
    badge_text = StringProperty('')
    '''
    Text that appears on the right side of the item, usually for displaying a count of sorts.


    :attr:`badge_text` is a :class:`~kivy.properties.StringProperty` and defaults to ''.
    '''
    use_active = BooleanProperty(True)
    '''If the button should change to the active color when selected.

    :attr:`use_active` is a :class:`~kivy.properties.BooleanProperty` and defaults to True.

    See also:
        :attr:`active_color`

        :attr:`active_color_type`
    '''

    # active_color = get_color_from_hex(colors['Red']['500'])
    # active_color_type = 'custom'

    def __init__(self, **kwargs):
        super(NavigationDrawerIconButton, self).__init__(**kwargs)
        self._set_active_color()
        self.theme_cls.bind(primary_color=self._set_active_color_primary, accent_color=self._set_active_color_accent)
        Clock.schedule_once(lambda x: self.on_icon(self, self.icon))

    def _set_active(self, active, list):
        if self.use_active:
            self._active = active
            if list.active_item != self:
                if list.active_item is not None:
                    list.active_item._active = False
            list.active_item = self

    def _set_active_color(self, *args):
        if self.active_color_type == 'primary':
            self._set_active_color_primary()
        elif self.active_color_type == 'accent':
            self._set_active_color_accent()

    # Note to future developers/myself: These must be separate functions
    def _set_active_color_primary(self, *args):
        if self.active_color_type == 'primary':
            self._active_color = self.theme_cls.primary_color

    def _set_active_color_accent(self, *args):
        if self.active_color_type == 'accent':
            self._active_color = self.theme_cls.accent_color

    def on_icon(self, instance, value):
        self.ids['_icon'].text = u"{}".format(md_icons[value])

    def on_active_color_type(self, *args):
        self._set_active_color(args)


class NavigationDrawerSubheader(OneLineListItem):
    '''
    A subheader for separating content in :class:`MDNavigationDrawer`

    Works well alongside :class:`NavigationDrawerDivider`
    '''
    disabled = True
    divider = None
    theme_text_color = 'Secondary'


class NavigationDrawerDivider(OneLineListItem):
    '''
    A small full-width divider that can be placed in the :class:`MDNavigationDrawer`
    '''
    disabled = True
    divider = None
    _txt_top_pad = NumericProperty(dp(8))
    _txt_bot_pad = NumericProperty(dp(8))

    def __init__(self, **kwargs):
        super(OneLineListItem, self).__init__(**kwargs)
        self.height = dp(16)


class MDNavigationDrawer(BoxLayout, ThemableBehavior, RectangularElevationBehavior):
    '''
    '''
    _elevation = NumericProperty(0)
    _header_container = ObjectProperty()
    _list = ObjectProperty()
    active_item = ObjectProperty(None)
    orientation = 'vertical'
    panel = ObjectProperty()
    shadow_color = ListProperty([0, 0, 0, 0])

    def __init__(self, **kwargs):
        super(MDNavigationDrawer, self).__init__(**kwargs)

    def add_widget(self, widget, index=0):
        '''
        If the widget is a subclass of :class:`~NavigationDrawerHeaderBase`, then it will be placed above the
        :class:`~kivy.uix.scrollview.ScrollView`. Otherwise, it will be placed in the main
        :class:`~kivy.uix.scrollview.ScrollView` content area.
        '''
        if issubclass(widget.__class__, BaseListItem):
            self._list.add_widget(widget, index)
            if len(self._list.children) == 1:
                widget._active = True
                self.active_item = widget
            widget.bind(on_release=lambda x: self.panel.toggle_state())
            widget.bind(on_release=lambda x: x._set_active(True, list=self))
        elif issubclass(widget.__class__, NavigationDrawerHeaderBase):
            self._header_container.add_widget(widget)
        else:
            super(MDNavigationDrawer, self).add_widget(widget, index)


class NavigationLayout(VendorNavigationDrawer, ThemableBehavior):
    '''
    The container layout that manages the :class:`MDNavigationDrawer`.
    '''
    opening_transition = StringProperty('out_sine')
    closing_transition = StringProperty('out_sine')
    min_dist_to_open = NumericProperty(0.2)
    min_dist_to_close = NumericProperty(0.8)
    anim_time = NumericProperty(0.2)
    separator_image = StringProperty('{}'.format(images_path + '/transparent.png'))
    side_panel_positioning = 'left'
    side_panel_width = NumericProperty(dp(320))
    max_shadow_opacity = NumericProperty(0.5)
    anim_type = StringProperty('slide_above_simple')

    def __init__(self, **kwargs):
        super(NavigationLayout, self).__init__(**kwargs)
        self.on_anim_type()

    def _anim_relax(self):
        if self.state == 'open':
            if self._anim_progress < self.min_dist_to_close:
                self.anim_to_state('closed')
            else:
                self.anim_to_state('open')
        else:
            if self._anim_progress > self.min_dist_to_open:
                self.anim_to_state('open')
            else:
                self.anim_to_state('closed')

    def on__anim_progress(self, *args):
        self.side_panel.shadow_color = [0, 0, 0, self.max_shadow_opacity*self._anim_progress]
        self.side_panel.elevation = 1 * self._anim_progress
        if self._anim_progress > 1:
            self._anim_progress = 1
        elif self._anim_progress < 0:
            self._anim_progress = 0
        if self._anim_progress >= 1:
            self.state = 'open'
        elif self._anim_progress <= 0:
            self.state = 'closed'

    def add_widget(self, widget, **kwargs):
        '''
        First widget added must be the content for the side/sliding panel.
        The next widget must be the main content.

        This layout only accepts two widgets, any more than two widgets will raise a ValueError
        '''
        # Internal default BoxLayouts
        if len(self.children) == 0:
            super(NavigationLayout, self).add_widget(widget)
            self._side_panel = widget
        elif len(self.children) == 1:
            super(NavigationLayout, self).add_widget(widget)
            self._main_panel = widget
        elif len(self.children) == 2:
            super(NavigationLayout, self).add_widget(widget)
            self._join_image = widget

        # Adding of user widgets
        elif self.side_panel is None:
            self.set_side_panel(widget)
            widget.panel = self
        elif self.main_panel is None:
            self.set_main_panel(widget)
        else:
            raise ValueError('Can\'t add more than two widgets directly to NavigationLayout')

    def toggle_nav_drawer(self):
        self.toggle_state(True)
