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

.. Note:: `See full example <https://github.com/HeaTTheatR/KivyMD/wiki/Components-Button>`_
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
)

from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.stencil_instructions import (
    StencilPush,
    StencilUse,
    StencilPop,
    StencilUnUse,
)
from kivy.graphics.vertex_instructions import Ellipse, RoundedRectangle
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.properties import (
    StringProperty,
    BoundedNumericProperty,
    ListProperty,
    AliasProperty,
    BooleanProperty,
    NumericProperty,
    OptionProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation

from kivymd.uix.behaviors.backgroundcolorbehavior import (
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    RectangularRippleBehavior,
)
from kivymd.uix.behaviors import (
    CommonElevationBehavior,
    RectangularElevationBehavior,
    CircularElevationBehavior,
)
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
#:import Animation kivy.animation.Animation
#:import md_icons kivymd.icon_definitions.md_icons
#:import colors kivymd.color_definitions.colors
#:import images_path kivymd.images_path


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
            rgba: self._current_button_color
        Ellipse:
            size: self.size
            pos: self.pos
            source: self.source if hasattr(self, "source") else ""

    size:
        (dp(48), dp(48)) \
        if not root.user_font_size \
        else (dp(root.user_font_size + 23), dp(root.user_font_size + 23))
    lbl_txt: lbl_txt
    padding: dp(12)
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
