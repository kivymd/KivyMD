"""
Components/Text Field
=====================

.. seealso::

    `Material Design spec, Text fields <https://material.io/components/text-fields>`_

.. rubric:: Text fields let users enter and edit text.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields.png
    :align: center

`KivyMD` provides the following field classes for use:

- MDTextField_
- MDTextFieldRound_
- MDTextFieldRect_

.. Note:: :class:`~MDTextField` inherited from
    :class:`~kivy.uix.textinput.TextInput`. Therefore, most parameters and all
    events of the :class:`~kivy.uix.textinput.TextInput` class are also
    available in the :class:`~MDTextField` class.

.. MDTextField:
MDTextField
-----------


:class:`~MDTextField` can be with helper text and without.

Without helper text mode
------------------------

.. code-block:: kv

    MDTextField:
        hint_text: "No helper text"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-no-helper-mode.gif
    :align: center

Helper text mode on ``on_focus`` event
--------------------------------------

.. code-block:: kv

    MDTextField:
        hint_text: "Helper text on focus"
        helper_text: "This will disappear when you click off"
        helper_text_mode: "on_focus"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-helper-mode-on-focus.gif
    :align: center

Persistent helper text mode
---------------------------

.. code-block:: kv

    MDTextField:
        hint_text: "Persistent helper text"
        helper_text: "Text is always here"
        helper_text_mode: "persistent"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-helper-mode-persistent.gif
    :align: center

Helper text mode `'on_error'`
----------------------------

To display an error in a text field when using the
``helper_text_mode: "on_error"`` parameter, set the `"error"` text field
parameter to `True`:

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    BoxLayout:
        padding: "10dp"

        MDTextField:
            id: text_field_error
            hint_text: "Helper text on error (press 'Enter')"
            helper_text: "There will always be a mistake"
            helper_text_mode: "on_error"
            pos_hint: {"center_y": .5}
    '''


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)

        def build(self):
            self.screen.ids.text_field_error.bind(
                on_text_validate=self.set_error_message,
                on_focus=self.set_error_message,
            )
            return self.screen

        def set_error_message(self, instance_textfield):
            self.screen.ids.text_field_error.error = True


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-helper-mode-on-error.gif
    :align: center

Helper text mode `'on_error'` (with required)
--------------------------------------------

.. code-block:: kv

    MDTextField:
        hint_text: "required = True"
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter text"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-required.gif
    :align: center

Text length control
-------------------

.. code-block:: kv

    MDTextField:
        hint_text: "Max text length = 5"
        max_text_length: 5

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-text-length.gif
    :align: center


Multi line text
---------------

.. code-block:: kv

    MDTextField:
        multiline: True
        hint_text: "Multi-line text"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-text-multi-line.gif
    :align: center

Color mode
----------

.. code-block:: kv

    MDTextField:
        hint_text: "color_mode = 'accent'"
        color_mode: 'accent'

Available options are  `'primary'`, `'accent'` or `'custom`'.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-color-mode.gif
    :align: center

.. code-block:: kv

    MDTextField:
        hint_text: "color_mode = 'custom'"
        color_mode: 'custom'
        helper_text_mode: "on_focus"
        helper_text: "Color is defined by 'line_color_focus' property"
        line_color_focus: 1, 0, 1, 1

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-color-mode-custom.gif
    :align: center

.. code-block:: kv

    MDTextField:
        hint_text: "Line color normal"
        line_color_normal: app.theme_cls.accent_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-line-color-normal.png
    :align: center

Rectangle mode
--------------

.. code-block:: kv

    MDTextField:
        hint_text: "Rectangle mode"
        mode: "rectangle"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-rectangle-mode.gif
    :align: center

Fill mode
---------

.. code-block:: kv

    MDTextField:
        hint_text: "Fill mode"
        mode: "fill"
        fill_color: 0, 0, 0, .4

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-fill-mode.gif
    :align: center

.. MDTextFieldRect:
MDTextFieldRect
---------------

.. Note:: :class:`~MDTextFieldRect` inherited from
    :class:`~kivy.uix.textinput.TextInput`. You can use all parameters and
    attributes of the :class:`~kivy.uix.textinput.TextInput` class in the
    :class:`~MDTextFieldRect` class.

.. code-block:: kv

    MDTextFieldRect:
        size_hint: 1, None
        height: "30dp"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-rect.gif
    :align: center

.. Warning:: While there is no way to change the color of the border.

.. MDTextFieldRound:
MDTextFieldRound
----------------

Without icon
------------

.. code-block:: kv

    MDTextFieldRound:
        hint_text: 'Empty field'

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-round.gif
    :align: center

With left icon
--------------

.. Warning:: The icons in the :class:`~MDTextFieldRound` are static. You cannot
    bind events to them.

.. code-block:: kv

    MDTextFieldRound:
        icon_left: "email"
        hint_text: "Field with left icon"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-round-left-icon.png
    :align: center

With left and right icons
-------------------------

.. code-block:: kv

    MDTextFieldRound:
        icon_left: 'key-variant'
        icon_right: 'eye-off'
        hint_text: 'Field with left and right icons'

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-round-left-right-icon.png
    :align: center

Control background color
------------------------

.. code-block:: kv

    MDTextFieldRound:
        icon_left: 'key-variant'
        normal_color: app.theme_cls.accent_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-round-normal-color.gif
    :align: center

.. code-block:: kv

    MDTextFieldRound:
        icon_left: 'key-variant'
        normal_color: app.theme_cls.accent_color
        color_active: 1, 0, 0, 1

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-round-active-color.gif
    :align: center

With right icon
---------------

.. Note:: The icon on the right is available for use in all text fields.

.. code-block:: kv

    MDTextField:
        hint_text: "Name"
        mode: "fill"
        fill_color: 0, 0, 0, .4
        icon_right: "arrow-down-drop-circle-outline"
        icon_right_color: app.theme_cls.primary_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-fill-mode-icon.png
    :align: center

.. code-block:: kv

    MDTextField:
        hint_text: "Name"
        icon_right: "arrow-down-drop-circle-outline"
        icon_right_color: app.theme_cls.primary_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-right-icon.png
    :align: center

.. code-block:: kv

    MDTextField:
        hint_text: "Name"
        mode: "rectangle"
        icon_right: "arrow-down-drop-circle-outline"
        icon_right_color: app.theme_cls.primary_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-rectangle-right-icon.png
    :align: center

.. seealso::

    See more information in the :class:`~MDTextFieldRect` class.
"""

