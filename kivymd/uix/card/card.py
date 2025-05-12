"""
Components/Card
===============

.. seealso::

    `Material Design 3 spec, Cards <https://m3.material.io/components/cards/overview>`_

.. rubric:: Cards contain content and actions about a single subject.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/cards.png
    :align: center

`KivyMD` provides the following card classes for use:

- MDCard_
- MDCardSwipe_

.. note:: :class:`~MDCard` inherited from
    :class:`~kivy.uix.boxlayout.BoxLayout`. You can use all parameters and
    attributes of the :class:`~kivy.uix.boxlayout.BoxLayout` class in the
    :class:`~MDCard` class.

.. MDCard:

MDCard
------

There are three types of cards: elevated, filled, and outlined:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/available-cards.png
    :align: center

1. Elevated card
2. Filled card
3. Outlined card

Example
-------

.. tabs::

    .. tab:: Declarative KV and imperative python styles

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import StringProperty

            from kivymd.app import MDApp
            from kivymd.uix.card import MDCard

            KV = '''
            <MyCard>
                padding: "4dp"
                size_hint: None, None
                size: "240dp", "100dp"

                MDRelativeLayout:

                    MDIconButton:
                        icon: "dots-vertical"
                        pos_hint: {"top": 1, "right": 1}

                    MDLabel:
                        text: root.text
                        adaptive_size: True
                        color: "grey"
                        pos: "12dp", "12dp"
                        bold: True


            MDScreen:
                theme_bg_color: "Custom"
                md_bg_color: self.theme_cls.backgroundColor

                MDBoxLayout:
                    id: box
                    adaptive_size: True
                    spacing: "12dp"
                    pos_hint: {"center_x": .5, "center_y": .5}
            '''


            class MyCard(MDCard):
                '''Implements a material card.'''

                text = StringProperty()


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)

                def on_start(self):
                    for style in ("elevated", "filled", "outlined"):
                        self.root.ids.box.add_widget(
                            MyCard(style=style, text=style.capitalize())
                        )


            Example().run()

    .. tab:: Declarative python styles

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import MDIconButton
            from kivymd.uix.card import MDCard
            from kivymd.uix.label import MDLabel
            from kivymd.uix.relativelayout import MDRelativeLayout
            from kivymd.uix.screen import MDScreen


            class MyCard(MDCard):
                '''Implements a material card.'''


            class Example(MDApp):
                def build(self):
                    return (
                        MDScreen(
                            MDBoxLayout(
                                id="box",
                                adaptive_size=True,
                                spacing="12dp",
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                            ),
                            theme_bg_color="Custom",
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )

                def on_start(self):
                    for style in ("elevated", "filled", "outlined"):
                        self.root..get_ids().box.add_widget(
                            MyCard(
                                MDRelativeLayout(
                                    MDIconButton(
                                        icon="dots-vertical",
                                        pos_hint={"top": 1, "right": 1}
                                    ),
                                    MDLabel(
                                        text=style.capitalize(),
                                        adaptive_size=True,
                                        pos=("12dp", "12dp"),
                                    ),
                                ),
                                style=style,
                                padding="4dp",
                                size_hint=(None, None),
                                size=("240dp", "100dp"),
                                ripple_behavior=True,
                            )
                        )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/card-usage.png
    :align: center

Elevated
--------

.. code-block:: kv

    MDCard
        style: "elevated"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/card-elevated.png
    :align: center

Filled
------

.. code-block:: kv

    MDCard
        style: "filled"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/card-filled.png
    :align: center

Outlined
--------

.. code-block:: kv

    MDCard
        style: "outlined"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/card-outlined.png
    :align: center


Customization of card
=====================

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDCard:
                    style: "elevated"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    padding: "4dp"
                    size_hint: None, None
                    size: "240dp", "100dp"
                    # Sets custom properties.
                    theme_shadow_color: "Custom"
                    shadow_color: "green"
                    theme_bg_color: "Custom"
                    md_bg_color: "white"
                    md_bg_color_disabled: "grey"
                    theme_shadow_offset: "Custom"
                    shadow_offset: (1, -2)
                    theme_shadow_softness: "Custom"
                    shadow_softness: 1
                    theme_elevation_level: "Custom"
                    elevation_level: 2

                    RelativeLayout:

                        MDIconButton:
                            icon: "dots-vertical"
                            pos_hint: {"top": 1, "right": 1}

                        MDLabel:
                            text: "Elevated"
                            adaptive_size: True
                            color: "grey"
                            pos: "12dp", "12dp"
                            bold: True
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Green"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDIconButton
            from kivymd.uix.card import MDCard
            from kivymd.uix.label import MDLabel
            from kivymd.uix.relativelayout import MDRelativeLayout
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Green"
                    return (
                        MDScreen(
                            MDCard(
                                MDRelativeLayout(
                                    MDIconButton(
                                        icon="dots-vertical",
                                        pos_hint={"top": 1, "right": 1},
                                    ),
                                    MDLabel(
                                        text="Elevated",
                                        adaptive_size=True,
                                        color="grey",
                                        pos=("12dp", "12dp"),
                                        bold=True,
                                    ),
                                ),
                                style="elevated",
                                pos_hint={"center_x": .5, "center_y": .5},
                                padding="4dp",
                                size_hint=(None, None),
                                size=("240dp", "100dp"),
                                # Sets custom properties.
                                theme_shadow_color="Custom",
                                shadow_color="green",
                                theme_bg_color="Custom",
                                md_bg_color="white",
                                md_bg_color_disabled="grey",
                                theme_shadow_offset="Custom",
                                shadow_offset=(1, -2),
                                theme_shadow_softness="Custom",
                                shadow_softness=1,
                                theme_elevation_level="Custom",
                                elevation_level=2,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/card-customization.png
    :align: center

.. MDCardSwipe:

MDCardSwipe
-----------

To create a card with `swipe-to-delete` behavior, you must create a new class
that inherits from the :class:`~MDCardSwipe` class:


.. code-block:: kv

    <SwipeToDeleteItem>
        size_hint_y: None
        height: content.height

        MDCardSwipeLayerBox:

        MDCardSwipeFrontBox:

            OneLineListItem:
                id: content
                text: root.text
                _no_ripple_effect: True

.. code-block:: python

    class SwipeToDeleteItem(MDCardSwipe):
        text = StringProperty()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sceleton-mdcard-swiper.png
    :align: center

Example
-------

.. tabs::

    .. tab:: Declarative KV and imperative python styles

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import StringProperty

            from kivymd.app import MDApp
            from kivymd.uix.card import MDCardSwipe

            KV = '''
            <SwipeToDeleteItem>:
                size_hint_y: None
                height: content.height

                MDCardSwipeLayerBox:
                    padding: "8dp"

                    MDIconButton:
                        icon: "trash-can"
                        pos_hint: {"center_y": .5}
                        on_release: app.remove_item(root)

                MDCardSwipeFrontBox:

                    MDListItem:
                        id: content
                        ripple_effect: False

                        MDListItemSupportingText
                            text: root.text


            MDScreen:

                MDScrollView:

                    MDList:
                        id: md_list
                        padding: 0
            '''


            class SwipeToDeleteItem(MDCardSwipe):
                text = StringProperty()


            class Example(MDApp):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    self.screen = Builder.load_string(KV)

                def build(self):
                    return self.screen

                def remove_item(self, instance):
                    self.screen.ids.md_list.remove_widget(instance)

                def on_start(self):
                    for i in range(20):
                        self.screen.ids.md_list.add_widget(
                            SwipeToDeleteItem(text=f"One-line item {i}")
                        )


            Example().run()

    .. tab:: Declarative python styles

        .. code-block:: python

            from kivy.properties import StringProperty

            from kivymd.app import MDApp
            from kivymd.uix.button import MDIconButton
            from kivymd.uix.card import (
                MDCardSwipe, MDCardSwipeLayerBox, MDCardSwipeFrontBox
            )
            from kivymd.uix.list import MDList, MDListItem, MDListItemSupportingText
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.scrollview import MDScrollView


            class SwipeToDeleteItem(MDCardSwipe):
                text = StringProperty()


            class Example(MDApp):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"

                def build(self):
                    return (
                        MDScreen(
                            MDScrollView(
                                MDList(
                                    id="md_list",
                                    padding=10,
                                )
                            )
                        )
                    )

                def remove_item(self, instance):
                    self.root.get_ids().md_list.remove_widget(instance)

                def on_start(self):
                    for i in range(20):
                        swipe_to_delete_item = SwipeToDeleteItem(
                            MDCardSwipeLayerBox(
                                MDIconButton(
                                    id="trash_can",
                                    icon="trash-can",
                                    pos_hint={"center_y": 0.5},
                                ),
                            ),
                            MDCardSwipeFrontBox(
                                MDListItem(
                                    MDListItemSupportingText(
                                        text=f"One-line item {i}",
                                    ),
                                    id="content",
                                    ripple_effect=False,
                                ),
                            ),
                            size_hint_y=None,
                        )
                        trash_can = swipe_to_delete_item.get_ids().trash_can
                        trash_can.bind(
                            on_release=lambda x, y=swipe_to_delete_item: self.remove_item(y)
                        )
                        self.root.get_ids().md_list.add_widget(swipe_to_delete_item)
                        swipe_to_delete_item.height = swipe_to_delete_item.get_ids().content.height


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/list-mdcard-swipe.gif
    :align: center

Binding a swipe to one of the sides of the screen
-------------------------------------------------

.. code-block:: kv

    <SwipeToDeleteItem>
        # By default, the parameter is "left"
        anchor: "right"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/mdcard-swipe-anchor-right.gif
    :align: center


.. Note:: You cannot use the left and right swipe at the same time.

Swipe behavior
--------------

.. code-block:: kv

    <SwipeToDeleteItem>
        # By default, the parameter is "hand"
        type_swipe: "hand"  # "auto"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hand-mdcard-swipe.gif
    :align: center

Removing an item using the ``type_swipe = "auto"`` parameter
------------------------------------------------------------

The map provides the :attr:`MDCardSwipe.on_swipe_complete` event.
You can use this event to remove items from a list:

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: kv

            <SwipeToDeleteItem>:
                on_swipe_complete: app.on_swipe_complete(root)

    .. tab:: Declarative python styles

        .. code-block:: kv

            .. code-block:: python

                MDCardSwipe(
                    ...
                    on_swipe_complete=self.on_swipe_complete,
                )

.. tabs::

    .. tab:: Imperative python styles

        .. code-block:: python

            def on_swipe_complete(self, instance):
                self.root.ids.md_list.remove_widget(instance)

    .. tab:: Decralative python styles

        .. code-block:: python

            def on_swipe_complete(self, instance):
                self.root.get_ids().md_list.remove_widget(instance)

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/auto-mdcard-swipe.gif
    :align: center


Add content to the bottom layer of the card
-------------------------------------------

To add content to the bottom layer of the card,
use the :class:`~MDCardSwipeLayerBox` class.

.. code-block:: kv

    <SwipeToDeleteItem>:

        MDCardSwipeLayerBox:
            padding: "8dp"

            MDIconButton:
                icon: "trash-can"
                pos_hint: {"center_y": .5}
                on_release: app.remove_item(root)

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/mdcard-swipe-content.png
    :align: center
"""

