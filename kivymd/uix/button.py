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
- MDBevelFlatButton_
- MDBevelFlatIconButton_
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
Use :class:`~BaseButton.font_size` attribute to resize the button:

.. code-block:: kv

    MDIconButton:
        icon: "android"
        font_size: "64sp"

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
        font_size : "18sp"
        font_name: "path/to/font"

.. warning:: You cannot use the ``size_hint_x`` parameter for `KivyMD` buttons
    (the width of the buttons is set automatically)!

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

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-rectangle-flat-icon-button.png
    :align: center

Button parameters :class:`~MDRectangleFlatButton` are the same as
button :class:`~MDRectangleFlatButton`:

.. code-block:: kv

    MDRectangleFlatIconButton:
        icon: "android"
        text: "MDRECTANGLEFLATICONBUTTON"

Without border
--------------

.. code-block:: python

    from kivy.uix.screenmanager import Screen

    from kivymd.app import MDApp
    from kivymd.uix.button import MDRectangleFlatIconButton


    class Example(MDApp):
        def build(self):
            screen = Screen()
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

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-round-flat-button.png
    :align: center

Button parameters :class:`~MDRoundFlatButton` are the same as
button :class:`~MDRectangleFlatButton`:

.. code-block:: kv

    MDRoundFlatButton:
        text: "MDROUNDFLATBUTTON"

.. warning:: The border color does change when using ``text_color`` parameter.

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
            'language-php' 'PHP',
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
    "MDBevelFlatButton",
    "MDBevelFlatIconButton",
    "MDFillRoundFlatButton",
    "MDFillRoundFlatIconButton",
    "MDTextButton",
    "MDFloatingActionButtonSpeedDial",
)

from pathlib import Path

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Line, Mesh, Rectangle
from kivy.graphics.context_instructions import Color
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics.stencil_instructions import (
    StencilPop,
    StencilPush,
    StencilUnUse,
    StencilUse,
)
from kivy.graphics.vertex_instructions import Ellipse, RoundedRectangle
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.metrics import dp, sp
from kivy.properties import (
    BooleanProperty,
    BoundedNumericProperty,
    DictProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    ReferenceListProperty,
    StringProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from kivymd import images_path
from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    CircularElevationBehavior,
    CircularRippleBehavior,
    CommonElevationBehavior,
    RectangularElevationBehavior,
    RectangularRippleBehavior,
)
from kivymd.uix.label import MDIcon, MDLabel
from kivymd.uix.tooltip import MDTooltip

Builder.load_string(
    """
#:import images_path kivymd.images_path
#:import md_icons kivymd.icon_definitions.md_icons
    """,
    filename="MDButtons.kv",
)


class button_background_behavior(Widget):
    r = BoundedNumericProperty(
        None,
        min=0.0,
        max=1.0,
        errorhandler=lambda x: 0 if x < 0 else (1 if x > 1 else x),
    )
    """The value of ``red`` in the ``rgba`` palette.

    :attr:`r` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `1.0`.
    """

    g = BoundedNumericProperty(
        None,
        min=0.0,
        max=1.0,
        errorhandler=lambda x: 0 if x < 0 else (1 if x > 1 else x),
    )
    """The value of ``green`` in the ``rgba`` palette.

    :attr:`g` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `1.0`.
    """

    b = BoundedNumericProperty(
        None,
        min=0.0,
        max=1.0,
        errorhandler=lambda x: 0 if x < 0 else (1 if x > 1 else x),
    )
    """The value of ``blue`` in the ``rgba`` palette.

    :attr:`b` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `1.0`.
    """

    a = BoundedNumericProperty(
        None,
        min=0.0,
        max=1.0,
        errorhandler=lambda x: 0 if x < 0 else (1 if x > 1 else x),
    )
    """The value of ``alpha channel`` in the ``rgba`` palette.

    :attr:`a` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `0.0`.
    """
    radius = BoundedNumericProperty(
        1,
        min=dp(2),
        max=None,
    )
    """Canvas radius.

    .. code-block:: python

        # Top left corner slice.
        MDBoxLayout:
            md_bg_color: app.theme_cls.primary_color
            radius: [25, 0, 0, 0]

    :attr:`radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    md_bg_color = ReferenceListProperty(r, g, b, a)
    """The background color of the widget (:class:`~kivy.uix.widget.Widget`)
    that will be inherited from the :attr:`BackgroundColorBehavior` class.

    For example:

    .. code-block:: kv

        Widget:
            canvas:
                Color:
                    rgba: 0, 1, 1, 1
                Rectangle:
                    size: self.size
                    pos: self.pos

    similar to code:

    .. code-block:: kv

        <MyWidget@BackgroundColorBehavior>
            md_bg_color: 0, 1, 1, 1

    :attr:`md_bg_color` is an :class:`~kivy.properties.ReferenceListProperty`
    and defaults to :attr:`r`, :attr:`g`, :attr:`b`, :attr:`a`.
    """


# ------------------------------------------------------------------------------
# BaseButton
# ------------------------------------------------------------------------------
#

Builder.load_string(
    """
<BaseButton>:
    size_hint: (None, None)
    anchor_x: 'center'
    anchor_y: 'center'
    # canvas.before:
    #     Color:
    #         rgba:1,1,1,1
    #     Rectangle:
    #         pos:self.pos
    #         size:self.size
