"""
Components/TextField
====================

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
-----------------------------

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
---------------------------------------------

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

Clickable icon for MDTextFieldRound
-----------------------------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty

    from kivymd.app import MDApp
    from kivymd.uix.relativelayout import MDRelativeLayout

    KV = '''
    <ClickableTextFieldRound>:
        size_hint_y: None
        height: text_field.height

        MDTextFieldRound:
            id: text_field
            hint_text: root.hint_text
            text: root.text
            password: True
            color_active: app.theme_cls.primary_light
            icon_left: "key-variant"
            padding:
                self._lbl_icon_left.texture_size[1] + dp(10) if self.icon_left else dp(15), \
                (self.height / 2) - (self.line_height / 2), \
                self._lbl_icon_right.texture_size[1] + dp(20), \
                0

        MDIconButton:
            icon: "eye-off"
            ripple_scale: .5
            pos_hint: {"center_y": .5}
            pos: text_field.width - self.width + dp(8), 0
            on_release:
                self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                text_field.password = False if text_field.password is True else True


    MDScreen:

        ClickableTextFieldRound:
            size_hint_x: None
            width: "300dp"
            hint_text: "Password"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class ClickableTextFieldRound(MDRelativeLayout):
        text = StringProperty()
        hint_text = StringProperty()
        # Here specify the required parameters for MDTextFieldRound:
        # [...]


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. seealso::

    See more information in the :class:`~MDTextFieldRect` class.
"""

__all__ = ("MDTextField", "MDTextFieldRect", "MDTextFieldRound")

import os
import re
from typing import NoReturn, Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    DictProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivymd import uix_path
from kivymd.font_definitions import theme_font_styles
from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDIcon

