"""
Buttons
=======

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Buttons <https://material.io/design/components/buttons.html>`

`Material Design spec, Buttons: floating action button <https://material.io/design/components/buttons-floating-action-button.html>`

Example
-------

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.theming import ThemeManager

Builder.load_string('''
<ExampleButtons@BoxLayout>
    orientation: 'vertical'

    MDToolbar:
        id: toolbar
        title: app.title
        md_bg_color: app.theme_cls.primary_color
        background_palette: 'Primary'
        elevation: 10
        left_action_items: [['dots-vertical', lambda x: None]]

    Screen:
        ScrollView:
            size_hint_x: None
            width: box.width
            pos_hint: {'center_x': .5}
            bar_width: 0

            BoxLayout:
                id: box
                padding: dp(10)
                size_hint: None, None
                size: self.minimum_size
                spacing: dp(10)
                orientation: 'vertical'
                pos_hint: {'center_x': .5}

                BoxLayout:
                    size_hint: None, None
                    width: self.minimum_width
                    height: dp(56)
                    spacing: '10dp'

                    MDIconButton:
                        icon: 'sd'

                    MDFloatingActionButton:
                        icon: 'plus'
                        opposite_colors: True
                        elevation_normal: 8

                    MDFloatingActionButton:
                        icon: 'check'
                        opposite_colors: True
                        elevation_normal: 8
                        md_bg_color: app.theme_cls.primary_color

                    MDIconButton:
                        icon: 'sd'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color

                MDFlatButton:
                    text: 'MDFlatButton'
                    pos_hint: {'center_x': .5}

                MDRaisedButton:
                    text: "MDRaisedButton"
                    elevation_normal: 2
                    opposite_colors: True
                    pos_hint: {'center_x': .5}

                MDRectangleFlatButton:
                    text: "MDRectangleFlatButton"
                    pos_hint: {'center_x': .5}

                MDRectangleFlatIconButton:
                    text: "MDRectangleFlatIconButton"
                    icon: "language-python"
                    width: dp(230)
                    pos_hint: {'center_x': .5}

                MDRoundFlatButton:
                    text: "MDRoundFlatButton"
                    pos_hint: {'center_x': .5}

                MDRoundFlatIconButton:
                    text: "MDRoundFlatIconButton"
                    icon: "language-python"
                    width: dp(200)
                    pos_hint: {'center_x': .5}

                MDFillRoundFlatButton:
                    text: "MDFillRoundFlatButton"
                    pos_hint: {'center_x': .5}

                MDFillRoundFlatIconButton:
                    text: "MDFillRoundFlatIconButton"
                    icon: "language-python"
                    pos_hint: {'center_x': .5}

                MDTextButton:
                    text: "MDTextButton"
                    pos_hint: {'center_x': .5}

                BoxLayout:
                    orientation: 'vertical'
                    spacing: '10dp'
                    size_hint: None, None
                    size: self.minimum_size
                    pos_hint: {'center_x': .5}

                    MDSeparator:

                    Label:
                        text: 'Button customization'
                        color: app.theme_cls.text_color
                        font_size: '20sp'
                        size_hint: None, None
                        size: self.texture_size

                    MDSeparator:

                ########################################
                #         CUSTOMIZATION BUTTONS
                ########################################

                MDRaisedButton:
                    text: "MDRaisedButton"
                    elevation_normal: 2
                    opposite_colors: True
                    pos_hint: {'center_x': .5}
                    text_color: 1, 0, 0, 1

                MDRaisedButton:
                    text: "MDRaisedButton"
                    elevation_normal: 2
                    opposite_colors: True
                    pos_hint: {'center_x': .5}
                    md_bg_color: 1, 0, 0, 1

                MDRectangleFlatButton:
                    text: "MDRectangleFlatButton"
                    pos_hint: {'center_x': .5}
                    text_color: 1, 1, 0, 1

                MDRectangleFlatButton:
                    text: "MDRectangleFlatButton"
                    pos_hint: {'center_x': .5}
                    md_bg_color: 1, 0, 0, 1
                    text_color: 1, 1, 0, 1

                MDRoundFlatButton:
                    text: "MDRoundFlatButton"
                    pos_hint: {'center_x': .5}
                    md_bg_color: 1, 0, 0, 1

                MDRoundFlatButton:
                    text: "MDRoundFlatButton"
                    pos_hint: {'center_x': .5}
                    md_bg_color: 1, 0, 0, 1

                MDRoundFlatButton:
                    text: "MDRoundFlatButton"
                    pos_hint: {'center_x': .5}
                    text_color: 1, 1, 0, 1
                    md_bg_color: 1, 0, 0, 1

                MDRoundFlatIconButton:
                    text: "MDRoundFlatIconButton"
                    pos_hint: {'center_x': .5}
                    text_color: 1, 1, 0, 1
                    width: dp(210)

                MDRoundFlatIconButton:
                    text: "MDRoundFlatIconButton"
                    pos_hint: {'center_x': .5}
                    text_color: 1, 1, 0, 1
                    md_bg_color: 1, 0, 0, 1
                    width: dp(210)

                MDFillRoundFlatIconButton:
                    text: "MDFillRoundFlatIconButton"
                    icon: "language-python"
                    pos_hint: {'center_x': .5}
                    text_color: 1, 1, 0, 1

                MDFillRoundFlatIconButton:
                    text: "MDFillRoundFlatIconButton"
                    icon: "language-python"
                    pos_hint: {'center_x': .5}
                    text_color: 1, 1, 0, 1
                    md_bg_color: 1, 0, 0, 1

                BoxLayout:
                    orientation: 'vertical'
                    spacing: '10dp'
                    size_hint: None, None
                    size: self.minimum_size
                    pos_hint: {'center_x': .5}

                    MDSeparator:

                    Label:
                        text: 'MDIconButton customization'
                        color: app.theme_cls.text_color
                        font_size: '20sp'
                        size_hint: None, None
                        size: self.texture_size

                    MDSeparator:

                    BoxLayout:
                        size_hint: None, None
                        size: self.minimum_size
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MDIconButton:
                            icon: "language-python"
                            user_font_size: "15sp"

                        MDIconButton:
                            icon: "language-python"
                            user_font_size: "20sp"

                        MDIconButton:
                            icon: "language-python"
                            user_font_size: "24sp"

                        MDIconButton:
                            icon: "language-python"
                            user_font_size: "36sp"

                        MDIconButton:
                            icon: "language-python"
                            user_font_size: "48sp"
''')


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = "Example Buttons"
    main_widget = None

    def build(self):
        return Factory.ExampleButtons()


Example().run()
"""

