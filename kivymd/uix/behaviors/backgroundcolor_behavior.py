"""
Behaviors/Background Color
==========================

.. note:: The following classes are intended for in-house use of the library.
"""

__all__ = ("BackgroundColorBehavior", "SpecificBackgroundColorBehavior")

from typing import List, NoReturn

from kivy.lang import Builder
from kivy.properties import (
    BoundedNumericProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
    ReferenceListProperty,
    StringProperty,
    VariableListProperty,
    ObjectProperty
)
from kivy.utils import get_color_from_hex
from kivy.graphics.instructions import CanvasBase
from kivymd.color_definitions import hue, palette, text_colors
from kivymd.theming import ThemeManager

from .elevation import CommonElevationBehavior

Builder.load_string(
    """
#:import RelativeLayout kivy.uix.relativelayout.RelativeLayout


# <BackgroundColorBehavior>


<RoundedRectangularColorBehavior>:
    _md_bg_color: md_bg_color
    PushMatrix
    Rotate:
        angle: self.angle
        origin: self._background_origin

    Color:
        rgba: self._md_bg_color
    RoundedRectangle:
        group: "Background_instruction"
        size: self.size
        pos: self.pos if not isinstance(self, RelativeLayout) else (0, 0)
        radius: root.radius
        source: root.background

    Color:
        rgba: self.line_color if self.line_color else (0, 0, 0, 0)
    Line:
        rounded_rectangle:
            [ \
            self.x, \
            self.y, \
            self.width, \
            self.height, \
            *self.radius, \
            100, \
            ]

    PopMatrix


<RectangularColorBehavior>:
    canvas.before:
        PushMatrix
        Rotate:
            angle: self.angle
            origin: self._background_origin

        Color:
            rgba: self._md_bg_color
        Rectangle:
            group: "Background_instruction"
            size: self.size
            pos: self.pos if not isinstance(self, RelativeLayout) else (0, 0)
            source: root.background

        Color:
            rgba: self.line_color if self.line_color else (0, 0, 0, 0)
        Line:
            rectangle: [\
                self.x, self.y, \
                self.width, self.height, \
            ]

        PopMatrix


<EllipseColorBehavior>:
    canvas.before:
        PushMatrix
        Rotate:
            angle: self.angle
            origin: self._background_origin

        Color:
            rgba: self._md_bg_color
        Ellipse:
            pos: self.pos
            size: self.size
            angle_start: self.angle_start
            angle_end: self.angle_end

        Color:
            rgba: self.line_color if self.line_color else (0, 0, 0, 0)
        Line:
            ellipse: [\
                self.x, self.y, \
                self.width, self.height, \
                self.angle_start,self.angle_end, \
                100, \
            ]

        PopMatrix

""",
    filename="BackgroundColorBehavior.kv",
)


