"""
Components/Toolbar
==================

.. seealso::

    `Material Design spec, App bars: top <https://material.io/components/app-bars-top>`_
    `Material Design spec, App bars: bottom <https://material.io/components/app-bars-bottom/app-bars-bottom.html>`_
    `Material Design 3 spec, App bars: bottom <https://m3.material.io/components/top-app-bar/overview>`_

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/app-bar-top.png
    :align: center

`KivyMD` provides the following toolbar positions for use:

- Top_
- Bottom_

.. Top:
Top
---

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "MDToolbar"

        MDLabel:
            text: "Content"
            halign: "center"
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-1.png
    :align: center

Add left menu
-------------

.. code-block:: kv

    MDToolbar:
        title: "MDToolbar"
        left_action_items: [["menu", lambda x: app.callback()]]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-2.png
    :align: center

.. note::

    The callback is optional. ``left_action_items: [["menu"]]`` would also work for a button that does nothing.

Add right menu
--------------

.. code-block:: kv

    MDToolbar:
        title: "MDToolbar"
        right_action_items: [["dots-vertical", lambda x: app.callback()]]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-3.png
    :align: center

Add two item to the right menu
------------------------------

.. code-block:: kv

    MDToolbar:
        title: "MDToolbar"
        right_action_items: [["dots-vertical", lambda x: app.callback_1()], ["clock", lambda x: app.callback_2()]]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-4.png
    :align: center

Change toolbar color
--------------------

.. code-block:: kv

    MDToolbar:
        title: "MDToolbar"
        md_bg_color: app.theme_cls.accent_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-5.png
    :align: center

Change toolbar text color
-------------------------

.. code-block:: kv

    MDToolbar:
        title: "MDToolbar"
        specific_text_color: app.theme_cls.accent_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-6.png
    :align: center

Shadow elevation control
------------------------

.. code-block:: kv

    MDToolbar:
        title: "Elevation 10"
        elevation: 10

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-7.png
    :align: center

.. Bottom:
Bottom
------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/app-bar-bottom.png
    :align: center

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDBoxLayout:

        # Will always be at the bottom of the screen.
        MDBottomAppBar:

            MDToolbar:
                title: "Title"
                icon: "git"
                type: "bottom"
                left_action_items: [["menu", lambda x: x]]
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-8.png
    :align: center

Event on floating button
------------------------

Event ``on_action_button``:

.. code-block:: kv

    MDBottomAppBar:

        MDToolbar:
            title: "Title"
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

        MDToolbar:
            title: "Title"
            icon: "git"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]
            mode: "end"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-9.png
    :align: center

.. code-block:: kv

    MDBottomAppBar:

        MDToolbar:
            title: "Title"
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
        md_bg_color: 0, 1, 0, 1

        MDToolbar:
            title: "Title"
            icon: "git"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]
            icon_color: 0, 1, 0, 1

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-11.png
    :align: center

Tooltips
--------

You can add MDTooltips to the Toolbar icons by ading a text string to the toolbar item, as shown below

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.snackbar import Snackbar

    KV = '''
    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "MDToolbar"
            left_action_items: [["menu", "This is the navigation"]]
            right_action_items:
                [["dots-vertical", lambda x: app.callback(x), "this is the More Actions"]]

        MDLabel:
            text: "Content"
            halign: "center"
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def callback(self, button):
            Snackbar(text="Hello World").open()

    Test().run()

Material design 3 style
-----------------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.utils import get_color_from_hex

    from kivymd.app import MDApp
    from kivymd.uix.toolbar import MDToolbar

    KV = '''
    MDScreen:

        MDBoxLayout:
            id: box
            orientation: "vertical"
            spacing: "12dp"
            pos_hint: {"top": 1}
            adaptive_height: True
    '''


    class TestNavigationDrawer(MDApp):
        def build(self):
            self.theme_cls.material_style = "M3"
            return Builder.load_string(KV)

        def on_start(self):
            for type_height in ["medium", "large", "small"]:
                self.root.ids.box.add_widget(
                    MDToolbar(
                        type_height=type_height,
                        headline_text=f"Headline {type_height.lower()}",
                        md_bg_color=get_color_from_hex("#2d2734"),
                        left_action_items=[["arrow-left", lambda x: x]],
                        right_action_items=[
                            ["attachment", lambda x: x],
                            ["calendar", lambda x: x],
                            ["dots-vertical", lambda x: x],
                        ],
                        title="Title" if type_height == "small" else ""
                    )
                )


    TestNavigationDrawer().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-m3.png
    :align: center
"""

__all__ = ("MDToolbar", "MDBottomAppBar", "MDActionTopAppBarButton")

import os
from math import cos, radians, sin
from typing import NoReturn, Union

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
    OptionProperty,
    StringProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivymd import uix_path
from kivymd.color_definitions import text_colors
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    FakeRectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.button import MDFloatingActionButton, MDIconButton
from kivymd.uix.tooltip import MDTooltip
from kivymd.utils.set_bars_colors import set_bars_colors

