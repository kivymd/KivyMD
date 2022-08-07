"""
Components/Selection
====================

.. seealso::

    `Material Design spec, Banner <https://material.io/design/interaction/selection.html>`_

.. rubric:: Selection refers to how users indicate specific items they intend to take action on.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/selection-previous.png
    :align: center

Entering selection mode
-----------------------

To select an item and enter selection mode, long press the item:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/enter-selection-mode.gif
    :align: center

Exiting selection mode
----------------------

To exit selection mode, tap each selected item until they’re all deselected:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/exit-selection-mode.gif
    :align: center

Larger selections
-----------------

.. note:: This feature is missing yet.

Events
------

.. code-block:: python

    def on_selected(self, instance_selection_list, instance_selection_item):
        '''Called when a list item is selected.'''

    def on_unselected(self, instance_selection_list, instance_selection_item):
        '''Called when a list item is unselected.'''

Example with TwoLineAvatarListItem
----------------------------------

.. code-block:: python

    from kivy.animation import Animation
    from kivy.lang import Builder
    from kivy.utils import get_color_from_hex

    from kivymd.app import MDApp
    from kivymd.uix.list import TwoLineAvatarListItem

    KV = '''
    <MyItem>
        text: "Two-line item with avatar"
        secondary_text: "Secondary text here"
        _no_ripple_effect: True

        ImageLeftWidget:
            source: "data/logo/kivy-icon-256.png"


    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            id: toolbar
            title: "Inbox"
            left_action_items: [["menu"]]
            right_action_items: [["magnify"], ["dots-vertical"]]
            md_bg_color: 0, 0, 0, 1

        MDBoxLayout:
            padding: "24dp", "8dp", 0, "8dp"
            adaptive_size: True

            MDLabel:
                text: "Today"
                adaptive_size: True

        ScrollView:

            MDSelectionList:
                id: selection_list
                spacing: "12dp"
                overlay_color: app.overlay_color[:-1] + [.2]
                icon_bg_color: app.overlay_color
                on_selected: app.on_selected(*args)
                on_unselected: app.on_unselected(*args)
                on_selected_mode: app.set_selection_mode(*args)
    '''


    class MyItem(TwoLineAvatarListItem):
        pass


    class Example(MDApp):
        overlay_color = get_color_from_hex("#6042e4")

        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for i in range(10):
                self.root.ids.selection_list.add_widget(MyItem())

        def set_selection_mode(self, instance_selection_list, mode):
            if mode:
                md_bg_color = self.overlay_color
                left_action_items = [
                    [
                        "close",
                        lambda x: self.root.ids.selection_list.unselected_all(),
                    ]
                ]
                right_action_items = [["trash-can"], ["dots-vertical"]]
            else:
                md_bg_color = (0, 0, 0, 1)
                left_action_items = [["menu"]]
                right_action_items = [["magnify"], ["dots-vertical"]]
                self.root.ids.toolbar.title = "Inbox"

            Animation(md_bg_color=md_bg_color, d=0.2).start(self.root.ids.toolbar)
            self.root.ids.toolbar.left_action_items = left_action_items
            self.root.ids.toolbar.right_action_items = right_action_items

        def on_selected(self, instance_selection_list, instance_selection_item):
            self.root.ids.toolbar.title = str(
                len(instance_selection_list.get_selected_list_items())
            )

        def on_unselected(self, instance_selection_list, instance_selection_item):
            if instance_selection_list.get_selected_list_items():
                self.root.ids.toolbar.title = str(
                    len(instance_selection_list.get_selected_list_items())
                )


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/selection-example-with-listItem.gif
    :align: center

Example with FitImage
---------------------

.. code-block:: python

    from kivy.animation import Animation
    from kivy.lang import Builder
    from kivy.properties import ColorProperty

    from kivymd.app import MDApp
    from kivymd.uix.fitimage import FitImage

    KV = '''
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: app.theme_cls.bg_light

        MDTopAppBar:
            id: toolbar
            title: "Inbox"
            left_action_items: [["menu"]]
            right_action_items: [["magnify"], ["dots-vertical"]]
            md_bg_color: app.theme_cls.bg_light
            specific_text_color: 0, 0, 0, 1

        MDBoxLayout:
            padding: "24dp", "8dp", 0, "8dp"
            adaptive_size: True

            MDLabel:
                text: "Today"
                adaptive_size: True

        ScrollView:

            MDSelectionList:
                id: selection_list
                padding: "24dp", 0, "24dp", "24dp"
                cols: 3
                spacing: "12dp"
                overlay_color: app.overlay_color[:-1] + [.2]
                icon_bg_color: app.overlay_color
                progress_round_color: app.progress_round_color
                on_selected: app.on_selected(*args)
                on_unselected: app.on_unselected(*args)
                on_selected_mode: app.set_selection_mode(*args)
    '''


    class Example(MDApp):
        overlay_color = ColorProperty("#6042e4")
        progress_round_color = "#ef514b"

        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for i in range(10):
                self.root.ids.selection_list.add_widget(
                    FitImage(
                        source="image.png",
                        size_hint_y=None,
                        height="240dp",
                    )
                )

        def set_selection_mode(self, instance_selection_list, mode):
            if mode:
                md_bg_color = self.overlay_color
                left_action_items = [
                    [
                        "close",
                        lambda x: self.root.ids.selection_list.unselected_all(),
                    ]
                ]
                right_action_items = [["trash-can"], ["dots-vertical"]]
            else:
                md_bg_color = (1, 1, 1, 1)
                left_action_items = [["menu"]]
                right_action_items = [["magnify"], ["dots-vertical"]]
                self.root.ids.toolbar.title = "Inbox"

            Animation(md_bg_color=md_bg_color, d=0.2).start(self.root.ids.toolbar)
            self.root.ids.toolbar.left_action_items = left_action_items
            self.root.ids.toolbar.right_action_items = right_action_items

        def on_selected(self, instance_selection_list, instance_selection_item):
            self.root.ids.toolbar.title = str(
                len(instance_selection_list.get_selected_list_items())
            )

        def on_unselected(self, instance_selection_list, instance_selection_item):
            if instance_selection_list.get_selected_list_items():
                self.root.ids.toolbar.title = str(
                    len(instance_selection_list.get_selected_list_items())
                )


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/selection-example-with-fitimage.gif
    :align: center
"""