""",
    filename="MDBaseButton.kv",
)


class BaseButton(
    ThemableBehavior,
    ButtonBehavior,
    button_background_behavior,
    AnchorLayout,
    Widget,
):
    """
    Abstract root class for all MD buttons.

    The BaseButton Class handles all the buttons Backend events and behaviors.

    .. wrning:: Do not use Alone.
        This base class must never be used alone, since this class has no UI
        instruction.

    This base class is the core of every button. normailizing the behavior
    between them all.

    .. note::
        This class is optimized by the use of flags. This flags allow or avoid the
        processing of the change of a property.
        For example, if the button has filling but no icon; This base class will
        then only execute the event related to the filling of the button and avoid
        any instruction related to the icon.

    The current avalilable flags are:
        #. :attr:`_is_filled` controlls if the button has a filling color or not
        #. :attr:`_has_line`  Controls if the widget mus be drawn with an outline it's colors
        #. :attr:`_has_text`  Controls if the widget has any text and it's colors
        #. :attr:`_has_icon`  Controls if the widget has any icon and it's colors

    All of the flags are :class:'~kivy.properties.BooleanProperty' wich default
    value is 'False'.

    """

    # -------------------------------------------------------------------------
    # Properties

    text = StringProperty("")
    """Test of the button.
    The text parameter will define the button's size.
    """

    show_label = BooleanProperty(None)
    """
    This property controls wheter if the button must or not Display the current label.
    This property is currently controlled by KV lang.

    :attr:`show_label` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """
    _current_markup = BooleanProperty(False)
    markup = BooleanProperty(False)
    """
    This property enables or dissables the markup processing in the button's
    Label, and only affects buttons that have a label.

    This property does not affect any icon button.

    .. note:: markup language.
    The MDlabel's markup langage is inherited from
    :class:`~kivy.uix.label.Label`.
    """

    lbl_txt = ObjectProperty()
    #
    text_color = ListProperty(None, allownone=False)
    """
    The color of the text in ``rgba`` format.

    :attr:`text_color` is a :class:`~kivy.properties.ListProperty`
    defaults to `[]`.
    """
    disabled_text_color = ListProperty(None, allownone=False)

    font_name = StringProperty("")
    """
    Font name.

    :attr:`font_name` is a :class:`~kivy.properties.StringProperty`
    defaults to `''`.
    """

    _current_font_size = BoundedNumericProperty(
        sp(14),
        min=sp(4),
        max=None,
        errorhandler=lambda x: sp(4),
    )
    # NumericProperty(14)
    """
    Font size.

    :attr:`_current_font_size ` is a :class:`~kivy.properties.NumericProperty`
    defaults to `14`.
    """

    font_size = NumericProperty(None)
    """Custom font size for :class:`~MDIconButton`.

    :attr:`font_size` is a :class:`~kivy.properties.NumericProperty`
    defaults to `0`.
    """

    icon = StringProperty(None)
    """Icon of the button. The icon must exists inside the icon_definitions
    dictionary otherwise, no icon will be shown.

    :attr:`icon` is a :class:`~kivy.properties.StringProperty`
    defaults to `''`.
    """
    icon_position = OptionProperty(None, options=["left", "right", "icon_only"])
    """
    This property defines the position of the icon.
    if it should be drawn before the text, after the text or if it should be
    only the icon drawn on screen.
    """

    md_bg_color_disabled = ListProperty()
    """Color disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ListProperty`
    defaults to `[]`.
    """

    line_color = ListProperty(None)
    """
    """

    line_width = NumericProperty("1dp")
    """
    """

    opposite_colors = BooleanProperty(None)
    """
    This porperty sets the opposite color theme for every theme text color.
    This only affects Primary, Secondary, Hint color themes.
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
            "Primary_color",
            "Accent_color",
            "White",
        ],
    )
    """
    Color theme of the Buttons's icon.

    Available options are: ( `"Primary"`, `"Secondary"`,
    `"Hint"`, `"Error"`, `"Custom"`, `"ContrastParentBackground"`,
    `"Primary_color"`, `"Accent_color"` ).

    .. warning:: Do not set to None:
        This set it's only meant to work as a placeholed when a new instance is
        created.
        After creation, the set will be automatically change to either "Primary"
        or "Custom" option. unless it already has a different setting.

    :attr:`theme_text_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    theme_icon_color = OptionProperty(
        None,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
            "Primary_color",
            "Accent_color",
            "White",
            "Text",
        ],
    )
    icon_color = ListProperty(None)
    """
    Color theme of the Buttons's icon.

    Available options are: ( `"Primary"`, `"Secondary"`,
    `"Hint"`, `"Error"`, `"Custom"`, `"ContrastParentBackground"`,
    `"Primary_color"`, `"Accent_color"` ).

    When the property is set to "Custom", the button's icon color will
    match the buttons.icon_color property.

    app.theme_cls.primary_color update event will be dissmised.
    (icon's color evaluation)

    .. warning:: Do not set to None:
        This set it's only meant to work as a placeholed when a new instance is
        created.

    :attr:`theme_icon_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    theme_button_color = OptionProperty(
        None,
        options=["Primary", "Accent", "Custom", "Error"],
    )
    """
    Button's Background Theme.

    This Property sets the button's background color behavior.

    When the property is set to "Primary", the button's background color will
    match the one from the theme_cls.primary_color.
    And the color will be updated everytime the primary pallete is changed.

    When the property is set to "Custom", the button's background color will
    match the buttons.md_bg_color property.
    app.theme_cls.primary_color update event will be dissmised.

    .. warning:: Do not set to None:
        This set it's only meant to work as a placeholed when a new instance is
        created.
        After creation, the set will be automatically change to either "Primary"
        or "Custom" option. unless it already has a different setting.


    :attr:`theme_button_color` is an :class:`~kivy.properties.OptionProperty`
    and is default to `None`.

    The available options are "None", "Primary", "Accent" and "Custom"
    """
    theme_line_color = OptionProperty(
        None,
        options=[
            "Text",
            "Icon",
            "Primary",
            "Custom",
            "Primary_color",
            "Accent_color",
        ],
    )
    """
    This property sets the button's outline color behavior.

    When the property is set to "Primary", the button's Outline color will
    match the one from the theme_cls.primary_color.
    And the color will be updated everytime the primary pallete is changed.

    When the property is set to "Custom", the button's background color will
    match the buttons.md_bg_color property.
    app.theme_cls.primary_color update event will be dissmised.

    .. warning:: Do not set to None:
        This set it's only meant to work as a placeholed when a new instance is
        created.
        After creation, the set will be automatically change to either "Primary"
        or "Custom" option. unless it already has a different setting.
    """
    # True Backend Colors, the canvas should pick the color from here
    # and the outside properties will update this values when necesary
    _current_button_color = ListProperty([1.0, 1.0, 1.0, 0.0])
    _current_text_color = ListProperty([1.0, 1.0, 1.0, 0.0])
    # _current_text = StringProperty("")
    _current_icon_color = ListProperty([1.0, 1.0, 1.0, 0.0])
    _current_line_color = ListProperty([1.0, 1.0, 1.0, 0.0])

    # State Color (Down, and Disabled)
    _md_bg_color_down = ListProperty([0.0, 0.0, 0.0, 0.1])
    _md_bg_color_disabled = ListProperty([0.0, 0.0, 0.0, 0.0])

    # Theme text color that's parsed to the Label
    _current_theme_text_color = OptionProperty(
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
    _current_theme_icon_color = OptionProperty(
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

    corner_type = OptionProperty(
        None, options=["Square", "Rounded", "Bevel", None], allownone=True
    )
    """
    This option property set the corner type, this porperty affects both the
    outline and the background shape and even the ripple behavior!!!
    avalilable options are:
    `"Square"`, `"Rounded"`, `"Bevel"`, deffault to None
    """
    # This opitons are for subvlassing, improves performance by avoiding
    # unecesary property update events.

    # Define if the widget background color must be procesed
    _is_filled = BooleanProperty(None)

    # Define if the widget outline color must be procesed
    _has_line = BooleanProperty(None)

    # Define if the widget text color must be procesed
    _has_text = BooleanProperty(None)

    # Define if the widget icon color must be procesed
    _has_icon = BooleanProperty(None)

    # Size of the Rounded Corner
    _radius = BoundedNumericProperty(
        1,
        min=1,
        max=None,
    )
    radius = NumericProperty(None)

    # height of the button
    _height = NumericProperty(0)

    # Root container
    container = ObjectProperty()

    # Deprecated
    user_font_size = NumericProperty(deprecated=True)
    """
    Custom font size for all :class:`~icon_behavior` classes.

    :attr:`font_size` is a :class:`~kivy.properties.NumericProperty`
    defaults to `0`.

    .. warning::
    The user_font_size property is deprecated and will be removed in future
    verisons, please use font_size instead.

    """

    def on_user_font_size(self, instance, value):
        Logger.info(
            "BaseButton: user_font_size is deprecated ::\n"
            "This property is now deprecated and will be "
            "removed in future updates. use font_size instead."
        )
        self.font_size = value

    # -------------------------------------------------------------------------
    # Function Definitions

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(primary_palette=self._on_primary_palette)
        Clock.schedule_once(self.__after_init__, -1)

    def __after_init__(self, *args):
        if self.opposite_colors is None:
            self.opposite_colors = False
        # Background configurations
        if self._is_filled is True:
            if self.theme_button_color is None:
                if self.md_bg_color == [None] * 4:
                    self.theme_button_color = "Primary"
                    self.md_bg_color = self.theme_cls._get_primary_color()
                else:
                    self.theme_button_color = "Custom"
            else:
                self.on_theme_button_color(self, self.theme_button_color)
        #
        if self.md_bg_color_disabled:
            self._md_bg_color_disabled = self.md_bg_color_disabled
        else:
            self._md_bg_color_disabled = self.theme_cls.disabled_hint_text_color
        # Text Configurations
        if self._has_text is True:
            if self.text_color is None:
                if self.theme_text_color is None:
                    self.theme_text_color = "Primary_color"
                    self.text_color = self._current_text_color
            else:
                self.theme_text_color = "Custom"
        if self.disabled_text_color is None:
            self.disabled_text_color = self.theme_cls.disabled_hint_text_color
        # Icon Configurations
        # Moved to icon_behavior.__after_init__
        # Line Configurations
        self.on_opposite_colors(self, self.on_opposite_colors)
        self.on__is_filled(self, self._is_filled)
        self.on_font_size(self, self.font_size)
        self.on_theme_button_color(self, self.theme_button_color)
        self.on_theme_text_color(self, self.theme_text_color)
        self.on_theme_icon_color(self, self.theme_icon_color)
        self.on_theme_line_color(self, self.theme_line_color)
        self.on_disabled(self, self.disabled)

    def on_radius(self, instance, value):
        if value > self.height // 2:
            self._radius = self.height // 2
            # self.radius = self._radius
        else:
            self._radius = self.radius

    def on_text(self, instance, value):
        self.on_theme_text_color(self, self.theme_text_color)

    def on_icon(self, instance, value):
        self.on_theme_icon_color(self, self.theme_icon_color)
        # Call the theme property of the icon property.

    def on__is_filled(self, instance, value):
        """
        This property's on_ event sets te current _current_button_color to
        transparent if the value is False. (meaning it should have no filling)

        otherwise, calls on_theme_button_color to update the background color
        according to the theme_button_color OoptionProperty.
        """
        if value is False:
            self._current_button_color[-1] = 0
        else:
            self.on_theme_button_color(self, self.theme_button_color)

    def _on_primary_palette(self, instance, value):
        """
        This funciton request the new color pallete of theme_cls and assigns it
        to the :attr:`_current_button_color`

        .. None:: External call
        This event is Called everytime the application's color palette changes.
        """
        # self.on_theme_button_color(self, self.theme_button_color)
        # Verifica el color de texto
        if self._is_filled:
            self.on_theme_button_color(self, self.theme_button_color)
        if self._has_text and self.show_label:
            self.on_theme_text_color(self, self.theme_text_color)
        if self._has_line:
            self.on_theme_line_color(self, self.theme_line_color)
        if self._has_icon:
            self.on_theme_icon_color(self, self.theme_icon_color)
        #

    def on_theme_button_color(self, ins, val):
        """
        This fucntion process the color theme of the buttons's background.

        this theme is not linked to any other configuration.
        """
        if self._is_filled is True:
            if self.disabled is True:
                self._current_button_color = (
                    self.theme_cls.disabled_hint_text_color
                )
                return
            if self.theme_button_color == "Primary":
                self._current_button_color = (
                    self.theme_cls._get_primary_color()[:]
                )

            elif self.theme_button_color == "Accent":
                self._current_button_color = self.theme_cls.accent_color

            elif self.theme_button_color == "Error":
                self._current_button_color = self.theme_cls.error_color

            elif self.theme_button_color == "Custom":
                if self.md_bg_color != [None] * 4:
                    self._current_button_color = self.md_bg_color
                else:
                    Logger.error(
                        f"{self.__class__}: on_theme_button_color :: Error\n\t"
                        "theme_button_color can't be 'Custom' if theres no"
                        "self.md_bg_color value\n\t"
                        "md_bg_color = {self.md_bg_color} invalid!!!"
                    )
                    self.theme_button_color = "Primary"
        else:
            self._current_button_color[-1] = 0

    def on_theme_text_color(self, instance, value):
        """
        This fucntion process the color theme of the buttons's Label.

        This property also updates the line and icon's color if their theme is
        set to `"Text"`.
        """
        if self._has_text is True:
            theme = self.theme_cls
            if self.disabled is True:
                self._current_theme_text_color = "Custom"
                self._current_text_color = (
                    self.theme_cls.disabled_hint_text_color
                )
                return
            if value == "Primary":
                self._current_theme_text_color = "Primary"
            elif value == "Secondary":
                self._current_theme_text_color = "Secondary"

            elif value == "Hint":
                self._current_theme_text_color = "Hint"

            elif value == "Error":
                self._current_theme_text_color = "Error"

            elif value == "ContrastParentBackground":
                self._current_theme_text_color = "ContrastParentBackground"

            elif value == "Custom":
                self._current_theme_text_color = "Custom"
                if self._is_filled is True:
                    if self.text_color == self._current_button_color:
                        self.text_color = [1] * 4
                    else:
                        if self.text_color:
                            self._current_text_color = self.text_color
                        else:
                            self.theme_text_color = "Primary"
                else:
                    if self.text_color:
                        self._current_text_color = self.text_color
                    else:
                        self.theme_text_color = "Primary"
                        # self._current_text_color = [0] * 4
            elif value == "Accent_color":
                self._current_theme_text_color = "Custom"
                self._current_text_color = theme.accent_color

            elif value == "Primary_color":
                self._current_theme_text_color = "Custom"
                self._current_text_color = theme.primary_color

            elif value == "White":
                self._current_theme_text_color = "Custom"
                self._current_text_color = [1, 1, 1, 1]

            if self.theme_line_color == "Text":
                Clock.schedule_once(
                    lambda x: self.on_theme_line_color(
                        self, self.theme_line_color
                    ),
                    -1,
                )
            if self.theme_icon_color == "Text":
                Clock.schedule_once(
                    lambda x: self.on_theme_icon_color(
                        self, self.theme_icon_color
                    ),
                    -1,
                )
            if self._is_filled is True:
                if self._current_text_color == self._current_button_color:
                    self._current_text_color = [1] * 4

    def on_theme_icon_color(self, instance, value):
        """
        This fucntion process the color theme of the buttons's Icon.
        """
        if self._has_icon:  # and self.disabled is False:
            theme = self.theme_cls
            self.unbind(
                _current_text_color=lambda x, y: setattr(
                    self, "_current_icon_color", y
                )
            )
            if self.disabled is True:
                self._current_theme_icon_color = "Custom"
                self._current_icon_color = (
                    self.theme_cls.disabled_hint_text_color
                )
                return
            if self.theme_icon_color == "Primary":
                self._current_theme_icon_color = "Primary"
            #
            elif self.theme_icon_color == "Secondary":
                self._current_theme_icon_color = "Secondary"
            #
            elif self.theme_icon_color == "Hint":
                self._current_theme_icon_color = "Hint"
            #
            elif self.theme_icon_color == "Error":
                self._current_theme_icon_color = "Error"
            #
            elif self.theme_icon_color == "ContrastParentBackground":
                self._current_theme_icon_color = "ContrastParentBackground"
            #
            elif self.theme_icon_color == "Custom":
                self._current_theme_icon_color = "Custom"
                if self.icon_color is None:
                    self.theme_icon_color = "Primary"
                else:
                    self._current_icon_color = self.icon_color
            #
            elif self.theme_icon_color == "Accent_color":
                self._current_theme_icon_color = "Custom"
                self._current_icon_color = theme.accent_color
            #
            elif self.theme_icon_color == "Primary_color":
                self._current_theme_icon_color = "Custom"
                self._current_icon_color = theme.primary_color
            #
            elif self.theme_icon_color == "White":
                self._current_theme_icon_color = "Custom"
                self._current_icon_color = [1, 1, 1, 1]
            #
            elif self.theme_icon_color == "Text":
                if self.lbl_txt:
                    self._current_theme_icon_color = "Custom"
                    self._current_icon_color = self.lbl_txt.color[:]
                    self.bind(
                        _current_text_color=lambda x, y: setattr(
                            self, "_current_icon_color", y
                        )
                    )
                else:
                    self.theme_icon_color = "Primary"
            #
            if self._is_filled:
                if self.md_bg_color == self._current_icon_color:
                    self._current_icon_color = [1] * 4
        else:
            self._current_icon_color[-1] = 0

    def on_opposite_colors(self, instance, value):
        self.on_theme_text_color(self, self.theme_text_color)
        self.on_theme_icon_color(self, self.theme_icon_color)
        self.on_theme_line_color(self, self.theme_line_color)

    def on__has_line(self, instance, value):
        self.on_theme_line_color(self, self.theme_line_color)

    def on_line_color(self, instance, value):
        self.on_theme_line_color(self, self.theme_line_color)

    def on_theme_line_color(self, instance, value):
        """
        This fucntion process the color theme of the buttons's outline.

        this theme is not linked to any other configuration.
        """
        if self._has_line is True:
            theme = self.theme_cls
            op = (not self.opposite_colors) if self.opposite_colors else False
            self.unbind(
                _current_text_color=lambda x, y: setattr(
                    self, "_current_line_color", y
                )
            )
            if self.theme_line_color == "Primary":
                self._current_line_color = (
                    theme.text_color if op else theme.opposite_text_color
                )

            elif self.theme_line_color == "Secondary":
                self._current_line_color = (
                    theme.secondary_text_color
                    if op
                    else theme.opposite_secondary_text_color
                )

            elif self.theme_line_color == "Hint":
                self._current_line_color = (
                    theme.disabled_hint_text_color
                    if op
                    else theme.opposite_disabled_hint_text_color
                )

            elif self.theme_line_color == "Error":
                self._current_line_color = theme.error_color

            elif self.theme_line_color == "Custom":
                # Force reload of the color
                # self._current_line_color = [0, 0, 0, 0]
                if self.line_color:
                    self._current_line_color = self.line_color
                else:
                    self.theme_line_color = "Primary_color"
                    # self.line_color = [0,0,0,1]
                pass

            elif self.theme_line_color == "Primary_color":
                self._current_line_color = theme.primary_color
                pass

            elif self.theme_line_color == "Accent_color":
                self._current_line_color = theme.accent_color
                pass

            elif self.theme_line_color == "White":
                self._current_line_color = [1, 1, 1, 1]

            elif self.theme_line_color == "Text":
                if self.lbl_txt:
                    self._current_line_color = self.lbl_txt.color[:]
                    self.bind(
                        _current_text_color=lambda x, y: setattr(
                            self, "_current_line_color", y
                        )
                    )

        else:
            self._current_line_color[-1] = 0

    def on_md_bg_color(self, instance, value):
        """
        Event launched when the button's md_bg_color property is changed.
        """
        if self._has_text:
            if any([x > 0.9 for x in value[:3]]):
                self._current_text_color = [0, 0, 0, 0]
        self.on_theme_button_color(self, self.theme_button_color)

    def on_text_color(self, instance, value):
        """
        Event launched when the button's text_color property is changed.
        """
        self.on_theme_text_color(self, self.theme_text_color)

    def on_icon_color(self, instance, value):
        """
        Event launched when the button's icon_color property is changed.
        """
        self.on_theme_icon_color(self, self.theme_icon_color)

    def on_disabled(self, instance, value):
        """
        Event launched when the button's disabled property is changed.
        """
        if self.disabled is True:
            if self._is_filled:
                self._current_button_color = self._md_bg_color_disabled
            if self._has_text:
                self._current_text_color = (
                    self.theme_cls.opposite_disabled_hint_text_color
                    if self.disabled_text_color is None
                    else self.disabled_text_color
                )
            if self._has_icon:
                self._current_icon_color = (
                    self.theme_cls.opposite_disabled_hint_text_color
                    if self.disabled_text_color is None
                    else self.disabled_text_color
                )
        else:
            if self._has_text:
                self.on_theme_text_color(self, self.theme_text_color)
            if self._has_icon:
                self.on_theme_icon_color(self, self.theme_icon_color)
            if self._is_filled:
                self.on_theme_button_color(self, self.theme_button_color)
            else:
                self._current_button_color[-1] = 0
        self._on_primary_palette(self, None)

    def on_font_size(self, instance, value):
        """
        Event launched when the button's font_size property is changed.
        """
        if value is not None:
            if value >= sp(4):
                self._current_font_size = value
            else:
                self.font_size = sp(4)
                self._current_font_size = sp(4)


class shaped_background_behaivor(BaseButton):
    # TODO Add to base button
    __bg_instruction = ObjectProperty()
    __bg_cl_instruction = ObjectProperty()
    __bg_coords = ObjectProperty()
    __bg_group_instructions = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__bg_group_instructions = InstructionGroup()
        Clock.schedule_once(
            lambda x: self.canvas.before.add(self.__bg_group_instructions), -1
        )

    def __after_init__(self, *dt):
        self._update_bg_color(self, self._current_button_color)
        self.bind(_current_button_color=self._update_bg_color)
        self.bind(_is_filled=self._update_bg_color)
        self.bind(pos=self._update_shape_coords)
        self.bind(size=self._update_shape_coords)
        super().__after_init__(*dt)

    def _update_shape_coords(self, *dt):
        if self.corner_type is not None:
            if self.radius:
                self.radius = (
                    self.height // 2
                    if self.radius > self.size[1] // 2
                    else self.radius
                )
            else:
                self.radius = self.height // 2
            if self._is_filled and self.__bg_instruction:
                if self.corner_type == "Square":
                    self.__bg_instruction.pos = self.pos
                    self.__bg_instruction.size = self.size
                    #
                if self.corner_type == "Rounded":
                    self.__bg_instruction.size = self.size
                    self.__bg_instruction.pos = self.pos
                    self.__bg_instruction.radius = [self._radius]
                    #
                if self.corner_type == "Bevel":
                    self.__bg_coords[0] = [
                        self.x + self._radius,
                        self.y,
                        self.right - self._radius,
                        self.y,
                        #
                        self.right - self._radius,
                        self.y,
                        self.right,
                        self.y + self._radius,
                        #
                        self.right,
                        self.y + self._radius,
                        self.right,
                        self.top - self._radius,
                        #
                        self.right,
                        self.top - self._radius,
                        self.right - self._radius,
                        self.top,
                        #
                        self.right - self._radius,
                        self.top,
                        self.x + self._radius,
                        self.top,
                        #
                        self.x + self._radius,
                        self.top,
                        self.x,
                        self.top - self._radius,
                        #
                        self.x,
                        self.top - self._radius,
                        self.x,
                        self.y + self._radius,
                        #
                        self.x,
                        self.y + self._radius,
                        self.x + self._radius,
                        self.y,
                    ]
                    self.__bg_instruction.vertices = self.__bg_coords[0]
            else:
                self.__bg_group_instructions.clear()
            pass

    def _update_bg_color(self, instance, value):
        if self._is_filled:
            # set a new color if it doesnt ave one
            if not self.__bg_cl_instruction:
                self.__bg_cl_instruction = Color(
                    *self._current_button_color,
                    # group="shaped_background_behaivor"
                )
                self.canvas.add(self.__bg_cl_instruction)
                if not self.__bg_instruction:
                    self.on_corner_type(self, self.corner_type)
            else:
                self.__bg_cl_instruction.rgba = self._current_button_color

    def on_corner_type(self, instance, value):
        if self._is_filled and self.__bg_group_instructions and value:
            if not self.__bg_cl_instruction:
                self._update_bg_color(1, 2)
            if self.corner_type == "Square":
                self.__bg_instruction = Rectangle(
                    pos=self.pos,
                    size=self.size,
                    # group="shaped_background_behaivor",
                )
                self.__bg_group_instructions.clear()
                self.__bg_group_instructions.add(self.__bg_cl_instruction)
                self.__bg_group_instructions.add(self.__bg_instruction)
            elif self.corner_type == "Rounded":
                self.__bg_instruction = RoundedRectangle(
                    size=self.size,
                    pos=self.pos,
                    radius=[self._radius],
                    # group="shaped_background_behaivor",
                )
                self.__bg_group_instructions.clear()
                self.__bg_group_instructions.add(self.__bg_cl_instruction)
                self.__bg_group_instructions.add(self.__bg_instruction)
            elif self.corner_type == "Bevel":
                self.__bg_coords = [
                    [
                        self.x + self._radius,
                        self.y,
                        self.right - self._radius,
                        self.y,
                        #
                        self.right - self._radius,
                        self.y,
                        self.right,
                        self.y + self._radius,
                        #
                        self.right,
                        self.y + self._radius,
                        self.right,
                        self.top - self._radius,
                        #
                        self.right,
                        self.top - self._radius,
                        self.right - self._radius,
                        self.top,
                        #
                        self.right - self._radius,
                        self.top,
                        self.x + self._radius,
                        self.top,
                        #
                        self.x + self._radius,
                        self.top,
                        self.x,
                        self.top - self._radius,
                        #
                        self.x,
                        self.top - self._radius,
                        self.x,
                        self.y + self._radius,
                        #
                        self.x,
                        self.y + self._radius,
                        self.x + self._radius,
                        self.y,
                    ],
                ]
                self.__bg_coords = self.__bg_coords + [[x for x in range(8)]]
                self.__bg_instruction = Mesh(
                    vertices=self.__bg_coords[0],
                    indices=self.__bg_coords[1],
                    mode="triangle_fan",
                    # group="shaped_background_behaivor",
                )
                self.__bg_group_instructions.clear()
                self.__bg_group_instructions.add(self.__bg_cl_instruction)
                self.__bg_group_instructions.add(self.__bg_instruction)

    def lay_canvas_instructions(self, *dt):
        with self.canvas.after:
            # start the stencil
            StencilPush()
            # all this instrucitons will be used as mask
            if self.corner_type == "Square":
                Rectangle(
                    pos=self.pos,
                    size=self.size,
                )
            elif self.corner_type == "Rounded":
                RoundedRectangle(
                    size=self.size, pos=self.pos, radius=[self._radius]
                )
            elif self.corner_type == "Bevel":
                Mesh(
                    vertices=[
                        self.x + self._radius,
                        self.y,
                        self.right - self._radius,
                        self.y,
                        #
                        self.right - self._radius,
                        self.y,
                        self.right,
                        self.y + self._radius,
                        #
                        self.right,
                        self.y + self._radius,
                        self.right,
                        self.top - self._radius,
                        #
                        self.right,
                        self.top - self._radius,
                        self.right - self._radius,
                        self.top,
                        #
                        self.right - self._radius,
                        self.top,
                        self.x + self._radius,
                        self.top,
                        #
                        self.x + self._radius,
                        self.top,
                        self.x,
                        self.top - self._radius,
                        #
                        self.x,
                        self.top - self._radius,
                        self.x,
                        self.y + self._radius,
                        #
                        self.x,
                        self.y + self._radius,
                        self.x + self._radius,
                        self.y,
                    ],
                    indices=[x for x in range(8)],
                    mode="triangle_fan",
                )
            # elements that will be clipped
            StencilUse()
            self.col_instruction = Color(rgba=self.ripple_color)
            self.ellipse = Ellipse(
                size=(self._ripple_rad, self._ripple_rad),
                pos=(
                    self.ripple_pos[0] - self._ripple_rad / 2.0,
                    self.ripple_pos[1] - self._ripple_rad / 2.0,
                ),
            )
            # elements that wont be necesary any more
            StencilUnUse()
            if self.corner_type == "Square":
                Rectangle(
                    pos=self.pos,
                    size=self.size,
                )
            elif self.corner_type == "Rounded":
                RoundedRectangle(
                    size=self.size, pos=self.pos, radius=[self._radius]
                )
            elif self.corner_type == "Bevel":
                Mesh(
                    vertices=[
                        self.x + self._radius,
                        self.y,
                        self.right - self._radius,
                        self.y,
                        #
                        self.right - self._radius,
                        self.y,
                        self.right,
                        self.y + self._radius,
                        #
                        self.right,
                        self.y + self._radius,
                        self.right,
                        self.top - self._radius,
                        #
                        self.right,
                        self.top - self._radius,
                        self.right - self._radius,
                        self.top,
                        #
                        self.right - self._radius,
                        self.top,
                        self.x + self._radius,
                        self.top,
                        #
                        self.x + self._radius,
                        self.top,
                        self.x,
                        self.top - self._radius,
                        #
                        self.x,
                        self.top - self._radius,
                        self.x,
                        self.y + self._radius,
                        #
                        self.x,
                        self.y + self._radius,
                        self.x + self._radius,
                        self.y,
                    ],
                    indices=[x for x in range(8)],
                    mode="triangle_fan",
                )
            # unload the stencil
            StencilPop()
        # this is binded somehow
        self.bind(ripple_color=self._set_color, _ripple_rad=self._set_ellipse)


class BaseOutlineButton(shaped_background_behaivor):
    __outline_canvas = ObjectProperty()
    __outline_instructions = ListProperty(None, allownone=True)
    __outline_coords = ListProperty(None, allownone=True)
    __current_line_group = StringProperty()
    __line_color = ObjectProperty()

    """
    This property indicates how the outline corners must be drawn.

    available options are:
    `"Square"`, `"Rounded"`, `"Bevel"`
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__outline_canvas = InstructionGroup()
        self.__line_color = Color(0, 0, 0, 1)
        self.bind(
            _current_line_color=lambda x, y: setattr(
                self.__line_color, "rgba", y
            )
            if self._has_line is True
            else None
        )
        # self.bind(pos=self._update_shape_coords)
        # self.bind(size=self._update_shape_coords)

    def __after_init__(self, *dt):
        if self._has_line is None:
            self._has_line = True
        super().__after_init__(*dt)
        if self._has_line:
            if self.line_color is None:
                if self._has_text is True:
                    self.theme_line_color = "Text"
                    # self._current_line_color = self._current_text_color
                elif self._has_icon is True:
                    self.theme_line_color = "Icon"
                    # self._current_line_color = self._current_icon_color
                else:
                    self.theme_line_color = "Primary_color"
        self.on_theme_line_color(self, self.theme_text_color)
        self.on_corner_type(self, self.corner_type)
        self.canvas.before.add(self.__outline_canvas)

    def _update_shape_coords(self, *dt):
        if self.corner_type is not None:
            super()._update_shape_coords(*dt)
            if self._has_line is True and self.__outline_coords not in (
                None,
                [],
            ):
                if self.corner_type == "Square":
                    self.__outline_coords = self.pos + self.size
                    self.__outline_instructions[
                        0
                    ].rectangle = self.__outline_coords

                elif self.corner_type == "Rounded":
                    self.__outline_coords = [
                        (
                            # Straight Lines
                            (  # Bottom
                                self.x + self._radius,
                                self.y,
                                self.right - self._radius,
                                self.y,
                            ),
                            (  # Right
                                self.right,
                                self.y + self._radius,
                                self.right,
                                self.top - self._radius,
                            ),
                            (  # Top
                                self.right - self._radius,
                                self.top,
                                self.x + self._radius,
                                self.top,
                            ),
                            (  # Left
                                self.x,
                                self.top - self._radius,
                                self.x,
                                self.y + self._radius,
                            ),
                        ),
                        # Corners
                        (
                            #   bt_lf
                            (
                                self.x + self._radius,
                                self.y + self._radius,
                                self._radius,
                                180,
                                270,
                            ),
                            #   bt_rt
                            (
                                self.right - self._radius,
                                self.y + self._radius,
                                self._radius,
                                180,
                                90,
                            ),
                            #   top_rt
                            (
                                self.right - self._radius,
                                self.top - self._radius,
                                self._radius,
                                0,
                                90,
                            ),
                            #   top_lf
                            (
                                self.x + self._radius,
                                self.top - self._radius,
                                self._radius,
                                270,
                                360,
                            ),
                        ),
                    ]
                    for i in range(4):
                        self.__outline_instructions[0][
                            i
                        ].points = self.__outline_coords[0][i]
                        self.__outline_instructions[1][
                            i
                        ].circle = self.__outline_coords[1][i]

                elif self.corner_type == "Bevel":
                    self.__outline_coords = [
                        self.x + self._radius,
                        self.y,
                        self.right - self._radius,
                        self.y,
                        self.right,
                        self.y + self._radius,
                        self.right,
                        self.top - self._radius,
                        self.right - self._radius,
                        self.top,
                        self.x + self._radius,
                        self.top,
                        self.x,
                        self.top - self._radius,
                        self.x,
                        self.y + self._radius,
                        self.x + self._radius,
                        self.y,
                    ]
                    self.__outline_instructions[
                        0
                    ].points = self.__outline_coords
            else:
                self.__outline_canvas.clear()

    def on_line_width(self, instance, value):
        """
        This event changes the line width of the outline instructions
        to the property's value
        """
        if self._has_line is True and self.__outline_instructions:
            for i in self.__outline_instructions:
                if self.corner_type == "Rounded":
                    i[0].width = value
                    i[1].width = value
                    i[2].width = value
                    i[3].width = value
                else:
                    i.width = value

    def on__current_line_color(self, instance, value):
        if self._has_line is True and self.__outline_coords not in (None, []):
            self.__line_color.rgba = self._current_line_color

    def on_corner_type(self, instance, value):
        super().on_corner_type(instance, value)

        if self._has_line is True:
            if self.__current_line_group:
                # self.canvas.remove_group(self.__current_line_group)
                self.__current_line_group = ""
                self.__outline_coords = None
                self.__outline_instructions = None
        # Onlu redraws if the widget must have outline
        if self._has_line is True:
            # if theres no Color instruciton in the property.
            self.__outline_canvas.clear()
            if not self.__line_color:
                self.__line_color = Color(*self._current_line_color)
            self.__line_color.rgba = self._current_line_color
            # Detects and draws the type.
            if self.corner_type == "Square":
                self.__current_line_group = "Square"
                self.__outline_coords = self.pos + self.size
                self.__outline_instructions = [
                    Line(
                        width=self.line_width,
                        group=self.__current_line_group,
                        rectangle=self.__outline_coords,
                    )
                ]
                self.__line_color.group = self.__current_line_group
                self.__outline_canvas.clear()
                self.__outline_canvas.add(self.__line_color)
                self.__outline_canvas.add(self.__outline_instructions[0])

            elif self.corner_type == "Rounded":
                self.__current_line_group = "Rounded"
                self.__outline_coords = [
                    (
                        # Straight Lines
                        (  # Bottom
                            self.x + self._radius,
                            self.y,
                            self.right - self._radius,
                            self.y,
                        ),
                        (  # Right
                            self.right,
                            self.y + self._radius,
                            self.right,
                            self.top - self._radius,
                        ),
                        (  # Top
                            self.right - self._radius,
                            self.top,
                            self.x + self._radius,
                            self.top,
                        ),
                        (  # Left
                            self.x,
                            self.top - self._radius,
                            self.x,
                            self.y + self._radius,
                        ),
                    ),
                    # Corners
                    (
                        #   bt_lf
                        (
                            self.x + self._radius,
                            self.y + self._radius,
                            self._radius,
                            180,
                            270,
                        ),
                        #   bt_rt
                        (
                            self.right - self._radius,
                            self.y + self._radius,
                            self._radius,
                            180,
                            90,
                        ),
                        #   top_rt
                        (
                            self.right - self._radius,
                            self.top - self._radius,
                            self._radius,
                            0,
                            90,
                        ),
                        #   top_lf
                        (
                            self.x + self._radius,
                            self.top - self._radius,
                            self._radius,
                            270,
                            360,
                        ),
                    ),
                ]
                self.__outline_instructions = [
                    (
                        Line(
                            width=self.line_width,
                            points=self.__outline_coords[0][0],
                        ),
                        Line(
                            width=self.line_width,
                            points=self.__outline_coords[0][1],
                        ),
                        Line(
                            width=self.line_width,
                            points=self.__outline_coords[0][2],
                        ),
                        Line(
                            width=self.line_width,
                            points=self.__outline_coords[0][3],
                        ),
                    ),
                    # Corners
                    (
                        Line(
                            width=self.line_width,
                            circle=self.__outline_coords[1][0],
                        ),
                        Line(
                            width=self.line_width,
                            circle=self.__outline_coords[1][1],
                        ),
                        Line(
                            width=self.line_width,
                            circle=self.__outline_coords[1][2],
                        ),
                        Line(
                            width=self.line_width,
                            circle=self.__outline_coords[1][3],
                        ),
                    ),
                ]
                self.__line_color.group = self.__current_line_group
                self.__outline_canvas.clear()
                self.__outline_canvas.add(self.__line_color)
                for i in self.__outline_instructions[0]:
                    self.__outline_canvas.add(i)
                for i in self.__outline_instructions[1]:
                    self.__outline_canvas.add(i)

            elif self.corner_type == "Bevel":
                self.__current_line_group = "Bevel"
                self.__outline_coords = [
                    self.x + self._radius,
                    self.y,
                    self.right - self._radius,
                    self.y,
                    self.right,
                    self.y + self._radius,
                    self.right,
                    self.top - self._radius,
                    self.right - self._radius,
                    self.top,
                    self.x + self._radius,
                    self.top,
                    self.x,
                    self.top - self._radius,
                    self.x,
                    self.y + self._radius,
                    self.x + self._radius,
                    self.y,
                ]
                self.__outline_instructions = [
                    Line(
                        width=self.line_width,
                        group=self.__current_line_group,
                        points=self.__outline_coords,
                    ),
                ]
                self.__line_color.group = self.__current_line_group
                self.__outline_canvas.add(self.__line_color)
                self.__outline_canvas.add(self.__outline_instructions[0])
            #

    def on_disabled(self, instance, value):
        if self.disabled:
            self.line_width = dp(0.001)
        else:
            self.line_width = dp(1)
        super().on_disabled(instance, value)