with open(
    os.path.join(uix_path, "toolbar", "toolbar.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDActionBottomAppBarButton(MDFloatingActionButton):
    _scale_x = NumericProperty(1)
    _scale_y = NumericProperty(1)


class MDActionTopAppBarButton(MDIconButton, MDTooltip):
    pass


class NotchedBox(
    ThemableBehavior,
    FakeRectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
    BoxLayout,
):
    elevation = NumericProperty(6)
    """
    Elevation value.

    :attr:`elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `6`.
    """

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


class MDToolbar(NotchedBox):
    """
    :Events:
        `on_action_button`
            Method for the button used for the :class:`~MDBottomAppBar` class.
    """

    left_action_items = ListProperty()
    """
    The icons on the left of the toolbar.
    To add one, append a list like the following:

    .. code-block:: kv

        left_action_items: [`'icon_name'`, callback, tooltip text]

    where `'icon_name'` is a string that corresponds to an icon definition,
    ``callback`` is the function called on a touch release event and
    ``tooltip text` is the text to be displayed in the tooltip. Both the
    ``callback`` and ``tooltip text`` are optional but the order must be
    preserved.

    :attr:`left_action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    right_action_items = ListProperty()
    """
    The icons on the left of the toolbar.
    Works the same way as :attr:`left_action_items`.

    :attr:`right_action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    title = StringProperty()
    """
    Text toolbar.

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    headline_text = StringProperty()
    """
    Headline text toolbar.

    .. versionadded:: 1.0.0

    :attr:`headline_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    headline_text_color = ColorProperty(None)
    """
    Headline text color.

    .. versionadded:: 1.0.0

    :attr:`headline_text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    anchor_title = OptionProperty(None, options=["left", "center", "right"])
    """
    Position toolbar title.
    Available options are: `'left'`, `'center'`, `'right'`.

    :attr:`anchor_title` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'left'`.
    """

    mode = OptionProperty(
        "center", options=["free-end", "free-center", "end", "center"]
    )
    """
    Floating button position. Only for :class:`~MDBottomAppBar` class.
    Available options are: `'free-end'`, `'free-center'`, `'end'`, `'center'`.

    :attr:`mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'center'`.
    """

    round = NumericProperty("10dp")
    """
    Rounding the corners at the notch for a button.
    Only for :class:`~MDBottomAppBar` class.

    :attr:`round` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'10dp'`.
    """

    icon = StringProperty("android")
    """
    Floating button. Only for :class:`~MDBottomAppBar` class.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    icon_color = ColorProperty()
    """
    Color action button. Only for :class:`~MDBottomAppBar` class.

    :attr:`icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[]`.
    """

    type = OptionProperty("top", options=["top", "bottom"])
    """
    When using the :class:`~MDBottomAppBar` class, the parameter ``type``
    must be set to `'bottom'`:

    .. code-block:: kv

        MDBottomAppBar:

            MDToolbar:
                type: "bottom"

    Available options are: `'top'`, `'bottom'`.

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'top'`.
    """

    type_height = OptionProperty("small", options=["medium", "large", "small"])
    """
    Toolbar height type.

    .. versionadded:: 1.0.0

    Available options are: 'small', 'large', 'small'.

    :attr:`type_height` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'small'`.
    """

    opposite_colors = BooleanProperty(False)
    """
    Changes the color of the label to the color opposite to the main theme.

    .. code-block:: kv

        MDToolbar:
            title: "MDToolbar"
            opposite_colors: True

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-opposite-true.png
        :align: center

    .. code-block:: kv

        MDToolbar:
            title: "MDToolbar"
            opposite_colors: True

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-opposite-false.png
        :align: center
    """

    md_bg_bottom_color = ColorProperty(None)
    """
    The background color for the toolbar with the ``bottom`` mode.

    .. versionadded:: 1.0.0

    :attr:`md_bg_bottom_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _shift = NumericProperty("3dp")

    def __init__(self, **kwargs):
        self.action_button = MDActionBottomAppBarButton()
        super().__init__(**kwargs)
        self.register_event_type("on_action_button")
        if not self.icon_color:
            self.icon_color = self.theme_cls.primary_color
        Window.bind(on_resize=self._on_resize)
        self.bind(specific_text_color=self.update_action_bar_text_colors)
        self.theme_cls.bind(material_style=self.update_bar_height)
        # self.bind(opposite_colors=self.update_opposite_colors)
        self.theme_cls.bind(primary_palette=self.update_md_bg_color)
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

    def set_headline_font_style(self, interval: Union[int, float]) -> NoReturn:
        if self.type_height in ("medium", "large"):
            self.ids.label_headline.font_style = {
                "medium": "H6",
                "large": "H5",
            }[self.type_height]

    def on_type(self, instance_toolbar, type_value: str) -> NoReturn:
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
            self.on_mode(None, self.mode)

    def on_type_height(
        self, instance_toolbar, height_type_value: str
    ) -> NoReturn:
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
        pass

    def on_md_bg_color(self, instance_toolbar, color_value: list) -> NoReturn:
        if self.type == "bottom":
            self.md_bg_color = [0, 0, 0, 0]
        else:
            set_bars_colors(color_value, None, self.theme_cls.theme_style)

    def on_left_action_items(
        self, instance_toolbar, items_value: list
    ) -> NoReturn:
        def on_left_action_items(interval: Union[int, float]):
            self.update_action_bar(self.ids.left_actions, items_value)

        Clock.schedule_once(on_left_action_items)

    def on_right_action_items(
        self, instance_toolbar, items_value: list
    ) -> NoReturn:
        def on_right_actions(interval: Union[int, float]):
            self.update_action_bar(self.ids.right_actions, items_value)

        Clock.schedule_once(on_right_actions)

    def on_icon(self, instance_toolbar, icon_name: str) -> NoReturn:
        self.action_button.icon = icon_name

    def on_icon_color(self, instance, icon_name: str) -> NoReturn:
        self.action_button.md_bg_color = icon_name

    def on_md_bg_bottom_color(
        self, instance_toolbar, color_value: list
    ) -> NoReturn:
        set_bars_colors(None, color_value, self.theme_cls.theme_style)

    def on_anchor_title(self, instance_toolbar, anchor_value: str) -> NoReturn:
        def on_anchor_title(interval: Union[int, float]):
            self.ids.label_title.halign = anchor_value

        Clock.schedule_once(on_anchor_title)

    def on_mode(self, instance_toolbar, mode_value: str) -> NoReturn:
        if self.type == "top":
            return

        def on_mode(interval: Union[int, float]):
            def set_button_pos(*args):
                self.action_button.x = x
                self.action_button.y = y - self._rounded_rectangle_height / 2
                self.action_button._hard_shadow_size = (0, 0)
                self.action_button._soft_shadow_size = (0, 0)
                anim = Animation(_scale_x=1, _scale_y=1, d=0.05)
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
            anim = Animation(_scale_x=0, _scale_y=0, d=0.1)
            anim.bind(on_complete=set_button_pos)
            anim.start(self.action_button)

        Clock.schedule_once(on_mode)

    def set_md_bg_color(self, instance_toolbar, color_value: list) -> NoReturn:
        if color_value == [1.0, 1.0, 1.0, 0.0]:
            self.md_bg_color = self.theme_cls.primary_color

    def set_notch(self) -> NoReturn:
        anim = Animation(d=0.1) + Animation(
            notch_radius=self.action_button.width / 2 + dp(8),
            d=0.1,
        )
        anim.start(self)

    def set_shadow(self, *args) -> NoReturn:
        self.action_button._elevation = self.action_button.elevation

    def update_bar_height(
        self, instance_theme_manager, material_style_value: str
    ) -> NoReturn:
        self.on_type_height(self, self.type_height)
        self.update_anchor_title(material_style_value)

    def update_floating_radius(self, interval: Union[int, float]) -> NoReturn:
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
    ) -> NoReturn:
        instance_box_layout.clear_widgets()
        new_width = 0
        for item in action_bar_items:
            new_width += dp(48)
            if len(item) == 1:
                item.append(lambda x: None)
            if len(item) > 1 and not item[1]:
                item[1] = lambda x: None
            if len(item) == 2:
                if type(item[1]) is str:
                    item.insert(1, lambda x: None)
                else:
                    item.append("")
            instance_box_layout.add_widget(
                MDActionTopAppBarButton(
                    icon=item[0],
                    on_release=item[1],
                    tooltip_text=item[2],
                    theme_text_color="Custom"
                    if not self.opposite_colors
                    else "Primary",
                    text_color=self.specific_text_color,
                    opposite_colors=self.opposite_colors,
                )
            )
        instance_box_layout.width = new_width

    def update_md_bg_color(self, *args) -> NoReturn:
        self.md_bg_color = self.theme_cls._get_primary_color()

    def update_opposite_colors(
        self, instance_toolbar, opposite_value: bool
    ) -> NoReturn:
        if opposite_value:
            self.ids.label_title.theme_text_color = ""

    def update_action_bar_text_colors(self, *args) -> NoReturn:
        for child in self.ids["left_actions"].children:
            child.text_color = self.specific_text_color
        for child in self.ids["right_actions"].children:
            child.text_color = self.specific_text_color

    def remove_notch(self) -> NoReturn:
        anim = Animation(d=0.1) + Animation(notch_radius=0, d=0.1)
        anim.start(self)

    def remove_shadow(self) -> NoReturn:
        self.action_button._elevation = 0

    def _on_resize(self, instance, width, height):
        if self.mode == "center":
            self.action_button.x = width / 2 - self.action_button.width / 2
        else:
            self.action_button.x = width - self.action_button.width * 2

    def _update_specific_text_color(self, instance, value):
        if self.specific_text_color in (
            [0.0, 0.0, 0.0, 0.87],
            [0.0, 0.0, 0.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
        ):
            self.specific_text_color = text_colors[
                self.theme_cls.primary_palette
            ][self.theme_cls.primary_hue]


class MDBottomAppBar(FloatLayout):
    md_bg_color = ColorProperty([0, 0, 0, 0])
    """
    Color toolbar.

    :attr:`md_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, MDToolbar):
            super().add_widget(widget)
            return super().add_widget(widget.action_button)