__all__ = (
    "MDTextField",
    "MDTextFieldRect",
    "MDTextFieldRound",
)

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

        # Disabled line.
        Color:
            rgba: self.line_color_normal if root.mode == "line" else (0, 0, 0, 0)
        Line:
            points: self.x, self.y + dp(16), self.x + self.width, self.y + dp(16)
            width: 1
            dash_length: dp(3)
            dash_offset: 2 if self.disabled else 0

        # Active line.
        Color:
            rgba: self._current_line_color if root.mode in ("line", "fill") and root.active_line else (0, 0, 0, 0)
        Rectangle:
            size: self._line_width, dp(2)
            pos: self.center_x - (self._line_width / 2), self.y + (dp(16) if root.mode != "fill" else 0)

        # Helper text.
        Color:
            rgba: self._current_error_color
        Rectangle:
            texture: self._msg_lbl.texture
            size:
                self._msg_lbl.texture_size[0] - (dp(3) if root.mode in ("fill", "rectangle") else 0), \
                self._msg_lbl.texture_size[1] - (dp(3) if root.mode in ("fill", "rectangle") else 0)
            pos: self.x + (dp(8) if root.mode == "fill" else 0), self.y + (dp(3) if root.mode in ("fill", "rectangle") else 0)

        # Texture of right Icon.
        Color:
            rgba: self.icon_right_color
        Rectangle:
            texture: self._lbl_icon_right.texture
            size: self._lbl_icon_right.texture_size if self.icon_right else (0, 0)
            pos:
                (self.width + self.x) - (self._lbl_icon_right.texture_size[1]) - dp(8), \
                self.center[1] - self._lbl_icon_right.texture_size[1] / 2 + (dp(8) if root.mode != "fill" else 0) \
                if root.mode != "rectangle" else \
                self.center[1] - self._lbl_icon_right.texture_size[1] / 2 - dp(4)

        Color:
            rgba: self._current_right_lbl_color
        Rectangle:
            texture: self._right_msg_lbl.texture
            size: self._right_msg_lbl.texture_size
            pos: self.width-self._right_msg_lbl.texture_size[0] + dp(45), self.y

        Color:
            rgba:
                (self._current_line_color if self.focus and not \
                self._cursor_blink else (0, 0, 0, 0))
        Rectangle:
            pos: (int(x) for x in self.cursor_pos)
            size: 1, -self.line_height

        # Hint text.
        Color:
            rgba: self._current_hint_text_color if not self.current_hint_text_color else self.current_hint_text_color
        Rectangle:
            texture: self._hint_lbl.texture
            size: self._hint_lbl.texture_size
            pos: self.x + (dp(8) if root.mode == "fill" else 0), self.y + self.height - self._hint_y

        Color:
            rgba:
                self.disabled_foreground_color if self.disabled else\
                (self.hint_text_color if not self.text and not\
                self.focus else self.foreground_color)

        # "rectangle" mode
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

    # "fill" mode.
    canvas.after:
        Color:
            rgba: root.fill_color if root.mode == "fill" else (0, 0, 0, 0)
        RoundedRectangle:
            pos: self.x, self.y
            size: self.width, self.height + dp(8)
            radius: [10, 10, 0, 0, 0]

    font_name: "Roboto" if not root.font_name else root.font_name
    foreground_color: app.theme_cls.text_color
    font_size: "16sp"
    bold: False
    padding:
        0 if root.mode != "fill" else "8dp", \
        "16dp" if root.mode != "fill" else "24dp", \
        0 if root.mode != "fill" and not root.icon_right else ("14dp" if not root.icon_right else self._lbl_icon_right.texture_size[1] + dp(20)), \
        "16dp" if root.mode == "fill" else "10dp"
    multiline: False
    size_hint_y: None
    height: self.minimum_height + (dp(8) if root.mode != "fill" else 0)


