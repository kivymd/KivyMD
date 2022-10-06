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

.. tabs::

    .. tab:: Declarative KV style

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
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDIconButton
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDIconButton(
                                icon="language-python",
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-button.png
    :align: center

The :class:`~MDIconButton.icon` parameter must have the name of the icon
from ``kivymd/icon_definitions.py`` file.

You can also use custom icons:

.. code-block:: kv

    MDIconButton:
        icon: "kivymd/images/logo/kivymd-icon-256.png"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-custom-button.png
    :align: center

By default, :class:`~MDIconButton` button has a size ``(dp(48), dp (48))``.
Use :class:`~BaseButton.icon_size` attribute to resize the button:

.. code-block:: kv

    MDIconButton:
        icon: "android"
        icon_size: "64sp"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-button-user-font-size.png
    :align: center

By default, the color of :class:`~MDIconButton`
(depending on the style of the application) is black or white.
You can change the color of :class:`~MDIconButton` as the text color
of :class:`~kivymd.uix.label.MDLabel`, substituting ``theme_icon_color`` for
``theme_text_color`` and ``icon_color`` for ``text_color``.

.. code-block:: kv

    MDIconButton:
        icon: "android"
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color

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

    from kivymd.app import MDApp
    from kivymd.uix.button import MDFloatingActionButton

    KV = '''
    MDScreen:
        md_bg_color: "#f7f2fa"

        MDBoxLayout:
            id: box
            spacing: "56dp"
            adaptive_size: True
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
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
                        theme_icon_color="Custom",
                        md_bg_color=data[type_button]["md_bg_color"],
                        icon_color=data[type_button]["text_color"],
                    )
                )


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-floating-action-button-m3.png
    :align: center

.. MDFlatButton:
MDFlatButton
------------

To change the text color of: class:`~MDFlatButton` use the ``text_color`` parameter:

.. code-block:: kv

    MDFlatButton:
        text: "MDFlatButton"
        theme_text_color: "Custom"
        text_color: "orange"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-flat-button-text-color.png
    :align: center

Or use markup:

.. code-block:: kv

    MDFlatButton:
        text: "[color=#00ffcc]MDFlatButton[/color]"

To specify the font size and font name, use the parameters as in the usual
`Kivy` buttons:

.. code-block:: kv

    MDFlatButton:
        text: "MDFlatButton"
        font_size: "18sp"
        font_name: "path/to/font"

.. MDRaisedButton:
MDRaisedButton
--------------

This button is similar to the :class:`~MDFlatButton` button except that you
can set the background color for :class:`~MDRaisedButton`:

.. code-block:: kv

    MDRaisedButton:
        text: "MDRaisedButton"
        md_bg_color: "red"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-raised-button.png
    :align: center

.. MDRectangleFlatButton:
MDRectangleFlatButton
---------------------

.. code-block:: kv

    MDRectangleFlatButton:
        text: "MDRectangleFlatButton"
        theme_text_color: "Custom"
        text_color: "white"
        line_color: "red"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-rectangle-flat-button-md-bg-color.png
    :align: center

.. MDRectangleFlatIconButton:
MDRectangleFlatIconButton
-------------------------

Button parameters :class:`~MDRectangleFlatIconButton` are the same as
button :class:`~MDRectangleFlatButton`, with the addition of the
``theme_icon_color`` and ``icon_color`` parameters as for :class:`~MDIconButton`.

.. code-block:: kv

    MDRectangleFlatIconButton:
        icon: "android"
        text: "MDRectangleFlatIconButton"
        theme_text_color: "Custom"
        text_color: "white"
        line_color: "red"
        theme_icon_color: "Custom"
        icon_color: "orange"

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
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return (
                MDScreen(
                    MDRectangleFlatIconButton(
                        text="MDRectangleFlatIconButton",
                        icon="language-python",
                        line_color=(0, 0, 0, 0),
                        pos_hint={"center_x": .5, "center_y": .5},
                    )
                )
            )


    Example().run()

.. code-block:: kv

    MDRectangleFlatIconButton:
        text: "MDRectangleFlatIconButton"
        icon: "language-python"
        line_color: 0, 0, 0, 0
        pos_hint: {"center_x": .5, "center_y": .5}

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-rectangle-flat-icon-button-without-border.png
    :align: center

.. MDRoundFlatButton:
MDRoundFlatButton
-----------------

.. code-block:: kv

    MDRoundFlatButton:
        text: "MDRoundFlatButton"
        text_color: "white"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-round-flat-button-text-color.png
    :align: center

.. MDRoundFlatIconButton:
MDRoundFlatIconButton
---------------------

Button parameters :class:`~MDRoundFlatIconButton` are the same as
button :class:`~MDRoundFlatButton`, with the addition of the
``theme_icon_color`` and ``icon_color`` parameters as for :class:`~MDIconButton`:

.. code-block:: kv

    MDRoundFlatIconButton:
        text: "MDRoundFlatIconButton"
        icon: "android"
        text_color: "white"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-round-flat-icon-button.png
    :align: center

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
button :class:`~MDRaisedButton`, with the addition of the
``theme_icon_color`` and ``icon_color`` parameters as for :class:`~MDIconButton`.

.. note:: Notice that the width of the :class:`~MDFillRoundFlatIconButton`
    button matches the size of the button text.

.. MDTextButton:
MDTextButton
------------

.. code-block:: kv

    MDTextButton:
        text: "MDTextButton"
        custom_color: "white"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-text-button.png
    :align: center

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
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial.gif
    :align: center

Or without KV Language:

.. tabs::

    .. tab:: Imperative python style

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
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    screen = MDScreen()
                    speed_dial = MDFloatingActionButtonSpeedDial()
                    speed_dial.data = self.data
                    speed_dial.root_button_anim = True
                    screen.add_widget(speed_dial)
                    return screen


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.uix.screen import MDScreen
            from kivymd.app import MDApp
            from kivymd.uix.button import MDFloatingActionButtonSpeedDial


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDFloatingActionButtonSpeedDial(
                                data={
                                    'Python': 'language-python',
                                    'PHP': 'language-php',
                                    'C++': 'language-cpp',
                                },
                                root_button_anim=True,
                            )
                        )
                    )


            Example().run()

You can use various types of animation of labels for buttons on the stack:

.. code-block:: kv

    MDFloatingActionButtonSpeedDial:
        hint_animation: True

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-hint.gif
    :align: center

You can set your color values for background, text of buttons etc:

.. code-block:: kv

    MDFloatingActionButtonSpeedDial:
        hint_animation: True
        bg_hint_color: app.theme_cls.primary_dark

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-hint-color.png
    :align: center

Binds to individual buttons
---------------------------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import DictProperty

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDFloatingActionButtonSpeedDial:
                    id: speed_dial
                    data: app.data
                    root_button_anim: True
                    hint_animation: True
            '''


            class Example(MDApp):
                data = DictProperty()

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    self.data = {
                        'Python': 'language-python',
                        'JS': [
                            'language-javascript',
                            "on_press", lambda x: print("pressed JS"),
                            "on_release", lambda x: print(
                                "stack_buttons",
                                self.root.ids.speed_dial.stack_buttons
                            )
                        ],
                        'PHP': [
                            'language-php',
                            "on_press", lambda x: print("pressed PHP"),
                            "on_release", self.callback
                        ],
                        'C++': [
                            'language-cpp',
                            "on_press", lambda x: print("pressed C++"),
                            "on_release", lambda x: self.callback()
                        ],
                    }
                    return Builder.load_string(KV)

                def callback(self, *args):
                    print(args)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDFloatingActionButtonSpeedDial
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDFloatingActionButtonSpeedDial(
                                id="speed_dial",
                                hint_animation=True,
                                root_button_anim=True,
                            )
                        )
                    )

                def on_start(self):
                    data = {
                        "Python": "language-python",
                        "JS": [
                            "language-javascript",
                            "on_press", lambda x: print("pressed JS"),
                            "on_release", lambda x: print(
                                "stack_buttons",
                                self.root.ids.speed_dial.stack_buttons
                            )
                        ],
                        "PHP": [
                            "language-php",
                            "on_press", lambda x: print("pressed PHP"),
                            "on_release", self.callback
                        ],
                        "C++": [
                            "language-cpp",
                            "on_press", lambda x: print("pressed C++"),
                            "on_release", lambda x: self.callback()
                        ],
                    }
                    self.root.ids.speed_dial.data = data

                def callback(self, *args):
                    print(args)


            Example().run()
