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

- Segmented buttons can contain icons, label text, or both
- Two types: single-select and multi-select
- Use for simple choices between two to five items (for more items or complex
  choices, use chips)

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-types.png
    :align: center

1. Single-select segmented button
2. Multi-select segmented button

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-anatomy.png
    :align: center

Icons
-----

Icons may be used as labels by themselves or alongside text.
If an icon is used without label text, it must clearly communicate the option
it represents.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-icons.png
    :align: center

Use with text and icon
----------------------

.. code-block:: kv

    MDSegmentedButton:

        MDSegmentedButtonItem:

            MDSegmentButtonIcon:
                icon: "language-python"

            MDSegmentButtonLabel:
                text: "Python"

        MDSegmentedButtonItem:

            MDSegmentButtonIcon:
                icon: "language-javascript"

            MDSegmentButtonLabel:
                text: "Java-Script"

        MDSegmentedButtonItem:

            MDSegmentButtonIcon:
                icon: "language-swift"

            MDSegmentButtonLabel:
                text: "Swift"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-use-with-text-and-icon.gif
    :align: center

Use without text with an icon
-----------------------------

.. code-block:: kv

    MDSegmentedButton:

        MDSegmentedButtonItem:

            MDSegmentButtonIcon:
                icon: "language-python"

        MDSegmentedButtonItem:

            MDSegmentButtonIcon:
                icon: "language-javascript"

        MDSegmentedButtonItem:

            MDSegmentButtonIcon:
                icon: "language-swift"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-use-without-text-with-an-icon.gif
    :align: center

Use only text
-------------

.. code-block:: kv

    MDSegmentedButton:

        MDSegmentedButtonItem:

            MDSegmentButtonLabel:
                text: "Python"

        MDSegmentedButtonItem:

            MDSegmentButtonLabel:
                text: "Java-Script"

        MDSegmentedButtonItem:

            MDSegmentButtonLabel:
                text: "Swift"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-use-only-text.gif
    :align: center

Multiselect
-----------

For multiple marking of elements, use the
:attr:`kivymd.uix.segmentedbutton.segmentedbutton.MDSegmentedButton.multiselect`
parameter:

.. code-block:: kv

    MDSegmentedButton:
        multiselect: True

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-multiselect-true.gif
    :align: center

Type
----

