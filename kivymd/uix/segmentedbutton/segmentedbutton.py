"""
Components/SegmentedButton
==========================

.. versionadded:: 1.2.0

.. seealso::

    `Material Design spec, Segmented buttons <https://m3.material.io/components/segmented-buttons/overview>`_

    `Segmented control <https://kivymd.readthedocs.io/en/latest/components/segmentedcontrol/>`_

.. rubric:: Segmented buttons help people select options, switch views,
    or sort elements.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-preview.png
    :align: center

Usage
-----

.. code-block:: kv

    MDScreen:

        MDSegmentedButton:

            MDSegmentedButtonItem:
                icon: ...
                text: ...

            MDSegmentedButtonItem:
                icon: ...
                text: ...

            MDSegmentedButtonItem:
                icon: ...
                text: ...

Example
-------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:

        MDSegmentedButton:
            pos_hint: {"center_x": .5, "center_y": .5}

            MDSegmentedButtonItem:
                text: "Walking"

            MDSegmentedButtonItem:
                text: "Transit"

            MDSegmentedButtonItem:
                text: "Driving"
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

By default, segmented buttons support single marking of elements:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-multiselect-false.gif
    :align: center

For multiple marking of elements, use the
:attr:`kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButton.multiselect`
parameter:

.. code-block:: kv

    MDSegmentedButton:
        multiselect: True

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-multiselect-true.gif
    :align: center

Control width
-------------

The width of the panel of segmented buttons will be equal to the width
of the texture of the widest button multiplied by the number of buttons:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-width-by-default.png
    :align: center

But you can use the `size_hint_x` parameter to specify the relative width:

.. code-block:: kv

    MDSegmentedButton:
        size_hint_x: .9

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-width-size-hint-x.png
    :align: center

Customization
-------------

You can see below in the documentation from which classes the
:class:`~kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButton` and
:class:`~kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButtonItem`
classes are inherited and use all their attributes such as
`md_bg_color`, `md_bg_color` etc. for additional customization of segments.

Events
------

- on_marked
    The method is called when a segment is marked.

- on_unmarked
    The method is called when a segment is unmarked.

.. code-block:: kv

    MDSegmentedButton:
        on_marked: app.on_marked(*args)

.. code-block:: python

    def on_marked(
        self,
        segment_button: MDSegmentedButton,
        segment_item: MDSegmentedButtonItem,
        marked: bool,
    ) -> None:
        print(segment_button)
        print(segment_item)
        print(marked)

A practical example
-------------------

.. code-block:: python

    import os

    from faker import Faker

    from kivy.clock import Clock
    from kivy.lang import Builder
    from kivy.properties import StringProperty

    from kivymd.app import MDApp
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.uix.segmentedbutton import MDSegmentedButton, MDSegmentedButtonItem
    from kivymd.utils import asynckivy

    KV = '''
    <UserCard>
        adaptive_height: True
        md_bg_color: "#343930"
        radius: 16

        TwoLineAvatarListItem:
            id: item
            divider: None
            _no_ripple_effect: True
            text: root.name
            secondary_text: root.path_to_file
            theme_text_color: "Custom"
            text_color: "#8A8D79"
            secondary_theme_text_color: self.theme_text_color
            secondary_text_color: self.text_color
            on_size:
                self.ids._left_container.size = (item.height, item.height)
                self.ids._left_container.x = dp(6)
                self._txt_right_pad = item.height + dp(12)

            ImageLeftWidget:
                source: root.album
                radius: root.radius


    MDScreen:
        md_bg_color: "#151514"

        MDBoxLayout:
            orientation: "vertical"
            padding: "12dp"
            spacing: "12dp"

            MDLabel:
                adaptive_height: True
                text: "Your downloads"
                font_style: "H5"
                theme_text_color: "Custom"
                text_color: "#8A8D79"

            MDSegmentedButton:
                size_hint_x: 1
                selected_color: "#303A29"
                line_color: "#343930"
                on_marked: app.on_marked(*args)

                MDSegmentedButtonItem:
                    text: "Songs"
                    active: True

                MDSegmentedButtonItem:
                    text: "Albums"

                MDSegmentedButtonItem:
                    text: "Podcasts"

            RecycleView:
                id: card_list
                viewclass: "UserCard"
                bar_width: 0

                RecycleBoxLayout:
                    orientation: 'vertical'
                    spacing: "16dp"
                    padding: "16dp"
                    default_size: None, dp(72)
                    default_size_hint: 1, None
                    size_hint_y: None
                    height: self.minimum_height
    '''


    class UserCard(MDBoxLayout):
        name = StringProperty()
        path_to_file = StringProperty()
        album = StringProperty()


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)

        def on_marked(
            self,
            segment_button: MDSegmentedButton,
            segment_item: MDSegmentedButtonItem,
            marked: bool,
        ) -> None:
            self.generate_card()

        def generate_card(self):
            async def generate_card():
                for i in range(10):
                    await asynckivy.sleep(0)
                    self.root.ids.card_list.data.append(
                        {
                            "name": fake.name(),
                            "path_to_file": f"{os.path.splitext(fake.file_path())[0]}.mp3",
                            "album": fake.image_url(),
                        }
                    )

            fake = Faker()
            self.root.ids.card_list.data = []
            Clock.schedule_once(lambda x: asynckivy.start(generate_card()))


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-practical-example.gif
    :align: center
"""

