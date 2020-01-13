"""
Text Fields
===========

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Text fields <https://material.io/design/components/text-fields.html>`_

Example
-------

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.theming import ThemeManager

Builder.load_string('''
#:import Window kivy.core.window.Window

#:set color_shadow [0, 0, 0, .2980392156862745]


<MyMDTextFieldRound@MDTextFieldRound>
    size_hint_x: None
    normal_color: color_shadow
    active_color: color_shadow


<TextFields@Screen>
    name: 'textfields'

    canvas:
        Color:
            rgba: 0, 0, 0, .2
        Rectangle:
            pos: self.pos
            size: self.size

    ScrollView:

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            padding: dp(48)
            spacing: dp(15)

            MyMDTextFieldRound:
                hint_text: 'Empty field'

            MyMDTextFieldRound:
                icon_left: 'email'
                hint_text: 'Field with left icon'

            MyMDTextFieldRound:
                icon_left: 'key-variant'
                icon_right: 'eye-off'
                hint_text: 'Field with left and right icons'

            MDTextField:
                hint_text: 'mode = "rectangle"'
                mode: "rectangle"

            MDTextField:
                input_filter: "int"
                hint_text: "Numeric field"

            MDTextField:
                hint_text: "No helper text"

            MDTextField:
                hint_text: "Helper text on focus"
                helper_text: "This will disappear when you click off"
                helper_text_mode: "on_focus"

            MDTextField:
                hint_text: "Persistent helper text"
                helper_text: "Text is always here"
                helper_text_mode: "persistent"

            Widget:
                size_hint_y: None
                height: dp(5)

            MDTextField:
                id: text_field_error
                hint_text: "Helper text on error (Hit Enter with  two characters here)"
                helper_text: "Two is my least favorite number"
                helper_text_mode: "on_error"

            MDTextField:
                hint_text: "Max text length = 10"
                max_text_length: 10

            MDTextField:
                hint_text: "required = True"
                required: True
                helper_text_mode: "on_error"

            MDTextField:
                multiline: True
                hint_text: "Multi-line text"
                helper_text: "Messages are also supported here"
                helper_text_mode: "persistent"

            MDTextField:
                hint_text: "color_mode = \'accent\'"
                color_mode: 'accent'

            MDTextField:
                hint_text: "color_mode = \'custom\'"
                color_mode: 'custom'
                helper_text_mode: "on_focus"
                helper_text: "Color is defined by \'line_color_focus\' property"
                line_color_focus: self.theme_cls.opposite_bg_normal

            MDTextField:
                hint_text: "disabled = True"
                disabled: True

            MDTextFieldRect:
                size_hint: None, None
                size: Window.width - dp(40), dp(30)
                pos_hint: {'center_y': .5, 'center_x': .5}
''')


class Example(MDApp):
    title = "Example Text Fields"
    main_widget = None

    def build(self):
        return Factory.TextFields()

    def show_password(self, field, button):
        '''
        Called when you press the right button in the password field
        for the screen TextFields.

        instance_field: kivy.uix.textinput.TextInput;
        instance_button: kivymd.button.MDIconButton;

        '''

        # Show or hide text of password, set focus field
        # and set icon of right button.
        field.password = not field.password
        field.focus = True
        button.icon = "eye" if button.icon == "eye-off" else "eye-off"


Example().run()
"""

import sys

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.graphics.context_instructions import Color
from kivy.lang import Builder
from kivy.properties import (
    NumericProperty,
    StringProperty,
    BooleanProperty,
    OptionProperty,
    ListProperty,
    ObjectProperty,
)
from kivy.metrics import dp
from kivy.metrics import sp

from kivymd.font_definitions import theme_font_styles
from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDIcon

