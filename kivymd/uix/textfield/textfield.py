"""
Components/Text fields
======================

.. seealso::

    `Material Design spec, Text fields <https://m3.material.io/components/text-fields/specs>`_

.. rubric:: Text fields let users enter text into a UI.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields.png
    :align: center

- Make sure text fields look interactive
- Two types: filled and outlined
- The text field’s state (blank, with input, error, etc) should be visible at a glance
- Keep labels and error messages brief and easy to act on
- Text fields commonly appear in forms and dialogs

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/available-fields.png
    :align: center

1. Filled text field
2. Outlined text field

Usage
-----

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDTextField:
                mode: "filled"

                MDTextFieldLeadingIcon:
                    icon: "magnify"

                MDTextFieldHintText:
                    text: "Hint text"

                MDTextFieldHelperText:
                    text: "Helper text"
                    mode: "persistent"

                MDTextFieldTrailingIcon:
                    icon: "information"

                MDTextFieldMaxLengthText:
                    max_text_length: 10

    .. tab:: Declarative Python style

        .. code-block:: python

            MDTextField(
                MDTextFieldLeadingIcon(
                    icon="magnify",
                ),
                MDTextFieldHintText(
                    text="Hint text",
                ),
                MDTextFieldHelperText(
                    text="Helper text",
                    mode="persistent",
                ),
                MDTextFieldTrailingIcon(
                    icon="information",
                ),
                MDTextFieldMaxLengthText(
                    max_text_length=10,
                ),
                mode="filled",
            )

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-anatomy.png
    :align: center

Available types of text fields
==============================

Filled mode
-----------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDTextField:
                mode: "filled"

    .. tab:: Declarative Python style

        .. code-block:: python

            MDTextField(
                mode="filled",
            )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-filled-mode.png
    :align: center

Outlined mode
-------------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDTextField:
                mode: "outlined"

    .. tab:: Declarative Python style

        .. code-block:: python

            MDTextField(
                mode="outlined",
            )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-outlined-mode.png
    :align: center

Example
-------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: app.theme_cls.backgroundColor

                MDTextField:
                    mode: "outlined"
                    size_hint_x: None
                    width: "240dp"
                    pos_hint: {"center_x": .5, "center_y": .5}

                    MDTextFieldLeadingIcon:
                        icon: "account"

                    MDTextFieldHintText:
                        text: "Outlined"

                    MDTextFieldHelperText:
                        text: "Helper text"
                        mode: "persistent"

                    MDTextFieldTrailingIcon:
                        icon: "information"

                    MDTextFieldMaxLengthText:
                        max_text_length: 10
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivymd.uix.textfield import (
                MDTextField,
                MDTextFieldLeadingIcon,
                MDTextFieldHintText,
                MDTextFieldHelperText,
                MDTextFieldTrailingIcon,
                MDTextFieldMaxLengthText,
            )

            from kivymd.uix.screen import MDScreen
            from kivymd.app import MDApp


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return MDScreen(
                        MDTextField(
                            MDTextFieldLeadingIcon(
                                icon="account",
                            ),
                            MDTextFieldHintText(
                                text="Hint text",
                            ),
                            MDTextFieldHelperText(
                                text="Helper text",
                                mode="persistent",
                            ),
                            MDTextFieldTrailingIcon(
                                icon="information",
                            ),
                            MDTextFieldMaxLengthText(
                                max_text_length=10,
                            ),
                            mode="outlined",
                            size_hint_x=None,
                            width="240dp",
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                        ),
                        md_bg_color=self.theme_cls.backgroundColor,
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-example.png
    :align: center

API break
=========

1.2.0 version
-------------

.. code-block:: kv

    MDTextField:
        mode: "rectangle"
        hint_text: "Hint text"
        helper_text: "Helper text"
        helper_text_mode: "persistent"
        max_text_length: 10
        icon_right: "information"

2.0.0 version
-------------

.. note:: The text field with the `round` type was removed in version `2.0.0`.

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDTextField:
                mode: "outlined"

                MDTextFieldLeadingIcon:
                    icon: "phone"

                MDTextFieldTrailingIcon:
                    icon: "information"

                MDTextFieldHintText:
                    text: "Hint text"

                MDTextFieldHelperText:
                    text: "Helper text"
                    mode: "persistent"

                MDTextFieldMaxLengthText:
                    max_text_length: 10

    .. tab:: Declarative Python style

        .. code-block:: python

            MDTextField(
                MDTextFieldLeadingIcon(
                    icon="magnify",
                ),
                MDTextFieldHintText(
                    text="Hint text",
                ),
                MDTextFieldHelperText(
                    text="Helper text",
                    mode="persistent",
                ),
                MDTextFieldTrailingIcon(
                    icon="information",
                ),
                MDTextFieldMaxLengthText(
                    max_text_length=10,
                ),
            )
"""

from __future__ import annotations

__all__ = (
    "BaseTextFieldIcon",
    "BaseTextFieldLabel",
    "Validator",
    "AutoFormatTelephoneNumber",
    "MDTextField",
    "MDTextFieldHelperText",
    "MDTextFieldMaxLengthText",
    "MDTextFieldHintText",
    "MDTextFieldLeadingIcon",
    "MDTextFieldTrailingIcon",
)

import os
import re
from datetime import date

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.textinput import TextInput

from kivymd import uix_path
from kivymd.font_definitions import theme_font_styles
from kivymd.theming import ThemableBehavior, ThemeManager
from kivymd.uix.behaviors import BackgroundColorBehavior, DeclarativeBehavior
from kivymd.uix.behaviors.state_layer_behavior import StateLayerBehavior
from kivymd.uix.label import MDIcon, MDLabel

