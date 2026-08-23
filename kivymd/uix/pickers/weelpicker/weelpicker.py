"""
Components/WheelPicker
======================

.. versionadded:: 2.0.1

.. seealso::

    `Human Interface Guidelines, Pickers <https://developer.apple.com/design/human-interface-guidelines/pickers>`_

.. rubric:: A picker displays one or more scrollable lists of distinct values
    that people can choose from.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-intro.png
    :align: center

Anatomy
=======

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-anatomy.png
    :align: center

Base example
============

.. code-block:: python

    import calendar

    from kivy.metrics import dp

    from kivymd.uix.pickers import IOSWheelPickerLabel, IOSWheelPicker
    from kivymd.app import MDApp
    from kivymd.uix.screen import MDScreen


    class MainScreen(MDScreen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            months = list(calendar.month_name)[1:]
            custom_cols = [
                (months, "August"),
            ]

            self.widgets = [
                IOSWheelPicker(
                    IOSWheelPickerLabel(
                        bold=True,
                        selected_color="white",
                        normal_color=(1, 1, 1, .5),
                    ),
                    columns=custom_cols,
                    visible_count=7,
                    picker_width=dp(320),
                    curve_factor=dp(35),
                )
            ]


    class ExampleApp(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return MainScreen(
                md_bg_color=self.theme_cls.backgroundColor
            )


    if __name__ == "__main__":
        ExampleApp().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-base-example.png
    :align: center

.. note:: Do not create the `WheelPicker` widget in `KV` files or strings.

Creating wheels pickers
=======================

1. Automatic generation of a numeric range
2. One list + explicitly selected value
3. List of elements only
4. Several columns
5. Combining different types of columns
6. Unit label

Automatic generation of a numeric range
---------------------------------------

.. code-block:: python

        custom_cols = [
            (
                0,   # start
                24,  # end
                12,  # current set value
            ),
        ]
        IOSWheelPicker(
            columns=custom_cols,
        )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-generation-numeric-range.png
    :align: center

One list + explicitly selected value
------------------------------------

.. code-block:: python

    months = list(calendar.month_name)[1:]
    custom_cols = [
        (
            months,    # list items
            "August",  # current set value
        ),
    ]
    IOSWheelPicker(
        columns=custom_cols,
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-list-explicitly-selected-value.png
    :align: center

List of elements only
---------------------

.. code-block:: python

    months = list(calendar.month_name)[1:]
    custom_cols = [
        (
            months,    # list items
        ),
    ]
    IOSWheelPicker(
        columns=custom_cols,
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-list-elements-only.png
    :align: center

Several columns
---------------

.. code-block:: python

    months = list(calendar.month_name)[1:]
    custom_cols = [
        (
            (1900, 2026, 2026),
            (months, "August"),
        ),
    ]
    IOSWheelPicker(
        columns=custom_cols,
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-several-columns.png
    :align: center

Combining different types of columns
------------------------------------

.. code-block:: python

    months = list(calendar.month_name)[1:]
        custom_cols = [
            (2020, 2030, 2026),
            (months, "August"),
            (1, 31, 15),
        ]
    IOSWheelPicker(
        columns=custom_cols,
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-combining-different-types-columns.png
    :align: center

Unit label
----------

.. code-block:: python

    months = list(calendar.month_name)[1:]
    custom_cols = [
        (
            (1, 31, 20, "DAY"),
            (months, "August", "Month"),
        ),
    ]
    IOSWheelPicker(
        IOSWheelPickerUnitLabel(
            bold=True,
        ),
        columns=custom_cols,
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-unit-label.png
    :align: center

Events
======

.. code-block:: python

    IOSWheelPicker(
        on_select=self.on_picker_select,
    )

    def on_picker_select(self, instance, values) -> None:
        '''
        Called when the selection changes in any column of the picker.

        :param instance: The :class:`~kivymd.uix.pickers.weelpicker.weelpicker.IOSWheelPicker`
            instance that triggered the event.
        :type instance: IOSWheelPicker

        :param values: A list containing the current selected values from all
            columns (e.g., ``[11, 'August']``).
        :type values: list[str | int]
        '''

        # <kivymd.uix.pickers.weelpicker.weelpicker.IOSWheelPicker object at 0x11ba020b0>
        # [11, 'August']
        print(instance)
        print(values)

Additional configuration parameters
==================================

Visible number of elements
--------------------------

.. code-block:: python

    IOSWheelPicker(
        visible_count=5,  # 10
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-visible-count-5.png
    :align: center

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-visible-count-10.png
    :align: center

Intensity factor of the 3D cylindrical curvature transformation
---------------------------------------------------------------

.. code-block:: python

    IOSWheelPicker(
        curve_factor=dp(15),  # 55
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-curve-factor-15.png
    :align: center

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-visible-count-10.png
    :align: center

Total layout width of the picker component
------------------------------------------

.. code-block:: python

    IOSWheelPicker(
        picker_width=dp(120),  # dp(320)
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-width-120.png
    :align: center

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-width-320.png
    :align: center

Pixel height of each row item
-----------------------------

.. code-block:: python

    IOSWheelPicker(
        item_height=dp(24),  # dp(36)
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-height-24.png
    :align: center

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-height-36.png
    :align: center

Customization
=============

.. code-block:: python

    import calendar

    from kivy.metrics import dp
    from kivy.uix.floatlayout import FloatLayout

    from kivymd.app import MDApp
    from kivymd.uix.screen import MDScreen
    from kivymd.uix.behaviors import IOSGlassBehavior, DeclarativeBehavior
    from kivymd.uix.fitimage import FitImage
    from kivymd.uix.pickers import IOSWheelPickerLabel, IOSWheelPicker


    class GlassContainer(DeclarativeBehavior, IOSGlassBehavior, FloatLayout):
        pass


    class MainScreen(MDScreen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            months = list(calendar.month_name)[1:]
            custom_cols = [
                (1, 31, 20),
                (months, "August"),
            ]

            bg_image = FitImage(source="/Users/ivanovyuri/Pictures/Screenshoots/111.png")

            self.widgets = [
                bg_image,
                GlassContainer(
                    IOSWheelPicker(
                        IOSWheelPickerLabel(
                            font_style="Title",
                            font_size="20sp",
                            bold=True,
                            selected_color="white",
                            normal_color=(1, 1, 1, .5),
                        ),
                        columns=custom_cols,
                        visible_count=7,
                        picker_width=dp(320),
                        curve_factor=dp(35),
                    ),
                    target_background=bg_image,
                    border_radius=[dp(26), dp(26), dp(26), dp(26)],
                    glass_color=[1.0, 1.0, 1.0, 0.18],
                    blur_amount=10.0,
                    size_hint=(None, None),
                    size=(dp(320), dp(200)),
                    pos_hint={"center_x": .5, "center_y": .5},
                )
            ]


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return MainScreen()


    if __name__ == "__main__":
        Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-pickers-customization.png
    :align: center
"""