# ------------------------------------------------------------------------------
# BasePressedButton
# ------------------------------------------------------------------------------
#


class BasePressedButton(BaseButton):
    """
    Abstract base class for those button which fade to a background color on
    press.
    """

    _fade_bg = ObjectProperty(None)

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
            # Button dimming animation.
            if self.md_bg_color[-1] == [0.0]:
                self._fade_bg = Animation(
                    duration=0.5, _current_button_color=self._md_bg_color_down
                )
                self._fade_bg.start(self)
            return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self and self._fade_bg:
            self._fade_bg.stop_property(self, "_current_button_color")
            Animation(
                duration=0.05, _current_button_color=self.md_bg_color
            ).start(self)
        return super().on_touch_up(touch)


# ------------------------------------------------------------------------------
# BaseFlatButton
# ------------------------------------------------------------------------------
#

Builder.load_string(
    """
<BaseFlatButton>:
""",
    filename="MDBaseFlatButton.kv",
)
#


class BaseFlatButton(BaseButton):
    """
    Abstract base class for flat buttons which do not elevate from material.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# ------------------------------------------------------------------------------
# BaseRaisedButton
# ------------------------------------------------------------------------------
#

# Builder.load_string(
#     """
# <BaseRaisedButton>:
# """,
#     filename="MDBaseRaisedButton.kv",
# )
# #