"""

from __future__ import annotations

__all__ = (
    "BaseButton",
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
from typing import Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import (
    BooleanProperty,
    BoundedNumericProperty,
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
from kivy.uix.floatlayout import FloatLayout
from kivy.weakproxy import WeakProxy

from kivymd import uix_path
from kivymd.color_definitions import text_colors
from kivymd.font_definitions import theme_font_styles
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    CommonElevationBehavior,
    DeclarativeBehavior,
    RectangularRippleBehavior,
    RotateBehavior,
)
from kivymd.uix.label import MDLabel
from kivymd.uix.tooltip import MDTooltip

with open(
    os.path.join(uix_path, "button", "button.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


theme_text_color_options = (
    "Primary",
    "Secondary",
    "Hint",
    "Error",
    "Custom",
    "ContrastParentBackground",
)

# FIXME: If you set a new elevation value for the button
#  (press the "Set elevation" button), then disable the button
#  (press the "Disabled" button), and then enable the button
#  (press the "Undisabled" button), then the previously set elevation value is
#  reset to zero.
#  In addition, if you set a new elevation value
#  (press the "Set elevation" button) and click on the button for which we set
#  the elevation value, then the new elevation value will receive the previous
#  elevation value. This problem is only related to the buttons.
#  For example, there is no such problem for the MDCard widget.

"""
from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:

    MDRaisedButton:
        size_hint: .5, .5
        id: button
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 0

    MDBoxLayout:
        adaptive_size: True
        pos_hint: {"center_x": .5}
        spacing: 12
        padding: 12

        MDRaisedButton:
            text: "Set elevation"
            pos_hint: {"center_x": .5, "bottom": 1}
            on_release: button.elevation = 4

        MDRaisedButton:
            text: "Disabled"
            pos_hint: {"center_x": .5, "bottom": 1}
            on_release: button.disabled = True

        MDRaisedButton:
            text: "Undisabled"
            pos_hint: {"center_x": .5, "bottom": 1}
            on_release: button.disabled = False
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()
"""


class BaseButton(
    DeclarativeBehavior,
    RectangularRippleBehavior,
    ThemableBehavior,
    ButtonBehavior,
    AnchorLayout,
):
    """
    Base class for all buttons.

    For more information, see in the
    :class:`~kivy.uix.anchorlayout.AnchorLayout` class documentation.
    """

    padding = VariableListProperty([dp(16), dp(8), dp(16), dp(8)])
    """
    Padding between the widget box and its children, in pixels:
    [padding_left, padding_top, padding_right, padding_bottom].

    padding also accepts a two argument form [padding_horizontal,
    padding_vertical] and a one argument form [padding].

    .. versionadded:: 1.0.0

    :attr:`padding` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to [16dp, 8dp, 16dp, 8dp].
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

    text = StringProperty("")
    """
    Button text.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon = StringProperty("")
    """
    Button icon.

    :attr:`icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    font_style = OptionProperty("Body1", options=theme_font_styles)
    """
    Button text font style.

    Available vanilla font_style are: `'H1'`, `'H2'`, `'H3'`, `'H4'`, `'H5'`,
    `'H6'`, `'Subtitle1'`, `'Subtitle2'`, `'Body1'`, `'Body2'`, `'Button'`,
    `'Caption'`, `'Overline'`, `'Icon'`.

    :attr:`font_style` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Body1'`.
    """

    theme_text_color = OptionProperty(None, options=theme_text_color_options)
    """
    Button text type. Available options are: (`"Primary"`, `"Secondary"`,
    `"Hint"`, `"Error"`, `"Custom"`, `"ContrastParentBackground"`).

    :attr:`theme_text_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None` (set by button class).
    """

    theme_icon_color = OptionProperty(None, options=theme_text_color_options)
    """
    Button icon type. Available options are: (`"Primary"`, `"Secondary"`,
    `"Hint"`, `"Error"`, `"Custom"`, `"ContrastParentBackground"`).

    .. versionadded:: 1.0.0

    :attr:`theme_icon_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None` (set by button subclass).
    """

    text_color = ColorProperty(None)
    """
    Button text color in (r, g, b, a) or string format.

    :attr:`text_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color = ColorProperty(None)
    """
    Button icon color in (r, g, b, a) or string format.

    :attr:`icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    font_name = StringProperty()
    """
    Button text font name.

    :attr:`font_name` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    font_size = NumericProperty("14sp")
    """
    Button text font size.

    :attr:`font_size` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `14sp`.
    """

    icon_size = NumericProperty()
    """
    Icon font size.
    Use this parameter as the font size, that is, in sp units.

    .. versionadded:: 1.0.0

    :attr:`icon_size` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    line_width = NumericProperty(1)
    """
    Line width for button border.

    :attr:`line_width` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    line_color = ColorProperty(None)
    """
    Line color in (r, g, b, a) or string format for button border.

    :attr:`line_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    line_color_disabled = ColorProperty(None)
    """
    Disabled line color in (r, g, b, a) or string format for button border.

    .. versionadded:: 1.0.0

    :attr:`line_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    md_bg_color = ColorProperty(None)
    """
    Button background color in (r, g, b, a) or string format.

    :attr:`md_bg_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the button when
    the button is disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    disabled_color = ColorProperty(None)
    """
    The color of the text and icon when the button is disabled,
    in (r, g, b, a) or string format.

    .. versionadded:: 1.0.0

    :attr:`disabled_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    rounded_button = BooleanProperty(False)
    """
    Should the button have fully rounded corners (e.g. like M3 buttons)?

    .. versionadded:: 1.0.0

    :attr:`rounded_button` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    # Note - _radius must be > 0 to avoid rendering issues.
    _radius = BoundedNumericProperty(dp(4), min=0.0999, errorvalue=0.1)
    # Properties used for rendering.
    _disabled_color = ColorProperty([0.0, 0.0, 0.0, 0.0])
    _md_bg_color = ColorProperty([0.0, 0.0, 0.0, 0.0])
    _md_bg_color_disabled = ColorProperty([0.0, 0.0, 0.0, 0.0])
    _line_color = ColorProperty([0.0, 0.0, 0.0, 0.0])
    _line_color_disabled = ColorProperty([0.0, 0.0, 0.0, 0.0])
    _theme_text_color = OptionProperty(None, options=theme_text_color_options)
    _theme_icon_color = OptionProperty(None, options=theme_text_color_options)
    _text_color = ColorProperty(None)
    _icon_color = ColorProperty(None)

    # Defaults which can be overridden in subclasses
    _min_width = NumericProperty(dp(64))
    _min_height = NumericProperty(dp(36))

    # Default colors - set to None to use primary theme colors
    _default_md_bg_color = [0.0, 0.0, 0.0, 0.0]
    _default_md_bg_color_disabled = [0.0, 0.0, 0.0, 0.0]
    _default_line_color = [0.0, 0.0, 0.0, 0.0]
    _default_line_color_disabled = [0.0, 0.0, 0.0, 0.0]
    _default_theme_text_color = StringProperty("Primary")
    _default_theme_icon_color = StringProperty("Primary")
    _default_text_color = ColorProperty(None)
    _default_icon_color = ColorProperty(None)

    _animation_fade_bg = ObjectProperty(None, allownone=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_cls.bind(
            primary_palette=self.set_all_colors,
            theme_style=self.set_all_colors,
        )
        self.bind(
            md_bg_color=self.set_button_colors,
            md_bg_color_disabled=self.set_button_colors,
            line_color=self.set_button_colors,
            line_color_disabled=self.set_button_colors,
            theme_text_color=self.set_text_color,
            text_color=self.set_text_color,
            theme_icon_color=self.set_icon_color,
            icon_color=self.set_icon_color,
            disabled_color=self.set_disabled_color,
            rounded_button=self.set_radius,
            height=self.set_radius,
        )
        Clock.schedule_once(self.set_all_colors)
        Clock.schedule_once(self.set_radius)

    def set_disabled_color(self, *args):
        """
        Sets the color for the icon, text and line of the button when button
        is disabled.
        """

        if self.disabled:
            disabled_color = (
                self.disabled_color
                if self.disabled_color
                else self.theme_cls.disabled_hint_text_color
            )
            self._disabled_color = disabled_color
            # Button icon color.
            if "lbl_ic" in self.ids:
                self.ids.lbl_ic.disabled_color = disabled_color
            # Button text color.
            if "lbl_txt" in self.ids:
                self.ids.lbl_txt.disabled_color = disabled_color
        else:
            self._disabled_color = self._line_color

    def set_all_colors(self, *args) -> None:
        """Set all button colours."""

        self.set_button_colors()
        self.set_text_color()
        self.set_icon_color()

    def set_button_colors(self, *args) -> None:
        """Set all button colours (except text/icons)."""

        # Set main color
        _md_bg_color = (
            self.md_bg_color
            or self._default_md_bg_color
            or self.theme_cls.primary_color
        )

        # Set disabled color
        _md_bg_color_disabled = (
            self.md_bg_color_disabled
            or (
                [sum(self.md_bg_color[0:3]) / 3.0] * 3
                + [0.38 if self.theme_cls.theme_style == "Light" else 0.5]
                if self.md_bg_color
                else None
            )
            or self._default_md_bg_color_disabled
            or self.theme_cls.disabled_primary_color
        )

        # Set line color
        _line_color = (
            self.line_color
            or self._default_line_color
            or self.theme_cls.primary_color
        )

        # Set disabled line color
        _line_color_disabled = (
            self.line_color_disabled
            or (
                [sum(self.line_color[0:3]) / 3.0] * 3
                + [0.38 if self.theme_cls.theme_style == "Light" else 0.5]
                if self.line_color
                else None
            )
            or self._default_line_color_disabled
            or self.theme_cls.disabled_primary_color
        )

        if self.theme_cls.theme_style_switch_animation:
            Animation(
                _md_bg_color=_md_bg_color,
                _md_bg_color_disabled=_md_bg_color_disabled,
                _line_color=_line_color,
                _line_color_disabled=_line_color_disabled,
                d=self.theme_cls.theme_style_switch_animation_duration,
                t="linear",
            ).start(self)
        else:
            self._md_bg_color = _md_bg_color
            self._md_bg_color_disabled = _md_bg_color_disabled
        self._line_color = _line_color
        self._line_color_disabled = _line_color_disabled

    def set_text_color(self, *args) -> None:
        """
        Set _theme_text_color and _text_color based on defaults and options.
        """

        self._theme_text_color = (
            self.theme_text_color or self._default_theme_text_color
        )
        if self._default_text_color == "PrimaryHue":
            default_text_color = text_colors[self.theme_cls.primary_palette][
                self.theme_cls.primary_hue
            ]
        elif self._default_text_color == "Primary":
            default_text_color = self.theme_cls.primary_color
        else:
            default_text_color = self.theme_cls.text_color
        self._text_color = self.text_color or default_text_color

    def set_icon_color(self, *args) -> None:
        """
        Set _theme_icon_color and _icon_color based on defaults and options.
        """

        self._theme_icon_color = (
            (self.theme_icon_color or self._default_theme_icon_color)
            if not self.disabled
            else "Custom"
        )
        if self._default_icon_color == "PrimaryHue":
            default_icon_color = text_colors[self.theme_cls.primary_palette][
                self.theme_cls.primary_hue
            ]
        elif self._default_icon_color == "Primary":
            default_icon_color = self.theme_cls.primary_color
        else:
            default_icon_color = self.theme_cls.text_color
        self._icon_color = self.icon_color or default_icon_color

    def set_radius(self, *args) -> None:
        """
        Set the radius, if we are a rounded button, based on the
        current height.
        """

        if self.rounded_button:
            self._radius = self.height / 2

    # Touch events that cause transparent buttons to fade to background
    def on_touch_down(self, touch):
        """
        Animates fade to background on press, for buttons with no
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
            Animation(duration=0.05, _md_bg_color=md_bg_color).start(self)
        return super().on_touch_up(touch)

    def on_disabled(self, instance_button, disabled_value: bool) -> None:
        if hasattr(super(), "on_disabled"):
            if self.disabled is True:
                Animation.cancel_all(self, "elevation")
            super().on_disabled(instance_button, disabled_value)
        Clock.schedule_once(self.set_disabled_color)


class ButtonElevationBehaviour(CommonElevationBehavior):
    """
    Implements elevation behavior as well as the recommended down/disabled
    colors for raised buttons.

    The minimum elevation for any raised button is `'1dp'`,
    by default, set to `'2dp'`.

    The `_elevation_raised` is automatically computed and is set to
    `self.elevation + 6` each time `self.elevation` is updated.
    """

    _elevation_raised = NumericProperty()
    _anim_raised = ObjectProperty(None, allownone=True)
    _default_elevation = 3

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.elevation == 0:
            self.elevation = self._default_elevation
        if hasattr(self, "radius"):
            self.bind(_radius=self.setter("radius"))
        Clock.schedule_once(self.create_anim_raised)
        self.on_disabled(self, self.disabled)

    def create_anim_raised(self, *args) -> None:
        self._elevation_raised = self.elevation + 1.2
        self._anim_raised = Animation(elevation=self.elevation + 1, d=0.15)

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
                self.stop_elevation_anim()
                return super().on_touch_up(touch)
            self.stop_elevation_anim()
        return super().on_touch_up(touch)

    def stop_elevation_anim(self):
        Animation.cancel_all(self, "elevation")
        self.elevation = self._elevation_raised - 1


class ButtonContentsText:
    """Contents for :class:`~BaseButton` class consisting of a single label."""


class ButtonContentsIcon:
    """
    Contents for a round BaseButton consisting of an :class:`~MDIcon` class.
    """

    _min_width = NumericProperty(0)

    def on_text_color(self, instance_button, color: list) -> None:
        """
        Set icon_color equal to text_color.
        For backwards compatibility - can use text_color instead
        of icon_color.
        """

        if color:
            self.icon_color = color


class ButtonContentsIconText:
    """
    Contents for :class:`~BaseButton` class consisting of a
    :class:`~kivy.uix.boxlayout.BoxLayout` with an icon and a label.
    """

    padding = VariableListProperty([dp(12), dp(8), dp(16), dp(8)])
    """
    Padding between the widget box and its children, in pixels:
    [padding_left, padding_top, padding_right, padding_bottom].

    padding also accepts a two argument form [padding_horizontal,
    padding_vertical] and a one argument form [padding].

    .. versionadded:: 1.0.0

    :attr:`padding` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to [12dp, 8dp, 16dp, 8dp].
    """


# Old MD Button classes


class OldButtonIconMixin:
    """Backwards-compatibility for icons."""

    icon = StringProperty("android")

    def on_icon_color(self, instance_button, color: list) -> None:
        """
        If we are setting an icon color, set theme_icon_color to Custom.
        For backwards compatibility (before theme_icon_color existed).
        """

        if color and (self.theme_text_color == "Custom"):
            self.theme_icon_color = "Custom"


class MDFlatButton(BaseButton, ButtonContentsText):
    """
    A flat rectangular button with (by default) no border or background.
    Text is the default text color.
    """

    padding = VariableListProperty([dp(8), dp(8), dp(8), dp(8)])
    """
    Padding between the widget box and its children, in pixels:
    [padding_left, padding_top, padding_right, padding_bottom].

    padding also accepts a two argument form [padding_horizontal,
    padding_vertical] and a one argument form [padding].

    .. versionadded:: 1.0.0

    :attr:`padding` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to [8dp, 8dp, 8dp, 8dp].
    """


class MDRaisedButton(BaseButton, ButtonElevationBehaviour, ButtonContentsText):
    """
    A flat button with (by default) a primary color fill and matching
    color text.
    """

    # FIXME: Move the underlying attributes to the :class:`~BaseButton` class.
    #  This applies to all classes of buttons that have similar attributes.
    _default_md_bg_color = None
    _default_md_bg_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_text_color = "PrimaryHue"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shadow_softness = 8
        self.shadow_offset = (0, 2)
        self.shadow_radius = self._radius * 2


class MDRectangleFlatButton(BaseButton, ButtonContentsText):
    """
    A flat button with (by default) a primary color border and primary
    color text.
    """

    _default_line_color = None
    _default_line_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_text_color = "Primary"


class MDRectangleFlatIconButton(
    BaseButton, OldButtonIconMixin, ButtonContentsIconText
):
    """
    A flat button with (by default) a primary color border, primary color text
    and a primary color icon on the left.
    """

    _default_line_color = None
    _default_line_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_theme_icon_color = "Custom"
    _default_text_color = "Primary"
    _default_icon_color = "Primary"


class MDRoundFlatButton(BaseButton, ButtonContentsText):
    """
    A flat button with (by default) fully rounded corners, a primary
    color border and primary color text.
    """

    _default_line_color = None
    _default_line_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_text_color = "Primary"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rounded_button = True


class MDRoundFlatIconButton(
    BaseButton, OldButtonIconMixin, ButtonContentsIconText
):
    """
    A flat button with (by default) rounded corners, a primary color border,
    primary color text and a primary color icon on the left.
    """

    _default_line_color = None
    _default_line_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_theme_icon_color = "Custom"
    _default_text_color = "Primary"
    _default_icon_color = "Primary"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rounded_button = True


class MDFillRoundFlatButton(BaseButton, ButtonContentsText):
    """
    A flat button with (by default) rounded corners, a primary color fill
    and primary color text.
    """

    _default_md_bg_color = None
    _default_md_bg_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_text_color = "PrimaryHue"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rounded_button = True


class MDFillRoundFlatIconButton(
    BaseButton, OldButtonIconMixin, ButtonContentsIconText
):
    """
    A flat button with (by default) rounded corners, a primary color fill,
    primary color text and a primary color icon on the left.
    """

    _default_md_bg_color = None
    _default_md_bg_color_disabled = None
    _default_theme_text_color = "Custom"
    _default_theme_icon_color = "Custom"
    _default_text_color = "PrimaryHue"
    _default_icon_color = "PrimaryHue"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rounded_button = True


class MDIconButton(BaseButton, OldButtonIconMixin, ButtonContentsIcon):
    """A simple rounded icon button."""

    icon = StringProperty("checkbox-blank-circle")
    """
    Button icon.

    :attr:`icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle'`.
    """

    _min_width = NumericProperty(0)
    _default_icon_pad = max(dp(48) - sp(24), 0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rounded_button = True
        # FIXME: GraphicException: Invalid width value, must be > 0
        self.line_width = 0.001
        Clock.schedule_once(self.set_size)

    def set_size(self, interval: Union[int, float]) -> None:
        """
        Sets the icon width/height based on the current `icon_size`
        attribute, or the default value if it is zero. The icon size
        is set to `(48, 48)` for an icon with the default font_size 24sp.
        """
        diameter = self._default_icon_pad + (self.icon_size or sp(24))
        self.width = diameter
        self.height = diameter


class MDFloatingActionButton(
    BaseButton, OldButtonIconMixin, ButtonElevationBehaviour, ButtonContentsIcon
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
    _default_theme_icon_color = "Custom"
    _default_icon_color = "PrimaryHue"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # FIXME: GraphicException: Invalid width value, must be > 0
        self.line_width = 0.001
        self.theme_cls.bind(material_style=self.set_size_and_radius)
        Clock.schedule_once(self.set_size)
        Clock.schedule_once(self.set__radius)
        Clock.schedule_once(self.set_font_size)

    def set_font_size(self, *args) -> None:
        if self.theme_cls.material_style == "M3":
            if self.type == "large":
                self.icon_size = "36sp"
            else:
                self.icon_size = 0

    def set__radius(self, *args) -> None:
        if self.theme_cls.material_style == "M2":
            self.shadow_radius = self.height / 2
            self.rounded_button = True
        else:
            self.shadow_softness = 8
            self.shadow_offset = (0, 2)
            self.rounded_button = False

            if self.type == "small":
                self._radius = dp(12)
            elif self.type == "standard":
                self._radius = dp(16)
            elif self.type == "large":
                self._radius = dp(28)

            self.shadow_radius = self._radius

    def set_size_and_radius(self, *args) -> None:
        self.set_size(args)
        self.set__radius(args)

    def set_size(self, *args) -> None:
        if self.theme_cls.material_style == "M2":
            self.size = dp(56), dp(56)
        else:
            if self.type == "small":
                self.size = dp(40), dp(40)
            elif self.type == "standard":
                self.size = dp(56), dp(56)
            elif self.type == "large":
                self.size = dp(96), dp(96)

    def on_type(self, instance_md_floating_action_button, type: str) -> None:
        self.set_size()
        self.set_font_size()


class MDTextButton(ButtonBehavior, MDLabel):
    color = ColorProperty(None)
    """
    Button color in (r, g, b, a) or string format.

    :attr:`color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    color_disabled = ColorProperty(None)
    """
    Button color disabled in (r, g, b, a) or string format.

    :attr:`color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _color = ColorProperty(None)  # last current button text color

    def animation_label(self) -> None:
        def set_default_state_label(*args):
            Animation(opacity=1, d=0.1, t="in_out_cubic").start(self)

        anim = Animation(opacity=0.5, d=0.2, t="in_out_cubic")
        anim.bind(on_complete=set_default_state_label)
        anim.start(self)

    def on_press(self, *args):
        self.animation_label()
        return super().on_press(*args)

    def on_disabled(self, instance_button, disabled_value) -> None:
        if disabled_value:
            if not self.color_disabled:
                self.color_disabled = self.theme_cls.disabled_hint_text_color
                self._color = self.color
            self.text_color = self.color_disabled
        else:
            self.text_color = self._color


