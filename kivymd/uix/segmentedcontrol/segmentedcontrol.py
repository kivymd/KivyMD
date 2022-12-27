"""
Components/SegmentedControl
===========================

.. versionadded:: 1.0.0

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-control-preview.jpg
    :align: center

Usage
=====

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp


            KV = '''
            MDScreen:

                MDSegmentedControl:
                    pos_hint: {"center_x": .5, "center_y": .5}

                    MDSegmentedControlItem:
                        text: "Male"

                    MDSegmentedControlItem:
                        text: "Female"

                    MDSegmentedControlItem:
                        text: "All"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.segmentedcontrol import (
                MDSegmentedControl, MDSegmentedControlItem
            )


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDSegmentedControl(
                                MDSegmentedControlItem(
                                    text="Male"
                                ),
                                MDSegmentedControlItem(
                                    text="Female"
                                ),
                                MDSegmentedControlItem(
                                    text="All"
                                ),
                                pos_hint={"center_x": 0.5, "center_y": 0.5}
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-usage.gif
    :align: center

Events
======

.. code-block:: kv

    MDSegmentedControl:
        on_active: app.on_active(*args)

.. code-block:: python

    def on_active(
        self,
        segmented_control: MDSegmentedControl,
        segmented_item: MDSegmentedControlItem,
    ) -> None:
        '''Called when the segment is activated.'''
"""

__all__ = ("MDSegmentedControl", "MDSegmentedControlItem")

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
    VariableListProperty,
)

from kivymd import uix_path
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDSeparator
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout

with open(
    os.path.join(uix_path, "segmentedcontrol", "segmentedcontrol.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSegmentedControlItem(MDLabel):
    """
    Implements a label to place on the :class:`~SegmentPanel` panel.

    See :class:`~kivymd.uix.label.MDLabel` class documentation for more
    information.
    """


# TODO: Add an attribute for the color of the active segment label.
class MDSegmentedControl(MDRelativeLayout):
    """
    Implements a segmented control panel.

    For more information, see in the
    :class:`~kivymd.uix.relativelayout.MDRelativeLayout` class documentation.

    :Events:
        `on_active`
            Called when the segment is activated.
    """

    md_bg_color = ColorProperty([0, 0, 0, 0])
    """
    Background color of the segment panel in (r, g, b, a) or string format.

    .. code-block:: kv

        MDSegmentedControl:
            md_bg_color: "brown"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-md-bg-color.png
        :align: center

    :attr:`md_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    segment_color = ColorProperty([0, 0, 0, 0])
    """
    Color of the active segment in (r, g, b, a) or string format.

    .. code-block:: kv

        MDSegmentedControl:
            md_bg_color: "brown"
            segment_color: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-segment-color.png
        :align: center

    .. code-block:: kv

        MDSegmentedControl:
            md_bg_color: "brown"
            segment_color: "red"

            MDSegmentedControlItem:
                text: "[color=fff]Male[/color]"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-text-color.png
        :align: center

    :attr:`segment_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    segment_panel_height = NumericProperty("42dp")
    """
    Height of the segment panel.

    .. code-block:: kv

        MDSegmentedControl:
            segment_panel_height: "56dp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-segment-panel-height.png
        :align: center

    :attr:`segment_panel_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'42dp'`.
    """

    separator_color = ColorProperty(None)
    """
    The color of the separator between the segments in (r, g, b, a) or string
    format.

    .. code-block:: kv

        MDSegmentedControl:
            md_bg_color: "brown"
            segment_color: "red"
            separator_color: "white"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-separator-color.png
        :align: center

    :attr:`separator_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    radius = VariableListProperty([16], length=4)
    """
    Radius of the segment panel.

    .. code-block:: kv

        MDSegmentedControl:
            radius: 0

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-segmented-control-segment-radius.png
        :align: center

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[16, 16, 16, 16]`.
    """

    segment_switching_transition = StringProperty("in_cubic")
    """
    Name of the animation type for the switch segment.

    :attr:`segment_switching_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'in_cubic'`.
    """

    segment_switching_duration = NumericProperty(0.2)
    """
    Name of the animation type for the switch segment.

    :attr:`segment_switching_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    current_active_segment = ObjectProperty()
    """
    The current active element of the :class:`~MDSegmentedControlItem` class.

    :attr:`current_active_segment` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    _segment_switch_x = NumericProperty(dp(4))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_active")

        Clock.schedule_once(self.set_default_colors)
        Clock.schedule_once(self._remove_last_separator)

    def set_default_colors(self, *args) -> None:
        """
        Sets the colors of the panel and the switch if the colors are not set
        by the user.
        """

        if self.md_bg_color == [0, 0, 0, 0]:
            self.md_bg_color = self.theme_cls.bg_darkest
        if self.segment_color == [0, 0, 0, 0]:
            self.segment_color = self.theme_cls.bg_dark

    def animation_segment_switch(self, widget: MDSegmentedControlItem) -> None:
        """Animates the movement of the switch."""

        Animation(
            _segment_switch_x=widget.x - dp(6),
            t=self.segment_switching_transition,
            d=self.segment_switching_duration,
        ).start(self)

    def update_segment_panel_width(
        self, widget: MDSegmentedControlItem
    ) -> None:
        """
        Sets the width of the panel for the elements of the
        :class:`~MDSegmentedControlItem` class.
        """

        widget.text_size = (None, None)
        widget.texture_update()
        self.ids.segment_panel.width += (
            widget.texture_size[0] + self.ids.segment_panel.spacing
        )

    def update_separator_color(self, widget: MDSeparator) -> None:
        """Updates the color of the separators between segments."""

        widget.color = (
            self.separator_color
            if self.separator_color
            else self.theme_cls.divider_color
        )

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, (SegmentPanel, SegmentSwitch)):
            return super().add_widget(widget)
        if isinstance(widget, MDSegmentedControlItem):
            Clock.schedule_once(
                lambda x: self.update_segment_panel_width(widget)
            )
            widget.bind(on_touch_down=self.on_press_segment)
            self.ids.segment_panel.add_widget(widget)
            separator = MDSeparator(orientation="vertical")
            self.ids.segment_panel.add_widget(separator)
            if not self.ids.segment_panel._started:
                self.ids.segment_panel._started = True
            else:
                self.ids.segment_panel.children_number += 1
            Clock.schedule_once(
                lambda x: self.update_separator_color(separator)
            )

    def on_active(self, *args) -> None:
        """Called when the segment is activated."""

    def on_press_segment(self, widget: MDSegmentedControlItem, touch):
        if widget.collide_point(touch.x, touch.y):
            self.animation_segment_switch(widget)
            self.current_active_segment = widget
            self.dispatch("on_active", widget)

    def _remove_last_separator(self, *args):
        self.ids.segment_panel.remove_widget(self.ids.segment_panel.children[0])


class SegmentSwitch(MDRaisedButton):
    """Implements a switch for the :class:`~MDSegmentedControl` class."""

    _no_ripple_effect = BooleanProperty(True)


class SegmentPanel(MDBoxLayout):
    """
    Implements a panel for placing items - :class:`~MDSegmentedControlItem`
    for the :class:`~MDSegmentedControl` class.
    """

    children_number = NumericProperty(1)

    _started = BooleanProperty(defaultvalue=False)