class BaseRaisedButton(CommonElevationBehavior, BaseButton):
    """
    Abstract base class for raised buttons which elevate from material.
    Raised buttons are to be used sparingly to emphasise primary/important
    actions.

    Implements elevation behavior as well as the recommended down/disabled
    colors for raised buttons.
    """

    _elevation_normal = NumericProperty(0)
    _elevation_raised = NumericProperty(0)
    _anim_raised = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._is_filled = True

    # def __after_init__(self,*dt):
    #     super().__after_init__(*dt)

    def on_elevation(self, instance, value):
        super().on_elevation(instance, value)
        self._elevation_normal = self.elevation
        self._elevation_raised = self.elevation
        self._anim_raised = Animation(_elevation=value + 2, d=0.2)
        self._anim_raised.bind(on_progress=self._do_anim_raised)

    def on_disabled(self, instance, value):
        if value is True:
            self._elevation = 0
            self._update_shadow(instance, 0)
        else:
            self._update_shadow(instance, self.elevation)
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
                return super().on_touch_up(touch)
            Animation.cancel_all(self, "_elevation")
            self._elevation = self._elevation_raised
            self._elevation_normal = self._elevation_raised
            self._update_shadow(self, self._elevation)
        return super().on_touch_up(touch)

    def _do_anim_raised(self, animation, instance, value):
        self._elevation += value
        if self._elevation < self._elevation_raised + 2:
            self._update_shadow(instance, self._elevation)


