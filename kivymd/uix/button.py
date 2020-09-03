from pathlib import Path

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Line, Mesh, Rectangle  # Color,
from kivy.graphics.context_instructions import (
    Color,
    PopMatrix,
    PushMatrix,
    Rotate,
)
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
from kivymd.uix.label import MDIcon
from kivymd.uix.tooltip import MDTooltip

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
    "MDFillRoundFlatButton",
    "MDFillRoundFlatIconButton",
    "MDTextButton",
    "MDFloatingActionButtonSpeedDial",
)


#


# import kivy.factory
#

Builder.load_string(
    """
#:import images_path kivymd.images_path
#:import md_icons kivymd.icon_definitions.md_icons
    """,
    filename="MDButtons.kv",
)


class button_background_behavior(Widget):
    r = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    """The value of ``red`` in the ``rgba`` palette.

    :attr:`r` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `1.0`.
    """

    g = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    """The value of ``green`` in the ``rgba`` palette.

    :attr:`g` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `1.0`.
    """

    b = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    """The value of ``blue`` in the ``rgba`` palette.

    :attr:`b` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `1.0`.
    """

    a = BoundedNumericProperty(0.0, min=0.0, max=1.0)
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

    text_color = ListProperty()
    """
    The color of the text in ``rgba`` format.

    :attr:`text_color` is a :class:`~kivy.properties.ListProperty`
    defaults to `[]`.
    """

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

    md_bg_color_disabled = ListProperty()
    """Color disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ListProperty`
    defaults to `[]`.
    """

    line_color = ListProperty([1.0, 1.0, 1.0, 0])
    """
    """

    line_width = NumericProperty(1)
    """
    """

    opposite_colors = BooleanProperty(False)
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
    icon_color = ListProperty([1.0, 1.0, 1.0, 0])
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

    corner_type = OptionProperty(None, options=["Square", "Rounded", "Bevel"])
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
        self.font_size = value

    # -------------------------------------------------------------------------
    # Function Definitions

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(primary_palette=self._on_primary_palette)
        Clock.schedule_once(self.__after_init__, -1)

    def __after_init__(self, *args):
        if self._is_filled is True:
            if self.theme_button_color is None:
                if self.md_bg_color == [1.0, 1.0, 1.0, 0.0]:
                    self.theme_button_color = "Primary"
                    self.md_bg_color = self.theme_cls._get_primary_color()
                else:
                    self.theme_button_color = "Custom"
        if self.md_bg_color_disabled:
            self._md_bg_color_disabled = self.md_bg_color_disabled
        else:
            self._md_bg_color_disabled = self.theme_cls.disabled_hint_text_color
        #
        self.on__is_filled(self, self._is_filled)
        self.on_disabled(self, self.disabled)
        self.on_font_size(self, self.font_size)
        self.on_theme_text_color(self, self.theme_text_color)

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
        self.on_theme_button_color(self, self.theme_button_color)
        # Verifica el color de texto
        if self._is_filled:
            if self.theme_button_color == "Primary":
                self._current_button_color = self.theme_cls._get_primary_color()
            else:
                self.on_theme_button_color(self, self.theme_button_color)

        if self._has_text:
            if self.theme_text_color == "Primary_color":
                self._current_text_color = self.theme_cls._get_primary_color()
            else:
                self.on_theme_text_color(self, self.theme_line_color)
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
            if self.theme_button_color == "Primary":
                self._current_button_color = (
                    self.theme_cls._get_primary_color()[:]
                )

            elif self.theme_button_color == "Accent":
                self._current_button_color = self.theme_cls.accent_color

            elif self.theme_button_color == "Error":
                self._current_button_color = self.theme_cls.error_color

            elif self.theme_button_color == "Custom":
                self._current_button_color = self.md_bg_color
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
                self._current_text_color = self.text_color

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

    def on_theme_icon_color(self, instance, value):
        """
        This fucntion process the color theme of the buttons's Icon.
        """
        if self._has_icon:
            theme = self.theme_cls
            if value == "Primary":
                self._current_theme_icon_color = "Primary"

            elif value == "Secondary":
                self._current_theme_icon_color = "Secondary"

            elif value == "Hint":
                self._current_theme_icon_color = "Hint"

            elif value == "Error":
                self._current_theme_icon_color = "Error"

            elif value == "ContrastParentBackground":
                self._current_theme_icon_color = "ContrastParentBackground"

            elif value == "Custom":
                self._current_theme_icon_color = "Custom"
                self._current_icon_color = self.icon_color

            elif value == "Accent_color":
                self._current_theme_icon_color = "Custom"
                self._current_icon_color = theme.accent_color

            elif value == "Primary_color":
                self._current_theme_icon_color = "Custom"
                self._current_icon_color = theme.primary_color

            elif value == "White":
                self._current_theme_icon_color = "Custom"
                self._current_icon_color = [1, 1, 1, 1]

            elif value == "Text":
                if self.lbl_txt:
                    self._current_theme_icon_color = "Custom"
                    self._current_icon_color = self.lbl_txt.color[:]
            else:
                self._current_icon_color[-1] = 0

    def on_theme_line_color(self, instance, value):
        """
        This fucntion process the color theme of the buttons's outline.

        this theme is not linked to any other configuration.
        """
        if self._has_line:
            theme = self.theme_cls
            op = not self.opposite_colors

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
                self._current_line_color = self.line_color
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
        if self._has_text is True and self.theme_text_color == "Custom":
            self._current_text_color = value
        else:
            pass

    def on_disabled(self, instance, value):
        """
        Event launched when the button's disabled property is changed.
        """
        if self.disabled is True:
            self._current_button_color = self._md_bg_color_disabled
        else:
            if self._is_filled:
                self._current_button_color = self.md_bg_color
            else:
                self._current_button_color[-1] = 0

    def on_font_size(self, instance, value):
        """
        Event launched when the button's font_size property is changed.
        """
        if value is not None:
            if value >= sp(4):
                self._current_font_size = value
            else:
                self.font_size = sp(4)


