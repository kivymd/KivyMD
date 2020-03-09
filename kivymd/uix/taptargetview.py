"""
.. seealso::

    `TapTargetView, GitHub <https://github.com/KeepSafe/TapTargetView>`_

    `TapTargetView, Material archive https://material.io/archive/guidelines/growth-communications/feature-discovery.html#>`_

.. rubric:: Attempt to mimic the working of Android's TapTargetView using Kivy and Python..
"""

from kivy.animation import Animation
from kivy.metrics import dp
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.event import EventDispatcher
from kivy.properties import (
    ObjectProperty,
    NumericProperty,
    ListProperty,
    StringProperty,
    BooleanProperty,
    OptionProperty,
)
from kivy.uix.label import Label


class MDTapTargetView(EventDispatcher):
    """Rough try to mimic the working of Android's TapTargetView."""

    widget = ObjectProperty()
    """
    Widget to add ``TapTargetView`` upon.

    :attr:`widget` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    outer_radius = NumericProperty(dp(300))
    """
    Radius for outer circle.

    :attr:`outer_radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(300)`.
    """

    outer_circle_color = ListProperty([1, 0, 0])
    """
    Color for the outer circle.

    :attr:`outer_circle_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[1, 0, 0]`.
    """

    outer_circle_alpha = NumericProperty(0.96)
    """
    Alpha value for outer circle.

    :attr:`outer_circle_alpha` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.96`.
    """

    target_radius = NumericProperty(dp(45))
    """
    Radius for target circle.

    :attr:`target_radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(45)`.
    """

    target_circle_color = ListProperty([1, 1, 1])
    """
    Color for target circle.

    :attr:`target_circle_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[1, 1, 1]`.
    """

    title_text = StringProperty()
    """
    Title to be shown on the view.

    :attr:`title_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    title_text_size = NumericProperty(dp(25))
    """
    Text size for title.

    :attr:`title_text_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(25)`.
    """

    title_text_color = ListProperty([1, 1, 1, 1])
    """
    Text color for title.

    :attr:`title_text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[1, 1, 1, 1]`.
    """

    title_text_bold = BooleanProperty(True)
    """
    Whether title should be bold.

    :attr:`title_text_bold` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    description_text = StringProperty()
    """
    Description to be shown below the title (keep it short).

    :attr:`description_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    description_text_size = NumericProperty(dp(20))
    """
    Text size for description text.

    :attr:`description_text_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(20)`.
    """

    description_text_color = ListProperty([0.9, 0.9, 0.9, 1])
    """
    Text size for description text.

    :attr:`description_text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0.9, 0.9, 0.9, 1]`.
    """

    description_text_bold = BooleanProperty(False)
    """
    Whether description should be bold.

    :attr:`description_text_bold` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    draw_shadow = BooleanProperty(False)
    """
    Whether to show shadow.

    :attr:`draw_shadow` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    cancelable = BooleanProperty(False)
    """
    Whether clicking outside the outer circle dismisses the view.

    :attr:`cancelable` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    widget_position = OptionProperty(
        "left",
        options=[
            "left",
            "right",
            "top",
            "bottom",
            "left_top",
            "right_top",
            "left_bottom",
            "right_bottom",
            "center",
        ],
    )
    """
    Sets the position of the widget on the outer_circle. Available options are
    `'left`', `'right`', `'top`', `'bottom`', `'left_top`', `'right_top`',
    `'left_bottom`', `'right_bottom`', `'center`'.

    :attr:`widget_position` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'left'`.
    """

    title_position = OptionProperty(
        "auto",
        options=[
            "auto",
            "left",
            "right",
            "top",
            "bottom",
            "left_top",
            "right_top",
            "left_bottom",
            "right_bottom",
        ],
    )
    """
    Sets the position of :attr`~title_text` on the outer circle. Only works if
    :attr`~widget_position` is set to `'center'`. In all other cases, it
    calculates the :attr`~title_position` itself.
    Must be set to other than `'auto`' when :attr`~widget_position` is set
    to `'center`'.
    Available options are `'auto'`, `'left`', `'right`', `'top`', `'bottom`',
    `'left_top`', `'right_top`', `'left_bottom`', `'right_bottom`', `'center`'.

    :attr:`title_position` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'auto'`.
    """

    stop_on_outer_touch = BooleanProperty(False)
    """
    Whether clicking on outer circle stops the animation.

    :attr:`stop_on_outer_touch` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    stop_on_target_touch = BooleanProperty(True)
    """
    Whether clicking on target circle should stop the animation.

    :attr:`stop_on_target_touch` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    end = ObjectProperty()
    """
    Function to be called when the animation stops.

    :attr:`end` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        self.ripple_max_dist = dp(90)
        self.outer_radius *= 2
        self.target_radius *= 2

        self.core_title_text = Label(
            markup=True, size_hint=(None, None), bold=self.title_text_bold
        )
        self.core_title_text.bind(texture_size=self.core_title_text.setter("size"))
        self.core_description_text = Label(markup=True, size_hint=(None, None))
        self.core_description_text.bind(
            texture_size=self.core_description_text.setter("size")
        )

        super().__init__(**kwargs)
        self.register_event_type("on_outer_touch")
        self.register_event_type("on_target_touch")
        self.register_event_type("on_outside_click")

    def _initialize(self):
        setattr(self.widget, "outer_radius", 0)
        setattr(self.widget, "target_radius", 0)
        setattr(self.widget, "target_ripple_radius", 0)
        setattr(self.widget, "target_ripple_alpha", 0)

        # Bind some function on widget event when this function is called
        # instead of when the class itself is initialized to prevent all
        # widgets of all instances to get bind at once and start messing up.
        self.widget.bind(on_touch_down=self._some_func)

    def _draw_canvas(self):
        _pos = self._ttv_pos()
        self.widget.canvas.before.clear()

        with self.widget.canvas.before:
            # Outer circle.
            Color(*self.outer_circle_color, self.outer_circle_alpha, group="ttv_group")
            _rad1 = self.widget.outer_radius
            Ellipse(size=(_rad1, _rad1), pos=_pos[0], group="ttv_group")

            # Title text.
            Color(*self.title_text_color, group="ttv_group")
            Rectangle(
                size=self.core_title_text.texture.size,
                texture=self.core_title_text.texture,
                pos=_pos[1],
                group="ttv_group",
            )

            # Description text.
            Color(*self.description_text_color, group="ttv_group")
            Rectangle(
                size=self.core_description_text.texture.size,
                texture=self.core_description_text.texture,
                pos=(_pos[1][0], _pos[1][1] - self.core_description_text.size[1] - 5),
                group="ttv_group",
            )

            # Target circle.
            Color(*self.target_circle_color, group="ttv_group")
            _rad2 = self.widget.target_radius
            Ellipse(
                size=(_rad2, _rad2),
                pos=(
                    self.widget.x - (_rad2 / 2 - self.widget.size[0] / 2),
                    self.widget.y - (_rad2 / 2 - self.widget.size[0] / 2),
                ),
                group="ttv_group",
            )

            # Target ripple.
            Color(
                *self.target_circle_color,
                self.widget.target_ripple_alpha,
                group="ttv_group",
            )
            _rad3 = self.widget.target_ripple_radius
            Ellipse(
                size=(_rad3, _rad3),
                pos=(
                    self.widget.x - (_rad3 / 2 - self.widget.size[0] / 2),
                    self.widget.y - (_rad3 / 2 - self.widget.size[0] / 2),
                ),
                group="ttv_group",
            )

    def stop(self, *args):
        # It needs a better implementation.
        self.anim_ripple.unbind(on_complete=self._repeat_ripple)
        self.description_text_color = [1, 1, 1, 0]
        self.title_text_color = [1, 1, 1, 0]
        anim = Animation(
            d=0.15,
            t="in_cubic",
            **dict(
                zip(
                    ["outer_radius", "target_radius", "target_ripple_radius"], [0, 0, 0]
                )
            ),
        )
        anim.bind(on_complete=self._after_stop)
        anim.start(self.widget)

    def _after_stop(self, *args):
        self.widget.canvas.before.remove_group("ttv_group")
        args[0].stop_all(self.widget)
        elev = getattr(self.widget, "elevation", None)

        if elev:
            self._fix_elev()
        if self.end:
            self.end(self)

        # Don't forget to unbind the function or it'll mess
        # up with other next bindings.
        self.widget.unbind(on_touch_down=self._some_func)

    def _fix_elev(self):
        with self.widget.canvas.before:
            Color(a=self.widget._soft_shadow_a)
            Rectangle(
                texture=self.widget._soft_shadow_texture,
                size=self.widget._soft_shadow_size,
                pos=self.widget._soft_shadow_pos,
            )
            Color(a=self.widget._hard_shadow_a)
            Rectangle(
                texture=self.widget._hard_shadow_texture,
                size=self.widget._hard_shadow_size,
                pos=self.widget._hard_shadow_pos,
            )

            Color(a=1)

    def start(self, *args):
        self._initialize()
        self._animate_outer()

    def _animate_outer(self):
        anim = Animation(
            d=0.2,
            t="out_cubic",
            **dict(
                zip(
                    ["outer_radius", "target_radius"],
                    [self.outer_radius, self.target_radius],
                )
            ),
        )
        anim.cancel_all(self.widget)
        anim.bind(on_progress=lambda x, y, z: self._draw_canvas())
        anim.bind(on_complete=self._animate_ripple)
        anim.start(self.widget)
        setattr(self.widget, "target_ripple_radius", self.target_radius)
        setattr(self.widget, "target_ripple_alpha", 1)

    def _animate_ripple(self, *args):
        self.anim_ripple = Animation(
            d=1,
            t="in_cubic",
            target_ripple_radius=self.target_radius + self.ripple_max_dist,
            target_ripple_alpha=0,
        )
        self.anim_ripple.stop_all(self.widget)
        self.anim_ripple.bind(on_progress=lambda x, y, z: self._draw_canvas())
        self.anim_ripple.bind(on_complete=self._repeat_ripple)
        self.anim_ripple.start(self.widget)

    def _repeat_ripple(self, *args):
        setattr(self.widget, "target_ripple_radius", self.target_radius)
        setattr(self.widget, "target_ripple_alpha", 1)
        self._animate_ripple()

    def on_description_text(self, instance, value):
        self.core_description_text.text = value

    def on_description_text_size(self, instance, value):
        self.core_description_text.font_size = value

    def on_description_text_bold(self, instance, value):
        self.core_description_text.bold = value

    def on_title_text(self, instance, value):
        self.core_title_text.text = value

    def on_title_text_size(self, instance, value):
        self.core_title_text.font_size = value

    def on_title_text_bold(self, instance, value):
        self.core_title_text.bold = value

    def on_target_touch(self):
        if self.stop_on_target_touch:
            self.stop()

    def on_outer_touch(self):
        if self.stop_on_outer_touch:
            self.stop()

    def on_outside_click(self):
        if self.cancelable:
            self.stop()

    def _some_func(self, wid, touch):
        """
        This function decides which one to dispatch based on the touch
        position.
        """

        if self._check_pos_target(touch.pos):
            self.dispatch("on_target_touch")
        elif self._check_pos_outer(touch.pos):
            self.dispatch("on_outer_touch")
        else:
            self.dispatch("on_outside_click")

    def _check_pos_outer(self, pos):
        """
        Checks if a given `pos` coordinate is within the :attr:`~outer_radius`.
        """

        cx = self.circ_pos[0] + self.outer_radius / 2
        cy = self.circ_pos[1] + self.outer_radius / 2
        r = self.outer_radius / 2
        h, k = pos

        lhs = (cx - h) ** 2 + (cy - k) ** 2
        rhs = r ** 2
        if lhs <= rhs:
            return True
        return False

    def _check_pos_target(self, pos):
        """
        Checks if a given `pos` coordinate is within the
        :attr:`~target_radius`.
        """

        cx = self.widget.pos[0] + self.widget.width / 2
        cy = self.widget.pos[1] + self.widget.height / 2
        r = self.target_radius / 2
        h, k = pos

        lhs = (cx - h) ** 2 + (cy - k) ** 2
        rhs = r ** 2
        if lhs <= rhs:
            return True
        return False

    def _ttv_pos(self):
        """
        Calculates the `pos` value for outer circle and text
        based on the position provided.

        :returns: A tuple containing pos for the circle and text.
        """

        _rad1 = self.widget.outer_radius
        _center_x = self.widget.x - (_rad1 / 2 - self.widget.size[0] / 2)
        _center_y = self.widget.y - (_rad1 / 2 - self.widget.size[0] / 2)

        if self.widget_position == "left":
            circ_pos = (_center_x + _rad1 / 3, _center_y)
            title_pos = (_center_x + _rad1 / 1.4, _center_y + _rad1 / 1.4)
        elif self.widget_position == "right":
            circ_pos = (_center_x - _rad1 / 3, _center_y)
            title_pos = (_center_x - _rad1 / 10, _center_y + _rad1 / 1.4)
        elif self.widget_position == "top":
            circ_pos = (_center_x, _center_y - _rad1 / 3)
            title_pos = (_center_x + _rad1 / 4, _center_y + _rad1 / 4)
        elif self.widget_position == "bottom":
            circ_pos = (_center_x, _center_y + _rad1 / 3)
            title_pos = (_center_x + _rad1 / 4, _center_y + _rad1 / 1.2)
        # Corner ones need to be at a little smaller distance
        # than edge ones that's why _rad1/4.
        elif self.widget_position == "left_top":
            circ_pos = (_center_x + _rad1 / 4, _center_y - _rad1 / 4)
            title_pos = (_center_x + _rad1 / 2, _center_y + _rad1 / 4)
        elif self.widget_position == "right_top":
            circ_pos = (_center_x - _rad1 / 4, _center_y - _rad1 / 4)
            title_pos = (_center_x - _rad1 / 10, _center_y + _rad1 / 4)
        elif self.widget_position == "left_bottom":
            circ_pos = (_center_x + _rad1 / 4, _center_y + _rad1 / 4)
            title_pos = (_center_x + _rad1 / 2, _center_y + _rad1 / 1.2)
        elif self.widget_position == "right_bottom":
            circ_pos = (_center_x - _rad1 / 4, _center_y + _rad1 / 4)
            title_pos = (_center_x, _center_y + _rad1 / 1.2)
        else:
            # Center.
            circ_pos = (_center_x, _center_y)

            if self.title_position == "auto":
                raise ValueError(
                    "widget_position='center' requires title_position to be set."
                )
            elif self.title_position == "left":
                title_pos = (_center_x + _rad1 / 10, _center_y + _rad1 / 2)
            elif self.title_position == "right":
                title_pos = (_center_x + _rad1 / 1.6, _center_y + _rad1 / 2)
            elif self.title_position == "top":
                title_pos = (_center_x + _rad1 / 2.5, _center_y + _rad1 / 1.3)
            elif self.title_position == "bottom":
                title_pos = (_center_x + _rad1 / 2.5, _center_y + _rad1 / 4)
            elif self.title_position == "left_top":
                title_pos = (_center_x + _rad1 / 8, _center_y + _rad1 / 1.4)
            elif self.title_position == "right_top":
                title_pos = (_center_x + _rad1 / 2, _center_y + _rad1 / 1.3)
            elif self.title_position == "left_bottom":
                title_pos = (_center_x + _rad1 / 8, _center_y + _rad1 / 4)
            elif self.title_position == "right_bottom":
                title_pos = (_center_x + _rad1 / 2, _center_y + _rad1 / 3.5)
            else:
                raise ValueError(
                    f"'{self.title_position}'"
                    f"is not a valid value for title_position"
                )

        self.circ_pos = circ_pos
        return circ_pos, title_pos
