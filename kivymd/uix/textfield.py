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

from kivy.app import App
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
                icon_type: 'without'
                hint_text: 'Field with `normal_color`'
                normal_color: [.432, .124, .8654, .1]

            MyMDTextFieldRound:
                icon_type: 'without'
                hint_text: 'Field without icon'

            MyMDTextFieldRound:
                icon_type: 'without'
                hint_text: 'Field with `require_text_error`'
                require_text_error: 'Field must be not empty!'

            MyMDTextFieldRound:
                icon_left: 'email'
                icon_type: 'left'
                hint_text: 'Field with left icon'

            MyMDTextFieldRound:
                icon_left: 'email'
                icon_right: 'account-box'
                icon_right_dasabled: True
                hint_text: 'Field with left and right disabled icons'

            MyMDTextFieldRound:
                icon_type: 'all'
                icon_left: 'key-variant'
                icon_right: 'eye-off'
                icon_right_dasabled: False
                icon_callback: app.show_password
                password: True
                hint_text: 'Field width type `password = True`'

            MyMDTextFieldRound:
                icon_left: 'email'
                icon_right: 'account-box'
                icon_right_dasabled: True
                field_height: dp(30)
                hint_text: 'Field with custom size icon'
                icon_size: "18sp"
                radius: dp(9)

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

            Widget:
                size_hint_y: None
                height: dp(5)

            MDTextFieldClear:
                hint_text: "Text field with clearing type"
