# -*- coding: utf-8 -*-
'''
Buttons
=======

`Material Design spec, Buttons page <https://www.google.com/design/spec/components/buttons.html>`_

`Material Design spec, Buttons: Floating Action Button page <https://www.google.com/design/spec/components/buttons-floating-action-button.html>`_

TO-DO: DOCUMENT MODULE
'''
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty, BoundedNumericProperty, \
    ListProperty, AliasProperty, BooleanProperty, NumericProperty, \
    OptionProperty, ReferenceListProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivymd.backgroundcolorbehavior import SpecificBackgroundColorBehavior
from kivymd.ripplebehavior import CircularRippleBehavior, \
    RectangularRippleBehavior
from kivymd.elevationbehavior import CommonElevationBehavior, \
    RectangularElevationBehavior, CircularElevationBehavior
from kivymd.theming import ThemableBehavior
from kivymd.color_definitions import colors

Builder.load_string('''
#:import md_icons kivymd.icon_definitions.md_icons
#:import colors kivymd.color_definitions.colors
#:import MDLabel kivymd.label.MDLabel
<BaseButton>:
    size_hint: (None, None)
    anchor_x: 'center'
    anchor_y: 'center'

<BaseFlatButton>:

<BaseRaisedButton>:

<BaseRoundButton>:
    canvas:
        Clear
        Color:
            rgba: self._current_button_color
        Ellipse:
            size: self.size
            pos: self.pos
    size: (dp(48), dp(48))
    content: content
    padding: dp(12)
    theme_text_color: 'Primary'
    MDLabel:
        id: content
        font_style: 'Icon'
        text: u"{}".format(md_icons[root.icon])
        theme_text_color: root.theme_text_color
        text_color: root.text_color
        disabled: root.disabled
        valign: 'middle'
        halign: 'center'
        opposite_colors: root.opposite_colors

<BaseRectangularButton>:
    canvas:
        Clear
        Color:
            rgba: self._current_button_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: (dp(2),)
    content: content
    height: dp(36)
    width: content.texture_size[0] + dp(32)
    padding: (dp(8), 0)
    theme_text_color: 'Primary'
    MDLabel:
        id: content
        text: root._capitalized_text
        font_style: 'Button'
        size_hint_x: None
        text_size: (None, root.height)
        height: self.texture_size[1]
        theme_text_color: root.theme_text_color
        text_color: root.text_color
        disabled: root.disabled
        valign: 'middle'
        halign: 'center'
        opposite_colors: root.opposite_colors

<MDRaisedButton>:
    md_bg_color: root.theme_cls.primary_color
    theme_text_color: 'Custom'
    text_color: root.specific_text_color

<MDFloatingActionButton>:
    # Defaults to 56-by-56 and a backround of the accent color according to
    # guidelines
    size: (dp(56), dp(56))
    md_bg_color: root.theme_cls.accent_color
    theme_text_color: 'Custom'
    text_color: root.specific_text_color
''')


class BaseButton(ThemableBehavior, ButtonBehavior,
                 SpecificBackgroundColorBehavior, AnchorLayout):
    '''
    Abstract base class for all MD buttons. This class handles the button's
    colors (disabled/down colors handled in children classes as those depend on
    type of button) as well as the disabled state.
    '''
    _md_bg_color_down = ListProperty(None, allownone=True)
    _md_bg_color_disabled = ListProperty(None, allownone=True)
    _current_button_color = ListProperty([0., 0., 0., 0.])
    theme_text_color = OptionProperty(None, allownone=True,
                                      options=['Primary', 'Secondary', 'Hint',
                                               'Error', 'Custom',
                                               'ContrastParentBackground'])
    text_color = ListProperty(None, allownone=True)
    opposite_colors = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(BaseButton, self).__init__(**kwargs)
        Clock.schedule_once(self._finish_init)

    def _finish_init(self, dt):
        self._update_color()

    def on_md_bg_color(self, instance, value):
        self._update_color()

    def _update_color(self):
        if not self.disabled:
            self._current_button_color = self.md_bg_color
        else:
            self._current_button_color = self.md_bg_color_disabled

    def _call_get_bg_color_down(self):
        return self._get_md_bg_color_down()

    def _get_md_bg_color_down(self):
        if self._md_bg_color_down:
            return self._md_bg_color_down
        else:
            raise NotImplementedError

    def _set_md_bg_color_down(self, value):
        self._md_bg_color_down = value

    md_bg_color_down = AliasProperty(_call_get_bg_color_down,
                                          _set_md_bg_color_down)

    def _call_get_bg_color_disabled(self):
        return self._get_md_bg_color_disabled()

    def _get_md_bg_color_disabled(self):
        if self._md_bg_color_disabled:
            return self._md_bg_color_disabled
        else:
            raise NotImplementedError

    def _set_md_bg_color_disabled(self, value):
        self._md_bg_color_disabled = value

    md_bg_color_disabled = AliasProperty(_call_get_bg_color_disabled,
                                              _set_md_bg_color_disabled)

    def on_disabled(self, instance, value):
        if value:
            self._current_button_color = self.md_bg_color_disabled
        else:
            self._current_button_color = self.md_bg_color
        super(BaseButton, self).on_disabled(instance, value)


