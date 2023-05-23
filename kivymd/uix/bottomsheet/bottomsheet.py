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

    MDScreen:

        [ Content screen ]

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

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-standard.png
    :align: center

Standard bottom sheets are elevated above the main UI region so their
visibility is not affected by panning or scrolling.

Standard bottom sheet example
-----------------------------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDBoxLayout:
                    orientation: "vertical"
                    padding: "12dp"
                    adaptive_height: True
                    pos_hint: {"top": 1}

                    MDSmartTile:
                        id: smart_tile
                        source: "https://picsum.photos/id/70/3011/2000"
                        radius: 16
                        box_radius: [0, 0, 16, 16]
                        size_hint_y: None
                        height: "240dp"
                        on_release:
                            bottom_sheet.open() \\
                            if bottom_sheet.state == "close" else \\
                            bottom_sheet.dismiss()

                        MDLabel:
                            bold: True
                            color: 1, 1, 1, 1
                            text:
                                "Tap to open the bottom sheet" \\
                                if bottom_sheet.state == "close" else \\
                                "Tap to close the bottom sheet"

                MDBottomSheet:
                    id: bottom_sheet
                    type: "standard"
                    bg_color: "grey"
                    default_opening_height: smart_tile.y - dp(12)
                    size_hint_y: None
                    height: root.height - (smart_tile.height + dp(24))
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.clock import Clock
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.bottomsheet import MDBottomSheet
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.imagelist import MDSmartTile
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return MDScreen(
                        MDBoxLayout(
                            MDSmartTile(
                                MDLabel(
                                    id="tile_label",
                                    text="Tap to open the bottom sheet",
                                    bold=True,
                                    color=(1, 1, 1, 1),
                                ),
                                id="smart_tile",
                                source="https://picsum.photos/id/70/3011/2000",
                                radius=16,
                                box_radius=[0, 0, 16, 16],
                                size_hint_y=None,
                                height="240dp",
                            ),
                            id="box",
                            orientation="vertical",
                            padding="12dp",
                            pos_hint={"top": 1},
                            adaptive_height=True,
                        ),
                        MDBottomSheet(
                            id="bottom_sheet",
                            size_hint_y=None,
                            type="standard",
                            bg_color="grey",
                        ),
                    )

                def open_bottom_sheet(self, *args):
                    bottom_sheet = self.root.ids.bottom_sheet
                    smart_tile = self.root.ids.box.ids.smart_tile
                    tile_label = smart_tile.ids.tile_label
                    bottom_sheet.open() if bottom_sheet.state == "close" else bottom_sheet.dismiss()
                    tile_label.text = (
                        "Tap to open the bottom sheet"
                        if bottom_sheet.state == "close"
                        else "Tap to close the bottom sheet"
                    )

                def on_start(self):
                    def on_start(*args):
                        bottom_sheet = self.root.ids.bottom_sheet
                        smart_tile = self.root.ids.box.ids.smart_tile
                        bottom_sheet.default_opening_height = smart_tile.y - dp(12)
                        bottom_sheet.height = self.root.height - (
                            smart_tile.height + dp(24)
                        )
                        smart_tile.bind(on_release=lambda x: self.open_bottom_sheet())

                    Clock.schedule_once(on_start, 1.2)


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-standard-example.gif
    :align: center

.. Modal:
Modal
-----

Like dialogs, `modal bottom sheets <https://m3.material.io/components/bottom-sheets/guidelines#1cb775b6-6d2b-4d50-96ad-1862727e986b>`_
appear in front of app content, disabling all other app functionality when
they appear, and remaining on screen until confirmed, dismissed, or a required
action has been taken.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-modal.png
    :align: center