''')


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    theme_cls.theme_style = "Dark"
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

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.graphics.context_instructions import Color
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
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
from kivy.uix.widget import Widget

from kivymd.font_definitions import theme_font_styles
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
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
    #disabled_color: self.theme_cls.disabled_hint_text_color
    size_hint_x: None
    width: self.texture_size[0]
    shorten: True
    shorten_from: "right"
    color: 0, 0, 0, 1


<MDTextFieldClear>
    size_hint_y: None
    height: self.minimum_height

    FloatLayout:

        MDTextField:
            id: field
            text: root.text
            password: root.password
            password_mask: root.password_mask
            pos_hint: {'center_x': .5}
            padding: 0, clear_btn.width + dp(15)
            hint_text: root.hint_text
            on_focus:
                clear_btn.custom_color = self.line_color_focus\
                if clear_btn.custom_color != self.line_color_focus\
                else self.line_color_normal
            on_text:
                root.text = self.text

        MDTextButton:
            id: clear_btn
            text: 'X'
            pos_hint: {'right': 1, 'top': .1}
            custom_color: field.line_color_normal
            on_press: root.refresh_field(field, clear_btn)


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

<MDTextFieldRound>
    orientation: 'vertical'
    size_hint: None, None
    height: self.minimum_height
    _instance_icon_left: icon_left
    _instance_icon_right: icon_right

    BoxLayout:
        id: box
        size_hint: None, None
        size: root.size[0], dp(48) if not root.field_height else root.field_height
        pos_hint: {'center_x': .5}

        canvas:
            Color:
                rgba: root._current_color
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [root.radius,]
        canvas.after:
            Color:
                rgba: root._outline_color
            Line:
                width: 1.1
                rounded_rectangle:
                    (self.x, self.y, self.width, self.height,\
                    root.radius, root.radius, root.radius, root.radius,\
                    self.height)

        MDIconButton:
            id: icon_left
            icon: root.icon_left
            disabled: True if root.icon_left_disabled else False
            theme_text_color: 'Custom'
            text_color: root.icon_left_color
            on_release: if root.icon_callback: root.icon_callback(field, self)
            user_font_size: root.icon_size
            pos_hint: {"center_y": .5}

        TextInput:
            id: field
            text: root.text
            password: root.password
            password_mask: root.password_mask
            background_active: f'{images_path}transparent.png'
            background_normal: f'{images_path}transparent.png'
            multiline: False
            padding: (box.height / 2) - (self.line_height / 2)
            cursor_color: root.cursor_color
            foreground_color: root.foreground_color
            hint_text: root.hint_text
            selection_color: root.selection_color
            hint_text_color: root.hint_text_color
            write_tab: root.write_tab
            input_filter: root.input_filter
            readonly: root.readonly
            tab_width:root.tab_width
            text_language: root.text_language
            font_context: root.font_context
            font_name: root.font_name
            font_family: root.font_family
            font_size: sp(root.font_size)
            allow_copy: root.allow_copy
            on_focus: root._on_focus(self)
            on_text:
                root.text = self.text
                root.dispatch("on_text")
            on_text_validate:
                root.dispatch("on_text_validate")

        MDIconButton:
            id: icon_right
            icon: root.icon_right
            disabled: True if root.icon_right_disabled else False
            theme_text_color: 'Custom'
            text_color: root.icon_right_color
            on_release: if root.icon_callback: root.icon_callback(field, self)
            user_font_size: root.icon_size
            pos_hint: {"center_y": .5}

    Widget:
        id: spacer
        size_hint_y: None
        height: 0

    Label:
        id: label_error_require
        size_hint: None, None
        size: self.texture_size
        color: root.error_color
        pos_hint: {'center_x': .5}
        halign: 'center'
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


class MDTextFieldClear(BoxLayout):
    hint_text = StringProperty()
    text = StringProperty()
    password = BooleanProperty(False)
    password_mask = StringProperty("*")

    def refresh_field(self, instance_field, instance_clear_button):
        def refresh_field(interval):
            instance_clear_button.custom_color = (
                instance_field.line_color_normal
            )
            instance_field.focus = True
            instance_field.text = ""

        Clock.schedule_once(refresh_field, 0.2)


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
        # self._hint_lbl.width = self.width

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
                    10
                )
            Animation(
                _line_blank_space_right_hint_text=self._line_blank_space_right_hint_text,
                _line_blank_space_left_hint_text=self._hint_lbl.x - dp(5),
                _current_hint_text_color=[1, 1, 0, 1],
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


class MDTextFieldRound(ThemableBehavior, BoxLayout):

    __events__ = ("on_text_validate", "on_text", "on_focus")

    write_tab = BooleanProperty(False)
    """write_tab property of TextInput"""

    input_filter = ObjectProperty(None)
    """input_filter from TextInput"""

    readonly = BooleanProperty(False)
    """readonly property from TextInput"""

    tab_width = NumericProperty(4)
    """tab_width property from TextInput"""

    text_language = StringProperty()
    """text_language property from TextInput"""

    """font related properties from TextInput"""
    font_context = StringProperty()

    font_family = StringProperty()

    font_name = StringProperty("Roboto")

    font_size = NumericProperty(15)

    allow_copy = BooleanProperty(True)
    """Whether copying text from the field is allowed or not"""

    width = NumericProperty(Window.width - dp(100))
    """Text field width."""

    icon_left = StringProperty("email-outline")
    """Left icon."""

    icon_right = StringProperty("email-outline")
    """Right icon."""

    icon_type = OptionProperty(
        "none", options=["right", "left", "all", "without"]
    )
    """Use one (left) or two (left and right) icons in the text field."""

    hint_text = StringProperty()
    """Hint text in the text field."""

    icon_left_color = ListProperty([1, 1, 1, 1])
    """Color of left icon."""

    icon_right_color = ListProperty([1, 1, 1, 1])
    """Color of right icon."""

    icon_size = NumericProperty(dp(24))
    """Size of icons."""

    active_color = ListProperty([1, 1, 1, 0.2])
    """The color of the text field when it is in focus."""

    normal_color = ListProperty([1, 1, 1, 0.5])
    """The color of the text field when it not in focus."""

    foreground_color = ListProperty([1, 1, 1, 1])
    """Text color."""

    hint_text_color = ListProperty([0.5, 0.5, 0.5, 1.0])
    """Text field hint color."""

    cursor_color = ListProperty()
    """Color of cursor"""

    selection_color = ListProperty()
    """Text selection color."""

    icon_callback = ObjectProperty()
    """The function that is called when you click on the icon 
    in the text field."""

    text = StringProperty()
    """Text of field."""

    icon_left_disabled = BooleanProperty(True)
    """Disable the left icon."""

    icon_right_disabled = BooleanProperty(False)
    """Disable the right icon."""

    password = BooleanProperty(False)
    """Hide text or notю"""

    password_mask = StringProperty("*")
    """Characters on which the text will be replaced
    if the `password` is True."""

    require_text_error = StringProperty()
    """Error text if the text field requires mandatory text."""

    require_error_callback = ObjectProperty()
    """The function that will be called when the unfocus.
    if `require_text_error` != ''
    """

    event_focus = ObjectProperty()
    """The function is called at the moment of focus/unfocus of the text field.
    """

    focus = BooleanProperty()
    """Whether or not the widget is focused"""

    radius = NumericProperty(dp(25))
    """The values ​​of the rounding of the corners of the tex field."""

    field_height = NumericProperty(0)
    """Text box height."""

    error_color = ListProperty(
        [0.7607843137254902, 0.2235294117647059, 0.2549019607843137, 1]
    )

    _current_color = ListProperty()

    _outline_color = ListProperty([0, 0, 0, 0])

    _instance_icon_left = ObjectProperty()

    _instance_icon_right = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not (len(self.cursor_color)):
            self.cursor_color = self.theme_cls.primary_color
        if not (len(self.selection_color)):
            self.selection_color = self.theme_cls.primary_color
            self.selection_color[3] = 0.75
        self._current_color = self.normal_color

    def _on_focus(self, field):
        self._current_color = (
            self.active_color if field.focus else self.normal_color
        )
        self.get_color_line(field, field.text, field.focus)
        self.hide_require_error(field.focus)
        if self.event_focus:
            self.event_focus(self, field, field.focus)
        self.focus = field.focus
        self.dispatch("on_focus")
        try:
            if self._instance_icon_left:
                self._instance_icon_left.text_color = (
                    self.theme_cls.primary_color
                    if field.focus
                    else self.icon_left_color
                )
        except ReferenceError:
            pass

    def on_icon_type(self, instance, value):
        def remove_icon_right():
            self.ids.box.remove_widget(self.ids.icon_right)
            self.add_widget(Widget(size_hint_x=None, width=dp(48)))

        if value == "left":
            remove_icon_right()
        elif value == "right":
            self.ids.box.remove_widget(self.ids.icon_left)
        elif value == "without":
            remove_icon_right()
            self.ids.box.remove_widget(self.ids.icon_left)
            self.add_widget(Widget(size_hint_x=None, width=dp(48)), index=0)

    def on_normal_color(self, instance, value):
        self._current_color = value

    def get_color_line(self, field_inastance, field_text, field_focus):
        if not field_focus:
            if self.require_text_error and field_text == "":
                self._outline_color = self.error_color
                self._instance_icon_left.text_color = self._outline_color
                if self.require_text_error != "":
                    self.show_require_error()
            else:
                self._outline_color = [0, 0, 0, 0]
        else:
            self._outline_color = self.theme_cls.primary_color

    def show_require_error(self):
        self.ids.label_error_require.text = self.require_text_error
        self.ids.spacer.height = "10dp"
        if self.require_error_callback:
            self.require_error_callback(self)

    def hide_require_error(self, focus):
        if focus:
            self.ids.label_error_require.text = ""
            self.ids.spacer.height = 0

    """ TextInput Events"""

    def on_text_validate(self):
        pass

    def on_text(self, *args):
        pass

    def on_focus(self, *args):
        pass