# SpeedDial classes


class BaseFloatingBottomButton(MDFloatingActionButton, MDTooltip):
    _canvas_width = NumericProperty(0)
    _padding_right = NumericProperty(0)
    _bg_color = ColorProperty(None)

    def set_size(self, interval: Union[int, float]) -> None:
        self.width = "46dp"
        self.height = "46dp"


class MDFloatingBottomButton(BaseFloatingBottomButton):
    _bg_color = ColorProperty(None)


class MDFloatingRootButton(RotateBehavior, MDFloatingActionButton):
    rotate_value_angle = NumericProperty(0)


class MDFloatingLabel(MDLabel):
    bg_color = ColorProperty([0, 0, 0, 0])


class MDFloatingActionButtonSpeedDial(
    DeclarativeBehavior, ThemableBehavior, FloatLayout
):
    """
    For more information, see in the
    :class:`~kivy.uix.floatlayout.FloatLayout` class documentation.

    :Events:
        :attr:`on_open`
            Called when a stack is opened.
        :attr:`on_close`
            Called when a stack is closed.
        :attr:`on_press_stack_button`
            Called at the on_press event for the stack button.
        :attr:`on_release_stack_button`
            Called at the on_press event for the stack button.
    """

    icon = StringProperty("plus")
    """
    Root button icon name.

    .. code-block:: kv

        MDFloatingActionButtonSpeedDial:
            icon: "pencil"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-icon.png
        :align: center

    :attr:`icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'plus'`.
    """

    anchor = OptionProperty("right", option=["right"])
    """
    Stack anchor. Available options are: `'right'`.

    :attr:`anchor` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'right'`.
    """

    label_text_color = ColorProperty(None)
    """
    Color of floating text labels in (r, g, b, a) or string format.

    .. code-block:: kv

        MDFloatingActionButtonSpeedDial:
            label_text_color: "orange"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-label-text-color.png
        :align: center

    :attr:`label_text_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    label_bg_color = ColorProperty([0, 0, 0, 0])
    """
    Background color of floating text labels in (r, g, b, a) or string format.

    .. code-block:: kv

        MDFloatingActionButtonSpeedDial:
            label_text_color: "black"
            label_bg_color: "orange"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-label-bg-color.png
        :align: center

    :attr:`label_bg_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    label_radius = VariableListProperty([0], length=4)
    """
    The radius of the background of floating text labels.

    .. code-block:: kv

        MDFloatingActionButtonSpeedDial:
            label_text_color: "black"
            label_bg_color: "orange"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-label-radius.png
        :align: center

    :attr:`label_radius` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    data = DictProperty()
    """
    Must be a dictionary.

    .. code-block:: python

        {
            'name-icon': 'Text label',
            ...,
            ...,
        }
    """

    right_pad = BooleanProperty(False)
    """
    If `True`, the background for the floating text label will increase by the
    number of pixels specified in the :attr:`~right_pad_value` parameter.

    Works only if the :attr:`~hint_animation` parameter is set to `True`.

    .. rubric:: False

    .. code-block:: kv

        MDFloatingActionButtonSpeedDial:
            hint_animation: True
            right_pad: False

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-right-pad.gif
        :align: center

    .. rubric:: True

    .. code-block:: kv

        MDFloatingActionButtonSpeedDial:
            hint_animation: True
            right_pad: True
            right_pad_value: "10dp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-right-pad-true.gif
        :align: center

    :attr:`right_pad` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    right_pad_value = NumericProperty(0)
    """
    See :attr:`~right_pad` parameter for more information.

    :attr:`right_pad_value` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
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
    Background color of root button in (r, g, b, a) or string format.

    .. code-clock:: kv

        MDFloatingActionButtonSpeedDial:
            bg_color_root_button: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-bg-color-root-button.png
        :align: center

    :attr:`bg_color_root_button` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    bg_color_stack_button = ColorProperty(None)
    """
    Background color of the stack buttons in (r, g, b, a) or string format.

    .. code-clock:: kv

        MDFloatingActionButtonSpeedDial:
            bg_color_root_button: "red"
            bg_color_stack_button: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-bg-color-stack-button.png
        :align: center

    :attr:`bg_color_stack_button` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    color_icon_stack_button = ColorProperty(None)
    """
    The color icon of the stack buttons in (r, g, b, a) or string format.

    .. code-clock:: kv

        MDFloatingActionButtonSpeedDial:
            bg_color_root_button: "red"
            bg_color_stack_button: "red"
            color_icon_stack_button: "white"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-color-icon-stack-button.png
        :align: center

    :attr:`color_icon_stack_button` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    color_icon_root_button = ColorProperty(None)
    """
    The color icon of the root button in (r, g, b, a) or string format.

    .. code-clock:: kv

        MDFloatingActionButtonSpeedDial:
            bg_color_root_button: "red"
            bg_color_stack_button: "red"
            color_icon_stack_button: "white"
            color_icon_root_button: self.color_icon_stack_button

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-color-icon-root-button.png
        :align: center

    :attr:`color_icon_root_button` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    bg_hint_color = ColorProperty(None)
    """
    Background color for the floating text of the buttons in (r, g, b, a)
    or string format.

    .. code-clock:: kv

        MDFloatingActionButtonSpeedDial:
            bg_hint_color: "red"
            hint_animation: True

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-bg-hint-color.png
        :align: center

    :attr:`bg_hint_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    hint_animation = BooleanProperty(False)
    """
    Whether to use button extension animation to display floating text.

    :attr:`hint_animation` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    stack_buttons = DictProperty()

    _label_pos_y_set = False
    _anim_buttons_data = {}
    _anim_labels_data = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_close")
        self.register_event_type("on_press_stack_button")
        self.register_event_type("on_release_stack_button")
        Window.bind(on_resize=self._update_pos_buttons)

    def on_open(self, *args):
        """Called when a stack is opened."""

    def on_close(self, *args):
        """Called when a stack is closed."""

    def on_leave(self, instance_button: MDFloatingBottomButton) -> None:
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
                                _elevation=0,
                            ).start(instance_button)
                            Animation(
                                opacity=0, d=0.1, t=self.opening_transition
                            ).start(widget)

    def on_enter(self, instance_button: MDFloatingBottomButton) -> None:
        """Called when the mouse cursor is over a button from the stack."""

        if self.state == "open":
            for widget in self.children:
                if isinstance(widget, MDFloatingLabel) and self.hint_animation:
                    Animation.cancel_all(widget)
                    for item in self.data.items():
                        if widget.text in item:
                            Animation(
                                _canvas_width=widget.width + dp(24),
                                _padding_right=self.right_pad_value
                                if self.right_pad
                                else 0,
                                d=self.opening_time,
                                t=self.opening_transition,
                            ).start(instance_button)
                            if (
                                instance_button.icon
                                == self.data[f"{widget.text}"]
                                or instance_button.icon
                                == self.data[f"{widget.text}"][0]
                            ):
                                Animation(
                                    opacity=1,
                                    d=self.opening_time,
                                    t=self.opening_transition,
                                ).start(widget)
                            else:
                                Animation(
                                    opacity=0, d=0.1, t=self.opening_transition
                                ).start(widget)

    def on_data(self, instance_speed_dial, data: dict) -> None:
        """Creates a stack of buttons."""

        def on_data(*args):
            # Bottom buttons.
            for name, parameters in data.items():
                name_icon = (
                    parameters if (type(parameters) is str) else parameters[0]
                )

                bottom_button = MDFloatingBottomButton(
                    icon=name_icon,
                    on_enter=self.on_enter,
                    on_leave=self.on_leave,
                    opacity=0,
                )
                bottom_button.bind(
                    on_press=lambda x: self.dispatch("on_press_stack_button"),
                    on_release=lambda x: self.dispatch(
                        "on_release_stack_button"
                    ),
                )

                if "on_press" in parameters:
                    callback = parameters[parameters.index("on_press") + 1]
                    bottom_button.bind(on_press=callback)

                if "on_release" in parameters:
                    callback = parameters[parameters.index("on_release") + 1]
                    bottom_button.bind(on_release=callback)

                self.set_pos_bottom_buttons(bottom_button)
                self.add_widget(bottom_button)
                self.stack_buttons[name] = WeakProxy(bottom_button)
                # Labels.
                floating_text = name
                if floating_text:
                    label = MDFloatingLabel(text=floating_text, opacity=0)
                    label.bg_color = self.label_bg_color
                    label.radius = self.label_radius
                    label.text_color = (
                        self.label_text_color
                        if self.label_text_color
                        else self.theme_cls.text_color
                    )
                    self.add_widget(label)
            # Top root button.
            root_button = MDFloatingRootButton(on_release=self.open_stack)
            root_button.icon = self.icon
            self.set_pos_root_button(root_button)
            self.add_widget(root_button)

        self.clear_widgets()
        self.stack_buttons = {}
        self._anim_buttons_data = {}
        self._anim_labels_data = {}
        self._label_pos_y_set = False
        Clock.schedule_once(on_data)

    def on_icon(self, instance_speed_dial, name_icon: str) -> None:
        self._set_button_property(MDFloatingRootButton, "icon", name_icon)

    def on_label_text_color(
        self, instance_speed_dial, color: list | str
    ) -> None:
        for widget in self.children:
            if isinstance(widget, MDFloatingLabel):
                widget.text_color = color

    def on_color_icon_stack_button(
        self, instance_speed_dial, color: list
    ) -> None:
        self._set_button_property(MDFloatingBottomButton, "icon_color", color)

    def on_hint_animation(self, instance_speed_dial, value: bool) -> None:
        for widget in self.children:
            if isinstance(widget, MDFloatingLabel):
                widget.md_bg_color = (0, 0, 0, 0)

    def on_bg_hint_color(self, instance_speed_dial, color: list) -> None:
        setattr(MDFloatingBottomButton, "_bg_color", color)

    def on_color_icon_root_button(
        self, instance_speed_dial, color: list
    ) -> None:
        self._set_button_property(MDFloatingRootButton, "icon_color", color)

    def on_bg_color_stack_button(
        self, instance_speed_dial, color: list
    ) -> None:
        self._set_button_property(MDFloatingBottomButton, "md_bg_color", color)

    def on_bg_color_root_button(self, instance_speed_dial, color: list) -> None:
        self._set_button_property(MDFloatingRootButton, "md_bg_color", color)

    def on_press_stack_button(self, *args) -> None:
        """
        Called at the on_press event for the stack button.

        .. code-block:: kv

            MDFloatingActionButtonSpeedDial:
                on_press_stack_button: print(*args)

        .. versionadded:: 1.1.0
        """

    def on_release_stack_button(self, *args) -> None:
        """
        Called at the on_release event for the stack button.

        .. code-block:: kv

            MDFloatingActionButtonSpeedDial:
                on_release_stack_button: print(*args)

        .. versionadded:: 1.1.0
        """

    def set_pos_labels(self, instance_floating_label: MDFloatingLabel) -> None:
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
    ) -> None:
        """
        Sets the position of the root button.
        Called when the application's root window is resized.
        """

        def set_pos_root_button(*args):
            if self.anchor == "right":
                instance_floating_root_button.y = dp(20)
                instance_floating_root_button.x = self.parent.width - (
                    dp(56) + dp(20)
                )

        Clock.schedule_once(set_pos_root_button)

    def set_pos_bottom_buttons(
        self, instance_floating_bottom_button: MDFloatingBottomButton
    ) -> None:
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
    ) -> None:
        """Opens a button stack."""

        for widget in self.children:
            if isinstance(widget, MDFloatingLabel):
                Animation.cancel_all(widget)

        if self.state != "open":
            y = 0
            label_position = dp(54)
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
                        rotate_value_angle=-45,
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

    def do_animation_open_stack(self, anim_data: dict) -> None:
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
                if widget.opacity > 0:
                    Animation(opacity=0, d=0.1).start(widget)
            elif (
                isinstance(widget, MDFloatingRootButton)
                and self.root_button_anim
            ):
                Animation(
                    rotate_value_angle=0,
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

    def _set_button_property(
        self, instance, property_name: str, property_value: str | list
    ):
        def set_count_widget(*args):
            if self.children:
                for widget in self.children:
                    if isinstance(widget, instance):
                        setattr(instance, property_name, property_value)
                        Clock.unschedule(set_count_widget)
                        break

        Clock.schedule_interval(set_count_widget, 0)
