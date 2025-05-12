"""
Components/CircularLayout
=========================

CircularLayout is a special layout that places widgets around a circle.

MDCircularLayout
----------------

.. rubric:: Usage

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            from kivy.lang.builder import Builder

            from kivymd.app import MDApp
            from kivymd.uix.label import MDLabel

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDCircularLayout:
                    id: container
                    pos_hint: {"center_x": .5, "center_y": .5}
                    row_spacing: min(self.size) * 0.1
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)

                def on_start(self):
                    for x in range(1, 49):
                        self.root.ids.container.add_widget(
                            MDLabel(text=f"{x}", adaptive_size=True)
                        )


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.clock import Clock

            from kivymd.app import MDApp
            from kivymd.uix.circularlayout import MDCircularLayout
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.screen = MDScreen(
                        MDCircularLayout(
                            id="container",
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                        ),
                        md_bg_color=self.theme_cls.backgroundColor
                    )
                    return self.screen

                def on_start(self):
                    def on_start(*args):
                        container.row_spacing = min(container.size) * 0.1

                    container = self.screen.get_ids().container
                    for x in range(1, 49):
                        self.screen.get_ids().container.add_widget(
                            MDLabel(text=f"{x}", adaptive_size=True)
                        )

                    Clock.schedule_once(on_start)


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/circular-layout.png
    :align: center
"""

__all__ = ("MDCircularLayout",)

from math import atan2, cos, degrees, radians, sin

from kivy.properties import BooleanProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout

from kivymd.uix.behaviors import DeclarativeBehavior


class MDCircularLayout(DeclarativeBehavior, FloatLayout):
    """
    Circular layout class.

    For more information see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.floatlayout.FloatLayout`
    classes documentation.
    """

    degree_spacing = NumericProperty(30)
    """
    The space between children in degree.

    :attr:`degree_spacing` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `30`.
    """

    circular_radius = NumericProperty(None, allownone=True)
    """
    Radius of circle. Radius will be the greatest value in the layout
    if `circular_radius` if not specified.

    :attr:`circular_radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    start_from = NumericProperty(60)
    """
    The positon of first child in degree.

    :attr:`start_from` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `60`.
    """

    max_degree = NumericProperty(360)
    """
    Maximum range in degree allowed for each row of widgets before jumping
    to the next row.

    :attr:`max_degree` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `360`.
    """

    circular_padding = NumericProperty("25dp")
    """
    Padding between outer widgets and the edge of the biggest circle.

    :attr:`circular_padding` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `25dp`.
    """

    row_spacing = NumericProperty("50dp")
    """
    Space between each row of widget.

    :attr:`row_spacing` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `50dp`.
    """

    clockwise = BooleanProperty(True)
    """
    Direction of widgets in circular direction.

    :attr:`clockwise` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind(
            row_spacing=self._update_layout,
        )

    def get_angle(self, pos: tuple) -> float:
        """Returns the angle of given pos."""

        center = [self.pos[0] + self.width / 2, self.pos[1] + self.height / 2]
        (dx, dy) = (center[0] - pos[0], center[1] - pos[1])
        angle = degrees(atan2(float(dy), float(dx)))
        angle += 180
        return angle

    def remove_widget(self, widget, **kwargs):
        super().remove_widget(widget, **kwargs)
        self._update_layout()

    def do_layout(self, *largs, **kwargs):
        self._update_layout()
        return super().do_layout(*largs, **kwargs)

    def _max_per_row(self):
        return int(self.max_degree / self.degree_spacing)

    def _update_layout(self, *args):
        for index, child in enumerate(reversed(self.children)):
            pos = self._point_on_circle(
                self._calculate_radius(index),
                self._calculate_degree(index),
            )
            child.center = pos

    def _calculate_radius(self, index):
        """Calculates the radius for given index."""

        idx = int(index / self._max_per_row())

        if not self.circular_radius:
            init_radius = (
                min([self.width / 2, self.height / 2]) - self.circular_padding
            )
        else:
            init_radius = self.circular_radius

        if idx != 0:
            space = self.row_spacing * idx
            init_radius -= space

        return init_radius

    def _calculate_degree(self, index):
        """Calculates the angle for given index."""

        if self.clockwise:
            degree = self.start_from - index * self.degree_spacing
        else:
            degree = self.start_from + index * self.degree_spacing

        return degree

    def _point_on_circle(self, radius, degree):
        angle = radians(degree)
        center = [self.pos[0] + self.width / 2, self.pos[1] + self.height / 2]
        x = center[0] + (radius * cos(angle))
        y = center[1] + (radius * sin(angle))
        return [x, y]


if __name__ == "__main__":
    from kivy.lang.builder import Builder

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDCircularLayout:
            id: container
            pos_hint: {"center_x": .5, "center_y": .5}
            row_spacing: min(self.size) * 0.1
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)

        def on_start(self):
            for x in range(1, 49):
                self.root.ids.container.add_widget(
                    MDLabel(text=f"{x}", adaptive_size=True)
                )


    Example().run()

