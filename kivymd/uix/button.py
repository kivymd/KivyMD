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
    Screen:

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
        text_color: 0, 0, 1, 1

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-flat-button-text-color.png
    :align: center

Or use markup:

.. code-block:: kv

    MDFlatButton:
        text: "[color=#00ffcc]MDFLATBUTTON[/color]"
        markup: True

To specify the font size and font name, use the parameters as in the usual
`Kivy` buttons:

.. code-block:: kv

    MDFlatButton:
        text: "MDFLATBUTTON"
        font_size: "18sp"
        font_name: "path/to/font"

.. warning:: You cannot use the ``size_hint_x`` parameter for `KivyMD` buttons
    (the width of the buttons is set automatically)!

However, if there is a need to increase the width of the button,
you can use the parameter ``increment_width``:

.. code-block:: kv

    MDFlatButton:
        text: "MDFLATBUTTON"
        increment_width: "164dp"

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

Button parameters :class:`~MDRectangleFlatButton` are the same as
button :class:`~MDRaisedButton`:

.. code-block:: kv

    MDRectangleFlatButton:
        text: "MDRECTANGLEFLATBUTTON"
        text_color: 0, 0, 1, 1
        md_bg_color: 1, 1, 0, 1

.. note:: Note that the frame color will be the same as the text color.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-rectangle-flat-button-md-bg-color.png
    :align: center

.. MDRectangleFlatIconButton:
MDRectangleFlatIconButton
---------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-rectangle-flat-icon-button.gif
    :align: center

Button parameters :class:`~MDRectangleFlatButton` are the same as
button :class:`~MDRectangleFlatButton`:

.. code-block:: kv

    MDRectangleFlatIconButton:
        icon: "android"
        text: "MDRECTANGLEFLATICONBUTTON"
        width: dp(280)

.. warning:: :class:`~MDRectangleFlatButton` does not stretch to match the
    text and is always ``dp(150)``. But you should not set the width of the
    button using parameter ``increment_width``. You should set the width
    instead using the ``width`` parameter.

.. MDRoundFlatButton:
MDRoundFlatButton
-----------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-round-flat-button.gif
    :align: center

Button parameters :class:`~MDRoundFlatButton` are the same as
button :class:`~MDRectangleFlatButton`:

.. code-block:: kv

    MDRoundFlatButton:
        text: "MDROUNDFLATBUTTON"

.. warning:: The border color does not change when using
    ``text_color`` parameter.

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
        width: dp(250)

.. warning:: The border color does not change when using
    ``text_color`` parameter.

.. warning:: :class:`~MDRoundFlatIconButton` does not stretch to match the
    text and is always ``dp(150)``. But you should not set the width of the
    button using parameter ``increment_width``. You should set the width
    instead using the ``width`` parameter.

.. MDFillRoundFlatButton:
MDFillRoundFlatButton
---------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-fill-round-flat-button.png
    :align: center

Button parameters :class:`~MDFillRoundFlatButton` are the same as
button :class:`~MDRaisedButton`.

