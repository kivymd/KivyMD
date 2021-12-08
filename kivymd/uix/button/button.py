"""
Components/Button
=================

.. seealso::

    `Material Design spec, Buttons <https://material.io/components/buttons>`_

    `Material Design spec, Buttons: floating action button <https://material.io/components/buttons-floating-action-button>`_

.. rubric:: Buttons allow users to take actions, and make choices,
    with a single tap.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/buttons.png
    :align: center

`KivyMD` provides the following button classes for use:

- MDIconButton_
- MDFloatingActionButton_
- MDFlatButton_
- MDRaisedButton_
- MDRectangleFlatButton_
- MDRectangleFlatIconButton_
- MDRoundFlatButton_
- MDRoundFlatIconButton_
- MDFillRoundFlatButton_
- MDFillRoundFlatIconButton_
- MDTextButton_
- MDFloatingActionButtonSpeedDial_

.. MDIconButton:
MDIconButton
------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-button.gif
    :align: center

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:

        MDIconButton:
            icon: "language-python"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

The :class:`~MDIconButton.icon` parameter must have the name of the icon
from ``kivymd/icon_definitions.py`` file.

You can also use custom icons:

.. code-block:: kv

    MDIconButton:
        icon: "data/logo/kivy-icon-256.png"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-custom-button.gif
    :align: center

By default, :class:`~MDIconButton` button has a size ``(dp(48), dp (48))``.
Use :class:`~BaseButton.user_font_size` attribute to resize the button:

.. code-block:: kv

    MDIconButton:
        icon: "android"
        user_font_size: "64sp"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-button-user-font-size.gif
    :align: center

By default, the color of :class:`~MDIconButton`
(depending on the style of the application) is black or white.
You can change the color of :class:`~MDIconButton` as the text color
of :class:`~kivymd.uix.label.MDLabel`:

.. code-block:: kv

    MDIconButton:
        icon: "android"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-button-theme-text-color.png
    :align: center

.. MDFloatingActionButton:
MDFloatingActionButton
----------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-floating-action-button.png
    :align: center

The above parameters for :class:`~MDIconButton` apply
to :class:`~MDFloatingActionButton`.

To change :class:`~MDFloatingActionButton` background, use the
``md_bg_color`` parameter:

.. code-block:: kv

    MDFloatingActionButton:
        icon: "android"
        md_bg_color: app.theme_cls.primary_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-floating-action-button-md-bg-color.png
    :align: center

Material design style 3
-----------------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.utils import get_color_from_hex

    from kivymd.app import MDApp
    from kivymd.uix.button import MDFloatingActionButton

    KV = '''
    #:import get_color_from_hex kivy.utils.get_color_from_hex


    MDScreen:
        md_bg_color: get_color_from_hex("#f7f2fa")

        MDBoxLayout:
            id: box
            spacing: "56dp"
            adaptive_size: True
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class TestNavigationDrawer(MDApp):
        def build(self):
            self.theme_cls.material_style = "M3"
            return Builder.load_string(KV)

        def on_start(self):
            data = {
                "standard": {"md_bg_color": "#fefbff", "text_color": "#6851a5"},
                "small": {"md_bg_color": "#e9dff7", "text_color": "#211c29"},
                "large": {"md_bg_color": "#f8d7e3", "text_color": "#311021"},
            }
            for type_button in data.keys():
                self.root.ids.box.add_widget(
                    MDFloatingActionButton(
                        icon="pencil",
                        type=type_button,
                        theme_text_color="Custom",
                        md_bg_color=get_color_from_hex(data[type_button]["md_bg_color"]),
                        text_color=get_color_from_hex(data[type_button]["text_color"]),
                    )
                )


    TestNavigationDrawer().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-floating-action-button-m3.gif
    :align: center

.. MDFlatButton:
MDFlatButton
------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-flat-button.gif
    :align: center

To change the text color of: class:`~MDFlatButton` use the ``text_color`` parameter:

.. code-block:: kv

    MDFlatButton:
        text: "MDFLATBUTTON"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-flat-button-text-color.png
    :align: center

Or use markup:

.. code-block:: kv

    MDFlatButton:
        text: "[color=#00ffcc]MDFLATBUTTON[/color]"

To specify the font size and font name, use the parameters as in the usual
`Kivy` buttons:

.. code-block:: kv

    MDFlatButton:
        text: "MDFLATBUTTON"
        font_size: "18sp"
        font_name: "path/to/font"

.. MDRaisedButton:
MDRaisedButton
--------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-raised-button.gif
    :align: center

This button is similar to the :class:`~MDFlatButton` button except that you
can set the background color for :class:`~MDRaisedButton`:

.. code-block:: kv

    MDRaisedButton:
        text: "MDRAISEDBUTTON"
        md_bg_color: 1, 0, 1, 1


.. MDRectangleFlatButton:
MDRectangleFlatButton
---------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-rectangle-flat-button.gif
    :align: center

.. code-block:: kv

    MDRectangleFlatButton:
        text: "MDRECTANGLEFLATBUTTON"
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-rectangle-flat-button-md-bg-color.png
    :align: center

.. MDRectangleFlatIconButton:
MDRectangleFlatIconButton
-------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-rectangle-flat-icon-button.png
    :align: center

Button parameters :class:`~MDRectangleFlatButton` are the same as
button :class:`~MDRectangleFlatButton`:

.. code-block:: kv

    MDRectangleFlatIconButton:
        icon: "android"
        text: "MDRECTANGLEFLATICONBUTTON"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        line_color: 1, 0, 1, 1
        icon_color: 1, 0, 0, 1

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-rectangle-flat-icon-button-custom.png
    :align: center

Without border
--------------

.. code-block:: python

    from kivymd.app import MDApp
    from kivymd.uix.screen import MDScreen
    from kivymd.uix.button import MDRectangleFlatIconButton


    class Example(MDApp):
        def build(self):
            screen = MDScreen()
            screen.add_widget(
                MDRectangleFlatIconButton(
                    text="MDRectangleFlatIconButton",
                    icon="language-python",
                    line_color=(0, 0, 0, 0),
                    pos_hint={"center_x": .5, "center_y": .5},
                )
            )
            return screen


    Example().run()

.. code-block:: kv

    MDRectangleFlatIconButton:
        text: "MDRectangleFlatIconButton"
        icon: "language-python"
        line_color: 0, 0, 0, 0
        pos_hint: {"center_x": .5, "center_y": .5}

.. MDRoundFlatButton:
MDRoundFlatButton
-----------------

.. code-block:: kv

    MDRoundFlatButton:
        text: "MDROUNDFLATBUTTON"
        text_color: 0, 1, 0, 1

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-round-flat-button-text-color.png
    :align: center

.. MDRoundFlatIconButton:
MDRoundFlatIconButton
---------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-round-flat-icon-button.png
    :align: center

Button parameters :class:`~MDRoundFlatIconButton` are the same as
button :class:`~MDRoundFlatButton`:

.. code-block:: kv

    MDRoundFlatIconButton:
        icon: "android"
        text: "MDROUNDFLATICONBUTTON"

.. MDFillRoundFlatButton:
MDFillRoundFlatButton
---------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-fill-round-flat-button.png
    :align: center

Button parameters :class:`~MDFillRoundFlatButton` are the same as
button :class:`~MDRaisedButton`.

.. MDFillRoundFlatIconButton:
MDFillRoundFlatIconButton
-------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-fill-round-flat-icon-button.png
    :align: center

Button parameters :class:`~MDFillRoundFlatIconButton` are the same as
button :class:`~MDRaisedButton`.

.. note:: Notice that the width of the :class:`~MDFillRoundFlatIconButton`
    button matches the size of the button text.

.. MDTextButton:
MDTextButton
------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-text-button.png
    :align: center

.. code-block:: kv

    MDTextButton:
        text: "MDTEXTBUTTON"
        custom_color: 0, 1, 0, 1

.. MDFloatingActionButtonSpeedDial:
MDFloatingActionButtonSpeedDial
-------------------------------

.. Note:: See the full list of arguments in the class
    :class:`~MDFloatingActionButtonSpeedDial`.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:

        MDFloatingActionButtonSpeedDial:
            data: app.data
            root_button_anim: True
    '''


    class Example(MDApp):
        data = {
            'Python': 'language-python',
            'PHP': 'language-php',
            'C++': 'language-cpp',
        }

        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial.gif
    :align: center

Or without KV Language:

.. code-block:: python

    from kivymd.uix.screen import MDScreen
    from kivymd.app import MDApp
    from kivymd.uix.button import MDFloatingActionButtonSpeedDial


    class Example(MDApp):
        data = {
            'Python': 'language-python',
            'PHP': 'language-php',
            'C++': 'language-cpp',
        }

        def build(self):
            screen = MDScreen()
            speed_dial = MDFloatingActionButtonSpeedDial()
            speed_dial.data = self.data
            speed_dial.root_button_anim = True
            screen.add_widget(speed_dial)
            return screen


    Example().run()

You can use various types of animation of labels for buttons on the stack:

.. code-block:: kv

    MDFloatingActionButtonSpeedDial:
        hint_animation: True

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-hint.gif
    :align: center

You can set your color values ​​for background, text of buttons etc:

.. code-block:: kv

    MDFloatingActionButtonSpeedDial:
        bg_hint_color: app.theme_cls.primary_light

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-hint-color.png
    :align: center

.. seealso::

    `See full example <https://github.com/kivymd/KivyMD/wiki/Components-Button>`_
"""

