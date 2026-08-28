"""
Behaviors/IOS Background Color
==============================

.. versionadded:: 2.0.1

.. note:: The following classes are intended for in-house use of the library.
"""

from __future__ import annotations

__all__ = ("IOSBackgroundColorBehavior",)

import math

from kivy.atlas import CoreImage
from kivy.lang import Builder
from kivy.properties import ColorProperty, ListProperty, ObjectProperty
from kivy.uix.relativelayout import RelativeLayout

from kivymd.uix.behaviors import BaseBackgroundColorBehavior

Builder.load_string(
    """
<IOSBackgroundColorBehavior>
    canvas.before:
        PushMatrix
        Rotate:
            angle: self.angle
            origin: self._background_origin
        Color:
            rgba: (1, 1, 1, 1) if root._texture else root._bg_color
        Mesh:
            group: "IOS_Background_instruction"
            vertices: root._squircle_vertices
            indices: root._squircle_indices
            mode: "triangle_fan"
            texture: root._texture
        Color:
            group: "ios-backgroundcolor-behavior-line-color"
            rgba: self._line_color
        SmoothLine:
            group: "IOS_Background_line_instruction"
            points: root._squircle_line_points
            width: root.line_width
            close: True
        PopMatrix
""",
    filename="IOSBackgroundColorBehavior.kv",
)


