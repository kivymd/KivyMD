"""
Components/RulerPicker
======================

.. versionadded:: 2.0.1

.. rubric:: A ruler picker displays a scrollable scale of discrete values,
    allowing people to select a precise number by dragging or flicking through
    tick marks.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-ruler-pickers-intro.png
    :align: center

Base example
------------

.. tabs::

    .. tab:: Imperative style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp


            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                IOSRulerPicker:
                    id: ruler
                    min: 100
                    max: 250
                    value: 180
                    size_hint_y: None
                    height: dp(40)
                    label_step: 20
                    pos_hint: {"center_y": .5}

                    IOSRulerPickerLabel:
                        step: 20
            '''


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)



            Example().run()

    .. tab:: Declarative style

        .. code-block:: python

            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.pickers import IOSRulerPicker, IOSRulerPickerLabel
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"

                    return MDScreen(
                        IOSRulerPicker(
                            IOSRulerPickerLabel(),
                            min=100,
                            max=250,
                            value=180,
                            size_hint_y=None,
                            height=dp(40),
                            label_step=20,
                            pos_hint={"center_y": .5},
                        ),
                        md_bg_color=self.theme_cls.backgroundColor,
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-ruler-base-example.gif
    :align: center
"""

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.text import Label as CoreLabel
from kivy.graphics import Color, InstructionGroup, Rectangle, RoundedRectangle
from kivy.metrics import dp, sp
from kivy.properties import ColorProperty, NumericProperty, ObjectProperty
from kivy.uix.widget import Widget

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.label import MDLabel

__all__ = (
    "IOSRulerPicker",
    "IOSRulerPickerLabel",
)


class IOSRulerPickerLabel(MDLabel):
    """
    Label configuration widget for :class:`~IOSRulerPicker`.

    For more information, see in the
    :class:`~kivymd.uix.label.MDLabel` class.
    """

    formatter = ObjectProperty(lambda val: str(int(round(val))))
    """
    Callable function used to format numeric values into custom text strings
    for labels.

    :attr:`formatter` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `lambda val: str(int(round(val)))`.
    """