with open(
    os.path.join(uix_path, "textfield", "textfield.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


# TODO: Add a class to work with the phone number mask.


class AutoFormatTelephoneNumber:
    """
    Implements automatic formatting of the text entered in the text field
    according to the mask, for example '+38 (###) ### ## ##'.

    .. warning:: This class has not yet been implemented and it is not
        recommended to use it yet.
    """

    def __init__(self):
        self._backspace = False

    def isnumeric(self, value) -> bool:
        try:
            int(value)
            return True
        except ValueError:
            return False

    def do_backspace(self, *args) -> None:
        """Do backspace operation from the current cursor position."""

        if self.validator and self.validator == "phone":
            self._backspace = True
            text = self.text
            text = text[:-1]
            self.text = text
            self._backspace = False

    def field_filter(self, value, boolean) -> None:
        if self.validator and self.validator == "phone":
            if len(self.text) == 14:
                return
            if self.isnumeric(value):
                return value
        return value

    def format(self, value) -> None:
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
        """Checks the validity of the email."""

        if not re.match(r"[^@]+@[^@]+\.[^@]+", text):
            return True
        return False

    def is_time_valid(self, text: str) -> bool:
        """Checks the validity of the time."""

        if re.match(r"^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$", text) or re.match(
            r"^(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])$", text
        ):
            return False

        return True

    def is_date_valid(self, text: str) -> bool:
        """Checks the validity of the date."""

        if not self.date_format:
            raise Exception("TextInput date_format was not defined.")

        # Regex strings.
        dd = "[0][1-9]|[1-2][0-9]|[3][0-1]"
        mm = "[0][1-9]|[1][0-2]"
        yyyy = "[0-9][0-9][0-9][0-9]"
        fmt = self.date_format.split("/")
        args = locals()
        # Access  the local variables  dict in the correct format based on
        # date_format split. Example: "mm/dd/yyyy" -> ["mm", "dd", "yyyy"]
        # args[fmt[0]] would be args["mm"] so the month regex string.
        if re.match(
            f"^({args[fmt[0]]})/({args[fmt[1]]})/({args[fmt[2]]})$", text
        ):
            input_split = text.split("/")
            args[fmt[0]] = input_split[0]
            args[fmt[1]] = input_split[1]
            args[fmt[2]] = input_split[2]
            # Organize input  into correct slots and try to convert
            # to datetime  object. This way February exceptions are
            # tested. Also tests with the date_interval are simpler
            # using datetime objects.
            try:
                datetime = date(
                    int(args["yyyy"]), int(args["mm"]), int(args["dd"])
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
            args = {}
            # Convert string inputs into datetime.date objects and store
            # them back into self.date_interval.
            try:
                if self.date_interval[0] and not isinstance(
                    self.date_interval[0], date
                ):
                    split = self.date_interval[0].split("/")
                    args[fmt[0]] = split[0]
                    args[fmt[1]] = split[1]
                    args[fmt[2]] = split[2]
                    self.date_interval[0] = date(
                        int(args["yyyy"]), int(args["mm"]), int(args["dd"])
                    )
                if self.date_interval[1] and not isinstance(
                    self.date_interval[1], date
                ):
                    split = self.date_interval[1].split("/")
                    args[fmt[0]] = split[0]
                    args[fmt[1]] = split[1]
                    args[fmt[2]] = split[2]
                    self.date_interval[1] = date(
                        int(args["yyyy"]), int(args["mm"]), int(args["dd"])
                    )

            except Exception:
                raise Exception(
                    r"TextInput date_interval was defined incorrectly, "
                    r"it must be composed of <class 'datetime.date'> objects "
                    r"or strings following current date_format."
                )

            # Test if the interval is valid.
            if isinstance(self.date_interval[0], date) and isinstance(
                self.date_interval[1], date
            ):
                if self.date_interval[0] >= self.date_interval[1]:
                    raise Exception(
                        "TextInput date_interval last date must be greater "
                        "than the first date or set to None."
                    )

        Clock.schedule_once(lambda x: on_date_interval())


class BaseTextFieldLabel(MDLabel):
    """
    Base texture for :class:`~MDTextField` class (helper text, max length,
    hint text).

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.

    .. versionadded:: 2.0.0
    """

    text_color_normal = ColorProperty(None)
    """
    Text color in (r, g, b, a) or string format when text field is out
    of focus.

    .. versionadded:: 1.0.0

    .. versionchanged:: 2.0.0
        The property was moved from class:`~MDTextField` class and renamed
        from `helper_text_color_normal` to `text_color_normal`.

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"
        
                    MDTextFieldHintText:
                        text: "Hint text color normal"
                        text_color_normal: "brown"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldHintText(
                        text="Hint text color normal",
                        text_color_normal="brown",
                    ),
                    mode="filled",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-text-color-normal.png
        :align: center

    :attr:`text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_color_focus = ColorProperty(None)
    """
    Text color in (r, g, b, a) or string format when the text field has
    focus.

    .. versionadded:: 1.0.0

    .. versionchanged:: 2.0.0
        The property was moved from class:`~MDTextField` class and renamed
        from `helper_text_color_focus` to `text_color_focus`.

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:

                    MDTextFieldHelperText:
                        text: "Helper text color focus"
                        text_color_focus: "brown"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldHelperText(
                        text="Helper text color focus",
                        text_color_normal="brown",
                    ),
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-text-color-focus.png
        :align: center

    :attr:`text_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """


class MDTextFieldHelperText(BaseTextFieldLabel):
    """
    Implements the helper text label.

    For more information, see in the :class:`~BaseTextFieldLabel`
    class documentation.

    .. versionadded:: 2.0.0
    """

    mode = OptionProperty(
        "on_focus", options=["on_error", "persistent", "on_focus"]
    )
    """
    Helper text mode. Available options are: `'on_error'`, `'persistent'`,
    `'on_focus'`.

    .. versionchanged:: 2.0.0
        The property was moved from class:`~MDTextField` class and renamed
        from `helper_text_mode` to `mode`.

    On focus
    --------

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"

                    MDTextFieldHelperText:
                        text: "Helper text"
                        mode: "on_focus"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldHelperText(
                        text="Helper text",
                        mode="on_focus",
                    ),
                    mode="filled",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-helper-text-mode-on-focus.gif
        :align: center

    On error
    --------

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"

                    MDTextFieldHelperText:
                        text: "Helper text"
                        mode: "on_error"

                    MDTextFieldMaxLengthText:
                        max_text_length: 5

        .. tab:: Declarative Python style
    
            .. code-block:: python

                MDTextField(
                    MDTextFieldHelperText(
                        text="Helper text",
                        mode="on_error",
                    ),
                    MDTextFieldMaxLengthText(
                        max_text_length=5,
                    ),
                    mode="filled",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-helper-text-mode-on-error.gif
        :align: center

    Persistent
    ----------

    .. tabs::
    
        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"

                    MDTextFieldHelperText:
                        text: "Helper text"
                        mode: "persistent"

        .. tab:: Declarative Python style
    
            .. code-block:: python

                MDTextField(
                    MDTextFieldHelperText(
                        text="Helper text",
                        mode="persistent",
                    ),
                    mode="filled",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-helper-text-mode-persistent.gif
        :align: center

    :attr:`mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'on_focus'`.
    """


class MDTextFieldMaxLengthText(BaseTextFieldLabel):
    """
    Implements the max length text label.

    For more information, see in the :class:`~BaseTextFieldLabel`
    class documentation.

    .. versionadded:: 2.0.0
    """

    max_text_length = NumericProperty(None)
    """
    Maximum allowed value of characters in a text field.

    .. versionchanged:: 2.0.0
        The property was moved from class:`~MDTextField`.

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"

                    MDTextFieldMaxLengthText:
                        max_text_length: 10

        .. tab:: Declarative Python style
    
            .. code-block:: python

                MDTextField(
                    MDTextFieldMaxLengthText(
                        max_text_length=10,
                    ),
                    mode="filled",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-max-text-length.png
        :align: center

    :attr:`max_text_length` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """


class MDTextFieldHintText(BaseTextFieldLabel):
    """
    Implements the hint text label.

    For more information, see in the :class:`~BaseTextFieldLabel`
    class documentation.

    .. versionadded:: 2.0.0

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"

                    MDTextFieldHintText:
                        text: "Hint text"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldHintText(
                        text="Hint text",
                    ),
                    mode="filled",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-hint-text.gif
        :align: center
    """


class BaseTextFieldIcon(MDIcon):
    """
    Base texture for :class:`~MDTextField` class (helper text, max length,
    hint text).

    For more information, see in the :class:`~kivymd.uix.label.label.MDIcon`
    class documentation.

    .. versionchanged:: 2.0.0
    """

    icon_color_normal = ColorProperty(None)
    """
    Icon color in (r, g, b, a) or string format when text field is out
    of focus.

    .. versionadded:: 1.0.0

    .. versionchanged:: 2.0.0
        The property was moved from class:`~MDTextField` class and renamed
        from `icon_right_color_normal/icon_left_color_normal`
        to `icon_color_normal`.

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"

                    MDTextFieldLeadingIcon:
                        icon: "phone"
                        theme_icon_color: "Custom"
                        icon_color_normal: "lightgreen"

                    MDTextFieldHintText:
                        text: "Leading icon color normal"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldLeadingIcon(
                        icon="phone",
                        theme_icon_color="Custom",
                        icon_color_normal="lightgreen",
                    ),
                    MDTextFieldHintText(
                        text="Leading icon color normal",
                    ),
                    mode="filled",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-leading-icon-color-normal.png
        :align: center

    :attr:`icon_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color_focus = ColorProperty(None)
    """
    Icon color in (r, g, b, a) or string format when the text field has
    focus.

    .. versionadded:: 1.0.0

    .. versionchanged:: 2.0.0
        The property was moved from class:`~MDTextField` class and renamed
        from `icon_right_color_focus/icon_left_color_focus `
        to `icon_color_focus`.

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"

                    MDTextFieldLeadingIcon:
                        icon: "phone"
                        theme_icon_color: "Custom"
                        icon_color_focus: "lightgreen"

                    MDTextFieldHintText:
                        text: "Leading icon color focus"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldLeadingIcon(
                        icon="phone",
                        theme_icon_color="Custom",
                        icon_color_focus="lightgreen",
                    ),
                    MDTextFieldHintText(
                        text="Leading icon color focus",
                    ),
                    mode="filled",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-leading-icon-color-focus.png
        :align: center

    :attr:`icon_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # kivymd.uix.textfield.textfield.MDTextField object.
    _text_field = ObjectProperty(None)

    def on_icon_color_normal(
        self,
        instance: BaseTextFieldIcon | MDTextFieldTrailingIcon,
        value: list | str,
    ):
        """
        Called when the `icon_color_normal` property of the icon is changed.

        If the associated text field is set, this method triggers an update
        to the icon's color appearance, ensuring that the correct color is
        used based on the focus state of the text field.

        Typically used to visually reflect property changes in real time
        in response to user interaction or theme updates.

        :param instance: The instance of `BaseTextFieldIcon` that had its
                         `icon_color_normal` property changed.
        :param value: The new color value, either as a list of RGBA components
                      or a string (e.g., a hex color or color name).
        """

        if self._text_field and not self._text_field.disabled:
            update_color_method = {
                MDTextFieldLeadingIcon: self._text_field._set_texture_leading_icons_color,
                MDTextFieldTrailingIcon: self._text_field._set_texture_trailing_icons_color,
            }.get(type(instance))

            if update_color_method:
                update_color_method(icon_color_focus=self._text_field.focus)


class MDTextFieldLeadingIcon(BaseTextFieldIcon):
    """
    Implements the leading icon.

    For more information, see in the :class:`~BaseTextFieldIcon`
    class documentation.

    .. versionadded:: 2.0.0

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"

                    MDTextFieldLeadingIcon:
                        icon: "phone"

                    MDTextFieldHintText:
                        text: "Field with leading icon"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldLeadingIcon(
                        icon="phone",
                    ),
                    MDTextFieldHintText(
                        text="Field with leading icon",
                    ),
                    mode="filled",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-leading-icon.png
        :align: center
    """


class MDTextFieldTrailingIcon(BaseTextFieldIcon):
    """
    Implements the trailing icon.

    For more information, see in the :class:`~BaseTextFieldIcon`
    class documentation.

    .. versionadded:: 2.0.0

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"

                    MDTextFieldTrailingIcon:
                        icon: "phone"

                    MDTextFieldHintText:
                        text: "Field with trailing icon"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldTrailingIcon(
                        icon="phone",
                    ),
                    MDTextFieldHintText(
                        text="Field with trailing icon",
                    ),
                    mode="filled",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-trailing-icon.png
        :align: center
    """


# TODO: Add a custom color for the disabled state of the text field.
class MDTextField(
    DeclarativeBehavior,
    StateLayerBehavior,
    ThemableBehavior,
    TextInput,
    Validator,
    AutoFormatTelephoneNumber,
    BackgroundColorBehavior,
):
    """
    Textfield class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.textinput.TextInput` and
    :class:`~Validator` and
    :class:`~AutoFormatTelephoneNumber` and
    :class:`~kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior`
    classes documentation.
    """

    font_style = StringProperty("Body")
    """
    Name of the style for the input text.

    .. versionadded:: 2.0.0

    .. seealso::

        `Font style names <https://kivymd.readthedocs.io/en/latest/components/label/#all-styles>`_

    :attr:`font_style` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Body'`.
    """

    role = StringProperty("large")
    """
    Role of font style.

    .. versionadded:: 2.0.0

    .. seealso::

        `Font style roles <https://kivymd.readthedocs.io/en/latest/components/label/#all-styles>`_

    :attr:`role` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'large'`.
    """

    mode = OptionProperty("outlined", options=["outlined", "filled"])
    """
    Text field mode. Available options are: `'outlined'`, `'filled'`.

    :attr:`mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'outlined'`.
    """

    error_color = ColorProperty(None)
    """
    Error color in (r, g, b, a) or string format for `required = True`
    or when the text field is in `error` state.

    :attr:`error_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    error = BooleanProperty(False)
    """
    If True, then the text field goes into `error` mode.

    :attr:`error` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    text_color_normal = ColorProperty(None)
    """
    Text color in (r, g, b, a) or string format when text field is out of focus.

    .. versionadded:: 1.0.0

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    theme_text_color: "Custom"
                    text_color_normal: "green"
                    text: "Text color normal"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    theme_text_color="Custom",
                    text_color_normal="green",
                    text="Text color normal",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-text-color-normal.png
        :align: center

    :attr:`text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_color_focus = ColorProperty(None)
    """
    Text color in (r, g, b, a) or string format when text field has focus.

    .. versionadded:: 1.0.0

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    theme_text_color: "Custom"
                    text_color_focus: "green"
                    text: "Text color focus"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    theme_text_color="Custom",
                    text_color_focus="green",
                    text="Text color focus",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-field-text-color-focus.png
        :align: center

    :attr:`text_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    radius = VariableListProperty([dp(4), dp(4), dp(4), dp(4)])
    """
    The corner radius for a text field in `filled/outlined` mode.

    :attr:`radius` is a :class:`~kivy.properties.VariableListProperty` and
    defaults to `[dp(4), dp(4), 0, 0]`.
    """

    required = BooleanProperty(False)
    """
    Required text. If True then the text field requires text.

    :attr:`required` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    line_color_normal = ColorProperty(None)
    """
    Line color normal (active indicator) in (r, g, b, a) or string format.

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"
                    theme_line_color: "Custom"
                    line_color_normal: "green"

                    MDTextFieldHelperText:
                        text: "Line color normal"
                        mode: "persistent"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldHelperText(
                        text="Line color normal",
                        mode="persistent",
                    ),
                    mode="filled",
                    theme_line_color="Custom",
                    line_color_normal="green",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-line-color-normal.png
        :align: center

    :attr:`line_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    line_color_focus = ColorProperty(None)
    """
    Line color focus (active indicator) in (r, g, b, a) or string format.

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"
                    theme_line_color: "Custom"
                    line_color_focus: "green"

                    MDTextFieldHelperText:
                        text: "Line color focus"
                        mode: "persistent"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldHelperText(
                        text="Line color focus",
                        mode="persistent",
                    ),
                    mode="filled",
                    theme_line_color="Custom",
                    line_color_focus="green",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-line-color-focus.png
        :align: center

    :attr:`line_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    fill_color_normal = ColorProperty(None)
    """
    Fill background color in (r, g, b, a) or string format in 'fill' mode when]
    text field is out of focus.

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"
                    theme_bg_color: "Custom"
                    fill_color_normal: 0, 1, 0, .2

                    MDTextFieldHelperText:
                        text: "Fill color normal"
                        mode: "persistent"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldHelperText(
                        text="Fill color normal",
                        mode="persistent",
                    ),
                    mode="filled",
                    theme_bg_color="Custom",
                    fill_color_normal=[0, 1, 0, .2],
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-fill-color-normal.png
        :align: center

    :attr:`fill_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    fill_color_focus = ColorProperty(None)
    """
    Fill background color in (r, g, b, a) or string format in 'fill' mode when
    the text field has focus.

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"
                    theme_bg_color: "Custom"
                    fill_color_focus: 0, 1, 0, .2

                    MDTextFieldHelperText:
                        text: "Fill color focus"
                        mode: "persistent"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldHelperText(
                        text="Fill color focus",
                        mode="persistent",
                    ),
                    mode="filled",
                    theme_bg_color="Custom",
                    fill_color_focus=[0, 1, 0, .2],
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-fill-color-focus.png
        :align: center

    :attr:`fill_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # TODO: Add minimum allowed height. Otherwise, if the value is,
    #  for example, 20, the text field will simply be lessened.
    max_height = NumericProperty(0)
    """
    Maximum height of the text box when `multiline = True`.

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"
                    max_height: "200dp"
                    multiline: True

                    MDTextFieldHelperText:
                        text: "multiline=True"
                        mode: "persistent"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldHelperText(
                        text="multiline=True",
                        mode="persistent",
                    ),
                    mode="filled",
                    max_height="200dp",
                    multiline=True,
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-multiline.gif
        :align: center

    :attr:`max_height` is a :class:`~kivy.properties.NumericProperty` and
    defaults to `0`.
    """

    phone_mask = StringProperty("")
    """
    This property has not yet been implemented and it is not recommended to
    use it yet.

    :attr:`phone_mask` is a :class:`~kivy.properties.StringProperty` and
    defaults to ''.
    """

    validator = OptionProperty(None, options=["date", "email", "time", "phone"])
    """
    The type of text field for entering Email, time, etc.
    Automatically sets the type of the text field as "error" if the user input
    does not match any of the set validation types.
    Available options are: `'date'`, `'email'`, `'time'`.

    When using `'date'`, :attr:`date_format` must be defined.

    .. versionadded:: 1.1.0

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: kv

                MDTextField:
                    mode: "filled"
                    validator: "email"

                    MDTextFieldHintText:
                        text: "Email"

                    MDTextFieldHelperText:
                        text: "user@gmail.com"
                        mode: "persistent"

        .. tab:: Declarative Python style

            .. code-block:: python

                MDTextField(
                    MDTextFieldHintText(
                        text="Email",
                    ),
                    MDTextFieldHelperText(
                        text="user@gmail.com",
                        mode="persistent",
                    ),
                    mode="filled",
                    validator="email",
                )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-email-validator.png
        :align: center

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: python

                from kivy.lang import Builder

                from kivymd.app import MDApp

                KV = '''
                MDScreen:
                    md_bg_color: self.theme_cls.backgroundColor

                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "28dp"
                        adaptive_height: True
                        size_hint_x: .8
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MDTextField:
                            validator: "date"
                            date_format: "dd/mm/yyyy"

                            MDTextFieldHintText:
                                text: "Date dd/mm/yyyy without limits"

                            MDTextFieldHelperText:
                                text: "Enter a valid dd/mm/yyyy date"

                        MDTextField:
                            validator: "date"
                            date_format: "mm/dd/yyyy"

                            MDTextFieldHintText:
                                text: "Date mm/dd/yyyy without limits"

                            MDTextFieldHelperText:
                                text: "Enter a valid mm/dd/yyyy date"

                        MDTextField:
                            validator: "date"
                            date_format: "yyyy/mm/dd"

                            MDTextFieldHintText:
                                text: "Date yyyy/mm/dd without limits"

                            MDTextFieldHelperText:
                                text: "Enter a valid yyyy/mm/dd date"

                        MDTextField:
                            validator: "date"
                            date_format: "dd/mm/yyyy"
                            date_interval: "01/01/1900", "01/01/2100"

                            MDTextFieldHintText:
                                text: "Date dd/mm/yyyy in [01/01/1900, 01/01/2100] interval"

                            MDTextFieldHelperText:
                                text: "Enter a valid dd/mm/yyyy date"

                        MDTextField:
                            validator: "date"
                            date_format: "dd/mm/yyyy"
                            date_interval: "01/01/1900", None

                            MDTextFieldHintText:
                                text: "Date dd/mm/yyyy in [01/01/1900, None] interval"

                            MDTextFieldHelperText:
                                text: "Enter a valid dd/mm/yyyy date"

                        MDTextField:
                            validator: "date"
                            date_format: "dd/mm/yyyy"
                            date_interval: None, "01/01/2100"

                            MDTextFieldHintText:
                                text: "Date dd/mm/yyyy in [None, 01/01/2100] interval"

                            MDTextFieldHelperText:
                                text: "Enter a valid dd/mm/yyyy date"
                '''


                class Example(MDApp):
                    def build(self):
                        self.theme_cls.primary_palette = "Olive"
                        return Builder.load_string(KV)


                Example().run()

        .. tab:: Declarative Python style

            .. code-block:: python

                from kivymd.app import MDApp
                from kivymd.uix.boxlayout import MDBoxLayout
                from kivymd.uix.screen import MDScreen
                from kivymd.uix.textfield import (
                    MDTextField, MDTextFieldHintText, MDTextFieldHelperText
                )


                class Example(MDApp):
                    def build(self):
                        self.theme_cls.primary_palette = "Olive"
                        return (
                            MDScreen(
                                MDBoxLayout(
                                    MDTextField(
                                        MDTextFieldHintText(
                                            text="Date dd/mm/yyyy without limits",
                                        ),
                                        MDTextFieldHelperText(
                                            text="Enter a valid dd/mm/yyyy date",
                                        ),
                                        validator="date",
                                        date_format="dd/mm/yyyy",
                                    ),
                                    MDTextField(
                                        MDTextFieldHintText(
                                            text="Date mm/dd/yyyy without limits",
                                        ),
                                        MDTextFieldHelperText(
                                            text="Enter a valid mm/dd/yyyy date",
                                        ),
                                        validator="date",
                                        date_format="mm/dd/yyyy",
                                    ),
                                    MDTextField(
                                        MDTextFieldHintText(
                                            text="Date yyyy/mm/dd without limits",
                                        ),
                                        MDTextFieldHelperText(
                                            text="Enter a valid yyyy/mm/dd date",
                                        ),
                                        validator="date",
                                        date_format="yyyy/mm/dd",
                                    ),
                                    MDTextField(
                                        MDTextFieldHintText(
                                            text="Date dd/mm/yyyy in [01/01/1900, 01/01/2100] interval",
                                        ),
                                        MDTextFieldHelperText(
                                            text="Enter a valid dd/mm/yyyy date",
                                        ),
                                        validator="date",
                                        date_format="dd/mm/yyyy",
                                        date_interval=["01/01/1900", "01/01/2100"],
                                    ),
                                    MDTextField(
                                        MDTextFieldHintText(
                                            text="Date dd/mm/yyyy in [01/01/1900, None] interval",
                                        ),
                                        MDTextFieldHelperText(
                                            text="Enter a valid dd/mm/yyyy date",
                                        ),
                                        validator="date",
                                        date_format="dd/mm/yyyy",
                                        date_interval=["01/01/1900", None],
                                    ),
                                    MDTextField(
                                        MDTextFieldHintText(
                                            text="Date dd/mm/yyyy in [None, 01/01/2100] interval",
                                        ),
                                        MDTextFieldHelperText(
                                            text="Enter a valid dd/mm/yyyy date",
                                        ),
                                        validator="date",
                                        date_format="dd/mm/yyyy",
                                        date_interval=[None, "01/01/2100"],
                                    ),
                                    orientation="vertical",
                                    spacing="28dp",
                                    adaptive_height=True,
                                    size_hint_x=.8,
                                    pos_hint={"center_x": .5, "center_y": .5},
                                ),
                                md_bg_color=self.theme_cls.backgroundColor,
                            )
                        )


                Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-fields-validator-date.png
        :align: center

    :attr:`validator` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    # Helper text label object.
    _helper_text_label = ObjectProperty()
    # Hint text label object.
    _hint_text_label = ObjectProperty()
    # Leading icon object.
    _leading_icon = ObjectProperty()
    # Trailing icon object.
    _trailing_icon = ObjectProperty()
    # Max length label object.
    _max_length_label = ObjectProperty()
    # Maximum length of characters to be input.
    _max_length = "0"
    # Active indicator height.
    _indicator_height = NumericProperty(dp(1))
    # Outline height.
    _outline_height = NumericProperty(dp(1))
    # The x-axis position of the hint text in the text field.
    _hint_x = NumericProperty(0)
    # The y-axis position of the hint text in the text field.
    _hint_y = NumericProperty(0)
    # The right/left lines coordinates of the text field in 'outlined' mode.
    _left_x_axis_pos = NumericProperty(dp(32))
    _right_x_axis_pos = NumericProperty(dp(32))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind(text=self.set_text)
        self.bind(_lines=self.adjust_height)
        self.theme_cls.bind(
            primary_palette=self.update_colors,
            theme_style=self.update_colors,
        )
        Clock.schedule_once(self._check_text)

    def update_colors(
        self, theme_manager: ThemeManager, theme_color: str
    ) -> None:
        """Fired when the `primary_palette` or `theme_style` value changes."""

        def update_colors(*args):
            if not self.disabled:
                self.on_focus(self, self.focus)
            else:
                self.on_disabled(self, self.disabled)

        Clock.schedule_once(update_colors, 1)

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, MDTextFieldHelperText):
            self._helper_text_label = widget
            self._set_texture_helper_text_color(text_color_focus=False)
        if isinstance(widget, MDTextFieldHintText):
            self._hint_text_label = widget
            self._set_texture_hint_text_color(text_color_focus=False)
        if isinstance(widget, MDTextFieldLeadingIcon):
            self._leading_icon = widget
            widget._text_field = self
            self._set_texture_leading_icons_color(icon_color_focus=False)
        if isinstance(widget, MDTextFieldTrailingIcon):
            self._trailing_icon = widget
            widget._text_field = self
            self._set_texture_trailing_icons_color(icon_color_focus=False)
        if isinstance(widget, MDTextFieldMaxLengthText):
            self._max_length_label = widget
            self._set_texture_max_length_color(text_color_focus=False)
        else:
            return super().add_widget(widget)

    def set_texture_color(
        self, texture, canvas_group, color: list, error: bool = False
    ) -> None:
        """
        Animates the color of the
        leading/trailing icons/hint/helper/max length text.
        """

        def update_texture(grop_name, instance):
            rectangle = self.canvas.before.get_group(grop_name)[0]
            rectangle.texture = instance.texture
            rectangle.size = instance.texture_size
            if instance is self._helper_text_label:
                rectangle.pos = self.get_adjusted_pos_helper_text_label()
            elif instance is self._leading_icon:
                if self._hint_text_label:
                    rectangle_hint = self.canvas.after.get_group(
                        "hint-text-rectangle"
                    )[0]
                    rectangle_hint.texture = self._hint_text_label.texture
                    rectangle_hint.size = self._hint_text_label.texture_size
                    rectangle_hint.pos = self.get_adjusted_pos_hint_text_label()
                    self._hint_text_label.texture_update()
                rectangle.pos = self.get_adjusted_pos_leading_icon()
            elif instance is self._trailing_icon:
                rectangle.pos = self.get_adjusted_pos_trailing_icon()
            elif instance is self._max_length_label:
                rectangle.pos = self.get_adjusted_pos_max_length_label()
            instance.texture_update()

        def update_hint_text_rectangle(*args):
            hint_text_rectangle = self.canvas.after.get_group(
                "hint-text-rectangle"
            )[0]
            hint_text_rectangle.texture = None
            texture.texture_update()
            hint_text_rectangle.texture = texture.texture

        if texture:
            Animation(rgba=color, d=0).start(canvas_group)
            a = Animation(color=color, d=0)

            if texture is self._hint_text_label:
                a.bind(on_complete=update_hint_text_rectangle)
            elif texture is self._helper_text_label:
                update_texture("helper-text-rectangle", self._helper_text_label)
            elif texture is self._leading_icon:
                update_texture("leading-icon-rectangle", self._leading_icon)
            elif texture is self._trailing_icon:
                update_texture("trailing-icon-rectangle", self._trailing_icon)
            elif texture is self._max_length_label:
                update_texture("max-length-rect", self._max_length_label)

            a.start(texture)

    def get_adjusted_pos_max_length_label(self) -> tuple:
        """
        Calculates the position of the max length label.

        Returns:
            tuple: (x, y) coordinates for positioning the max length label.
        """

        return (
            (self.x + self.width)
            - (self._max_length_label.texture_size[0] + dp(16)),
            self.y - dp(18),
        )

    def get_adjusted_pos_helper_text_label(self) -> tuple:
        """
        Calculates the position of the helper text label based on the
        textfield mode.

        Returns:
            tuple: (x, y) coordinates for positioning the helper text label.
        """

        return (
            self.x
            + (
                dp(16)
                if self.mode == "filled"
                else (0 if self.mode == "filled" else dp(12))
            ),
            self.y + dp(-18),
        )

    def get_adjusted_pos_trailing_icon(self) -> tuple:
        """
        Calculates the adjusted position of the trailing icon.

        Returns:
            tuple: (x, y) coordinates for positioning the trailing icon.
        """

        return (
            (self.width + self.x)
            - (self._trailing_icon.texture_size[1])
            - dp(14),
            self.center_y - self._trailing_icon.texture_size[1] / 2,
        )

    def get_adjusted_pos_leading_icon(self) -> tuple:
        """
        Calculates the adjusted position of the leading icon based on the
        textfield mode and icon size.

        Returns:
            tuple: (x, y) coordinates for positioning the leading icon.
        """

        return (
            self.x
            + (
                dp(12)
                if self.mode != "outlined"
                else (
                    dp(12)
                    if self.mode != "filled"
                    else (dp(4) if not self._leading_icon else dp(16))
                )
            ),
            self.center_y - self._leading_icon.texture_size[1] / 2,
        )

    def get_adjusted_pos_hint_text_label(self) -> tuple:
        """
        Calculates the adjusted position of the hint text label based on the
        presence of a leading icon and whether the textfield is multiline.

        Returns:
            tuple: (x, y) position coordinates for the hint text label.
        """

        return (
            self.x
            + (
                dp(16)
                if not self._leading_icon
                else self._leading_icon.texture_size[0] + dp(28) + self._hint_x
            ),
            (
                (
                    self.y
                    + self.height
                    + (self._hint_text_label.texture_size[1] / 2)
                    - (self.height / 2)
                    - self._hint_y
                )
                if not self.multiline
                else (
                    self.top - self._hint_text_label.texture_size[1] + dp(8)
                    if self.text
                    else (
                        self.y
                        + self.height
                        + (self._hint_text_label.texture_size[1] / 2)
                        - (self.height / 2)
                        - self._hint_y
                    )
                )
            ),
        )

    def set_pos_hint_text(self, y: float, x: float) -> None:
        """Animates the x-axis width and y-axis height of the hint text."""

        Animation(_hint_y=y, _hint_x=x, d=0.2, t="out_quad").start(self)

    def set_hint_text_font_size(self) -> None:
        """Animates the font size of the hint text."""

        Animation(
            size=self._hint_text_label.texture_size, d=0.2, t="out_quad"
        ).start(self.canvas.after.get_group("hint-text-rectangle")[0])

    def set_space_in_line(
        self, left_width: float | int, right_width: float | int
    ) -> None:
        """
        Animates the length of the right line of the text field for the
        hint text.
        """

        Animation(_left_x_axis_pos=left_width, d=0.2, t="out_quad").start(self)
        Animation(_right_x_axis_pos=right_width, d=0.2, t="out_quad").start(
            self
        )

    def set_max_text_length(self) -> None:
        """
        Fired when text is entered into a text field.
        Set max length text and updated max length texture.
        """

        if self._max_length_label:
            self._max_length_label.text = ""
            self._max_length_label.text = (
                f"{len(self.text)}/{self._max_length_label.max_text_length}"
            )
            self._max_length_label.texture_update()
            max_length_rect = self.canvas.before.get_group("max-length-rect")[0]
            max_length_rect.texture = None
            max_length_rect.texture = self._max_length_label.texture
            max_length_rect.size = self._max_length_label.texture_size
            max_length_rect.pos = (
                (self.x + self.width)
                - (self._max_length_label.texture_size[0] + dp(16)),
                self.y - dp(18),
            )

    def adjust_height(self, *args) -> None:
        """Adjusts the height of the text field in multiline mode."""

        if self.multiline:
            line_height = self.line_height
            line_count = max(1, len(self._lines))
            padding_top, padding_bottom = (
                self.padding[1] + dp(18),
                self.padding[3],
            )
            new_height = line_height * line_count + padding_top + padding_bottom
            self.height = max(new_height, dp(56))

    def set_text(self, instance, text: str) -> None:
        """Fired when text is entered into a text field."""

        def set_text(*args):
            self.text = re.sub("\n", " ", text) if not self.multiline else text
            self.set_max_text_length()

            if self.text and self._get_has_error() or self._get_has_error():
                self.error = True
            elif self.text and not self._get_has_error():
                self.error = False

            # Start the appropriate texture animations when programmatically
            # pasting text into a text field.
            if len(self.text) and not self.focus:
                if self._hint_text_label:
                    self._hint_text_label.font_size = theme_font_styles[
                        self._hint_text_label.font_style
                    ]["small"]["font-size"]
                    self._hint_text_label.texture_update()
                    self.set_hint_text_font_size()

            if (not self.text and not self.focus) or (
                self.text and not self.focus
            ):
                self.on_focus(instance, False)

            if self.multiline:
                self.adjust_height()

        set_text()

    def on_focus(self, instance, focus: bool) -> None:
        """Fired when the `focus` value changes."""

        if focus:
            if self.mode == "filled":
                Animation(_indicator_height=dp(1.25), d=0).start(self)
            else:
                Animation(_outline_height=dp(1.25), d=0).start(self)

            if self._trailing_icon:
                self._set_texture_trailing_icons_color(icon_color_focus=True)
            if self._leading_icon:
                self._set_texture_leading_icons_color(icon_color_focus=True)
            if self._max_length_label and not self.error:
                self._set_texture_max_length_color(text_color_focus=True)

            if self._helper_text_label and self._helper_text_label.mode in (
                "on_focus",
                "persistent",
            ):
                self._set_texture_helper_text_color(text_color_focus=True)
            if (
                self._helper_text_label
                and self._helper_text_label.mode == "on_error"
                and not self.error
            ):
                Clock.schedule_once(
                    lambda x: self.set_texture_color(
                        self._helper_text_label,
                        self.canvas.before.get_group("helper-text-color")[0],
                        self.theme_cls.transparentColor,
                    )
                )
            if self._hint_text_label:
                self._set_texture_hint_text_color(text_color_focus=True)
                self.set_pos_hint_text(
                    0 if self.mode != "outlined" else dp(-14),
                    (
                        (
                            -(
                                (
                                    self._leading_icon.texture_size[0]
                                    if self._leading_icon
                                    else 0
                                )
                                + dp(12)
                            )
                            if self._leading_icon
                            else 0
                        )
                        if self.mode == "outlined"
                        else -(
                            (
                                self._leading_icon.texture_size[0]
                                if self._leading_icon
                                else 0
                            )
                            - dp(24)
                        )
                    ),
                )
                self._hint_text_label.font_size = theme_font_styles[
                    self._hint_text_label.font_style
                ]["small"]["font-size"]
                self._hint_text_label.texture_update()
                self.set_hint_text_font_size()
                if self.mode == "outlined":
                    self.set_space_in_line(
                        dp(14), self._hint_text_label.texture_size[0] + dp(18)
                    )
        else:
            if self.mode == "filled":
                Animation(_indicator_height=dp(1), d=0).start(self)
            else:
                Animation(_outline_height=dp(1), d=0).start(self)

            if self._leading_icon:
                self._set_texture_leading_icons_color(icon_color_focus=False)
            if self._trailing_icon:
                self._set_texture_trailing_icons_color(icon_color_focus=False)
            if self._max_length_label and not self.error:
                self._set_texture_max_length_color(text_color_focus=False)
            if (
                self._helper_text_label
                and self._helper_text_label.mode in ["on_focus", "on_error"]
                and (
                    self._helper_text_label.mode == "on_focus" or not self.error
                )
            ):
                Clock.schedule_once(
                    lambda x: self.set_texture_color(
                        self._helper_text_label,
                        self.canvas.before.get_group("helper-text-color")[0],
                        self.theme_cls.transparentColor,
                    )
                )
            elif (
                self._helper_text_label
                and self._helper_text_label.mode == "persistent"
            ):
                self._set_texture_helper_text_color(text_color_focus=False)

            if not self.text:
                if self._hint_text_label:
                    if self.mode == "outlined":
                        self.set_space_in_line(dp(32), dp(32))
                    self._hint_text_label.font_size = theme_font_styles[
                        self._hint_text_label.font_style
                    ]["large"]["font-size"]
                    self._hint_text_label.texture_update()
                    self.set_hint_text_font_size()
                    self.set_pos_hint_text(
                        (self.height / 2)
                        - (self._hint_text_label.texture_size[1] / 2)
                        - (
                            dp(8)
                            if self.multiline and self.height != dp(56)
                            else 0
                        ),
                        0,
                    )
            else:
                if self._hint_text_label:
                    if self.mode == "outlined":
                        self.set_space_in_line(
                            dp(14),
                            self._hint_text_label.texture_size[0] + dp(18),
                        )
                    Clock.schedule_once(
                        lambda x: self.set_pos_hint_text(
                            0 if self.mode != "outlined" else dp(-14),
                            (
                                (
                                    -(
                                        (
                                            self._leading_icon.texture_size[0]
                                            if self._leading_icon
                                            else 0
                                        )
                                        + dp(12)
                                    )
                                    if self._leading_icon
                                    else 0
                                )
                                if self.mode == "outlined"
                                else -(
                                    (
                                        self._leading_icon.texture_size[0]
                                        if self._leading_icon
                                        else 0
                                    )
                                    - dp(24)
                                )
                            ),
                        )
                    )

            if self._hint_text_label:
                self._set_texture_hint_text_color(text_color_focus=False)

    def on_disabled(self, instance, disabled: bool) -> None:
        """Fired when the `disabled` value changes."""

        super().on_disabled(instance, disabled)

        def on_disabled(*args):
            if disabled:
                self._set_disabled_colors()
            else:
                self._set_enabled_colors()

        Clock.schedule_once(on_disabled, 0.2)

    def on_error(self, instance, error: bool) -> None:
        """
        Changes the primary colors of the text box to match the `error` value
        (text field is in an error state or not).
        """

        if error:
            if self._max_length_label:
                Clock.schedule_once(
                    lambda x: self.set_texture_color(
                        self._max_length_label,
                        self.canvas.before.get_group("max-length-color")[0],
                        self._get_error_color(),
                    )
                )
            if self._hint_text_label:
                Clock.schedule_once(
                    lambda x: self.set_texture_color(
                        self._hint_text_label,
                        self.canvas.after.get_group("hint-text-color")[0],
                        self._get_error_color(),
                    ),
                )
            if self._helper_text_label and self._helper_text_label.mode in (
                "persistent",
                "on_error",
            ):
                Clock.schedule_once(
                    lambda x: self.set_texture_color(
                        self._helper_text_label,
                        self.canvas.before.get_group("helper-text-color")[0],
                        self._get_error_color(),
                    )
                )
            if self._trailing_icon:
                Clock.schedule_once(
                    lambda x: self.set_texture_color(
                        self._trailing_icon,
                        self.canvas.before.get_group("trailing-icons-color")[0],
                        self._get_error_color(),
                    )
                )
        else:
            self.on_focus(self, self.focus)

    def on_height(self, instance, value_height: float) -> None:
        if value_height >= self.max_height and self.max_height:
            self.height = self.max_height

    def _set_texture_max_length_color(self, text_color_focus=False):
        label = self._max_length_label
        color = (
            label.text_color_focus
            if text_color_focus
            else label.text_color_normal
        ) or self.theme_cls.onSurfaceVariantColor

        Clock.schedule_once(
            lambda x: self.set_texture_color(
                label,
                self.canvas.before.get_group("max-length-color")[0],
                color,
            )
        )

    def _set_texture_hint_text_color(self, text_color_focus=False):
        label = self._hint_text_label
        if self.error:
            color = self._get_error_color()
        else:
            base_color = (
                label.text_color_focus
                if text_color_focus
                else label.text_color_normal
            )
            color = base_color or self.theme_cls.primaryColor

        Clock.schedule_once(
            lambda dt: self.set_texture_color(
                label,
                self.canvas.after.get_group("hint-text-color")[0],
                color,
            )
        )

    def _set_texture_helper_text_color(self, text_color_focus=False):
        label = self._helper_text_label

        if self.error:
            color = self._get_error_color()
        else:
            color = (
                label.text_color_focus
                if text_color_focus
                else label.text_color_normal
            ) or self.theme_cls.onSurfaceVariantColor

        Clock.schedule_once(
            lambda x: self.set_texture_color(
                label,
                self.canvas.before.get_group("helper-text-color")[0],
                color,
            )
        )

    def _set_texture_leading_icons_color(self, icon_color_focus=False):
        icon = self._leading_icon

        if icon.theme_icon_color == "Primary":
            color = self.theme_cls.onSurfaceVariantColor
        else:
            color = (
                icon.icon_color_focus
                if icon_color_focus
                else icon.icon_color_normal
            ) or self.theme_cls.onSurfaceVariantColor

        Clock.schedule_once(
            lambda x: self.set_texture_color(
                icon,
                self.canvas.before.get_group("leading-icons-color")[0],
                color,
            )
        )

    def _set_texture_trailing_icons_color(self, icon_color_focus=False):
        icon = self._trailing_icon

        if self.error:
            color = self._get_error_color()
        elif icon.theme_icon_color == "Primary":
            color = self.theme_cls.onSurfaceVariantColor
        else:
            color = (
                icon.icon_color_focus
                if icon_color_focus
                else icon.icon_color_normal
            )
            if not color:
                color = self.theme_cls.onSurfaceVariantColor

        Clock.schedule_once(
            lambda x: self.set_texture_color(
                icon,
                self.canvas.before.get_group("trailing-icons-color")[0],
                color,
            )
        )

    def _set_enabled_colors(self):
        def schedule_set_texture_color(widget, group_name, color):
            Clock.schedule_once(
                lambda x: self.set_texture_color(widget, group_name, color)
            )

        max_length_label_group = self.canvas.before.get_group(
            "max-length-color"
        )
        helper_text_label_group = self.canvas.before.get_group(
            "helper-text-color"
        )
        hint_text_label_group = self.canvas.after.get_group("hint-text-color")
        leading_icon_group = self.canvas.before.get_group("leading-icons-color")
        trailing_icon_group = self.canvas.before.get_group(
            "trailing-icons-color"
        )

        error_color = self._get_error_color()
        on_surface_variant_color = self.theme_cls.onSurfaceVariantColor

        if self._max_length_label:
            schedule_set_texture_color(
                self._max_length_label,
                max_length_label_group[0],
                (
                    self._max_length_label.color[:-1] + [1]
                    if not self.error
                    else error_color
                ),
            )
        if self._helper_text_label:
            schedule_set_texture_color(
                self._helper_text_label,
                helper_text_label_group[0],
                (
                    on_surface_variant_color
                    if not self._helper_text_label.text_color_focus
                    else (
                        self._helper_text_label.text_color_focus
                        if not self.error
                        else error_color
                    )
                ),
            )
        if self._hint_text_label:
            schedule_set_texture_color(
                self._hint_text_label,
                hint_text_label_group[0],
                (
                    on_surface_variant_color
                    if not self._hint_text_label.text_color_normal
                    else (
                        self._hint_text_label.text_color_normal
                        if not self.error
                        else error_color
                    )
                ),
            )
        if self._leading_icon:
            schedule_set_texture_color(
                self._leading_icon,
                leading_icon_group[0],
                (
                    on_surface_variant_color
                    if self._leading_icon.theme_icon_color == "Primary"
                    or not self._leading_icon.icon_color_normal
                    else self._leading_icon.icon_color_normal
                ),
            )
        if self._trailing_icon:
            schedule_set_texture_color(
                self._trailing_icon,
                trailing_icon_group[0],
                (
                    on_surface_variant_color
                    if self._trailing_icon.theme_icon_color == "Primary"
                    or not self._trailing_icon.icon_color_normal
                    else (
                        self._trailing_icon.icon_color_normal
                        if not self.error
                        else error_color
                    )
                ),
            )

    def _set_disabled_colors(self):
        """
        Sets the color and opacity of various widget components when the widget
        is disabled.

        For each of the following components (if present):
        - Maximum length label (`_max_length_label`)
        - Helper text label (`_helper_text_label`)
        - Hint text label (`_hint_text_label`)
        - Leading icon (`_leading_icon`)
        - Trailing icon (`_trailing_icon`)

        Determines the base color to use:
        - If the component has an `icon_color_disabled` attribute and it's not
          None, uses it (without the alpha channel).
        - Otherwise, uses `self.theme_cls.disabledTextColor`
          (without the alpha channel).

        Schedules a call via `Clock.schedule_once` to apply the final RGBA
        color (base + opacity) using the `set_texture_color()` method.
        """

        def schedule_set_texture_color(widget, group, opacity):
            if widget and group:
                color = (
                    widget.icon_color_disabled[:-1]
                    if hasattr(widget, "icon_color_disabled")
                    and widget.icon_color_disabled
                    else self.theme_cls.disabledTextColor[:-1]
                )
                Clock.schedule_once(
                    lambda x: self.set_texture_color(
                        widget, group[0], color + [opacity]
                    )
                )

        groups = {
            "_max_length_label": (
                self.canvas.before.get_group("max-length-color"),
                self.text_field_opacity_value_disabled_max_length_label,
            ),
            "_helper_text_label": (
                self.canvas.before.get_group("helper-text-color"),
                self.text_field_opacity_value_disabled_helper_text_label,
            ),
            "_hint_text_label": (
                self.canvas.after.get_group("hint-text-color"),
                self.text_field_opacity_value_disabled_hint_text_label,
            ),
            "_leading_icon": (
                self.canvas.before.get_group("leading-icons-color"),
                self.text_field_opacity_value_disabled_leading_icon,
            ),
            "_trailing_icon": (
                self.canvas.before.get_group("trailing-icons-color"),
                self.text_field_opacity_value_disabled_trailing_icon,
            ),
        }

        for attr, (group, opacity) in groups.items():
            widget = getattr(self, attr, None)
            schedule_set_texture_color(widget, group, opacity)

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
        if (
            self._max_length_label
            and self._max_length_label.max_text_length is not None
            and len(self.text) > self._max_length_label.max_text_length
        ):
            has_error = True
        else:
            if all((self.required, len(self.text) == 0)):
                has_error = True
            else:
                has_error = False
        return has_error

    def _get_error_color(self):
        return (
            self.theme_cls.errorColor
            if not self.error_color
            else self.error_color
        )

    def _check_text(self, *args) -> None:
        self.set_text(self, self.text)

    def _refresh_hint_text(self):
        """Method override to avoid duplicate hint text texture."""
