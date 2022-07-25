"""
Components/Label
================

.. rubric:: The :class:`MDLabel` widget is for rendering text.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/label.png
    :align: center

- MDLabel_
- MDIcon_

.. MDLabel:
MDLabel
-------

Class :class:`MDLabel` inherited from the :class:`~kivy.uix.label.Label` class
but for :class:`MDLabel` the ``text_size`` parameter is ``(self.width, None)``
and default is positioned on the left:

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:

        MDBoxLayout:
            orientation: "vertical"

            MDTopAppBar:
                title: "MDLabel"

            MDLabel:
                text: "MDLabel"
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-to-left.png
    :align: center

.. Note:: See :attr:`~kivy.uix.label.Label.halign`
    and :attr:`~kivy.uix.label.Label.valign` attributes
    of the :class:`~kivy.uix.label.Label` class

.. code-block:: kv

        MDLabel:
            text: "MDLabel"
            halign: "center"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-to-center.png
    :align: center

:class:`~MDLabel` color:
------------------------

:class:`~MDLabel` provides standard color themes for label color management:

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel

    KV = '''
    MDScreen:

        MDBoxLayout:
            id: box
            orientation: "vertical"

            MDTopAppBar:
                title: "MDLabel"
    '''


    class Test(MDApp):
        def build(self):
            screen = Builder.load_string(KV)
            # Names of standard color themes.
            for name_theme in [
                "Primary",
                "Secondary",
                "Hint",
                "Error",
                "ContrastParentBackground",
            ]:
                screen.ids.box.add_widget(
                    MDLabel(
                        text=name_theme,
                        halign="center",
                        theme_text_color=name_theme,
                    )
                )
            return screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-theme-text-color.png
    :align: center

To use a custom color for :class:`~MDLabel`, use a theme `'Custom'`.
After that, you can specify the desired color in the ``rgba`` format
in the ``text_color`` parameter:

.. code-block:: kv

    MDLabel:
        text: "Custom color"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-custom-color.png
    :align: center

:class:`~MDLabel` provides standard font styles for labels. To do this,
specify the name of the desired style in the :attr:`~MDLabel.font_style`
parameter:

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel
    from kivymd.font_definitions import theme_font_styles


    KV = '''
    MDScreen:

        MDBoxLayout:
            orientation: "vertical"

            MDTopAppBar:
                title: "MDLabel"

            ScrollView:

                MDList:
                    id: box
    '''


    class Test(MDApp):
        def build(self):
            screen = Builder.load_string(KV)
            # Names of standard font styles.
            for name_style in theme_font_styles[:-1]:
                screen.ids.box.add_widget(
                    MDLabel(
                        text=f"{name_style} style",
                        halign="center",
                        font_style=name_style,
                    )
                )
            return screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-font-style.gif
    :align: center

.. MDIcon:
MDIcon
-------

You can use labels to display material design icons using the
:class:`~MDIcon` class.

.. seealso::

    `Material Design Icons <https://materialdesignicons.com/>`_

    `Material Design Icon Names <https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py>`_

The :class:`~MDIcon` class is inherited from
:class:`~MDLabel` and has the same parameters.

.. Warning:: For the :class:`~MDIcon` class, you cannot use ``text``
    and ``font_style`` options!

.. code-block:: kv

    MDIcon:
        icon: "gmail"
        pos_hint: {"center_x": .5, "center_y": .5}

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon.png
    :align: center

MDIcon with badge icon
----------------------

.. code-block:: kv

    MDIcon:
        icon: "gmail"
        badge_icon: "numeric-10"
        pos_hint: {"center_x": .5, "center_y": .5}

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-badge.png
    :align: center
"""

__all__ = ("MDLabel", "MDIcon")

import os
from typing import Union

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import sp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.label import Label

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.theming_dynamic_text import get_contrast_text_color
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.floatlayout import MDFloatLayout

__MDLabel_colors__ = {
    "Primary": "text_color",
    "Secondary": "secondary_text_color",
    "Hint": "disabled_hint_text_color",
    "Error": "error_color",
    "OP": {
        "Primary": "opposite_text_color",
        "Secondary": "opposite_secondary_text_color",
        "Hint": "opposite_disabled_hint_text_color",
    },
}