# ------------------------------------------------------------------------------
# BaseRectangularButton
# ------------------------------------------------------------------------------
#


Builder.load_string(
    """
<BaseRectangularButton>:
    # lbl_txt: lbl_txt.__self__
    container: container.__self__
    # padding: (dp(8), 0)  # For MDRectangleFlatIconButton
    width: (container.width + dp((32 if self._has_line or self._is_filled else 16) if len(container.children) == 1 else (28 if self._is_filled or self._has_line else 22) ) ) if len(container.children) > 0 else dp(64)
    height: root.internal_padding + sp(root._current_font_size)
    # canvas.before:
    #     Color:
    #         rgb:[0.780, 0, 0.447]
    #     Rectangle:
    #         pos:self.pos
    #         size:self.size
    BoxLayout:
        size_hint: None, None
        size: self.minimum_width, self.minimum_height
        width: self.minimum_width
        id: container
        spacing: root.spacing
        # canvas.before:
        #     Color:
        #         rgb:[0.545, 0.780, 0]
        #     Rectangle:
        #         pos:self.pos
        #         size:self.size
        #     Color:
        #         rgb:1,0,0
        #     Rectangle:
        #         pos:self.pos
        #         size:5,5
        #     Rectangle:
        #         pos:self.pos
        #         size:-5,-5
        #     Color:
        #         rgb:1,0,1,1
        #     Rectangle:
        #         pos:self.right,self.top
        #         size:5,5
        #     Rectangle:
        #         pos:self.right,self.top
        #         size:-5,-5
        on_children:
            root.Update_Container_size()
    """,
    filename="MDBaseRectangularButton.kv",
)


