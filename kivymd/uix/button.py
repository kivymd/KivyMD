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

The length of the shadow is controlled by the ``elevation_normal`` parameter:

.. code-block:: kv

    MDFloatingActionButton:
        icon: "android"
        elevation_normal: 12

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-floating-action-button-elevation-normal.png
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
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivymd.color_definitions import text_colors
from kivymd.font_definitions import theme_font_styles
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    CircularElevationBehavior,
    CircularRippleBehavior,
    CommonElevationBehavior,
    FakeRectangularElevationBehavior,
    RectangularRippleBehavior,
)
from kivymd.uix.label import MDLabel
from kivymd.uix.tooltip import MDTooltip

Builder.load_string(
    """
<BaseButton>
    canvas:
        Clear
        Color:
            rgba:
                self.md_bg_color if not self.disabled else \
                (root.md_bg_color_disabled if root.md_bg_color_disabled \
                else root.theme_cls.disabled_hint_text_color)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [root._radius, ]

    lbl_txt: lbl_txt
    size_hint: None, None
    height: dp(20) + lbl_txt.texture_size[1]
    width: lbl_txt.texture_size[0] + dp(24)

    MDLabel:
        id: lbl_txt
        text: root.text
        font_size: root.font_size
        font_style: root.font_style
        adaptive_size: True
        -text_size: None, None
        theme_text_color: root.theme_text_color
        text_color: root.text_color
        markup: True
        disabled: root.disabled
        opposite_colors: root.opposite_colors
        font_name: root.font_name if root.font_name else self.font_name


<BaseRoundButton>
    canvas:
        Clear
        Color:
            rgba:
                (self.md_bg_color if root.icon in md_icons else (0, 0, 0, 0)) \
                if not root.disabled else \
                (root.md_bg_color_disabled if root.md_bg_color_disabled \
                else root.theme_cls.disabled_hint_text_color)
        Ellipse:
            size: self.size
            pos: self.pos
            source: self.source if hasattr(self, "source") else ""

    size: "48dp", "48dp"
    lbl_txt: lbl_txt
    padding: "12dp" if root.icon in md_icons else (0, 0, 0, 0)

    MDIcon:
        id: lbl_txt
        icon: root.icon
        font_size: root.user_font_size if root.user_font_size else self.font_size
        font_name: root.font_name if root.font_name else self.font_name
        theme_text_color: root.theme_text_color
        text_color:
            root.text_color if not root.disabled else \
            (root.md_bg_color_disabled if root.md_bg_color_disabled \
            else root.theme_cls.disabled_hint_text_color)
        disabled: root.disabled
        valign: "middle"
        halign: "center"
        opposite_colors: root.opposite_colors


<MDRoundFlatButton>
    canvas.before:
        Clear
        Color:
            rgba:
                (root.theme_cls.primary_color if not root.line_color else root.line_color) \
                if not root.disabled else \
                (root.md_bg_color_disabled if root.md_bg_color_disabled \
                else root.theme_cls.disabled_hint_text_color)
        Line:
            width: root.line_width
            rounded_rectangle:
                (self.x, self.y, self.width, self.height,\
                root._radius, root._radius, root._radius, root._radius,\
                self.height)

    theme_text_color: "Custom"


<MDFillRoundFlatButton>
    canvas.before:
        Clear
        Color:
            rgba:
                (root.theme_cls.primary_color if root.md_bg_color == [0.0, 0.0, 0.0, 0.0] \
                else root.md_bg_color) if not root.disabled else \
                (root.md_bg_color_disabled if root.md_bg_color_disabled \
                else root.theme_cls.disabled_hint_text_color)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [root._radius, ]

    line_width: 0.001
    theme_text_color: "Custom"


<MDFillRoundFlatIconButton>
    canvas.before:
        Clear
        Color:
            rgba:
                (root.theme_cls.primary_color if root.md_bg_color == [0.0, 0.0, 0.0, 0.0] \
                else root.md_bg_color) if not root.disabled else \
                (root.md_bg_color_disabled if root.md_bg_color_disabled \
                else root.theme_cls.disabled_hint_text_color)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [root._radius, ]

    line_width: 0.001
    theme_text_color: "Custom"


<MDRectangleFlatButton>
    canvas.before:
        Clear
        Color:
            rgba:
                (root.theme_cls.primary_color if not root.line_color else root.line_color) \
                if not root.disabled else \
                (root.md_bg_color_disabled if root.md_bg_color_disabled \
                else root.theme_cls.disabled_hint_text_color)
        Line:
            width: root.line_width
            rectangle: (self.x, self.y, self.width, self.height)

    theme_text_color: "Custom"


<MDRectangleFlatIconButton>
    canvas.before:
        Clear
        Color:
            rgba:
                (root.theme_cls.primary_color if not root.line_color else root.line_color) \
                if not root.disabled else \
                (root.md_bg_color_disabled if root.md_bg_color_disabled \
                else root.theme_cls.disabled_hint_text_color)
        Line:
            width: root.line_width
            rectangle: (self.x, self.y, self.width, self.height)

    size_hint_x: None
    width: root.lbl_txt.width + lbl_ic.width * 2 + box.spacing

    MDBoxLayout:
        id: box
        size_hint: None, None
        size: root.size
        padding: "10dp", 0, 0, 0
        spacing: "8dp"

        MDIcon:
            id: lbl_ic
            icon: root.icon
            theme_text_color: "Custom"
            text_color:
                (root.theme_cls.primary_color if not root.icon_color else root.icon_color) \
                if not root.disabled else \
                (root.md_bg_color_disabled if root.md_bg_color_disabled \
                else root.theme_cls.disabled_hint_text_color)
            size_hint_x: None
            width: self.texture_size[0]

        MDLabel:
            id: lbl
            text: root.text
            font_size: root.font_size
            font_style: root.font_style
            adaptive_size: True
            -text_size: None, None
            theme_text_color: "Custom"
            text_color: root.text_color
            markup: True
            disabled: root.disabled
            opposite_colors: root.opposite_colors
            font_name: root.font_name if root.font_name else self.font_name
            pos_hint: {"center_y": .5}


<MDRoundFlatIconButton>
    canvas.before:
        Clear
        Color:
            rgba:
                (root.theme_cls.primary_color if not root.line_color else root.line_color) \
                if not root.disabled else \
                (root.md_bg_color_disabled if root.md_bg_color_disabled \
                else root.theme_cls.disabled_hint_text_color)
        Line:
            width: root.line_width
            rounded_rectangle:
                (self.x, self.y, self.width, self.height,\
                root._radius, root._radius, root._radius, root._radius,\
                self.height)

    size_hint_x: None
    width: root.lbl_txt.width + lbl_ic.width * 2 + box.spacing

    MDBoxLayout:
        id: box
        size_hint: None, None
        size: root.size
        padding: "10dp", 0, 0, 0
        spacing: "8dp"

        MDIcon:
            id: lbl_ic
            icon: root.icon
            theme_text_color: "Custom"
            text_color:
                (root.theme_cls.primary_color if not root.icon_color else root.icon_color) \
                if not root.disabled else \
                (root.md_bg_color_disabled if root.md_bg_color_disabled \
                else root.theme_cls.disabled_hint_text_color)
            size_hint_x: None
            width: self.texture_size[0]

        MDLabel:
            id: lbl
            text: root.text
            font_size: root.font_size
            font_style: root.font_style
            adaptive_size: True
            -text_size: None, None
            theme_text_color: root.theme_text_color
            text_color: root.text_color
            markup: True
            disabled: root.disabled
            opposite_colors: root.opposite_colors
            font_name: root.font_name if root.font_name else self.font_name
            pos_hint: {"center_y": .5}


<MDIconButton>
    on_size: root.set_size(0)


<MDFloatingActionButton>
    theme_text_color: "Custom"
    # theme_text_color: root.theme_text_color
    # opposite_colors: root.opposite_colors
    on_size: root.set_size(0)


<MDTextButton>
    adaptive_size: True
    color: root.theme_cls.primary_color if not root.color else root.color
    opacity: 1


<BaseFloatingBottomButton>
    theme_text_color: "Custom"
    md_bg_color: self.theme_cls.primary_color

    canvas.before:
        Color:
            rgba:
                self.theme_cls.primary_color \
                if not self._bg_color else self._bg_color
        RoundedRectangle:
            pos:
                (self.x - self._canvas_width + dp(1.5)) + self._padding_right / 2, \
                self.y - self._padding_right / 2 + dp(1.5)
            size:
                self.width + self._canvas_width - dp(3), \
                self.height + self._padding_right - dp(3)
            radius: [self.height / 2]


<BaseFloatingRootButton>
    theme_text_color: "Custom"
    md_bg_color: self.theme_cls.primary_color

    canvas.before:
        PushMatrix
        Rotate:
            angle: self._angle
            axis: (0, 0, 1)
            origin: self.center
    canvas.after:
        PopMatrix


<BaseFloatingLabel>
    size_hint: None, None
    padding: "8dp", "4dp", "8dp", "4dp"
    height: label.texture_size[1] + self.padding[1] * 2
    width: label.texture_size[0] + self.padding[0] * 2
    elevation: 10

    canvas:
        Color:
            rgba:
                self.theme_cls.primary_color \
                if not root.bg_color else root.bg_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [5]

    Label:
        id: label
        markup: True
        text: root.text
        size_hint: None, None
        size: self.texture_size
        color: root.theme_cls.text_color if not root.text_color else root.text_color
"""
)