.. MDFillRoundFlatIconButton:
MDFillRoundFlatIconButton
---------------------

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
    Screen:

        MDFloatingActionButtonSpeedDial:
            data: app.data
            rotation_root_button: True
    '''


    class Example(MDApp):
        data = {
            'language-python': 'Python',
            'language-php': 'PHP',
            'language-cpp': 'C++',
        }

        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial.gif
    :align: center

Or without KV Language:

.. code-block:: python

    from kivy.uix.screenmanager import Screen

    from kivymd.app import MDApp
    from kivymd.uix.button import MDFloatingActionButtonSpeedDial


    class Example(MDApp):
        data = {
            'language-python': 'Python',
            'language-php': 'PHP',
            'language-cpp': 'C++',
        }

        def build(self):
            screen = Screen()
            speed_dial = MDFloatingActionButtonSpeedDial()
            speed_dial.data = self.data
            speed_dial.rotation_root_button = True
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

    `See full example <https://github.com/HeaTTheatR/KivyMD/wiki/Components-Button>`_
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

from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Ellipse, RoundedRectangle
from kivy.graphics.stencil_instructions import (
    StencilPush,
    StencilUse,
    StencilPop,
    StencilUnUse,
)
from kivy.properties import (
    StringProperty,
    BoundedNumericProperty,
    ListProperty,
    AliasProperty,
    BooleanProperty,
    NumericProperty,
    OptionProperty,
    ObjectProperty,
    DictProperty,
)

from kivymd.theming import ThemableBehavior
from kivymd.uix.tooltip import MDTooltip
from kivymd.uix.behaviors import (
    CommonElevationBehavior,
    RectangularElevationBehavior,
    CircularElevationBehavior,
    SpecificBackgroundColorBehavior,
    CircularRippleBehavior,
    RectangularRippleBehavior,
)

Builder.load_string(
    """
#:import images_path kivymd.images_path
#:import md_icons kivymd.icon_definitions.md_icons


<BaseButton>
    size_hint: (None, None)
    anchor_x: 'center'
    anchor_y: 'center'


<BaseFlatButton>


<BaseRaisedButton>


<BaseRoundButton>
    canvas:
        Clear
        Color:
            rgba: self._current_button_color if root.icon in md_icons else (0, 0, 0, 0)
        Ellipse:
            size: self.size
            pos: self.pos
            source: self.source if hasattr(self, "source") else ""

    size:
        (dp(48), dp(48)) \
        if not root.user_font_size \
        else (dp(root.user_font_size + 23), dp(root.user_font_size + 23))
    lbl_txt: lbl_txt
    padding: dp(12) if root.icon in md_icons else 0
    theme_text_color: 'Primary'

    MDIcon:
        id: lbl_txt
        icon: root.icon
        font_size:
            root.user_font_size \
            if root.user_font_size \
            else self.font_size
        font_name: root.font_name if root.font_name is not None else self.font_name
        theme_text_color: root.theme_text_color
        text_color: root.text_color
        disabled: root.disabled
        valign: 'middle'
        halign: 'center'
        opposite_colors: root.opposite_colors


<BaseRectangularButton>
    canvas:
        Clear
        Color:
            rgba: self._current_button_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: (root._radius, )

    lbl_txt: lbl_txt
    height: dp(36) if not root._height else root._height
    width: lbl_txt.texture_size[0] + root.increment_width
    padding: (dp(8), 0)
    theme_text_color: 'Primary' if not root.text_color else 'Custom'
    markup: False

    MDLabel:
        id: lbl_txt
        text: root.text if root.button_label else ''
        font_size: sp(root.font_size)
        font_name: root.font_name if root.font_name is not None else self.font_name
        can_capitalize: root.can_capitalize
        size_hint_x: None
        text_size: (None, root.height)
        height: self.texture_size[1]
        theme_text_color: root.theme_text_color
        text_color: root.text_color
        markup: root.markup
        disabled: root.disabled
        valign: 'middle'
        halign: 'center'
        opposite_colors: root.opposite_colors


<MDRoundFlatButton>
    canvas.before:
        Color:
            rgba:
                root.theme_cls.primary_color \
                if root.md_bg_color == [0.0, 0.0, 0.0, 0.0] \
                else root.md_bg_color
        Line:
            width: 1
            rounded_rectangle:
                (self.x, self.y, self.width, self.height,\
                root._radius, root._radius, root._radius, root._radius,\
                self.height)

    theme_text_color: 'Custom'
    text_color:
        root.theme_cls.primary_color \
        if not root.text_color else root.text_color


<MDFillRoundFlatButton>
    canvas.before:
        Color:
            rgba:
                root.theme_cls.primary_color \
                if root.md_bg_color == [0.0, 0.0, 0.0, 0.0] \
                else root.md_bg_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [root._radius, ]

    text_color: root.specific_text_color


<MDFillRoundFlatIconButton>
    text_color: root.specific_text_color

    BoxLayout:
        spacing: dp(10)

        MDIcon:
            id: lbl_ic
            icon: root.icon
            theme_text_color: 'Custom'
            text_color:
                root.specific_text_color \
                if root.text_color == root.theme_cls.primary_color \
                else root.text_color
            size_hint_x: None
            #width: self.texture_size[0]


<MDRectangleFlatButton>
    canvas.before:
        Color:
            rgba:
                root.theme_cls.primary_color \
                if not root.text_color else root.text_color
        Line:
            width: 1
            rectangle: (self.x, self.y, self.width, self.height)

    theme_text_color: 'Custom'
    text_color:
        root.theme_cls.primary_color \
        if not root.text_color else root.text_color


<MDRectangleFlatIconButton>
    canvas.before:
        Color:
            rgba:
                root.theme_cls.primary_color \
                if not root.text_color else root.text_color
        Line:
            width: 1
            rectangle: (self.x, self.y, self.width, self.height)

    size_hint_x: None
    width: dp(150)
    markup: False

    BoxLayout:
        spacing: dp(10)

        MDIcon:
            id: lbl_ic
            icon: root.icon
            theme_text_color: 'Custom'
            text_color:
                root.theme_cls.primary_color \
                if not root.text_color else root.text_color
            size_hint_x: None
            width: self.texture_size[0]

        MDLabel:
            id: lbl_txt
            text: root.text
            font_size: sp(root.font_size)
            font_name: root.font_name if root.font_name is not None else self.font_name
            can_capitalize: root.can_capitalize
            shorten: True
            theme_text_color: 'Custom'
            text_color:
                root.theme_cls.primary_color \
                if not root.text_color else root.text_color
            markup: root.markup


<MDRoundFlatIconButton>
    size_hint_x: None
    width: dp(150)
    markup: False

    BoxLayout:
        spacing: dp(10)

        MDIcon:
            id: lbl_ic
            icon: root.icon
            theme_text_color: 'Custom'
            text_color:
                root.theme_cls.primary_color \
                if not root.text_color else root.text_color
            size_hint_x: None
            width: self.texture_size[0]

        MDLabel:
            id: lbl_txt
            text: root.text
            font_size: sp(root.font_size)
            font_name: root.font_name if root.font_name is not None else self.font_name
            can_capitalize: root.can_capitalize
            shorten: True
            theme_text_color: 'Custom'
            text_color:
                root.theme_cls.primary_color \
                if not root.text_color else root.text_color
            markup: root.markup


<MDRaisedButton>
    md_bg_color: root.theme_cls.primary_color
    theme_text_color: 'Custom'
    text_color: root.specific_text_color


<MDFloatingActionButton>
    # Defaults to 56-by-56 and a background of the accent color according to
    # guidelines
    size: (dp(56), dp(56))
    md_bg_color: root.theme_cls.accent_color
    theme_text_color: 'Custom'
    text_color: root.specific_text_color


<MDTextButton>
    size_hint: None, None
    size: self.texture_size
    color:
        root.theme_cls.primary_color \
        if not len(root.custom_color) else root.custom_color
    background_down: f'{images_path}transparent.png'
    background_normal: f'{images_path}transparent.png'
    opacity: 1


# SpeedDial classes


<BaseFloatingBottomButton>
    size_hint: None, None
    size: dp(46), dp(46)
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
    elevation: 5
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
            rgba: self.theme_cls.primary_color if not root.bg_color else root.bg_color
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


class BaseButton(
    ThemableBehavior,
    ButtonBehavior,
    SpecificBackgroundColorBehavior,
    AnchorLayout,
    Widget,
):
    """
    Abstract base class for all MD buttons. This class handles the button's
    colors (disabled/down colors handled in children classes as those depend on
    type of button) as well as the disabled state.
    """

    theme_text_color = OptionProperty(
        None,
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
    Button text type. Available options are: (`"Primary"`, `"Secondary"`,
    `"Hint"`, `"Error"`, `"Custom"`, `"ContrastParentBackground"`).

    :attr:`theme_text_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    text_color = ListProperty(None, allownone=True)
    """
    Text color in ``rgba`` format.

    :attr:`text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `None`.
    """

    font_name = StringProperty(None)
    """
    Font name.

    :attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
    """

    font_size = NumericProperty(14)
    """
    Font size.

    :attr:`font_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `14`.
    """

    user_font_size = NumericProperty()
    """Custom font size for :class:`~MDIconButton`.
    
    :attr:`user_font_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    opposite_colors = BooleanProperty(False)

    _md_bg_color_down = ListProperty(None, allownone=True)
    _md_bg_color_disabled = ListProperty(None, allownone=True)
    _current_button_color = ListProperty([0.0, 0.0, 0.0, 0.0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._finish_init)

    def _finish_init(self, dt):
        self._update_color()

    def on_md_bg_color(self, instance, value):
        self._update_color()

    def _update_color(self):
        if not self.disabled:
            self._current_button_color = self.md_bg_color
        else:
            self._current_button_color = self.md_bg_color_disabled

    def _call_get_bg_color_down(self):
        return self._get_md_bg_color_down()

    def _get_md_bg_color_down(self):
        if self._md_bg_color_down:
            return self._md_bg_color_down
        else:
            raise NotImplementedError

    def _set_md_bg_color_down(self, value):
        self._md_bg_color_down = value

    md_bg_color_down = AliasProperty(
        _call_get_bg_color_down, _set_md_bg_color_down
    )
    """
    Value of the current button background color.

    :attr:`md_bg_color_down` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`md_bg_color_down`,
    property is readonly.
    """

    def _call_get_bg_color_disabled(self):
        return self._get_md_bg_color_disabled()

    def _get_md_bg_color_disabled(self):
        if self._md_bg_color_disabled:
            return self._md_bg_color_disabled
        else:
            raise NotImplementedError

    def _set_md_bg_color_disabled(self, value):
        self._md_bg_color_disabled = value

    md_bg_color_disabled = AliasProperty(
        _call_get_bg_color_disabled, _set_md_bg_color_disabled
    )
    """
    Value of the current button disabled color.

    :attr:`md_bg_color_disabled` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`md_bg_color_disabled`,
    property is readonly.
    """

    def on_disabled(self, instance, value):
        if self.disabled:
            self._current_button_color = self.md_bg_color_disabled
        else:
            self._current_button_color = self.md_bg_color


class BasePressedButton(BaseButton):
    """
    Abstract base class for those button which fade to a background color on
    press.
    """

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
            self.fade_bg = Animation(
                duration=0.5, _current_button_color=self.md_bg_color_down
            )
            self.fade_bg.start(self)
            return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            self.fade_bg.stop_property(self, "_current_button_color")
            Animation(
                duration=0.05, _current_button_color=self.md_bg_color
            ).start(self)
        return super().on_touch_up(touch)


class BaseFlatButton(BaseButton):
    """
    Abstract base class for flat buttons which do not elevate from material.

    Enforces the recommended down/disabled colors for flat buttons
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = (0.0, 0.0, 0.0, 0.0)

    def _get_md_bg_color_down(self):
        if self.theme_cls.theme_style == "Dark":
            c = get_color_from_hex("cccccc")
            c[3] = 0.25
        else:
            c = get_color_from_hex("999999")
            c[3] = 0.4
        return c

    def _get_md_bg_color_disabled(self):
        bg_c = self.md_bg_color
        if bg_c[3] == 0:  # transparent background
            c = bg_c
        else:
            if self.theme_cls.theme_style == "Dark":
                c = (1.0, 1.0, 1.0, 0.12)
            else:
                c = (0.0, 0.0, 0.0, 0.12)
        return c


class BaseRaisedButton(CommonElevationBehavior, BaseButton):
    """
    Abstract base class for raised buttons which elevate from material.
    Raised buttons are to be used sparingly to emphasise primary/important
    actions.

    Implements elevation behavior as well as the recommended down/disabled
    colors for raised buttons.
    """

    def __init__(self, **kwargs):
        if self.elevation_raised == 0 and self.elevation_normal + 6 <= 12:
            self.elevation_raised = self.elevation_normal + 6
        elif self.elevation_raised == 0:
            self.elevation_raised = 12
        super().__init__(**kwargs)
        self.elevation_press_anim = Animation(
            elevation=self.elevation_raised, duration=0.2, t="out_quad"
        )
        self.elevation_release_anim = Animation(
            elevation=self.elevation_normal, duration=0.2, t="out_quad"
        )

    _elev_norm = NumericProperty(2)

    def _get_elev_norm(self):
        return self._elev_norm

    def _set_elev_norm(self, value):
        self._elev_norm = value if value <= 12 else 12
        self._elev_raised = (value + 6) if value + 6 <= 12 else 12
        self.elevation = self._elev_norm
        self.elevation_release_anim = Animation(
            elevation=value, duration=0.2, t="out_quad"
        )

    elevation_normal = AliasProperty(
        _get_elev_norm, _set_elev_norm, bind=("_elev_norm",)
    )
    _elev_raised = NumericProperty(8)

    def _get_elev_raised(self):
        return self._elev_raised

    def _set_elev_raised(self, value):
        self._elev_raised = value if value + self._elev_norm <= 12 else 12
        self.elevation_press_anim = Animation(
            elevation=value, duration=0.2, t="out_quad"
        )

    elevation_raised = AliasProperty(
        _get_elev_raised, _set_elev_raised, bind=("_elev_raised",)
    )

    def on_disabled(self, instance, value):
        if self.disabled:
            self.elevation = 0
        else:
            self.elevation = self.elevation_normal
        super().on_disabled(instance, value)

    def on_touch_down(self, touch):
        if not self.disabled:
            if touch.is_mouse_scrolling:
                return False
            if not self.collide_point(touch.x, touch.y):
                return False
            if self in touch.ud:
                return False
            self.elevation_press_anim.stop(self)
            self.elevation_press_anim.start(self)
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if not self.disabled:
            if touch.grab_current is not self:
                return super().on_touch_up(touch)
            self.elevation_release_anim.stop(self)
            self.elevation_release_anim.start(self)
        return super().on_touch_up(touch)

    def _get_md_bg_color_down(self):
        t = self.theme_cls
        c = self.md_bg_color  # Default to no change on touch
        # Material design specifies using darker hue when on Dark theme
        if t.theme_style == "Dark":
            if self.md_bg_color == t.primary_color:
                c = t.primary_dark
            elif self.md_bg_color == t.accent_color:
                c = t.accent_dark
        return c

    def _get_md_bg_color_disabled(self):
        if self.theme_cls.theme_style == "Dark":
            c = (1.0, 1.0, 1.0, 0.12)
        else:
            c = (0.0, 0.0, 0.0, 0.12)
        return c


class BaseRoundButton(CircularRippleBehavior, BaseButton):
    """
    Abstract base class for all round buttons, bringing in the appropriate
    on-touch behavior
    """

    pass


class BaseRectangularButton(RectangularRippleBehavior, BaseButton):
    """
    Abstract base class for all rectangular buttons, bringing in the
    appropriate on-touch behavior. Also maintains the correct minimum width
    as stated in guidelines.
    """

    width = BoundedNumericProperty(
        88, min=88, max=None, errorhandler=lambda x: 88
    )
    text = StringProperty("")
    """Button text.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    increment_width = NumericProperty("32dp")
    """
    Button extra width value.

    :attr:`increment_width` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'32dp'`.
    """

    button_label = BooleanProperty(True)
    """
    If ``False`` the text on the button will not be displayed.

    :attr:`button_label` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    can_capitalize = BooleanProperty(True)

    _radius = NumericProperty("2dp")
    _height = NumericProperty(0)


class MDIconButton(BaseRoundButton, BaseFlatButton, BasePressedButton):
    icon = StringProperty("checkbox-blank-circle")
    """
    Button icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle'`.
    """


class MDFlatButton(BaseRectangularButton, BaseFlatButton, BasePressedButton):
    pass


class BaseFlatIconButton(MDFlatButton):
    icon = StringProperty("android")
    """
    Button icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    text = StringProperty("")
    """Button text.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    button_label = BooleanProperty(False)


class MDRaisedButton(
    BaseRectangularButton,
    RectangularElevationBehavior,
    BaseRaisedButton,
    BasePressedButton,
):
    pass


class MDFloatingActionButton(
    BaseRoundButton, CircularElevationBehavior, BaseRaisedButton
):
    icon = StringProperty("android")
    """
    Button icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    background_palette = StringProperty("Accent")
    """
    The name of the palette used for the background color of the button.

    :attr:`background_palette` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Accent'`.
    """


class MDRoundImageButton(MDFloatingActionButton):
    source = StringProperty()
    """Path to button image.

    :attr:`source` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    _current_button_color = [1, 1, 1, 1]

    def on_source(self, instance, value):
        self.source = value

    def on_size(self, instance, value):
        self.remove_widget(self.ids.lbl_txt)


class MDRectangleFlatButton(MDFlatButton):
    pass


class MDRoundFlatButton(MDFlatButton):
    _radius = NumericProperty("18dp")

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


class MDTextButton(ThemableBehavior, Button):
    custom_color = ListProperty()
    """Custom user button color if ``rgba`` format.

    :attr:`custom_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    def animation_label(self):
        def set_default_state_label(*args):
            Animation(opacity=1, d=0.1, t="in_out_cubic").start(self)

        anim = Animation(opacity=0.5, d=0.2, t="in_out_cubic")
        anim.bind(on_complete=set_default_state_label)
        anim.start(self)

    def on_press(self, *args):
        self.animation_label()
        return super().on_press(*args)


class MDCustomRoundIconButton(CircularRippleBehavior, ButtonBehavior, Image):
    pass


class MDFillRoundFlatButton(MDRoundFlatButton):
    pass


class MDRectangleFlatIconButton(BaseFlatIconButton):
    pass


class MDRoundFlatIconButton(MDRoundFlatButton, BaseFlatIconButton):
    pass


class MDFillRoundFlatIconButton(MDFillRoundFlatButton):
    icon = StringProperty("android")
    """
    Button icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    increment_width = NumericProperty("80dp")
    """
    Button extra width value.

    :attr:`increment_width` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'80dp'`.
    """


# SpeedDial classes


class BaseFloatingRootButton(MDFloatingActionButton):
    _angle = NumericProperty(0)


class BaseFloatingBottomButton(MDFloatingActionButton, MDTooltip):
    _canvas_width = NumericProperty(0)
    _padding_right = NumericProperty(0)
    _bg_color = ListProperty()


class BaseFloatingLabel(
    ThemableBehavior, RectangularElevationBehavior, BoxLayout
):
    text = StringProperty()
    text_color = ListProperty()
    bg_color = ListProperty()


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

    label_text_color = ListProperty([0, 0, 0, 1])
    """
    Floating text color in ``rgba`` format.

    :attr:`label_text_color` is a :class:`~kivy.properties.ListProperty`
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
    If `True`, the button will increase on the right side by 2.5 piesels
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

    rotation_root_button = BooleanProperty(False)
    """
    If ``True`` then the root button will rotate 45 degrees when the stack
    is opened.

    :attr:`rotation_root_button` is a :class:`~kivy.properties.BooleanProperty`
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

    bg_color_root_button = ListProperty()
    """
    Root button color in ``rgba`` format.

    :attr:`bg_color_root_button` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    bg_color_stack_button = ListProperty()
    """
    The color of the buttons in the stack ``rgba`` format.

    :attr:`bg_color_stack_button` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    color_icon_stack_button = ListProperty()
    """
    The color icon of the buttons in the stack ``rgba`` format.

    :attr:`color_icon_stack_button` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    color_icon_root_button = ListProperty()
    """
    The color icon of the root button ``rgba`` format.

    :attr:`color_icon_root_button` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    bg_hint_color = ListProperty()
    """
    Background color for the text of the buttons in the stack ``rgba`` format.

    :attr:`bg_hint_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
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
                    if self.data[instance.icon] == widget.text:
                        Animation(
                            _canvas_width=0,
                            _padding_right=0,
                            d=self.opening_time,
                            t=self.opening_transition,
                        ).start(instance)
                        if self.hint_animation:
                            Animation(
                                opacity=0, d=0.1, t=self.opening_transition,
                            ).start(widget)
                        break

    def on_enter(self, instance):
        """Called when the mouse cursor is over a button from the stack."""

        if self.state == "open":
            for widget in self.children:
                if isinstance(widget, MDFloatingLabel) and self.hint_animation:
                    widget.elevation = 0
                    if self.data[instance.icon] == widget.text:
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

    def on_data(self, instance, value):
        """Creates a stack of buttons."""

        # Bottom buttons.
        for name_icon in self.data.keys():
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
            floating_text = value[name_icon]
            if floating_text:
                label = MDFloatingLabel(text=floating_text, opacity=0)
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
            l = dp(56)
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
                    l += dp(56)
                    # Sets the position of signatures only once.
                    if not self._label_pos_y_set:
                        widget.y = widget.y * 2 + l
                        widget.x = Window.width - widget.width - dp(86)
                    if not self._anim_labels_data:
                        anim_labels_data[widget] = Animation(
                            opacity=1, d=self.opening_time
                        )
                elif (
                    isinstance(widget, MDFloatingRootButton)
                    and self.rotation_root_button
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
                and self.rotation_root_button
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
