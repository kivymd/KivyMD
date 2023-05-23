"""
Components/Toolbar
==================

.. seealso::

    `Material Design spec, App bars: top <https://material.io/components/app-bars-top>`_

    `Material Design spec, App bars: bottom <https://material.io/components/app-bars-bottom/app-bars-bottom.html>`_

    `Material Design 3 spec, App bars: top <https://m3.material.io/components/top-app-bar/overview>`_

    `Material Design 3 spec, App bars: bottom <https://m3.material.io/components/bottom-app-bar/overview>`_

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/app-bar-top.png
    :align: center

`KivyMD` provides the following bar positions for use:

- TopAppBar_
- BottomAppBar_

.. TopAppBar_:
TopAppBar
---------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: "#1E1E15"

        MDTopAppBar:
            title: "MDTopAppBar"

        MDLabel:
            text: "Content"
            halign: "center"
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-1.png
    :align: center

Add left menu
-------------

.. code-block:: kv

    MDTopAppBar:
        title: "MDTopAppBar"
        anchor_title: "left"
        left_action_items: [["menu", lambda x: app.callback()]]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-2.png
    :align: center

.. note::

    The callback is optional. ``left_action_items: [["menu"]]`` would also work for a button that does nothing.

Add right menu
--------------

.. code-block:: kv

    MDTopAppBar:
        title: "MDTopAppBar"
        anchor_title: "left"
        right_action_items: [["dots-vertical", lambda x: app.callback()]]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-3.png
    :align: center

Add two item to the right menu
------------------------------

.. code-block:: kv

    MDTopAppBar:
        title: "MDTopAppBar"
        anchor_title: "left"
        right_action_items:
            [
            ["dots-vertical", lambda x: app.callback_1()],
            ["clock", lambda x: app.callback_2()]
            ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-4.png
    :align: center

Change bar color
----------------

.. code-block:: kv

    MDTopAppBar:
        title: "MDTopAppBar"
        anchor_title: "left"
        md_bg_color: "brown"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-5.png
    :align: center

Change bar text color
---------------------

.. code-block:: kv

    MDTopAppBar:
        title: "MDTopAppBar"
        anchor_title: "left"
        specific_text_color: "white"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-6.png
    :align: center

Shadow elevation control
------------------------

.. code-block:: kv

    MDTopAppBar:
        title: "Elevation 4"
        anchor_title: "left"
        elevation: 4
        shadow_color: "brown"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-7.png
    :align: center

.. BottomAppBar:
BottomAppBar
------------

M2 style bottom app bar
-----------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/app-bar-bottom.png
    :align: center

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDBoxLayout:
        md_bg_color: "#1E1E15"

        # Will always be at the bottom of the screen.
        MDBottomAppBar:

            MDTopAppBar:
                title: "MDBottomAppBar"
                icon: "git"
                type: "bottom"
                left_action_items: [["menu", lambda x: x]]
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.material_style = "M2"
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-8.png
    :align: center

Event on floating button
------------------------

Event ``on_action_button``:

.. code-block:: kv

    MDBottomAppBar:

        MDTopAppBar:
            title: "MDBottomAppBar"
            icon: "git"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]
            on_action_button: app.callback(self.icon)

Floating button position
------------------------

Mode:

- `'free-end'`
- `'free-center'`
- `'end'`
- `'center'`

.. code-block:: kv

    MDBottomAppBar:

        MDTopAppBar:
            title: "MDBottomAppBar"
            icon: "git"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]
            mode: "end"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-9.png
    :align: center

.. code-block:: kv

    MDBottomAppBar:

        MDTopAppBar:
            title: "MDBottomAppBar"
            icon: "git"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]
            mode: "free-end"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-10.png
    :align: center

Custom color
------------

.. code-block:: kv

    MDBottomAppBar:

        MDTopAppBar:
            title: "MDBottomAppBar"
            icon: "git"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]
            icon_color: 0, 1, 0, 1
            md_bg_bottom_color: "brown"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-11.png
    :align: center

M3 style bottom app bar
-----------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/app-bar-bottom-m3.png
    :align: center

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDFloatLayout:
        md_bg_color: "#151511"

        MDBottomAppBar:
            md_bg_color: "#232217"
            icon_color: "#8A8D79"

            MDFabBottomAppBarButton:
                icon: "plus"
                md_bg_color: "#373A22"
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-app-bar-m3-style-1.png
    :align: center

Add action items
----------------

.. code-block:: kv

    #:import MDActionBottomAppBarButton kivymd.uix.toolbar.MDActionBottomAppBarButton


    MDFloatLayout:

        MDBottomAppBar:
            action_items:
                [
                MDActionBottomAppBarButton(icon="gmail"),
                MDActionBottomAppBarButton(icon="label-outline"),
                MDActionBottomAppBarButton(icon="bookmark"),
                ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-app-bar-m3-style-2.png
    :align: center

Change action items
-------------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    #:import MDActionBottomAppBarButton kivymd.uix.toolbar.MDActionBottomAppBarButton


    MDFloatLayout:
        md_bg_color: "#151511"

        MDBottomAppBar:
            id: bottom_appbar
            md_bg_color: "#232217"
            icon_color: "#8A8D79"
            action_items:
                [
                MDActionBottomAppBarButton(icon="gmail"),
                MDActionBottomAppBarButton(icon="bookmark"),
                ]

            MDFabBottomAppBarButton:
                icon: "plus"
                md_bg_color: "#373A22"
                on_release: app.change_actions_items()
    '''


    class Example(MDApp):
        def change_actions_items(self):
            self.root.ids.bottom_appbar.action_items = [
                MDActionBottomAppBarButton(icon="magnify"),
                MDActionBottomAppBarButton(icon="trash-can-outline"),
                MDActionBottomAppBarButton(icon="download-box-outline"),
            ]

        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-app-bar-m3-style-3.gif
    :align: center

A practical example
-------------------

.. code-block:: python

    from kivy.clock import Clock
    from kivy.lang import Builder
    from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
    from kivy.uix.behaviors import FocusBehavior
    from kivy.uix.recycleboxlayout import RecycleBoxLayout
    from kivy.uix.recycleview.layout import LayoutSelectionBehavior
    from kivy.uix.recycleview.views import RecycleDataViewBehavior

    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.uix.toolbar import MDActionBottomAppBarButton
    from kivymd.app import MDApp
    from kivymd.utils import asynckivy

    from faker import Faker  # pip install Faker

    KV = '''
    #:import MDFabBottomAppBarButton kivymd.uix.toolbar.MDFabBottomAppBarButton


    <UserCard>
        orientation: "vertical"
        adaptive_height: True
        md_bg_color: "#373A22" if self.selected else "#1F1E15"
        radius: 16
        padding: 0, 0, 0, "16dp"

        TwoLineAvatarListItem:
            divider: None
            _no_ripple_effect: True
            text: root.name
            secondary_text: root.time
            theme_text_color: "Custom"
            text_color: "#8A8D79"
            secondary_theme_text_color: self.theme_text_color
            secondary_text_color: self.text_color

            ImageLeftWidget:
                source: root.avatar
                radius: self.height / 2

        MDLabel:
            text: root.text
            adaptive_height: True
            theme_text_color: "Custom"
            text_color: "#8A8D79"
            padding_x: "16dp"
            shorten: True
            shorten_from: "right"

        Widget:


    MDFloatLayout:
        md_bg_color: "#151511"

        RecycleView:
            id: card_list
            viewclass: "UserCard"

            SelectableRecycleGridLayout:
                orientation: 'vertical'
                spacing: "16dp"
                padding: "16dp"
                default_size: None, dp(120)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                multiselect: True
                touch_multiselect: True

        MDBottomAppBar:
            id: bottom_appbar
            scroll_cls: card_list
            allow_hidden: True
            md_bg_color: "#232217"
            icon_color: "#8A8D79"

            MDFabBottomAppBarButton:
                id: fab_button
                icon: "plus"
                md_bg_color: "#373A22"
    '''


    class UserCard(RecycleDataViewBehavior, MDBoxLayout):
        name = StringProperty()
        time = StringProperty()
        text = StringProperty()
        avatar = StringProperty()
        callback = ObjectProperty(lambda x: x)

        index = None
        selected = BooleanProperty(False)
        selectable = BooleanProperty(True)

        def refresh_view_attrs(self, rv, index, data):
            self.index = index
            return super().refresh_view_attrs(rv, index, data)

        def on_touch_down(self, touch):
            if super().on_touch_down(touch):
                return True
            if self.collide_point(*touch.pos) and self.selectable:
                Clock.schedule_once(self.callback)
                return self.parent.select_with_touch(self.index, touch)

        def apply_selection(self, rv, index, is_selected):
            self.selected = is_selected
            rv.data[index]["selected"] = is_selected


    class SelectableRecycleGridLayout(
        FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout
    ):
        pass


    class Test(MDApp):
        selected_cards = False

        def build(self):
            return Builder.load_string(KV)

        def on_tap_card(self, *args):
            datas = [data["selected"] for data in self.root.ids.card_list.data]
            if True in datas and not self.selected_cards:
                self.root.ids.bottom_appbar.action_items = [
                    MDActionBottomAppBarButton(icon="gmail"),
                    MDActionBottomAppBarButton(icon="label-outline"),
                    MDActionBottomAppBarButton(icon="bookmark"),
                ]
                self.root.ids.fab_button.icon = "pencil"
                self.selected_cards = True
            else:
                if len(list(set(datas))) == 1 and not list(set(datas))[0]:
                    self.selected_cards = False
                if not self.selected_cards:
                    self.root.ids.bottom_appbar.action_items = [
                        MDActionBottomAppBarButton(icon="magnify"),
                        MDActionBottomAppBarButton(icon="trash-can-outline"),
                        MDActionBottomAppBarButton(icon="download-box-outline"),
                    ]
                    self.root.ids.fab_button.icon = "plus"

        def on_start(self):
            async def generate_card():
                for i in range(10):
                    await asynckivy.sleep(0)
                    self.root.ids.card_list.data.append(
                        {
                            "name": fake.name(),
                            "time": fake.date(),
                            "avatar": fake.image_url(),
                            "text": fake.text(),
                            "selected": False,
                            "callback": self.on_tap_card,
                        }
                    )

            self.on_tap_card()
            fake = Faker()
            Clock.schedule_once(lambda x: asynckivy.start(generate_card()))


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-app-bar-m3-style-4.gif
    :align: center

Tooltips
--------

You can add MDTooltips to the icons by adding a text string to the bar item,
as shown below:

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.snackbar import Snackbar

    KV = '''
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "MDTopAppBar"
            left_action_items: [["menu", "This is the navigation"]]
            right_action_items:
                [
                [
                "dots-vertical",
                lambda x: app.callback(x),
                "this is the More Actions"
                ]
                ]

        MDLabel:
            text: "Content"
            halign: "center"
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.material_style = "M2"
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return Builder.load_string(KV)

        def callback(self, button):
            Snackbar(text="Hello World").open()


    Example().run()

M3 style top app bar
--------------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.toolbar import MDTopAppBar

    KV = '''
    MDScreen:

        MDBoxLayout:
            id: box
            orientation: "vertical"
            spacing: "12dp"
            pos_hint: {"top": 1}
            adaptive_height: True
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return Builder.load_string(KV)

        def on_start(self):
            for type_height in ["medium", "large", "small"]:
                self.root.ids.box.add_widget(
                    MDTopAppBar(
                        type_height=type_height,
                        headline_text=f"Headline {type_height.lower()}",
                        md_bg_color="brown",
                        left_action_items=[["arrow-left", lambda x: x]],
                        right_action_items=[
                            ["attachment", lambda x: x],
                            ["calendar", lambda x: x],
                            ["dots-vertical", lambda x: x],
                        ],
                        title="Title" if type_height == "small" else "",
                        anchor_title="left",
                    )
                )


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-m3.png
    :align: center
"""