class BasePressedButton(BaseButton):
    '''
    Abstract base class for those button which fade to a background color on
    press.
    '''
    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            return False
        elif not self.collide_point(touch.x, touch.y):
            return False
        elif self in touch.ud:
            return False
        elif self.disabled:
            return False
        else:
            self.fade_bg = Animation(duration=.5,
                    _current_button_color=self.md_bg_color_down)
            self.fade_bg.start(self)
            return super(BaseButton, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            self.fade_bg.stop_property(self, '_current_button_color')
            Animation(duration=.05,
                      _current_button_color=self.md_bg_color).start(self)
        return super(BaseButton, self).on_touch_up(touch)


class BaseFlatButton(BaseButton):
    '''
    Abstract base class for flat buttons which do not elevate from material.

    Enforces the recommended down/disabled colors for flat buttons
    '''

    def __init__(self, **kwargs):
        super(BaseFlatButton, self).__init__(**kwargs)
        self.md_bg_color = (0., 0., 0., 0.)

    def _get_md_bg_color_down(self):
        if self.theme_cls.theme_style == 'Dark':
            c = get_color_from_hex('cccccc')
            c[3] = 0.25
        else:
            c = get_color_from_hex('999999')
            c[3] = 0.4
        return c

    def _get_md_bg_color_disabled(self):
        bg_c = self.md_bg_color
        if bg_c[3] == 0:  # transparent background
            c = bg_c
        else:
            if self.theme_cls.theme_style == 'Dark':
                c = (1., 1., 1., 0.12)
            else:
                c = (0., 0., 0., 0.12)
        return c


class BaseRaisedButton(CommonElevationBehavior, BaseButton):
    '''
    Abstract base class for raised buttons which elevate from material.
    Raised buttons are to be used sparingly to emphasise primary/important
    actions.

    Implements elevation behavior as well as the recommended down/disabled
    colors for raised buttons.
    '''
    def __init__(self, **kwargs):
        if self.elevation_raised == 0 and self.elevation_normal + 6 <= 12:
            self.elevation_raised = self.elevation_normal + 6
        elif self.elevation_raised == 0:
            self.elevation_raised = 12
        super(BaseRaisedButton, self).__init__(**kwargs)
        self.elevation_press_anim = Animation(elevation=self.elevation_raised,
                                              duration=.2, t='out_quad')
        self.elevation_release_anim = Animation(
            elevation=self.elevation_normal, duration=.2, t='out_quad')

    _elev_norm = NumericProperty(2)

    def _get_elev_norm(self):
        return self._elev_norm

    def _set_elev_norm(self, value):
        self._elev_norm = value if value <= 12 else 12
        self._elev_raised = (value + 6) if value + 6 <= 12 else 12
        self.elevation = self._elev_norm
        self.elevation_release_anim = Animation(elevation=value,
                                                duration=.2, t='out_quad')

    elevation_normal = AliasProperty(_get_elev_norm, _set_elev_norm,
                                     bind=('_elev_norm',))

    _elev_raised = NumericProperty(8)

    def _get_elev_raised(self):
        return self._elev_raised

    def _set_elev_raised(self, value):
        self._elev_raised = value if value + self._elev_norm <= 12 else 12
        self.elevation_press_anim = Animation(elevation=value,
                                              duration=.2, t='out_quad')

    elevation_raised = AliasProperty(_get_elev_raised, _set_elev_raised,
                                     bind=('_elev_raised',))

    def on_disabled(self, instance, value):
        if value:
            self.elevation = 0
        else:
            self.elevation = self.elevation_normal
        super(BaseRaisedButton, self).on_disabled(instance, value)
    
    def on_touch_down(self, touch):
        if not self.disabled:
            if touch.is_mouse_scrolling:
                return False
            if not self.collide_point(touch.x, touch.y):
                return False
            if self in touch.ud:
                return False
            self.elevation_press_anim.stop(self)
            self.elevation_press_anim.start(self)
        return super(BaseRaisedButton, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if not self.disabled:
            if touch.grab_current is not self:
                return super(ButtonBehavior, self).on_touch_up(touch)
            self.elevation_release_anim.stop(self)
            self.elevation_release_anim.start(self)
        return super(BaseRaisedButton, self).on_touch_up(touch)

    def _get_md_bg_color_down(self):
        t = self.theme_cls
        c = self.md_bg_color  # Default to no change on touch
        # Material design specifies using darker hue when on Dark theme
        if t.theme_style == 'Dark':
            if self.md_bg_color == t.primary_color:
                c = t.primary_dark
            elif self.md_bg_color == t.accent_color:
                c = t.accent_dark
        return c

    def _get_md_bg_color_disabled(self):
        if self.theme_cls.theme_style == 'Dark':
            c = (1., 1., 1., 0.12)
        else:
            c = (0., 0., 0., 0.12)
        return c


class BaseRoundButton(CircularRippleBehavior, BaseButton):
    '''
    Abstract base class for all round buttons, bringing in the appropriate
    on-touch behavior
    '''
    pass


class BaseRectangularButton(RectangularRippleBehavior, BaseButton):
    '''
    Abstract base class for all rectangular buttons, bringing in the
    appropriate on-touch behavior. Also maintains the correct minimum width
    as stated in guidelines.
    '''
    width = BoundedNumericProperty(dp(88), min=dp(88), max=None,
                                   errorhandler=lambda x: dp(88))
    text = StringProperty('')
    _capitalized_text = StringProperty('')

    def on_text(self, instance, value):
        self._capitalized_text = value.upper()


class MDIconButton(BaseRoundButton, BaseFlatButton, BasePressedButton):
    icon = StringProperty('checkbox-blank-circle')


class MDFlatButton(BaseRectangularButton, BaseFlatButton, BasePressedButton):
    pass


class MDRaisedButton(BaseRectangularButton, RectangularElevationBehavior,
                     BaseRaisedButton, BasePressedButton):
    pass


class MDFloatingActionButton(BaseRoundButton, CircularElevationBehavior,
                             BaseRaisedButton):
    icon = StringProperty('android')
    background_palette = StringProperty('Accent')