class IOSRulerPicker(DeclarativeBehavior, ThemableBehavior, Widget):
    """
    An iOS-style ruler picker widget that allows users to select numeric values
    by scrolling a visual ruler.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.widget.Widget`
    classes documentation.
    """

    step = NumericProperty(1)
    """
    Value interval between adjacent ticks.

    :attr:`step` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    min = NumericProperty(100)
    """
    Minimum selectable value on the ruler.

    :attr:`min` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `100`.
    """

    max = NumericProperty(250)
    """
    Maximum selectable value on the ruler.

    :attr:`max` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `250`.
    """

    value = NumericProperty(0)
    """
    Current selected value on the ruler.

    :attr:`value` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    division_distance = NumericProperty(dp(12))
    """
    Physical distance between adjacent tick marks in density-independent pixels.

    :attr:`division_distance` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(12)`.
    """

    tick_width = NumericProperty(dp(2))
    """
    Width of individual ruler tick lines.

    :attr:`tick_width` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(2)`.
    """

    center_indicator_width = NumericProperty(dp(4))
    """
    Width of the static center indicator marker.

    :attr:`center_indicator_width` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(4)`.
    """

    indicator_color = ColorProperty([1, 1, 1, 1])
    """
    Color of the static center indicator marker in RGBA format.

    :attr:`indicator_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 1]`.
    """

    primary_tick_color = ColorProperty([0.3, 0.3, 0.3, 1])
    """
    Color of the ruler tick marks in RGBA format.

    :attr:`primary_tick_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0.3, 0.3, 0.3, 1]`.
    """

    secondary_tick_color = ColorProperty([0.7, 0.7, 0.7, 1])
    """
    Color of major tick marks located directly above numeric labels in RGBA
    format. Accepts a hex string, color name, or RGBA list.

    :attr:`secondary_tick_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0.7, 0.7, 0.7, 1]`.
    """

    label = ObjectProperty(None, allownone=True)
    """
    Optional :class:`~IOSRulerPickerLabel` instance used to render numeric
    labels under tick marks. If `None`, labels will not be displayed.

    :attr:`label` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    label_step = NumericProperty(1)
    """
    Interval step between displayed numeric labels
    (e.g., `1` for every tick, `5` for major ticks).

    :attr:`label_step` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._touch_active = False
        self._velocity = 0
        self._last_touch_x = 0
        self._scroll_event = None
        self._snap_anim = None
        self._max_touch_delta = dp(40)

        # Graphic instruction pool setup.
        self._pool_size = 120
        self._tick_pool = []
        self._label_pool = []
        self._label_cache = {}

        self._ticks_group = InstructionGroup()
        self._labels_group = InstructionGroup()
        self._indicator_group = InstructionGroup()

        self._setup_graphics_pool()

        self.bind(
            pos=self._update_canvas,
            size=self._update_canvas,
            value=self._update_canvas,
            step=self._update_canvas,
            division_distance=self._update_canvas,
            primary_tick_color=self._update_canvas,
            secondary_tick_color=self._update_canvas,
            indicator_color=self._update_canvas,
            label=self._on_label_changed,
        )

    def _on_label_changed(self, instance, value):
        if value:
            value.bind(
                font_size=self._trigger_update,
                font_name=self._trigger_update,
                text_color=self._trigger_update,
                formatter=self._trigger_update,
            )
        self._trigger_update()

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, IOSRulerPickerLabel):
            self.label = widget
            return

        return super().add_widget(widget, *args, **kwargs)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return super().on_touch_down(touch)

        if self._snap_anim:
            self._snap_anim.cancel(self)
        if self._scroll_event:
            self._scroll_event.cancel()

        touch.grab(self)
        self._touch_active = True
        self._last_touch_x = touch.x
        self._velocity = 0

        return True

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            dx = touch.x - self._last_touch_x
            self._velocity = dx
            self._last_touch_x = touch.x

            max_delta = self._max_touch_delta
            dx = max(-max_delta, min(max_delta, dx))

            val_delta = -dx / self.division_distance * self.step
            self.value = max(self.min, min(self.max, self.value + val_delta))

            return True

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self._touch_active = False

            if abs(self._velocity) > dp(2):
                self._scroll_event = Clock.schedule_interval(
                    self._apply_inertia, 1 / 80
                )
            else:
                self._snap_to_nearest()

            return True

        return super().on_touch_up(touch)

    def _trigger_update(self, *args):
        Clock.schedule_once(self._update_canvas, -1)

    def _setup_graphics_pool(self) -> None:
        """
        Pre-allocates Canvas graphic instructions for object pooling to
        optimize rendering performance during scrolling.
        """

        for _ in range(self._pool_size):
            color_instr = Color(0, 0, 0, 0)
            rect_instr = RoundedRectangle(pos=(0, 0), size=(0, 0), radius=[0])
            self._ticks_group.add(color_instr)
            self._ticks_group.add(rect_instr)
            self._tick_pool.append((color_instr, rect_instr))

            lbl_color_instr = Color(0, 0, 0, 0)
            lbl_rect_instr = Rectangle(pos=(0, 0), size=(0, 0))
            self._labels_group.add(lbl_color_instr)
            self._labels_group.add(lbl_rect_instr)
            self._label_pool.append((lbl_color_instr, lbl_rect_instr))

        self._center_color = Color(*self.indicator_color)
        self._center_rect = RoundedRectangle(
            pos=(0, 0), size=(0, 0), radius=[self.center_indicator_width / 2.0]
        )
        self._indicator_group.add(self._center_color)
        self._indicator_group.add(self._center_rect)

        self.canvas.add(self._ticks_group)
        self.canvas.add(self._labels_group)
        self.canvas.add(self._indicator_group)

    def _get_label_texture(self, text: str):
        lbl = self.label
        font_size = lbl.font_size if lbl else sp(14)
        font_name = lbl.font_name if lbl else "Roboto"

        cache_key = (text, font_size, font_name)

        if cache_key not in self._label_cache:
            core_lbl = CoreLabel(
                text=text,
                font_size=font_size,
                font_name=font_name,
            )
            core_lbl.refresh()
            self._label_cache[cache_key] = core_lbl.texture

        return self._label_cache[cache_key]

    def _apply_inertia(self, dt: float) -> None:
        """
        Applies deceleration inertia with Delta Time calculation to ensure consistent
        decay behavior regardless of screen refresh rate.
        """

        fps_factor = dt * 60.0
        val_delta = (
            -self._velocity / self.division_distance * self.step * fps_factor
        )
        new_val = max(self.min, min(self.max, self.value + val_delta))
        self.value = new_val

        self._velocity *= 0.92**fps_factor

        if abs(self._velocity) < 0.1 or self.value in (self.min, self.max):
            if self._scroll_event:
                self._scroll_event.cancel()
                self._scroll_event = None

            self._snap_to_nearest()

    def _snap_to_nearest(self) -> None:
        """
        Animates the current value to the nearest discrete step mark using an
        ease-out curve.
        """

        if self._snap_anim:
            self._snap_anim.cancel(self)

        steps_from_min = round((self.value - self.min) / self.step)
        target_val = self.min + steps_from_min * self.step
        target_val = max(self.min, min(self.max, target_val))

        if abs(self.value - target_val) < 1e-5:
            self.value = target_val
            return

        self._snap_anim = Animation(value=target_val, d=0.15, t="out_quad")
        self._snap_anim.start(self)

    def _update_canvas(self, *args) -> None:
        """
        Redraws visible ruler ticks using the pre-allocated instruction pool.
        Calculates position, dynamic height magnification, and edge fading for
        each tick.
        """

        if not self.width or not self.height:
            return

        has_labels = self.label is not None

        center_x = self.x + self.width / 2.0
        center_y = self.y + self.height / 2.0
        half_width = self.width / 2.0

        base_h_normal = self.height * 0.25 if has_labels else self.height * 0.35
        base_h_major = self.height * 0.45 if has_labels else self.height * 0.55
        max_h_center = self.height * 0.55 if has_labels else self.height * 0.7

        tick_center_y = center_y + (dp(12) if has_labels else 0)

        div_dist = self.division_distance
        t_width = self.tick_width
        half_t_width = t_width / 2.0
        c_width = self.center_indicator_width
        tick_pool = self._tick_pool
        label_pool = self._label_pool
        pool_size = self._pool_size

        clamped_val = max(self.min, min(self.max, self.value))
        current_tick_idx = (clamped_val - self.min) / self.step
        total_ticks = int((self.max - self.min) / self.step)

        visible_count = int(half_width / div_dist) + 2
        start_idx = max(0, int(current_tick_idx - visible_count))
        end_idx = min(total_ticks, int(current_tick_idx + visible_count))

        pool_idx = 0

        minor_r, minor_g, minor_b, minor_a = self.primary_tick_color
        major_r, major_g, major_b, major_a = self.secondary_tick_color

        if has_labels and self.label.text_color:
            lr, lg, lb, la = self.label.text_color
        else:
            lr, lg, lb, la = 0.5, 0.5, 0.5, 1.0

        lbl_step = self.label_step if has_labels else 1

        for i in range(start_idx, end_idx + 1):
            if pool_idx >= pool_size:
                break

            tick_x = center_x + (i - current_tick_idx) * div_dist
            dist_center = abs(tick_x - center_x)

            if dist_center > half_width:
                continue

            dist_norm = dist_center / half_width
            alpha = 1.0 - (dist_norm * dist_norm)
            proximity = 1.0 - dist_norm
            proximity_cubed = proximity * proximity * proximity

            has_label = has_labels and (i % lbl_step == 0)

            is_major_height = (i % 5 == 0) or has_label
            base_h = base_h_major if is_major_height else base_h_normal
            tick_h = base_h + (max_h_center - base_h) * proximity_cubed

            if has_label:
                cr, cg, cb, ca = major_r, major_g, major_b, major_a
            else:
                cr, cg, cb, ca = minor_r, minor_g, minor_b, minor_a

            # Drawing the tick mark.
            color_instr, rect_instr = tick_pool[pool_idx]
            color_instr.rgba = (cr, cg, cb, alpha * ca)
            rect_instr.pos = (
                tick_x - half_t_width,
                tick_center_y - tick_h / 2.0,
            )
            rect_instr.size = (t_width, tick_h)
            rect_instr.radius = [half_t_width]

            # Drawing the number below the tick mark.
            lbl_color_instr, lbl_rect_instr = label_pool[pool_idx]
            if has_label:
                val_at_tick = self.min + i * self.step
                text_str = self.label.formatter(val_at_tick)
                texture = self._get_label_texture(text_str)

                lbl_color_instr.rgba = (lr, lg, lb, alpha * la)
                lbl_rect_instr.texture = texture
                lbl_rect_instr.pos = (
                    tick_x - texture.width / 2.0,
                    tick_center_y - max_h_center / 2.0 - texture.height - dp(6),
                )
                lbl_rect_instr.size = texture.size
            else:
                lbl_color_instr.rgba = (0, 0, 0, 0)
                lbl_rect_instr.size = (0, 0)

            pool_idx += 1

        # Reset remaining unused pool items.
        for color_instr, rect_instr in tick_pool[pool_idx:]:
            color_instr.rgba = (0, 0, 0, 0)
            rect_instr.size = (0, 0)

        for lbl_color_instr, lbl_rect_instr in label_pool[pool_idx:]:
            lbl_color_instr.rgba = (0, 0, 0, 0)
            lbl_rect_instr.size = (0, 0)

        # Update center indicator marker.
        self._center_color.rgba = self.indicator_color
        self._center_rect.pos = (
            center_x - c_width / 2.0,
            tick_center_y - max_h_center / 2.0,
        )
        self._center_rect.size = (c_width, max_h_center)