from __future__ import annotations

__all__ = (
    "MDTopAppBar",
    "MDBottomAppBar",
    "MDActionBottomAppBarButton",
    "MDFabBottomAppBarButton",
    "MDActionOverFlowButton",
)

import os
from math import cos, radians, sin
from typing import Union

from kivy import Logger
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView

from kivymd import uix_path
from kivymd.color_definitions import text_colors
from kivymd.material_resources import TOP_APP_BAR_ELEVATION
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    CommonElevationBehavior,
    DeclarativeBehavior,
    RotateBehavior,
    ScaleBehavior,
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.button import MDFloatingActionButton, MDIconButton
from kivymd.uix.controllers import WindowController
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tooltip import MDTooltip
from kivymd.utils import asynckivy
from kivymd.utils.set_bars_colors import set_bars_colors

with open(
    os.path.join(uix_path, "toolbar", "toolbar.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDFabBottomAppBarButton(
    MDFloatingActionButton, RotateBehavior, ScaleBehavior, MDTooltip
):
    """
    Implements a floating action button (FAB) for a bar with type 'bottom'.

    For more information, see in the
    :class:`~kivymd.uix.button.MDFloatingActionButton` and
    :class:`~kivymd.uix.behaviors.RotateBehavior` and
    :class:`~kivymd.uix.behaviors.ScaleBehavior` and
    :class:`~kivymd.uix.tooltip.MDTooltip`
    classes documentation.
    """

    def set__radius(self, *args) -> None:
        super().set__radius()
        if self.theme_cls.material_style == "M3":
            self.elevation = 0


class ActionTopAppBarButton(MDIconButton, MDTooltip):
    """
    Implements action buttons on the bar.

    For more information, see in the
    :class:`~kivymd.uix.button.MDIconButton` and
    :class:`~kivymd.uix.tooltip.MDTooltip`
    classes documentation.
    """

    # The text of the menu item of the corresponding action button that will
    # be displayed in the `OverFlowMenu` menu.
    overflow_text = StringProperty()


class MDActionBottomAppBarButton(ActionTopAppBarButton):
    """
    Implements action buttons for a :class:'MDBottomAppBar' class.

    .. versionadded:: 1.2.0

    For more information, see in the
    :class:`~kivymd.uix.button.MDIconButton` and
    :class:`~kivymd.uix.tooltip.MDTooltip`
    classes documentation.
    """


class MDActionOverFlowButton(ActionTopAppBarButton):
    """
    Implements a bar action button for the `OverFlowMenu` menu.

    For more information, see in the
    :class:`~kivymd.uix.button.MDIconButton` and
    :class:`~kivymd.uix.tooltip.MDTooltip`
    classes documentation.
    """

    icon = "dots-vertical"


class OverFlowMenu(MDDropdownMenu):
    """
    Implements a menu for the items (:class:`~OverFlowMenuItem`) of the
    corresponding action buttons.
    """


class OverFlowMenuItem(OneLineIconListItem):
    """Implements a menu (:class:`~OverFlowMenu`) item."""

    icon = StringProperty()


class NotchedBox(
    ThemableBehavior,
    CommonElevationBehavior,
    SpecificBackgroundColorBehavior,
    BoxLayout,
):
    elevation = NumericProperty(TOP_APP_BAR_ELEVATION)
    notch_radius = NumericProperty()
    notch_center_x = NumericProperty("100dp")

    _indices_right = ListProperty()
    _vertices_right = ListProperty()
    _indices_left = ListProperty()
    _vertices_left = ListProperty()
    _rounded_rectangle_height = NumericProperty("6dp")
    _total_angle = NumericProperty(180)
    _rectangle_left_pos = ListProperty([0, 0])
    _rectangle_left_width = NumericProperty()
    _rectangle_right_pos = ListProperty([0, 0])
    _rectangle_right_width = NumericProperty()
    _rounding_percentage = NumericProperty(0.15)
    _shift = NumericProperty(dp(4))

    def __init__(self, **kw):
        super().__init__(**kw)
        self.bind(
            size=self._update_canvas,
            pos=self._update_canvas,
            notch_radius=self._update_canvas,
            notch_center_x=self._update_canvas,
        )
        Clock.schedule_once(self._update_canvas)

    def _update_canvas(self, *args):
        pos = self.pos
        size = [
            self.width,
            self.size[1] - self._rounded_rectangle_height / 2,
        ]
        notch_center_x = self.pos[0] + self.notch_center_x
        circle_radius = self.notch_radius
        degree_diff = int((180 - self._total_angle) / 2)
        circle_center = [notch_center_x, pos[1] + size[1]]
        left_circle_pos = self._points_on_circle(
            circle_center, circle_radius, 180 + degree_diff, 270
        )

        self._rectangle_left_pos = [
            pos[0],
            pos[1] + size[1] - self._rounded_rectangle_height / 2,
        ]
        self._rectangle_left_width = left_circle_pos[0][0] - self.pos[0]

        right_circle_pos = self._points_on_circle(
            circle_center, circle_radius, -degree_diff, -90
        )

        self._rectangle_right_pos = [
            right_circle_pos[0][0],
            pos[1] + size[1] - self._rounded_rectangle_height / 2,
        ]
        self._rectangle_right_width = pos[0] + size[0] - right_circle_pos[0][0]

        raw_vertices_left = self._make_vertices(
            pos, [notch_center_x - pos[0], size[1]], "left", left_circle_pos
        )
        raw_vertices_right = self._make_vertices(
            [notch_center_x, pos[1]],
            [size[0] + pos[0] - notch_center_x, size[1]],
            "right",
            right_circle_pos,
        )

        left_vertices, left_indices = self._make_vertices_indices(
            raw_vertices_left
        )
        right_vertices, right_indices = self._make_vertices_indices(
            raw_vertices_right
        )

        self._update_mesh(left_vertices, left_indices, "left")
        self._update_mesh(right_vertices, right_indices, "right")

    def _update_mesh(self, vertices, indices, mode):
        if mode == "left":
            self._indices_left = indices
            self._vertices_left = vertices
        else:
            self._indices_right = indices
            self._vertices_right = vertices
        return True

    @staticmethod
    def _make_vertices_indices(points_list):
        vertices = []
        indices = []
        for index, point in enumerate(points_list):
            indices.append(index)
            vertices.extend([point[0], point[1], 0, 0])

        return [vertices, indices]

    @staticmethod
    def _make_vertices(rectangle_pos, rectangle_size, mode, notch_points=[]):
        x = rectangle_pos[0]
        y = rectangle_pos[1]
        w = rectangle_size[0]
        h = rectangle_size[1]

        if mode == "left":
            rectangle_vertices = [[x, y], [x, y + h]]
        elif mode == "right":
            rectangle_vertices = [[x + w, y], [x + w, y + h]]
        rectangle_vertices.extend(notch_points)
        if mode == "left":
            rectangle_vertices.extend([[x + w, y]])
        elif mode == "right":
            rectangle_vertices.extend([[x, y]])

        return rectangle_vertices

    @staticmethod
    def _points_on_circle(center, radius, start_angle, end_angle):
        points = []
        y_diff = False
        if end_angle >= 180:
            step = 1
            end_angle += 1
        elif end_angle <= 0:
            step = -1
            end_angle -= 1
        else:
            raise Exception("Invalid value for start angle")

        for degree in range(start_angle, end_angle, step):
            angle = radians(degree)
            x = center[0] + (radius * cos(angle))
            y = center[1] + (radius * sin(angle))

            if y_diff is False:
                y_diff = abs(y - center[1])

            y += y_diff
            points.append([x, y])

        return points


class MDTopAppBar(DeclarativeBehavior, NotchedBox, WindowController):
    """
    Top app bar class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.DeclarativeBehavior` and
    :class:`~NotchedBox` and
    :class:`~kivymd.uix.controllers.WindowController`
    classes documentation.

    :Events:
        `on_action_button`
            Method for the button used for the :class:`~MDBottomAppBar` class.
    """

    left_action_items = ListProperty()
    """
    The icons on the left of the bar.
    To add one, append a list like the following:

    .. code-block:: kv

        MDTopAppBar:
            left_action_items:
                ["dots-vertical", callback, "tooltip text", "overflow text"]

    ``icon_name`` - is a string that corresponds to an icon definition:

    .. code-block:: kv

        MDTopAppBar:
            right_action_items: [["home"]]

    ``callback`` - is the function called on a touch release event and:

    .. code-block:: kv

        MDTopAppBar:
            right_action_items: [["home", lambda x: app.callback(x)]]

    .. code-block:: python

        class Test(MDApp):
            def callback(self, instance_action_top_appbar_button):
                print(instance_action_top_appbar_button)

    ``tooltip text`` - is the text to be displayed in the tooltip:

    .. code-block:: kv

        MDTopAppBar:
            right_action_items:
                [
                ["home", lambda x: app.callback(x), "Home"],
                ["message-star", lambda x: app.callback(x), "Message star"],
                ["message-question", lambda x: app.callback(x), "Message question"],
                ["message-reply", lambda x: app.callback(x), "Message reply"],
                ]

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-tooltip-text.png
        :align: center

    ``overflow text`` - is the text for menu items (:class:`~OverFlowMenuItem`)
    of the corresponding action buttons:

    .. code-block:: kv

        MDTopAppBar:
            use_overflow: True
            right_action_items:
                [
                ["home", lambda x: x, "", "Home"],
                ["message-star", lambda x: x, "", "Message star"],
                ["message-question", lambda x: x, "" , "Message question"],
                ["message-reply", lambda x: x, "", "Message reply"],
                ]

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-overflow-text.png
        :align: center

    ``icon color`` - icon color:

    .. code-block:: kv

        MDTopAppBar:
            right_action_items:
                [
                [
                "dots-vertical",
                callback,
                "tooltip text",
                "overflow text",
                (1, 1, 1, 1),
                ]
                ]

    Both the ``callback`` and ``tooltip text`` and ``overflow text`` and ``icon color`` are
    optional but the order must be preserved.

    :attr:`left_action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    right_action_items = ListProperty()
    """
    The icons on the left of the bar.
    Works the same way as :attr:`left_action_items`.

    :attr:`right_action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    title = StringProperty()
    """
    Text app bar.

    .. code-block:: kv

        MDTopAppBar:
            title: "MDTopAppBar"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-title.png
        :align: center

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    mode = OptionProperty(
        "center", options=["free-end", "free-center", "end", "center"]
    )
    """
    Floating button position. Only for :class:`~MDBottomAppBar` class.
    Available options are: `'free-end'`, `'free-center'`, `'end'`, `'center'`.

    .. rubric:: Mode "end":

    .. code-block:: kv

        MDBottomAppBar:

            MDTopAppBar:
                title: "Title"
                icon: "git"
                type: "bottom"
                left_action_items: [["menu", lambda x: x]]
                mode: "end"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-9.png
        :align: center

    .. rubric:: Mode "free-end":

    .. code-block:: kv

        MDBottomAppBar:

            MDTopAppBar:
                mode: "free-end"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-10.png
        :align: center

    .. rubric:: Mode "free-center":

    .. code-block:: kv

        MDBottomAppBar:

            MDTopAppBar:
                mode: "free-center"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-free-center.png
        :align: center

    .. rubric:: Mode "center":

    .. code-block:: kv

        MDBottomAppBar:

            MDTopAppBar:
                mode: "center"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-center.png
        :align: center

    :attr:`mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'center'`.
    """

    type = OptionProperty("top", options=["top", "bottom"])
    """
    When using the :class:`~MDBottomAppBar` class, the parameter ``type``
    must be set to `'bottom'`:

    .. code-block:: kv

        MDBottomAppBar:

            MDTopAppBar:
                type: "bottom"

    Available options are: `'top'`, `'bottom'`.

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'top'`.
    """

    opposite_colors = BooleanProperty(False)
    """
    Changes the color of the label to the color opposite to the main theme.

    .. code-block:: kv

        MDTopAppBar:
            opposite_colors: True

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-opposite-true.png
        :align: center

    .. code-block:: kv

        MDTopAppBar:
            opposite_colors: False

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-opposite-false.png
        :align: center
    """

    md_bg_bottom_color = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format for the bar with the
    ``bottom`` mode.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDBottomAppBar:

            MDTopAppBar:
                md_bg_bottom_color: "brown"
                icon_color: self.md_bg_bottom_color

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-md-bg-bottom-color.png
        :align: center

    :attr:`md_bg_bottom_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    set_bars_color = BooleanProperty(False)
    """
    If `True` the background color of the bar status will be set automatically
    according to the current color of the bar.

    .. versionadded:: 1.0.0

    See `set_bars_colors <https://kivymd.readthedocs.io/en/latest/api/kivymd/utils/set_bars_colors/>`_
    for more information.

    :attr:`set_bars_color` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    use_overflow = BooleanProperty(False)
    """
    As a top app bar is resized, actions move to the overflow menu from right
    to left.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDTopAppBar:
            title: "MDTopAppBar"
            use_overflow: True
            right_action_items:
                [
                ["home", lambda x: x, "Home", "Home"],
                ["message-star", lambda x: x, "Message star", "Message star"],
                ["message-question", lambda x: x, "Message question", "Message question"],
                ["message-reply", lambda x: x, "Message reply", "Message reply"],
                ]

    :attr:`use_overflow` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    overflow_cls = ObjectProperty()
    """
    Must be an object of the :class:`~kivymd.uix.menu.MDDropdownMenu' class.
    See :class:`~kivymd.uix.menu.MDDropdownMenu` class documentation for more
    information.

    .. versionadded:: 1.0.0

    .. code-block:: python

        from kivy.lang import Builder

        from kivymd.app import MDApp
        from kivymd.uix.menu import MDDropdownMenu

        KV = '''
        #:import CustomOverFlowMenu __main__.CustomOverFlowMenu


        MDBoxLayout:
            orientation: "vertical"

            MDTopAppBar:
                title: "MDTopAppBar"
                use_overflow: True
                overflow_cls: CustomOverFlowMenu()
                right_action_items:
                    [
                    ["home", lambda x: x, "Home", "Home"],
                    ["message-star", lambda x: x, "Message star", "Message star"],
                    ["message-question", lambda x: x, "Message question", "Message question"],
                    ["message-reply", lambda x: x, "Message reply", "Message reply"],
                    ]

            MDLabel:
                text: "Content"
                halign: "center"
        '''


        class CustomOverFlowMenu(MDDropdownMenu):
            # In this class you can set custom properties for the overflow menu.
            pass


        class Example(MDApp):
            def build(self):
                return Builder.load_string(KV)

            def callback(self, instance_action_top_appbar_button):
                print(instance_action_top_appbar_button)


        Example().run()

    :attr:`overflow_cls` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    # Attributes only for the BottomAppBar class.

    icon = StringProperty()
    """
    Floating button. Only for :class:`~MDBottomAppBar` class.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    icon_color = ColorProperty()
    """
    Color in (r, g, b, a) or string format action button. Only for
    :class:`~MDBottomAppBar` class.

    :attr:`icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[]`.
    """

    # MD3 Style attributes.

    anchor_title = OptionProperty(None, options=["left", "center", "right"])
    """
    Position bar title. Only used with `material_style = 'M3'`
    Available options are: `'left'`, `'center'`, `'right'`.

    :attr:`anchor_title` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    headline_text = StringProperty()
    """
    Headline text bar.

    .. versionadded:: 1.0.0

    :attr:`headline_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    headline_text_color = ColorProperty(None)
    """
    Headline text color in (r, g, b, a) or string format.

    .. versionadded:: 1.0.0

    :attr:`headline_text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    type_height = OptionProperty("small", options=["medium", "large", "small"])
    """
    Bar height type.

    .. versionadded:: 1.0.0

    Available options are: 'medium', 'large', 'small'.

    :attr:`type_height` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'small'`.
    """

    # List of action buttons (ActionTopAppBarButton instance) that have been
    # .added to the overflow
    _hidden_items = []
    # See `kivymd.uix.menu.MDDropdownMenu.items` attribute.
    _overflow_menu_items = []

    def __init__(self, **kwargs):
        self.action_button = MDFabBottomAppBarButton()
        super().__init__(**kwargs)
        self.register_event_type("on_action_button")

        if not self.icon_color:
            self.icon_color = self.theme_cls.primary_color

        self.bind(specific_text_color=self.update_action_bar_text_colors)
        self.theme_cls.bind(
            material_style=self.update_bar_height,
            primary_palette=self.update_md_bg_color,
        )

        Clock.schedule_once(
            lambda x: self.on_left_action_items(0, self.left_action_items)
        )
        Clock.schedule_once(
            lambda x: self.on_right_action_items(0, self.right_action_items)
        )
        Clock.schedule_once(lambda x: self.set_md_bg_color(0, self.md_bg_color))
        Clock.schedule_once(lambda x: self.on_type_height(0, self.type_height))
        Clock.schedule_once(
            lambda x: self.update_anchor_title(self.theme_cls.material_style)
        )
        Clock.schedule_once(self.update_floating_radius)
        Clock.schedule_once(self.check_overflow_cls)

    def set_headline_font_style(self, interval: Union[int, float]) -> None:
        if self.type_height in ("medium", "large"):
            self.ids.label_headline.font_style = {
                "medium": "H6",
                "large": "H5",
            }[self.type_height]

    def on_width(self, instance_toolbar, width: float) -> None:
        """
        Called when the bar is resized (size of the application window).
        """

        if self.mode == "center":
            self.action_button.x = width / 2 - self.action_button.width / 2
        else:
            self.action_button.x = width - self.action_button.width * 2

        # The user reduces the width of the window.
        if (
            self.get_window_width_resizing_direction() == "left"
            and self.use_overflow
            and self.ids.label_title.is_shortened
        ):
            if not self.overflow_action_button_is_added():
                self.add_overflow_button()
            self.add_action_button_to_overflow()
        # The user increases the width of the window.
        if (
            self.get_window_width_resizing_direction() == "right"
            and self.use_overflow
            and not self.ids.label_title.is_shortened
            and self.overflow_cls.items
        ):
            self.return_action_button_to_toolbar()

    def return_action_button_to_toolbar(self) -> None:
        if len(self._hidden_items):
            action_button = self._hidden_items.pop()
            self.ids.right_actions.add_widget(action_button, index=1)
            self.update_overflow_menu_items(action_button)
            if not len(self._hidden_items):
                self.remove_overflow_button()

    def remove_overflow_button(self) -> None:
        """Removes an overflow button to the bar."""

        if self.overflow_action_button_is_added():
            action_overflow_button = self.ids.right_actions.children[0]
            self.ids.right_actions.remove_widget(action_overflow_button)
            self._overflow_menu_items = []

    def add_overflow_button(self) -> None:
        """Adds an overflow button to the bar."""

        self.ids.right_actions.add_widget(
            MDActionOverFlowButton(
                theme_text_color="Custom"
                if not self.opposite_colors
                else "Primary",
                text_color=self.specific_text_color,
                opposite_colors=self.opposite_colors,
                on_release=lambda x: self.overflow_cls.open(),
            )
        )

    def overflow_action_button_is_added(self) -> bool:
        """
        Returns `True` if at least one action button
        (:class:`~ActionTopAppBarButton') on the bar is added to the
        overflow.
        """

        if (
            not self.ids.right_actions.children[0].__class__
            is MDActionOverFlowButton
        ):
            return False
        return True

    def add_action_button_to_overflow(self):
        """Adds an overflow button to the bar."""

        if len(self.ids.right_actions.children) > 1:
            button_to_be_added = self.ids.right_actions.children[1]
            self._hidden_items.append(button_to_be_added)
            self.ids.right_actions.remove_widget(button_to_be_added)

            self._overflow_menu_items.append(
                {
                    "viewclass": "OverFlowMenuItem",
                    "icon": button_to_be_added.icon,
                    "text": button_to_be_added.overflow_text,
                    "height": dp(48),
                    "on_press": lambda *x: button_to_be_added.on_release(*x),
                }
            )
            self.overflow_cls.items = self._overflow_menu_items
            self.overflow_cls.caller = self.ids.right_actions.children[0]

    def check_overflow_cls(self, interval: Union[int, float]) -> None:
        """
        If the user does not set the :attr:`overflow_cls` attribute but uses
        overflows, the :attr:`overflow_cls` attribute will use the default
        value.
        """

        if not self.overflow_cls:
            self.overflow_cls = self.get_default_overflow_cls()

    def on_type(self, instance_toolbar, type_value: str) -> None:
        """Called when the value of the  :attr:`type` attribute changes."""

        if type_value == "bottom":
            self.action_button.bind(center_x=self.setter("notch_center_x"))
            self.action_button.bind(
                on_release=lambda x: self.dispatch("on_action_button")
            )
            self.action_button.x = (
                Window.width / 2 - self.action_button.width / 2
            )
            self.action_button.y = (
                (self.center[1] - self.height / 2)
                + self.theme_cls.standard_increment / 2
                + self._shift
            )
            self.shadow_offset = [0, 30]
            self.on_mode(None, self.mode)

    def on_type_height(self, instance_toolbar, height_type_value: str) -> None:
        """
        Called when the value of the  :attr:`type_height` attribute changes.
        """

        if self.theme_cls.material_style == "M2":
            self.height = self.theme_cls.standard_increment
        else:
            if self.type != "bottom":
                if height_type_value == "small":
                    self.height = dp(64)
                elif height_type_value == "medium":
                    self.height = dp(112)
                elif height_type_value == "large":
                    self.height = dp(152)
            else:
                self.height = self.theme_cls.standard_increment
        Clock.schedule_once(self.set_headline_font_style)

    def on_action_button(self, *args):
        """
        Method for the button used for the :class:`~MDBottomAppBar` class.
        """

    def on_overflow_cls(
        self, instance_toolbar, instance_overflow_cls: MDDropdownMenu
    ) -> None:
        """
        Called when the value of the  :attr:`overflow_cls` attribute changes.
        """

        self.overflow_cls = instance_overflow_cls

    def on_md_bg_color(self, instance_toolbar, color_value: list) -> None:
        """
        Called when the value of the  :attr:`md_bg_color` attribute changes.
        """

        def on_md_bg_color(interval: Union[int, float]):
            if self.type == "bottom":
                self.md_bg_color = [0, 0, 0, 0]
            else:
                if self.set_bars_color:
                    set_bars_colors(
                        color_value, None, self.theme_cls.theme_style
                    )

        Clock.schedule_once(on_md_bg_color)

    def on_left_action_items(self, instance_toolbar, items_value: list) -> None:
        """
        Called when the value of the  :attr:`left_action_items` attribute
        changes.
        """

        def on_left_action_items(interval: Union[int, float]):
            self.update_action_bar(self.ids.left_actions, items_value)

        Clock.schedule_once(on_left_action_items)

    def on_right_action_items(
        self, instance_toolbar, items_value: list
    ) -> None:
        """
        Called when the value of the  :attr:`right_action_items` attribute
        changes.
        """

        def on_right_actions(interval: Union[int, float]):
            self.update_action_bar(self.ids.right_actions, items_value)

        Clock.schedule_once(on_right_actions)

    def on_icon(self, instance_toolbar, icon_name: str) -> None:
        """Called when the value of the  :attr:`icon` attribute changes."""

        self.action_button.icon = icon_name

    def on_icon_color(self, instance, icon_name: str) -> None:
        """
        Called when the value of the  :attr:`icon_color` attribute changes.
        """

        self.action_button.md_bg_color = icon_name

    def on_md_bg_bottom_color(
        self, instance_toolbar, color_value: list
    ) -> None:
        """
        Called when the value of the  :attr:`md_bg_bottom_color` attribute
        changes.
        """

        set_bars_colors(None, color_value, self.theme_cls.theme_style)

    def on_anchor_title(self, instance_toolbar, anchor_value: str) -> None:
        """
        Called when the value of the  :attr:`anchor_title` attribute changes.
        """

        def on_anchor_title(interval: Union[int, float]):
            self.ids.label_title.halign = anchor_value

        Clock.schedule_once(on_anchor_title)

    def on_mode(self, instance_toolbar, mode_value: str) -> None:
        """Called when the value of the  :attr:`made` attribute changes."""

        if self.type == "top":
            return

        def on_mode(interval: Union[int, float]):
            def set_button_pos(*args):
                self.action_button.x = x
                self.action_button.y = y - self._rounded_rectangle_height / 2
                self.action_button._hard_shadow_size = (0, 0)
                self.action_button._soft_shadow_size = (0, 0)
                anim = Animation(
                    scale_value_x=1, scale_value_y=1, scale_value_z=1, d=0.05
                )
                anim.bind(on_complete=self.set_shadow)
                anim.start(self.action_button)

            if mode_value == "center":
                self.set_notch()
                x = Window.width / 2 - self.action_button.width / 2
                y = (
                    (self.center[1] - self.height / 2)
                    + self.theme_cls.standard_increment / 2
                    + self._shift
                )
            elif mode_value == "end":
                self.set_notch()
                x = Window.width - self.action_button.width * 2
                y = (
                    (self.center[1] - self.height / 2)
                    + self.theme_cls.standard_increment / 2
                    + self._shift
                )
                self.right_action_items = []
            elif mode_value == "free-end":
                self.remove_notch()
                x = Window.width - self.action_button.width - dp(10)
                y = self.action_button.height + self.action_button.height / 2
            elif mode_value == "free-center":
                self.remove_notch()
                x = Window.width / 2 - self.action_button.width / 2
                y = self.action_button.height + self.action_button.height / 2
            self.remove_shadow()
            anim = Animation(
                scale_value_x=0, scale_value_y=0, scale_value_z=0, d=0.1
            )
            anim.bind(on_complete=set_button_pos)
            anim.start(self.action_button)

        Clock.schedule_once(on_mode)

    def set_md_bg_color(self, instance_toolbar, color_value: list) -> None:
        if color_value == [1.0, 1.0, 1.0, 0.0]:
            self.md_bg_color = self.theme_cls.primary_color

    def set_notch(self) -> None:
        anim = Animation(d=0.1) + Animation(
            notch_radius=self.action_button.width / 2 + dp(8),
            d=0.1,
        )
        anim.start(self)

    def set_shadow(self, *args) -> None:
        self.action_button._elevation = self.action_button.elevation

    def get_default_overflow_cls(self) -> OverFlowMenu:
        return OverFlowMenu(width_mult=4)

    def update_overflow_menu_items(self, action_button) -> None:
        for data in self.overflow_cls.items:
            if data["icon"] == action_button.icon:
                self.overflow_cls.items.remove(data)
                break

    def update_bar_height(
        self, instance_theme_manager, material_style_value: str
    ) -> None:
        self.on_type_height(self, self.type_height)
        self.update_anchor_title(material_style_value)

    def update_floating_radius(self, interval: Union[int, float]) -> None:
        self.action_button.radius = self.action_button.width / 2

    def update_anchor_title(self, material_style_value: str) -> str:
        if material_style_value == "M2":
            self.anchor_title = "left"
        elif material_style_value == "M3" and self.type != "bottom":
            if not self.anchor_title:
                self.anchor_title = "center"
        elif material_style_value == "M3" and self.type == "bottom":
            self.anchor_title = "left"
        return self.anchor_title

    def update_action_bar(
        self, instance_box_layout, action_bar_items: list
    ) -> None:
        instance_box_layout.clear_widgets()
        new_width = 0

        for item in action_bar_items:
            new_width += dp(48)
            if len(item) == 1:
                item.append(lambda x: None)
            if len(item) > 1 and not item[1]:
                item[1] = lambda x: None
            if len(item) == 2:
                if isinstance(item[1], str) or isinstance(item[1], tuple):
                    item.insert(1, lambda x: None)
                else:
                    item.append("")
            if len(item) == 3:
                if isinstance(item[2], tuple):
                    item.insert(2, "")

            instance_box_layout.add_widget(
                ActionTopAppBarButton(
                    icon=item[0],
                    on_release=item[1],
                    tooltip_text=item[2],
                    overflow_text=item[3]
                    if (len(item) == 4 and isinstance(item[3], str))
                    else "",
                    theme_text_color="Custom"
                    if not self.opposite_colors
                    else "Primary",
                    text_color=self.specific_text_color
                    if not (len(item) == 4 and isinstance(item[3], tuple))
                    else item[3],
                    opposite_colors=self.opposite_colors,
                )
            )

        instance_box_layout.width = new_width

    def update_md_bg_color(self, *args) -> None:
        self.md_bg_color = self.theme_cls._get_primary_color()

    def update_action_bar_text_colors(self, *args) -> None:
        for child in self.ids.left_actions.children:
            child.text_color = self.specific_text_color
        for child in self.ids.right_actions.children:
            child.text_color = self.specific_text_color

    def remove_notch(self) -> None:
        anim = Animation(d=0.1) + Animation(notch_radius=0, d=0.1)
        anim.start(self)

    def remove_shadow(self) -> None:
        self.action_button._elevation = 0

    def _update_specific_text_color(self, instance, value):
        if self.specific_text_color in (
            [0.0, 0.0, 0.0, 0.87],
            [0.0, 0.0, 0.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
        ):
            self.specific_text_color = text_colors[
                self.theme_cls.primary_palette
            ][self.theme_cls.primary_hue]


class MDBottomAppBar(
    DeclarativeBehavior,
    ThemableBehavior,
    SpecificBackgroundColorBehavior,
    CommonElevationBehavior,
    FloatLayout,
):
    """
    Bottom app bar class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.SpecificBackgroundColorBehavior` and
    :class:`~kivymd.uix.behaviors.CommonElevationBehavior` and
    :class:`~kivy.uix.floatlayout.FloatLayout`
    classes documentation.

    :Events:
        `on_show_bar`
            The method is called when the :class:`~MDBottomAppBar` panel
            is shown.
        `on_hide_bar`
            The method is called when the :class:`~MDBottomAppBar` panel
            is hidden.
    """

    md_bg_color = ColorProperty([0, 0, 0, 0])
    """
    Color bar in (r, g, b, a) or string format.

    :attr:`md_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    icon_color = ColorProperty(None)
    """
    Color bar in (r, g, b, a) or string format.

    .. versionadded:: 1.2.0

    :attr:`icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    action_items = ListProperty()
    """
    The icons on the left bar.

    .. versionadded:: 1.2.0

    :attr:`action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    animation = BooleanProperty(True)
    """
    # TODO: add description.
    # FIXME: changing the value does not affect anything.

    .. versionadded:: 1.2.0

    :attr:`animation` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    show_transition = StringProperty("linear")
    """
    Type of button display transition.

    .. versionadded:: 1.2.0

    :attr:`show_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'linear'`.
    """

    hide_transition = StringProperty("in_back")
    """
    Type of button hidden transition.

    .. versionadded:: 1.2.0

    :attr:`hide_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'in_back'`.
    """

    hide_duration = NumericProperty(0.4)
    """
    Duration of button hidden transition.

    .. versionadded:: 1.2.0

    :attr:`hide_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    show_duration = NumericProperty(0.2)
    """
    Duration of button display transition.

    .. versionadded:: 1.2.0

    :attr:`show_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    scroll_cls = ObjectProperty()
    """
    Widget inherited from the :class:`~kivy.uix.scrollview.ScrollView` class.
    The value must be set if the :attr:`allow_hidden` parameter is `True`.

    .. versionadded:: 1.2.0

    :attr:`scroll_cls` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    allow_hidden = BooleanProperty(False)
    """
    Allows or disables hiding the panel when scrolling content.
    If the value is `True`, the :attr:`scroll_cls` parameter must be specified.

    .. versionadded:: 1.2.0

    :attr:`allow_hidden` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    bar_is_hidden = BooleanProperty(False)
    """
    Is the panel currently hidden.

    .. versionadded:: 1.2.0

    :attr:`bar_is_hidden` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _padding = dp(16)
    _x = -dp(48)
    _scroll_cls_y = 0
    _cache = []
    _current_data = []
    _wait_removed = False
    _animated_hidden = True
    _animated_show = True
    _fab_bottom_app_bar_button = None
    _action_overflow_button = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint_y = None
        if self.theme_cls.material_style == "M3":
            self.register_event_type("on_show_bar")
            self.register_event_type("on_hide_bar")

            self.height = dp(80)
            Clock.schedule_once(self.set_bg_color)

    def button_centering_animation(
        self,
        button: MDActionOverFlowButton
        | MDActionBottomAppBarButton
        | MDFabBottomAppBarButton,
    ) -> None:
        """
        Animation of centering buttons for
        :class:`~MDActionOverFlowButton`,
        :class:`~MDActionBottomAppBarButton` and
        :class:`~MDFabBottomAppBarButton` classes.
        """

        if self.animation:
            Animation(
                y=self.height / 2 - dp(48) / 2,
                opacity=1,
                d=self.show_duration,
                t=self.show_transition,
            ).start(button)

    def check_scroll_direction(self, scroll_cls, y: float) -> None:
        """
        Checks the scrolling direction.
        Depending on the scrolling direction, hides or shows the
        :class:`~MDBottomAppBar` panel.
        """

        if round(y, 1) < self._scroll_cls_y and not self.bar_is_hidden:
            self.hide_bar()
        if round(y, 1) > self._scroll_cls_y and self.bar_is_hidden:
            self.show_bar()

        self._scroll_cls_y = round(y, 1)

    def show_bar(self) -> None:
        """Show :class:`~MDBottomAppBar` panel."""

        def on_complete(*args):
            self.dispatch("on_show_bar")

        def on_progress(animation, instance, progress):
            if progress > 0.5 and self._animated_show:
                self._animated_show = False
                for i, widget in enumerate(self.children):
                    if isinstance(widget, MDActionBottomAppBarButton):
                        anim_icon = Animation(
                            y=self.height / 2 - dp(48) / 2,
                            d=self.show_duration,
                            t=self.show_transition,
                        )
                        Clock.schedule_once(
                            lambda x, y=widget: anim_icon.start(y),
                            i / 10,
                        )
                if self._fab_bottom_app_bar_button:
                    Animation(
                        y=self._fab_bottom_app_bar_button.y + dp(4),
                        d=self.show_duration,
                        t=self.show_transition,
                    ).start(self._fab_bottom_app_bar_button)

        self.bar_is_hidden = False
        self._animated_show = True
        anim = Animation(
            y=0,
            d=self.show_duration,
            t=self.show_transition,
        )
        anim.bind(on_progress=on_progress, on_complete=on_complete)
        anim.start(self)

    def hide_bar(self) -> None:
        """Hide :class:`~MDBottomAppBar` panel."""

        def on_complete(*args):
            self.dispatch("on_hide_bar")

        def on_progress(animation, instance, progress):
            if (
                progress > 0.5
                and self._animated_hidden
                and widget_icon == instance.icon
            ):
                self._animated_hidden = False
                anim_bar = Animation(
                    y=-self.height,
                    d=self.hide_duration,
                    # t=self.hide_transition,
                )
                anim_bar.bind(on_complete=on_complete)
                anim_bar.start(self)

                if self._fab_bottom_app_bar_button:
                    Animation(
                        y=self._fab_bottom_app_bar_button.y - dp(4),
                        d=self.hide_duration,
                        t=self.hide_transition,
                    ).start(self._fab_bottom_app_bar_button)

        self.bar_is_hidden = True
        self._animated_hidden = True
        len_children = len(self.children)
        widget_icon = ""

        for i, widget in enumerate(self.children):
            if isinstance(widget, MDActionBottomAppBarButton):
                anim = Animation(
                    y=-widget.height,
                    d=self.hide_duration,
                    t=self.hide_transition,
                )
                if i + 2 == len_children:
                    widget_icon = widget.icon
                    anim.bind(on_progress=on_progress)
                Clock.schedule_once(
                    lambda x, y=widget: anim.start(y),
                    i / 10,
                )

    def on_show_bar(self, *args) -> None:
        """
        The method is called when the :class:`~MDBottomAppBar` panel
        is shown.
        """

    def on_hide_bar(self, *args) -> None:
        """
        The method is called when the :class:`~MDBottomAppBar` panel
        is hidden.
        """

    def on_scroll_cls(self, instance, scroll_cls) -> None:
        """
        Called when the value of the :attr:`scroll_cls` attribute changes.
        """

        def on_scroll_cls(*args):
            if not self.allow_hidden:
                Logger.warning(
                    "KivyMD: "
                    "In order for the bottom bar to be automatically hidden "
                    "in addition to the `scroll_cls` parameter, set the value "
                    "of the `allow_hidden` parameter to `True`"
                )

            if issubclass(scroll_cls.__class__, ScrollView):
                if self.allow_hidden:
                    scroll_cls.bind(scroll_y=self.check_scroll_direction)
            else:
                raise TypeError(
                    f"The `scroll_cls` parameter must be an object inherited from "
                    f"the {ScrollView} class"
                )

        if self.theme_cls.material_style == "M3":
            Clock.schedule_once(on_scroll_cls)

    def on_size(self, *args) -> None:
        """Called when the root screen is resized."""

        if (
            self._fab_bottom_app_bar_button
            and self.theme_cls.material_style == "M3"
        ):
            self._fab_bottom_app_bar_button.x = Window.width - (dp(56) + dp(16))

    def on_action_items(self, instance, value: list) -> None:
        """
        Called when the value of the :attr:`action_items` attribute changes.
        """

        if self.theme_cls.material_style == "M2":
            return

        def wait_removed(*args):
            if len(self.children) == 1 or not self.children:
                Clock.unschedule(wait_removed)
                self._wait_removed = False
                self._x = -dp(48)
                asynckivy.start(add_widget())

        async def add_widget():
            for button in value:
                await asynckivy.sleep(0)
                self.add_widget(button)

        if self._cache:
            self._cache.append(value)

            for data in self._cache:
                if value[0] in data:
                    for i, widget in enumerate(self.children):
                        if not self._wait_removed:
                            Clock.schedule_interval(wait_removed, 0)
                            self._wait_removed = True
                        if isinstance(widget, MDActionBottomAppBarButton):
                            anim = Animation(
                                y=-widget.height,
                                d=self.hide_duration,
                                t=self.hide_transition,
                            )
                            anim.bind(
                                on_complete=lambda x, y=widget: self.remove_widget(
                                    y
                                )
                            )
                            Clock.schedule_once(
                                lambda x, y=widget: anim.start(y),
                                i / 10,
                            )
        else:
            self._cache.append(value)
            self._current_data = value
            asynckivy.start(add_widget())

    def set_fab_opacity(self, *ars) -> None:
        """
        Sets the transparency value of the:class:`~MDFabBottomAppBarButton`
        button.
        """

        self._fab_bottom_app_bar_button.ids.lbl_ic.opacity = 1

    def set_fab_icon(self, instance, value) -> None:
        """
        Animates the size of the :class:`~MDFabBottomAppBarButton` button.
        """

        self._fab_bottom_app_bar_button.ids.lbl_ic.opacity = 0
        anim = Animation(
            scale_value_x=0,
            scale_value_y=0,
            opacity=0,
            d=self.hide_duration,
            t=self.hide_transition,
        ) + Animation(
            scale_value_x=1,
            scale_value_y=1,
            opacity=1,
            d=self.show_duration,
            t=self.show_transition,
        )
        anim.bind(on_complete=self.set_fab_opacity)
        anim.start(instance)

    def set_bg_color(self, *args) -> None:
        """
        Sets the background color for the :class:`~MDBottomAppBar` class.
        """

        if self.md_bg_color == [0, 0, 0, 0]:
            self.md_bg_color = self.theme_cls.primary_color

    def set_icon_color(
        self, widget: MDActionOverFlowButton | MDActionBottomAppBarButton
    ) -> None:
        """
        Sets the icon color for the :class:`~MDActionOverFlowButton` and
        :class:`~MDActionBottomAppBarButton` classes.
        """

        if self.icon_color:
            widget.theme_icon_color = "Custom"
            widget.icon_color = self.icon_color

    def add_widget(self, widget, index=0, canvas=None):
        # For M2 style.
        if (
            isinstance(widget, MDTopAppBar)
            and self.theme_cls.material_style == "M2"
        ):
            super().add_widget(widget)
            widget.elevation = 0
            return super().add_widget(widget.action_button)
        # For M3 style.
        if self.theme_cls.material_style == "M3":
            if isinstance(widget, MDActionBottomAppBarButton):
                self._x += widget.width
                widget.pos = (
                    self._x + self._padding,
                    -dp(48) if self.animation else self.height / 2 - dp(48) / 2,
                )
                widget.opacity = int(not self.animation)
                self.set_icon_color(widget)
                super().add_widget(widget)
                self.button_centering_animation(widget)
            elif isinstance(widget, MDFabBottomAppBarButton):
                widget.bind(icon=self.set_fab_icon)
                self._fab_bottom_app_bar_button = widget
                Clock.schedule_once(self.set_fab_opacity)
                widget.scale_value_x = int(not self.animation)
                widget.scale_value_y = int(not self.animation)
                widget.pos = (
                    Window.width - (dp(56) + self._padding),
                    self.height / 2 - dp(56) / 2,
                )
                super().add_widget(widget)