class BaseRectangularButton(RectangularRippleBehavior, BaseButton):
    """
    Abstract base class for all rectangular buttons, bringing in the
    appropriate on-touch behavior.

    It also maintains the correct minimum width as stated in guidelines.

    """

    spacing = NumericProperty(8)
    internal_padding = NumericProperty("23dp")
    width = BoundedNumericProperty(
        88, min=88, max=None, errorhandler=lambda x: 88
    )
    __bg_instruction = ObjectProperty(None)

    lbl_txt = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *args):
        if self._has_text is None:
            self._has_text = True
        if self._has_text is True:
            self.show_label = True
        if self.text_color:
            self.theme_text_color = "Custom"
        else:
            self.theme_text_color = "Primary"
            # self.on_text_color(self,self.text_color)
        super().__after_init__(*args)
        self.container = self.ids.container
        self.container.bind(children=self.Update_Container_size)
        self.theme_text_color = "Custom" if self.text_color else "Primary_color"

    def on__current_font_size(self, instance, value):
        pass
        # super().on__current_font_size(instance, value)
        if self.lbl_txt:
            self.lbl_txt.font_size = value
            self.lbl_txt.text_size = (None, value)
            self.lbl_txt.height = value

    def on_theme_text_color(self, instance, value):
        super().on_theme_text_color(instance, value)
        if self.lbl_txt and self.opposite_colors:
            self.lbl_txt.opposite_colors = self.opposite_colors

    def on__has_text(self, instance, value):
        if value is True:
            if not self.lbl_txt:
                self.lbl_txt = MDLabel(
                    text=self.text if self.show_label else "",
                    font_size=self._current_font_size,
                    theme_text_color=self._current_theme_text_color,
                    # opposite_colors=self.opposite_colors,
                    text_color=self._current_text_color,
                    valign="middle",
                    markup=self._current_markup,
                    disabled=self.disabled,
                    size_hint_x=None,
                    size_hint_y=None,
                    text_size=(None, self._current_font_size),
                    height=self._current_font_size,
                )
                # ################################################################
                # # TODO REMOVE THIS TEST
                # ################################################################
                # with self.lbl_txt.canvas.before:
                #     Color(0, 0.780, 0.564, 1)
                #     # cl=Color(0, 0.780, 0.564,.5)
                #     rt = Rectangle(pos=self.lbl_txt.pos, size=self.lbl_txt.size)
                #     self.lbl_txt.bind(pos=lambda x, y: setattr(rt, "pos", y))
                #     self.lbl_txt.bind(size=lambda x, y: setattr(rt, "size", y))
                # ################################################################
                self.bind(
                    text=lambda x, y: setattr(self.lbl_txt, "text", y),
                    opposite_colors=lambda x, y: setattr(
                        self.lbl_txt, "opposite_colors", y
                    ),
                    _current_text_color=lambda x, y: setattr(
                        self.lbl_txt, "text_color", y
                    ),
                    _current_theme_text_color=lambda x, y: setattr(
                        self.lbl_txt, "theme_text_color", y
                    ),
                    _current_markup=lambda x, y: setattr(
                        self.lbl_txt, "markup", y
                    ),
                    disabled=lambda x, y: setattr(self.lbl_txt, "disabled", y),
                )
                self.lbl_txt.font_name = (
                    self.font_name
                    if self.font_name
                    else self.theme_cls.font_styles["Button"][0]
                )
                self.container.add_widget(self.lbl_txt)
                self.lbl_txt.bind(texture_size=self.Update_Container_size)
        else:
            if self.lbl_txt:
                self.lbl_txt.unbind(texture_size=self.Update_Container_size)
                self.unbind(
                    text=lambda x, y: setattr(self.lbl_txt, "text", y),
                    opposite_colors=lambda x, y: setattr(
                        self.lbl_txt, "opposite_colors", y
                    ),
                    _current_text_color=lambda x, y: setattr(
                        self.lbl_txt, "text_color", y
                    ),
                    _current_theme_text_color=lambda x, y: setattr(
                        self.lbl_txt, "theme_text_color", y
                    ),
                    _current_markup=lambda x, y: setattr(
                        self.lbl_txt, "markup", y
                    ),
                    disabled=lambda x, y: setattr(self.lbl_txt, "disabled", y),
                )
                self.container.remove_widget(self.lbl_txt)

    def Update_Container_size(self, *dt):
        if self.show_label and self.lbl_txt and self._has_text:
            self.lbl_txt.height = self._current_font_size
            self.lbl_txt.width = self.lbl_txt.texture_size[0]
            self.lbl_txt.text_size = [None, self._current_font_size]
            if self._has_icon is True:
                self.lbl_txt.height = self.container.height
        pass
        if hasattr(self, "icon_position"):
            if self.icon_position == "icon_only":
                self.size = [
                    self._current_font_size * 2,
                    self._current_font_size * 2,
                ]
                return
        else:
            self.container.width = self.container.minimum_width

    def on_disabled(self, instance, value):
        if self.lbl_txt is not None:
            # self.lbl_txt.disabled = True - self.disabled
            self.lbl_txt.disabled = self.disabled
            self._current_markup = False if value is True else self.markup
        super().on_disabled(instance, value)

    def on_markup(self, instance, value):
        self._current_markup = value


