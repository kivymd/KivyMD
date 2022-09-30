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
    MDScreen:

        MDTextField:
            id: text_field_error
            hint_text: "Helper text on error (press 'Enter')"
            helper_text: "There will always be a mistake"
            helper_text_mode: "on_error"
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint_x: .5
    '''


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)

        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
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
        text: "required = True"
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

Round mode
---------

.. code-block:: kv

    MDTextField:
        hint_text: "Round mode"
        mode: "round"
        max_text_length: 15
        helper_text: "Massage"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-round-mode.gif
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
        background_color: app.theme_cls.bg_normal

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-rect.gif
    :align: center

.. Warning:: While there is no way to change the color of the border.

Clickable icon for MDTextField
------------------------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty

    from kivymd.app import MDApp
    from kivymd.uix.relativelayout import MDRelativeLayout

    KV = '''
    <ClickableTextFieldRound>:
        size_hint_y: None
        height: text_field.height

        MDTextField:
            id: text_field
            hint_text: root.hint_text
            text: root.text
            password: True
            icon_left: "key-variant"

        MDIconButton:
            icon: "eye-off"
            pos_hint: {"center_y": .5}
            pos: text_field.width - self.width + dp(8), 0
            theme_text_color: "Hint"
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

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-clickable_right-icon.gif
    :align: center

.. seealso::

    See more information in the :class:`~MDTextFieldRect` class.