from __future__ import annotations

__all__ = (
    "MDCard",
    "MDCardSwipe",
    "MDCardSwipeFrontBox",
    "MDCardSwipeLayerBox",
)

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    CommonElevationBehavior,
    DeclarativeBehavior,
    RectangularRippleBehavior,
)
from kivymd.uix.behaviors.state_layer_behavior import StateLayerBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout

with open(
    os.path.join(uix_path, "card", "card.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read(), filename="MDCard.kv")


class MDCard(
    DeclarativeBehavior,
    MDAdaptiveWidget,
    ThemableBehavior,
    BackgroundColorBehavior,
    CommonElevationBehavior,
    RectangularRippleBehavior,
    StateLayerBehavior,
    ButtonBehavior,
    BoxLayout,
):
    """
    Card class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.uix.MDAdaptiveWidget` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout` and
    classes documentation.
    """

    ripple_behavior = BooleanProperty(False)
    """
    Use ripple effect for card.

    :attr:`ripple_behavior` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    radius = VariableListProperty([dp(16), dp(16), dp(16), dp(16)])
    """
    Card radius by default.

    .. versionadded:: 1.0.0

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(16), dp(16), dp(16), dp(16)]`.
    """

    style = OptionProperty("filled", options=("filled", "elevated", "outlined"))
    """
    Card type.

    .. versionadded:: 1.0.0

    Available options are: 'filled', 'elevated', 'outlined'.

    :attr:`style` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the card when
    the card is disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(
            lambda x: self.on_ripple_behavior(0, self.ripple_behavior)
        )

    def on_press(self, *args) -> None:
        """Fired when the button is pressed."""

        self._on_press(args)

    def on_release(self, *args) -> None:
        """
        Fired when the button is released
        (i.e. the touch/click that pressed the button goes away).
        """

        self._on_release(args)

    def on_ripple_behavior(self, interval: int | float, value: bool) -> None:
        """Fired when the :attr:`ripple_behavior` value changes."""

        self.ripple_effect = not self.ripple_effect

    def set_properties_widget(self) -> None:
        """Fired `on_release/on_press/on_enter/on_leave` events."""

        super().set_properties_widget()

        if not self.disabled:
            if self._state == self.state_hover and self.focus_behavior:
                self._elevation_level = self.elevation_level
                self._shadow_softness = self.shadow_softness
                self._bg_color = self.md_bg_color

                if self.style in ["filled", "outlined"]:
                    if self.theme_elevation_level == "Primary":
                        self.elevation_level = 0
                    if self.theme_shadow_softness == "Primary":
                        self.shadow_softness = 0
                else:
                    if self.theme_elevation_level == "Primary":
                        self.elevation_level = 2
                    if self.theme_shadow_softness == "Primary":
                        self.shadow_softness = dp(4)
                    if self.theme_shadow_offset == "Primary":
                        self.shadow_offset = [0, -2]
            elif self._state == self.state_press:
                if self.theme_elevation_level == "Primary":
                    self.elevation_level = 1
                if self.theme_shadow_softness == "Primary":
                    self.shadow_softness = 0
            elif not self._state:
                if self.theme_elevation_level == "Primary":
                    self.elevation_level = 1
                if self.theme_shadow_softness == "Primary":
                    self.shadow_softness = 0
                if self.theme_shadow_offset == "Primary":
                    self.shadow_offset = [0, -2]
                self.md_bg_color = self._bg_color


class MDCardSwipe(MDRelativeLayout):
    """
    Card swipe class.

    For more information, see in the
    :class:`~kivymd.uix.relativelayout.MDRelativeLayout` class documentation.

    :Events:
        :attr:`on_swipe_complete`
            Fired when a swipe of card is completed.
    """

    open_progress = NumericProperty(0.0)
    """
    Percent of visible part of side panel. The percent is specified as a
    floating point number in the range 0-1. 0.0 if panel is closed and 1.0 if
    panel is opened.

    :attr:`open_progress` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.0`.
    """

    opening_transition = StringProperty("out_cubic")
    """
    The name of the animation transition type to use when animating to
    the :attr:`state` `'opened'`.

    :attr:`opening_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    closing_transition = StringProperty("out_sine")
    """
    The name of the animation transition type to use when animating to
    the :attr:`state` 'closed'.

    :attr:`closing_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_sine'`.
    """

    closing_interval = NumericProperty(0)
    """
    Interval for closing the front layer.

    .. versionadded:: 1.1.0

    :attr:`closing_interval` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    anchor = OptionProperty("left", options=("left", "right"))
    """
    Anchoring screen edge for card. Available options are: `'left'`, `'right'`.

    :attr:`anchor` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `left`.
    """

    swipe_distance = NumericProperty(50)
    """
    The distance of the swipe with which the movement of navigation drawer
    begins.

    :attr:`swipe_distance` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `50`.
    """

    opening_time = NumericProperty(0.2)
    """
    The time taken for the card to slide to the :attr:`state` `'open'`.

    :attr:`opening_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    state = OptionProperty("closed", options=("closed", "opened"))
    """
    Detailed state. Sets before :attr:`state`. Bind to :attr:`state` instead
    of :attr:`status`. Available options are: `'closed'`,  `'opened'`.

    :attr:`status` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'closed'`.
    """

    max_swipe_x = NumericProperty(0.3)
    """
    If, after the events of :attr:`~on_touch_up` card position exceeds this
    value - will automatically execute the method :attr:`~open_card`,
    and if not - will automatically be :attr:`~close_card` method.

    :attr:`max_swipe_x` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.3`.
    """

    max_opened_x = NumericProperty("100dp")
    """
    The value of the position the card shifts to when :attr:`~type_swipe`
    s set to `'hand'`.

    :attr:`max_opened_x` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `100dp`.
    """

    type_swipe = OptionProperty("hand", options=("auto", "hand"))
    """
    Type of card opening when swipe. Shift the card to the edge or to
    a set position :attr:`~max_opened_x`. Available options are:
    `'auto'`, `'hand'`.

    :attr:`type_swipe` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `auto`.
    """

    _opens_process = False
    _to_closed = True
    _distance = 0

    __events__ = ("on_swipe_complete",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_swipe_complete(self, *args):
        """Fired when a swipe of card is completed."""

    def on_anchor(
        self, instance_swipe_to_delete_item, anchor_value: str
    ) -> None:
        """Fired when the value of :attr:`anchor` changes."""

        if anchor_value == "right":
            self.open_progress = 1.0
        else:
            self.open_progress = 0.0

    def on_open_progress(
        self, instance_swipe_to_delete_item, progress_value: float
    ) -> None:
        """Fired when the value of :attr:`open_progress` changes."""

        def on_open_progress(*args):
            if self.anchor == "left":
                self.children[0].x = self.width * progress_value
            else:
                self.children[0].x = self.width * progress_value - self.width

        Clock.schedule_once(on_open_progress)

    def on_touch_move(self, touch):
        if self.collide_point(touch.x, touch.y):
            self._distance += touch.dx
            expr = False

            if self.anchor == "left" and touch.dx >= 0:
                expr = abs(self._distance) < self.swipe_distance
            elif self.anchor == "right" and touch.dx < 0:
                expr = abs(self._distance) > self.swipe_distance

            if expr and not self._opens_process:
                self._opens_process = True
                self._to_closed = False
            if self._opens_process:
                self.open_progress = max(
                    min(self.open_progress + touch.dx / self.width, 2.5), 0
                )
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        self._distance = 0
        if self.collide_point(touch.x, touch.y):
            if not self._to_closed:
                self._opens_process = False
                self._complete_swipe()
        return super().on_touch_up(touch)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            if self.state == "opened":
                self._to_closed = True
                Clock.schedule_once(self.close_card, self.closing_interval)
        return super().on_touch_down(touch)

    def open_card(self) -> None:
        """Animates the opening of the card."""

        if self.type_swipe == "hand":
            swipe_x = (
                self.max_opened_x
                if self.anchor == "left"
                else -self.max_opened_x
            )
        else:
            swipe_x = self.width if self.anchor == "left" else 0
        anim = Animation(
            x=swipe_x, t=self.opening_transition, d=self.opening_time
        )
        anim.bind(on_complete=self._on_swipe_complete)
        anim.start(self.children[0])
        self.state = "opened"

    def close_card(self, *args) -> None:
        """Animates the closing of the card."""

        anim = Animation(x=0, t=self.closing_transition, d=self.opening_time)
        anim.bind(on_complete=self._reset_open_progress)
        anim.start(self.children[0])
        self.state = "closed"

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, (MDCardSwipeFrontBox, MDCardSwipeLayerBox)):
            return super().add_widget(widget)

    def _complete_swipe(self) -> None:
        expr = (
            self.open_progress <= self.max_swipe_x
            if self.anchor == "left"
            else self.open_progress >= self.max_swipe_x
        )
        if expr:
            Clock.schedule_once(self.close_card, self.closing_interval)
        else:
            self.open_card()

    def _on_swipe_complete(self, *args):
        self.dispatch("on_swipe_complete")

    def _reset_open_progress(self, *args):
        self.open_progress = 0.0 if self.anchor == "left" else 1.0
        self._to_closed = False
        self.dispatch("on_swipe_complete")


class MDCardSwipeFrontBox(MDCard):
    """
    Card swipe front box.

    For more information, see in the :class:`~MDCard` class documentation.
    """


class MDCardSwipeLayerBox(MDBoxLayout):
    """
    Card swipe back box.

    For more information, see in the :class:`~kivymd.uix.boxlayout.MDBoxLayout`
    class documentation.
    """