class BaseButton(ThemableBehavior, ButtonBehavior, AnchorLayout):
    """Base class for all buttons."""

    text = StringProperty(" ")
    """
    Button text.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `' '`.
    """

    theme_text_color = OptionProperty(
        "Primary",
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

    md_bg_color = ColorProperty([1.0, 1.0, 1.0, 0])
    """
    Button background color.

    :attr:`md_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1.0, 1.0, 1.0, 0]`.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    Disabled button text color.

    :attr:`md_bg_color_disabled` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _radius = NumericProperty(0)
    _md_bg_color = ColorProperty(None)  # last current button color

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.md_bg_color_disabled:
            self.md_bg_color_disabled = self.theme_cls.disabled_hint_text_color
        self.theme_cls.bind(primary_palette=self.update_md_bg_color)
        self.theme_cls.bind(theme_style=self.update_text_color)
        Clock.schedule_once(self.set_md_bg_color)
        if not self.text_color:
            self.text_color = self.theme_cls.text_color

    def update_text_color(self, instance, value):
        pass

    def set_md_bg_color(self, interval):
        """Checks if a value is set for the `md_bg_color` parameter."""

        if self.md_bg_color == [1.0, 1.0, 1.0, 0]:
            self.md_bg_color = self.theme_cls.primary_color
        if not self.md_bg_color_disabled:
            self.md_bg_color_disabled = self.theme_cls.disabled_hint_text_color

    def update_md_bg_color(self, instance, value):
        """Called when the application color palette changes."""

        self.md_bg_color = self.theme_cls._get_primary_color()
        self.update_text_color(instance, value)

    def on_disabled(self, instance, value):
        """
        Sets the color of the button at the moment of setting the parameter
        `disabled`.
        """

        # Sets button background color (disabled).
        if value:
            if not self.md_bg_color_disabled:
                self.md_bg_color_disabled = (
                    self.theme_cls.disabled_hint_text_color
                )
            self.md_bg_color = self.md_bg_color_disabled
        # Sets last current button background color.
        else:
            self.md_bg_color = (
                self._md_bg_color
                if self._md_bg_color
                else self.theme_cls.primary_color
            )

    def on_md_bg_color(self, instance, value):
        """Sets last current button background color."""

        if self.md_bg_color != self.md_bg_color_disabled:
            self._md_bg_color = value


class BasePressedButton(BaseButton):
    """
    Base class for those button which fade to a background color on press.
    """

    animation_fade_bg = None
    current_md_bg_color = ColorProperty(None)

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
            if self.md_bg_color == [0.0, 0.0, 0.0, 0.0]:
                self.current_md_bg_color = self.md_bg_color
                self.animation_fade_bg = Animation(
                    duration=0.5, md_bg_color=[0.0, 0.0, 0.0, 0.1]
                )
                self.animation_fade_bg.start(self)
            return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if (
            self.collide_point(touch.x, touch.y)
            and self.animation_fade_bg
            and not self.disabled
        ):
            self.animation_fade_bg.stop_property(self, "md_bg_color")
            Animation(
                duration=0.05, md_bg_color=self.current_md_bg_color
            ).start(self)
        return super().on_touch_up(touch)


class BaseRectangularButton(
    RectangularRippleBehavior,
    FakeRectangularElevationBehavior,
    BackgroundColorBehavior,
    BasePressedButton,
    BaseButton,
):
    """Base class for all rectangular buttons."""

    def on_width(self, *args):
        if self.width < 88:
            self.width = 88


class BaseFlatButton(BaseRectangularButton):
    def update_md_bg_color(self, instance, value):
        """Called when the application color palette changes."""

        self.text_color = self.theme_cls.primary_color

    def set_text_color(self, interval):
        """Sets the text color if no custom value is specified."""

        if self.text_color in ([0.0, 0.0, 0.0, 0.87], [1, 0, 1, 1]):
            self.theme_text_color = "Custom"
            self.text_color = self.theme_cls.primary_color

    def on_md_bg_color(self, instance, value):
        """
        We override this method, thus prohibiting setting the background color
        for the button.

        Allows to set the background color only in the rangefrom
        [0.0, 0.0, 0.0, 0.0] to [0.0, 0.0, 0.0, 0.1]. This color is set in
        the :class:`BasePressedButton` class when the button is pressed and
        Ignore other custom colors.
        """

        if value[:-1] != [0.0, 0.0, 0.0]:
            self.md_bg_color = [0.0, 0.0, 0.0, 0.0]

    def on_disabled(self, instance, value):
        if value and not self.disabled:
            self.md_bg_color = (
                self.md_bg_color_disabled
                if self.md_bg_color_disabled
                else self.theme_cls.disabled_hint_text_color
            )
        else:
            self.md_bg_color = [0.0, 0.0, 0.0, 0.0]

    def on_elevation(self, instance, value):
        """
        We are overriding this method to not allow set the `elevation` value
        for this type of button.
        """
        self.elevation = 0
        self._elevation = 0
        super().on_elevation(instance, value)


class BaseElevationButton(CommonElevationBehavior, BaseButton):
    """
    Base class for raised buttons.
    Implements elevation behavior as well as the recommended down/disabled
    colors for raised buttons.

    The minimum elevation for any raised button is `"1dp"`,
    by default, set to `"2dp"`.

    the _elevation_raised is automatically computed and is set to
    self.elevation + 6 each time self.elevation is updated.

    """

    _elevation_raised = NumericProperty()
    _anim_raised = None

    def __init__(self, **kwargs):
        if self.elevation == 0:
            self.elevation = 2
        super().__init__(**kwargs)
        self.on_elevation(self, self.elevation)

    def on_elevation(self, instance, value):
        super().on_elevation(instance, value)
        self._elevation_raised = self.elevation + 6
        self._anim_raised = Animation(_elevation=self._elevation_raised, d=0.15)

    def on__elevation_raised(self, instance, value):
        Animation.cancel_all(self, "_elevation")
        self._anim_raised = Animation(_elevation=self._elevation_raised, d=0.15)

    def on_disabled(self, instance, value):
        if self.disabled is True:
            Animation.cancel_all(self, "_elevation")
        super().on_disabled(instance, value)

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
                if isinstance(self, MDFloatingActionButton):
                    self.stop_elevation_anim()
                return super().on_touch_up(touch)
            self.stop_elevation_anim()
        return super().on_touch_up(touch)

    def stop_elevation_anim(self):
        Animation.cancel_all(self, "_elevation")
        self._elevation = self.elevation


class BaseCircularElevationButton(
    CircularElevationBehavior, BaseElevationButton, BaseButton
):
    pass


class BaseRoundButton(CircularRippleBehavior, BaseButton):
    """
    Base class for all round buttons, bringing in the appropriate
    on-touch behavior
    """

    md_bg_color = ColorProperty([0.0, 0.0, 0.0, 0.0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_text)
        Clock.schedule_once(self.set_text_color)

    def set_text_color(self, interval):
        if not self.text_color:
            self.text_color = self.theme_cls._get_text_color()

    def set_text(self, interval):
        self.text = ""


class BaseRectangleFlatButton(BaseFlatButton, BaseElevationButton):
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

    md_bg_color = ColorProperty([0.0, 0.0, 0.0, 0.0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_text_color)


class MDRaisedButton(BaseRectangularButton, BaseElevationButton):
    theme_text_color = StringProperty("Custom")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.update_text_color)

    def update_text_color(self, *args):
        if self.text_color in (
            [0.0, 0.0, 0.0, 0.87],
            [0.0, 0.0, 0.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
        ):
            self.text_color = text_colors[self.theme_cls.primary_palette][
                self.theme_cls.primary_hue
            ]


class MDFlatButton(BaseFlatButton):
    md_bg_color = ColorProperty([0.0, 0.0, 0.0, 0.0])


class MDRectangleFlatButton(BaseRectangleFlatButton):
    # TODO: If the user has set a custom text color, then when the application
    #  color palette changes, the text color will also change to the current
    #  color of the color scheme. Do need to preserve custom text colors when
    #  changing the application palette?
    pass


class MDRectangleFlatIconButton(BaseRectangleFlatButton):
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.remove_label)
        Clock.schedule_once(self.set_icon_color)

    def update_md_bg_color(self, instance, value):
        self.text_color = self.theme_cls.primary_color
        self.icon_color = self.theme_cls.primary_color

    def set_icon_color(self, interval):
        """Sets the icon color if no custom value is specified."""

        if not self.icon_color:
            self.icon_color = self.theme_cls.primary_color

    def remove_label(self, interval):
        self.remove_widget(self.ids.lbl_txt)


class MDRoundFlatButton(MDFlatButton):
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

    _radius = NumericProperty(18)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_text_color)

    def lay_canvas_instructions(self):
        with self.canvas.after:
            StencilPush()
            RoundedRectangle(
                size=self.size, pos=self.pos, radius=[self._radius]
            )
            StencilUse()
            self.col_instruction = Color(rgba=self.ripple_color)
            self.ellipse = Ellipse(
                size=(self._ripple_rad, self._ripple_rad),
                pos=(
                    self.ripple_pos[0] - self._ripple_rad / 2.0,
                    self.ripple_pos[1] - self._ripple_rad / 2.0,
                ),
            )
            StencilUnUse()
            RoundedRectangle(
                size=self.size, pos=self.pos, radius=[self._radius]
            )
            StencilPop()
        self.bind(ripple_color=self._set_color, _ripple_rad=self._set_ellipse)


class MDRoundFlatIconButton(MDRoundFlatButton):
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.remove_label)
        Clock.schedule_once(self.set_icon_color)

    def set_icon_color(self, interval):
        """Sets the icon color if no custom value is specified."""

        if not self.icon_color:
            self.icon_color = self.theme_cls.primary_color

    def update_md_bg_color(self, instance, value):
        self.text_color = self.theme_cls.primary_color
        self.icon_color = self.theme_cls.primary_color

    # From Python code.
    def on_icon_color(self, instance, value):
        def set_icon_color(interval):
            self.icon_color = value

        Clock.schedule_once(set_icon_color)

    def remove_label(self, interval):
        self.remove_widget(self.ids.lbl_txt)


class MDFillRoundFlatButton(MDRoundFlatButton):
    opposite_colors = BooleanProperty(True)

    def __init__(self, **kwargs):
        # Some blatant shit :(
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_text_color)

    def set_text_color(self, interval):
        if self.text_color in (
            [0.0, 0.0, 0.0, 0.87],
            [0.0, 0.0, 0.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
        ):
            self.text_color = text_colors[self.theme_cls.primary_palette][
                self.theme_cls.primary_hue
            ]

    def update_md_bg_color(self, instance, value):
        self.md_bg_color = self.theme_cls.primary_color
        self.set_text_color(0)

    def on_md_bg_color(self, instance, value):
        self.set_text_color(0)


class MDFillRoundFlatIconButton(MDRoundFlatIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.update_text_color)
        Clock.schedule_once(self.update_icon_color)

    def set_md_bg_color(self, interval):
        if self.md_bg_color == [0.0, 0.0, 0.0, 0.0]:
            self.md_bg_color = self.theme_cls.primary_color

    def on_md_bg_color(self, instance, value):
        self.md_bg_color = value
        if self.md_bg_color != self.md_bg_color_disabled:
            self._md_bg_color = value

    def update_md_bg_color(self, instance, value):
        """Called when the application color palette changes."""

        self.md_bg_color = self.theme_cls._get_primary_color()
        self.update_text_color(instance, value)
        if self.icon_color in (
            [0.0, 0.0, 0.0, 0.87],
            [0.0, 0.0, 0.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
        ):
            self.icon_color = text_colors[self.theme_cls.primary_palette][
                self.theme_cls.primary_hue
            ]

    def update_text_color(self, *args):
        if self.text_color in (
            [0.0, 0.0, 0.0, 0.87],
            [0.0, 0.0, 0.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
        ):
            self.text_color = text_colors[self.theme_cls.primary_palette][
                self.theme_cls.primary_hue
            ]

    def set_text_color(self, interval):
        pass

    def update_icon_color(self, interval):
        if not self.icon_color:
            self.icon_color = text_colors[self.theme_cls.primary_palette][
                self.theme_cls.primary_hue
            ]

    def on_disabled(self, instance, value):
        if value:
            if not self.md_bg_color_disabled:
                self.md_bg_color_disabled = (
                    self.theme_cls.disabled_hint_text_color
                )
            self.md_bg_color = self.md_bg_color_disabled
        else:
            if self._md_bg_color:
                self.md_bg_color = self._md_bg_color

    def set_icon_color(self, interval):
        pass


class MDIconButton(BaseRoundButton, BasePressedButton):
    icon = StringProperty("checkbox-blank-circle")
    """
    Button icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle'`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(primary_palette=self.update_md_bg_color)
        Clock.schedule_once(self.set_size)
        self.on_md_bg_color(self, [0.0, 0.0, 0.0, 0.0])

    def set_size(self, interval):
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

    def update_md_bg_color(self, instance, value):
        if self.md_bg_color != [0.0, 0.0, 0.0, 0.0]:
            self.md_bg_color = self.theme_cls._get_primary_color()


class MDFloatingActionButton(
    BaseRoundButton, BasePressedButton, BaseCircularElevationButton
):
    icon = StringProperty("android")
    """
    Button icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    # FIXME: The `opposite_colors` parameter does not work for this type
    #  of buttons
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(primary_palette=self.update_md_bg_color)
        Clock.schedule_once(self.set_md_bg_color)
        Clock.schedule_once(self.set_size)
        Clock.schedule_once(self.update_text_color)

    def update_text_color(self, *args):
        if self.text_color in (
            [0.0, 0.0, 0.0, 0.87],
            [0.0, 0.0, 0.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
        ):
            self.text_color = text_colors[self.theme_cls.primary_palette][
                self.theme_cls.primary_hue
            ]

    def set_md_bg_color(self, interval):
        if self.md_bg_color == [0.0, 0.0, 0.0, 0.0]:
            self.md_bg_color = self.theme_cls.primary_color

    def set_size(self, interval):
        self.width = "56dp"
        self.height = "56dp"

    def on_touch_down(self, touch):
        super(MDFloatingActionButton, self).on_touch_down(touch)
        if self.collide_point(touch.x, touch.y):
            return True

    def on_touch_move(self, touch):
        super(MDFloatingActionButton, self).on_touch_move(touch)
        if self.collide_point(touch.x, touch.y):
            return True

    def on_touch_up(self, touch):
        super(MDFloatingActionButton, self).on_touch_up(touch)
        if self.collide_point(touch.x, touch.y):
            return True


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

    def animation_label(self):
        def set_default_state_label(*args):
            Animation(opacity=1, d=0.1, t="in_out_cubic").start(self)

        anim = Animation(opacity=0.5, d=0.2, t="in_out_cubic")
        anim.bind(on_complete=set_default_state_label)
        anim.start(self)

    def on_press(self, *args):
        self.animation_label()
        return super().on_press(*args)

    def on_md_bg_color(self, instance, value):
        self.md_bg_color = [0.0, 0.0, 0.0, 0.0]

    def on_disabled(self, instance, value):
        if value:
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

    def set_size(self, interval):
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

    def on_leave(self, instance):
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
                            ).start(instance)
                            if self.hint_animation:
                                Animation(
                                    opacity=0, d=0.1, t=self.opening_transition
                                ).start(widget)
                            break
                    break

    def on_enter(self, instance):
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
                            ).start(instance)
                            if self.hint_animation:
                                Animation(
                                    opacity=1,
                                    d=self.opening_time,
                                    t=self.opening_transition,
                                ).start(widget)
                            break
                    break

    def on_data(self, instance, value):
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
        for name, name_icon in value.items():
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

    def on_icon(self, instance, value):
        self._get_count_widget(MDFloatingRootButton).icon = value

    def on_label_text_color(self, instance, value):
        for widget in self.children:
            if isinstance(widget, MDFloatingLabel):
                widget.text_color = value

    def on_color_icon_stack_button(self, instance, value):
        for widget in self.children:
            if isinstance(widget, MDFloatingBottomButton):
                widget.text_color = value

    def on_hint_animation(self, instance, value):
        for widget in self.children:
            if isinstance(widget, MDFloatingLabel):
                widget.bg_color = (0, 0, 0, 0)

    def on_bg_hint_color(self, instance, value):
        for widget in self.children:
            if isinstance(widget, MDFloatingBottomButton):
                widget._bg_color = value

    def on_color_icon_root_button(self, instance, value):
        self._get_count_widget(MDFloatingRootButton).text_color = value

    def on_bg_color_stack_button(self, instance, value):
        for widget in self.children:
            if isinstance(widget, MDFloatingBottomButton):
                widget.md_bg_color = value

    def on_bg_color_root_button(self, instance, value):
        self._get_count_widget(MDFloatingRootButton).md_bg_color = value

    def set_pos_labels(self, widget):
        """Sets the position of the floating labels."""

        if self.anchor == "right":
            widget.x = Window.width - widget.width - dp(86)

    def set_pos_root_button(self, instance):
        """Sets the position of the root button."""

        if self.anchor == "right":
            instance.y = dp(20)
            instance.x = Window.width - (dp(56) + dp(20))

    def set_pos_bottom_buttons(self, instance):
        """Sets the position of the bottom buttons in a stack."""

        if self.anchor == "right":
            if self.state != "open":
                instance.y = instance.height / 2
            instance.x = Window.width - (instance.height + instance.width / 2)

    def open_stack(self, instance):
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

    def do_animation_open_stack(self, anim_data):
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