Modal bottom sheet example
--------------------------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDBoxLayout:
                    orientation: "vertical"
                    padding: "12dp"
                    adaptive_height: True
                    pos_hint: {"top": 1}

                    MDSmartTile:
                        id: smart_tile
                        source: "https://picsum.photos/id/70/3011/2000"
                        radius: 16
                        box_radius: [0, 0, 16, 16]
                        size_hint_y: None
                        height: "240dp"
                        on_release: bottom_sheet.open()

                        MDLabel:
                            bold: True
                            color: 1, 1, 1, 1
                            text: "Tap to open the modal bottom sheet"

                MDBottomSheet:
                    id: bottom_sheet
                    bg_color: "grey"
                    default_opening_height: smart_tile.y - dp(12)
                    size_hint_y: None
                    height: root.height - (smart_tile.height + dp(24))
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.clock import Clock
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.bottomsheet import MDBottomSheet
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.imagelist import MDSmartTile
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return MDScreen(
                        MDBoxLayout(
                            MDSmartTile(
                                MDLabel(
                                    id="tile_label",
                                    text="Tap to open the modal bottom sheet",
                                    bold=True,
                                    color=(1, 1, 1, 1),
                                ),
                                id="smart_tile",
                                source="https://picsum.photos/id/70/3011/2000",
                                radius=16,
                                box_radius=[0, 0, 16, 16],
                                size_hint_y=None,
                                height="240dp",
                            ),
                            id="box",
                            orientation="vertical",
                            padding="12dp",
                            pos_hint={"top": 1},
                            adaptive_height=True,
                        ),
                        MDBottomSheet(
                            id="bottom_sheet",
                            size_hint_y=None,
                            bg_color="grey",
                        ),
                    )

                def open_bottom_sheet(self, *args):
                    bottom_sheet = self.root.ids.bottom_sheet
                    bottom_sheet.open()

                def on_start(self):
                    def on_start(*args):
                        bottom_sheet = self.root.ids.bottom_sheet
                        smart_tile = self.root.ids.box.ids.smart_tile
                        bottom_sheet.default_opening_height = smart_tile.y - dp(12)
                        bottom_sheet.height = self.root.height - (
                                smart_tile.height + dp(24)
                        )
                        smart_tile.bind(on_release=lambda x: self.open_bottom_sheet())

                    Clock.schedule_once(on_start, 1.2)


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-modal-example.gif
    :align: center

Tapping the scrim dismisses a modal bottom sheet.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-modal-tapping.png
    :align: center

Custom positioning
------------------

The optional drag handle provides an affordance for custom sheet height,
or for a quick toggle through preset heights.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-drag-handle.png
    :align: center

.. code-block:: kv

    MDBottomSheet:

        MDBottomSheetDragHandle:

By default, when you drag and then release the drag handle, the bottom sheet
will be closed or expand to the full screen, depending on whether you released
the drag handle closer to the top or to the bottom of the screen:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-drag-handle.gif
    :align: center

In order to manually adjust the height of the bottom sheet with the drag handle,
set the `auto_positioning` parameter to `False`:

.. code-block:: kv

    MDBottomSheet:
        auto_positioning: False

        MDBottomSheetDragHandle:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-drag-handle-auto-positioning.gif
    :align: center

Add elements to :class:`~MDBottomSheetDragHandleTitle` class
------------------------------------------------------------

.. code-block:: kv

    MDBottomSheet:

        MDBottomSheetDragHandle:

            MDBottomSheetDragHandleTitle:
                text: "MDBottomSheet"
                adaptive_height: True
                font_style: "H6"
                pos_hint: {"center_y": .5}

            MDBottomSheetDragHandleButton:
                icon: "close"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-drag-handle-elements.png
    :align: center

Add custom content to :class:`~MDBottomSheet` class
---------------------------------------------------

To add custom content to the bottom sheet, use the
:class:`~MDBottomSheetContent` class:

.. code-block:: kv

    MDBottomSheet:
        bg_color: "darkgrey"
        type: "standard"
        max_opening_height: self.height
        default_opening_height: self.max_opening_height
        adaptive_height: True

        MDBottomSheetDragHandle:
            drag_handle_color: "grey"

        MDBottomSheetContent:
            padding: "16dp"

            MDLabel:
                text: "Content"
                halign: "center"
                font_style: "H5"
                adaptive_height: True

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-content.png
    :align: center

A practical example with standard bottom sheet
----------------------------------------------