__all__ = (
    "MDIconButton",
    "MDFloatingActionButton",
    "MDFlatButton",
    "MDRaisedButton",
    "MDRectangleFlatButton",
    "MDRectangleFlatIconButton",
    "MDRoundFlatButton",
    "MDRoundFlatIconButton",
    "MDFillRoundFlatButton",
    "MDFillRoundFlatIconButton",
    "MDTextButton",
    "MDFloatingActionButtonSpeedDial",
)

import os
from typing import NoReturn, Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.stencil_instructions import (
    StencilPop,
    StencilPush,
    StencilUnUse,
    StencilUse,
)
from kivy.graphics.vertex_instructions import Ellipse, RoundedRectangle
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    DictProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivymd import uix_path
from kivymd.color_definitions import text_colors
from kivymd.font_definitions import theme_font_styles
from kivymd.theming import ThemableBehavior, ThemeManager
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    CommonElevationBehavior,
    FakeRectangularElevationBehavior,
    RectangularRippleBehavior,
    RoundedRectangularElevationBehavior,
)
from kivymd.uix.label import MDLabel
from kivymd.uix.tooltip import MDTooltip

with open(
    os.path.join(uix_path, "button", "button.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class BaseButton(RectangularRippleBehavior, ThemableBehavior, ButtonBehavior,
                 AnchorLayout):
    """Base class for all buttons."""

    padding = VariableListProperty([dp(16), dp(12), dp(16), dp(12)])
    """
    Padding between the widget box and its children, in pixels:
    [padding_left, padding_top, padding_right, padding_bottom].

    padding also accepts a two argument form [padding_horizontal,
    padding_vertical] and a one argument form [padding].

    .. versionadded:: 1.0.0

    :attr:`padding` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to [0, 0, 0, 0].
    """

    halign = OptionProperty("center", options=("left", "center", "right"))
    """
    Horizontal anchor.

    .. versionadded:: 1.0.0

    :attr:`anchor_x` is an :class:`~kivy.properties.OptionProperty`
    and defaults to 'center'. It accepts values of 'left', 'center' or 'right'.
    """

    valign = OptionProperty("center", options=("top", "center", "bottom"))
    """
    Vertical anchor.

    .. versionadded:: 1.0.0

    :attr:`anchor_y` is an :class:`~kivy.properties.OptionProperty`
    and defaults to 'center'. It accepts values of 'top', 'center' or 'bottom'.
    """

    theme_text_color = OptionProperty(
        None,
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
    Button text type. Available options are: (`"Primary"`, `"Secondary"`,
    `"Hint"`, `"Error"`, `"Custom"`, `"ContrastParentBackground"`).

    :attr:`theme_text_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    text_color = ColorProperty(None)
    """
    Button text color in (r, g, b, a) format.

    :attr:`text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    font_name = StringProperty()
    """
    Button text font name.

    :attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    font_size = NumericProperty("14sp")
    """
    Button text font size.

    :attr:`font_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `14sp`.
    """

    user_font_size = NumericProperty(0)
    """
    Custom font size for :class:`~MDIconButton`.

    :attr:`user_font_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    font_style = OptionProperty("Body1", options=theme_font_styles)
    """
    Button text font style.

    Available vanilla font_style are: `'H1'`, `'H2'`, `'H3'`, `'H4'`, `'H5'`,
    `'H6'`, `'Subtitle1'`, `'Subtitle2'`, `'Body1'`, `'Body2'`, `'Button'`,
    `'Caption'`, `'Overline'`, `'Icon'`.

    :attr:`font_style` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Body1'`.
    """

    line_width = NumericProperty(1)
    """
    Line width for button border.

    :attr:`line_width` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    line_color = ColorProperty(None)
    """
    Line color for button border.

    :attr:`line_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    line_color_disabled = ColorProperty(None)
    """
    Line color for button border.

    :attr:`line_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    md_bg_color = ColorProperty(None)
    """
    Button background color.

    :attr:`md_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    Disabled button text color.

    :attr:`md_bg_color_disabled` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _radius = NumericProperty(0)
    _min_width = NumericProperty(None)
    _md_bg_color = ColorProperty(None)
    _md_bg_color_disabled = ColorProperty(None)
    _line_color = ColorProperty(None)
    _line_color_disabled = ColorProperty(None)
    _theme_text_color = OptionProperty(
        None,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
        ],
    )
    _text_color = ColorProperty(None)

    # Default colors - set to None to use primary theme colors
    _default_md_bg_color = [0.0, 0.0, 0.0, 0.0]
    _default_md_bg_color_disabled = [0.0, 0.0, 0.0, 0.0]
    _default_line_color = [0.0, 0.0, 0.0, 0.0]
    _default_line_color_disabled = [0.0, 0.0, 0.0, 0.0]
    _default_theme_text_color = StringProperty('Primary')
    _default_text_color = ColorProperty(None)

    _animation_fade_bg = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(primary_palette=self.set_button_colors)
        self.theme_cls.bind(primary_palette=self.set_text_color)
        self.theme_cls.bind(theme_style=self.set_button_colors)
        self.theme_cls.bind(theme_style=self.set_text_color)
        self.bind(md_bg_color=self.set_button_colors)
        self.bind(md_bg_color_disabled=self.set_button_colors)
        self.bind(line_color=self.set_button_colors)
        self.bind(line_color_disabled=self.set_button_colors)
        self.bind(theme_text_color=self.set_text_color)
        self.bind(text_color=self.set_text_color)
        Clock.schedule_once(self.set_button_colors)
        Clock.schedule_once(self.set_text_color)

    def set_button_colors(self, *args) -> NoReturn:
        """Set all button colours (except text)."""

        # Set main color
        self._md_bg_color = (
            self.md_bg_color
            or self._default_md_bg_color
            or self.theme_cls.primary_color
        )

        # Set disabled color
        self._md_bg_color_disabled = (
            self.md_bg_color_disabled
            or (
                [sum(self.md_bg_color[0:3]) / 3.0] * 3
                + [0.38 if self.theme_cls.theme_style == 'Light' else 0.5]
                if self.md_bg_color else None
            )
            or self._default_md_bg_color_disabled
            or self.theme_cls.disabled_primary_color
        )

        # Set line color
        self._line_color = (
            self.line_color
            or self._default_line_color
            or self.theme_cls.primary_color
        )

        # Set disabled line color
        self._line_color_disabled = (
            self.line_color_disabled
            or (
                [sum(self.line_color[0:3]) / 3.0] * 3
                + [0.38 if self.theme_cls.theme_style == 'Light' else 0.5]
                if self.line_color else None
            )
            or self._default_line_color_disabled
            or self.theme_cls.disabled_primary_color
        )

    def set_text_color(self, *args) -> NoReturn:
        """Set _theme_text_color and _text_color based on defaults
        and options.
        """
        self._theme_text_color = (
            self.theme_text_color or self._default_theme_text_color
        )
        if self._default_text_color == 'PrimaryHue':
            default_text_color = (
                text_colors[self.theme_cls.primary_palette]
                [self.theme_cls.primary_hue]
            )
        elif self._default_text_color == 'Primary':
            default_text_color = self.theme_cls.primary_color
        else:
            default_text_color = self.theme_cls.text_color
        self._text_color = self.text_color or default_text_color

    def update_text_color(self, *args) -> NoReturn:
        pass

    def on_md_bg_color(self, instance_button, color: list) -> NoReturn:
        pass

    #def _remove_shadow(self, interval: Union[int, float]) -> NoReturn:
        #self.canvas.before.remove_group("soft_shadow")

    def on_width(self, instance_button, width: float) -> NoReturn:
        """If the button style has a minimum width set, enforce it here."""
        if self._min_width and (self.width < self._min_width):
            self.width = self._min_width

    # Touch events that cause transparent buttons to fade to background
    def on_touch_down(self, touch):
        """Animates fade to background on press, for buttons with no
        background color.
        """
        if touch.is_mouse_scrolling:
            return False
        elif not self.collide_point(touch.x, touch.y):
            return False
        elif self in touch.ud:
            return False
        elif self.disabled:
            return False
        else:
            if self._md_bg_color[3] == 0.0:
                self._animation_fade_bg = Animation(
                    duration=0.5, _md_bg_color=[0.0, 0.0, 0.0, 0.1]
                )
                self._animation_fade_bg.start(self)
            return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        """Animates return to original background on touch release."""
        if not self.disabled and self._animation_fade_bg:
            self._animation_fade_bg.stop_property(self, "_md_bg_color")
            self._animation_fade_bg = None
            md_bg_color = (
                self.md_bg_color
                or self._default_md_bg_color
                or self.theme_cls.primary_color
            )
            Animation(
                duration=0.05, _md_bg_color=md_bg_color
            ).start(self)
        return super().on_touch_up(touch)


class ButtonContentsText():
    """Contents for BaseButton consisting of a single label."""

    text = StringProperty(" ")
    """
    Button text.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `' '`.
    """

    _min_width = NumericProperty(88)


class ButtonContentsIcon():
    """Contents for a round BaseButton consisting of an MDIcon."""

    icon_size = NumericProperty()
    """
    Icon font size.
    Use this parameter as the font size, that is, in sp units.

    .. versionadded:: 1.0.0

    :attr:`icon_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    icon = StringProperty("checkbox-blank-circle")
    """
    Button icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle'`.
    """

    icon_color = ColorProperty(None)
    """
    Button icon color.

    :attr:`icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """
    _icon_color = ColorProperty(None)

    def set_text_color(self, *args):
        super().set_text_color()
        self._icon_color = self.icon_color or self._text_color


class ButtonContentsIconText():
    """Contents for BaseButton consisting of a BoxLayout
    with an icon and a label."""

    text = StringProperty(" ")
    """
    Button text.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `' '`.
    """

    icon_size = NumericProperty()
    """
    Icon font size.
    Use this parameter as the font size, that is, in sp units.

    .. versionadded:: 1.0.0

    :attr:`icon_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    icon = StringProperty("android")
    """
    Button icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    icon_color = ColorProperty(None)
    """
    Button icon color.

    :attr:`icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """
    _icon_color = ColorProperty(None)

    _min_width = NumericProperty(88)

    def set_text_color(self, *args):
        super().set_text_color()
        self._icon_color = self.icon_color or self._text_color


class ButtonElevationBehaviour(CommonElevationBehavior):
    """
    Implements elevation behavior as well as the recommended down/disabled
    colors for raised buttons.

    The minimum elevation for any raised button is `"1dp"`,
    by default, set to `"2dp"`.

    the _elevation_raised is automatically computed and is set to
    self.elevation + 6 each time self.elevation is updated.
    """

    _elevation_raised = NumericProperty()
    _anim_raised = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        if self.elevation == 0:
            self.elevation = 2
        super().__init__(**kwargs)
        self.bind(_radius=self.setter('radius'))
        self.on_elevation(self, self.elevation)

    def on_elevation(self, instance_button, elevation_value: int) -> NoReturn:
        super().on_elevation(instance_button, elevation_value)
        self._elevation_raised = self.elevation + 6
        self._anim_raised = Animation(_elevation=self._elevation_raised, d=0.15)

    def on__elevation_raised(
        self, instance_button, elevation_value: int
    ) -> NoReturn:
        Animation.cancel_all(self, "_elevation")
        self._anim_raised = Animation(_elevation=self._elevation_raised, d=0.15)

    def on_disabled(self, instance_button, disabled_value: bool) -> NoReturn:
        if self.disabled is True:
            Animation.cancel_all(self, "_elevation")
        super().on_disabled(instance_button, disabled_value)

    def on_touch_down(self, touch):
        if not self.disabled:
            if touch.is_mouse_scrolling:
                return False
            if not self.collide_point(touch.x, touch.y):
                return False
            if self in touch.ud:
                return False
            if self._anim_raised:
                self._anim_raised.start(self)
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if not self.disabled:
            if touch.grab_current is not self:
                #if isinstance(self, MDFloatingActionButton):
                self.stop_elevation_anim()
                return super().on_touch_up(touch)
            self.stop_elevation_anim()
        return super().on_touch_up(touch)

    def stop_elevation_anim(self):
        Animation.cancel_all(self, "_elevation")
        self._elevation = self.elevation


# MD Button classes


class MDFlatButton(ButtonContentsText, BaseButton):
    """A flat rectangular button with (by default) no border or
    background. Text is the default text color.
    """
    pass


class MDRaisedButton(
    FakeRectangularElevationBehavior, ButtonElevationBehaviour,
    ButtonContentsText, BaseButton
):
    """A flat button with (by default) a primary color fill and matching
    color text.
    """
    _default_md_bg_color = None
    _default_md_bg_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_text_color = "PrimaryHue"


class MDRectangleFlatButton(ButtonContentsText, BaseButton):
    """A flat button with (by default) a primary color border and primary
    color text.
    """
    _default_line_color = None
    _default_line_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_text_color = "Primary"


class MDRectangleFlatIconButton(ButtonContentsIconText, BaseButton):
    """A flat button with (by default) a primary color border,
    primary color text and a primary color icon on the left.
    """
    _default_line_color = None
    _default_line_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_text_color = "Primary"


class MDRoundFlatButton(ButtonContentsText, BaseButton):
    """A flat button with (by default) rounded corners, a primary
    color border and primary color text.
    """
    _default_line_color = None
    _default_line_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_text_color = "Primary"
    _radius = NumericProperty("18dp")


class MDRoundFlatIconButton(ButtonContentsIconText, BaseButton):
    """A flat button with (by default) rounded corners, a primary
    color border, primary color text and a primary color icon on
    the left.
    """
    _default_line_color = None
    _default_line_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_text_color = "Primary"
    _radius = NumericProperty("18dp")


class MDFillRoundFlatButton(ButtonContentsText, BaseButton):
    """A flat button with (by default) rounded corners, a primary
    color fill and primary color text.
    """
    _default_md_bg_color = None
    _default_md_bg_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_text_color = "PrimaryHue"
    _radius = NumericProperty("18dp")


class MDFillRoundFlatIconButton(ButtonContentsIconText, BaseButton):
    """A flat button with (by default) rounded corners, a primary
    color fill, primary color text and a primary color icon on
    the left.
    """
    _default_md_bg_color = None
    _default_md_bg_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_text_color = "PrimaryHue"
    _radius = NumericProperty("18dp")


class MDIconButton(ButtonContentsIcon, BaseButton):
    icon = StringProperty("checkbox-blank-circle")
    """
    Button icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle'`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.theme_cls.bind(primary_palette=self.update_md_bg_color)
        Clock.schedule_once(self.set_size)
        self.on_md_bg_color(self, [0.0, 0.0, 0.0, 0.0])

    def set_size(self, interval: Union[int, float]) -> NoReturn:
        """
        Sets the custom icon size if the value of the `user_font_size`
        attribute is not zero. Otherwise, the icon size is set to `(48, 48)`.
        """

        self.width = (
            "48dp" if not self.user_font_size else dp(self.user_font_size + 23)
        )
        self.height = (
            "48dp" if not self.user_font_size else dp(self.user_font_size + 23)
        )

    def on_width(self, instance_button, width: Union[int, float]) -> NoReturn:
        """Sets the radius to half the width."""
        self._radius = self.width / 2


class MDFloatingActionButton(
    RoundedRectangularElevationBehavior, ButtonElevationBehaviour,
    ButtonContentsIcon, BaseButton
):
    """
    Implementation
    `FAB <https://m3.material.io/components/floating-action-button/overview>`_
    button.
    """

    type = OptionProperty("standard", options=["small", "large", "standard"])
    """
    Type of M3 button.

    .. versionadded:: 1.0.0

    Available options are: 'small', 'large', 'standard'.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-floating-action-button-types.png
        :align: center

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'standard'`.
    """

    _default_md_bg_color = None
    _default_md_bg_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_text_color = "PrimaryHue"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(
            material_style=self.set_size,
        )
        Clock.schedule_once(self.set_size)
        Clock.schedule_once(self.set_radius)
        Clock.schedule_once(self.set_font_size)


    def set_font_size(self, *args) -> NoReturn:
        if self.theme_cls.material_style == "M3":
            if self.type == "large":
                self.user_font_size = "36sp"
            else:
                self.user_font_size = 0

    def set_radius(self, *args) -> NoReturn:
        if self.theme_cls.material_style == "M2":
            self._radius = self.width / 2
        else:
            if self.type == "large":
                self._radius = 32
            elif self.type == "standard":
                self._radius = 16
            elif self.type == "small":
                self._radius = 14

    def set_size(self, *args) -> NoReturn:
        if self.theme_cls.material_style == "M2":
            self.width = dp(56)
            self.height = dp(56)
        else:
            if self.type == "small":
                self.size = (dp(40), dp(40))
            elif self.type == "standard":
                self.width = dp(56)
                self.height = dp(56)
            elif self.type == "large":
                self.width = dp(96)
                self.height = dp(96)

    def on_type(
        self, instance_md_floating_action_button, type: str
    ) -> NoReturn:
        self.set_size()
        self.set_font_size()

    #def on_touch_down(self, touch):
        #super(MDFloatingActionButton, self).on_touch_down(touch)
        #if self.collide_point(touch.x, touch.y):
            #return True

    #def on_touch_move(self, touch):
        #super(MDFloatingActionButton, self).on_touch_move(touch)
        #if self.collide_point(touch.x, touch.y):
            #return True

    #def on_touch_up(self, touch):
        #super(MDFloatingActionButton, self).on_touch_up(touch)
        #if self.collide_point(touch.x, touch.y):
            #return True


class MDTextButton(ButtonBehavior, MDLabel):
    color = ColorProperty(None)
    """
    Button color in (r, g, b, a) format.

    :attr:`color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    color_disabled = ColorProperty(None)
    """
    Button color disabled in (r, g, b, a) format.

    :attr:`color_disabled` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _color = ColorProperty(None)  # last current button text color

    def animation_label(self) -> NoReturn:
        def set_default_state_label(*args):
            Animation(opacity=1, d=0.1, t="in_out_cubic").start(self)

        anim = Animation(opacity=0.5, d=0.2, t="in_out_cubic")
        anim.bind(on_complete=set_default_state_label)
        anim.start(self)

    def on_press(self, *args):
        self.animation_label()
        return super().on_press(*args)

    def on_disabled(self, instance_button, disabled_value) -> NoReturn:
        if disabled_value:
            if not self.color_disabled:
                self.color_disabled = self.theme_cls.disabled_hint_text_color
                self._color = self.color
            self.text_color = self.color_disabled
        else:
            self.text_color = self._color


# SpeedDial classes


class BaseFloatingRootButton(MDFloatingActionButton):
    _angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.elevation = 5


class BaseFloatingBottomButton(MDFloatingActionButton, MDTooltip):
    _canvas_width = NumericProperty(0)
    _padding_right = NumericProperty(0)
    _bg_color = ColorProperty(None)

    def set_size(self, interval: Union[int, float]) -> NoReturn:
        self.width = "46dp"
        self.height = "46dp"


class BaseFloatingLabel(
    ThemableBehavior, FakeRectangularElevationBehavior, BoxLayout
):
    text = StringProperty()
    text_color = ColorProperty(None)
    bg_color = ColorProperty(None)


class MDFloatingBottomButton(BaseFloatingBottomButton):
    pass


class MDFloatingRootButton(BaseFloatingRootButton):
    pass


class MDFloatingLabel(BaseFloatingLabel):
    pass


class MDFloatingActionButtonSpeedDial(ThemableBehavior, FloatLayout):
    """
    :Events:
        :attr:`on_open`
            Called when a stack is opened.
        :attr:`on_close`
            Called when a stack is closed.
    """

    icon = StringProperty("plus")
    """
    Root button icon name.

    :attr:`icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'plus'`.
    """

    anchor = OptionProperty("right", option=["right"])
    """
    Stack anchor. Available options are: `'right'`.

    :attr:`anchor` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'right'`.
    """

    callback = ObjectProperty(lambda x: None)
    """
    Custom callback.

    .. code-block:: kv

        MDFloatingActionButtonSpeedDial:
            callback: app.callback

    .. code-block:: python

        def callback(self, instance):
            print(instance.icon)


    :attr:`callback` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    label_text_color = ColorProperty([0, 0, 0, 1])
    """
    Floating text color in (r, g, b, a) format.

    :attr:`label_text_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 1]`.
    """

    data = DictProperty()
    """
    Must be a dictionary

    .. code-block:: python

        {
            'name-icon': 'Text label',
            ...,
            ...,
        }
    """

    right_pad = BooleanProperty(True)
    """
    If `True`, the button will increase on the right side by 2.5 pixels
    if the :attr:`~hint_animation` parameter equal to `True`.

    .. rubric:: False

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-right-pad.gif
        :align: center

    .. rubric:: True

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-right-pad-true.gif
        :align: center

    :attr:`right_pad` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    root_button_anim = BooleanProperty(False)
    """
    If ``True`` then the root button will rotate 45 degrees when the stack
    is opened.

    :attr:`root_button_anim` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    opening_transition = StringProperty("out_cubic")
    """
    The name of the stack opening animation type.

    :attr:`opening_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    closing_transition = StringProperty("out_cubic")
    """
    The name of the stack closing animation type.

    :attr:`closing_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    opening_transition_button_rotation = StringProperty("out_cubic")
    """
    The name of the animation type to rotate the root button when opening the
    stack.

    :attr:`opening_transition_button_rotation` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    closing_transition_button_rotation = StringProperty("out_cubic")
    """
    The name of the animation type to rotate the root button when closing the
    stack.

    :attr:`closing_transition_button_rotation` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    opening_time = NumericProperty(0.5)
    """
    Time required for the stack to go to: attr:`state` `'open'`.

    :attr:`opening_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    closing_time = NumericProperty(0.2)
    """
    Time required for the stack to go to: attr:`state` `'close'`.

    :attr:`closing_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    opening_time_button_rotation = NumericProperty(0.2)
    """
    Time required to rotate the root button 45 degrees during the stack
    opening animation.

    :attr:`opening_time_button_rotation` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    closing_time_button_rotation = NumericProperty(0.2)
    """
    Time required to rotate the root button 0 degrees during the stack
    closing animation.

    :attr:`closing_time_button_rotation` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    state = OptionProperty("close", options=("close", "open"))
    """
    Indicates whether the stack is closed or open.
    Available options are: `'close'`, `'open'`.

    :attr:`state` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'close'`.
    """

    bg_color_root_button = ColorProperty(None)
    """
    Root button color in (r, g, b, a) format.

    :attr:`bg_color_root_button` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[]`.
    """

    bg_color_stack_button = ColorProperty(None)
    """
    The color of the buttons in the stack (r, g, b, a) format.

    :attr:`bg_color_stack_button` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[]`.
    """

    color_icon_stack_button = ColorProperty(None)
    """
    The color icon of the buttons in the stack (r, g, b, a) format.

    :attr:`color_icon_stack_button` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[]`.
    """

    color_icon_root_button = ColorProperty(None)
    """
    The color icon of the root button (r, g, b, a) format.

    :attr:`color_icon_root_button` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[]`.
    """

    bg_hint_color = ColorProperty(None)
    """
    Background color for the text of the buttons in the stack (r, g, b, a) format.

    :attr:`bg_hint_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    hint_animation = BooleanProperty(False)
    """
    Whether to use button extension animation to display text labels.

    :attr:`hint_animation` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _label_pos_y_set = False
    _anim_buttons_data = {}
    _anim_labels_data = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_close")
        Window.bind(on_resize=self._update_pos_buttons)

    def on_open(self, *args):
        """Called when a stack is opened."""

    def on_close(self, *args):
        """Called when a stack is closed."""

    def on_leave(self, instance_button: MDFloatingBottomButton) -> NoReturn:
        """Called when the mouse cursor goes outside the button of stack."""

        if self.state == "open":
            for widget in self.children:
                if isinstance(widget, MDFloatingLabel) and self.hint_animation:
                    Animation.cancel_all(widget)
                    for item in self.data.items():
                        if widget.text in item:
                            Animation(
                                _canvas_width=0,
                                _padding_right=0,
                                d=self.opening_time,
                                t=self.opening_transition,
                            ).start(instance_button)
                            if self.hint_animation:
                                Animation(
                                    opacity=0, d=0.1, t=self.opening_transition
                                ).start(widget)
                            break
                    break

    def on_enter(self, instance_button: MDFloatingBottomButton) -> NoReturn:
        """Called when the mouse cursor is over a button from the stack."""

        if self.state == "open":
            for widget in self.children:
                if isinstance(widget, MDFloatingLabel) and self.hint_animation:
                    widget._elevation = 0
                    for item in self.data.items():
                        if widget.text in item:
                            Animation(
                                _canvas_width=widget.width + dp(24),
                                _padding_right=dp(5) if self.right_pad else 0,
                                d=self.opening_time,
                                t=self.opening_transition,
                            ).start(instance_button)
                            if self.hint_animation:
                                Animation(
                                    opacity=1,
                                    d=self.opening_time,
                                    t=self.opening_transition,
                                ).start(widget)
                            break
                    break

    def on_data(self, instance_speed_dial, data: dict) -> NoReturn:
        """Creates a stack of buttons."""

        # FIXME: Don't know how to fix AttributeError error:
        # File "kivymd/uix/button.py", line 1597, in on_data
        #     self.add_widget(bottom_button)
        # File "kivy/uix/floatlayout.py", line 140, in add_widget
        #     return super(FloatLayout, self).add_widget(widget, index, canvas)
        # File "kivy/uix/layout.py", line 97, in add_widget
        #     return super(Layout, self).add_widget(widget, index, canvas)
        # File "kivy/uix/widget.py", line 629, in add_widget
        #     canvas.add(widget.canvas)
        # AttributeError: 'NoneType' object has no attribute 'add'
        super().__init__()
        self.clear_widgets()
        self._anim_buttons_data = {}
        self._anim_labels_data = {}
        self._label_pos_y_set = False

        # Bottom buttons.
        for name, name_icon in data.items():
            bottom_button = MDFloatingBottomButton(
                icon=name_icon,
                on_enter=self.on_enter,
                on_leave=self.on_leave,
                opacity=0,
            )
            bottom_button.bind(
                on_release=lambda x=bottom_button: self.callback(x)
            )
            self.set_pos_bottom_buttons(bottom_button)
            self.add_widget(bottom_button)
            # Labels.
            floating_text = name
            if floating_text:
                label = MDFloatingLabel(text=floating_text, opacity=0)
                label.text_color = self.label_text_color
                self.add_widget(label)
        # Top root button.
        root_button = MDFloatingRootButton(on_release=self.open_stack)
        root_button.icon = self.icon
        self.set_pos_root_button(root_button)
        self.add_widget(root_button)

    def on_icon(self, instance_speed_dial, name_icon: str) -> NoReturn:
        self._get_count_widget(MDFloatingRootButton).icon = name_icon

    def on_label_text_color(self, instance_speed_dial, color: list) -> NoReturn:
        for widget in self.children:
            if isinstance(widget, MDFloatingLabel):
                widget.text_color = color

    def on_color_icon_stack_button(
        self, instance_speed_dial, color: list
    ) -> NoReturn:
        for widget in self.children:
            if isinstance(widget, MDFloatingBottomButton):
                widget.text_color = color

    def on_hint_animation(self, instance_speed_dial, value: bool) -> NoReturn:
        for widget in self.children:
            if isinstance(widget, MDFloatingLabel):
                widget.bg_color = (0, 0, 0, 0)

    def on_bg_hint_color(self, instance_speed_dial, color: list) -> NoReturn:
        for widget in self.children:
            if isinstance(widget, MDFloatingBottomButton):
                widget._bg_color = color

    def on_color_icon_root_button(
        self, instance_speed_dial, color: list
    ) -> NoReturn:
        self._get_count_widget(MDFloatingRootButton).text_color = color

    def on_bg_color_stack_button(
        self, instance_speed_dial, color: list
    ) -> NoReturn:
        for widget in self.children:
            if isinstance(widget, MDFloatingBottomButton):
                widget.md_bg_color = color

    def on_bg_color_root_button(
        self, instance_speed_dial, color: list
    ) -> NoReturn:
        self._get_count_widget(MDFloatingRootButton).md_bg_color = color

    def set_pos_labels(
        self, instance_floating_label: MDFloatingLabel
    ) -> NoReturn:
        """
        Sets the position of the floating labels.
        Called when the application's root window is resized.
        """

        if self.anchor == "right":
            instance_floating_label.x = (
                Window.width - instance_floating_label.width - dp(86)
            )

    def set_pos_root_button(
        self, instance_floating_root_button: MDFloatingRootButton
    ) -> NoReturn:
        """
        Sets the position of the root button.
        Called when the application's root window is resized.
        """

        if self.anchor == "right":
            instance_floating_root_button.y = dp(20)
            instance_floating_root_button.x = Window.width - (dp(56) + dp(20))

    def set_pos_bottom_buttons(
        self, instance_floating_bottom_button: MDFloatingBottomButton
    ) -> NoReturn:
        """
        Sets the position of the bottom buttons in a stack.
        Called when the application's root window is resized.
        """

        if self.anchor == "right":
            if self.state != "open":
                instance_floating_bottom_button.y = (
                    instance_floating_bottom_button.height / 2
                )
            instance_floating_bottom_button.x = Window.width - (
                instance_floating_bottom_button.height
                + instance_floating_bottom_button.width / 2
            )

    def open_stack(
        self, instance_floating_root_button: MDFloatingRootButton
    ) -> NoReturn:
        """Opens a button stack."""

        for widget in self.children:
            if isinstance(widget, MDFloatingLabel):
                Animation.cancel_all(widget)

        if self.state != "open":
            y = 0
            label_position = dp(56)
            anim_buttons_data = {}
            anim_labels_data = {}

            for widget in self.children:
                if isinstance(widget, MDFloatingBottomButton):
                    # Sets new button positions.
                    y += dp(56)
                    widget.y = widget.y * 2 + y
                    if not self._anim_buttons_data:
                        anim_buttons_data[widget] = Animation(
                            opacity=1,
                            d=self.opening_time,
                            t=self.opening_transition,
                        )
                elif isinstance(widget, MDFloatingLabel):
                    # Sets new labels positions.
                    label_position += dp(56)
                    # Sets the position of signatures only once.
                    if not self._label_pos_y_set:
                        widget.y = widget.y * 2 + label_position
                        widget.x = Window.width - widget.width - dp(86)
                    if not self._anim_labels_data:
                        anim_labels_data[widget] = Animation(
                            opacity=1, d=self.opening_time
                        )
                elif (
                    isinstance(widget, MDFloatingRootButton)
                    and self.root_button_anim
                ):
                    # Rotates the root button 45 degrees.
                    Animation(
                        _angle=-45,
                        d=self.opening_time_button_rotation,
                        t=self.opening_transition_button_rotation,
                    ).start(widget)

            if anim_buttons_data:
                self._anim_buttons_data = anim_buttons_data
            if anim_labels_data and not self.hint_animation:
                self._anim_labels_data = anim_labels_data

            self.state = "open"
            self.dispatch("on_open")
            self.do_animation_open_stack(self._anim_buttons_data)
            self.do_animation_open_stack(self._anim_labels_data)
            if not self._label_pos_y_set:
                self._label_pos_y_set = True
        else:
            self.close_stack()

    def do_animation_open_stack(self, anim_data: dict) -> NoReturn:
        """
        :param anim_data:
            {
                <kivymd.uix.button.MDFloatingBottomButton object>:
                    <kivy.animation.Animation>,
                <kivymd.uix.button.MDFloatingBottomButton object>:
                    <kivy.animation.Animation object>,
                ...,
            }
        """

        def on_progress(animation, widget, value):
            if value >= 0.1:
                animation_open_stack()

        def animation_open_stack(*args):
            try:
                widget = next(widgets_list)
                animation = anim_data[widget]
                animation.bind(on_progress=on_progress)
                animation.start(widget)
            except StopIteration:
                pass

        widgets_list = iter(list(anim_data.keys()))
        animation_open_stack()

    def close_stack(self):
        """Closes the button stack."""

        for widget in self.children:
            if isinstance(widget, MDFloatingBottomButton):
                Animation(
                    y=widget.height / 2,
                    d=self.closing_time,
                    t=self.closing_transition,
                    opacity=0,
                ).start(widget)
            elif isinstance(widget, MDFloatingLabel):
                Animation(opacity=0, d=0.1).start(widget)
            elif (
                isinstance(widget, MDFloatingRootButton)
                and self.root_button_anim
            ):
                Animation(
                    _angle=0,
                    d=self.closing_time_button_rotation,
                    t=self.closing_transition_button_rotation,
                ).start(widget)
        self.state = "close"
        self.dispatch("on_close")

    def _update_pos_buttons(self, instance, width, height):
        # Updates button positions when resizing screen.
        for widget in self.children:
            if isinstance(widget, MDFloatingBottomButton):
                self.set_pos_bottom_buttons(widget)
            elif isinstance(widget, MDFloatingRootButton):
                self.set_pos_root_button(widget)
            elif isinstance(widget, MDFloatingLabel):
                self.set_pos_labels(widget)

    def _get_count_widget(self, instance):
        widget = None
        for widget in self.children:
            if isinstance(widget, instance):
                break
        return widget