<TextfieldLabel>
    size_hint_x: None
    width: self.texture_size[0]
    shorten: True
    shorten_from: "right"


<MDTextFieldRect>
    on_focus:
        root.anim_rect([root.x, root.y, root.right, root.y, root.right, \
        root.top, root.x, root.top, root.x, root.y], 1) if root.focus \
        else root.anim_rect([root.x - dp(60), root.y - dp(60), \
        root.right + dp(60), root.y - dp(60),
        root.right + dp(60), root.top + dp(60), \
        root.x - dp(60), root.top + dp(60), \
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
    helper_text = StringProperty("This field is required")
    """
    Text for ``helper_text`` mode.

    :attr:`helper_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'This field is required'`.
    """

    helper_text_mode = OptionProperty(
        "none", options=["none", "on_error", "persistent", "on_focus"]
    )
    """
    Helper text mode. Available options are: `'on_error'`, `'persistent'`,
    `'on_focus'`.

    :attr:`helper_text_mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'none'`.
    """

    max_text_length = NumericProperty(None)
    """
    Maximum allowed value of characters in a text field.

    :attr:`max_text_length` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    required = BooleanProperty(False)
    """
    Required text. If True then the text field requires text.

    :attr:`required` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    color_mode = OptionProperty(
        "primary", options=["primary", "accent", "custom"]
    )
    """
    Color text mode. Available options are: `'primary'`, `'accent'`,
    `'custom'`.

    :attr:`color_mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'primary'`.
    """

    mode = OptionProperty("line", options=["rectangle", "fill"])
    """
    Text field mode. Available options are: `'line'`, `'rectangle'`, `'fill'`.

    :attr:`mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'line'`.
    """

    line_color_normal = ListProperty()
    """
    Line color normal in ``rgba`` format.

    :attr:`line_color_normal` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    line_color_focus = ListProperty()
    """
    Line color focus in ``rgba`` format.

    :attr:`line_color_focus` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    error_color = ListProperty()
    """
    Error color in ``rgba`` format for ``required = True``.

    :attr:`error_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    fill_color = ListProperty([0, 0, 0, 0])
    """
    The background color of the fill in rgba format when the ``mode`` parameter 
    is "fill".

    :attr:`fill_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    active_line = BooleanProperty(True)
    """
    Show active line or not.

    :attr:`active_line` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    error = BooleanProperty(False)
    """
    If True, then the text field goes into ``error`` mode.

    :attr:`error` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    current_hint_text_color = ListProperty()
    """
    ``hint_text`` text color.

    :attr:`current_hint_text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    icon_right = StringProperty()
    """Right icon.

    :attr:`icon_right` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_right_color = ListProperty([0, 0, 0, 1])
    """Color of right icon in ``rgba`` format.

    :attr:`icon_right_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 1]`.
    """

    _text_len_error = BooleanProperty(False)
    _hint_lbl_font_size = NumericProperty("16sp")
    _line_blank_space_right_hint_text = NumericProperty(0)
    _line_blank_space_left_hint_text = NumericProperty(0)
    _hint_y = NumericProperty("38dp")
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
        self._lbl_icon_right = MDIcon(theme_text_color="Custom")
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

    def on_icon_right(self, instance, value):
        self._lbl_icon_right.icon = value

    def on_icon_right_color(self, instance, value):
        self._lbl_icon_right.text_color = value

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
            _fill_color = self.fill_color
            _fill_color[3] = self.fill_color[3] - 0.1
            Animation(
                _line_blank_space_right_hint_text=self._line_blank_space_right_hint_text,
                _line_blank_space_left_hint_text=self._hint_lbl.x - dp(5),
                _current_hint_text_color=self.line_color_focus,
                fill_color=_fill_color,
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
            _fill_color = self.fill_color
            _fill_color[3] = self.fill_color[3] + 0.1
            Animation(
                fill_color=_fill_color, duration=0.2, t="out_quad",
            ).start(self)
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
    """Left icon.

    :attr:`icon_left` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_left_color = ListProperty([0, 0, 0, 1])
    """Color of left icon in ``rgba`` format.

    :attr:`icon_left_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 1]`.
    """

    icon_right = StringProperty()
    """Right icon.

    :attr:`icon_right` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_right_color = ListProperty([0, 0, 0, 1])
    """Color of right icon.

    :attr:`icon_right_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 1]`.
    """

    line_color = ListProperty()
    """Field line color.

    :attr:`line_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    normal_color = ListProperty()
    """Field color if `focus` is `False`.

    :attr:`normal_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    color_active = ListProperty()
    """Field color if `focus` is `True`.

    :attr:`color_active` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

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