Builder.load_string(
    """
#:import images_path kivymd.images_path


<MDTextField>

    canvas.before:
        Clear
        Color:
            rgba: self.line_color_normal if root.mode == "line" else [0, 0, 0, 0]
        Line:
            points:
                self.x, self.y + dp(16), self.x + self.width, self.y + dp(16)
            width: 1
            dash_length: dp(3)
            dash_offset: 2 if self.disabled else 0

        Color:
            rgba: self._current_line_color if root.mode == "line" else [0, 0, 0, 0]
        Rectangle:
            size: self._line_width, dp(2)
            pos: self.center_x - (self._line_width / 2), self.y + dp(16)

        Color:
            rgba: self._current_error_color
        Rectangle:
            texture: self._msg_lbl.texture
            size: self._msg_lbl.texture_size
            pos: self.x, self.y

        Color:
            rgba: self._current_right_lbl_color
        Rectangle:
            texture: self._right_msg_lbl.texture
            size: self._right_msg_lbl.texture_size
            pos: self.width-self._right_msg_lbl.texture_size[0]+dp(45), self.y

        Color:
            rgba:
                (self._current_line_color if self.focus and not \
                self._cursor_blink else (0, 0, 0, 0))
        Rectangle:
            pos: [int(x) for x in self.cursor_pos]
            size: 1, -self.line_height

        Color:
            rgba: self._current_hint_text_color
        Rectangle:
            texture: self._hint_lbl.texture
            size: self._hint_lbl.texture_size
            pos: self.x, self.y + self.height - self._hint_y

        Color:
            rgba:
                self.disabled_foreground_color if self.disabled else\
                (self.hint_text_color if not self.text and not\
                self.focus else self.foreground_color)

        Color:
            rgba: self._current_line_color
        Line:
            width: dp(1) if root.mode == "rectangle" else dp(0.00001)
            points:
                (
                self.x + root._line_blank_space_right_hint_text, self.top - self._hint_lbl.texture_size[1] // 2,
                self.right + dp(12), self.top - self._hint_lbl.texture_size[1] // 2,
                self.right + dp(12), self.y,
                self.x - dp(12), self.y,
                self.x - dp(12), self.top - self._hint_lbl.texture_size[1] // 2,
                self.x + root._line_blank_space_left_hint_text, self.top - self._hint_lbl.texture_size[1] // 2
                )

    font_name: 'Roboto'
    foreground_color: app.theme_cls.text_color
    font_size: sp(16)
    bold: False
    padding: 0, dp(16), 0, dp(10)
    multiline: False
    size_hint_y: None
    height: self.minimum_height + dp(8)


<TextfieldLabel>
    size_hint_x: None
    width: self.texture_size[0]
    shorten: True
    shorten_from: "right"


<MDTextFieldRect>
    on_focus:
        root.anim_rect([root.x, root.y, root.right, root.y, root.right,\
        root.top, root.x, root.top, root.x, root.y], 1) if root.focus\
        else root.anim_rect([root.x - dp(60), root.y - dp(60),\
        root.right + dp(60), root.y - dp(60),
        root.right + dp(60), root.top + dp(60),\
        root.x - dp(60), root.top + dp(60),\
        root.x - dp(60), root.y - dp(60)], 0)

    canvas.after:
        Color:
            rgba: root._primary_color
        Line:
            width: dp(1.5)
            points:
                (
                self.x - dp(60), self.y - dp(60),
                self.right + dp(60), self.y - dp(60),
                self.right + dp(60), self.top + dp(60),
                self.x - dp(60), self.top + dp(60),
                self.x - dp(60), self.y - dp(60)
                )


<MDTextFieldRound>:
    multiline: False
    size_hint: 1, None
    height: self.line_height + dp(10)
    background_active: f'{images_path}transparent.png'
    background_normal: f'{images_path}transparent.png'
    padding:
        self._lbl_icon_left.texture_size[1] + dp(10) if self.icon_left else dp(15), \
        (self.height / 2) - (self.line_height / 2), \
        self._lbl_icon_right.texture_size[1] + dp(20) if self.icon_right else dp(15), \
        0

    canvas.before:
        Color:
            rgba: self.normal_color if not self.focus else self._color_active
        Ellipse:
            angle_start: 180
            angle_end: 360
            pos: self.pos[0] - self.size[1] / 2, self.pos[1]
            size: self.size[1], self.size[1]
        Ellipse:
            angle_start: 360
            angle_end: 540
            pos: self.size[0] + self.pos[0] - self.size[1]/2.0, self.pos[1]
            size: self.size[1], self.size[1]
        Rectangle:
            pos: self.pos
            size: self.size

        Color:
            rgba: self.line_color
        Line:
            points: self.pos[0] , self.pos[1], self.pos[0] + self.size[0], self.pos[1]
        Line:
            points: self.pos[0], self.pos[1] + self.size[1], self.pos[0] + self.size[0], self.pos[1] + self.size[1]
        Line:
            ellipse: self.pos[0] - self.size[1] / 2, self.pos[1], self.size[1], self.size[1], 180, 360
        Line:
            ellipse: self.size[0] + self.pos[0] - self.size[1] / 2.0, self.pos[1], self.size[1], self.size[1], 360, 540

        # Texture of left Icon.
        Color:
            rgba: self.icon_left_color
        Rectangle:
            texture: self._lbl_icon_left.texture
            size:
                self._lbl_icon_left.texture_size if self.icon_left \
                else (0, 0)
            pos:
                self.x, \
                self.center[1] - self._lbl_icon_right.texture_size[1] / 2

        # Texture of right Icon.
        Color:
            rgba: self.icon_right_color
        Rectangle:
            texture: self._lbl_icon_right.texture
            size:
                self._lbl_icon_right.texture_size if self.icon_right \
                else (0, 0)
            pos:
                (self.width + self.x) - (self._lbl_icon_right.texture_size[1]), \
                self.center[1] - self._lbl_icon_right.texture_size[1] / 2

        Color:
            rgba:
                root.theme_cls.disabled_hint_text_color if not self.focus \
                else root.foreground_color
"""
)


