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

.. Warning:: :class:`~MDTooltip` only works correctly with button and label classes.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    <TooltipMDIconButton@MDIconButton+MDTooltip>


    MDScreen:

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
    `click here <https://github.com/kivymd/KivyMD/wiki/Components-Tooltips>`_.
"""

__all__ = ("MDTooltip", "MDTooltipViewClass")

import os
from typing import NoReturn, Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BoundedNumericProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.boxlayout import BoxLayout

from kivymd import uix_path
from kivymd.font_definitions import theme_font_styles
from kivymd.material_resources import DEVICE_TYPE
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import HoverBehavior, TouchBehavior

with open(
    os.path.join(uix_path, "tooltip", "tooltip.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDTooltip(ThemableBehavior, HoverBehavior, TouchBehavior):
    tooltip_bg_color = ColorProperty(None)
    """
    Tooltip background color in ``rgba`` format.

    :attr:`tooltip_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    tooltip_text_color = ColorProperty(None)
    """
    Tooltip text color in ``rgba`` format.

    :attr:`tooltip_text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    tooltip_text = StringProperty()
    """
    Tooltip text.

    :attr:`tooltip_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    tooltip_font_style = OptionProperty("Caption", options=theme_font_styles)
    """
    Tooltip font style. Available options are: `'H1'`, `'H2'`, `'H3'`, `'H4'`,
    `'H5'`, `'H6'`, `'Subtitle1'`, `'Subtitle2'`, `'Body1'`, `'Body2'`,
    `'Button'`, `'Caption'`, `'Overline'`, `'Icon'`.

    :attr:`tooltip_font_style` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Caption'`.
    """

    tooltip_radius = ListProperty(
        [
            dp(7),
        ]
    )
    """
    Corner radius values.

    :attr:`radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(7),]`.
    """

    tooltip_display_delay = BoundedNumericProperty(0, min=0, max=4)
    """
    Tooltip dsiplay delay.

    :attr:`tooltip_display_delay` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `0`, min of `0` & max of `4`. This property only works on desktop.
    """

    shift_y = NumericProperty()
    """
    Y-offset of tooltip text.

    :attr:`shift_y` is an :class:`~kivy.properties.StringProperty`
    and defaults to `0`.
    """

    _tooltip = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_show")
        self.register_event_type("on_dismiss")

    def delete_clock(self, widget, touch, *args):
        if self.collide_point(touch.x, touch.y) and touch.grab_current:
            try:
                Clock.unschedule(touch.ud["event"])
            except KeyError:
                pass
            self.on_leave()

    def adjust_tooltip_position(self, x: float, y: float) -> tuple:
        """
        Returns the coordinates of the tooltip that fit into the borders of the
        screen.
        """

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

    def display_tooltip(self, interval: Union[int, float]) -> NoReturn:
        if not self._tooltip:
            return
        Window.add_widget(self._tooltip)
        pos = self.to_window(self.center_x, self.center_y)
        x = pos[0] - self._tooltip.width / 2

        if not self.shift_y:
            y = pos[1] - self._tooltip.height / 2 - self.height / 2 - dp(20)
        else:
            y = pos[1] - self._tooltip.height / 2 - self.height + self.shift_y

        x, y = self.adjust_tooltip_position(x, y)
        self._tooltip.pos = (x, y)

        if DEVICE_TYPE == "desktop":
            Clock.schedule_once(
                self.animation_tooltip_show, self.tooltip_display_delay
            )
        else:
            Clock.schedule_once(self.animation_tooltip_show, 0)

    def animation_tooltip_show(self, interval: Union[int, float]) -> NoReturn:
        """Animation of opening tooltip on the screen."""

        if self._tooltip:
            (
                Animation(_scale_x=1, _scale_y=1, d=0.1)
                + Animation(opacity=1, d=0.2)
            ).start(self._tooltip)
            self.dispatch("on_show")

    def animation_tooltip_dismiss(
        self, interval: Union[int, float]
    ) -> NoReturn:
        """
        .. versionadded:: 1.0.0

        Animation of closing tooltip on the screen.
        """

        if self._tooltip:
            anim = Animation(_scale_x=0, _scale_y=0, d=0.1) + Animation(
                opacity=0, d=0.2
            )
            anim.bind(on_complete=self._on_dismiss_anim_complete)
            anim.start(self._tooltip)

    def remove_tooltip(self, *args) -> NoReturn:
        """Removes the tooltip widget from the screen."""

        Window.remove_widget(self._tooltip)

    def on_long_touch(self, touch, *args) -> NoReturn:
        if DEVICE_TYPE != "desktop":
            self.on_enter(True)

    def on_enter(self, *args) -> NoReturn:
        """
        See
        :attr:`~kivymd.uix.behaviors.hover_behavior.HoverBehavior.on_enter`
        method in :class:`~kivymd.uix.behaviors.hover_behavior.HoverBehavior`
        class.
        """

        if not args and DEVICE_TYPE == "desktop":
            if self.tooltip_text:
                self._tooltip = MDTooltipViewClass(
                    tooltip_bg_color=self.tooltip_bg_color,
                    tooltip_text_color=self.tooltip_text_color,
                    tooltip_text=self.tooltip_text,
                    tooltip_font_style=self.tooltip_font_style,
                    tooltip_radius=self.tooltip_radius,
                )
                Clock.schedule_once(self.display_tooltip, -1)

    def on_leave(self) -> NoReturn:
        """
        See
        :attr:`~kivymd.uix.behaviors.hover_behavior.HoverBehavior.on_leave`
        method in :class:`~kivymd.uix.behaviors.hover_behavior.HoverBehavior`
        class.
        """

        if self._tooltip:
            Clock.schedule_once(self.animation_tooltip_dismiss)

    def on_show(self) -> NoReturn:
        """Default dismiss event handler."""

    def on_dismiss(self) -> NoReturn:
        """
        .. versionadded:: 1.0.0

        Default dismiss event handler.
        """

    def _on_dismiss_anim_complete(self, *args):
        self.dispatch("on_dismiss")
        self.remove_tooltip()
        self._tooltip = None


class MDTooltipViewClass(ThemableBehavior, BoxLayout):
    tooltip_bg_color = ColorProperty(None)
    """
    See :attr:`~MDTooltip.tooltip_bg_color`.
    """

    tooltip_text_color = ColorProperty(None)
    """
    See :attr:`~MDTooltip.tooltip_text_color`.
    """

    tooltip_text = StringProperty()
    """
    See :attr:`~MDTooltip.tooltip_text`.
    """

    tooltip_font_style = OptionProperty("Caption", options=theme_font_styles)
    """
    See :attr:`~MDTooltip.tooltip_font_style`.
    """

    tooltip_radius = ListProperty()
    """
    See :attr:`~MDTooltip.tooltip_radius`.
    """

    _scale_x = NumericProperty(0)
    _scale_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = [
            dp(8) if DEVICE_TYPE == "desktop" else dp(16),
            dp(4),
            dp(8) if DEVICE_TYPE == "desktop" else dp(16),
            dp(4),
        ]