(A double tap on the map to open the bottom sheet)

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
    from kivy_garden.mapview import MapView

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import TouchBehavior
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.utils import asynckivy

    KV = '''
    #:import MapSource kivy_garden.mapview.MapSource
    #:import asynckivy kivymd.utils.asynckivy


    <TypeMapElement>
        orientation: "vertical"
        adaptive_height: True
        spacing: "8dp"

        MDIconButton:
            id: icon
            icon: root.icon
            md_bg_color: "#EDF1F9" if not root.selected else app.theme_cls.primary_color
            pos_hint: {"center_x": .5}
            theme_icon_color: "Custom"
            icon_color: "white" if root.selected else "black"
            on_release: app.set_active_element(root, root.title.lower())

        MDLabel:
            font_size: "14sp"
            text: root.title
            pos_hint: {"center_x": .5}
            halign: "center"
            adaptive_height: True


    MDScreen:

        CustomMapView:
            bottom_sheet: bottom_sheet
            map_source: MapSource(url=app.map_sources[app.current_map])
            lat: 46.5124
            lon: 47.9812
            zoom: 12

        MDBottomSheet:
            id: bottom_sheet
            elevation: 2
            shadow_softness: 6
            bg_color: "white"
            type: "standard"
            max_opening_height: self.height
            default_opening_height: self.max_opening_height
            adaptive_height: True
            on_open: asynckivy.start(app.generate_content())

            MDBottomSheetDragHandle:
                drag_handle_color: "grey"

                MDBottomSheetDragHandleTitle:
                    text: "Select type map"
                    adaptive_height: True
                    bold: True
                    pos_hint: {"center_y": .5}

                MDBottomSheetDragHandleButton:
                    icon: "close"
                    _no_ripple_effect: True
                    on_release: bottom_sheet.dismiss()

            MDBottomSheetContent:
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
                self.bottom_sheet.open()


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

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-sheet-real-example.gif
    :align: center

"""

__all__ = (
    "MDCustomBottomSheet",
    "MDGridBottomSheet",
    "MDListBottomSheet",
    "MDBottomSheet",
    "MDBottomSheetContent",
    "MDBottomSheetDragHandle",
    "MDBottomSheetDragHandleTitle",
    "MDBottomSheetDragHandleButton",
)

import os

from kivy import Logger
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.screenmanager import Screen

from kivymd import uix_path
from kivymd.uix.behaviors import CommonElevationBehavior, TouchBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.widget import MDWidget

with open(
    os.path.join(uix_path, "bottomsheet", "bottomsheet.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class BottomSheetDragHandle(MDWidget):
    pass


class BottomSheetDragHandleContainer(MDBoxLayout):
    pass


class BottomSheetScrimLayer(MDWidget):
    """
    Implements a transparency layer to shade the parent widget
    on which the bottom sheet is displayed.
    """


class MDBottomSheetContent(MDBoxLayout):
    """
    Implements a container for custom content for the :class:`~MDBottomSheet`
    class

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` class documentation.

    .. versionadded:: 1.2.0
    """


class MDBottomSheetDragHandleButton(MDIconButton):
    """
    Implements a close button (or other functionality) for the
    :class:`~MDBottomSheetDragHandle` container.

    For more information, see in the
    :class:`~kivymd.uix.button.MDIconButton` class documentation.

    .. versionadded:: 1.2.0
    """


class MDBottomSheetDragHandleTitle(MDLabel):
    """
    Implements a header for the :class:`~MDBottomSheetDragHandle` container.

    For more information, see in the
    :class:`~kivymd.uix.label.MDLabel` class documentation.

    .. versionadded:: 1.2.0
    """


class MDBottomSheetDragHandle(MDBoxLayout):
    """
    Implements a container that can place the header of the bottom sheet
    and the close button. Also implements the event of dragging the
    bottom sheet on the parent screen.

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` class documentation.

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


class MDBottomSheet(MDBoxLayout, CommonElevationBehavior, TouchBehavior):
    """
    Bottom sheet class.

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` and
    :class:`~kivymd.uix.behaviors.touch_behavior.CommonElevationBehavior` and
    :class:`~kivymd.uix.behaviors.touch_behavior.TouchBehavior`
    classes documentation.

    :Events:
        `on_open`
            Event when opening the bottom sheet.
        `on_close`
            Event when closing the bottom sheet.
        `on_progress`
            Bottom sheet opening/closing progress event.
    """

    auto_dismiss = BooleanProperty(True)
    """
    This property determines if the view is automatically
    dismissed when the user clicks outside it.

    .. versionadded:: 1.2.0

    :attr:`auto_dismiss` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    type = OptionProperty("modal", options=["modal", "standard"])
    """
    Type sheet. There are two types of bottom sheets: standard and modal.
    Available options are: `'modal'`, `'standard'`.

    .. versionadded:: 1.2.0

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'modal`.
    """

    auto_positioning = BooleanProperty(True)
    """
    Close or expand the bottom menu automatically when you release the
    drag handle.

    .. versionadded:: 1.2.0

    :attr:`auto_positioning` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    max_opening_height = NumericProperty(None, allownone=True)
    """
    The maximum height a that the bottom sheet can be opened using the
    drag handle.

    .. versionadded:: 1.2.0

    .. code-block:: kv

        MDBottomSheet:
            max_opening_height: "300dp"

            MDBottomSheetDragHandle:

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-max-opening-height.gif
        :align: center

    :attr:`max_opening_height` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `None`.
    """

    opening_transition = StringProperty("out_cubic")
    """
    The name of the animation transition type to use when animating to
    the :attr:`state` `'open'`.

    .. versionadded:: 1.2.0

    :attr:`opening_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    closing_transition = StringProperty("out_sine")
    """The name of the animation transition type to use when animating to
    the :attr:`state` 'close'.

    .. versionadded:: 1.2.0

    :attr:`closing_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_sine'`.
    """

    default_opening_height = NumericProperty(dp(200))
    """
    Default opening height of the bottom sheet.

    .. versionadded:: 1.2.0

    :attr:`default_opening_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(100)`.
    """

    duration_opening = NumericProperty(0.15)
    """
    The duration of the bottom sheet opening animation.

    :attr:`duration_opening` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.15`.
    """

    duration_closing = NumericProperty(0.15)
    """
    The duration of the bottom sheet dialog closing animation.

    :attr:`duration_closing` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.15`.
    """

    animation = BooleanProperty(True)
    """
    Whether to use animation for opening and closing of the bottom sheet
    or not.

    :attr:`animation` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    state = OptionProperty("close", options=["close", "open"])
    """
    Menu state. Available options are: `'close'`, `'open'`.

    .. versionadded:: 1.2.0

    :attr:`state` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'close'`.
    """

    scrim_layer_color = ColorProperty([0, 0, 0, 1])
    """
    Color for scrim in (r, g, b, a) or string format.

    .. versionadded:: 1.2.0

    :attr:`scrim_layer_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 1]`.
    """

    bg_color = ColorProperty(None)
    """
    Background color of bottom sheet in (r, g, b, a) or string format.

    :attr:`bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    radius_from = OptionProperty(
        None,
        options=[
            "top_left",
            "top_right",
            "top",
            "bottom_right",
            "bottom_left",
            "bottom",
        ],
        allownone=True,
        deprecated=True,
    )
    """
    Sets which corners to cut from the dialog. Available options are:
    `"top_left"`, `"top_right"`, `"top"`, `"bottom_right"`, `"bottom_left"`,
    `"bottom"`.

    .. deprecated:: 1.2.0
        Use :attr:`radius` instead.

    :attr:`radius_from` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    value_transparent = ColorProperty([0, 0, 0, 0.8], deprecated=True)
    """
    Background color in (r, g, b, a) or string format transparency value when
    opening a dialog.

    .. deprecated:: 1.2.0

    :attr:`value_transparent` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.8]`.
    """

    _diff_between_touch_height_sheet = 0
    _alpha_channel_value = 0
    # Menu state:
    #     - value 'down' - menu is captured;
    #     - value 'none' - menu is not captured;
    _state = OptionProperty("none", options=["none", "down"])
    # There was a touch to the bottom sheet.
    _touch_sheet = False
    # kivymd.uix.bottomsheet.bottomsheet.BottomSheetScrimLayer object.
    _scrim_layer = ObjectProperty(None, allownone=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.y = -Window.height  # start bottom sheet position
        Clock.schedule_once(self.check_parent)
        Clock.schedule_once(self.check_max_opening_height)
        Clock.schedule_once(self.add_scrim_layer)
        self.register_event_type("on_open")
        self.register_event_type("on_close")
        self.register_event_type("on_progress")

    def on_progress(self, *args) -> None:
        """Bottom sheet opening/closing progress event."""

    def on_open(self, *args) -> None:
        """Event when opening the bottom sheet."""

    def on_close(self, *args) -> None:
        """Event when closing the bottom sheet."""

    def on_long_touch(self, touch, *args):
        if self.ids.drag_handle_container.collide_point(touch.x, touch.y):
            self._state = "down"

    def on_touch_down(self, touch):
        if self.type == "standard":
            super().on_touch_down(touch)

        if self.collide_point(touch.x, touch.y):
            self._touch_sheet = not self._touch_sheet
            if self.type == "standard":
                return True
            elif self.type == "modal":
                return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self._diff_between_touch_height_sheet = 0
        self._alpha_channel_value = 0

        if self.collide_point(touch.x, touch.y):
            self._touch_sheet = not self._touch_sheet
            if self.auto_positioning:
                if self._state == "down":
                    self._set_state(touch.y)
        else:
            if self._state == "down":
                self._touch_sheet = not self._touch_sheet
                self._set_state(touch.y)

    def on_touch_move(self, touch):
        if self._state == "down":
            if not self._diff_between_touch_height_sheet:
                self._diff_between_touch_height_sheet = (
                    abs(self.y) if self.y else self.height
                ) - touch.y

            # FIXME: the behavior of the drag handle looks strange:
            #  sometimes the bottom sheet is dragged as needed, and sometimes
            #  it's position does not correspond to the cursor coordinates.
            y = -(
                (self.height - touch.y)
                - 0  # self._diff_between_touch_height_sheet
            )

            if y > 0:
                self.y = 0
                return
            if self.max_opening_height and touch.y > self.max_opening_height:
                self.y = -(self.height - self.max_opening_height)
                return

            self.y = y

            if self._scrim_layer and self.type == "modal":
                if not self._alpha_channel_value:
                    self._alpha_channel_value = (
                        self._scrim_layer.md_bg_color[-1] - touch.psy
                    )

                self._scrim_layer.md_bg_color = self._scrim_layer.md_bg_color[
                    :-1
                ] + [touch.psy + self._alpha_channel_value]

            #
            # if self.radius == [0.0, 0.0, 0.0, 0.0]:
            #     self.radius = [16, 16, 0, 0]

        return super().on_touch_move(touch)

    def on_type(self, *args) -> None:
        self.add_scrim_layer()

    def add_scrim_layer(self, *args) -> None:
        """
        Adds a scrim layer to the parent widget on which the bottom sheet
        will be displayed.
        """

        if not self._scrim_layer and self.type == "modal":
            self._scrim_layer = BottomSheetScrimLayer()
            self.parent.add_widget(self._scrim_layer, index=1)
            self._scrim_layer.bind(on_touch_down=self._on_touch_down_layer)
        if self._scrim_layer and self.type == "standard":
            self.parent.remove_widget(self._scrim_layer)
            self._scrim_layer = None

    def check_max_opening_height(self, *args) -> None:
        if (
            self.max_opening_height
            and self.max_opening_height < self.default_opening_height
        ):
            raise ValueError(
                "The value of `max_opening_height` cannot be less "
                "than the value of `default_opening_height`"
            )

    def check_parent(self, *args) -> None:
        """
        Checks the type of parent widget to which the bottom sheet
        will be added.
        """

        if not issubclass(self.parent.__class__, Screen):
            raise TypeError(
                f"The bottom sheet can only be added to the {Screen} "
                f"or {MDScreen} widgets."
            )

    def dismiss(self, *args) -> None:
        """Dismiss of bottom sheet."""

        anim = Animation(
            y=-self.height,
            d=self.duration_closing if self.animation else 0,
            t=self.closing_transition,
        )
        anim.bind(
            on_complete=lambda x, y: self.dispatch("on_close"),
            on_progress=lambda x, y, z: self.dispatch("on_progress", z),
        )
        anim.start(self)

        # Animation(
        #     radius=[16, 16, 0, 0],
        #     d=self.duration_closing if self.animation else 0,
        # ).start(self)

        if self.type == "modal":
            Animation(
                md_bg_color=self.scrim_layer_color[:-1] + [0],
                d=self.duration_closing if self.animation else 0,
            ).start(self._scrim_layer)

        self.state = "close"

    def expand(self) -> None:
        """Expand of bottom sheet."""

        Animation(
            y=0
            if not self.max_opening_height
            else -(self.height - self.default_opening_height),
            d=self.duration_opening if self.animation else 0,
            t=self.opening_transition,
        ).start(self)

        # Animation(
        #     radius=[0, 0, 0, 0],
        #     d=self.duration_opening if self.animation else 0,
        # ).start(self)

    def open(self, *args) -> None:
        """Opening of bottom sheet."""

        anim = Animation(
            y=-(self.height - self.default_opening_height),
            d=self.duration_opening if self.animation else 0,
            t=self.opening_transition,
        )
        anim.bind(
            on_complete=lambda x, y: self.dispatch("on_open"),
            on_progress=lambda x, y, z: self.dispatch("on_progress", z),
        )
        anim.start(self)

        if self.type == "modal":
            alpha_channel_value = 100 / self.parent.height
            Animation(
                md_bg_color=self.scrim_layer_color[:-1] + [alpha_channel_value],
                d=self.duration_opening if self.animation else 0,
            ).start(self._scrim_layer)

        self.state = "open"

    def clear_content(self) -> None:
        """Removes custom content from the bottom sheet."""

        self.ids.container.clear_widgets()

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDBottomSheetDragHandle):
            self.ids.drag_handle_container.add_widget(widget)
            return
        elif isinstance(widget, MDBottomSheetContent):
            self.ids.container.add_widget(widget)
            return
        return super().add_widget(widget)

    def _set_state(self, y):
        self._state = "none"
        if y < self.height / 2:
            self.dismiss()
        elif y > self.height / 2:
            self.expand()

    def _on_touch_down_layer(self, instance, touch):
        if instance.collide_point(touch.x, touch.y):
            if self._touch_sheet:
                return True

        if self.state == "open" and not self.auto_dismiss:
            return True
        elif self.state == "open" and self.auto_dismiss:
            self.dismiss()
            return True


class MDCustomBottomSheet(MDBottomSheet):
    """
    .. deprecated:: 1.2.0
        Use :class:`~kivymd.uix.bottomsheet.bottomsheet.MDBottomSheet`
        class instead.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Logger.warning(
            "KivyMD: "
            "The `MDCustomBottomSheet` class has been deprecated. "
            "Use the `MDBottomSheet` class instead."
        )


class MDListBottomSheet(MDBottomSheet):
    """
    .. deprecated:: 1.2.0
        Use :class:`~kivymd.uix.bottomsheet.bottomsheet.MDBottomSheet`
        class instead.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Logger.warning(
            "KivyMD: "
            "The `MDListBottomSheet` class has been deprecated. "
            "Use the `MDBottomSheet` class instead."
        )


class MDGridBottomSheet(MDBottomSheet):
    """
    .. deprecated:: 1.2.0
        Use :class:`~kivymd.uix.bottomsheet.bottomsheet.MDBottomSheet`
        class instead.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Logger.warning(
            "KivyMD: "
            "The `MDGridBottomSheet` class has been deprecated. "
            "Use the `MDBottomSheet` class instead."
        )