class shaped_background_behaivor(BaseButton):
    # TODO Add to base button
    __bg_instruction = ObjectProperty()
    __bg_cl_instruction = ObjectProperty()
    __bg_coords = ObjectProperty()
    __bg_group_instructions = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # if self.radius:
        #     self.radius = self.height//2 if self.radius > self.size[1]//2 else self.radius
        # else:
        #     self.radius=self.height//2
        self.__bg_group_instructions = InstructionGroup()
        self.bind(_current_button_color=self._update_bg_color)
        self.bind(_is_filled=self._update_bg_color)
        self.bind(pos=self._update_shape_coords)
        self.bind(size=self._update_shape_coords)
        Clock.schedule_once(
            lambda x: self.canvas.before.add(self.__bg_group_instructions), -1
        )

    def __after_init__(self, *dt):
        self._update_bg_color(self, self._current_button_color)
        super().__after_init__(*dt)

    def _update_shape_coords(self, *dt):
        if self.radius:
            self.radius = (
                self.height // 2
                if self.radius > self.size[1] // 2
                else self.radius
            )
        else:
            self.radius = self.height // 2
        if self._is_filled:
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
        if self._is_filled and self.__bg_group_instructions:
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

        # canvas:
        #     Color:
        #         rgba: self._current_button_color
        #     RoundedRectangle:
        #         size: self.size
        #         pos: self.pos
        #         radius: (root._radius, )

    # pass
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
        self.canvas.add(self.__outline_canvas)
        self.__line_color = Color(0, 0, 0, 1)
        # self.bind(pos=self._update_shape_coords)
        # self.bind(size=self._update_shape_coords)

    def __after_init__(self, *dt):
        super().__after_init__(*dt)
        self.on_corner_type(self, self.on_corner_type)

    def _update_shape_coords(self, *dt):
        super()._update_shape_coords(*dt)
        if self._has_line is True and self.__outline_coords not in (None, []):
            if self.corner_type == "Square":
                self.__outline_coords = self.pos + self.size
                self.__outline_instructions[0].rectangle = self.__outline_coords

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
                self.__outline_instructions[0].points = self.__outline_coords
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
            else:
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
        self._is_filled = False
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

    def on_elevation(self, instance, value):
        self._elevation_normal = self.elevation
        self._elevation_raised = self.elevation
        self._anim_raised = Animation(_elevation=value + 2, d=0.2)
        self._anim_raised.bind(on_progress=self._do_anim_raised)
        self._update_elevation(instance, value)

    def on_disabled(self, instance, value):
        if value is True:
            self._elevation = 0
            self._update_shadow(instance, 0)
        else:
            self._update_elevation(instance, self._elevation_normal)
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
<BaseRectangularButton>
    lbl_txt: lbl_txt.__self__
    container: container.__self__
    # padding: (dp(8), 0)  # For MDRectangleFlatIconButton
    width: container.width + dp(24)
    height: dp(22) + sp(root._current_font_size )
    # canvas:
    #     Color:
    #         rgba:[0.6, 0.55, 0.45, 1]
    #     Rectangle:
    #         pos:self.pos
    #         size:self.size
    BoxLayout:
        size_hint:None, None
        # size: self.minimum_width, self.minimum_height
        width: self.minimum_width
        id: container
        spacing: root.spacing
        # canvas.before:
        #     Color:
        #         rgb:.42, .67, .55
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
            self.width = self.minimum_width
            self.height = self.minimum_height
        MDLabel:
            id: lbl_txt
            text: root.text if root.show_label else ''
            font_size : sp(root._current_font_size )
            font_name: root.font_name if root.font_name else self.font_name
            size_hint_x: None
            text_size: (None, dp(22) + sp(root._current_font_size ))
            height: self.texture_size[1]
            theme_text_color: root._current_theme_text_color
            text_color: root._current_text_color
            markup: root.markup
            valign: 'middle'
            disabled: root.disabled
            opposite_colors: root.opposite_colors
            on_texture_size:
                root._update_width()
            # canvas.before:
            #     Color:
            #         rgb:.5, .5, .6
            #     Rectangle:
            #         pos:self.pos
            #         size:self.size
    """,
    filename="MDBaseRectangularButton.kv",
)


class BaseRectangularButton(RectangularRippleBehavior, BaseButton):
    """
    Abstract base class for all rectangular buttons, bringing in the
    appropriate on-touch behavior.

    It also maintains the correct minimum width as stated in guidelines.

    """

    spacing = NumericProperty(4)
    # spacing = BoundedNumericProperty(
    #     4, min=0, max=None, errorhandler=lambda x: 4
    # )
    width = BoundedNumericProperty(
        88, min=88, max=None, errorhandler=lambda x: 88
    )
    __bg_instruction = ObjectProperty(None)

    lbl_txt = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *args):
        if self.text_color:
            self.theme_text_color = "Custom"
        super().__after_init__(*args)
        self.lbl_txt = self.ids.lbl_txt
        self.container = self.ids.container
        self.lbl_txt.bind(texture_size=self._update_width)
        self.on_theme_text_color(self, self.theme_text_color)
        self.theme_text_color = "Custom" if self.text_color else "Primary_color"
        self._update_width()
        # Logger.debug(f"TEST: AFTER_INIT IN BaseRectangularButton ::  self : {self}")
        # Logger.debug(f"TEST: AFTER_INIT IN BaseRectangularButton ::  text_color : {self.text_color}")

    def _update_width(self, *dt):
        for i in self.container.children:
            if hasattr(i, "texture_size"):
                i.text_size = None, self.height
                i.width = i.texture_size[0]
                i.height = self.container.height
        if hasattr(self, "icon_position"):
            if self.icon_position == "icon_only":
                if not self.font_size:
                    self.size = [dp(48), dp(48)]
                else:
                    self.size = [
                        self.font_size + dp(24),
                        self.font_size + dp(24),
                    ]
                return
        # self.container.width = self.container.minimum_width
        self.container.height = self.height
        Logger.debug(
            f"TEST: TEXT={self.text}\n"
            f"\tChildren == self.container in [{type(self)}]::{self.children[0] is self.container}\n"
            f"\tchildren:\t{self.children[0]}; size:{self.children[0].size} \n"
            f"\tcontainer:\t{self.container}; size:{self.container.size}\n"
            f"\tself size:\t{self.size}\n"
            "\n"
        )

    # _height = NumericProperty(0)


class icon_behavior(BaseRectangularButton):
    icon_position = OptionProperty(None, options=["left", "right", "icon_only"])
    __icon = ObjectProperty()
    __Icon_instruction = ObjectProperty(None)
    __icon_cl_bg = ObjectProperty()
    __icon_cl_bg_l = ListProperty()
    __icon_bg = ObjectProperty()
    __icon_source = StringProperty()
    __had_fill = BooleanProperty()
    icon_rotation = NumericProperty()
    __current_rotation = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._has_icon = True
        # self._is_filled = True
        if not self.theme_icon_color:
            self.theme_icon_color = "Text"
        if not self.icon_position:
            if isinstance(self, MDIconButton):
                self.icon_position = "icon_only"
            else:
                self.icon_position = "left"
        if not self.font_size:
            self.font_size = (
                "12sp"
                if not isinstance(self, MDFloatingActionButton)
                else "32sp"
            )
        self.__icon_source = ""
        self.bind(_current_icon_color=self._update_icon)
        self.bind(_current_font_size=self._update_icon)
        self.bind(pos=self.update_icon_canvas_coords)
        self.__Icon_instruction = InstructionGroup()
        self.bind(size=self.update_icon_canvas_coords)
        Clock.schedule_once(
            lambda x: self.canvas.add(self.__Icon_instruction), -1
        )
        # self.bind(_current_text_color=self._update_icon)

    def update_icon_canvas_coords(self, *dt):
        if self.__icon_bg and Path(self.icon).resolve().exists():
            self.__icon_bg.pos = (
                self.pos
                if self.icon_position == "icon_only"
                else self.__icon.pos
            )
            self.__icon_bg.size = [self.height, self.height]

    def update_icon_canvas(self, *dt):
        if self.__icon and self.__Icon_instruction and self.icon:
            # self.unbind(pos=self.update_icon_canvas, size=self.update_icon_canvas)
            if Path(self.icon).resolve().exists():
                if not self.__icon_bg:
                    self.__icon_bg = Rectangle(
                        pos=self.pos,
                        size=[self.height, self.height],
                        soruce=self.icon,
                    )
                else:
                    if self.__icon_bg.source == self.icon:
                        return
                    self.__icon_bg.pos = (
                        self.pos
                        if self.icon_position == "icon_only"
                        else self.__icon.pos
                    )
                    self.__icon_bg.size = [self.height, self.height]
                    self.__icon_bg.source = self.icon
                #
                if not self.__icon_cl_bg:
                    self.__icon_cl_bg_l = (
                        [1, 0, 0, 1] if self.disabled is False else [0.1] * 4
                    )
                    self.__icon_cl_bg = Color(self.__icon_cl_bg_l)
                    # self.__icon_cl_bg = Color([1]*4)
                else:
                    self.__icon_cl_bg_l = (
                        [1, 0, 0, 1] if self.disabled is False else [0.1] * 4
                    )
                    pass
                #
                self.__icon.size = [self.height, self.height]
                self.__Icon_instruction.clear()
                self.__Icon_instruction.add(self.__icon_cl_bg)
                self.__Icon_instruction.add(self.__icon_bg)
            else:
                self.__Icon_instruction.clear()
            # self.bind(pos=self.update_icon_canvas, size=self.update_icon_canvas)

    def __after_init__(self, *dt):
        super().__after_init__(*dt)
        self._update_icon(self, 1)
        self.on_icon(self, self.on_icon)
        # self.update_icon_canvas()
        self.on_icon_position(self, self.icon_position)
        Clock.schedule_once(self.update_icon_canvas, -1)

    def on_icon(self, instance, value):
        if self._has_icon and self.container:
            icon_error = 0
            if not self.__icon:
                self.__icon = MDIcon(
                    icon="" if not self.icon else self.icon,
                    theme_text_color=self._current_theme_icon_color,
                    font_size=self._current_font_size,
                    text_color=self._current_icon_color,
                    size_hint=[None, None],
                    halign="center",
                    valign="middle",
                    disabled=self.disabled,
                )
                self.__icon.bind(texture_size=self._update_width)
                self.bind(font_size=self._update_icon)
            if self.icon:
                if self.icon in md_icons:
                    self.__icon.icon = self.icon
                elif Path(self.icon).resolve().exists():
                    self.__icon.icon = ""
                    Clock.schedule_once(self.update_icon_canvas, -1)
                else:
                    icon_error = True
                self.__icon.width = self.__icon.texture_size[0]
                self.__icon.height = self.__icon.texture_size[1]
                self.on_icon_position(self, self.icon_position)

            if self.__icon in self.container.children and icon_error is True:
                Logger.error(f"Invalid Icon {self.icon} at {self}")
                self.container.remove_widget(self.__icon)

    def _update_icon(self, instance, value):
        if self.__icon:
            self.__icon.text_color = self._current_icon_color
            self.__icon.theme_text_color = self._current_theme_icon_color
            if self._has_text:
                self.__icon.font_size = self._current_font_size + (
                    self._current_font_size * 0.70
                )
            else:
                self.__icon.font_size = self._current_font_size
            self.__icon.size = self.__icon.texture_size
            self.update_icon_canvas()

    def on_icon_position(self, instance, value):
        if self.__icon and self.container:
            if self.__icon.parent:
                self.__icon.parent.remove_widget(self.__icon)
            if self.lbl_txt.parent:
                self.lbl_txt.parent.remove_widget(self.lbl_txt)
            #
            if self.icon_position == "left":
                self.container.add_widget(self.__icon)
                self.container.add_widget(self.lbl_txt)
            #
            elif self.icon_position == "right":
                self.container.add_widget(self.lbl_txt)
                self.container.add_widget(self.__icon)
            #
            elif self.icon_position == "icon_only":
                self.container.add_widget(self.__icon)
            #
            else:
                self.container.remove_widget(self.__icon)
            self._update_width(self.__icon.texture_size)
            self.update_icon_canvas()
            #

    def on__has_line(self, instance, value):
        self.on_theme_line_color(self, self.theme_line_color)

    def on__has_icon(self, instance, value):
        self.on_icon(self, self.icon)
        if value is True:
            self.on_icon_position(self, self.icon_position)
            self.on_theme_icon_color(self, self.theme_icon_color)
        else:
            self._current_icon_color[-1] = 0
            if self.__icon:
                self.container.remove_widget(self.__icon)

    def on_disabled(self, instance, value):
        if (
            self.__icon_cl_bg
            and self.__Icon_instruction
            and Path(self.icon).resolve().exists()
        ):
            self.__icon_cl_bg.rgba = (
                (
                    [0.7, 0.7, 0.7, 0.8]
                    if self._is_filled is False
                    else [0.7, 0.7, 0.7, 0.6]
                )
                if value is True
                else [1] * 4
            )
        super().on_disabled(instance, value)

    def rotate_icon(self, degree, *dt):
        if self.__icon:
            if self.icon_position == "icon_only":
                with self.__icon.canvas.before:
                    PushMatrix()
                    Rotate(angle=degree, origin=self.__icon.center)
            else:
                with self.__Icon_instruction:
                    PushMatrix()
                    Rotate(angle=degree, origin=self.__icon.center)

            with self.__icon.canvas:
                PopMatrix()

    def on_icon_rotation(self, instance, value):
        val = value - self.__current_rotation
        self.rotate_icon(val)
        self.__current_rotation = value

    def rot_90(self, *dt, reverse=False):
        if self.__icon:
            self.ev = Animation(
                icon_rotation=(0 if reverse else -90),
                duration=0.125,
                t="in_quad",
            )
            self.ev.start(self)


# ------------------------------------------------------------------------------
# BaseRoundButton
# ------------------------------------------------------------------------------
#

# Builder.load_string(
#     """
# <BaseRoundButton>:
#     canvas:
#         Clear
#         Color:
#             rgba: self._current_button_color if root.icon in md_icons else (0, 0, 0, 0)
#         Ellipse:
#             size: self.size
#             pos: self.pos
#             source: self.source if hasattr(self, "source") else ""
#
#     size:
#         (dp(48), dp(48)) \
#         if not root.font_size \
#         else (dp(root.font_size + 23), dp(root.font_size + 23))
#     lbl_txt: lbl_txt
#     padding: (dp(12), dp(12), dp(12), dp(12)) if root.icon in md_icons else (0, 0, 0, 0)
#
#     MDIcon:
#         id: lbl_txt
#         icon: root.icon
#         font_size :
#             root.font_size \
#             if root.font_size \
#             else self._current_font_size
#         font_name: root.font_name if root.font_name else self.font_name
#         theme_text_color: root._current_theme_text_color
#         text_color: root._current_text_color
#         disabled: root.disabled
#         valign: 'middle'
#         halign: 'center'
#         opposite_colors: root.opposite_colors
#     """,
#     filename="MDBaseRoundButton.kv",
# )