from __future__ import annotations

__all__ = (
    "IOSWheelPicker",
    "IOSWheelPickerLabel",
    "IOSWheelPickerUnitLabel",
)

import math

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import (
    Color,
    PopMatrix,
    PushMatrix,
    RoundedRectangle,
    Scale,
    Translate,
)
from kivy.metrics import dp
from kivy.properties import BooleanProperty, ColorProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.label import MDLabel


class IOSWheelPickerUnitLabel(MDLabel):
    """
    Text label widget used for column unit indicators.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """

    normal_color = ColorProperty(None, allownone=True)
    """
    The text color the unit label.

    :attr:`normal_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        self._user_normal_color = "normal_color" in kwargs

        super().__init__(**kwargs)

        # FIXME: It's just a workaround, since the marker isn't positioned in
        #  the center.
        self.padding = [0, dp(4), 0, 0]

        self.bind(normal_color=self._update_text_color)
        self.theme_cls.bind(
            theme_style=self._on_theme_style_change,
            primary_palette=self._on_theme_style_change,
        )

        if not self._user_normal_color:
            self.normal_color = self.theme_cls.primaryColor

        self._update_text_color()

    def _update_text_color(self, *args):
        if self.normal_color:
            self.text_color = self.normal_color

    def _on_theme_style_change(self, instance, value):
        if not self._user_normal_color:
            self.normal_color = self.theme_cls.primaryColor


class IOSWheelPickerLabel(MDLabel):
    """
    Text label widget supporting 3D scale and translation transformations
    relative to its center point.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """

    selected_color = ColorProperty(None)
    """
    The text color when the label is currently selected
    (e.g., inside the picker selection zone).

    :attr:`selected_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    normal_color = ColorProperty(None)
    """
    The text color when the label is in its unselected or idle state.

    :attr:`normal_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        self._user_selected_color = "selected_color" in kwargs
        self._user_normal_color = "normal_color" in kwargs

        super().__init__(**kwargs)

        with self.canvas.before:
            PushMatrix()
            self.translate_inst = Translate(0, 0, 0)
            self.scale_inst = Scale(1, 1, 1)
        with self.canvas.after:
            PopMatrix()

        self.theme_cls.bind(
            theme_style=self._on_theme_style_change,
            primary_palette=self._on_theme_style_change,
        )

        if not self._user_normal_color:
            self.normal_color = list(self.theme_cls.secondaryColor)
        if not self._user_selected_color:
            self.selected_color = list(self.theme_cls.primaryColor)

    def _on_theme_style_change(self, instance, value):
        if not self._user_selected_color:
            self.selected_color = list(self.theme_cls.primaryColor)
        if not self._user_normal_color:
            self.normal_color = list(self.theme_cls.secondaryColor)

    def apply_3d_transform(self, scale_x, scale_y) -> None:
        """
        Applies horizontal and vertical scaling transforms relative to the
        label's center origin.

        :param scale_x: The horizontal scale factor.
        :param scale_y: The vertical scale factor.
        """

        self.scale_inst.x = scale_x
        self.scale_inst.y = scale_y
        self.scale_inst.origin = self.center