from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.stencil_instructions import (
    StencilPush,
    StencilUse,
    StencilPop,
    StencilUnUse,
)
from kivy.graphics.vertex_instructions import Ellipse, RoundedRectangle
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.properties import (
    StringProperty,
    BoundedNumericProperty,
    ListProperty,
    AliasProperty,
    BooleanProperty,
    NumericProperty,
    OptionProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation

from kivymd.uix.behaviors.backgroundcolorbehavior import (
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    RectangularRippleBehavior,
)
from kivymd.uix.behaviors import (
    CommonElevationBehavior,
    RectangularElevationBehavior,
    CircularElevationBehavior,
)
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
#:import Animation kivy.animation.Animation
#:import md_icons kivymd.icon_definitions.md_icons
#:import colors kivymd.color_definitions.colors
#:import images_path kivymd.images_path


<BaseButton>
    size_hint: (None, None)
    anchor_x: 'center'
    anchor_y: 'center'


<BaseFlatButton>


<BaseRaisedButton>


<BaseRoundButton>
    canvas:
        Clear
        Color:
            rgba: self._current_button_color
        Ellipse:
            size: self.size
            pos: self.pos

    size:
        (dp(48), dp(48)) \
        if not root.user_font_size \
        else (dp(root.user_font_size + 23), dp(root.user_font_size + 23))
    lbl_txt: lbl_txt
    padding: dp(12)
    theme_text_color: 'Primary'

    MDIcon:
        id: lbl_txt
        icon: root.icon
        font_size:
            root.user_font_size \
            if root.user_font_size \
            else self.font_size
        theme_text_color: root.theme_text_color
        text_color: root.text_color
        disabled: root.disabled
        valign: 'middle'
        halign: 'center'
        opposite_colors: root.opposite_colors


<BaseRectangularButton>
    canvas:
        Clear
        Color:
            rgba: self._current_button_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: (root._radius, )

    lbl_txt: lbl_txt
    height: dp(36) if not root._height else root._height
    width: lbl_txt.texture_size[0] + root.increment_width
    padding: (dp(8), 0)
    theme_text_color: 'Primary' if not root.text_color else 'Custom'
    markup: False

    MDLabel:
        id: lbl_txt
        text: root.text if root.button_label else ''
        font_size: sp(root.font_size)
        can_capitalize: root.can_capitalize
        size_hint_x: None
        text_size: (None, root.height)
        height: self.texture_size[1]
        theme_text_color: root.theme_text_color
        text_color: root.text_color
        markup: root.markup
        disabled: root.disabled
        valign: 'middle'
        halign: 'center'
        opposite_colors: root.opposite_colors


<MDRoundFlatButton>
    canvas.before:
        Color:
            rgba:
                root.theme_cls.primary_color \
                if root.md_bg_color == [0.0, 0.0, 0.0, 0.0] \
                else root.md_bg_color
        Line:
            width: 1
            rounded_rectangle:
                (self.x, self.y, self.width, self.height,\
                root._radius, root._radius, root._radius, root._radius,\
                self.height)

    theme_text_color: 'Custom'
    text_color:
        root.theme_cls.primary_color \
        if not root.text_color else root.text_color


<MDFillRoundFlatButton>
    canvas.before:
        Color:
            rgba:
                root.theme_cls.primary_color \
                if root.md_bg_color == [0.0, 0.0, 0.0, 0.0] \
                else root.md_bg_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [root._radius, ]

    text_color: root.specific_text_color


<MDFillRoundFlatIconButton>
    text_color: root.specific_text_color

    BoxLayout:
        spacing: dp(10)

        MDIcon:
            id: lbl_ic
            icon: root.icon
            theme_text_color: 'Custom'
            text_color:
                root.specific_text_color \
                if root.text_color == root.theme_cls.primary_color \
                else root.text_color
            size_hint_x: None
            #width: self.texture_size[0]


<MDRectangleFlatButton>
    canvas.before:
        Color:
            rgba:
                root.theme_cls.primary_color \
                if not root.text_color else root.text_color
        Line:
            width: 1
            rectangle: (self.x, self.y, self.width, self.height)

    theme_text_color: 'Custom'
    text_color:
        root.theme_cls.primary_color \
        if not root.text_color else root.text_color


<MDRectangleFlatIconButton>
    canvas.before:
        Color:
            rgba:
                root.theme_cls.primary_color \
                if not root.text_color else root.text_color
        Line:
            width: 1
            rectangle: (self.x, self.y, self.width, self.height)

    size_hint_x: None
    width: dp(150)
    markup: False

    BoxLayout:
        spacing: dp(10)

        MDIcon:
            id: lbl_ic
            icon: root.icon
            theme_text_color: 'Custom'
            text_color:
                root.theme_cls.primary_color \
                if not root.text_color else root.text_color
            size_hint_x: None
            width: self.texture_size[0]

        MDLabel:
            id: lbl_txt
            text: root.text
            on_text: print(root.text_color)
            font_size: sp(root.font_size)
            can_capitalize: root.can_capitalize
            shorten: True
            theme_text_color: 'Custom'
            text_color:
                root.theme_cls.primary_color \
                if not root.text_color else root.text_color
            markup: root.markup


<MDRoundFlatIconButton>
    size_hint_x: None
    width: dp(150)
    markup: False

    BoxLayout:
        spacing: dp(10)

        MDIcon:
            id: lbl_ic
            icon: root.icon
            theme_text_color: 'Custom'
            text_color:
                root.theme_cls.primary_color \
                if not root.text_color else root.text_color
            size_hint_x: None
            width: self.texture_size[0]

        MDLabel:
            id: lbl_txt
            text: root.text
            font_size: sp(root.font_size)
            can_capitalize: root.can_capitalize
            shorten: True
            theme_text_color: 'Custom'
            text_color:
                root.theme_cls.primary_color \
                if not root.text_color else root.text_color
            markup: root.markup


<MDRaisedButton>
    md_bg_color: root.theme_cls.primary_color
    theme_text_color: 'Custom'
    text_color: root.specific_text_color


<MDFloatingActionButton>
    # Defaults to 56-by-56 and a background of the accent color according to
    # guidelines
    size: (dp(56), dp(56))
    md_bg_color: root.theme_cls.accent_color
    theme_text_color: 'Custom'
    text_color: root.specific_text_color


<MDTextButton>
    size_hint: None, None
    size: self.texture_size
    color:
        root.theme_cls.primary_color \
        if not len(root.custom_color) else root.custom_color
    background_down: f'{images_path}transparent.png'
    background_normal: f'{images_path}transparent.png'
    opacity: 1
"""
)


class BaseButton(
    ThemableBehavior,
    ButtonBehavior,
    SpecificBackgroundColorBehavior,
    AnchorLayout,
):
    """
    Abstract base class for all MD buttons. This class handles the button's
    colors (disabled/down colors handled in children classes as those depend on
    type of button) as well as the disabled state.
    """

    _md_bg_color_down = ListProperty(None, allownone=True)
    _md_bg_color_disabled = ListProperty(None, allownone=True)
    _current_button_color = ListProperty([0.0, 0.0, 0.0, 0.0])
    theme_text_color = OptionProperty(
        None,
        allownone=True,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
        ],
    )
    text_color = ListProperty(None, allownone=True)
    opposite_colors = BooleanProperty(False)
    font_name = StringProperty()
    font_size = NumericProperty(14)
    user_font_size = NumericProperty()
    """Custom font size."""

    def on_font_name(self, instance, value):
        instance.ids.lbl_txt.font_name = value

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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

    md_bg_color_down = AliasProperty(
        _call_get_bg_color_down, _set_md_bg_color_down
    )

    def _call_get_bg_color_disabled(self):
        return self._get_md_bg_color_disabled()

    def _get_md_bg_color_disabled(self):
        if self._md_bg_color_disabled:
            return self._md_bg_color_disabled
        else:
            raise NotImplementedError

    def _set_md_bg_color_disabled(self, value):
        self._md_bg_color_disabled = value

    md_bg_color_disabled = AliasProperty(
        _call_get_bg_color_disabled, _set_md_bg_color_disabled
    )

    def on_disabled(self, instance, value):
        if self.disabled:
            self._current_button_color = self.md_bg_color_disabled
        else:
            self._current_button_color = self.md_bg_color


class BasePressedButton(BaseButton):
    """
    Abstract base class for those button which fade to a background color on
    press.
    """

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
            self.fade_bg = Animation(
                duration=0.5, _current_button_color=self.md_bg_color_down
            )
            self.fade_bg.start(self)
            return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            self.fade_bg.stop_property(self, "_current_button_color")
            Animation(
                duration=0.05, _current_button_color=self.md_bg_color
            ).start(self)
        return super().on_touch_up(touch)


class BaseFlatButton(BaseButton):
    """
    Abstract base class for flat buttons which do not elevate from material.

    Enforces the recommended down/disabled colors for flat buttons
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = (0.0, 0.0, 0.0, 0.0)

    def _get_md_bg_color_down(self):
        if self.theme_cls.theme_style == "Dark":
            c = get_color_from_hex("cccccc")
            c[3] = 0.25
        else:
            c = get_color_from_hex("999999")
            c[3] = 0.4
        return c

    def _get_md_bg_color_disabled(self):
        bg_c = self.md_bg_color
        if bg_c[3] == 0:  # transparent background
            c = bg_c
        else:
            if self.theme_cls.theme_style == "Dark":
                c = (1.0, 1.0, 1.0, 0.12)
            else:
                c = (0.0, 0.0, 0.0, 0.12)
        return c


class BaseRaisedButton(CommonElevationBehavior, BaseButton):
    """
    Abstract base class for raised buttons which elevate from material.
    Raised buttons are to be used sparingly to emphasise primary/important
    actions.

    Implements elevation behavior as well as the recommended down/disabled
    colors for raised buttons.
    """

    def __init__(self, **kwargs):
        if self.elevation_raised == 0 and self.elevation_normal + 6 <= 12:
            self.elevation_raised = self.elevation_normal + 6
        elif self.elevation_raised == 0:
            self.elevation_raised = 12
        super().__init__(**kwargs)
        self.elevation_press_anim = Animation(
            elevation=self.elevation_raised, duration=0.2, t="out_quad"
        )
        self.elevation_release_anim = Animation(
            elevation=self.elevation_normal, duration=0.2, t="out_quad"
        )

    _elev_norm = NumericProperty(2)

    def _get_elev_norm(self):
        return self._elev_norm

    def _set_elev_norm(self, value):
        self._elev_norm = value if value <= 12 else 12
        self._elev_raised = (value + 6) if value + 6 <= 12 else 12
        self.elevation = self._elev_norm
        self.elevation_release_anim = Animation(
            elevation=value, duration=0.2, t="out_quad"
        )

    elevation_normal = AliasProperty(
        _get_elev_norm, _set_elev_norm, bind=("_elev_norm",)
    )
    _elev_raised = NumericProperty(8)

    def _get_elev_raised(self):
        return self._elev_raised

    def _set_elev_raised(self, value):
        self._elev_raised = value if value + self._elev_norm <= 12 else 12
        self.elevation_press_anim = Animation(
            elevation=value, duration=0.2, t="out_quad"
        )

    elevation_raised = AliasProperty(
        _get_elev_raised, _set_elev_raised, bind=("_elev_raised",)
    )

    def on_disabled(self, instance, value):
        if self.disabled:
            self.elevation = 0
        else:
            self.elevation = self.elevation_normal
        super().on_disabled(instance, value)

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
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if not self.disabled:
            if touch.grab_current is not self:
                return super().on_touch_up(touch)
            self.elevation_release_anim.stop(self)
            self.elevation_release_anim.start(self)
        return super().on_touch_up(touch)

    def _get_md_bg_color_down(self):
        t = self.theme_cls
        c = self.md_bg_color  # Default to no change on touch
        # Material design specifies using darker hue when on Dark theme
        if t.theme_style == "Dark":
            if self.md_bg_color == t.primary_color:
                c = t.primary_dark
            elif self.md_bg_color == t.accent_color:
                c = t.accent_dark
        return c

    def _get_md_bg_color_disabled(self):
        if self.theme_cls.theme_style == "Dark":
            c = (1.0, 1.0, 1.0, 0.12)
        else:
            c = (0.0, 0.0, 0.0, 0.12)
        return c


class BaseRoundButton(CircularRippleBehavior, BaseButton):
    """
    Abstract base class for all round buttons, bringing in the appropriate
    on-touch behavior
    """

    pass


class BaseRectangularButton(RectangularRippleBehavior, BaseButton):
    """
    Abstract base class for all rectangular buttons, bringing in the
    appropriate on-touch behavior. Also maintains the correct minimum width
    as stated in guidelines.
    """

    width = BoundedNumericProperty(
        dp(88), min=dp(88), max=None, errorhandler=lambda x: dp(88)
    )
    text = StringProperty("")
    increment_width = NumericProperty(dp(32))
    _radius = NumericProperty(dp(2))
    _height = NumericProperty(dp(0))
    button_label = BooleanProperty(True)
    can_capitalize = BooleanProperty(True)


class MDIconButton(BaseRoundButton, BaseFlatButton, BasePressedButton):
    icon = StringProperty("checkbox-blank-circle")
    """Button icon."""


class MDFlatButton(BaseRectangularButton, BaseFlatButton, BasePressedButton):
    pass


class BaseFlatIconButton(MDFlatButton):
    icon = StringProperty("android")
    text = StringProperty("")
    button_label = BooleanProperty(False)


class MDRaisedButton(
    BaseRectangularButton,
    RectangularElevationBehavior,
    BaseRaisedButton,
    BasePressedButton,
):
    pass


class MDFloatingActionButton(
    BaseRoundButton, CircularElevationBehavior, BaseRaisedButton
):
    icon = StringProperty("android")
    background_palette = StringProperty("Accent")


class MDRectangleFlatButton(MDFlatButton):
    pass


class MDRoundFlatButton(MDFlatButton):
    _radius = NumericProperty(dp(18))

    def lay_canvas_instructions(self):
        with self.canvas.after:
            StencilPush()
            RoundedRectangle(
                size=self.size, pos=self.pos, radius=[self._radius]
            )
            StencilUse()
            self.col_instruction = Color(rgba=self.ripple_color)
            self.ellipse = Ellipse(
                size=(self.ripple_rad, self.ripple_rad),
                pos=(
                    self.ripple_pos[0] - self.ripple_rad / 2.0,
                    self.ripple_pos[1] - self.ripple_rad / 2.0,
                ),
            )
            StencilUnUse()
            RoundedRectangle(
                size=self.size, pos=self.pos, radius=[self._radius]
            )
            StencilPop()
        self.bind(ripple_color=self._set_color, ripple_rad=self._set_ellipse)


class MDTextButton(ThemableBehavior, Button):
    custom_color = ListProperty()
    """Custom user button color"""

    def animation_label(self):
        def set_default_state_label(*args):
            Animation(opacity=1, d=0.1, t="in_out_cubic").start(self)

        anim = Animation(opacity=0.5, d=0.2, t="in_out_cubic")
        anim.bind(on_complete=set_default_state_label)
        anim.start(self)

    def on_press(self, *args):
        self.animation_label()
        return super().on_press(*args)


class MDCustomRoundIconButton(CircularRippleBehavior, ButtonBehavior, Image):
    pass


class MDFillRoundFlatButton(MDRoundFlatButton):
    pass


class MDRectangleFlatIconButton(BaseFlatIconButton):
    pass


class MDRoundFlatIconButton(MDRoundFlatButton, BaseFlatIconButton):
    pass


class MDFillRoundFlatIconButton(MDFillRoundFlatButton):
    icon = StringProperty("android")
    increment_width = dp(80)