Builder.load_string(
    """
<BaseRoundButton>
        # Todo fix the background drawing to allow a mesh instead of a
        # RoundedRectangle to complete the behavior

    # height: dp(22) + sp(root._current_font_size )
    # width: container.width + dp(24)
    # container: container.__self__
    # size:
    #     (dp(48), dp(48)) \
    #     if not root.font_size \
    #     else (dp(root.font_size + 23), dp(root.font_size + 23))
    # BoxLayout:
    #     size_hint:None, None
    #     size: self.minimum_width, self.minimum_height
    #     # size:10, 10
    #     id: container
    #     # spacing: root.spacing
    #     canvas:
    #         Color:
    #             rgb:.32, .47, .85
    #         Rectangle:
    #             pos:self.pos
    #             size:self.size
    #         Color:
    #             rgb:1,.2,.7
    #         Rectangle:
    #             pos:self.pos
    #             size:5,-5
    #         Rectangle:
    #             pos:self.pos
    #             size:-5,5
    #         Color:
    #             rgb:.51,0.5,.71
    #         Rectangle:
    #             pos:self.right,self.top
    #             size:5,-5
    #         Rectangle:
    #             pos:self.right,self.top
    #             size:-5,+5

    """,
    filename="MDBaseRoundButton.kv",
)


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

    width = BoundedNumericProperty(
        dp(24), min=dp(24), max=None, errorhandler=lambda x: dp(24)
    )
    height = BoundedNumericProperty(
        dp(24), min=dp(24), max=None, errorhandler=lambda x: dp(24)
    )

    def __init__(self, **kwargs):
        self.corner_type = "Rounded"
        self._is_filled = True
        super().__init__(**kwargs)

    def __after_init__(self, *args):
        super().__after_init__(*args)
        # self.container = self.ids.container

    def on_width(self, instance, value):
        self.height = value
        self.radius = self.height // 2

    def on_height(self, instance, value):
        self.width = value
        self.radius = self.width // 2

    def on_icon(self, *dt):
        if hasattr(self, "__icon"):
            if self.__icon.source is not None:
                self._is_filled = True
                self.__bg_instruction.source = self.__icon.source
            else:
                if isinstance(self, MDIconButton):
                    self._is_filled = False
                    self.__bg_instruction.source = None
        super().on_icon(*dt)
        pass

    # def _update_width(self, *dt):
    #     pass


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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._is_filled = False
        # self._is_filled = True