class IOSWheelPickerColumn(ThemableBehavior, RelativeLayout):
    """
    Implements a 3D cylindrical wheel column widget for pickers, supporting
    smooth inertial touch scrolling, label pooling, and selection highlighting.

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.relativelayout.RelativeLayout`
    classes documentation.

    :Events:
        :attr:`on_select`
            Fired when an item settles into the central selection zone.
    """

    __events__ = ("on_select",)

    range_min = NumericProperty(0)
    """
    The minimum integer value for auto-generated numeric ranges.

    :attr:`range_min` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    range_max = NumericProperty(59)
    """
    The maximum integer value for auto-generated numeric ranges.

    :attr:`range_max` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `59`.
    """

    selected_value = NumericProperty(0)
    """
    The currently selected item value or index.

    :attr:`selected_value` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    item_height = NumericProperty(dp(36))
    """
    The pixel height reserved for each item row in the wheel.

    :attr:`item_height` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(36)`.
    """

    visible_count = NumericProperty(5)
    """
    The total number of items visible simultaneously along the vertical axis.

    :attr:`visible_count` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `5`.
    """

    side = NumericProperty(0)
    """
    Side alignment index determining horizontal 3D curve offset
    (`-1` for left-side column, `0` for center, `1` for right-side column).

    :attr:`side` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    curve_factor = NumericProperty(dp(45))
    """
    The intensity factor of the 3D cylindrical curvature distortion.

    :attr:`curve_factor` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(45)`.
    """

    has_unit = BooleanProperty(False)
    """
    Indicates whether a measurement unit label is appended, shifting text
    horizontal centering.

    :attr:`has_unit` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    scroll_offset = NumericProperty(0.0)
    """
    The current floating-point scroll position measured in item units.

    :attr:`scroll_offset` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.0`.
    """

    selected_color = ColorProperty(None)
    """
    The highlight text color applied when an item enters the selection zone.

    :attr:`selected_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    normal_color = ColorProperty(None)
    """
    The default text color for unselected items outside the central zone.

    :attr:`normal_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0.75, 0.75, 0.75, 1]`.
    """

    def __init__(
        self,
        items=None,
        label_template=None,
        selected_color=None,
        normal_color=None,
        **kwargs,
    ):
        self._user_selected_color = selected_color is not None
        self._user_normal_color = normal_color is not None

        self.items_list = items
        self.label_template = label_template

        if selected_color:
            kwargs["selected_color"] = selected_color
        if normal_color:
            kwargs["normal_color"] = normal_color

        if self.items_list:
            self.n_items = len(self.items_list)
            kwargs["range_min"] = 0
            kwargs["range_max"] = self.n_items - 1
        else:
            r_min = kwargs.get("range_min", 0)
            r_max = kwargs.get("range_max", 59)
            self.n_items = max(1, r_max - r_min + 1)

        super().__init__(**kwargs)

        self.scroll_offset = float(
            (self.selected_value - self.range_min) % self.n_items
        )

        self._anim = None
        self._last_touch_y = 0
        self._last_touch_time = 0
        self._velocity = 0

        self.pool_size = self.visible_count + 4
        self.label_pool = []

        self._init_label_pool()

        self.theme_cls.bind(
            theme_style=self._on_theme_style_change,
            primary_palette=self._on_theme_style_change,
        )
        self.bind(scroll_offset=self.update_3d_transforms)
        self.bind(size=self._on_size)

        Clock.schedule_once(self.update_3d_transforms)

    def _instantiate_label(self) -> IOSWheelPickerLabel:
        if not self.label_template:
            return IOSWheelPickerLabel(size_hint=(None, None))

        tmpl = self.label_template
        cls = tmpl.__class__

        lbl = cls(
            bold=tmpl.bold,
            font_style=tmpl.font_style,
            font_size=tmpl.font_size,
            font_name=tmpl.font_name,
            size_hint=(None, None),
        )

        if tmpl._user_selected_color:
            lbl.selected_color = tmpl.selected_color
            lbl._user_selected_color = True
        if tmpl._user_normal_color:
            lbl.normal_color = tmpl.normal_color
            lbl._user_normal_color = True

        return lbl

    def _init_label_pool(self):
        for _ in range(self.pool_size):
            lbl = self._instantiate_label()
            self.label_pool.append(lbl)
            self.add_widget(lbl)

    def _on_theme_style_change(self, instance, value):
        for lbl in self.label_pool:
            if hasattr(lbl, "_on_theme_style_change"):
                lbl._on_theme_style_change(instance, value)
        self.update_3d_transforms()

    def _resolve_color(self, lbl, is_selected: bool):
        if is_selected:
            if lbl._user_selected_color and lbl.selected_color is not None:
                return lbl.selected_color
            if self._user_selected_color and self.selected_color is not None:
                return self.selected_color

            return list(self.theme_cls.primaryColor)
        else:
            if lbl._user_normal_color and lbl.normal_color is not None:
                return lbl.normal_color
            if self._user_normal_color and self.normal_color is not None:
                return self.normal_color

            return list(self.theme_cls.secondaryColor)

    def _on_size(self, *args):
        pad_right = dp(6) if self.has_unit else 0

        for lbl in self.label_pool:
            lbl.size = (self.width, self.item_height)
            lbl.text_size = (max(1, self.width - pad_right), self.item_height)
            lbl.valign = "center"
            lbl.halign = "right" if self.has_unit else "center"

        self.update_3d_transforms()

    def on_select(self, value):
        """
        Default handler for the :attr:`on_select` event.

        :param value: The value or string selected by the wheel position.
        """

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self._anim:
                self._anim.cancel(self)
                self._anim = None

            self._last_touch_y = touch.y
            self._last_touch_time = Clock.get_time()
            self._velocity = 0
            touch.grab(self)

            return True

        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            now = Clock.get_time()
            dt = max(0.001, now - self._last_touch_time)
            dy = touch.y - self._last_touch_y

            delta_offset = dy / self.item_height
            self.scroll_offset -= delta_offset

            inst_vel = -delta_offset / dt
            self._velocity = 0.6 * self._velocity + 0.4 * inst_vel

            self._last_touch_y = touch.y
            self._last_touch_time = now

            return True

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)

            throw_distance = self._velocity * 0.18
            target_offset = round(self.scroll_offset + throw_distance)

            dist = abs(target_offset - self.scroll_offset)
            duration = max(0.18, min(0.45, dist * 0.08))

            if self._anim:
                self._anim.cancel(self)

            self._anim = Animation(
                scroll_offset=float(target_offset), d=duration, t="out_quad"
            )

            def _on_complete(anim, widget):
                widget.selected_value = (
                    int(round(widget.scroll_offset)) % widget.n_items
                ) + widget.range_min
                widget._anim = None
                widget.dispatch("on_select", widget.get_current_display_value())

            self._anim.bind(on_complete=_on_complete)
            self._anim.start(self)

            return True

        return super().on_touch_up(touch)

    def get_current_display_value(self) -> str | int:
        """
        Returns the item value currently positioned at the selector center.
        """

        idx = int(round(self.scroll_offset)) % self.n_items
        return self.items_list[idx] if self.items_list else idx + self.range_min


    def update_3d_transforms(self, *args):
        """
        Recalculates and applies 3D cylindrical spatial positioning, scaling,
        perspective curvature, and opacity fading for all active pooled label
        widgets.
        """

        if not self.label_pool or self.height <= 10:
            return

        half_height = self.height / 2.0
        max_visible_dist = self.item_height * (self.visible_count / 2.0)
        radius = self.height * 0.45
        half_pool = self.pool_size // 2

        base_idx = int(math.floor(self.scroll_offset))

        for idx, lbl in enumerate(self.label_pool):
            dist_item = base_idx + (idx - half_pool)

            if self.items_list:
                item_idx = dist_item % self.n_items
                lbl.text = str(self.items_list[item_idx])
            else:
                item_val = (dist_item % self.n_items) + self.range_min
                lbl.text = (
                    f"{item_val:02d}" if self.range_max > 9 else str(item_val)
                )

            dist_from_center_px = (
                dist_item - self.scroll_offset
            ) * self.item_height
            abs_dist = abs(dist_from_center_px)

            if abs_dist >= max_visible_dist - dp(4):
                lbl.opacity = 0
                continue

            angle_rad = dist_from_center_px / radius

            if abs(angle_rad) > 1.25:
                lbl.opacity = 0
                continue

            cos_val = math.cos(angle_rad)
            sin_val = math.sin(angle_rad)

            projected_y = sin_val * radius
            offset_x = -self.side * (1.0 - cos_val) * self.curve_factor

            scale_y = max(0.35, cos_val**1.2)
            scale_x = max(0.70, 0.70 + 0.30 * cos_val)

            edge_fade = max(0.0, 1.0 - (abs_dist / max_visible_dist) ** 1.8)
            alpha = edge_fade * (cos_val**1.5)

            lbl.center_x = self.width * 0.50 + offset_x
            lbl.center_y = half_height + projected_y - dp(2.5)

            lbl.apply_3d_transform(scale_x, scale_y)

            in_selection_glass = abs_dist < (self.item_height / 2.5)
            lbl.text_color = self._resolve_color(lbl, is_selected=in_selection_glass)

            lbl.opacity = 1.0 if in_selection_glass else max(0.0, alpha)


class IOSColumnWrapper(BoxLayout):
    """
    Container layout wrapper that encapsulates a single
    :class:`~IOSWheelPickerColumn` and an optional measurement unit label
    within an iOS-style picker component.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """

    def __init__(
        self,
        col_data,
        label=None,
        unit_label=None,
        selected_color=None,
        normal_color=None,
        side=0,
        total_cols=1,
        visible_count=5,
        item_height=dp(36),
        curve_factor=dp(30),
        **kwargs,
    ):
        super().__init__(orientation="horizontal", spacing=dp(12), **kwargs)

        if isinstance(col_data[0], (list, tuple)):
            items = col_data[0]
            raw_val = col_data[1] if len(col_data) > 1 else 0
            unit_text = col_data[2] if len(col_data) > 2 else None
            range_min, range_max = 0, len(items) - 1

            if isinstance(raw_val, str) and raw_val in items:
                selected_val = items.index(raw_val)
            elif isinstance(raw_val, int):
                selected_val = raw_val
            else:
                selected_val = 0
        else:
            items = None
            range_min = col_data[0]
            range_max = col_data[1]
            selected_val = col_data[2] if len(col_data) > 2 else range_min
            unit_text = col_data[3] if len(col_data) > 3 else None

        has_unit = bool(unit_text)

        self.wheel = IOSWheelPickerColumn(
            items=items,
            label_template=label,
            selected_color=selected_color,
            normal_color=normal_color,
            range_min=range_min,
            range_max=range_max,
            selected_value=selected_val,
            visible_count=visible_count,
            item_height=item_height,
            curve_factor=curve_factor,
            has_unit=has_unit,
            side=side,
            size_hint=(1, 1),
        )
        self.add_widget(self.wheel)

        if has_unit and unit_label:
            cls = unit_label.__class__
            self.unit_label = cls(
                text=unit_text,
                bold=unit_label.bold,
                font_style=unit_label.font_style,
                font_size=unit_label.font_size,
                font_name=unit_label.font_name,
            )
            if unit_label._user_normal_color:
                self.unit_label.normal_color = unit_label.normal_color
                self.unit_label._user_normal_color = True

            self.add_widget(self.unit_label)


class IOSWheelPicker(DeclarativeBehavior, RelativeLayout):
    """
    Implements an iOS-style multi-column wheel picker with 3D cylindrical
    scrolling, customizable item stylingand  selection highlighting.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.relativelayout.RelativeLayout`
    classes documentation.

    :Events:
        :attr:`on_select`
            Fired when an item selection changes in any of the picker columns.
    """

    __events__ = ("on_select",)

    selection_bg_color = ColorProperty([1, 1, 1, 0.18])
    """
    Background color of the central active row selection glass bar in HEX/RGBA
    or string format.

    :attr:`selection_bg_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 0.18]`.
    """

    _label: IOSWheelPickerLabel | None = None
    _unit_label: IOSWheelPickerUnitLabel | None = None

    def __init__(
        self,
        *args,
        columns=None,
        selected_color=None,
        normal_color=None,
        visible_count=5,
        item_height=dp(36),
        curve_factor=dp(30),
        picker_width=dp(340),
        selection_bg_color=None,
        **kwargs,
    ):
        """
        :param columns: List of column definitions. Each item can be a tuple
            for numeric bounds `(min, max, default, unit)` or a tuple with
            custom items `(items_list, default, unit)`.
        :type columns: list or tuple, optional

        :param label: Template instance or dictionary used to construct pooled
            labels inside columns.
        :type label: object or dict, optional

        :param selected_color: RGBA color applied to the selected item inside
            the glass zone.
        :type selected_color: list or tuple, defaults to `(0.2, 0.8, 1, 1)`

        :param normal_color: RGBA color applied to unselected or idle items.
        :type normal_color: list or tuple, defaults to `(0.7, 0.7, 0.7, 1)`

        :param visible_count: Number of rows simultaneously visible along the
            vertical axis.
        :type visible_count: int, defaults to `5`

        :param item_height: Pixel height of each row item.
        :type item_height: float, defaults to `dp(36)`

        :param curve_factor: Intensity factor of the 3D cylindrical curvature
            transformation.
        :type curve_factor: float, defaults to `dp(45)`

        :param picker_width: Total layout width of the picker component.
        :type picker_width: float, defaults to `dp(330)`
        """

        if selection_bg_color:
            kwargs["selection_bg_color"] = selection_bg_color

        super().__init__(*args, **kwargs)

        self.columns_data = (
            columns
            if columns is not None
            else [(0, 23, 12, "H"), (0, 59, 30, "M"), (0, 59, 0, "S")]
        )
        self.selected_color = selected_color
        self.normal_color = normal_color
        self.visible_count = visible_count
        self.item_height = item_height
        self.curve_factor = curve_factor
        self.picker_width = picker_width

        self.size_hint = (None, None)
        self.size = (self.picker_width, self.item_height * self.visible_count)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        with self.canvas.before:
            self.selection_color_inst = Color(*self.selection_bg_color)
            self.selection_rect = RoundedRectangle(
                pos=(dp(6), (self.height - self.item_height) / 2.0),
                size=(max(1, self.width - dp(12)), self.item_height),
                radius=[dp(10)],
            )

        self.bind(
            size=self._update_selection_rect,
            selection_bg_color=self._update_selection_rect,
        )
        Clock.schedule_once(self._update_selection_rect)

        self.columns_box = BoxLayout(
            orientation="horizontal",
            size_hint=(1, 1),
            pos=(0, 0),
            padding=(dp(16), 0, dp(16), 0),
        )
        super().add_widget(self.columns_box)

        self.cols = []
        self._build_columns()

    def on_select(self, values):
        """Default handler for the :attr:`on_select` event."""

    def get_values(self):
        """
        Retrieves current display values across all active picker columns.
        """

        return [col.wheel.get_current_display_value() for col in self.cols]

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, IOSWheelPickerLabel):
            self. _label = widget
            self._build_columns()
        elif isinstance(widget, IOSWheelPickerUnitLabel):
            self. _unit_label = widget
            self._build_columns()
        else:
            super().add_widget(widget, *args, **kwargs)

    def _build_columns(self):
        """Creates or rebuilds columns with the current  _label/ _unit_label."""

        if not hasattr(self, "columns_box"):
            return

        self.columns_box.clear_widgets()
        self.cols.clear()

        total_cols = len(self.columns_data)

        for i, col_data in enumerate(self.columns_data):
            if total_cols == 1:
                side = 0
            elif i == 0:
                side = -1
            elif i == total_cols - 1:
                side = 1
            else:
                side = 0

            col = IOSColumnWrapper(
                col_data=col_data,
                label=self._label,
                unit_label=self._unit_label,
                selected_color=self.selected_color,
                normal_color=self.normal_color,
                side=side,
                total_cols=total_cols,
                visible_count=self.visible_count,
                item_height=self.item_height,
                curve_factor=self.curve_factor,
            )
            col.wheel.bind(on_select=self._on_column_select)
            self.cols.append(col)
            self.columns_box.add_widget(col)

    def _on_column_select(self, instance, value):
        self.dispatch("on_select", self.get_values())

    def _update_selection_rect(self, *args):
        """
        Recalculates size and positional parameters for the translucent
        selection rectangle.
        """

        if hasattr(self, "selection_color_inst"):
            self.selection_color_inst.rgba = self.selection_bg_color
        if hasattr(self, "selection_rect"):
            self.selection_rect.pos = (
                dp(6),
                (self.height - self.item_height) / 2.0,
            )
            self.selection_rect.size = (
                max(1, self.width - dp(12)),
                self.item_height,
            )