class MDTextFieldRect(ThemableBehavior, TextInput):
    _primary_color = ListProperty([0, 0, 0, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._update_primary_color()
        self.theme_cls.bind(primary_color=self._update_primary_color)
        self.root_color = Color()

    def _update_primary_color(self, *args):
        self._primary_color = self.theme_cls.primary_color
        self._primary_color[3] = 0

    def anim_rect(self, points, alpha):
        instance_line = self.canvas.children[-1].children[-1]
        instance_color = self.canvas.children[-1].children[0]
        if alpha == 1:
            d_line = 0.3
            d_color = 0.4
        else:
            d_line = 0.05
            d_color = 0.05

        Animation(points=points, d=d_line, t="out_cubic").start(instance_line)
        Animation(a=alpha, d=d_color).start(instance_color)


class FixedHintTextInput(TextInput):
    hint_text = StringProperty("")

    def on__hint_text(self, instance, value):
        pass

    def _refresh_hint_text(self):
        pass


class TextfieldLabel(ThemableBehavior, Label):
    field = ObjectProperty()
    font_style = OptionProperty("Body1", options=theme_font_styles)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = sp(self.theme_cls.font_styles[self.font_style][1])


class MDTextField(ThemableBehavior, FixedHintTextInput):
    # TODO: Add class fields description.
    helper_text = StringProperty("This field is required")

    helper_text_mode = OptionProperty(
        "none", options=["none", "on_error", "persistent", "on_focus"]
    )

    max_text_length = NumericProperty(None)

    required = BooleanProperty(False)

    color_mode = OptionProperty(
        "primary", options=["primary", "accent", "custom"]
    )

    mode = OptionProperty("line", options=["rectangle"])

    line_color_normal = ListProperty()

    line_color_focus = ListProperty()

    error_color = ListProperty()

    error = BooleanProperty(False)

    _text_len_error = BooleanProperty(False)
    _hint_lbl_font_size = NumericProperty(sp(16))
    _line_blank_space_right_hint_text = NumericProperty(0)
    _line_blank_space_left_hint_text = NumericProperty(0)
    _hint_y = NumericProperty(dp(38))
    _line_width = NumericProperty(0)
    _current_line_color = ListProperty([0.0, 0.0, 0.0, 0.0])
    _current_error_color = ListProperty([0.0, 0.0, 0.0, 0.0])
    _current_hint_text_color = ListProperty([0.0, 0.0, 0.0, 0.0])
    _current_right_lbl_color = ListProperty([0.0, 0.0, 0.0, 0.0])

    def __init__(self, **kwargs):
        self._msg_lbl = TextfieldLabel(
            font_style="Caption",
            halign="left",
            valign="middle",
            text=self.helper_text,
            field=self,
        )
        self._right_msg_lbl = TextfieldLabel(
            font_style="Caption",
            halign="right",
            valign="middle",
            text="",
            field=self,
        )
        self._hint_lbl = TextfieldLabel(
            font_style="Subtitle1", halign="left", valign="middle", field=self
        )
        super().__init__(**kwargs)
        self.line_color_normal = self.theme_cls.divider_color
        self.line_color_focus = self.theme_cls.primary_color
        self.error_color = self.theme_cls.error_color

        self._current_hint_text_color = self.theme_cls.disabled_hint_text_color
        self._current_line_color = self.theme_cls.primary_color

        self.bind(
            helper_text=self._set_msg,
            hint_text=self._set_hint,
            _hint_lbl_font_size=self._hint_lbl.setter("font_size"),
            helper_text_mode=self._set_message_mode,
            max_text_length=self._set_max_text_length,
            text=self.on_text,
        )
        self.theme_cls.bind(
            primary_color=self._update_primary_color,
            theme_style=self._update_theme_style,
            accent_color=self._update_accent_color,
        )
        self.has_had_text = False

    def _update_colors(self, color):
        self.line_color_focus = color
        if not self.error and not self._text_len_error:
            self._current_line_color = color
            if self.focus:
                self._current_line_color = color

    def _update_accent_color(self, *args):
        if self.color_mode == "accent":
            self._update_colors(self.theme_cls.accent_color)

    def _update_primary_color(self, *args):
        if self.color_mode == "primary":
            self._update_colors(self.theme_cls.primary_color)

    def _update_theme_style(self, *args):
        self.line_color_normal = self.theme_cls.divider_color
        if not any([self.error, self._text_len_error]):
            if not self.focus:
                self._current_hint_text_color = (
                    self.theme_cls.disabled_hint_text_color
                )
                self._current_right_lbl_color = (
                    self.theme_cls.disabled_hint_text_color
                )
                if self.helper_text_mode == "persistent":
                    self._current_error_color = (
                        self.theme_cls.disabled_hint_text_color
                    )

    def on_width(self, instance, width):
        if (
            any([self.focus, self.error, self._text_len_error])
            and instance is not None
        ):
            self._line_width = width
        self._msg_lbl.width = self.width
        self._right_msg_lbl.width = self.width

    def on_focus(self, *args):
        disabled_hint_text_color = self.theme_cls.disabled_hint_text_color
        Animation.cancel_all(
            self, "_line_width", "_hint_y", "_hint_lbl_font_size"
        )
        if self.max_text_length is None:
            max_text_length = sys.maxsize
        else:
            max_text_length = self.max_text_length
        if len(self.text) > max_text_length or all(
            [self.required, len(self.text) == 0, self.has_had_text]
        ):
            self._text_len_error = True
        if self.error or all(
            [
                self.max_text_length is not None
                and len(self.text) > self.max_text_length
            ]
        ):
            has_error = True
        else:
            if all([self.required, len(self.text) == 0, self.has_had_text]):
                has_error = True
            else:
                has_error = False

        if self.focus:
            if not self._line_blank_space_right_hint_text:
                self._line_blank_space_right_hint_text = self._hint_lbl.texture_size[
                    0
                ] - dp(
                    25
                )
            Animation(
                _line_blank_space_right_hint_text=self._line_blank_space_right_hint_text,
                _line_blank_space_left_hint_text=self._hint_lbl.x - dp(5),
                _current_hint_text_color=self.line_color_focus,
                duration=0.2,
                t="out_quad",
            ).start(self)
            self.has_had_text = True
            Animation.cancel_all(
                self, "_line_width", "_hint_y", "_hint_lbl_font_size"
            )
            if not self.text:
                Animation(
                    _hint_y=dp(14),
                    _hint_lbl_font_size=sp(12),
                    duration=0.2,
                    t="out_quad",
                ).start(self)
            Animation(_line_width=self.width, duration=0.2, t="out_quad").start(
                self
            )
            if has_error:
                Animation(
                    duration=0.2,
                    _current_hint_text_color=self.error_color,
                    _current_right_lbl_color=self.error_color,
                    _current_line_color=self.error_color,
                ).start(self)
                if self.helper_text_mode == "on_error" and (
                    self.error or self._text_len_error
                ):
                    Animation(
                        duration=0.2, _current_error_color=self.error_color
                    ).start(self)
                elif (
                    self.helper_text_mode == "on_error"
                    and not self.error
                    and not self._text_len_error
                ):
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
                elif self.helper_text_mode == "persistent":
                    Animation(
                        duration=0.2,
                        _current_error_color=disabled_hint_text_color,
                    ).start(self)
                elif self.helper_text_mode == "on_focus":
                    Animation(
                        duration=0.2,
                        _current_error_color=disabled_hint_text_color,
                    ).start(self)
            else:
                Animation(
                    duration=0.2,
                    _current_right_lbl_color=disabled_hint_text_color,
                ).start(self)
                Animation(duration=0.2, color=self.line_color_focus).start(
                    self._hint_lbl
                )
                if self.helper_text_mode == "on_error":
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
                if self.helper_text_mode == "persistent":
                    Animation(
                        duration=0.2,
                        _current_error_color=disabled_hint_text_color,
                    ).start(self)
                elif self.helper_text_mode == "on_focus":
                    Animation(
                        duration=0.2,
                        _current_error_color=disabled_hint_text_color,
                    ).start(self)
        else:
            if not self.text:
                Animation(
                    _hint_y=dp(38),
                    _hint_lbl_font_size=sp(16),
                    duration=0.2,
                    t="out_quad",
                ).start(self)
                Animation(
                    _line_blank_space_right_hint_text=0,
                    _line_blank_space_left_hint_text=0,
                    duration=0.2,
                    t="out_quad",
                ).start(self)
            if has_error:
                Animation(
                    duration=0.2,
                    _current_line_color=self.error_color,
                    _current_hint_text_color=self.error_color,
                    _current_right_lbl_color=self.error_color,
                ).start(self)
                if self.helper_text_mode == "on_error" and (
                    self.error or self._text_len_error
                ):
                    Animation(
                        duration=0.2, _current_error_color=self.error_color
                    ).start(self)
                elif (
                    self.helper_text_mode == "on_error"
                    and not self.error
                    and not self._text_len_error
                ):
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
                elif self.helper_text_mode == "persistent":
                    Animation(
                        duration=0.2,
                        _current_error_color=disabled_hint_text_color,
                    ).start(self)
                elif self.helper_text_mode == "on_focus":
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
            else:
                Animation(duration=0.2, color=(1, 1, 1, 1)).start(
                    self._hint_lbl
                )
                Animation(
                    duration=0.2,
                    _current_line_color=self.line_color_focus,
                    _current_hint_text_color=disabled_hint_text_color,
                    _current_right_lbl_color=(0, 0, 0, 0),
                ).start(self)
                if self.helper_text_mode == "on_error":
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
                elif self.helper_text_mode == "persistent":
                    Animation(
                        duration=0.2,
                        _current_error_color=disabled_hint_text_color,
                    ).start(self)
                elif self.helper_text_mode == "on_focus":
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
                Animation(_line_width=0, duration=0.2, t="out_quad").start(self)

    def on_text(self, instance, text):
        if len(text) > 0:
            self.has_had_text = True
        if self.max_text_length is not None:
            self._right_msg_lbl.text = f"{len(text)}/{self.max_text_length}"
            max_text_length = self.max_text_length
        else:
            max_text_length = sys.maxsize
        if len(text) > max_text_length or all(
            [self.required, len(self.text) == 0, self.has_had_text]
        ):
            self._text_len_error = True
        else:
            self._text_len_error = False
        if self.error or self._text_len_error:
            if self.focus:
                Animation(
                    duration=0.2,
                    _current_hint_text_color=self.error_color,
                    _current_line_color=self.error_color,
                ).start(self)
                if self.helper_text_mode == "on_error" and (
                    self.error or self._text_len_error
                ):
                    Animation(
                        duration=0.2, _current_error_color=self.error_color
                    ).start(self)
                if self._text_len_error:
                    Animation(
                        duration=0.2, _current_right_lbl_color=self.error_color
                    ).start(self)
        else:
            if self.focus:
                disabled_hint_text_color = (
                    self.theme_cls.disabled_hint_text_color
                )
                Animation(
                    duration=0.2,
                    _current_right_lbl_color=disabled_hint_text_color,
                ).start(self)
                Animation(
                    duration=0.2,
                    _current_hint_text_color=self.line_color_focus,
                    _current_line_color=self.line_color_focus,
                ).start(self)
                if self.helper_text_mode == "on_error":
                    Animation(
                        duration=0.2, _current_error_color=(0, 0, 0, 0)
                    ).start(self)
        if len(self.text) != 0 and not self.focus:
            self._hint_y = dp(14)
            self._hint_lbl_font_size = sp(12)

    def on_text_validate(self):
        self.has_had_text = True
        if self.max_text_length is None:
            max_text_length = sys.maxsize
        else:
            max_text_length = self.max_text_length
        if len(self.text) > max_text_length or all(
            [self.required, len(self.text) == 0, self.has_had_text]
        ):
            self._text_len_error = True

    def _set_hint(self, instance, text):
        self._hint_lbl.text = text

    def _set_msg(self, instance, text):
        self._msg_lbl.text = text
        self.helper_text = text

    def _set_message_mode(self, instance, text):
        self.helper_text_mode = text
        if self.helper_text_mode == "persistent":
            disabled_hint_text_color = self.theme_cls.disabled_hint_text_color
            Animation(
                duration=0.1, _current_error_color=disabled_hint_text_color
            ).start(self)

    def _set_max_text_length(self, instance, length):
        self.max_text_length = length
        self._right_msg_lbl.text = f"{len(self.text)}/{length}"

    def on_color_mode(self, instance, mode):
        if mode == "primary":
            self._update_primary_color()
        elif mode == "accent":
            self._update_accent_color()
        elif mode == "custom":
            self._update_colors(self.line_color_focus)

    def on_line_color_focus(self, *args):
        if self.color_mode == "custom":
            self._update_colors(self.line_color_focus)


class MDTextFieldRound(ThemableBehavior, TextInput):
    icon_left = StringProperty()
    """Left icon."""

    icon_left_color = ListProperty([0, 0, 0, 1])
    """Color of left icon."""

    icon_right = StringProperty()
    """Right icon."""

    icon_right_color = ListProperty([0, 0, 0, 1])
    """Color of right icon."""

    line_color = ListProperty()
    """Field line color."""

    normal_color = ListProperty()
    """Field color if `focus` is `False`."""

    color_active = ListProperty()
    """Field color if `focus` is `True`."""

    _color_active = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._lbl_icon_left = MDIcon(theme_text_color="Custom")
        self._lbl_icon_right = MDIcon(theme_text_color="Custom")
        self.cursor_color = self.theme_cls.primary_color

        if not self.normal_color:
            self.normal_color = self.theme_cls.primary_light
        if not self.line_color:
            self.line_color = self.theme_cls.primary_dark
        if not self.color_active:
            self._color_active = [0, 0, 0, 0.5]

    def on_focus(self, instance, value):
        if value:
            self.icon_left_color = self.theme_cls.primary_color
            self.icon_right_color = self.theme_cls.primary_color
        else:
            self.icon_left_color = self.theme_cls.text_color
            self.icon_right_color = self.theme_cls.text_color

    def on_icon_left(self, instance, value):
        self._lbl_icon_left.icon = value

    def on_icon_left_color(self, instance, value):
        self._lbl_icon_left.text_color = value

    def on_icon_right(self, instance, value):
        self._lbl_icon_right.icon = value

    def on_icon_right_color(self, instance, value):
        self._lbl_icon_right.text_color = value

    def on_color_active(self, instance, value):
        if value != [0, 0, 0, 0.5]:
            self._color_active = value
            self._color_active[-1] = 0.5
        else:
            self._color_active = value
