"""
Components/BottomSheet
======================

.. seealso::

    `Material Design spec, Sheets: bottom <https://m3.material.io/components/bottom-sheets/overview>`_

.. rubric:: Bottom sheets are surfaces containing supplementary content that are anchored to the bottom of the screen.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet.png
    :align: center

Usage
=====

.. code-block:: kv

    Root:

        MDNavigationLayout:

            MDScreenManager:

                [...]

            MDBottomSheet:


The bottom sheet has two types:

- Standard_
- Modal_

.. Standard:

Standard
--------

`Standard bottom sheets <https://m3.material.io/components/bottom-sheets/guidelines#aa1caae4-2d86-4c8c-af09-548a6f666b8a>`_
co-exist with the screen’s main UI region and allow for simultaneously viewing
and interacting with both regions, especially when the main UI region is
frequently scrolled or panned.

Use a standard bottom sheet to display content that complements the screen’s
primary content, such as an audio player in a music app.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-standard.gif
    :align: center

Standard bottom sheets are elevated above the main UI region so their
visibility is not affected by panning or scrolling.

.. Modal:

Modal
-----

Like dialogs, `modal bottom sheets <https://m3.material.io/components/bottom-sheets/guidelines#1cb775b6-6d2b-4d50-96ad-1862727e986b>`_
appear in front of app content, disabling all other app functionality when
they appear, and remaining on screen until confirmed, dismissed, or a required
action has been taken.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-modal.gif
    :align: center

Tapping the scrim dismisses a modal bottom sheet.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-modal-tapping.png
    :align: center

Add elements to :class:`~MDBottomSheetDragHandleTitle` class
------------------------------------------------------------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDBottomSheet:
                    size_hint_y: None
                    height: "84dp"

                    MDBottomSheetDragHandle:

                        MDBottomSheetDragHandleTitle:
                            text: "MDBottomSheet"
                            adaptive_height: True
                            pos_hint: {"center_y": .5}

                        MDBottomSheetDragHandleButton:
                            icon: "close"
            '''


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.bottomsheet import (
                MDBottomSheet,
                MDBottomSheetDragHandle,
                MDBottomSheetDragHandleTitle,
                MDBottomSheetDragHandleButton,
            )
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDBottomSheet(
                                MDBottomSheetDragHandle(
                                    MDBottomSheetDragHandleTitle(
                                        text="MDBottomSheet",
                                        adaptive_height=True,
                                        pos_hint={"center_y": 0.5},
                                    ),
                                    MDBottomSheetDragHandleButton(
                                        icon="close",
                                    ),
                                ),
                                size_hint_y=None,
                                height="84dp",
                            ),
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-drag-handle-elements.png
    :align: center

A practical example with standard bottom sheet
----------------------------------------------

(A double tap on the map to open the bottom sheet)

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            import asynckivy

            from kivy.lang import Builder
            from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
            from kivy_garden.mapview import MapView

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import TouchBehavior
            from kivymd.uix.boxlayout import MDBoxLayout

            KV = '''
            #:import MapSource kivy_garden.mapview.MapSource
            #:import asynckivy asynckivy


            <TypeMapElement>
                orientation: "vertical"
                adaptive_height: True
                spacing: "8dp"

                MDIconButton:
                    id: icon
                    icon: root.icon
                    theme_bg_color: "Custom"
                    md_bg_color: "#EDF1F9" if not root.selected else app.theme_cls.primaryColor
                    pos_hint: {"center_x": .5}
                    theme_icon_color: "Custom"
                    icon_color: "white" if root.selected else "black"
                    on_release: app.set_active_element(root, root.title.lower())

                MDLabel:
                    text: root.title
                    pos_hint: {"center_x": .5}
                    halign: "center"
                    adaptive_height: True


            MDScreen:

                MDNavigationLayout:

                    MDScreenManager:

                        MDScreen:

                            CustomMapView:
                                bottom_sheet: bottom_sheet
                                map_source: MapSource(url=app.map_sources[app.current_map])
                                lat: 46.5124
                                lon: 47.9812
                                zoom: 12

                    MDBottomSheet:
                        id: bottom_sheet
                        sheet_type: "standard"
                        size_hint_y: None
                        height: "150dp"
                        on_open: asynckivy.start(app.generate_content())

                        MDBottomSheetDragHandle:
                            drag_handle_color: "grey"

                            MDBottomSheetDragHandleTitle:
                                text: "Select type map"
                                pos_hint: {"center_y": .5}

                            MDBottomSheetDragHandleButton:
                                icon: "close"
                                ripple_effect: False
                                on_release: bottom_sheet.set_state("toggle")

                        BoxLayout:
                            id: content_container
                            padding: 0, 0, 0, "16dp"
            '''


            class TypeMapElement(MDBoxLayout):
                selected = BooleanProperty(False)
                icon = StringProperty()
                title = StringProperty()


            class CustomMapView(MapView, TouchBehavior):
                bottom_sheet = ObjectProperty()

                def on_double_tap(self, touch, *args):
                    if self.bottom_sheet:
                        self.bottom_sheet.set_state("toggle")


            class Example(MDApp):
                map_sources = {
                    "street": "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
                    "sputnik": "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
                    "hybrid": "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
                }
                current_map = StringProperty("street")

                async def generate_content(self):
                    icons = {
                        "street": "google-street-view",
                        "sputnik": "space-station",
                        "hybrid": "map-legend",
                    }
                    if not self.root.ids.content_container.children:
                        for i, title in enumerate(self.map_sources.keys()):
                            await asynckivy.sleep(0)
                            self.root.ids.content_container.add_widget(
                                TypeMapElement(
                                    title=title.capitalize(),
                                    icon=icons[title],
                                    selected=not i,
                                )
                            )

                def set_active_element(self, instance, type_map):
                    for element in self.root.ids.content_container.children:
                        if instance == element:
                            element.selected = True
                            self.current_map = type_map
                        else:
                            element.selected = False

                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
            from kivy_garden.mapview import MapView

            import asynckivy
            from kivy_garden.mapview import MapSource

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import TouchBehavior, DeclarativeBehavior
            from kivymd.uix.bottomsheet import (
                MDBottomSheet,
                MDBottomSheetDragHandle,
                MDBottomSheetDragHandleTitle,
                MDBottomSheetDragHandleButton,
            )
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import MDIconButton
            from kivymd.uix.label import MDLabel
            from kivymd.uix.navigationdrawer import MDNavigationLayout
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.screenmanager import MDScreenManager


            class TypeMapElement(MDBoxLayout):
                selected = BooleanProperty(False)
                icon = StringProperty()
                title = StringProperty()


            class CustomMapView(DeclarativeBehavior, MapView, TouchBehavior):
                bottom_sheet = ObjectProperty()

                def on_double_tap(self, touch, *args):
                    if self.bottom_sheet:
                        self.bottom_sheet.set_state("toggle")


            class Example(MDApp):
                map_sources = {
                    "street": "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
                    "sputnik": "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
                    "hybrid": "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
                }
                current_map = StringProperty("street")

                async def generate_content(self):
                    icons = {
                        "street": "google-street-view",
                        "sputnik": "space-station",
                        "hybrid": "map-legend",
                    }
                    if not self.screen.get_ids().content_container.children:
                        for i, title in enumerate(self.map_sources.keys()):
                            await asynckivy.sleep(0)
                            type_map_element = TypeMapElement(
                                MDIconButton(
                                    id=f"icon_{icons[title]}",
                                    icon=icons[title],
                                    theme_bg_color="Custom",
                                    md_bg_color="#EDF1F9",
                                    pos_hint={"center_x": 0.5},
                                    theme_icon_color="Custom",
                                    icon_color="black"
                                ),
                                MDLabel(
                                    text=title,
                                    pos_hint={"center_x": 0.5},
                                    halign="center",
                                    adaptive_height=True,
                                ),
                                orientation="vertical",
                                adaptive_height=True,
                                spacing="8dp",
                                title=title.capitalize(),
                                icon=icons[title],
                                selected=not i,
                            )
                            icon = type_map_element.get_ids()[f"icon_{icons[title]}"]
                            icon.bind(
                                on_release=lambda x=icon, z=type_map_element, y=title.lower(): self.set_active_element(
                                    x, z, y
                                )
                            )
                            self.screen.get_ids().content_container.add_widget(
                                type_map_element
                            )

                def set_active_element(self, button, instance, type_map):
                    for element in self.screen.get_ids().content_container.children:
                        if instance is element:
                            element.selected = True
                            button.md_bg_color = self.theme_cls.primaryColor
                            button.icon_color = "white"
                            self.current_map = type_map
                            self.screen.get_ids().custom_mapview.map_source = MapSource(
                                url=self.map_sources[self.current_map]
                            )
                        else:
                            for widget in element.children:
                                if isinstance(widget, MDIconButton) and not widget is button:
                                    element.selected = False
                                    widget.md_bg_color = "#EDF1F9"
                                    widget.icon_color = "black"

                def build(self):
                    self.screen = MDScreen(
                        MDNavigationLayout(
                            MDScreenManager(
                                MDScreen(
                                    CustomMapView(
                                        id="custom_mapview",
                                        map_source=MapSource(
                                            url=self.map_sources[self.current_map]
                                        ),
                                        lat=46.5124,
                                        lon=47.9812,
                                        zoom=12,
                                    )
                                )
                            ),
                            MDBottomSheet(
                                MDBottomSheetDragHandle(
                                    MDBottomSheetDragHandleTitle(
                                        text="Select type map",
                                        pos_hint={"center_y": 0.5},
                                    ),
                                    MDBottomSheetDragHandleButton(
                                        id="handle_button",
                                        icon="close",
                                        ripple_effect=False,
                                    ),
                                    drag_handle_color="grey",
                                ),
                                MDBoxLayout(
                                    id="content_container",
                                    padding=(0, 0, 0, "16dp"),
                                ),
                                id="bottom_sheet",
                                sheet_type="standard",
                                size_hint_y=None,
                                height="150dp",
                                on_open=lambda x: asynckivy.start(self.generate_content()),
                            ),
                        )
                    )
                    bottom_sheet = self.screen.get_ids().bottom_sheet
                    self.screen.get_ids().custom_mapview.bottom_sheet = bottom_sheet
                    self.screen.get_ids().handle_button.bind(
                        on_release=lambda x: bottom_sheet.set_state("toggle")
                    )
                    return self.screen


            Example().run()

API break
=========

1.2.0 version
-------------

.. code-block:: kv

    Root:

        MDBottomSheet:

            # Optional.
            MDBottomSheetDragHandle:

                # Optional.
                MDBottomSheetDragHandleTitle:

                # Optional.
                MDBottomSheetDragHandleButton:

            MDBottomSheetContent:
                [...]

2.0.0 version
-------------

.. code-block:: kv

    Root:

        MDNavigationLayout:

            MDScreenManager:

                # Your screen.
                MDScreen:

            MDBottomSheet:

                # Optional.
                MDBottomSheetDragHandle:

                    # Optional.
                    MDBottomSheetDragHandleTitle:

                    # Optional.
                    MDBottomSheetDragHandleButton:
                        icon: "close"

                # Your content.
                BoxLayout:
"""