class icon_behavior(BaseRectangularButton):
    """
    This class defines all the icon button related behavior. it allows almost
    any button to draw an icon inside
    """

    __icon = ObjectProperty()
    icon_rotation = NumericProperty(0)
    __icon_mode = OptionProperty(None, options=["icon", "image", "error"])
    _current_icon_font_size = NumericProperty(0)
    source = StringProperty(None, allownone=False)
    next_icon = ObjectProperty(None, allownone=True)

    def zoom_in_animation(self, next_icon=None):
        if self.__icon:
            self.__icon.zoom_in_animation(
                next_icon=next_icon,
                callback=lambda *x: setattr(self, "icon", self.__icon.icon),
            )

    def on_next_icon(self, instenca, value):
        if self.__icon:
            self.__icon.next_icon = value

    def on_source(self, instenca, value):
        self.icon = value

    def __after_init__(self, *dt):
        super().__after_init__(*dt)
        #
        if self._has_icon is None:
            self._has_icon = True
        #
        if self.theme_icon_color is None:
            if self._has_text:
                self.theme_icon_color = "Text"
            else:
                self.theme_icon_color = "Primary"
        #
        if not self.icon_position:
            if isinstance(self, (MDIconButton, MDFloatingActionButton)):
                self.icon_position = "icon_only"
            else:
                self.icon_position = "left"
        #
        if not self.font_size:
            if isinstance(self, (MDIconButton, MDFloatingActionButton)):
                self._current_font_size = sp(24)
            else:
                self._current_font_size = sp(14)
        # self.bind(_current_font_size = self.Update_Container_size)
        self.on__has_icon(self, self._has_icon)
        self.on_icon(self, self.icon)
        self.on_icon_position(self, self.icon_position)
        self.on_theme_icon_color(self, self.theme_icon_color)
        self.Update_Container_size()

    def on_theme_icon_color(self, instance, value):
        if self.__icon:
            self.__icon.on_theme_text_color(self, self.__icon.theme_text_color)
        super().on_theme_icon_color(instance, value)

    def on_icon(self, instance, value):
        if self._has_icon and self.container and self.__icon:
            if value:
                if value in md_icons:
                    self.__icon_mode = "icon"
                    self.__icon.icon = self.icon
                elif Path(self.icon).resolve().exists():
                    self.__icon.icon = self.icon
                    self.__icon_mode = "image"
                else:
                    self.__icon_mode = "error"
                self.__icon.width = self.__icon.texture_size[0]
                self.__icon.height = self.__icon.texture_size[1]
                self.on_icon_position(self, self.icon_position)
            if (
                self.__icon in self.container.children
                and self.__icon_mode == "error"
            ):
                Logger.error(f"Invalid Icon {self.icon} at {self}")
                self.container.remove_widget(self.__icon)
        super().on_icon(instance, value)

    def on_icon_position(self, instance, value):
        if self.__icon and self.container:
            if self.__icon.parent:
                self.__icon.parent.remove_widget(self.__icon)
            #
            if self.lbl_txt:
                if self.lbl_txt.parent:
                    self.lbl_txt.parent.remove_widget(self.lbl_txt)
            #
            if self.icon_position == "left":
                self.container.add_widget(self.__icon)
                if self._has_text is True:
                    self.container.add_widget(self.lbl_txt)
            elif self.icon_position == "right":
                if self._has_text is True:
                    self.container.add_widget(self.lbl_txt)
                self.container.add_widget(self.__icon)
            elif self.icon_position == "icon_only":
                self.container.add_widget(self.__icon)
            else:
                self.container.remove_widget(self.__icon)
            self.Update_Container_size(self.__icon.texture_size)

    def on__has_icon(self, instance, value):
        if value is True:
            if not self.__icon:
                self.__icon = MDIcon(
                    icon=self.icon,
                    theme_text_color=self._current_theme_icon_color,
                    font_size=(
                        round(self._current_font_size * 1.28)
                        if self._has_text is True
                        else self._current_font_size
                    ),
                    text_color=self._current_icon_color,
                    size_hint=[None, None],
                    halign="center",
                    valign="middle",
                    disabled=self.disabled,
                    static_size=False,
                )
                # ################################################################
                # # TODO REMOVE THIS TEST
                # ################################################################
                # with self.__icon.canvas.before:
                #     Color(0, 0.780, 0.564, 1)
                #     # cl=Color(0, 0.780, 0.564,.5)
                #     rt = Rectangle(pos=self.__icon.pos, size=self.__icon.size)
                #     # binding block, unbind when it's not necesary !!!
                #     self.__icon.bind(pos=lambda x, y: setattr(rt, "pos", y))
                #     self.__icon.bind(size=lambda x, y: setattr(rt, "size", y))
                # ################################################################
                self.bind(
                    opposite_colors=lambda x, y: setattr(
                        self.__icon, "opposite_colors", y
                    ),
                    _current_icon_color=lambda x, y: setattr(
                        self.__icon, "text_color", y
                    ),
                    _current_theme_icon_color=lambda x, y: setattr(
                        self.__icon, "theme_text_color", y
                    ),
                    disabled=lambda x, y: setattr(self.__icon, "disabled", y),
                )
                self.__icon.bind(
                    size=self.Update_Container_size,
                    # texture_size = self.Update_Container_size,
                    texture_size=lambda *x: self.Update_Container_size()
                    if self.__icon.static_size is not True
                    else "",
                )
            self.on_icon(self, self.icon)
            self.on_icon_position(self, self.icon_position)
            self.on_theme_icon_color(self, self.theme_icon_color)
            self.Update_Container_size()
        else:
            self._current_icon_color[-1] = 0
            if self.__icon:
                self.unbind(
                    opposite_colors=lambda x, y: setattr(
                        self.__icon, "opposite_colors", y
                    ),
                    _current_icon_color=lambda x, y: setattr(
                        self.__icon, "text_color", y
                    ),
                    _current_theme_icon_color=lambda x, y: setattr(
                        self.__icon, "theme_text_color", y
                    ),
                    disabled=lambda x, y: setattr(self.__icon, "disabled", y),
                )
                self.__icon.unbind(
                    size=self.Update_Container_size,
                    # texture_size = self.Update_Container_size,
                    texture_size=lambda *x: self.Update_Container_size()
                    if self.__icon.static_size is not True
                    else "",
                )
                self.__icon.next_icon = None  # removes any link that avoids gc
                self.container.remove_widget(self.__icon)

    def get_icon_prop(self, prop):
        if self.__icon:
            return getattr(self.__icon, prop)

    def Update_Container_size(self, *dt):
        self.on__current_font_size(self, self._current_font_size)
        if self.__icon and self._has_icon:
            if self.__icon.static_size is not True:
                self.__icon.size = [self.__icon.font_size] * 2
            else:
                self.__icon.size = self.__icon.size
            # self.__icon.size = [self.__icon.font_size] * 2

        super().Update_Container_size(*dt)

    def on_icon_rotation(self, instance, degree):
        if self.__icon and self._has_icon is True:
            self.__icon.rotation = degree

    def rot_90(self, clockwise=True):
        if self.__icon:
            if clockwise is True:
                self.__icon.animate_rotation(
                    -90 if self.__icon.rotation == 0 else 0
                )
            else:
                self.__icon.animate_rotation(
                    90 if self.__icon.rotation == 0 else 0
                )

    def on__current_font_size(self, instance, value):
        super().on__current_font_size(instance, value)
        if self.__icon and value:
            if not isinstance(self, (MDIconButton,)):
                self.__icon.font_size = round(1.285 * value)
            else:
                self.__icon.font_size = value

    def on_disabled(self, instance, value):
        if self.__icon is not None:
            # self.__icon.disabled = True - self.disabled
            # self.__icon.disabled = self.disabled
            self.__icon.on_disabled(self, self.__icon.disabled)
        super().on_disabled(instance, value)


# ------------------------------------------------------------------------------
# BaseRoundButton
# ------------------------------------------------------------------------------


class BaseRoundButton(
    CircularRippleBehavior,
    icon_behavior,
    BaseOutlineButton,
):
    """
    Abstract base class for all round buttons, bringing in the appropriate
    on-touch behavior
    """

    spacing = NumericProperty(dp(4))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self._is_filled = True

    def __after_init__(self, *args):
        if self.corner_type is None:
            self.corner_type = "Rounded"
        super().__after_init__(*args)
        # self.container = self.ids.container

    def on_width(self, instance, value):
        self.height = value
        self.radius = self.height // 2

    def on_height(self, instance, value):
        self.width = value
        self.radius = self.height // 2

    def on_size(self, instance, value):
        # super().on_size(instance, value)
        if self.size[0] < dp(24):
            self.size[0] = dp(24)
        if self.size[1] < dp(24):
            self.size[1] = dp(24)


# ------------------------------------------------------------------------------
# MDIconButton
# ------------------------------------------------------------------------------
#


class MDIconButton(BaseRoundButton, BaseFlatButton, BasePressedButton):
    # icon = StringProperty("checkbox-blank-circle")
    """
    Button icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle'`.
    """

    def __after_init__(self, *kwargs):
        if self._has_icon is None:
            self._has_icon = True
        #
        if self._has_text is None:
            self._has_text = False
        #
        if self._has_line is None:
            self._has_line = False
        #
        if self._is_filled is None:
            self._is_filled = False
        #
        if self.text_color is not None:
            self.icon_color = self.text_color
            self.theme_icon_color = "Custom"

        if self.icon_color is None:
            self.theme_icon_color = "Primary"
        else:
            self.theme_icon_color = "Custom"
        #
        super().__after_init__(*kwargs)

    def on_text_color(self, instance, value):
        self.icon_color = self.text_color
        self.theme_icon_color = "Custom"
        f"TEST TEXTCOLOR: {self} \n\ttext_color = {self.text_color}"


# ------------------------------------------------------------------------------
# MDFlatButton
# ------------------------------------------------------------------------------
#


class MDFlatButton(
    BaseRectangularButton,
    BaseFlatButton,
    BasePressedButton,
):
    test = OptionProperty(0, options=[1, 2, 3])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.show_label = True

    def __after_init__(self, *kwargs):
        if self._has_text is None:
            self._has_text = True
        if self._is_filled is None:
            self._is_filled = False
        super().__after_init__(*kwargs)


# ------------------------------------------------------------------------------
# MDRectangleFlatButton
# ------------------------------------------------------------------------------


class MDRectangleFlatButton(BaseOutlineButton, MDFlatButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *args):
        if self.corner_type is None:
            self.corner_type = "Square"
        super().__after_init__(*args)


# ------------------------------------------------------------------------------
# MDRectangleFlatIconButton
# ------------------------------------------------------------------------------


class MDRectangleFlatIconButton(MDRectangleFlatButton, icon_behavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *args):
        super().__after_init__(*args)
        # self.theme_button_color = "Primary" if self.theme_button_color is None else "Custom"


# ------------------------------------------------------------------------------
# MDRoundFlatButton
# ------------------------------------------------------------------------------


class MDRoundFlatButton(MDRectangleFlatButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *dt):
        if self.corner_type is None:
            self.corner_type = "Rounded"
        super().__after_init__(*dt)


# ------------------------------------------------------------------------------
# MDRoundFlatIconButton
# ------------------------------------------------------------------------------


class MDRoundFlatIconButton(MDRoundFlatButton, icon_behavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *dt):
        super().__after_init__(*dt)


# ------------------------------------------------------------------------------
# MDBevelFlatButton
# ------------------------------------------------------------------------------