Density can be used in denser UIs where space is limited. Density is only
applied to the height. Each step down in density removes 4dp from the height.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/segmented-button-type.png
    :align: center

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.uix.label import MDLabel
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.uix.segmentedbutton import (
        MDSegmentedButton,
        MDSegmentedButtonItem,
        MDSegmentButtonLabel,
    )
    from kivymd.app import MDApp

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDBoxLayout:
            id: box
            orientation: "vertical"
            size_hint_x: .7
            adaptive_height: True
            spacing: "24dp"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Example(MDApp):
        def on_start(self):
            for segment_type in ["large", "normal", "medium", "small"]:
                self.root.ids.box.add_widget(
                    MDBoxLayout(
                        MDLabel(
                            text=f"Type '{segment_type}'",
                            adaptive_height=True,
                            bold=True,
                            pos_hint={"center_y": 0.5},
                            halign="center",
                        ),
                        MDSegmentedButton(
                            MDSegmentedButtonItem(
                                MDSegmentButtonLabel(
                                    text="Songs",
                                ),
                            ),
                            MDSegmentedButtonItem(
                                MDSegmentButtonLabel(
                                    text="Albums",
                                ),
                            ),
                            MDSegmentedButtonItem(
                                MDSegmentButtonLabel(
                                    text="Podcasts",
                                ),
                            ),
                            type=segment_type,
                        ),
                        orientation="vertical",
                        spacing="12dp",
                        adaptive_height=True,
                    )
                )

        def build(self):
            return Builder.load_string(KV)


    Example().run()

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

    import asynckivy

    KV = '''
    <UserCard>
        adaptive_height: True
        radius: 16

        MDListItem:
            radius: 16
            theme_bg_color: "Custom"
            md_bg_color: self.theme_cls.secondaryContainerColor

            MDListItemLeadingAvatar:
                source: root.album

            MDListItemHeadlineText:
                text: root.name

            MDListItemSupportingText:
                text: root.path_to_file


    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDBoxLayout:
            orientation: "vertical"
            padding: "12dp"
            spacing: "12dp"

            MDLabel:
                adaptive_height: True
                text: "Your downloads"
                theme_font_style: "Custom"
                font_style: "Display"
                role: "small"

            MDSegmentedButton:
                size_hint_x: 1

                MDSegmentedButtonItem:
                    on_active: app.generate_card()

                    MDSegmentButtonLabel:
                        text: "Songs"
                        active: True

                MDSegmentedButtonItem:
                    on_active: app.generate_card()

                    MDSegmentButtonLabel:
                        text: "Albums"

                MDSegmentedButtonItem:
                    on_active: app.generate_card()

                    MDSegmentButtonLabel:
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
            self.theme_cls.primary_palette = "Olive"
            return Builder.load_string(KV)

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

API break
=========

1.2.0 version
-------------

.. code-block:: kv

    MDSegmentedButton:
        on_marked: func(*args)

        MDSegmentedButtonItem:
            icon: ...
            text: ...

2.0.0 version
-------------

.. code-block:: kv

    MDSegmentedButton:

        MDSegmentedButtonItem:
            on_active: func(*args)

            MDSegmentButtonIcon:
                icon: ...

            MDSegmentButtonLabel:
                text: ...

"""

from __future__ import annotations

__all__ = (
    "MDSegmentedButton",
    "MDSegmentedButtonItem",
    "MDSegmentButtonLabel",
    "MDSegmentButtonIcon",
)

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
    OptionProperty,
    ObjectProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

from kivymd.theming import ThemableBehavior
from kivymd import uix_path
from kivymd.uix.behaviors import (
    RectangularRippleBehavior,
    DeclarativeBehavior,
    BackgroundColorBehavior,
)
from kivymd.uix.behaviors.state_layer_behavior import StateLayerBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDIcon, MDLabel

with open(
    os.path.join(uix_path, "segmentedbutton", "segmentedbutton.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read(), filename="MDSegmentedButton")


class MDSegmentedButtonItem(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    RectangularRippleBehavior,
    ButtonBehavior,
    StateLayerBehavior,
    RelativeLayout,
):
    """
    Segment button item.

    For more information see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior` and
    :class:`~kivy.uix.relativelayout.RelativeLayout` and
    class documentation.
    """

    selected_color = ColorProperty(None)
    """
    Color of the marked segment.

    .. versionadded:: 2.0.0

    :attr:`selected_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the list item when
    the list item is disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    active = BooleanProperty(False)
    """
    Background color of an disabled segment.

    :attr:`active` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _icon = ObjectProperty()  # MDSegmentButtonIcon object
    _label = ObjectProperty()  # MDSegmentButtonLabel object
    _segmented_button = ObjectProperty()  # MDSegmentedButton object
    _line_color = ColorProperty(None)

    def add_widget(self, widget, *args, **kwargs):
        def add_selected_icon(container: MDSegmentedButtonItemContainer):
            selected_icon = MDSegmentButtonSelectedIcon(
                _segmented_button=self._segmented_button, _item=self
            )
            container.add_widget(selected_icon, index=1)

        if isinstance(
            widget,
            (MDSegmentButtonLabel, MDSegmentButtonIcon),
        ):
            if isinstance(widget, MDSegmentButtonLabel):
                self._label = widget
            elif isinstance(widget, MDSegmentButtonIcon):
                self._icon = widget
            Clock.schedule_once(
                lambda x: self._segmented_button._set_size_hint_min_x(widget)
            )
            self.ids.container.add_widget(widget)
        elif isinstance(widget, MDSegmentedButtonItemContainer):
            Clock.schedule_once(lambda x: add_selected_icon(widget))
            return super().add_widget(widget)

    def on_line_color(self, instance, value) -> None:
        """Fired when the values of :attr:`line_color` change."""

        if not self.disabled and self.theme_line_color == "Custom":
            self._line_color = value

    def on_active(self, instance, value) -> None:
        """
        Fired when the :attr:`active` value changes.
        Animates the marker icon for the element.
        """

        def set_active(*args):
            t = (
                self._segmented_button.opening_icon_transition
                if value
                else self._segmented_button.hiding_icon_transition
            )
            d = (
                self._segmented_button.opening_icon_duration
                if value
                else self._segmented_button.hiding_icon_duration
            )

            if self._icon and self._segmented_button:
                if self._label:
                    Animation(font_size=0 if value else sp(18), t=t, d=d).start(
                        self._icon
                    )

            selected_icon = self._get_selected_icon_from_container()
            if selected_icon:
                Animation(font_size=sp(18) if value else 0, t=t, d=d).start(
                    selected_icon
                )

        Clock.schedule_once(set_active, 0.5)

    def on_disabled(self, instance, value) -> None:
        """Fired when the :attr:`disabled` value changes."""

        selected_icon = None

        if self._icon and self._segmented_button:
            selected_icon = self._get_selected_icon_from_item()
        elif not self._icon and self._segmented_button:
            selected_icon = self._get_selected_icon_from_container()

        if selected_icon:
            selected_icon.state_layer_color = self.theme_cls.transparentColor

    def _get_selected_icon_from_container(self):
        selected_icon = None
        for item in self.ids.container.children:
            if isinstance(item, MDSegmentButtonSelectedIcon):
                selected_icon = item
                break
        return selected_icon

    def _get_selected_icon_from_item(self):
        selected_icon = None
        for item in self.children:
            if isinstance(item, MDSegmentButtonSelectedIcon):
                selected_icon = item
                break
        return selected_icon


class MDSegmentedButton(MDBoxLayout):
    """
    Segment button panel.

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` class documentation.
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

    hiding_icon_duration = NumericProperty(0.1)
    """
    Duration of hiding the current icon.

    :attr:`hiding_icon_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    opening_icon_transition = StringProperty("linear")
    """
    The name of the transition that opens a new icon of the "marked" type.

    :attr:`opening_icon_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'linear'`.
    """

    opening_icon_duration = NumericProperty(0.1)
    """
    The duration of opening a new icon of the "marked" type.

    :attr:`opening_icon_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.1`.
    """

    selected_segments = ListProperty()
    """
    The list of :class:`~MDSegmentedButtonItem` objects that are currently
    marked.

    :attr:`selected_segments` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    type = OptionProperty(
        "large", options=["large", "normal", "medium", "small"]
    )
    """
    Density can be used in denser UIs where space is limited.
    Density is only applied to the height. Each step down in density removes
    '4dp' from the height.

    .. versionadded:: 2.0.0

    Available options are: 'large', 'normal', 'medium', 'small'.

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'large'`.
    """

    selected_icon_color = ColorProperty(None)
    """
    Color in (r, g, b, a) or string format of the icon of the marked segment.

    .. versionadded:: 2.0.0

    :attr:`selected_icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    def get_marked_items(self) -> list:
        """Returns a list of active item objects."""

        return [item for item in self.ids.container.children if item.active]

    def get_items(self) -> list:
        """Returns a list of item objects."""

        return [item for item in self.ids.container.children]

    def adjust_segment_radius(self, *args) -> None:
        """Rounds off the first and last elements."""

        _rad = self.height / 2

        _last_radius = [0, _rad, _rad, 0]
        _first_radius = [_rad, 0, 0, _rad]
        _optimal_radius = [0, 0, 0, 0]

        _child_count = len(self.ids.container.children)

        for count, child in enumerate(self.ids.container.children):
            if count == 0:
                child.radius = _last_radius
            elif count == _child_count - 1:
                child.radius = _first_radius
            else:
                child.radius = _optimal_radius

    def mark_item(self, segment_item: MDSegmentedButtonItem) -> None:
        """Fired when a segment element is clicked (`on_release` event)."""

        if not segment_item.disabled:
            if not segment_item.active and not self.multiselect:
                segment_item.active = True
            elif self.multiselect:
                segment_item.active = not segment_item.active

            if not self.multiselect:
                for widget in self.ids.container.children:
                    if segment_item is not widget:
                        widget.active = False

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDSegmentedButtonItem):
            widget._segmented_button = self
            widget.bind(on_release=self.mark_item)
            self.ids.container.add_widget(widget)
            self.adjust_segment_radius()
        elif isinstance(widget, MDSegmentedButtonContainer):
            return super().add_widget(widget)

    def remove_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDSegmentedButtonItem):
            for child in widget.children[0].children:
                if isinstance(child, MDSegmentButtonLabel) or isinstance(
                    child, MDSegmentButtonIcon
                ):
                    self._set_size_hint_min_x(child, sign=-1)
            self.ids.container.remove_widget(widget)
            self.adjust_segment_radius()
        elif isinstance(widget, MDSegmentedButtonContainer):
            return super().remove_widget(widget)

    def _set_size_hint_min_x(
        self, widget: MDSegmentButtonLabel | MDSegmentButtonIcon, sign: int = 1
    ):
        self.ids.container.size_hint_min_x += sign * (
            widget.texture_size[0] + dp(36)
        )


class MDSegmentedButtonContainer(BoxLayout):
    """
    Implements a container for placing :class:`~MDSegmentedButtonItem`
    elements.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """


class MDSegmentedButtonItemContainer(BoxLayout):
    """
    Implements a container for placing :class:`~MDSegmentButtonLabel`
    and :class:`~MDSegmentButtonLabel` elements.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """


class MDSegmentButtonSelectedIcon(MDIcon):
    """
    Implements the selected icon with scaling behavior
    for :class:`~MDSegmentedButtonItem` class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDIcon` class documentation.
    """

    _segmented_button = ObjectProperty()  # MDSegmentedButton object
    _item = ObjectProperty()  # MDSegmentedButtonItem object


class MDSegmentButtonIcon(MDIcon):
    """
    Implements a icon for :class:`~MDSegmentedButtonItem` class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDIcon` class documentation.
    """


class MDSegmentButtonLabel(MDLabel):
    """
    Implements a label for :class:`~MDSegmentedButtonItem` class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """
