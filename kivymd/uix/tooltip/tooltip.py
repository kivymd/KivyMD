"""
Components/Tooltip
==================

.. seealso::

    `Material Design spec, Tooltips <https://m3.material.io/components/tooltips/specs>`_

.. rubric:: Tooltips display brief labels or messages.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tooltip-m3-preview.png
    :align: center

- Use tooltips to add additional context to a button or other UI element
- Two types: plain and rich
- Use plain tooltips to describe elements or actions of icon buttons
- Use rich tooltips to provide more details, like describing the value of a feature
- Rich tooltips can include an optional title, link, and buttons

**KivyMD provides two types of tooltip:**

1. Plain tooltip
2. Rich tooltip

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tooltip-m3-type.png
    :align: center

Usage of tooltip plain
----------------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty

    from kivymd.uix.button import MDButton
    from kivymd.uix.tooltip import MDTooltip
    from kivymd.app import MDApp

    KV = '''
    <YourTooltipClass>

        MDTooltipPlain:
            text:
                "Grant value is calculated using the closing stock price \\\\n" \\
                "from the day before the grant date. Amounts do not \\\\n" \\
                "reflect tax witholdings."


    <TooltipMDIconButton>

        MDButtonText:
            text: root.text


    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        TooltipMDIconButton:
            text: "Tooltip button"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class YourTooltipClass(MDTooltip):
        '''Implements your tooltip base class.'''


    class TooltipMDIconButton(YourTooltipClass, MDButton):
        '''Implements a button with tooltip behavior.'''

        text = StringProperty()


    class Example(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Olive"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tooltip-m3-plain-usage.gif
    :align: center

The anatomy of a plain tooltip
------------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tooltip-m3-plain-anatomy.png
    :align: center

Usage of tooltip rich
---------------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty

    from kivymd.uix.button import MDButton
    from kivymd.uix.tooltip import MDTooltip
    from kivymd.app import MDApp

    KV = '''
    <YourTooltipClass>

        MDTooltipRich:
            id: tooltip
            auto_dismiss: False

            MDTooltipRichSubhead:
                text: "Add others"

            MDTooltipRichSupportingText:
                text:
                    "Grant value is calculated using the closing stock price \\\\n" \\
                    "from the day before the grant date. Amounts do not \\\\n" \\
                    "reflect tax witholdings."

            MDTooltipRichActionButton:
                on_press: tooltip.dismiss()

                MDButtonText:
                    text: "Learn more"


    <TooltipMDIconButton>

        MDButtonText:
            text: root.text


    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        TooltipMDIconButton:
            text: "Tooltip button"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class YourTooltipClass(MDTooltip):
        '''Implements your tooltip base class.'''


    class TooltipMDIconButton(YourTooltipClass, MDButton):
        '''Implements a button with tooltip behavior.'''

        text = StringProperty()


    class Example(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Olive"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tooltip-m3-rich-usage.gif
    :align: center

The anatomy of a plain tooltip
------------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tooltip-m3-rich-anatomy.png
    :align: center
"""

__all__ = (
    "MDTooltip",
    "MDTooltipPlain",
    "MDTooltipRich",
    "MDTooltipRichActionButton",
    "MDTooltipRichSubhead",
    "MDTooltipRichSupportingText",
)

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BoundedNumericProperty,
    NumericProperty,
    BooleanProperty,
)
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.behaviors.state_layer_behavior import StateLayerBehavior
from kivymd.uix.button import MDButton
from kivymd.uix.label import MDLabel
from kivymd import uix_path
from kivymd.material_resources import DEVICE_TYPE
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    TouchBehavior,
    ScaleBehavior,
    DeclarativeBehavior,
    BackgroundColorBehavior,
    CommonElevationBehavior,
)