with open(
    os.path.join(uix_path, "textfield", "textfield.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDTextFieldRect(ThemableBehavior, TextInput):
    line_anim = BooleanProperty(True)
    """
    If True, then text field shows animated line when on focus.

    :attr:`line_anim` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    def get_rect_instruction(self):
        canvas_instructions = self.canvas.after.get_group("rectangle")
        return canvas_instructions[0]

    _rectangle = AliasProperty(get_rect_instruction, cache=True)
    """
    It is the :class:`~kivy.graphics.vertex_instructions.Line`
    instruction reference of the field rectangle.

    :attr:`_rectangle` is an :class:`~kivy.properties.AliasProperty`.
    """

    def get_color_instruction(self):
        canvas_instructions = self.canvas.after.get_group("color")
        return canvas_instructions[0]

    _rectangle_color = AliasProperty(get_color_instruction, cache=True)
    """
    It is the :class:`~kivy.graphics.context_instructions.Color`
    instruction reference of the field rectangle.

    :attr:`_rectangle_color` is an :class:`~kivy.properties.AliasProperty`.
    """

    _primary_color = ColorProperty((0, 0, 0, 0))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._update_primary_color()
        self.theme_cls.bind(primary_color=self._update_primary_color)

    def anim_rect(self, points, alpha):
        if alpha == 1:
            d_line = 0.3
            d_color = 0.4
        else:
            d_line = 0.05
            d_color = 0.05

        Animation(
            points=points, d=(d_line if self.line_anim else 0), t="out_cubic"
        ).start(self._rectangle)
        Animation(a=alpha, d=(d_color if self.line_anim else 0)).start(
            self._rectangle_color
        )

    def _update_primary_color(self, *args):
        self._primary_color = self.theme_cls.primary_color
        self._primary_color[3] = 0


class TextfieldLabel(ThemableBehavior, Label):
    """Base texture for :class:`~MDTextField` class."""

    font_style = OptionProperty("Body1", options=theme_font_styles)
    # <kivymd.uix.textfield.MDTextField object>
    field = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = sp(self.theme_cls.font_styles[self.font_style][1])


class MDTextField(ThemableBehavior, TextInput):
    helper_text = StringProperty()
    """
    Text for ``helper_text`` mode.

    :attr:`helper_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    helper_text_mode = OptionProperty(
        "on_focus", options=["on_error", "persistent", "on_focus"]
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
        "primary", options=["primary", "accent", "custom"], deprecated=True
    )
    """
    Color text mode. Available options are: `'primary'`, `'accent'`,
    `'custom'`.

    .. deprecated:: 1.0.0
        Don't use this attribute.

    :attr:`color_mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'primary'`.
    """

    mode = OptionProperty("line", options=["rectangle", "fill", "line"])
    """
    Text field mode. Available options are: `'line'`, `'rectangle'`, `'fill'`.

    :attr:`mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'line'`.
    """

    line_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Line color normal (static underline line) in ``rgba`` format.

    .. code-block:: kv

        MDTextField:
            hint_text: "line_color_normal"
            line_color_normal: 1, 0, 1, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-line-color-normal.gif
        :align: center

    :attr:`line_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    line_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Line color focus (active underline line) in ``rgba`` format.

    .. code-block:: kv

        MDTextField:
            hint_text: "line_color_focus"
            line_color_focus: 0, 1, 0, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-line-color-focus.gif
        :align: center

    :attr:`line_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    line_anim = BooleanProperty(True)
    """
    If True, then text field shows animated line when on focus.

    :attr:`line_anim` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    error_color = ColorProperty([0, 0, 0, 0])
    """
    Error color in ``rgba`` format for ``required = True``.

    :attr:`error_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    fill_color = ColorProperty([0, 0, 0, 0], deprecated=True)
    """
    The background color of the fill in rgba format when the ``mode`` parameter
    is "fill".

    .. deprecated:: 1.0.0
        Use :attr:`fill_color_normal` and :attr:`fill_color_focus` instead.

    :attr:`fill_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    fill_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Fill background color in 'fill' mode when text field is out of focus.

    :attr:`fill_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    fill_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Fill background color in 'fill' mode when the text field has focus.

    :attr:`fill_color_focus` is an :class:`~kivy.properties.ColorProperty`
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

    current_hint_text_color = ColorProperty([0, 0, 0, 0], deprecated=True)
    """
    Hint text color.

    .. deprecated:: 1.0.0
        Use :attr:`hint_text_color_normal` and :attr:`hint_text_color_focus` instead.

    :attr:`current_hint_text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    hint_text_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Hint text color when text field is out of focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            hint_text: "hint_text_color_normal"
            hint_text_color_normal: 0, 1, 0, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-hint-text-color-normal.gif
        :align: center

    :attr:`hint_text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    hint_text_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Hint text color when the text field has focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            hint_text: "hint_text_color_focus"
            hint_text_color_focus: 0, 1, 0, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-hint-text-color-focus.gif
        :align: center

    :attr:`hint_text_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    helper_text_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Helper text color when text field is out of focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            helper_text: "helper_text_color_normal"
            helper_text_mode: "persistent"
            helper_text_color_normal: 0, 1, 0, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-helper-text-color-normal.png
        :align: center

    :attr:`helper_text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    helper_text_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Helper text color when the text field has focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            helper_text: "helper_text_color_focus"
            helper_text_mode: "persistent"
            helper_text_color_focus: 0, 1, 0, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-helper-text-color-focus.gif
        :align: center

    :attr:`helper_text_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    icon_right_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Color of right icon when text field is out of focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            icon_right: "language-python"
            hint_text: "icon_right_color_normal"
            icon_right_color_normal: 0, 1, 0, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-icon-right-color-normal.gif
        :align: center

    :attr:`icon_right_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    icon_right_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Color of right icon  when the text field has focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            icon_right: "language-python"
            hint_text: "icon_right_color_focus"
            icon_right_color_focus: 0, 1, 0, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-icon-right-color-focus.gif
        :align: center

    :attr:`icon_right_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    icon_left_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Color of right icon when text field is out of focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            icon_right: "language-python"
            hint_text: "icon_right_color_normal"
            icon_left_color_normal: 0, 1, 0, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-icon-right-color-normal.gif
        :align: center

    :attr:`icon_left_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    icon_left_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Color of right icon  when the text field has focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            icon_right: "language-python"
            hint_text: "icon_right_color_focus"
            icon_right_color_focus: 0, 1, 0, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-icon-right-color-focus.gif
        :align: center

    :attr:`icon_left_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    max_length_text_color = ColorProperty([0, 0, 0, 0])
    """
    Text color of the maximum length of characters to be input.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            hint_text: "max_length_text_color"
            max_length_text_color: 0, 1, 0, 1
            max_text_length: 5

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-max-length-text-color.gif
        :align: center

    :attr:`max_length_text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    icon_right = StringProperty()
    """
    Right icon texture.

    .. note:: It's just a texture. It has no press/touch events.

    :attr:`icon_right` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_left = StringProperty()
    """
    Left icon texture.

    .. versionadded:: 1.0.0

    .. note:: It's just a texture. It has no press/touch events.
        Also note that you cannot use the left and right icons at the same time yet.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-left-icon.png
        :align: center

    :attr:`icon_left` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_right_color = ColorProperty([0, 0, 0, 1], deprecated=True)
    """
    Color of right icon in ``rgba`` format.

    .. deprecated:: 1.0.0
        Don't use this attribute.

    :attr:`icon_right_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 1]`.
    """

    text_color = ColorProperty([0, 0, 0, 0], deprecated=True)
    """
    Text color in ``rgba`` format.

    .. deprecated:: 1.0.0
        Use :attr:`text_color_normal` and :attr:`text_color_focus` instead.

    :attr:`text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    text_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Text color in ``rgba`` format when text field is out of focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            hint_text: "text_color_normal"
            text_color_normal: 0, 1, 0, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-text-color-normal.gif
        :align: center

    :attr:`text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    text_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Text color in ``rgba`` format when text field has focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            hint_text: "text_color_focus"
            text_color_focus: 0, 1, 0, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-text-color-focus.gif
        :align: center

    :attr:`text_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    font_size = NumericProperty("16sp")
    """
    Font size of the text in pixels.

    :attr:`font_size` is a :class:`~kivy.properties.NumericProperty` and
    defaults to `'16sp'`.
    """

    # TODO: Add minimum allowed height. Otherwise, if the value is,
    #  for example, 20, the text field will simply be lessened.
    max_height = NumericProperty(0)
    """
    Maximum height of the text box when `multiline = True`.

    .. code-block:: kv

        MDTextField:
            size_hint_x: .5
            hint_text: "multiline=True"
            max_height: "200dp"
            mode: "fill"
            fill_color: 0, 0, 0, .4
            multiline: True
            pos_hint: {"center_x": .5, "center_y": .5}

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-fill-mode-multiline-max-height.gif
        :align: center

    :attr:`max_height` is a :class:`~kivy.properties.NumericProperty` and
    defaults to `0`.
    """

    radius = ListProperty([10, 10, 0, 0])
    """
    The corner radius for a text field in `fill` mode.

    :attr:`radius` is a :class:`~kivy.properties.ListProperty` and
    defaults to `[10, 10, 0, 0]`.
    """

    font_name_helper_text = StringProperty("Roboto")
    """
    Font name for helper text.

    :attr:`font_name_helper_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Roboto'`.
    """

    font_name_hint_text = StringProperty("Roboto")
    """
    Font name for hint text.

    :attr:`font_name_hint_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Roboto'`.
    """

    font_name_max_length = StringProperty("Roboto")
    """
    Font name for max text length.

    :attr:`font_name_max_length` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Roboto'`.
    """

    # The x-axis position of the hint text in the text field.
    _hint_x = NumericProperty(0)
    # The y-axis position of the hint text in the text field.
    _hint_y = NumericProperty("38dp")
    # Width of underline that animates when the focus of the text field.
    _underline_width = NumericProperty(0)
    # Font size for hint text.
    _hint_text_font_size = NumericProperty(sp(16))

    # Label object for `helper_text` parameter.
    _helper_text_label = None
    # Label object for `max_text_length` parameter.
    _max_length_label = None
    # Label object for `hint_text` parameter.
    _hint_text_label = None
    # `MDIcon` object for the icon on the right.
    _icon_right_label = None
    # `MDIcon` object for the icon on the left.
    _icon_left_label = None

    # The left and right coordinates of the text field in 'rectangle' mode.
    #
    # ┍──blank_space_left     blank_space_right──────────────┑
    # |                                                      |
    # |                                                      |
    # |                                                      |
    # ┕──────────────────────────────────────────────────────┙
    _line_blank_space_right_point = NumericProperty(0)
    _line_blank_space_left_point = NumericProperty(0)

    # The values of colors that are used in the KV file to display the color
    # of the corresponding texture.
    _fill_color = ColorProperty([0, 0, 0, 0])
    _text_color_normal = ColorProperty([0, 0, 0, 0])
    _hint_text_color = ColorProperty([0, 0, 0, 0])
    _helper_text_color = ColorProperty([0, 0, 0, 0])
    _max_length_text_color = ColorProperty([0, 0, 0, 0])
    _icon_right_color = ColorProperty([0, 0, 0, 0])
    _icon_left_color = ColorProperty([0, 0, 0, 0])
    _line_color_normal = ColorProperty([0, 0, 0, 0])
    _line_color_focus = ColorProperty([0, 0, 0, 0])

    # List of color attribute names that should be updated when changing the
    # application color palette.
    _colors_to_updated = ListProperty()

    def __init__(self, **kwargs):
        self.set_objects_labels()
        Clock.schedule_once(self._set_attr_names_to_updated)
        Clock.schedule_once(self.set_colors_to_updated)
        Clock.schedule_once(self.set_default_colors)
        super().__init__(**kwargs)
        self.bind(
            _hint_text_font_size=self._hint_text_label.setter("font_size"),
            _icon_right_color=self._icon_right_label.setter("text_color"),
            _icon_left_color=self._icon_left_label.setter("text_color"),
            text=self.set_text,
        )
        self.theme_cls.bind(
            primary_color=lambda x, y: self.set_default_colors(0, True),
            theme_style=lambda x, y: self.set_default_colors(0, True),
        )
        Clock.schedule_once(self.check_text)

    # TODO: Is this method necessary?
    #  During testing, a quick double-click on the text box does not stop
    #  the animation of the hint text height.
    def cancel_all_animations_on_double_click(self) -> NoReturn:
        """
        Cancels the animations of the text field when double-clicking on the
        text field.
        """

        if (
            self._hint_y == dp(38)
            and not self.text
            or self._hint_y == dp(14)
            and self.text
        ):
            Animation.cancel_all(
                self,
                "_underline_width",
                "_hint_y",
                "_hint_x",
                "_hint_text_font_size",
            )

    def set_colors_to_updated(self, interval: Union[float, int]) -> NoReturn:
        for attr_name in self._attr_names_to_updated.keys():
            if getattr(self, attr_name) == [0, 0, 0, 0]:
                self._colors_to_updated.append(attr_name)

    def set_default_colors(
        self, interval: Union[float, int], updated: bool = False
    ) -> NoReturn:
        """
        Sets the default text field colors when initializing a text field
        object. Also called when the application palette changes.

        :param updated: If `True` - the color theme of the application has
                        been changed. Updating the meanings of the colors.
        """

        self._set_attr_names_to_updated(0)
        for attr_name in self._attr_names_to_updated.keys():
            self._set_color(
                attr_name, self._attr_names_to_updated[attr_name], updated
            )

        if self.error_color == [0, 0, 0, 0] or updated:
            self.error_color = self.theme_cls.error_color
        if self.max_length_text_color == [0, 0, 0, 0] or updated:
            self.max_length_text_color = self.theme_cls.disabled_hint_text_color

        self._hint_text_color = self.hint_text_color_normal
        self._text_color_normal = self.text_color_normal
        self._fill_color = self.fill_color_normal
        self._icon_right_color = self.icon_right_color_normal
        self._icon_left_color = self.icon_left_color_normal
        self._max_length_text_color = [0, 0, 0, 0]

        if self.helper_text_mode in ("on_focus", "on_error"):
            self._helper_text_color = [0, 0, 0, 0]
        elif self.helper_text_mode == "persistent":
            self._helper_text_color = self.helper_text_color_normal

        self._line_color_normal = self.line_color_normal
        self._line_color_focus = self.line_color_focus

    def set_notch_rectangle(self, joining: bool = False) -> NoReturn:
        """
        Animates a notch for the hint text in the rectangle of the text field
        of type `rectangle`.
        """

        def on_progress(*args):
            self._line_blank_space_right_point = (
                self._hint_text_label.width + dp(5) if not joining else 0
            )

        if self.hint_text:
            animation = Animation(
                _line_blank_space_left_point=self._hint_text_label.x - dp(5)
                if not joining
                else 0,
                duration=0.2,
                t="out_quad",
            )
            animation.bind(on_progress=on_progress)
            animation.start(self)

    def set_active_underline_width(self, width: Union[float, int]) -> NoReturn:
        """Animates the width of the active underline line."""

        Animation(
            _underline_width=width,
            duration=(0.2 if self.line_anim else 0),
            t="out_quad",
        ).start(self)

    def set_static_underline_color(self, color: list) -> NoReturn:
        """Animates the color of a static underline line."""

        Animation(
            _line_color_normal=color,
            duration=(0.2 if self.line_anim else 0),
            t="out_quad",
        ).start(self)

    def set_active_underline_color(self, color: list) -> NoReturn:
        """Animates the fill color for 'fill' mode."""

        Animation(_line_color_focus=color, duration=0.2, t="out_quad").start(
            self
        )

    def set_fill_color(self, color: list) -> NoReturn:
        """Animates the color of the hint text."""

        Animation(_fill_color=color, duration=0.2, t="out_quad").start(self)

    def set_helper_text_color(self, color: list) -> NoReturn:
        """Animates the color of the hint text."""

        Animation(_helper_text_color=color, duration=0.2, t="out_quad").start(
            self
        )

    def set_max_length_text_color(self, color: list) -> NoReturn:
        """Animates the color of the max length text."""

        Animation(
            _max_length_text_color=color, duration=0.2, t="out_quad"
        ).start(self)

    def set_icon_right_color(self, color: list) -> NoReturn:
        """Animates the color of the icon right."""

        Animation(_icon_right_color=color, duration=0.2, t="out_quad").start(
            self
        )

    def set_icon_left_color(self, color: list) -> NoReturn:
        """Animates the color of the icon left."""

        Animation(_icon_left_color=color, duration=0.2, t="out_quad").start(
            self
        )

    def set_hint_text_color(self, focus: bool, error: bool = False) -> NoReturn:
        """Animates the color of the hint text."""

        Animation(
            _hint_text_color=(
                self.hint_text_color_normal
                if not focus
                else self.hint_text_color_focus
            )
            if not error
            else self.error_color,
            duration=0.2,
            t="out_quad",
        ).start(self)

    def set_pos_hint_text(self, y: float, x: float = 0) -> NoReturn:
        """Animates the x-axis width and y-axis height of the hint text."""

        Animation(_hint_y=y, duration=0.2, t="out_quad").start(self)
        if self.mode == "rectangle":
            Animation(
                _hint_x=x if not self.icon_left else dp(-16),
                duration=0.2,
                t="out_quad",
            ).start(self)
        elif self.mode == "fill":
            Animation(
                _hint_x=dp(16) if not self.icon_left else dp(36),
                duration=0.2,
                t="out_quad",
            ).start(self)
        elif self.mode == "line":
            Animation(
                _hint_x=dp(0) if not self.icon_left else dp(36),
                duration=0.2,
                t="out_quad",
            ).start(self)

    def set_hint_text_font_size(self, font_size: float) -> NoReturn:
        """Animates the font size of the hint text."""

        Animation(
            _hint_text_font_size=font_size, duration=0.2, t="out_quad"
        ).start(self)

    def set_max_text_length(self) -> NoReturn:
        """Called when text is entered into a text field."""

        if self.max_text_length:
            self._max_length_label.text = (
                f"{len(self.text)}/{self.max_text_length}"
            )

    def check_text(self, interval: Union[float, int]) -> NoReturn:
        self.set_text(self, self.text)

    def set_text(self, instance_text_field, text: str) -> NoReturn:
        """Called when text is entered into a text field."""

        self.text = re.sub("\n", " ", text) if not self.multiline else text
        self.set_max_text_length()

        if self.text and self.max_length_text_color and self._get_has_error():
            self.error = True
        if (
            self.text
            and self.max_length_text_color
            and not self._get_has_error()
        ):
            self.error = False

        # Start the appropriate texture animations when programmatically
        # pasting text into a text field.
        if len(self.text) != 0 and not self.focus:
            self.set_pos_hint_text(
                (dp(28) if self.mode != "line" else dp(18))
                if self.mode != "rectangle"
                else dp(10)
            )
            self.set_hint_text_font_size(sp(12))
            if self.mode == "rectangle":
                self.set_notch_rectangle()

        if not self.text:
            self.on_focus(instance_text_field, False)
            self.focus = False

    def set_objects_labels(self) -> NoReturn:
        """
        Creates labels objects for the parameters`helper_text`,`hint_text`,
        etc.
        """

        self._helper_text_label = TextfieldLabel(
            font_style="Caption",
            halign="left",
            valign="middle",
            field=self,
            font_name=self.font_name_helper_text,
        )
        self._max_length_label = TextfieldLabel(
            font_style="Caption",
            halign="right",
            valign="middle",
            text="",
            field=self,
        )
        self._hint_text_label = TextfieldLabel(
            font_style="Subtitle1", halign="left", valign="middle", field=self
        )
        self._icon_right_label = MDIcon(theme_text_color="Custom")
        self._icon_left_label = MDIcon(theme_text_color="Custom")

    def on_helper_text(self, instance_text_field, helper_text: str) -> NoReturn:
        self._helper_text_label.text = helper_text

    def on_focus(self, instance_text_field, focus: bool) -> NoReturn:
        # TODO: See `cancel_all_animations_on_double_click` method.
        # self.cancel_all_animations_on_double_click()

        if focus:
            if self.mode == "rectangle":
                self.set_notch_rectangle()
            self.set_static_underline_color([0, 0, 0, 0])
            if (
                self.helper_text_mode in ("on_focus", "persistent")
                and self.helper_text
            ):
                self.set_helper_text_color(self.helper_text_color_focus)
            if self.mode == "fill":
                self.set_fill_color(self.fill_color_focus)
            self.set_active_underline_width(self.width)

            self.set_pos_hint_text(
                (dp(28) if self.mode != "line" else dp(18))
                if self.mode != "rectangle"
                else dp(10)
            )
            self.set_hint_text_color(focus)
            self.set_hint_text_font_size(sp(12))

            if self.max_text_length:
                self.set_max_length_text_color(self.max_length_text_color)
            if self.icon_right:
                self.set_icon_right_color(self.icon_right_color_focus)
            if self.icon_left:
                self.set_icon_left_color(self.icon_left_color_focus)

            if self.error:
                if self.hint_text:
                    self.set_hint_text_color(focus, self.error)
                if self.helper_text:
                    self.set_helper_text_color(self.error_color)
                if self.max_text_length:
                    self.set_max_length_text_color(self.error_color)
                if self.icon_right:
                    self.set_icon_right_color(self.error_color)
                if self.icon_left:
                    self.set_icon_left_color(self.error_color)
        else:
            if self.helper_text_mode == "persistent" and self.helper_text:
                self.set_helper_text_color(self.helper_text_color_normal)
            if self.mode == "rectangle" and not self.text:
                self.set_notch_rectangle(joining=True)
            if not self.text:
                self.set_pos_hint_text(
                    dp(38)
                    if not self.icon_left or self.mode == "rectangle"
                    else (dp(34) if not self.mode == "fill" else dp(38))
                )
                self.set_hint_text_font_size(sp(16))
            if self.icon_right:
                self.set_icon_right_color(self.icon_right_color_normal)
            if self.icon_left:
                self.set_icon_left_color(self.icon_left_color_normal)
            if self.hint_text:
                self.set_hint_text_color(focus, self.error)

            self.set_active_underline_width(0)
            self.set_max_length_text_color([0, 0, 0, 0])

            if self.mode == "fill":
                self.set_fill_color(self.fill_color_normal)

            self.error = self._get_has_error() or self.error
            if self.error:
                self.set_static_underline_color(self.error_color)
            else:
                self.set_static_underline_color(self.line_color_normal)

    def on_icon_left(self, instance_text_field, icon_name: str) -> NoReturn:
        self._icon_left_label.icon = icon_name

    def on_icon_right(self, instance_text_field, icon_name: str) -> NoReturn:
        self._icon_right_label.icon = icon_name

    def on_disabled(
        self, instance_text_field, disabled_value: bool
    ) -> NoReturn:
        pass

    def on_error(self, instance_text_field, error: bool) -> NoReturn:
        """
        Changes the primary colors of the text box to match the `error` value
        (text field is in an error state or not).
        """

        if error:
            self.set_max_length_text_color(self.error_color)
            self.set_active_underline_color(self.error_color)
            if self.hint_text:
                self.set_hint_text_color(self.focus, self.error)
            if self.helper_text:
                self.set_helper_text_color(self.error_color)
            if self.icon_right:
                self.set_icon_right_color(self.error_color)
            if self.icon_left:
                self.set_icon_left_color(self.error_color)
            if self.helper_text_mode == "on_error":
                self.set_helper_text_color(self.error_color)
        else:
            self.set_max_length_text_color(self.max_length_text_color)
            self.set_active_underline_color(self._line_color_focus)
            if self.hint_text:
                self.set_hint_text_color(self.focus)
            if self.helper_text:
                self.set_helper_text_color(self.helper_text_color_focus)
            if self.icon_right:
                self.set_icon_right_color(self.icon_right_color_focus)
            if self.icon_left:
                self.set_icon_left_color(self.icon_left_color_focus)
            if self.helper_text_mode in ("on_focus", "on_error"):
                self.set_helper_text_color([0, 0, 0, 0])
            elif self.helper_text_mode == "persistent":
                self.set_helper_text_color(self.helper_text_color_normal)

    def on_hint_text(self, instance_text_field, hint_text: str) -> NoReturn:
        self._hint_text_label.text = hint_text
        self._hint_text_label.font_size = sp(16)

    def on_width(self, instance_text_field, width: float) -> NoReturn:
        """Called when the application window is resized."""

        if self.focus:
            self._underline_width = self.width

    def on_height(self, instance_text_field, value_height: float) -> NoReturn:
        if value_height >= self.max_height and self.max_height:
            self.height = self.max_height

    def on_text_color_normal(self, instance_text_field, color: list):
        self._text_color_normal = color

    def on_hint_text_color_normal(self, instance_text_field, color: list):
        self._hint_text_color = color

    def on_helper_text_color_normal(self, instance_text_field, color: list):
        self._helper_text_color = color

    def on_icon_right_color_normal(self, instance_text_field, color: list):
        self._icon_right_color = color

    def on_line_color_normal(self, instance_text_field, color: list):
        self._line_color_normal = color

    def on_max_length_text_color(self, instance_text_field, color: list):
        self._max_length_text_color = color

    def _set_color(self, attr_name: str, color: str, updated: bool) -> NoReturn:
        if attr_name in self._colors_to_updated or updated:
            if attr_name in self._colors_to_updated:
                setattr(self, attr_name, color)

    def _set_attr_names_to_updated(
        self, interval: Union[float, int]
    ) -> NoReturn:
        """
        Sets and update the default color dictionary for text field textures.
        """

        self._attr_names_to_updated = {
            "line_color_normal": self.theme_cls.disabled_hint_text_color,
            "line_color_focus": self.theme_cls.primary_color,
            "hint_text_color_normal": self.theme_cls.disabled_hint_text_color,
            "hint_text_color_focus": self.theme_cls.primary_color,
            "helper_text_color_normal": self.theme_cls.disabled_hint_text_color,
            "helper_text_color_focus": self.theme_cls.disabled_hint_text_color,
            "text_color_normal": self.theme_cls.disabled_hint_text_color,
            "text_color_focus": self.theme_cls.primary_color,
            "fill_color_normal": self.theme_cls.bg_darkest,
            "fill_color_focus": self.theme_cls.bg_dark,
            "icon_right_color_normal": self.theme_cls.disabled_hint_text_color,
            "icon_right_color_focus": self.theme_cls.primary_color,
            "icon_left_color_normal": self.theme_cls.disabled_hint_text_color,
            "icon_left_color_focus": self.theme_cls.primary_color,
        }

    def _get_has_error(self) -> bool:
        """
        Returns `False` or `True` depending on the state of the text field,
        for example when the allowed character limit has been exceeded or when
        the :attr:`~MDTextField.required` parameter is set to `True`.
        """

        if self.max_text_length and len(self.text) > self.max_text_length:
            has_error = True
        else:
            if all((self.required, len(self.text) == 0)):
                has_error = True
            else:
                has_error = False
        return has_error

    def _refresh_hint_text(self):
        """Method override to avoid duplicate hint text texture."""


class MDTextFieldRound(ThemableBehavior, TextInput):
    icon_left = StringProperty()
    """
    Left icon.

    :attr:`icon_left` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_left_color = ColorProperty((0, 0, 0, 1))
    """
    Color of left icon in ``rgba`` format.

    :attr:`icon_left_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `(0, 0, 0, 1)`.
    """

    icon_right = StringProperty()
    """
    Right icon.

    :attr:`icon_right` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_right_color = ColorProperty((0, 0, 0, 1))
    """
    Color of right icon.

    :attr:`icon_right_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `(0, 0, 0, 1)`.
    """

    line_color = ColorProperty(None)
    """
    Field line color.

    :attr:`line_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    normal_color = ColorProperty(None)
    """
    Field color if `focus` is `False`.

    :attr:`normal_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    color_active = ColorProperty(None)
    """
    Field color if `focus` is `True`.

    :attr:`color_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _color_active = ColorProperty(None)
    _icon_left_color_copy = ColorProperty(None)
    _icon_right_color_copy = ColorProperty(None)

    def __init__(self, **kwargs):
        self._lbl_icon_left = MDIcon(theme_text_color="Custom")
        self._lbl_icon_right = MDIcon(theme_text_color="Custom")
        super().__init__(**kwargs)
        self.cursor_color = self.theme_cls.primary_color
        self.icon_left_color = self.theme_cls.text_color
        self.icon_right_color = self.theme_cls.text_color

        if not self.normal_color:
            self.normal_color = self.theme_cls.primary_light
        if not self.line_color:
            self.line_color = self.theme_cls.primary_dark
        if not self.color_active:
            self._color_active = (0.5, 0.5, 0.5, 0.5)

    def on_focus(self, instance_text_field, focus_value: bool) -> NoReturn:
        if focus_value:
            self.icon_left_color = self.theme_cls.primary_color
            self.icon_right_color = self.theme_cls.primary_color
        else:
            self.icon_left_color = (
                self._icon_left_color_copy or self.theme_cls.text_color
            )
            self.icon_right_color = (
                self._icon_right_color_copy or self.theme_cls.text_color
            )

    def on_icon_left(self, instance_text_field, icon_name: str) -> NoReturn:
        self._lbl_icon_left.icon = icon_name

    def on_icon_left_color(self, instance_text_field, color: list) -> NoReturn:
        self._lbl_icon_left.text_color = color
        if (
            not self._icon_left_color_copy
            and color != self.theme_cls.text_color
            and color != self.theme_cls.primary_color
        ):
            self._icon_left_color_copy = color

    def on_icon_right(self, instance_text_field, icon_name: str) -> NoReturn:
        self._lbl_icon_right.icon = icon_name

    def on_icon_right_color(self, instance_text_field, color: list) -> NoReturn:
        self._lbl_icon_right.text_color = color
        if (
            not self._icon_right_color_copy
            and color != self.theme_cls.text_color
            and color != self.theme_cls.primary_color
        ):
            self._icon_right_color_copy = color

    def on_color_active(self, instance_text_field, color: list) -> NoReturn:
        if color != [0, 0, 0, 0.5]:
            self._color_active = color
            self._color_active[-1] = 0.5
        else:
            self._color_active = color


if __name__ == "__main__":
    from kivy.lang import Builder
    from kivy.uix.textinput import TextInput

    from kivymd.app import MDApp

    KV = """
MDScreen:

    MDBoxLayout:
        id: box
        orientation: "vertical"
        spacing: "28dp"
        adaptive_height: True
        size_hint_x: .8
        pos_hint: {"center_x": .5, "center_y": .5}

        MDTextField:
            hint_text: "Label"
            helper_text: "Error massage"
            mode: "rectangle"

        MDTextField:
            icon_left: "git"
            hint_text: "Label"
            helper_text: "Error massage"
            mode: "rectangle"

        MDTextField:
            icon_left: "git"
            hint_text: "Label"
            helper_text: "Error massage"
            mode: "fill"

        MDTextField:
            hint_text: "Label"
            helper_text: "Error massage"
            mode: "fill"

        MDTextField:
            hint_text: "Label"
            helper_text: "Error massage"

        MDTextField:
            icon_left: "git"
            hint_text: "Label"
            helper_text: "Error massage"

        MDFlatButton:
            text: "SET TEXT"
            pos_hint: {"center_x": .5}
            on_release: app.set_text()
"""

    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def set_text(self):
            for widget in self.root.ids.box.children:
                if issubclass(widget.__class__, TextInput):
                    widget.text = "Input text"

    Test().run()