"""

__all__ = ("MDTextField", "MDTextFieldRect")

import os
import re
from datetime import date
from typing import Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
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
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.label import MDIcon

with open(
    os.path.join(uix_path, "textfield", "textfield.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


# TODO: Add a class to work with the phone number mask.


class AutoFormatTelephoneNumber:
    """
    Implements automatic formatting of the text entered in the text field
    according to the mask, for example '+38 (###) ### ## ##'.
    """

    def __init__(self):
        self._backspace = False

    def isnumeric(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def do_backspace(self, *args):
        if self.validator and self.validator == "phone":
            self._backspace = True
            text = self.text
            text = text[:-1]
            self.text = text
            self._backspace = False

    def field_filter(self, value, boolean):
        if self.validator and self.validator == "phone":
            if len(self.text) == 14:
                return
            if self.isnumeric(value):
                return value
        return value

    def format(self, value):
        if value != "" and not value.isspace() and not self._backspace:
            if len(value) <= 1 and self.focus:
                self.text = value
                self._check_cursor()
            elif len(value) == 4:
                start = self.text[:-1]
                end = self.text[-1]
                self.text = "%s) %s" % (start, end)
                self._check_cursor()
            elif len(value) == 8:
                self.text += "-"
                self._check_cursor()
            elif len(value) in [12, 16]:
                start = self.text[:-1]
                end = self.text[-1]
                self.text = "%s-%s" % (start, end)
                self._check_cursor()

    def _check_cursor(self):
        def set_pos_cursor(pos_corsor, interval=0.5):
            self.cursor = (pos_corsor, 0)

        if self.focus:
            Clock.schedule_once(lambda x: set_pos_cursor(len(self.text)), 0.1)


class Validator:
    """Container class for various validation methods."""

    datetime_date = ObjectProperty()
    """
    The last valid date as a <class 'datetime.date'> object.

    :attr:`datetime_date` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    date_interval = ListProperty([None, None])
    """
    The date interval that is valid for input.
    Can be entered as <class 'datetime.date'> objects or a string format.
    Both values or just one value can be entered.

    In string format, must follow the current date_format.
    Example: Given date_format -> "mm/dd/yyyy"
    Input examples -> "12/31/1900", "12/31/2100" or "12/31/1900", None.

    :attr:`date_interval` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[None, None]`.
    """

    date_format = OptionProperty(
        None,
        options=[
            "dd/mm/yyyy",
            "mm/dd/yyyy",
            "yyyy/mm/dd",
        ],
    )

    """
    Format of date strings that will be entered.
    Available options are: `'dd/mm/yyyy'`, `'mm/dd/yyyy'`, `'yyyy/mm/dd'`.

    :attr:`date_format` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    def is_email_valid(self, text: str) -> bool:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", text):
            return True
        return False

    def is_time_valid(self, text: str) -> bool:
        if re.match(r"^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$", text) or re.match(
            r"^(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])$", text
        ):
            return False

        return True

    def is_date_valid(self, text: str) -> bool:
        if not self.date_format:
            raise Exception("TextInput date_format was not defined.")

        # Regex strings.
        dd = "[0][1-9]|[1-2][0-9]|[3][0-1]"
        mm = "[0][1-9]|[1][0-2]"
        yyyy = "[0-9][0-9][0-9][0-9]"
        fmt = self.date_format.split("/")
        largs = locals()
        # Access  the local variables  dict in the correct format based on
        # date_format split. Example: "mm/dd/yyyy" -> ["mm", "dd", "yyyy"]
        # largs[fmt[0]] would be largs["mm"] so the month regex string.
        if re.match(
            f"^({largs[fmt[0]]})/({largs[fmt[1]]})/({largs[fmt[2]]})$", text
        ):
            input_split = text.split("/")
            largs[fmt[0]] = input_split[0]
            largs[fmt[1]] = input_split[1]
            largs[fmt[2]] = input_split[2]
            # Organize input  into correct slots and try to convert
            # to datetime  object. This way February exceptions are
            # tested. Also tests with the date_interval are simpler
            # using datetime objects.
            try:
                datetime = date(
                    int(largs["yyyy"]), int(largs["mm"]), int(largs["dd"])
                )
            except ValueError:
                return True

            if self.date_interval:
                if (
                    self.date_interval[0]
                    and not self.date_interval[0] <= datetime
                    or self.date_interval[1]
                    and not datetime <= self.date_interval[1]
                ):
                    return True

            self.datetime_date = datetime
            return False
        return True

    def on_date_interval(self, *args) -> None:
        """Default event handler for date_interval input."""

        def on_date_interval():
            if not self.date_format:
                raise Exception("TextInput date_format was not defined.")

            fmt = self.date_format.split("/")
            largs = {}
            # Convert string inputs into datetime.date objects and store
            # them back into self.date_interval.
            try:
                if self.date_interval[0] and not isinstance(
                    self.date_interval[0], date
                ):
                    split = self.date_interval[0].split("/")
                    largs[fmt[0]] = split[0]
                    largs[fmt[1]] = split[1]
                    largs[fmt[2]] = split[2]
                    self.date_interval[0] = date(
                        int(largs["yyyy"]), int(largs["mm"]), int(largs["dd"])
                    )
                if self.date_interval[1] and not isinstance(
                    self.date_interval[1], date
                ):
                    split = self.date_interval[1].split("/")
                    largs[fmt[0]] = split[0]
                    largs[fmt[1]] = split[1]
                    largs[fmt[2]] = split[2]
                    self.date_interval[1] = date(
                        int(largs["yyyy"]), int(largs["mm"]), int(largs["dd"])
                    )

            except Exception:
                raise Exception(
                    r"TextInput date_interval was defined incorrectly, it must "
                    r"be composed of <class 'datetime.date'> objects or strings"
                    r" following current date_format."
                )

            # Test if the interval is valid.
            if isinstance(self.date_interval[0], date) and isinstance(
                self.date_interval[1], date
            ):
                if self.date_interval[0] >= self.date_interval[1]:
                    raise Exception(
                        "TextInput date_interval last date must be greater"
                        " than the first date or set to None."
                    )

        Clock.schedule_once(lambda x: on_date_interval())


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


class MDTextField(
    DeclarativeBehavior,
    ThemableBehavior,
    TextInput,
    Validator,
    AutoFormatTelephoneNumber,
):
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

    mode = OptionProperty(
        "line", options=["rectangle", "round", "fill", "line"]
    )
    """
    Text field mode.
    Available options are: `'line'`, `'rectangle'`, `'fill'`, `'round'`.

    :attr:`mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'line'`.
    """

    phone_mask = StringProperty("")

    validator = OptionProperty(None, options=["date", "email", "time", "phone"])
    """
    The type of text field for entering Email, time, etc.
    Automatically sets the type of the text field as "error" if the user input
    does not match any of the set validation types.
    Available options are: `'date'`, `'email'`, `'time'`.

    When using `'date'`, :attr:`date_format` must be defined.

    .. versionadded:: 1.1.0

    .. code-block:: python

        MDTextField:
            hint_text: "Email"
            helper_text: "user@gmail.com"
            validator: "email"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-validator.png
        :align: center

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: python

                from kivy.lang import Builder

                from kivymd.app import MDApp

                KV = '''
                MDScreen:

                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "20dp"
                        adaptive_height: True
                        size_hint_x: .8
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MDTextField:
                            hint_text: "Date dd/mm/yyyy without limits"
                            helper_text: "Enter a valid dd/mm/yyyy date"
                            validator: "date"
                            date_format: "dd/mm/yyyy"

                        MDTextField:
                            hint_text: "Date mm/dd/yyyy without limits"
                            helper_text: "Enter a valid mm/dd/yyyy date"
                            validator: "date"
                            date_format: "mm/dd/yyyy"

                        MDTextField:
                            hint_text: "Date yyyy/mm/dd without limits"
                            helper_text: "Enter a valid yyyy/mm/dd date"
                            validator: "date"
                            date_format: "yyyy/mm/dd"

                        MDTextField:
                            hint_text: "Date dd/mm/yyyy in [01/01/1900, 01/01/2100] interval"
                            helper_text: "Enter a valid dd/mm/yyyy date"
                            validator: "date"
                            date_format: "dd/mm/yyyy"
                            date_interval: "01/01/1900", "01/01/2100"

                        MDTextField:
                            hint_text: "Date dd/mm/yyyy in [01/01/1900, None] interval"
                            helper_text: "Enter a valid dd/mm/yyyy date"
                            validator: "date"
                            date_format: "dd/mm/yyyy"
                            date_interval: "01/01/1900", None

                        MDTextField:
                            hint_text: "Date dd/mm/yyyy in [None, 01/01/2100] interval"
                            helper_text: "Enter a valid dd/mm/yyyy date"
                            validator: "date"
                            date_format: "dd/mm/yyyy"
                            date_interval: None, "01/01/2100"
                '''


                class Test(MDApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_palette = "Orange"
                        return Builder.load_string(KV)


                Test().run()

        .. tab:: Declarative python style

            .. code-block:: python

                from kivymd.app import MDApp
                from kivymd.uix.boxlayout import MDBoxLayout
                from kivymd.uix.screen import MDScreen
                from kivymd.uix.textfield import MDTextField


                class Test(MDApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_palette = "Orange"
                        return (
                            MDScreen(
                                MDBoxLayout(
                                    MDTextField(
                                        hint_text="Date dd/mm/yyyy without limits",
                                        helper_text="Enter a valid dd/mm/yyyy date",
                                        validator="date",
                                        date_format="dd/mm/yyyy",
                                    ),
                                    MDTextField(
                                        hint_text="Date mm/dd/yyyy without limits",
                                        helper_text="Enter a valid mm/dd/yyyy date",
                                        validator="date",
                                        date_format="mm/dd/yyyy",
                                    ),
                                    MDTextField(
                                        hint_text="Date yyyy/mm/dd without limits",
                                        helper_text="Enter a valid yyyy/mm/dd date",
                                        validator="date",
                                        date_format="yyyy/mm/dd",
                                    ),
                                    MDTextField(
                                        hint_text="Date dd/mm/yyyy in [01/01/1900, 01/01/2100] interval",
                                        helper_text="Enter a valid dd/mm/yyyy date",
                                        validator="date",
                                        date_format="dd/mm/yyyy",
                                        date_interval=["01/01/1900", "01/01/2100"],
                                    ),
                                    MDTextField(
                                        hint_text="Date dd/mm/yyyy in [01/01/1900, None] interval",
                                        helper_text="Enter a valid dd/mm/yyyy date",
                                        validator="date",
                                        date_format="dd/mm/yyyy",
                                        date_interval=["01/01/1900", None],
                                    ),
                                    MDTextField(
                                        hint_text="Date dd/mm/yyyy in [None, 01/01/2100] interval",
                                        helper_text="Enter a valid dd/mm/yyyy date",
                                        validator="date",
                                        date_format="dd/mm/yyyy",
                                        date_interval=[None, "01/01/2100"],
                                    ),
                                    orientation="vertical",
                                    spacing="20dp",
                                    adaptive_height=True,
                                    size_hint_x=0.8,
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                )
                            )
                        )


                Test().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-validator-date.png
        :align: center

    :attr:`validator` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    line_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Line color normal (static underline line) in (r, g, b, a) or string format.

    .. code-block:: kv

        MDTextField:
            hint_text: "line_color_normal"
            line_color_normal: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-line-color-normal.png
        :align: center

    :attr:`line_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    line_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Line color focus (active underline line) in (r, g, b, a) or string format.

    .. code-block:: kv

        MDTextField:
            hint_text: "line_color_focus"
            line_color_focus: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-line-color-focus.gif
        :align: center

    :attr:`line_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    line_anim = BooleanProperty(True)
    """
    If True, then text field shows animated underline when on focus.

    :attr:`line_anim` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    error_color = ColorProperty([0, 0, 0, 0])
    """
    Error color in (r, g, b, a) or string format for ``required = True``.

    :attr:`error_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    fill_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Fill background color in (r, g, b, a) or string format in 'fill' mode when]
    text field is out of focus.

    .. code=block:: kv

        MDTextField:
            hint_text: "Fill mode"
            mode: "fill"
            fill_color_normal: "brown"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-fill-color-normal.png
        :align: center

    :attr:`fill_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    fill_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Fill background color in (r, g, b, a) or string format in 'fill' mode when
    the text field has focus.

    .. code=block:: kv

        MDTextField:
            hint_text: "Fill mode"
            mode: "fill"
            fill_color_focus: "brown"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-fill-color-focus.gif
        :align: center

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

    hint_text_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Hint text color in (r, g, b, a) or string format when text field is out
    of focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            hint_text: "hint_text_color_normal"
            hint_text_color_normal: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-hint-text-color-normal.png
        :align: center

    :attr:`hint_text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    hint_text_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Hint text color in (r, g, b, a) or string format when the text field has
    focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            hint_text: "hint_text_color_focus"
            hint_text_color_focus: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-hint-text-color-focus.gif
        :align: center

    :attr:`hint_text_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    helper_text_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Helper text color in (r, g, b, a) or string format when text field is out
    of focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            helper_text: "helper_text_color_normal"
            helper_text_mode: "persistent"
            helper_text_color_normal: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-helper-text-color-normal.png
        :align: center

    :attr:`helper_text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    helper_text_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Helper text color in (r, g, b, a) or string format when the text field has
    focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            helper_text: "helper_text_color_focus"
            helper_text_mode: "persistent"
            helper_text_color_focus: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-helper-text-color-focus.gif
        :align: center

    :attr:`helper_text_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    icon_right_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Color in (r, g, b, a) or string format of right icon when text field is out
    of focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            icon_right: "language-python"
            hint_text: "icon_right_color_normal"
            icon_right_color_normal: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-icon-right-color-normal.png
        :align: center

    :attr:`icon_right_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    icon_right_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Color in (r, g, b, a) or string format of right icon  when the text field
    has focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            icon_right: "language-python"
            hint_text: "icon_right_color_focus"
            icon_right_color_focus: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-icon-right-color-focus.gif
        :align: center

    :attr:`icon_right_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    icon_left_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Color in (r, g, b, a) or string format of right icon when text field is out
    of focus.

    .. versionadded:: 1.0.0

    :attr:`icon_left_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    icon_left_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Color in (r, g, b, a) or string format of right icon  when the text field
    has focus.

    .. versionadded:: 1.0.0

    :attr:`icon_left_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    max_length_text_color = ColorProperty([0, 0, 0, 0])
    """
    Text color in (r, g, b, a) or string format of the maximum length of
    characters to be input.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            hint_text: "max_length_text_color"
            max_length_text_color: "red"
            max_text_length: 5

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-max-length-text-color.png
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

    text_color_normal = ColorProperty([0, 0, 0, 0])
    """
    Text color in (r, g, b, a) or string format when text field is out of focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            hint_text: "text_color_normal"
            text_color_normal: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-text-color-normal.png
        :align: center

    :attr:`text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    text_color_focus = ColorProperty([0, 0, 0, 0])
    """
    Text color in (r, g, b, a) or string format when text field has focus.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTextField:
            hint_text: "text_color_focus"
            text_color_focus: "red"

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

    # Text to restore the text of the tale after clearing the text field.
    __hint_text = StringProperty()
    # List of color attribute names that should be updated when changing the
    # application color palette.
    _colors_to_updated = ListProperty()

    def __init__(self, *args, **kwargs):
        self.set_objects_labels()
        Clock.schedule_once(self._set_attr_names_to_updated)
        Clock.schedule_once(self.set_colors_to_updated)
        Clock.schedule_once(self.set_default_colors)
        super().__init__(*args, **kwargs)
        self.bind(
            _hint_text_font_size=self._hint_text_label.setter("font_size"),
            _icon_right_color=self._icon_right_label.setter("text_color"),
            _icon_left_color=self._icon_left_label.setter("text_color"),
            text=self.set_text,
        )
        self.theme_cls.bind(
            primary_color=self.set_default_colors,
            theme_style=self.set_default_colors,
        )
        Clock.schedule_once(self.check_text)

    # TODO: Is this method necessary?
    #  During testing, a quick double-click on the text box does not stop
    #  the animation of the hint text height.
    def cancel_all_animations_on_double_click(self) -> None:
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

    def set_colors_to_updated(self, interval: Union[float, int]) -> None:
        for attr_name in self._attr_names_to_updated.keys():
            if getattr(self, attr_name) == [0, 0, 0, 0]:
                self._colors_to_updated.append(attr_name)

    def set_default_colors(
        self, interval: Union[float, int], updated: bool = False
    ) -> None:
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
            self.error_color = (
                self.theme_cls.error_color
                if self.error_color == [0, 0, 0, 0]
                else self.error_color
            )
        if self.max_length_text_color == [0, 0, 0, 0] or updated:
            self.max_length_text_color = (
                self.theme_cls.disabled_hint_text_color
                if self.max_length_text_color == [0, 0, 0, 0]
                else self.max_length_text_color
            )

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

    def set_notch_rectangle(self, joining: bool = False) -> None:
        """
        Animates a notch for the hint text in the rectangle of the text field
        of type `rectangle`.
        """

        def on_progress(*args):
            self._line_blank_space_right_point = (
                self._hint_text_label.width + dp(17) if not joining else 0
            )

        if self.hint_text:
            animation = Animation(
                _line_blank_space_left_point=self._hint_text_label.x - dp(-7)
                if not joining
                else 0,
                duration=0.2,
                t="out_quad",
            )
            animation.bind(on_progress=on_progress)
            animation.start(self)

    def set_active_underline_width(self, width: Union[float, int]) -> None:
        """Animates the width of the active underline line."""

        Animation(
            _underline_width=width,
            duration=(0.2 if self.line_anim else 0),
            t="out_quad",
        ).start(self)

    def set_static_underline_color(self, color: list) -> None:
        """Animates the color of a static underline line."""

        Animation(
            _line_color_normal=color,
            duration=(0.2 if self.line_anim else 0),
            t="out_quad",
        ).start(self)

    def set_active_underline_color(self, color: list) -> None:
        """Animates the fill color for 'fill' mode."""

        Animation(_line_color_focus=color, duration=0.2, t="out_quad").start(
            self
        )

    def set_fill_color(self, color: list) -> None:
        """Animates the color of the hint text."""

        Animation(_fill_color=color, duration=0.2, t="out_quad").start(self)

    def set_helper_text_color(self, color: list) -> None:
        """Animates the color of the hint text."""

        Animation(_helper_text_color=color, duration=0.2, t="out_quad").start(
            self
        )

    def set_max_length_text_color(self, color: list) -> None:
        """Animates the color of the max length text."""

        Animation(
            _max_length_text_color=color, duration=0.2, t="out_quad"
        ).start(self)

    def set_icon_right_color(self, color: list) -> None:
        """Animates the color of the icon right."""

        Animation(_icon_right_color=color, duration=0.2, t="out_quad").start(
            self
        )

    def set_icon_left_color(self, color: list) -> None:
        """Animates the color of the icon left."""

        Animation(_icon_left_color=color, duration=0.2, t="out_quad").start(
            self
        )

    def set_hint_text_color(self, focus: bool, error: bool = False) -> None:
        """Animates the color of the hint text."""

        if self.mode != "round":
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

    def set_pos_hint_text(self, y: float, x: float = 12) -> None:
        """Animates the x-axis width and y-axis height of the hint text."""

        if self.mode != "round":
            Animation(_hint_y=y, duration=0.2, t="out_quad").start(self)
            if self.mode == "rectangle":
                if not self.icon_left:
                    _hint_x = x
                else:
                    if y == dp(10):
                        _hint_x = dp(-4)
                    else:
                        _hint_x = dp(20)

                Animation(
                    _hint_x=_hint_x,
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

    def set_hint_text_font_size(self, font_size: float) -> None:
        """Animates the font size of the hint text."""

        if self.mode != "round":
            Animation(
                _hint_text_font_size=font_size, duration=0.2, t="out_quad"
            ).start(self)

    def set_max_text_length(self) -> None:
        """Called when text is entered into a text field."""

        if self.max_text_length:
            self._max_length_label.text = (
                f"{len(self.text)}/{self.max_text_length}"
            )

    def check_text(self, interval: Union[float, int]) -> None:
        self.set_text(self, self.text)

    def set_text(self, instance_text_field, text: str) -> None:
        """Called when text is entered into a text field."""

        self.text = re.sub("\n", " ", text) if not self.multiline else text
        self.set_max_text_length()
        if self.validator and self.validator == "phone":
            pass
            # self.format(self.text)

        if (self.text and self.max_length_text_color) or self._get_has_error():
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

        if not self.text and not self.focus:
            self.on_focus(instance_text_field, False)

        if self.mode == "round" and self.text:
            self.hint_text = ""
        if self.mode == "round" and not self.text:
            self.hint_text = self.__hint_text

    def set_x_pos(self):
        pass

    def set_objects_labels(self) -> None:
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

    def on_helper_text(self, instance_text_field, helper_text: str) -> None:
        self._helper_text_label.text = helper_text

    def on_focus(self, instance_text_field, focus: bool) -> None:
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
                if self.mode == "rectangle":
                    y = dp(38)
                elif self.mode == "fill":
                    y = dp(46)
                else:
                    y = dp(34)

                self.set_pos_hint_text(y)
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

    def on_icon_left(self, instance_text_field, icon_name: str) -> None:
        self._icon_left_label.icon = icon_name

    def on_icon_right(self, instance_text_field, icon_name: str) -> None:
        self._icon_right_label.icon = icon_name

    def on_disabled(self, instance_text_field, disabled_value: bool) -> None:
        pass

    def on_error(self, instance_text_field, error: bool) -> None:
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
            self.set_active_underline_color(self.line_color_focus)
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

    def on_hint_text(self, instance_text_field, hint_text: str) -> None:
        if hint_text:
            self.__hint_text = hint_text
        self._hint_text_label.text = hint_text
        self._hint_text_label.font_size = sp(16)

    def on_width(self, instance_text_field, width: float) -> None:
        """Called when the application window is resized."""

        if self.focus:
            self._underline_width = self.width

    def on_height(self, instance_text_field, value_height: float) -> None:
        if value_height >= self.max_height and self.max_height:
            self.height = self.max_height

    def on_text_color_normal(
        self, instance_text_field, color: Union[list, str]
    ):
        self._text_color_normal = color

    def on_hint_text_color_normal(
        self, instance_text_field, color: Union[list, str]
    ):
        self._hint_text_color = color

    def on_helper_text_color_normal(
        self, instance_text_field, color: Union[list, str]
    ):
        self._helper_text_color = color

    def on_icon_right_color_normal(
        self, instance_text_field, color: Union[list, str]
    ):
        self._icon_right_color = color

    def on_line_color_normal(
        self, instance_text_field, color: Union[list, str]
    ):
        self._line_color_normal = color

    def on_max_length_text_color(
        self, instance_text_field, color: Union[list, str]
    ):
        self._max_length_text_color = color

    def _set_color(self, attr_name: str, color: str, updated: bool) -> None:
        if attr_name in self._colors_to_updated or updated:
            if attr_name in self._colors_to_updated:
                setattr(self, attr_name, color)

    def _set_attr_names_to_updated(self, interval: Union[float, int]) -> None:
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

        if self.validator and self.validator != "phone":
            has_error = {
                "date": self.is_date_valid,
                "email": self.is_email_valid,
                "time": self.is_time_valid,
            }[self.validator](self.text)
            return has_error
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


if __name__ == "__main__":
    from kivy.core.window import Window
    from kivy.lang import Builder
    from kivy.uix.textinput import TextInput

    Window.size = (800, 750)

    from kivymd.app import MDApp

    KV = """
MDScreen:

    MDBoxLayout:
        id: box
        orientation: "vertical"
        spacing: "20dp"
        adaptive_height: True
        size_hint_x: .8
        pos_hint: {"center_x": .5, "center_y": .5}

        MDTextField:
            hint_text: "Label"
            helper_text: "Error message"
            mode: "rectangle"
            max_text_length: 5

        MDTextField:
            icon_left: "git"
            hint_text: "Label"
            helper_text: "Error message"
            mode: "rectangle"

        MDTextField:
            icon_left: "git"
            hint_text: "Label"
            helper_text: "Error message"
            mode: "fill"

        MDTextField:
            hint_text: "Label"
            helper_text: "Error message"
            mode: "fill"

        MDTextField:
            hint_text: "Label"
            helper_text: "Error message"

        MDTextField:
            icon_left: "git"
            hint_text: "Label"
            helper_text: "Error message"

        MDTextField:
            hint_text: "Round mode"
            mode: "round"
            max_text_length: 15
            helper_text: "Message"

        MDTextField:
            hint_text: "Date dd/mm/yyyy in [01/01/1900, 01/01/2100] interval"
            helper_text: "Enter a valid dd/mm/yyyy date"
            validator: "date"
            date_format: "dd/mm/yyyy"
            date_interval: "01/01/1900", "01/01/2100"

        MDTextField:
            hint_text: "Email"
            helper_text: "user@gmail.com"
            validator: "email"

        MDFlatButton:
            text: "SET TEXT"
            pos_hint: {"center_x": .5}
            on_release: app.set_text()
"""

    class Test(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return Builder.load_string(KV)

        def set_text(self):
            for widget in self.root.ids.box.children:
                if issubclass(widget.__class__, TextInput):
                    widget.text = "Input text"

    Test().run()