class MDBevelFlatButton(MDRectangleFlatButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *dt):
        if self.corner_type is None:
            self.corner_type = "Bevel"
        super().__after_init__(*dt)


# ------------------------------------------------------------------------------
# MDBevelFlatIconButton
# ------------------------------------------------------------------------------


class MDBevelFlatIconButton(MDRoundFlatButton, icon_behavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *dt):
        super().__after_init__(*dt)


# ------------------------------------------------------------------------------
# MDRaisedButton
# ------------------------------------------------------------------------------
#

Builder.load_string(
    """
<MDRaisedButton>:
    """,
    filename="MDRaisedButton.kv",
)


class MDRaisedButton(
    BaseRectangularButton,
    RectangularElevationBehavior,
    BaseRaisedButton,
    BasePressedButton,
    BaseOutlineButton,
):
    """
    The MDRaisedButton has a behavior similar to :class:`~MDFlatButton` With
    the difference that you can set a background color and a elevation.

    bases: :class:`~BaseRectangularButton`,
    :class:`~RectangularElevationBehavior`,
    :class:`~BaseRaisedButton`,
    :class:`~BasePressedButton`
    """

    def __after_init__(self, *args):
        # self.text_color=[1]*4
        self.opposite_colors = False
        if self.show_label is None:
            self.show_label = True
        if self._has_line is None:
            self._has_line = False
        self.corner_type = "Square"
        if self.theme_text_color is None:
            self.theme_text_color = "White"
            self.text_color = self._current_text_color
        self._has_text = True

        super().__after_init__(*args)


# ------------------------------------------------------------------------------
# MDFloatingActionButton
# ------------------------------------------------------------------------------
#

Builder.load_string(
    """
<MDFloatingActionButton>
    # Defaults to 56-by-56 and a background of the accent color according to
    # guidelines
    # size: (dp(56), dp(56))
    theme_text_color: 'Custom'
    """,
    filename="MDFloatingActionButton.kv",
)


class MDFloatingActionButton(MDIconButton, CircularElevationBehavior):
    """
    MDFloatingActionButton is a circular button with CircularElevationBehavior
    and CircularRippleBehavior. this allows you to place the button anywhere
    over the layout.

    Check the examples for better usage advice.
    bases: `MDIconButton`, `CircularElevationBehavior`
    """

    action_mode = OptionProperty(None, options=["regular", "mini FAB"])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self._is_filled = True
        self.internal_padding = "32dp"

    def on_action_mode(self, instance, value):
        if value:
            if value == "regular":
                self.internal_padding = dp(32)
            else:
                self.internal_padding = dp(8)

    def shadow_preset(self, *dt):
        if self.elevation is None:
            self.elevation = 10
        super().shadow_preset(*dt)

    def __after_init__(self, *args):
        if self._is_filled is None:
            self._is_filled = True
        if self.md_bg_color != [None] * 4:
            self.theme_button_color = "Custom"
        if self.action_mode is None:
            self.action_mode = "regular"
        if self.theme_button_color is None:
            self.theme_button_color = "Accent"
        if self.theme_text_color is None:
            self.theme_text_color = "Primary"
        super().__after_init__(*args)

        if not self.font_size:
            self._current_font_size = dp(24)


# ------------------------------------------------------------------------------
# MDRoundImageButton
# ------------------------------------------------------------------------------
#

Builder.load_string(
    """

    """,
    filename="MDRoundImageButton.kv",
)


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


# ------------------------------------------------------------------------------
# MDTextButton
# ------------------------------------------------------------------------------
#

Builder.load_string(
    """
<MDTextButton>
    size_hint: None, None
    size: self.texture_size
    color:
        root.theme_cls.primary_color \
        if not len(root.custom_color) else root.custom_color
    background_down: f'{images_path}transparent.png'
    background_normal: f'{images_path}transparent.png'
    opacity: 1
    """,
    filename="MDTextButton.kv",
)


class MDTextButton(ThemableBehavior, Button):
    """
    This button inherits directly from kivy.uix.button.Button with the
    advantage that inherits from the ThemableBehavior meta class too.
    This allows the button to behavior in the same way as the Material Design
    Standard requires.
    """

    custom_color = ListProperty()
    """Custom user button color in ``rgba`` format.

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

    def on_disabled(self, instance, value):
        # super().on_disabled(instance,value)
        if value:
            self.disabled_color = self.theme_cls.disabled_hint_text_color
            self.background_disabled_normal = f"{images_path}transparent.png"


# ------------------------------------------------------------------------------
# MDCustomRoundIconButton
# ------------------------------------------------------------------------------
#


class MDCustomRoundIconButton(CircularRippleBehavior, ButtonBehavior, Image):
    pass


# ------------------------------------------------------------------------------
# MDFillRoundFlatButton
# ------------------------------------------------------------------------------
#


class MDFillRoundFlatButton(
    RectangularElevationBehavior,
    MDRoundFlatButton,
    BasePressedButton,
):
    """
    This kind of button doesn't support transparency in it's background
    """

    _elevation_normal = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *args):
        self._has_line = False
        self._is_filled = True
        self.corner_type = "Rounded"
        if self.theme_text_color is None:
            self.theme_text_color = "White"
            self.text_color = self._current_text_color
        self.theme_icon_color = "Text"
        self.on_theme_icon_color(self, self.theme_icon_color)
        self.on_corner_type(self, self.corner_type)
        super().__after_init__(*args)


# ------------------------------------------------------------------------------
# MDFillRoundFlatIconButton
# ------------------------------------------------------------------------------
#


class MDFillRoundFlatIconButton(MDFillRoundFlatButton, icon_behavior):
    # text_color = ListProperty((1, 1, 1, 1))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *args):
        self._is_filled = True
        self._has_text = True
        self._has_icon = True
        super().__after_init__(*args)
        self.on_theme_icon_color(self, self.theme_icon_color)

    # def _on_primary_palette(self, instance, value):
    #     super()._on_primary_palette(instance, value)
    # self._current_button_color = self.theme_cls.primary_color


# SpeedDial classes

# ------------------------------------------------------------------------------
# BaseFloatingRootButton
# ------------------------------------------------------------------------------
#

# Builder.load_string(
#     """
# <BaseFloatingRootButton>
#     theme_text_color: "Custom"
#     md_bg_color: self.theme_cls.primary_color
#
#     canvas:
#         PushMatrix
#         Rotate:
#             angle: self._angle
#             axis: (0, 0, 1)
#             origin: self.center
#         # PopMatrix
#     canvas.after:
#         PopMatrix
#     """,
#     filename="BaseFloatingRootButton.kv",
# )


class BaseFloatingRootButton(MDFloatingActionButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.elevation = 5


# ------------------------------------------------------------------------------
# BaseFloatingBottomButton
# ------------------------------------------------------------------------------
#

Builder.load_string(
    """
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
    """,
    filename="BaseFloatingBottomButton.kv",
)


class BaseFloatingBottomButton(MDFloatingActionButton, MDTooltip):
    _canvas_width = NumericProperty(0)
    _padding_right = NumericProperty(0)
    _bg_color = ListProperty()


# ------------------------------------------------------------------------------
# BaseFloatingLabel
# ------------------------------------------------------------------------------
#

Builder.load_string(
    """
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
        color: root.text_color if root.text_color else  [1]*4
    """,
    filename="BaseFloatingLabel.kv",
)


class BaseFloatingLabel(
    ThemableBehavior,
    RectangularElevationBehavior,
    BoxLayout
    #
):
    text = StringProperty()
    text_color = ListProperty()
    bg_color = ListProperty()


# ------------------------------------------------------------------------------
# MDFloatingBottomButton
# ------------------------------------------------------------------------------
#


class MDFloatingBottomButton(BaseFloatingBottomButton):
    pass


# ------------------------------------------------------------------------------
# MDFloatingRootButton
# ------------------------------------------------------------------------------
#


class MDFloatingRootButton(BaseFloatingRootButton):
    pass


# ------------------------------------------------------------------------------
# MDFloatingLabel
# ------------------------------------------------------------------------------
#


class MDFloatingLabel(BaseFloatingLabel):
    pass


# ------------------------------------------------------------------------------
# MDFloatingActionButtonSpeedDial
# ------------------------------------------------------------------------------
#


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
        # kv lang
        MDFloatingActionButtonSpeedDial:
            callback: app.callback

    .. code-block:: python
        # Python
        def callback(self, instance):
            Logger.debug(instance.icon)


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

        data = {
            'name-icon': 'Text label',
            [...],
            [...],
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
                                opacity=0, d=0.1, t=self.opening_transition
                            ).start(widget)
                        break

    def on_enter(self, instance):
        """Called when the mouse cursor is over a button from the stack."""

        if self.state == "open":
            for widget in self.children:
                if isinstance(widget, MDFloatingLabel) and self.hint_animation:
                    widget.elevation = 1
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
        for name_icon in value.keys():
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
                label.text_color = self.label_text_color
                self.add_widget(label)
        # Top root button.
        self.root_button = MDFloatingRootButton(on_release=self.open_stack)
        self.root_button.icon = self.icon
        self.set_pos_root_button(self.root_button)
        self.add_widget(self.root_button)

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
                    and self.rotation_root_button
                ):
                    # Rotates the root button 45 degrees.
                    self.root_button.rot_90(clockwise=True)

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
                self.root_button.rot_90(clockwise=True)
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