with open(
    os.path.join(uix_path, "label", "label.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDLabel(DeclarativeBehavior, ThemableBehavior, Label, MDAdaptiveWidget):
    font_style = StringProperty("Body1")
    """
    Label font style.

    Available vanilla font_style are: `'H1'`, `'H2'`, `'H3'`, `'H4'`, `'H5'`,
    `'H6'`, `'Subtitle1'`, `'Subtitle2'`, `'Body1'`, `'Body2'`, `'Button'`,
    `'Caption'`, `'Overline'`, `'Icon'`.

    :attr:`font_style` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Body1'`.
    """

    _capitalizing = BooleanProperty(False)

    def _get_text(self):
        if self._capitalizing:
            return self._text.upper()
        return self._text

    def _set_text(self, value):
        self._text = value

    _text = StringProperty()

    text = AliasProperty(_get_text, _set_text, bind=["_text", "_capitalizing"])
    """Text of the label."""

    theme_text_color = OptionProperty(
        "Primary",
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
    """
    Label color scheme name.

    Available options are: `'Primary'`, `'Secondary'`, `'Hint'`, `'Error'`,
    `'Custom'`, `'ContrastParentBackground'`.

    :attr:`theme_text_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    text_color = ColorProperty(None)
    """
    Label text color in (r, g, b, a) format.

    :attr:`text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _text_color_str = StringProperty()

    parent_background = ColorProperty(None)
    can_capitalize = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            font_style=self.update_font_style,
            can_capitalize=self.update_font_style,
        )
        self.on_theme_text_color(None, self.theme_text_color)
        self.update_font_style(None, "")
        self.on_opposite_colors(None, self.opposite_colors)
        Clock.schedule_once(self.check_font_styles)
        self.theme_cls.bind(theme_style=self._do_update_theme_color)

    def check_font_styles(self, interval: Union[int, float] = 0) -> bool:
        if self.font_style not in list(self.theme_cls.font_styles.keys()):
            raise ValueError(
                f"MDLabel.font_style is set to an invalid option '{self.font_style}'."
                f"Must be one of: {list(self.theme_cls.font_styles)}"
            )
        else:
            return True

    def update_font_style(self, instance_label, font_style: str) -> None:
        if self.check_font_styles() is True:
            font_info = self.theme_cls.font_styles[self.font_style]
            self.font_name = font_info[0]
            self.font_size = sp(font_info[1])
            if font_info[2] and self.can_capitalize:
                self._capitalizing = True
            else:
                self._capitalizing = False

        # TODO: Add letter spacing change
        # self.letter_spacing = font_info[3]

    def on_theme_text_color(
        self, instance_label, theme_text_color: str
    ) -> None:
        op = self.opposite_colors
        if op:
            self._text_color_str = __MDLabel_colors__.get("OP", "").get(
                theme_text_color, ""
            )
        else:
            self._text_color_str = __MDLabel_colors__.get(theme_text_color, "")
        if self._text_color_str:
            self._do_update_theme_color()
        else:
            # 'Custom' and 'ContrastParentBackground' lead here, as well as the
            # generic None value it's not yet been set
            self._text_color_str = ""
            if theme_text_color == "Custom" and self.text_color:
                self.color = self.text_color
            elif (
                theme_text_color == "ContrastParentBackground"
                and self.parent_background
            ):
                self.color = get_contrast_text_color(self.parent_background)
            else:
                self.color = [0, 0, 0, 1]

    def on_text_color(self, instance_label, color: list) -> None:
        if self.theme_text_color == "Custom":
            self.color = self.text_color

    def on_opposite_colors(self, *args) -> None:
        self.on_theme_text_color(self, self.theme_text_color)

    def _do_update_theme_color(self, *args):
        if self._text_color_str:
            self.color = getattr(self.theme_cls, self._text_color_str)
            if not self.disabled:
                self.color = getattr(self.theme_cls, self._text_color_str)
            else:
                self.color = getattr(self.theme_cls, "disabled_hint_text_color")


class MDIcon(MDFloatLayout, MDLabel):
    icon = StringProperty("android")
    """
    Label icon name.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    badge_icon = StringProperty()
    """
    Label badge icon name.

    .. versionadded:: 1.0.0

    :attr:`badge_icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    badge_icon_color = ColorProperty([1, 1, 1, 1])
    """
    Badge icon color in (r, g, b, a) format.

    .. versionadded:: 1.0.0

    :attr:`badge_icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    badge_bg_color = ColorProperty(None)
    """
    Badge icon background color in (r, g, b, a) format.

    .. versionadded:: 1.0.0

    :attr:`badge_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    badge_font_size = NumericProperty()
    """
    Badge font size.

    .. versionadded:: 1.0.0

    :attr:`badge_font_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    source = StringProperty(None, allownone=True)
    """
    Path to icon.

    :attr:`source` is an :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        from kivymd.uix.selectioncontrol import MDCheckbox

        super().__init__(**kwargs)
        if not isinstance(self, MDCheckbox):
            self.size_hint = (None, None)
            self.size = self.texture_size
            self.adaptive_size = True
