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

Example
-------

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

        MDToolbar:
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
"""

__all__ = ("MDSelectionList",)

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ObjectProperty,
    NumericProperty,
    StringProperty,
    ListProperty,
    ColorProperty
)

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import MDList
from kivymd.uix.relativelayout import MDRelativeLayout

Builder.load_string(
    """
<SelectionIconCheck>
    theme_text_color: "Custom"
    text_color: self.icon_check_color

    canvas.before:
        PushMatrix
        Scale:
            x: root.scale
            y: root.scale
            z: root.scale
            origin: self.center
    canvas.after:
        PopMatrix


<SelectionItem>
    md_bg_color: root.overlay_color if root.selected else (0, 0, 0, 0)

    canvas:
        Color:
            rgba:
                ( \
                self.theme_cls.primary_color \
                if not root.selected_round_color \
                else root.selected_round_color \
                ) \
                if root._progress_animation else \
                (0, 0, 0, 0)
        Ellipse:
            size: self.selected_round_size, self.selected_round_size
            pos:
                self.instance_item.center_x - self.selected_round_size / 2, \
                self.instance_item.center_y - self.selected_round_size / 2
        Color:
            rgba:
                self.theme_cls.primary_color[:-1] + [.3] \
                if not root.selected_round_color \
                else root.selected_round_color[:-1] + [.3]
        SmoothLine:
            width: dp(4)
            circle:
                self.instance_item.center_x, \
                self.instance_item.center_y, \
                self.selected_round_size * 0.58, \
                0, root._progress_line_end
"""
)


class SelectionIconCheck(MDIconButton):
    scale = NumericProperty(0)
    icon_check_color = ColorProperty([1, 1, 1, 1])


class SelectionItem(ThemableBehavior, MDRelativeLayout, TouchBehavior):
    selected = BooleanProperty(False)
    owner = ObjectProperty()
    instance_item = ObjectProperty()
    instance_icon = ObjectProperty()
    overlay_color = ColorProperty([0, 0, 0, 0.2])
    selected_round_size = NumericProperty(dp(46))
    selected_round_color = ColorProperty(None)

    _progress_round = NumericProperty(0)
    _progress_line_end = NumericProperty(0)
    _progress_animation = BooleanProperty(False)
    _touch_long = BooleanProperty(False)

    def do_selected_item(self, *args):
        Animation(scale=1, d=0.2).start(self.instance_icon)
        self.selected = True
        self._progress_animation = False
        self.owner.dispatch("on_selected", self)

    def do_unselected_item(self):
        Animation(scale=0, d=0.2).start(self.instance_icon)
        self.selected = False
        self.owner.dispatch("on_unselected", self)

    def reset_progress_animation(self):
        Animation.cancel_all(self)
        self._progress_animation = False

    def on_long_touch(self, *args):
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

    def on__touch_long(self, instance, value):
        if not value:
            self.reset_progress_animation()

    def on__progress_animation(self, instance, value):
        if value:
            anim = Animation(_progress_line_end=360, d=1, t="in_out_quad")
            anim.bind(on_complete=self.do_selected_item)
            anim.start(self)
        else:
            self._progress_line_end = 0


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

    icon_check_color = ColorProperty([1, 1, 1, 1])
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

    selected_round_size = NumericProperty(dp(46))
    """
    Size of the spinner for switching of `selected_mode` mode.

    :attr:`selected_round_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(46)`.
    """

    selected_round_color = ColorProperty(None)
    """
    Color of the spinner for switching of `selected_mode` mode.

    :attr:`selected_round_color` is an :class:`~kivy.properties.NumericProperty`
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
            selected_round_size=self.selected_round_size,
            selected_round_color=self.selected_round_color,
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

    def get_selected(self):
        selected = False
        for item in self.children:
            if item.selected:
                selected = True
                break
        return selected

    def get_selected_list_items(self):
        selected_list_items = []
        for item in self.children:
            if item.selected:
                selected_list_items.append(item)
        return selected_list_items

    def unselected_all(self):
        for item in self.children:
            item.do_unselected_item()
        self.selected_mode = False

    def selected_all(self):
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
