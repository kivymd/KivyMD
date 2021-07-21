"""
Components/CircularLayout
=========================

CircularLayout is a special layout that places widgets around a circle.

MDCircularLayout
----------------

.. rubric:: Usage

.. code-block::

    from kivy.lang.builder import Builder
    from kivy.uix.label import Label

    from kivymd.app import MDApp

    kv = '''
    MDScreen:

        MDCircularLayout:
            id: container
            pos_hint: {"center_x": .5, "center_y": .5}
            row_spacing: min(self.size) * 0.1
    '''


    class Main(MDApp):
        def build(self):
            return Builder.load_string(kv)

        def on_start(self):
            for x in range(1, 49):
                self.root.ids.container.add_widget(
                    Label(text=f"{x}", color=[0, 0, 0, 1])
                )


    Main().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/circular-layout.png
    :align: center
"""

__all__ = ("MDCircularLayout",)

from math import atan2, cos, degrees, radians, sin

from kivy.properties import BooleanProperty, NumericProperty

from kivymd.uix.floatlayout import MDFloatLayout


class MDCircularLayout(MDFloatLayout):

    degree_spacing = NumericProperty(30)
    """
    The space between children in degree.

    :attr:`degree_spacing` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `30`.
    """

    circular_radius = NumericProperty(None, allownone=True)
    """
    Radius of circle. Radius will be the greatest value in the layout if `circular_radius` if not specified.

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
    Maximum range in degree allowed for each row of widgets before jumping to the next row.

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
    from kivy.uix.label import Label

    from kivymd.app import MDApp

    kv = """
MDScreen:

    MDCircularLayout:
        id: container
        pos_hint: {"center_x": .5, "center_y": .5}
        row_spacing: min(self.size) * 0.1
    """

    class Main(MDApp):
        def build(self):
            return Builder.load_string(kv)

        def on_start(self):
            for x in range(1, 49):
                self.root.ids.container.add_widget(
                    Label(text=f"{x}", color=[0, 0, 0, 1])
                )

    Main().run()
