from kivy.properties import ListProperty, StringProperty
from kivy.uix.widget import Widget


class PieChartLine(Widget):
    text = StringProperty()
    line_color = ListProperty(
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
    )
    angle_start = ListProperty([0, 0, 0, 0])
    angle_end = ListProperty([0, 0, 0, 0])