class IOSBackgroundColorBehavior(BaseBackgroundColorBehavior):
    """
    An abstract base class for managing graphical background properties for
    iOS-style widgets.
    """

    bg_color = ColorProperty([0, 0, 0, 0])
    """
    The background color of the widget.

    :attr:`bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    _bg_color = ColorProperty([0, 0, 0, 0])
    _line_color = ColorProperty([0, 0, 0, 0])

    _squircle_vertices = ListProperty([])
    _squircle_indices = ListProperty([])
    _squircle_line_points = ListProperty([])

    _texture = ObjectProperty(None, allownone=True)

    def __init__(self, **kwarg):
        super().__init__(**kwarg)

        self.bind(
            pos=self._update_squircle_mesh,
            size=self._update_squircle_mesh,
            radius=self._update_squircle_mesh,
        )

        if self.background:
            self._update_texture(self, self.background)

    def on_background(self, instance, value: str):
        """Fired when the values of :attr:`background` change."""

        self._update_texture(instance, value)

    def on_bg_color(self, instance, color: list | str):
        """Fired when the values of :attr:`bg_color` change."""

        self._bg_color = color

    def on_line_color(self, instance, color: list | str):
        """Fired when the values of :attr:`line_color` change."""

        self._line_color = color

    def _update_texture(self, instance, value: str):
        if value:
            try:
                self._texture = CoreImage(value).texture
            except Exception as e:
                self._texture = None
        else:
            self._texture = None

    def _update_squircle_mesh(self, *args):
        w, h = self.width, self.height

        if w <= 0 or h <= 0:
            self._squircle_vertices = []
            self._squircle_indices = []
            self._squircle_line_points = []

            return

        is_relative = isinstance(self, RelativeLayout)
        x = 0.0 if is_relative else self.x
        y = 0.0 if is_relative else self.y

        r = self.radius[0] if self.radius else 0

        def get_uv(px, py):
            u = (px - x) / w
            v = 1.0 - ((py - y) / h)

            return u, v

        if r <= 0:
            pts = [(x, y + h), (x + w, y + h), (x + w, y), (x, y)]
            cx, cy = x + w / 2.0, y + h / 2.0
            cu, cv = get_uv(cx, cy)

            vertices = [cx, cy, cu, cv]
            line_pts = []

            for px, py in pts:
                u, v = get_uv(px, py)
                vertices.extend((px, py, u, v))
                line_pts.extend((px, py))

            self._squircle_vertices = vertices
            self._squircle_indices = [0, 1, 2, 3, 4, 1]
            self._squircle_line_points = line_pts

            return

        K = 1.52866483
        r = min(r, min(w, h) / (2.0 * K))

        def cubic(p0, p1, p2, p3, steps=6):
            points = []

            for i in range(steps + 1):
                t = i / steps
                u = 1.0 - t
                px = (
                    u * u * u * p0[0]
                    + 3.0 * u * u * t * p1[0]
                    + 3.0 * u * t * t * p2[0]
                    + t * t * t * p3[0]
                )
                py = (
                    u * u * u * p0[1]
                    + 3.0 * u * u * t * p1[1]
                    + 3.0 * u * t * t * p2[1]
                    + t * t * t * p3[1]
                )
                points.append((px, py))

            return points

        def TL(a, b):
            return (x + a * r, y + h - b * r)

        def TR(a, b):
            return (x + w - a * r, y + h - b * r)

        def BR(a, b):
            return (x + w - a * r, y + b * r)

        def BL(a, b):
            return (x + a * r, y + b * r)

        pts = []

        def add_line(point):
            if not pts or point != pts[-1]:
                pts.append(point)

        def add_curve(p0, p1, p2, p3):
            curve = cubic(p0, p1, p2, p3)

            if pts and curve:
                curve = curve[1:]

            pts.extend(curve)

        add_line(TL(K, 0))
        add_line(TR(K, 0))

        add_curve(
            TR(K, 0),
            TR(1.08849323, 0),
            TR(0.86840689, 0),
            TR(0.66993427, 0.06549600),
        )
        add_line(TR(0.63149399, 0.07491100))
        add_curve(
            TR(0.63149399, 0.07491100),
            TR(0.37282392, 0.16905899),
            TR(0.16906013, 0.37282401),
            TR(0.07491176, 0.63149399),
        )
        add_curve(
            TR(0.07491176, 0.63149399),
            TR(0.0, 0.86840701),
            TR(0.0, 1.08849299),
            TR(0.0, K),
        )

        add_line(BR(0, K))

        add_curve(
            BR(0, K),
            BR(0, 1.08849323),
            BR(0, 0.86840689),
            BR(0.06549569, 0.66993493),
        )
        add_line(BR(0.07491111, 0.63149399))
        add_curve(
            BR(0.07491111, 0.63149399),
            BR(0.16905883, 0.37282392),
            BR(0.37282392, 0.16905883),
            BR(0.63149399, 0.07491111),
        )
        add_curve(
            BR(0.63149399, 0.07491111),
            BR(0.86840689, 0.0),
            BR(1.08849323, 0.0),
            BR(K, 0.0),
        )

        add_line(BL(K, 0))

        add_curve(
            BL(K, 0),
            BL(1.08849299, 0.0),
            BL(0.86840701, 0.0),
            BL(0.66993397, 0.06549569),
        )
        add_line(BL(0.63149399, 0.07491111))
        add_curve(
            BL(0.63149399, 0.07491111),
            BL(0.37282401, 0.16905883),
            BL(0.16906001, 0.37282392),
            BL(0.07491100, 0.63149399),
        )
        add_curve(
            BL(0.07491100, 0.63149399),
            BL(0.0, 0.86840689),
            BL(0.0, 1.08849323),
            BL(0.0, K),
        )

        add_line(TL(0, K))

        add_curve(
            TL(0, K),
            TL(0.0, 1.08849299),
            TL(0.0, 0.86840701),
            TL(0.06549600, 0.66993397),
        )
        add_line(TL(0.07491100, 0.63149399))
        add_curve(
            TL(0.07491100, 0.63149399),
            TL(0.16906001, 0.37282401),
            TL(0.37282401, 0.16906001),
            TL(0.63149399, 0.07491100),
        )
        add_curve(
            TL(0.63149399, 0.07491100),
            TL(0.86840701, 0.0),
            TL(1.08849299, 0.0),
            TL(K, 0.0),
        )

        unique_pts = []

        for px, py in pts:
            if not unique_pts:
                unique_pts.append((px, py))
                continue
            lx, ly = unique_pts[-1]

            if math.hypot(px - lx, py - ly) > 0.001:
                unique_pts.append((px, py))

        cx = x + w / 2.0
        cy = y + h / 2.0
        cu, cv = get_uv(cx, cy)

        vertices = [cx, cy, cu, cv]
        line_pts = []

        for px, py in unique_pts:
            u, v = get_uv(px, py)
            vertices.extend((px, py, u, v))
            line_pts.extend((px, py))

        self._squircle_vertices = vertices
        self._squircle_indices = list(range(len(unique_pts) + 1))
        self._squircle_indices.append(1)
        self._squircle_line_points = line_pts
