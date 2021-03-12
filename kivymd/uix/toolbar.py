"""
Components/Toolbar
==================

.. seealso::

    `Material Design spec, App bars: top <https://material.io/components/app-bars-top>`_

    `Material Design spec, App bars: bottom <https://material.io/components/app-bars-bottom/app-bars-bottom.html>`_

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

MDToolbar with Menus
--------------------

A Toolbar without Menus is not particularly useful. However, the
:class:`~MDDropdownMenu` works well with the standard
:class:`~kivymd.uix.toolbar.MDToolbar` to provide this functionality,
as shown in the image below.

.. seealso::

    See the
    `MDDropdownMenu documentation
    <https://kivymd.readthedocs.io/en/latest/components/menu/#menu-with-mdtoolbar>`_
    for details of how to implement this.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-menu.gif
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
            right_action_items: [["dots-vertical", lambda x: app.callback(x), "this is the More Actions"]]

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

.. seealso::

    `Components-Bottom-App-Bar <https://github.com/kivymd/KivyMD/wiki/Components-Bottom-App-Bar>`_
"""

from math import cos, radians, sin

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

from kivymd.color_definitions import text_colors
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    FakeRectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.button import MDFloatingActionButton, MDIconButton
from kivymd.uix.tooltip import MDTooltip