from __future__ import annotations

__all__ = ("MDSegmentedButton", "MDSegmentedButtonItem")

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior

from kivymd import uix_path
from kivymd.uix.behaviors import RectangularRippleBehavior, ScaleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDIcon

with open(
    os.path.join(uix_path, "segmentedbutton", "segmentedbutton.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSegmentedButtonItem(
    RectangularRippleBehavior, ButtonBehavior, MDFloatLayout
):
    """
    Segment button item.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.RectangularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.boxlayout.MDBoxLayout`
    class documentation.
    """

    icon = StringProperty()
    """
    Icon segment.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    text = StringProperty()
    """
    Text segment.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    active = BooleanProperty(False)
    """
    Background color of an disabled segment.

    :attr:`active` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    disabled_color = ColorProperty(None)
    """
    Is active segment.

    :attr:`active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _no_ripple_effect = BooleanProperty(True)
    _current_icon = ""
    _current_md_bg_color = None

    def on_disabled(self, instance, value: bool) -> None:
        def on_disabled(*args):
            if value:
                if not self._current_md_bg_color:
                    self._current_md_bg_color = self.md_bg_color
                self.md_bg_color = (
                    self.theme_cls.disabled_hint_text_color
                    if not self.disabled_color
                    else self.disabled_color
                )
            else:
                if self._current_md_bg_color:
                    self.md_bg_color = self._current_md_bg_color
                    self._current_md_bg_color = None

        Clock.schedule_once(on_disabled)

    def on_icon(self, instance, icon_name: str):
        if icon_name != "check":
            self._current_icon = icon_name


# TODO:
#  Add the feature to use both text and icons in segments -
#      https://m3.material.io/components/segmented-buttons/guidelines#26abac1c-c6bd-44c1-a969-8c910c880b98
#  Icons: optional check icon to indicate selected state -
#      https://m3.material.io/components/segmented-buttons/overview#7b80f313-7d3a-4865-b26c-1f7ec98ba694
#  Hovered: add a color for the hovered segment -
#      https://m3.material.io/components/segmented-buttons/specs#d730b3ba-c59e-4ef8-b652-20979fe20b67
#  Density: Each step down in density removes 4dp from the height -
#      https://m3.material.io/components/segmented-buttons/specs#2d5cab36-1deb-40bd-9e37-bc2bb1657009


class MDSegmentedButton(MDBoxLayout):
    """
    Segment button panel.

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` class documentation.

    :Events:
        `on_marked`
            The method is called when a segment is marked.
        `on_unmarked`
            The method is called when a segment is unmarked.
    """

    radius = VariableListProperty([20], length=4)
    """
    Panel radius.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[20, 20, 20, 20]`.
    """

    multiselect = BooleanProperty(False)
    """
    Do I allow multiple segment selection.

    :attr:`multiselect` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    hiding_icon_transition = StringProperty("linear")
    """
    Name of the transition hiding the current icon.

    :attr:`hiding_icon_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'linear'`.
    """

    hiding_icon_duration = NumericProperty(0.05)
    """
    Duration of hiding the current icon.

    :attr:`hiding_icon_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.05`.
    """

    opening_icon_transition = StringProperty("linear")
    """
    The name of the transition that opens a new icon of the "marked" type.

    :attr:`opening_icon_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'linear'`.
    """

    opening_icon_duration = NumericProperty(0.05)
    """
    The duration of opening a new icon of the "marked" type.

    :attr:`opening_icon_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.05`.
    """

    selected_items = ListProperty()
    """
    The list of :class:`~MDSegmentedButtonItem` objects that are currently
    marked.

    :attr:`selected_items` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    selected_color = ColorProperty(None)
    """
    Color of the marked segment.

    :attr:`selected_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_marked")
        self.register_event_type("on_unmarked")
        Clock.schedule_once(self.mark_segment)
        Clock.schedule_once(self.adjust_segment_radius)
        Clock.schedule_once(self.adjust_segment_panel_width, 2)

    def mark_segment(self, *args) -> None:
        """Programmatically marks a segment."""

        for widget in self.children:
            if widget.active:
                widget.active = False
                widget.dispatch("on_release")

                if not self.multiselect:
                    break

    def adjust_segment_radius(self, *args) -> None:
        """Rounds off the first and last elements."""

        if self.children[0].radius == [0, 0, 0, 0]:
            self.children[0].radius = (0, self.height / 2, self.height / 2, 0)
        if self.children[-1].radius == [0, 0, 0, 0]:
            self.children[-1].radius = (self.height / 2, 0, 0, self.height / 2)

    def adjust_segment_panel_width(self, *args) -> None:
        """
        Sets the width of all segments and the width of the panel
        by the widest segment.
        """

        if not self.size_hint_x:
            width_list = [
                widget.ids.label_text.texture_size[0]
                + (dp(72) if widget.icon else dp(48))
                for widget in self.children
            ]
            max_width = max(width_list)
            self.width = max_width * len(width_list)
        else:
            max_width = self.width / len(self.children)

        for widget in self.children:
            widget.width = max_width

        self.opacity = 1

        for widget in self.children:
            if widget.active:
                widget.dispatch("on_release")

    def shift_segment_text(self, segment_item: MDSegmentedButtonItem) -> None:
        """
        Shifts the segment text to the right, thus freeing up space
        for the icon (when the segment is marked).
        """

        Animation(
            x=(
                segment_item.ids.label_text.x
                + (
                    dp(16)
                    if not segment_item.icon and not segment_item.active
                    else 0
                )
            )
            if not segment_item.active
            else (
                segment_item.ids.label_text.x
                - (
                    dp(16)
                    if not segment_item.icon and segment_item.active
                    else 0
                )
            ),
            d=0.2,
        ).start(segment_item.ids.label_text)

    def show_icon_marked_segment(
        self, segment_item: MDSegmentedButtonItem
    ) -> None:
        """
        Sets the icon for the marked segment and changes the icon scale
        to the normal scale.
        """

        segment_item.ids.scale_icon.icon = "check"
        if segment_item.ids.scale_icon.icon == "check" and segment_item.active:
            segment_item.ids.scale_icon.icon = segment_item._current_icon

        Animation(
            scale_value_x=1,
            scale_value_y=1,
            d=self.opening_icon_duration,
            t=self.opening_icon_transition,
        ).start(segment_item.ids.scale_icon)

        self.shift_segment_text(segment_item)
        self.set_selected_segment_list(segment_item)
        self.set_bg_marked_segment(segment_item)

    def hide_icon_marked_segment(
        self, segment_item: MDSegmentedButtonItem
    ) -> None:
        """Changes the scale of the icon of the marked segment to zero."""

        anim = Animation(
            scale_value_x=0,
            scale_value_y=0,
            d=self.hiding_icon_duration,
            t=self.hiding_icon_transition,
        )
        anim.bind(
            on_complete=lambda x, y: self.show_icon_marked_segment(segment_item)
        )
        anim.start(segment_item.ids.scale_icon)

    def restore_bg_segment(self, segment_item) -> None:
        Animation(md_bg_color=self.md_bg_color, d=0.2).start(segment_item)

    def set_bg_marked_segment(self, segment_item) -> None:
        if segment_item.active:
            Animation(
                md_bg_color=self.selected_color
                if self.selected_color
                else self.theme_cls.primary_color,
                d=0.2,
            ).start(segment_item)

    def set_selected_segment_list(self, segment_item) -> None:
        segment_item.active = not segment_item.active

        if segment_item.active:
            self.selected_items.append(segment_item)
            self.dispatch("on_marked", segment_item, segment_item.active)
        else:
            if segment_item in self.selected_items:
                self.selected_items.remove(segment_item)
                self.dispatch("on_unmarked", segment_item, segment_item.active)

    def mark_item(self, segment_item: MDSegmentedButtonItem) -> None:
        if segment_item.active and not self.multiselect:
            return
        if not self.multiselect and self.selected_items:
            self.uncheck_item()
        else:
            if segment_item.active:
                self.restore_bg_segment(segment_item)

        self.hide_icon_marked_segment(segment_item)

    def uncheck_item(self) -> None:
        for item in self.children:
            if item.active:
                self.hide_icon_marked_segment(item)
                self.restore_bg_segment(item)
                break

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDSegmentedButtonItem):
            widget.bind(on_release=self.mark_item)
            return super().add_widget(widget)

    def on_size(self, instance_segment_button, size: list) -> None:
        """Called when the root screen is resized."""

        if self.size_hint_x:
            max_width = size[0] / len(self.children)
            for widget in self.children:
                widget.width = max_width

    def on_marked(self, *args):
        """The method is called when a segment is marked."""

    def on_unmarked(self, *args):
        """The method is called when a segment is unmarked."""


class SegmentButtonIcon(MDIcon, ScaleBehavior):
    """Implements an icon with scaling behavior."""