__all__ = ("MDSelectionList",)

import os
from typing import Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import (
    Ellipse,
    RoundedRectangle,
    SmoothLine,
)
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import MDList
from kivymd.uix.relativelayout import MDRelativeLayout

with open(
    os.path.join(uix_path, "selection", "selection.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class SelectionIconCheck(MDIconButton):
    """Implements the icon for the checked item."""

    scale = NumericProperty(0)
    icon_check_color = ColorProperty([0, 0, 0, 1])


class SelectionItem(ThemableBehavior, MDRelativeLayout, TouchBehavior):
    selected = BooleanProperty(False)
    """
    Whether or not an item is checked.

    :attr:`selected` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    owner = ObjectProperty()
    """
    Instance of :class:`~kivymd.uix.selection.MDSelectionList` class.

    :attr:`owner` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    instance_item = ObjectProperty()
    """
    User item. Must be a Kivy or KivyMD widget.

    :attr:`instance_item` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    instance_icon = ObjectProperty()
    """
    Instance of :class:`~kivymd.uix.selection.SelectionIconCheck` class.

    :attr:`instance_icon` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    overlay_color = ColorProperty([0, 0, 0, 0.2])
    """See :attr:`~MDSelectionList.overlay_color`."""

    progress_round_size = NumericProperty(dp(46))
    """See :attr:`~MDSelectionList.progress_round_size`."""

    progress_round_color = ColorProperty(None)
    """See :attr:`~MDSelectionList.progress_round_color`."""

    _progress_round = NumericProperty(0)
    _progress_line_end = NumericProperty(0)
    _progress_animation = BooleanProperty(False)
    _touch_long = BooleanProperty(False)
    _instance_progress_inner_circle_color = ObjectProperty()
    _instance_progress_inner_circle_ellipse = ObjectProperty()
    _instance_progress_inner_outer_color = ObjectProperty()
    _instance_progress_inner_outer_line = ObjectProperty()
    _instance_overlay_color = ObjectProperty()
    _instance_overlay_rounded_rec = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_progress_round)

    def set_progress_round(self, interval: Union[int, float]) -> None:
        with self.canvas.after:
            self._instance_progress_inner_circle_color = Color(
                rgba=(0, 0, 0, 0)
            )
            self._instance_progress_inner_circle_ellipse = Ellipse(
                size=self.get_progress_round_size(),
                pos=self.get_progress_round_pos(),
            )
            self.bind(
                pos=self.update_progress_inner_circle_ellipse,
                size=self.update_progress_inner_circle_ellipse,
            )
            # FIXME: Radius value is not displayed.
            self._instance_overlay_color = Color(rgba=(0, 0, 0, 0))
            self._instance_overlay_rounded_rec = RoundedRectangle(
                size=self.size,
                pos=self.pos,
                radius=self.instance_item.radius
                if hasattr(self.instance_item, "radius")
                else [
                    0,
                ],
            )
            self.bind(
                pos=self.update_overlay_rounded_rec,
                size=self.update_overlay_rounded_rec,
            )
            self._instance_progress_inner_outer_color = Color(rgba=(0, 0, 0, 0))
            self._instance_progress_inner_outer_line = SmoothLine(
                width=dp(4),
                circle=[
                    self.center_x,
                    self.center_y,
                    self.progress_round_size * 0.58,
                    0,
                    0,
                ],
            )

    def do_selected_item(self, *args) -> None:
        Animation(scale=1, d=0.2).start(self.instance_icon)
        self.selected = True
        self._progress_animation = False
        self._instance_overlay_color.rgba = self.get_overlay_color()
        self.owner.dispatch("on_selected", self)

    def do_unselected_item(self) -> None:
        Animation(scale=0, d=0.2).start(self.instance_icon)
        self.selected = False
        self._instance_overlay_color.rgba = self.get_overlay_color()
        self.owner.dispatch("on_unselected", self)

    def do_animation_progress_line(
        self, animation: Animation, instance_selection_item, value: float
    ) -> None:
        self._instance_progress_inner_outer_line.circle = (
            self.center_x,
            self.center_y,
            self.progress_round_size * 0.58,
            0,
            360 * value,
        )

    def update_overlay_rounded_rec(self, *args) -> None:
        self._instance_overlay_rounded_rec.size = self.size
        self._instance_overlay_rounded_rec.pos = self.pos

    def update_progress_inner_circle_ellipse(self, *args) -> None:
        self._instance_progress_inner_circle_ellipse.size = (
            self.get_progress_round_size()
        )
        self._instance_progress_inner_circle_ellipse.pos = (
            self.get_progress_round_pos()
        )

    def reset_progress_animation(self) -> None:
        Animation.cancel_all(self)
        self._progress_animation = False
        self._instance_progress_inner_circle_color.rgba = (0, 0, 0, 0)
        self._instance_progress_inner_outer_color.rgba = (0, 0, 0, 0)
        self._instance_progress_inner_outer_line.circle = [
            self.center_x,
            self.center_y,
            self.progress_round_size * 0.58,
            0,
            0,
        ]
        self._progress_line_end = 0

    def get_overlay_color(self) -> list:
        return self.overlay_color if self.selected else (0, 0, 0, 0)

    def get_progress_round_pos(self) -> tuple:
        return (
            (self.pos[0] + self.width / 2) - self.progress_round_size / 2,
            self.center_y - self.progress_round_size / 2,
        )

    def get_progress_round_size(self) -> tuple:
        return self.progress_round_size, self.progress_round_size

    def get_progress_round_color(self) -> tuple:
        return (
            self.theme_cls.primary_color
            if not self.progress_round_color
            else self.progress_round_color
        )

    def get_progress_line_color(self) -> tuple:
        return (
            self.theme_cls.primary_color[:-1] + [0.5]
            if not self.progress_round_color
            else self.progress_round_color[:-1] + [0.5]
        )

    def on_long_touch(self, *args) -> None:
        if not self.owner.get_selected():
            self._touch_long = True
            self._progress_animation = True

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            if self._touch_long:
                self._touch_long = False
        return super().on_touch_up(touch)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.selected:
                self.do_unselected_item()
            else:
                if self.owner.selected_mode:
                    self.do_selected_item()
        return super().on_touch_down(touch)

    def on__touch_long(self, instance_selection_tem, touch_value: bool) -> None:
        if not touch_value:
            self.reset_progress_animation()

    def on__progress_animation(
        self, instance_selection_tem, touch_value: bool
    ) -> None:
        if touch_value:
            anim = Animation(_progress_line_end=360, d=1, t="in_out_quad")
            anim.bind(
                on_progress=self.do_animation_progress_line,
                on_complete=self.do_selected_item,
            )
            anim.start(self)
            self._instance_progress_inner_outer_color.rgba = (
                self.get_progress_line_color()
            )
            self._instance_progress_inner_circle_color.rgba = (
                self.get_progress_round_color()
            )
        else:
            self.reset_progress_animation()


class MDSelectionList(MDList):
    """
    :Events:
        `on_selected`
            Called when a list item is selected.
        `on_unselected`
            Called when a list item is unselected.
    """

    selected_mode = BooleanProperty(False)
    """
    List item selection mode. If `True` when clicking on a list item, it will
    be selected.

    :attr:`selected_mode` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    icon = StringProperty("check")
    """
    Name of the icon with which the selected list item will be marked.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'check'`.
    """

    icon_pos = ListProperty()
    """
    The position of the icon that will mark the selected list item.

    :attr:`icon_pos` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    icon_bg_color = ColorProperty([1, 1, 1, 1])
    """
    Background color of the icon that will mark the selected list item.

    :attr:`icon_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 1]`.
    """

    icon_check_color = ColorProperty([0, 0, 0, 1])
    """
    Color of the icon that will mark the selected list item.

    :attr:`icon_check_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 1]`.
    """

    overlay_color = ColorProperty([0, 0, 0, 0.2])
    """
    The overlay color of the selected list item..

    :attr:`overlay_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.2]]`.
    """

    progress_round_size = NumericProperty(dp(46))
    """
    Size of the spinner for switching of `selected_mode` mode.

    :attr:`progress_round_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(46)`.
    """

    progress_round_color = ColorProperty(None)
    """
    Color of the spinner for switching of `selected_mode` mode.

    :attr:`progress_round_color` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_selected")
        self.register_event_type("on_unselected")

    def add_widget(self, widget, index=0, canvas=None):
        selection_icon = SelectionIconCheck(
            icon=self.icon,
            md_bg_color=self.icon_bg_color,
            icon_check_color=self.icon_check_color,
        )
        container = SelectionItem(
            size_hint=(1, None),
            height=widget.height,
            instance_item=widget,
            instance_icon=selection_icon,
            overlay_color=self.overlay_color,
            progress_round_size=self.progress_round_size,
            progress_round_color=self.progress_round_color,
            owner=self,
        )
        container.add_widget(widget)

        if not self.icon_pos:
            pos = (
                dp(12),
                container.height / 2 - selection_icon.height / 2,
            )
        else:
            pos = self.icon_pos
        selection_icon.pos = pos
        container.add_widget(selection_icon)
        return super().add_widget(container, index, canvas)

    def get_selected(self) -> bool:
        """Returns ``True`` if at least one item in the list is checked."""

        selected = False
        for item in self.children:
            if item.selected:
                selected = True
                break
        return selected

    def get_selected_list_items(self) -> list:
        """
        Returns a list of marked objects:

        [<kivymd.uix.selection.SelectionItem object>, ...]
        """

        selected_list_items = []
        for item in self.children:
            if item.selected:
                selected_list_items.append(item)
        return selected_list_items

    def unselected_all(self) -> None:
        for item in self.children:
            item.do_unselected_item()
        self.selected_mode = False

    def selected_all(self) -> None:
        for item in self.children:
            item.do_selected_item()
        self.selected_mode = True

    def on_selected(self, *args):
        """Called when a list item is selected."""

        if not self.selected_mode:
            self.selected_mode = True

    def on_unselected(self, *args):
        """Called when a list item is unselected."""

        self.selected_mode = self.get_selected()
