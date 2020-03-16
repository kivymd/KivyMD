"""
Components/Tooltip
==================

.. seealso::

    `Material Design spec, Tooltips <https://material.io/components/tooltips>`_

.. rubric:: Tooltips display informative text when users hover over, focus on,
    or tap an element.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tooltip.png
    :align: center

To use the :class:`~MDTooltip` class, you must create a new class inherited
from the :class:`~MDTooltip` class:

In Kv-language:

.. code-block:: kv

    <TooltipMDIconButton@MDIconButton+MDTooltip>

In Python code:

.. code-block:: python

    class TooltipMDIconButton(MDIconButton, MDTooltip):
        pass

.. Warning:: :class:`~MDTooltip` only works correctly with button classes.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    <TooltipMDIconButton@MDIconButton+MDTooltip>


    Screen:

        TooltipMDIconButton:
            icon: "language-python"
            tooltip_text: self.icon
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tooltip.gif
    :align: center

.. Note:: The behavior of tooltips on desktop and mobile devices is different.
    For more detailed information,
    `click here <https://github.com/HeaTTheatR/KivyMD/wiki/Components-Tooltips>`_.
"""

__all__ = ("MDTooltip", "MDTooltipViewClass")

from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty, NumericProperty

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import HoverBehavior, TouchBehavior
from kivymd.material_resources import DEVICE_TYPE

Builder.load_string(
    """
#:import DEVICE_TYPE kivymd.material_resources.DEVICE_TYPE


<MDTooltipViewClass>
    size_hint: None, None
    width: self.minimum_width
    height: self.minimum_height + root.padding[1]
    opacity: 0

    padding:
        dp(8) if DEVICE_TYPE == "desktop" else dp(16), \
        dp(4), \
        dp(8) if DEVICE_TYPE == "desktop" else dp(16), \
        dp(4)

    canvas.before:
        PushMatrix
        Color:
            rgba:
                root.theme_cls.opposite_bg_dark if not root.tooltip_bg_color \
                else root.tooltip_bg_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [5]
        Scale:
            origin: self.center
            x: root._scale_x
            y: root._scale_y
    canvas.after:
        PopMatrix


    Label:
        id: label_tooltip
        text: root.tooltip_text
        size_hint: None, None
        size: self.texture_size
        bold: True
        color:
            ([0, 0, 0, 1] if not root.tooltip_text_color else root.tooltip_text_color) \
            if root.theme_cls.theme_style == "Dark" else \
            ([1, 1, 1, 1] if not root.tooltip_text_color else root.tooltip_text_color)
        pos_hint: {"center_y": .5}
"""
)


class MDTooltip(ThemableBehavior, HoverBehavior, TouchBehavior, BoxLayout):
    tooltip_bg_color = ListProperty()
    """Tooltip background color in ``rgba`` format.
    
    :attr:`tooltip_bg_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    tooltip_text_color = ListProperty()
    """Tooltip text color in ``rgba`` format.

    :attr:`tooltip_text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    tooltip_text = StringProperty()
    """Tooltip text.

    :attr:`tooltip_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    _tooltip = None

    def delete_clock(self, widget, touch, *args):
        if self.collide_point(touch.x, touch.y) and touch.grab_current:
            try:
                Clock.unschedule(touch.ud["event"])
            except KeyError:
                pass
            self.on_leave()

    def adjust_tooltip_position(self, x, y):
        """Returns the coordinates of the tooltip
        that fit into the borders of the screen."""

        # If the position of the tooltip is outside the right border
        # of the screen.
        if x + self._tooltip.width > Window.width:
            x = Window.width - (self._tooltip.width + dp(10))
        else:
            # If the position of the tooltip is outside the left border
            # of the screen.
            if x < 0:
                x = "10dp"
        # If the tooltip position is below bottom the screen border.
        if y < 0:
            y = dp(10)
        # If the tooltip position is below top the screen border.
        else:
            if Window.height - self._tooltip.height < y:
                y = Window.height - (self._tooltip.height + dp(10))
        return x, y

    def display_tooltip(self, interval):
        if not self._tooltip:
            return
        Window.add_widget(self._tooltip)
        pos = self.to_window(self.center_x, self.center_y)
        x = pos[0] - self._tooltip.width / 2
        y = pos[1] - self._tooltip.height / 2 - self.height / 2 - dp(20)
        x, y = self.adjust_tooltip_position(x, y)
        self._tooltip.pos = (x, y)
        Clock.schedule_once(self.animation_tooltip_show, 0)

    def animation_tooltip_show(self, interval):
        if not self._tooltip:
            return
        (
            Animation(_scale_x=1, _scale_y=1, d=0.1)
            + Animation(opacity=1, d=0.2)
        ).start(self._tooltip)

    def remove_tooltip(self, *args):
        Window.remove_widget(self._tooltip)

    def on_long_touch(self, touch, *args):
        if DEVICE_TYPE != "desktop":
            self.on_enter(True)

    def on_enter(self, *args):
        """See
        :attr:`~kivymd.uix.behaviors.hover_behavior.HoverBehavior.on_enter`
        method in :class:`~kivymd.uix.behaviors.hover_behavior.HoverBehavior`
        class.
        """

        if not args and DEVICE_TYPE != "desktop":
            return
        else:
            if not self.tooltip_text:
                return
            self._tooltip = MDTooltipViewClass(
                tooltip_bg_color=self.tooltip_bg_color,
                tooltip_text_color=self.tooltip_text_color,
                tooltip_text=self.tooltip_text,
            )
            Clock.schedule_once(self.display_tooltip, -1)

    def on_leave(self):
        """See
        :attr:`~kivymd.uix.behaviors.hover_behavior.HoverBehavior.on_leave`
        method in :class:`~kivymd.uix.behaviors.hover_behavior.HoverBehavior`
        class.
        """

        if self._tooltip:
            Window.remove_widget(self._tooltip)
            self._tooltip = None


class MDTooltipViewClass(ThemableBehavior, BoxLayout):
    tooltip_bg_color = ListProperty()
    """
    See :attr:`~MDTooltip.tooltip_bg_color`.
    """

    tooltip_text_color = ListProperty()
    """
    See :attr:`~MDTooltip.tooltip_text_color`.
    """

    tooltip_text = StringProperty()
    """
    See :attr:`~MDTooltip.tooltip_text`.
    """

    _scale_x = NumericProperty(0)
    _scale_y = NumericProperty(0)
