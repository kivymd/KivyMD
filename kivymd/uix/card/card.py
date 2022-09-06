"""
Components/Card
===============

.. seealso::

    `Material Design spec, Cards <https://material.io/components/cards>`_ and
    `Material Design 3 spec, Cards <https://m3.material.io/components/cards/specs>`_

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

An example of the implementation of a card in the style of material design version 3
------------------------------------------------------------------------------------

.. tabs::

    .. tab:: Declarative KV and imperative python styles

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import StringProperty

            from kivymd.app import MDApp
            from kivymd.uix.card import MDCard

            KV = '''
            <MD3Card>
                padding: 4
                size_hint: None, None
                size: "200dp", "100dp"

                MDRelativeLayout:

                    MDIconButton:
                        icon: "dots-vertical"
                        pos_hint: {"top": 1, "right": 1}

                    MDLabel:
                        id: label
                        text: root.text
                        adaptive_size: True
                        color: "grey"
                        pos: "12dp", "12dp"
                        bold: True


            MDScreen:

                MDBoxLayout:
                    id: box
                    adaptive_size: True
                    spacing: "56dp"
                    pos_hint: {"center_x": .5, "center_y": .5}
            '''


            class MD3Card(MDCard):
                '''Implements a material design v3 card.'''

                text = StringProperty()


            class Example(MDApp):
                def build(self):
                    self.theme_cls.material_style = "M3"
                    return Builder.load_string(KV)

                def on_start(self):
                    styles = {
                        "elevated": "#f6eeee", "filled": "#f4dedc", "outlined": "#f8f5f4"
                    }
                    for style in styles.keys():
                        self.root.ids.box.add_widget(
                            MD3Card(
                                line_color=(0.2, 0.2, 0.2, 0.8),
                                style=style,
                                text=style.capitalize(),
                                md_bg_color=styles[style],
                            )
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


            class MD3Card(MDCard):
                '''Implements a material design v3 card.'''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.material_style = "M3"
                    return (
                        MDScreen(
                            MDBoxLayout(
                                id="box",
                                adaptive_size=True,
                                spacing="56dp",
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                            )
                        )
                    )

                def on_start(self):
                    styles = {
                        "elevated": "#f6eeee", "filled": "#f4dedc", "outlined": "#f8f5f4"
                    }
                    for style in styles.keys():
                        self.root.ids.box.add_widget(
                            MD3Card(
                                MDRelativeLayout(
                                    MDIconButton(
                                        icon="dots-vertical",
                                        pos_hint={"top": 1, "right": 1}
                                    ),
                                    MDLabel(
                                        text=style.capitalize(),
                                        adaptive_size=True,
                                        color="grey",
                                        pos=("12dp", "12dp"),
                                    ),
                                ),
                                line_color=(0.2, 0.2, 0.2, 0.8),
                                style=style,
                                padding="4dp",
                                size_hint=(None, None),
                                size=("200dp", "100dp"),
                                md_bg_color=styles[style],
                            )
                        )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/cards-m3.png
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

End full code
-------------

.. tabs::

    .. tab:: Declarative KV and imperative python styles

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import StringProperty

            from kivymd.app import MDApp
            from kivymd.uix.card import MDCardSwipe

            KV = '''
            <SwipeToDeleteItem>
                size_hint_y: None
                height: content.height

                MDCardSwipeLayerBox:
                    # Content under the card.

                MDCardSwipeFrontBox:

                    # Content of card.
                    OneLineListItem:
                        id: content
                        text: root.text
                        _no_ripple_effect: True


            MDScreen:

                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        elevation: 4
                        title: "MDCardSwipe"

                    MDScrollView:
                        scroll_timeout : 100

                        MDList:
                            id: md_list
                            padding: 0
            '''


            class SwipeToDeleteItem(MDCardSwipe):
                '''Card with `swipe-to-delete` behavior.'''

                text = StringProperty()


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)

                def on_start(self):
                    '''Creates a list of cards.'''

                    for i in range(20):
                        self.root.ids.md_list.add_widget(
                            SwipeToDeleteItem(text=f"One-line item {i}")
                        )


            Example().run()

    .. tab:: Declarative python styles

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.card import (
                MDCardSwipe, MDCardSwipeLayerBox, MDCardSwipeFrontBox
            )
            from kivymd.uix.list import MDList, OneLineListItem
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.scrollview import MDScrollView
            from kivymd.uix.toolbar import MDTopAppBar


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDBoxLayout(
                                MDTopAppBar(
                                    elevation=4,
                                    title="MDCardSwipe",
                                ),
                                MDScrollView(
                                    MDList(
                                        id="md_list",
                                    ),
                                    id="scroll",
                                    scroll_timeout=100,
                                ),
                                id="box",
                                orientation="vertical",
                            ),
                        )
                    )

                def on_start(self):
                    '''Creates a list of cards.'''

                    for i in range(20):
                        self.root.ids.box.ids.scroll.ids.md_list.add_widget(
                            MDCardSwipe(
                                MDCardSwipeLayerBox(),
                                MDCardSwipeFrontBox(
                                    OneLineListItem(
                                        id="content",
                                        text=f"One-line item {i}",
                                        _no_ripple_effect=True,
                                    )
                                ),
                                size_hint_y=None,
                                height="52dp",
                            )
                        )


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
        type_swipe: "hand"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hand-mdcard-swipe.gif
    :align: center

.. code-block:: kv

    <SwipeToDeleteItem>:
        type_swipe: "auto"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/auto-mdcard-swipe.gif
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
                self.root.ids.box.ids.scroll.ids.md_list.remove_widget(instance)

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/autodelete-mdcard-swipe.gif
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

End full code
-------------

.. tabs::

    .. tab:: Declarative KV styles

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

                    OneLineListItem:
                        id: content
                        text: root.text
                        _no_ripple_effect: True


            MDScreen:

                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        elevation: 4
                        title: "MDCardSwipe"

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

    .. tab:: Decralative python styles

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import MDIconButton
            from kivymd.uix.card import (
                MDCardSwipe, MDCardSwipeLayerBox, MDCardSwipeFrontBox
            )
            from kivymd.uix.list import MDList, OneLineListItem
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.scrollview import MDScrollView
            from kivymd.uix.toolbar import MDTopAppBar


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDBoxLayout(
                                MDTopAppBar(
                                    elevation=4,
                                    title="MDCardSwipe",
                                ),
                                MDScrollView(
                                    MDList(
                                        id="md_list",
                                    ),
                                    id="scroll",
                                    scroll_timeout=100,
                                ),
                                id="box",
                                orientation="vertical",
                            ),
                        )
                    )

                def on_start(self):
                    '''Creates a list of cards.'''

                    for i in range(20):
                        self.root.ids.box.ids.scroll.ids.md_list.add_widget(
                            MDCardSwipe(
                                MDCardSwipeLayerBox(
                                    MDIconButton(
                                        icon="trash-can",
                                        pos_hint={"center_y": 0.5},
                                        on_release=self.remove_item,
                                    ),
                                ),
                                MDCardSwipeFrontBox(
                                    OneLineListItem(
                                        id="content",
                                        text=f"One-line item {i}",
                                        _no_ripple_effect=True,
                                    )
                                ),
                                size_hint_y=None,
                                height="52dp",
                            )
                        )

                def remove_item(self, instance):
                    self.root.ids.box.ids.scroll.ids.md_list.remove_widget(
                        instance.parent.parent
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/handdelete-mdcard-swipe.gif
    :align: center

Focus behavior
--------------

.. code-block:: kv

    MDCard:
        focus_behavior: True

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDCard:
                    size_hint: .7, .4
                    focus_behavior: True
                    pos_hint: {"center_x": .5, "center_y": .5}
                    md_bg_color: "darkgrey"
                    unfocus_color: "darkgrey"
                    focus_color: "grey"
                    elevation: 6
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python styles

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.card import  MDCard
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDCard(
                                size_hint=(0.7, 0.4),
                                focus_behavior=True,
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                                md_bg_color="darkgrey",
                                unfocus_color="darkgrey",
                                focus_color="grey",
                                elevation=6,
                            ),
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/card-focus.gif
    :align: center

Ripple behavior
---------------

.. code-block:: kv

    MDCard:
        ripple_behavior: True

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/card-behavior.gif
    :align: center

"""