__all__ = (
    "MDBottomSheet",
    "MDBottomSheetDragHandle",
    "MDBottomSheetDragHandleTitle",
    "MDBottomSheetDragHandleButton",
)

import os

from kivy.lang import Builder
from kivy.properties import ColorProperty, OptionProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.navigationdrawer import MDNavigationDrawer

with open(
    os.path.join(uix_path, "bottomsheet", "bottomsheet.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read(), filename="MDBottomSheet.kv")


class BottomSheetDragHandle(Widget):
    pass


class BottomSheetDragHandleContainer(BoxLayout):
    pass


class MDBottomSheetDragHandleButton(MDIconButton):
    """
    Implements a close button (or other functionality) for the
    :class:`~MDBottomSheetDragHandle` container.

    For more information, see in the
    :class:`~kivymd.uix.button.button.MDIconButton` class documentation.

    .. versionadded:: 1.2.0
    """


class MDBottomSheetDragHandleTitle(MDLabel):
    """
    Implements a header for the :class:`~MDBottomSheetDragHandle` container.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.

    .. versionadded:: 1.2.0
    """


class MDBottomSheetDragHandle(DeclarativeBehavior, BoxLayout):
    """
    Implements a container that can place the header of the bottom sheet
    and the close button. Also implements the event of dragging the
    bottom sheet on the parent screen.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.DeclarativeBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout` classes documentation.

    .. versionadded:: 1.2.0
    """

    drag_handle_color = ColorProperty(None)
    """
    Color of drag handle element in (r, g, b, a) or string format.

    .. code-block:: kv

        MDBottomSheet:

            MDBottomSheetDragHandle:
                drag_handle_color: "white"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-sheet-drag-handle-color.png
        :align: center

    :attr:`drag_handle_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(
            widget,
            (MDBottomSheetDragHandleTitle, MDBottomSheetDragHandleButton),
        ):
            self.ids.header_container.add_widget(widget)
        elif isinstance(
            widget,
            (BottomSheetDragHandleContainer, BottomSheetDragHandle),
        ):
            return super().add_widget(widget)


class MDBottomSheet(MDNavigationDrawer):
    """
    Bottom sheet class.

    For more information, see in the
    :class:`~kivymd.uix.navigationdrawer.navigationdrawer.MDNavigationDrawer`
    class documentation.
    """

    sheet_type = OptionProperty("modal", options=("standard", "modal"))
    """
    Type of sheet.

    Standard bottom sheets co-exist with the screen’s main UI region and allow
    for simultaneously viewing and interacting with both regions, especially
    when the main UI region is frequently scrolled or panned. Use a standard
    bottom sheet to display content that complements the screen’s primary
    content, such as an audio player in a music app.

    Like dialogs, modal bottom sheets appear in front of app content,
    disabling all other app functionality when they appear, and remaining on
    screen until confirmed, dismissed, or a required action has been taken.

    .. versionchanged:: 2.0.0

        Rename from `type` to `sheet_type`.

    :attr:`sheet_type` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'modal'`.
    """

    def on_sheet_type(self, instance, value) -> None:
        """Fired when the :attr:`sheet_type` value changes."""

        self.drawer_type = value

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDBottomSheetDragHandle):
            self.ids.drag_handle_container.add_widget(widget)
            return
        return super().add_widget(widget)

    def on_touch_move(self, touch):
        if self.enable_swiping:
            if self.status == "closed":
                if (
                    self.get_dist_from_side(touch.oy) <= self.swipe_edge_width
                    and abs(touch.y - touch.oy) > self.swipe_distance
                ):
                    self.status = "opening_with_swipe"
            elif self.status == "opened":
                if abs(touch.y - touch.oy) > self.swipe_distance:
                    self.status = "closing_with_swipe"

        if self.status in ("opening_with_swipe", "closing_with_swipe"):
            self.open_progress = max(
                min(
                    self.open_progress
                    + (touch.dy if self.anchor == "left" else -touch.dy)
                    / self.height,
                    1,
                ),
                0,
            )
            return True
        return super().on_touch_move(touch)