Builder.load_string(
    """
#:import m_res kivymd.material_resources


<MDActionBottomAppBarButton>
    md_bg_color: self.theme_cls.primary_color

    canvas.before:
        PushMatrix
        Scale:
            origin: self.center
            x: root._scale_x
            y: root._scale_y
    canvas.after:
        PopMatrix


<NotchedBox>
    size_hint_y: None
    height: root.theme_cls.standard_increment
    padding: [root.theme_cls.horizontal_margins - dp(12), 0]
    # opposite_colors: False
    elevation: root.elevation

    canvas:
        Color:
            rgba:
                ( \
                root.theme_cls.primary_color \
                if root.md_bg_color == [0, 0, 0, 0] \
                else root.md_bg_color \
                ) \
                if root.type == "top" else \
                ( \
                root.theme_cls.primary_color \
                if root.parent.md_bg_color == [0, 0, 0, 0] \
                else root.parent.md_bg_color \
                )
        Mesh:
            vertices: root._vertices_left
            indices: root._indices_left
            mode: "triangle_fan"
        Mesh:
            vertices: root._vertices_right
            indices: root._indices_right
            mode: "triangle_fan"
        RoundedRectangle:
            pos: root._rectangle_left_pos
            size: root._rectangle_left_width, root._rounded_rectangle_height
            radius:
                [0,] if root.mode == "normal" \
                else [0, root.notch_radius * root._rounding_percentage, 0, 0]
        RoundedRectangle:
            pos: root._rectangle_right_pos
            size: root._rectangle_right_width, root._rounded_rectangle_height
            radius:
                [0,] if root.mode == "normal" \
                else [root.notch_radius * root._rounding_percentage, 0, 0, 0]


<MDToolbar>

    BoxLayout:
        id: left_actions
        orientation: "horizontal"
        size_hint_x: None
        padding: [0, (self.height - dp(48)) / 2]

    BoxLayout:
        padding: dp(12), 0

        MDLabel:
            id: label_title
            font_style: "H6"
            opposite_colors: root.opposite_colors
            theme_text_color: "Custom" if not root.opposite_colors else "Primary"
            text_color: root.specific_text_color
            text: root.title
            shorten: True
            shorten_from: "right"
            halign: root.anchor_title
            markup: True

    BoxLayout:
        id: right_actions
        orientation: "horizontal"
        size_hint_x: None
        padding: [0, (self.height - dp(48)) / 2]
"""
)


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

    anchor_title = OptionProperty("left", options=["left", "center", "right"])
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
    Onle for :class:`~MDBottomAppBar` class.

    :attr:`round` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'10dp'`.
    """

    icon = StringProperty("android")
    """
    Floating button. Onle for :class:`~MDBottomAppBar` class.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    icon_color = ColorProperty()
    """
    Color action button. Onle for :class:`~MDBottomAppBar` class.

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

    opposite_colors = BooleanProperty(False)

    _shift = NumericProperty("3.5dp")

    def __init__(self, **kwargs):
        self.action_button = MDActionBottomAppBarButton()
        super().__init__(**kwargs)
        self.register_event_type("on_action_button")
        if not self.icon_color:
            self.icon_color = self.theme_cls.primary_color
        Window.bind(on_resize=self._on_resize)
        self.bind(specific_text_color=self.update_action_bar_text_colors)
        # self.bind(opposite_colors=self.update_opposite_colors)
        self.theme_cls.bind(primary_palette=self.update_md_bg_color)
        Clock.schedule_once(
            lambda x: self.on_left_action_items(0, self.left_action_items)
        )
        Clock.schedule_once(
            lambda x: self.on_right_action_items(0, self.right_action_items)
        )
        Clock.schedule_once(lambda x: self.set_md_bg_color(0, self.md_bg_color))

    def on_type(self, instance, value):
        if value == "bottom":
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

    def on_action_button(self, *args):
        pass

    def on_md_bg_color(self, instance, value):
        if self.type == "bottom":
            self.md_bg_color = [0, 0, 0, 0]

    def on_left_action_items(self, instance, value):
        self.update_action_bar(self.ids["left_actions"], value)

    def on_right_action_items(self, instance, value):
        self.update_action_bar(self.ids["right_actions"], value)

    def set_md_bg_color(self, instance, value):
        if value == [1.0, 1.0, 1.0, 0.0]:
            self.md_bg_color = self.theme_cls.primary_color

    def update_action_bar(self, action_bar, action_bar_items):
        action_bar.clear_widgets()
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
            action_bar.add_widget(
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
        action_bar.width = new_width

    def update_md_bg_color(self, *args):
        self.md_bg_color = self.theme_cls._get_primary_color()

    def update_opposite_colors(self, instance, value):
        if value:
            self.ids.label_title.theme_text_color = ""

    def update_action_bar_text_colors(self, *args):
        for child in self.ids["left_actions"].children:
            child.text_color = self.specific_text_color
        for child in self.ids["right_actions"].children:
            child.text_color = self.specific_text_color

    def on_icon(self, instance, value):
        self.action_button.icon = value

    def on_icon_color(self, instance, value):
        self.action_button.md_bg_color = value

    def on_mode(self, instance, value):
        if self.type == "top":
            return

        def set_button_pos(*args):
            self.action_button.x = x
            self.action_button.y = y - self._rounded_rectangle_height / 2
            self.action_button._hard_shadow_size = (0, 0)
            self.action_button._soft_shadow_size = (0, 0)
            anim = Animation(_scale_x=1, _scale_y=1, d=0.05)
            anim.bind(on_complete=self.set_shadow)
            anim.start(self.action_button)

        if value == "center":
            self.set_notch()
            x = Window.width / 2 - self.action_button.width / 2
            y = (
                (self.center[1] - self.height / 2)
                + self.theme_cls.standard_increment / 2
                + self._shift
            )
        elif value == "end":

            self.set_notch()
            x = Window.width - self.action_button.width * 2
            y = (
                (self.center[1] - self.height / 2)
                + self.theme_cls.standard_increment / 2
                + self._shift
            )
            self.right_action_items = []
        elif value == "free-end":
            self.remove_notch()
            x = Window.width - self.action_button.width - dp(10)
            y = self.action_button.height + self.action_button.height / 2
        elif value == "free-center":
            self.remove_notch()
            x = Window.width / 2 - self.action_button.width / 2
            y = self.action_button.height + self.action_button.height / 2
        self.remove_shadow()
        anim = Animation(_scale_x=0, _scale_y=0, d=0.1)
        anim.bind(on_complete=set_button_pos)
        anim.start(self.action_button)

    def remove_notch(self):
        anim = Animation(d=0.1) + Animation(
            notch_radius=0,
            d=0.1,
        )
        anim.start(self)

    def set_notch(self):
        anim = Animation(d=0.1) + Animation(
            notch_radius=self.action_button.width / 2 + dp(8),
            d=0.1,
        )
        anim.start(self)

    def remove_shadow(self):
        self.action_button._elevation = 0

    def set_shadow(self, *args):
        self.action_button._elevation = self.action_button.elevation

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