class BackgroundColorBehavior(CommonElevationBehavior):
    """
    This is a Meta class, `BackgroundColorBehavior` will manage all the color
    behavior that is shared across kivymd, here we set the memory namespaces
    and basic behavior.

    Rememebr that most MD widgets relly in this class as it manages the
    background color.

    Usually we define our canvas instructions on the new widget, you can use
    this class directly as controller and add your own instructions or you
    can use one of the pre fabricated instructions such as:
    * :class:`~RoundedRectangularColorBehavior` : Draws a RoundedRectangle.
    * :class:`~RectangularColorBehavior`: Draws a Rectangle.
    * :class:`~EllipseColorBehavior`: Draws an Ellipse.

    Rememebr that all this pre fabricated classes work directly under the
    canvas.before canvas layer.

    """
    background = StringProperty()
    """
    Background image path.

    :attr:`background` is a :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
    """

    r = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    """
    The value of ``red`` in the ``rgba`` palette.

    :attr:`r` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `1.0`.
    """

    g = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    """
    The value of ``green`` in the ``rgba`` palette.

    :attr:`g` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `1.0`.
    """

    b = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    """
    The value of ``blue`` in the ``rgba`` palette.

    :attr:`b` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `1.0`.
    """

    a = BoundedNumericProperty(0.0, min=0.0, max=1.0)
    """
    The value of ``alpha channel`` in the ``rgba`` palette.

    :attr:`a` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `0.0`.
    """

    radius = VariableListProperty([0], length=4)
    """
    Canvas radius.

    .. code-block:: python

        # Top left corner slice.
        MDBoxLayout:
            md_bg_color: app.theme_cls.primary_color
            radius: [25, 0, 0, 0]

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    _md_bg_color = ReferenceListProperty(r, g, b, a)
    """
    Current color of the widget.

    This color will reflect directly on the canvas instruction that is bound to.

    You can change this color and turn back to :attr:`md_bg_color` anytime.

    This has been done this way to allow developers to easely manage the current
    color and the "default" color.
    """

    md_bg_color = ColorProperty(None)
    """
    The background color of the widget (:class:`~kivy.uix.widget.Widget`)
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

        <MyWidget@RectangularColorBehavior>
            md_bg_color: 0, 1, 1, 1

    use any of the following behaviors that already have canvas instructions:
    * :class:`~RoundedRectangularColorBehavior`
    * :class:`~RectangularColorBehavior`
    * :class:`~EllipseColorBehavior`

    :attr:`md_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to :attr:`r`, :attr:`g`, :attr:`b`, :attr:`a`.
    """

    md_bg_color_disabled = ColorProperty(None)


    line_color = ColorProperty([0, 0, 0, 0])
    """
    If a custom value is specified for the `line_color parameter`, the border
    of the specified color will be used to border the widget:

    .. code-block:: kv

        MDBoxLayout:
            size_hint: .5, .2
            md_bg_color: 0, 1, 1, .5
            line_color: 0, 0, 1, 1
            radius: [24, ]

    .. versionadded:: 0.104.2

    :attr:`line_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    angle = NumericProperty(0)
    background_origin = ListProperty(None)

    _background_x = NumericProperty(0)
    _background_y = NumericProperty(0)
    _background_origin = ReferenceListProperty(
        _background_x,
        _background_y,
    )

    def __init__(self, **kwarg):
        super().__init__(**kwarg)
        self.bind(pos=self.update_background_origin)
        self.bind(md_bg_color=self.update_bg_color)

    def update_bg_color(self, instance, value: list) -> NoReturn:
        """
        This method updates the background color in a standard way.
        rememebr _md_bg_color is the current background color.
        while the md_bg_color is the Normal state of the background.
        this is done to help developers to design icons that have different
        states easier, rather than cleaning up or making a widget from 0.

        Overwrite this method to extend the functionallity.

        rememrber to keep the on_disabled method active as it will keep the
        disbaled status of the widget.
        """
        if self.disabled is True:
            self.on_disabled(self, self.disabled)
            return

        if self.md_bg_color:
            self._md_bg_color = self.md_bg_color

    def update_background_origin(
        self, instance_md_widget, pos: List[float]
    ) -> NoReturn:
        if self.background_origin:
            self._background_origin = self.background_origin
        else:
            self._background_origin = self.center

    def on_disabled(self, instance, value: bool) -> NoReturn:
        if value is False:
            self.update_bg_color(self, self.md_bg_color)
            return
        if self.md_bg_color_disabled:
            self._md_bg_color = self.md_bg_color_disabled


class SpecificBackgroundColorBehavior(BackgroundColorBehavior):
    background_palette = OptionProperty(
        "Primary", options=["Primary", "Accent", *palette]
    )
    """
    See :attr:`kivymd.color_definitions.palette`.

    :attr:`background_palette` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    background_hue = OptionProperty("500", options=hue)
    """
    See :attr:`kivymd.color_definitions.hue`.

    :attr:`background_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'500'`.
    """

    specific_text_color = ColorProperty([0, 0, 0, 0.87])
    """
    :attr:`specific_text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.87]`.
    """

    specific_secondary_text_color = ColorProperty([0, 0, 0, 0.87])
    """
    :attr:`specific_secondary_text_color`is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.87]`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if hasattr(self, "theme_cls"):
            self.theme_cls.bind(
                primary_palette=self._update_specific_text_color
            )
            self.theme_cls.bind(accent_palette=self._update_specific_text_color)
            self.theme_cls.bind(theme_style=self._update_specific_text_color)
        self.bind(background_hue=self._update_specific_text_color)
        self.bind(background_palette=self._update_specific_text_color)
        self._update_specific_text_color(None, None)

    def _update_specific_text_color(
        self, instance_theme_manager: ThemeManager, theme_style: str
    ) -> NoReturn:
        if hasattr(self, "theme_cls"):
            palette = {
                "Primary": self.theme_cls.primary_palette,
                "Accent": self.theme_cls.accent_palette,
            }.get(self.background_palette, self.background_palette)
        else:
            palette = {"Primary": "Blue", "Accent": "Amber"}.get(
                self.background_palette, self.background_palette
            )
        color = get_color_from_hex(text_colors[palette][self.background_hue])
        secondary_color = color[:]
        # Check for black text (need to adjust opacity).
        if (color[0] + color[1] + color[2]) == 0:
            color[3] = 0.87
            secondary_color[3] = 0.54
        else:
            secondary_color[3] = 0.7
        self.specific_text_color = color
        self.specific_secondary_text_color = secondary_color


class RoundedRectangularColorBehavior(BackgroundColorBehavior):
    pass


class RectangularColorBehavior(BackgroundColorBehavior):
    pass


class EllipseColorBehavior(BackgroundColorBehavior):
    angle_start: int = NumericProperty(0)
    angle_end: int = NumericProperty(360)
    pass