# ------------------------------------------------------------------------------
# MDFlatButton
# ------------------------------------------------------------------------------
#


class MDFlatButton(
    BaseRectangularButton,
    BaseFlatButton,
    BasePressedButton,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._has_text = True
        self.show_label = True
        self._is_filled = False

    def __after_init__(self, *kwargs):
        super().__after_init__(*kwargs)


# ------------------------------------------------------------------------------
# BaseFlatIconButton
# ------------------------------------------------------------------------------
#
# Builder.load_string(
#     """
#
#     """,
#     filename="MDBaseFlatIconButton.kv",
# )
# class BaseFlatIconButton(MDFlatButton):
# icon = StringProperty("android")
# """
# Button icon.
#
# :attr:`icon` is an :class:`~kivy.properties.StringProperty`
# and defaults to `'android'`.
# """

# text = StringProperty("")
# """Button text.
#
# :attr:`text` is an :class:`~kivy.properties.StringProperty`
# and defaults to `''`.
# """

# show_label = BooleanProperty(False)

# def __init__(self, **kwargs):
#     super().__init__(**kwargs)

# def _on_primary_palette(self, instance, value):
#     super().pansd
#     self.text_color = self.theme_cls._get_primary_color()
#     super()._on_primary_palette(instance, value)
# pass

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._has_text = True
        self.show_label = True
        self._has_line = False
        self.corner_type = "Square"

    def __after_init__(self, *args):
        if self.theme_text_color is None:
            self.theme_text_color = "White"
            self.text_color = self._current_text_color
        self.on_theme_icon_color(self, self.theme_icon_color)
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

    background_palette = StringProperty("Accent", deprecated=True)
    """
    The name of the palette used for the background color of the button.

    :attr:`background_palette` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Accent'

    This property is now deprecated and will be removed in next updates
    use theme_button_color instead`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._is_filled = True
        self.theme_button_color = "Accent"

    def __after_init__(self, *args):
        super().__after_init__(*args)

        if not self.font_size:
            self.font_size = dp(56)
            self.size = dp(56), dp(56)
        # if self.md_bg_color == [1.0, 1.0, 1.0, 0.0]:
        # self.theme_button_color = "Accent"
        # self.md_bg_color = self.theme_cls.accent_color
        # self.md_bg_color=self.theme_cls._get_primary_color()

    # def on_md_bg_color(self, instance, value):
    #     super().on_md_bg_color()
    # if value != self.theme_cls.accent_color:
    #     self._current_button_color = value


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
# MDRectangleFlatButton
# ------------------------------------------------------------------------------
#
# Builder.load_string(
#     """
# #: import _RoundedRectangle kivy.graphics.vertex_instructions.RoundedRectangle
# <MDRectangleFlatButton>:
#     canvas:
#         Color:
#             rgba: root._current_line_color
#         # Side Lines
#         Line:
#             width: root.line_width
#             rectangle: (self.x, self.y, self.width, self.height)
#
#
#
#
#     """,
#     filename="MDRectangleFlatButton.kv",
# )
class MDRectangleFlatButton(BaseOutlineButton, MDFlatButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *args):
        super().__after_init__(*args)
        self._has_line = True if self._has_line is None else self._has_line
        if self.theme_line_color is None:
            self.theme_line_color = "Text"
        if self.corner_type is None:
            self.corner_type = "Square"

    # self.on_corner_type(self,self.on_corner_type)


# ------------------------------------------------------------------------------
# MDRoundFlatButton
# ------------------------------------------------------------------------------
#
# Builder.load_string(
#     """
#
#     """,
#     filename="MDRoundFlatButton.kv",
# )
class MDRoundFlatButton(BaseOutlineButton, MDFlatButton):
    # _radius = NumericProperty("18dp")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._has_line = False if self._has_line is False else True
        if self.theme_line_color is None:
            self.theme_line_color = "Text"
        if self.corner_type is None:
            self.corner_type = "Rounded"
        # self.corner_type = "Bevel"

    # def __after_init__(self,*dt):
    #     super().__after_init__(*dt)
    #     self.on_corner_type(self,self.on_corner_type)


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
    # CircularElevationBehavior,
    # shaped_background_behaivor,
    # MDRaisedButton,
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
        self.corner_type = "Rounded"
        self._is_filled = True
        self._has_line = False

    def __after_init__(self, *args):
        if self.theme_text_color is None:
            self.theme_text_color = "White"
            self.text_color = self._current_text_color
        self.on_theme_icon_color(self, self.theme_icon_color)
        super().__after_init__(*args)
        self.on_corner_type(self, self.on_corner_type)


# ------------------------------------------------------------------------------
# MDRectangleFlatIconButton
# ------------------------------------------------------------------------------
#


class MDRectangleFlatIconButton(MDRectangleFlatButton, icon_behavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *args):
        Logger.debug(
            "TEST: __after_init__\n"
            f"  Text:\t{self.text}\n"
            f"  Type:\t{type(self)}\n"
            f"  _has_line {self._has_line}\n\n"
        )
        self.on__has_line(self, self._has_line)
        super().__after_init__(*args)


# ------------------------------------------------------------------------------
# MDRoundFlatIconButton
# ------------------------------------------------------------------------------
#


class MDRoundFlatIconButton(MDRoundFlatButton, icon_behavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # if not self.icon:
        #     self.icon = "home"
        # if self.radius is None:
        #     self.radius=self.size[1]//2


# ------------------------------------------------------------------------------
# MDFillRoundFlatIconButton
# ------------------------------------------------------------------------------
#


class MDFillRoundFlatIconButton(MDFillRoundFlatButton, icon_behavior):
    # text_color = ListProperty((1, 1, 1, 1))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __after_init__(self, *args):
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

Builder.load_string(
    """
<BaseFloatingRootButton>
    theme_text_color: "Custom"
    md_bg_color: self.theme_cls.primary_color

    canvas:
        PushMatrix
        Rotate:
            angle: self._angle
            axis: (0, 0, 1)
            origin: self.center
        # PopMatrix
    canvas.after:
        PopMatrix
    """,
    filename="BaseFloatingRootButton.kv",
)


class BaseFloatingRootButton(MDFloatingActionButton):
    _angle = NumericProperty(0)

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
                Logger.debug(
                    f"ROTATION of {widget}, parent: {widget.parent}\n"
                    f"canvas: {self.canvas.children[0].children}"
                )
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


# ------------------------------------------------------------------------------
# TEST APP WILL BE REMOVED
# ------------------------------------------------------------------------------
#

if __name__ == "__main__":
    from kivy.uix.screenmanager import Screen

    from kivymd.app import MDApp

    kv = """
Screen:
    ScrollView:
        do_scroll_y:True
        GridLayout:
            id: x
            cols: 3
            # spacing:dp(10)
            MDBoxLayout:
                # size_hint_x:None
                md_bg_color:.1,.2,.3,1
            MDBoxLayout:
                # size_hint_x:None
                md_bg_color:.1,.3,.3,1
            MDBoxLayout
                # size_hint_x:None
                md_bg_color:.4,.3,.3,1
"""

    class Custom_flat_btn(MDFlatButton):
        def __init__(self, **kwargs):
            super(Custom_flat_btn, self).__init__(**kwargs)

        pass

    class App(MDApp):
        buttons = ListProperty([])

        def build(self):
            screen = Screen()
            self.container = Builder.load_string(kv)
            screen.add_widget(self.container)
            return screen

        def on_start(self, *dt):
            self.after_build()

        def after_build(self, *dt):
            self.buttons = [
                MDFlatButton(
                    text="MDFLATBUTTON",
                    text_color=[0, 0, 1, 1],
                ),
                MDFlatButton(
                    text="MDFLATBUTTON",
                    text_color=[0, 0, 1, 1],
                ),
                MDFlatButton(
                    text="MDFLATBUTTON",
                    text_color=[0, 0, 1, 1],
                ),
            ]

            self.buttons = self.buttons + [
                MDRaisedButton(
                    text="MDRaisedButton",
                    text_color=[0, 0, 1, 1],
                    # md_bg_color=[1, 1, 0, 1],
                    # elevation=10
                ),
                MDRaisedButton(
                    text="MDRaisedButton",
                    # text_color=[0, 0, 1, 1],
                    # md_bg_color=[1, 0, 1, 1],
                    # elevation=9
                ),
                MDRaisedButton(
                    text="MDRaisedButton",
                    # text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 0, 0, 1],
                    # elevation=16
                ),
            ]
            #

            Logger.debug("MAINAPP: Adding MDRectangleFlatButton")
            self.buttons = self.buttons + [
                MDRectangleFlatButton(
                    text="MDRectangleFlatButton",
                    #
                ),
                MDRectangleFlatButton(
                    text="MDRectangleFlatButton",
                    corner_type="Bevel",
                    radius=dp(24),
                    #
                ),
                MDRectangleFlatButton(
                    text="MDRectangleFlatButton",
                    corner_type="Rounded",
                    spacing=dp(32),
                    # text_color=[0, 0, 1, 1],
                    # md_bg_color=[1, 0, 0, 1],
                ),
            ]
            #

            Logger.debug("MAINAPP: Adding MDRectangleFlatIconButton")
            self.buttons = self.buttons + [
                MDRectangleFlatIconButton(
                    text="MDRectangleFlatIconButton",
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 1, 0, 1],
                    corner_type="Square",
                    radius=dp(24),
                    # spacing=dp(8),
                ),
                MDRectangleFlatIconButton(
                    text="MDRectangleFlatIconButton",
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 0, 1, 1],
                    icon_position="right",
                    spacing=dp(16),
                    corner_type="Bevel",
                    radius=dp(24),
                ),
                MDRectangleFlatIconButton(
                    text="MDRectangleFlatIconButton",
                    radius=22,
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 0, 1, 1],
                    corner_type="Rounded",
                    spacing=dp(32),
                    # theme_line_color="Text"
                ),
            ]
            #

            Logger.debug("MAINAPP: Adding MDRoundFlatButton")
            self.buttons = self.buttons + [
                MDRoundFlatButton(
                    text="MDRoundFlatButton",
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 1, 0, 1],
                ),
                MDRoundFlatButton(
                    text="MDRoundFlatButton",
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 0, 1, 1],
                ),
                MDRoundFlatButton(
                    text="MDRoundFlatButton",
                    text_color=[0, 0, 1, 1],
                    # theme_line_color="Text"
                    # md_bg_color=[1, 0, 0, 1],
                ),
            ]
            #
            #
            Logger.debug("MAINAPP: Adding MDRoundFlatIconButton")
            self.buttons = self.buttons + [
                MDRoundFlatIconButton(
                    text="MDRoundFlatIconButton",
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 1, 0, 1],
                ),
                MDRoundFlatIconButton(
                    text="MDRoundFlatIconButton",
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 0, 1, 1],
                ),
                MDRoundFlatIconButton(
                    text="MDRoundFlatIconButton",
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 0, 0, 1],
                ),
            ]
            #

            Logger.debug("MAINAPP: Adding MDFillRoundFlatButton")
            self.buttons = self.buttons + [
                MDFillRoundFlatButton(
                    text="MDFillRoundFlatButton",
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 1, 0, 1],
                ),
                MDFillRoundFlatButton(
                    text="MDFillRoundFlatButton",
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 0, 1, 1],
                ),
                MDFillRoundFlatButton(
                    text="MDFillRoundFlatButton",
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 0, 0, 1],
                ),
            ]
            #

            Logger.debug("MAINAPP: Adding MDFillRoundFlatIconButton")
            self.buttons = self.buttons + [
                MDFillRoundFlatIconButton(
                    text="MDFillRoundFlatIconButton 1",
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 1, 0, 1],
                ),
                MDFillRoundFlatIconButton(
                    text="MDFillRoundFlatIconButton 2",
                    text_color=[0, 0, 1, 1],
                    icon_position="right",
                    md_bg_color=[1, 0, 1, 1],
                ),
                MDFillRoundFlatIconButton(
                    text="MDFillRoundFlatIconButton 3",
                    text_color=[0, 0, 1, 1],
                    md_bg_color=[1, 0, 0, 1],
                    icon="C:/Users/manue/Documents/SilverBits/IAI/training-software/source/etc/images/Login2.png",
                ),
            ]
            #

            Logger.debug("MAINAPP: Adding MDTextButton")
            self.buttons = self.buttons + [
                MDTextButton(
                    text="MDTextButton",
                    # text_color= [0, 0, 1, 1],
                    # md_bg_color=[1, 1, 0, 1],
                ),
                MDTextButton(
                    text="MDTextButton",
                    # text_color= [0, 0, 1, 1],
                    # md_bg_color=[1, 0, 1, 1],
                ),
                MDTextButton(
                    text="MDTextButton",
                    # text_color= [0, 0, 1, 1],
                    # md_bg_color=[1, 0, 0, 1],
                ),
            ]
            #
            Logger.debug("MAINAPP: Adding MDIconButton")
            self.buttons = self.buttons + [
                MDIconButton(
                    icon="android",
                    font_size="14sp",
                ),
                MDIconButton(
                    icon="home",
                    font_size="34sp",
                ),
                MDIconButton(
                    icon="C:/Users/manue/Documents/SilverBits/IAI/training-software/source/etc/images/Login.png",
                    font_size="4sp",
                    text_color=self.theme_cls.primary_color,
                ),
            ]
            #

            Logger.debug("MAINAPP: Adding MDFloatingActionButton")
            self.buttons = self.buttons + [
                MDFloatingActionButton(
                    icon="android",
                    md_bg_color=app.theme_cls.primary_color,
                ),
                # MDFloatingActionButtonSpeedDial(
                #     data={
                #         "language-python": "Python",
                #         "language-php": "PHP",
                #         "language-cpp": "C++",
                #         "language-java": "java",
                #     },
                #     rotation_root_button=True,
                # ),
                MDFillRoundFlatIconButton(
                    text="MDFillRoundFlatIconButton",
                    md_bg_color=[1, 0, 1, 1],  # not work
                    elevation=10,
                ),
                MDFillRoundFlatIconButton(
                    text="MDFillRoundFlatIconButton",
                    md_bg_color=[1, 0, 1, 1],  # not work
                    elevation=10,
                ),
                # MDFillRoundFlatIconButton(
                #     text="MDFillRoundFlatIconButton",
                #     md_bg_color=[1, 0, 1, 1],  # not work
                #     elevation= 16
                # ),
            ]
            # XAX=MDFillRoundFlatIconButton(
            #     text="ВВВВВВВВВ",
            #     md_bg_color=[1, 0, 0, 1],  # not work
            #     pos=[150,200],
            # )
            # XAX.bind(on_release=lambda *x: print(dir(XAX)))
            # self.root.add_widget(
            #     XAX,
            # )
            # Logger.debug(f"MAINAPP: self.buttons is {self.buttons}")

            for i in self.buttons:
                self.container.ids.x.add_widget(i)
            # Logger.debug("MAINAPP: Changing bindimgs to on_release events")
            for i in self.buttons[::3]:
                i.on_release = self.change_theme_color3
            for i in self.buttons[1::3]:
                i.on_release = self.change_to_custom
            for i in self.buttons[2::3]:
                i.on_release = self.fake_disable

        def change_theme_color3(self, *dt):
            self.theme_cls.primary_palette = (
                "Teal"
                if self.theme_cls.primary_palette == "Blue"
                else (
                    "Blue"
                    if self.theme_cls.primary_palette == "Orange"
                    else (
                        "Orange"
                        if self.theme_cls.primary_palette == "Green"
                        else (
                            "Green"
                            if self.theme_cls.primary_palette == "Red"
                            else (
                                "Red"
                                if self.theme_cls.primary_palette == "Teal"
                                else ("Teal")
                            )
                        )
                    )
                )
            )
            Logger.debug("")
            Logger.debug(
                f"change_theme_color3: Setting up primary palete to {self.theme_cls.primary_palette}\n{'_'*80}\n"
            )
            # for i in self.root.children[0].children:
            #     Logger.debug(f"{i}:{i._current_button_color}")

        tema = "Custom"
        theme_text_color = "Primary"

        def change_to_custom(self):
            self.tema = "Custom" if self.tema == "Primary" else "Primary"
            self.theme_text_color = (
                "Primary"
                if self.theme_text_color == "Secondary"
                else (
                    "Secondary"
                    if self.theme_text_color == "Hint"
                    else (
                        "Hint"
                        if self.theme_text_color == "Error"
                        else (
                            "Error"
                            if self.theme_text_color == "Custom"
                            else (
                                "Custom"
                                if self.theme_text_color == "Primary_color"
                                else (
                                    "Primary_color"
                                    if self.theme_text_color == "Accent_color"
                                    else (
                                        "Accent_color"
                                        if self.theme_text_color == "Primary"
                                        else ("Primary")
                                    )
                                )
                            )
                        )
                    )
                )
            )

            # Logger.debug(f"Cambiando a tema = {self.tema}")
            Logger.debug(
                f"Cambiando theme_text_color = {self.theme_text_color}"
            )
            for i in self.container.ids.x.children[::3]:
                if hasattr(i, "theme_button_color"):
                    i.theme_button_color = self.tema
                    i.theme_text_color = self.theme_text_color
                    i.theme_line_color = (
                        "Text" if i.theme_line_color == "Custom" else "Custom"
                    )
                    i.corner_type = ["Square", "Rounded", "Bevel"][
                        self.le_counter
                    ]
                    try:
                        i.icon_rotation = i.icon_rotation + 10
                        i.text = f"spacing:{i.spacing};tema_btn:{self.tema} ; tema_text:{self.theme_text_color} ; tema_line:{i.theme_line_color}: corner_type:{i.corner_type}"
                        i.icon = (
                            "home"
                            if self.le_counter % 3 == 0
                            else (
                                "android"
                                if self.le_counter % 3 == 1
                                else "C:/Users/manue/Documents/SilverBits/IAI/training-software/source/etc/images/Login.png"
                            )
                        )
                        # if isinstance(i, MDIconButton):
                        # i.font_size = i.font_size + 4
                    except Exception as e:
                        Logger.debug(f"TEXT: EXCEPTION : {e}")
                        pass
            self.le_counter = self.le_counter + 1
            Logger.debug("-" * 80)
            pass

        le_counter = BoundedNumericProperty(
            0, min=0, max=2, errorhandler=lambda x: 0
        )

        def fake_disable(self, *dt):
            Clock.schedule_once(self.lockunlock)
            Clock.schedule_once(self.lockunlock, 3)
            pass

        def lockunlock(self, *dt):
            self.root.disabled = True if self.root.disabled is False else False

    app = App()
    app.run()
# from kivy.lang import Builder

# from kivymd.app import MDApp