__all__ = (
    "MDCard",
    "MDCardSwipe",
    "MDCardSwipeFrontBox",
    "MDCardSwipeLayerBox",
    "MDSeparator",
)

import os
from typing import Union

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
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex

from kivymd import uix_path
from kivymd.color_definitions import colors
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    CommonElevationBehavior,
    DeclarativeBehavior,
    RectangularRippleBehavior,
)
from kivymd.uix.behaviors.focus_behavior import FocusBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout

with open(
    os.path.join(uix_path, "card", "card.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSeparator(ThemableBehavior, MDBoxLayout):
    """A separator line."""

    color = ColorProperty(None)
    """
    Separator color.

    :attr:`color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_orientation()

    def on_orientation(self, *args) -> None:
        self.size_hint = (
            (1, None) if self.orientation == "horizontal" else (None, 1)
        )
        if self.orientation == "horizontal":
            self.height = dp(1)
        else:
            self.width = dp(1)


class MDCard(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    RectangularRippleBehavior,
    CommonElevationBehavior,
    FocusBehavior,
    BoxLayout,
):
    focus_behavior = BooleanProperty(False)
    """
    Using focus when hovering over a card.

    :attr:`focus_behavior` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    ripple_behavior = BooleanProperty(False)
    """
    Use ripple effect for card.

    :attr:`ripple_behavior` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    radius = VariableListProperty([dp(6), dp(6), dp(6), dp(6)])
    """
    Card radius by default.

    .. versionadded:: 1.0.0

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(6), dp(6), dp(6), dp(6)]`.
    """

    style = OptionProperty(None, options=("filled", "elevated", "outlined"))
    """
    Card type.

    .. versionadded:: 1.0.0

    Available options are: 'filled', 'elevated', 'outlined'.

    :attr:`style` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'elevated'`.
    """

    _bg_color_map = (
        get_color_from_hex(colors["Light"]["CardsDialogs"]),
        get_color_from_hex(colors["Dark"]["CardsDialogs"]),
        [1.0, 1.0, 1.0, 0.0],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_cls.bind(
            material_style=self.set_style, theme_style=self.update_md_bg_color
        )
        Clock.schedule_once(self.set_style)
        Clock.schedule_once(
            lambda x: self.on_ripple_behavior(0, self.ripple_behavior)
        )
        self.update_md_bg_color(self, self.theme_cls.theme_style)

    def update_md_bg_color(self, instance_card, theme_style: str) -> None:
        if self.md_bg_color in self._bg_color_map:
            self.md_bg_color = get_color_from_hex(
                colors[theme_style]["CardsDialogs"]
            )

    def set_style(self, *args) -> None:
        self.set_radius()
        self.set_elevation()
        self.set_line_color()

    def set_line_color(self) -> None:
        if self.theme_cls.material_style == "M3":
            if self.style == "elevated" or self.style == "filled":
                self.line_color = [0, 0, 0, 0]

    def set_elevation(self) -> None:
        if self.theme_cls.material_style == "M3":
            if self.style == "outlined" or self.style == "filled":
                self.elevation = 0
            elif self.style == "elevated":
                self.elevation = 2

    def set_radius(self) -> None:
        if (
            self.radius == [dp(6), dp(6), dp(6), dp(6)]
            and self.theme_cls.material_style == "M3"
        ):
            self.radius = [dp(16), dp(16), dp(16), dp(16)]
        elif (
            self.radius == [dp(16), dp(16), dp(16), dp(16)]
            and self.theme_cls.material_style == "M2"
        ):
            self.radius = [dp(6), dp(6), dp(6), dp(6)]

    def on_ripple_behavior(
        self, interval: Union[int, float], value_behavior: bool
    ) -> None:
        self._no_ripple_effect = False if value_behavior else True


class MDCardSwipe(MDRelativeLayout):
    """
    :Events:
        :attr:`on_swipe_complete`
            Called when a swipe of card is completed.
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

    def __init__(self, *args, **kwargs):
        self.register_event_type("on_swipe_complete")
        super().__init__(*args, **kwargs)

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, (MDCardSwipeFrontBox, MDCardSwipeLayerBox)):
            return super().add_widget(widget)

    def on_swipe_complete(self, *args):
        """Called when a swipe of card is completed."""

    def on_anchor(
        self, instance_swipe_to_delete_item, anchor_value: str
    ) -> None:
        if anchor_value == "right":
            self.open_progress = 1.0
        else:
            self.open_progress = 0.0

    def on_open_progress(
        self, instance_swipe_to_delete_item, progress_value: float
    ) -> None:
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
                self.complete_swipe()
        return super().on_touch_up(touch)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            if self.state == "opened":
                self._to_closed = True
                Clock.schedule_once(self.close_card, self.closing_interval)
        return super().on_touch_down(touch)

    def complete_swipe(self) -> None:
        expr = (
            self.open_progress <= self.max_swipe_x
            if self.anchor == "left"
            else self.open_progress >= self.max_swipe_x
        )
        if expr:
            Clock.schedule_once(self.close_card, self.closing_interval)
        else:
            self.open_card()

    def open_card(self) -> None:
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
        anim = Animation(x=0, t=self.closing_transition, d=self.opening_time)
        anim.bind(on_complete=self._reset_open_progress)
        anim.start(self.children[0])
        self.state = "closed"

    def _on_swipe_complete(self, *args):
        self.dispatch("on_swipe_complete")

    def _reset_open_progress(self, *args):
        self.open_progress = 0.0 if self.anchor == "left" else 1.0
        self._to_closed = False
        self.dispatch("on_swipe_complete")


class MDCardSwipeFrontBox(MDCard):
    pass


class MDCardSwipeLayerBox(MDBoxLayout):
    pass