with open(
    os.path.join(uix_path, "tooltip", "tooltip.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDTooltip(TouchBehavior):
    """
    Tooltip class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.touch_behavior.TouchBehavior`
    class documentation.

    :Events:
        `on_open`:
            Fired when the tooltip opens.
        `on_dismiss`:
            Fired when the tooltip is closed.
    """

    tooltip_display_delay = BoundedNumericProperty(0, min=0, max=4)
    """
    Tooltip display delay.
    
    .. note:: This property only works on desktop.

    :attr:`tooltip_display_delay` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `0`, min of `0` & max of `4`.
    """

    shift_y = NumericProperty()
    """
    Y-offset of tooltip to the top.

    :attr:`shift_y` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    shift_right = NumericProperty()
    """
    Shifting the tooltip to the right.

    .. versionadded:: 1.0.0

    :attr:`shift_right` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    shift_left = NumericProperty()
    """
    Shifting the tooltip to the left.

    .. versionadded:: 1.0.0

    :attr:`shift_left` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    _tooltip = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_dismiss")

    def delete_clock(self, widget, touch, *args):
        if self.collide_point(touch.x, touch.y) and touch.grab_current:
            try:
                Clock.unschedule(touch.ud["event"])
            except KeyError:
                pass
            self.on_leave()

    def adjust_tooltip_position(self) -> tuple:
        """
        Returns the coordinates of the tooltip that fit into the borders
        of the screen.
        """

        pos = self.to_window(self.center_x, self.center_y)
        if not self.shift_right and not self.shift_left:
            x = pos[0] - (self._tooltip.width / 2)
        else:
            if self.shift_right:
                x = pos[0] - (self._tooltip.width / 2) + self.shift_right
            if self.shift_left:
                x = pos[0] - (self._tooltip.width / 2) - self.shift_left

        if not self.shift_y:
            y = pos[1] - (self._tooltip.height + self.height)
        else:
            y = pos[1] - self._tooltip.height / 2 - self.height + self.shift_y

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

    def display_tooltip(self, *args) -> None:
        """Adds a tooltip widget to the screen and animates its display."""

        if not self._tooltip or self._tooltip.parent:
            return

        Window.add_widget(self._tooltip)
        x, y = self.adjust_tooltip_position()
        self._tooltip.pos = (x, y)

        if DEVICE_TYPE == "desktop":
            Clock.schedule_once(
                self.animation_tooltip_show, self.tooltip_display_delay
            )
        else:
            Clock.schedule_once(self.animation_tooltip_show, 0)

    def animation_tooltip_show(self, *args) -> None:
        """Animation of opening tooltip on the screen."""

        if self._tooltip:
            self._tooltip.shadow_color = self._tooltip.theme_cls.shadowColor
            (
                Animation(scale_value_x=1, scale_value_y=1, d=0.2)
                + Animation(opacity=1, d=0.2)
            ).start(self._tooltip)
            self.dispatch("on_open")

    def animation_tooltip_dismiss(self, *args) -> None:
        """
        Animation of closing tooltip on the screen.

        .. versionadded:: 1.0.0
        """

        if self._tooltip:
            self._tooltip.shadow_color = (
                self._tooltip.theme_cls.transparentColor
            )
            anim = Animation(
                scale_value_x=0, scale_value_y=0, d=0.2
            ) + Animation(opacity=0, d=0.2)
            anim.bind(on_complete=self._on_dismiss_anim_complete)
            anim.start(self._tooltip)

    def remove_tooltip(self, *args) -> None:
        """Removes the tooltip widget from the screen."""

        Window.remove_widget(self._tooltip)

    def add_widget(self, widget, *args, **kwargs):
        """Add a new widget as a child of this widget."""

        if isinstance(widget, (MDTooltipPlain, MDTooltipRich)):
            self._tooltip = widget
            widget._tooltip = self
        else:
            return super().add_widget(widget)

    def on_long_touch(self, touch, *args) -> None:
        if DEVICE_TYPE != "desktop":
            Clock.schedule_once(self.display_tooltip, -1)
            Clock.schedule_once(
                self.animation_tooltip_show, self.tooltip_display_delay
            )

    def on_enter(self, *args) -> None:
        """Fired when mouse enter the bbox of the widget."""

        super().on_enter()

        if DEVICE_TYPE == "desktop":
            if self._tooltip:
                self.remove_tooltip()

            Clock.schedule_once(self.display_tooltip, 0.2)

    def on_leave(self, *args) -> None:
        """Fired when the mouse goes outside the widget border."""

        super().on_leave()

        if self._tooltip and (
            not isinstance(self._tooltip, MDTooltipRich)
            or self._tooltip.auto_dismiss
        ):
            Clock.schedule_once(self.animation_tooltip_dismiss)

    def on_open(self) -> None:
        """
        Default display event handler.

        .. versionchanged:: 2.0.0 Rename from `on_show` to `on_open`.
        """

    def on_dismiss(self) -> None:
        """
        Default dismiss event handler.

        .. versionadded:: 1.0.0
        """

    def _on_dismiss_anim_complete(self, *args):
        self.dispatch("on_dismiss")
        self.remove_tooltip()
        # self._tooltip = None

    def _on_release(self, *args):
        ...


class MDTooltipPlain(MDLabel, ScaleBehavior):
    """
    Tooltip plain class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` and
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior`
    classes documentation.
    """


class MDTooltipRichSupportingText(MDLabel):
    """
    Implements supporting text for the :class:`~MDTooltipRich` class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """


class MDTooltipRichSubhead(MDLabel):
    """
    Implements subhead text for the :class:`~MDTooltipRich` class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """


class MDTooltipRichActionButton(MDButton):
    """
    Implements action button for the :class:`~MDTooltipRich` class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.button.button.MDButton` class documentation.
    """

    # Override methods.
    # Their functionality is not needed in this class.

    def _set_state_layer_color(self) -> None:
        ...

    def on_enter(self) -> None:
        ...

    def on_leave(self) -> None:
        ...


class MDTooltipRich(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    CommonElevationBehavior,
    ScaleBehavior,
    StateLayerBehavior,
    BoxLayout,
):
    """
    Tooltip rich class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    :class:`~kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout` and
    classes documentation.
    """

    auto_dismiss = BooleanProperty(True)
    """
    This property determines if the view is automatically dismissed when
    the cursor goes outside of the tooltip body.

    :attr:`auto_dismiss` is a :class:`~kivy.properties.BooleanProperty` and
    defaults to True.
    """

    _tooltip = None

    def on_leave(self) -> None:
        """Fired when the mouse goes outside the widget border."""

        super().on_leave()

        if self._tooltip:
            Clock.schedule_once(self._tooltip.animation_tooltip_dismiss)

    def dismiss(self) -> None:
        """Hides the tooltip."""

        self.on_leave()
