"""
Components/Hero
===============

.. versionadded:: 1.0.0

.. rubric:: Use the :class:`~MDHeroFrom` widget to animate a widget from one
    screen to the next.

- The hero refers to the widget that flies between screens.
- Create a hero animation using KivyMD’s :class:`~MDHeroFrom` widget.
- Fly the hero from one screen to another.
- Animate the transformation of a hero’s shape from circular to rectangular while flying it from one screen to another.
- The :class:`~MDHeroFrom` widget in KivyMD implements a style of animation commonly known as shared element transitions or shared element animations.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe
            src="https://www.youtube.com/embed/qfQ4mmMR2Kg"
            frameborder="0"
            allowfullscreen
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

The widget that will move from screen A to screen B will be a hero. To move
a widget from one screen to another using hero animation, you need to do the
following:

- On screen **A**, place the :class:`~MDHeroFrom` container.
- Sets a tag (string) for the :class:`~MDHeroFrom` container.
- Place a hero in the :class:`~MDHeroFrom` container.
- On screen **B**, place the :class:`~MDHeroTo` container - our hero from screen **A **will fly into this container.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hero-base.png
    :align: center

.. warning::
    :class:`~MDHeroFrom` container cannot have more than one child widget.

Base example
------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreenManager:

        MDScreen:
            name: "screen A"
            md_bg_color: "lightblue"

            MDHeroFrom:
                id: hero_from
                tag: "hero"
                size_hint: None, None
                size: "120dp", "120dp"
                pos_hint: {"top": .98}
                x: 24

                FitImage:
                    source: "https://github.com/kivymd/internal/raw/main/logo/kivymd_logo_blue.png"
                    size_hint: None, None
                    size: hero_from.size

            MDRaisedButton:
                text: "Move Hero To Screen B"
                pos_hint: {"center_x": .5}
                y: "36dp"
                on_release:
                    root.current_hero = "hero"
                    root.current = "screen B"

        MDScreen:
            name: "screen B"
            hero_to: hero_to
            md_bg_color: "cadetblue"

            MDHeroTo:
                id: hero_to
                size_hint: None, None
                size: "220dp", "220dp"
                pos_hint: {"center_x": .5, "center_y": .5}

            MDRaisedButton:
                text: "Move Hero To Screen A"
                pos_hint: {"center_x": .5}
                y: "36dp"
                on_release:
                    root.current_hero = "hero"
                    root.current = "screen A"
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hero-usage.gif
    :align: center


Note that the child of the :class:`~MDHeroFrom` widget must have the size of the parent:

.. code-block:: kv

    MDHeroFrom:
        id: hero_from

        FitImage:
            size_hint: None, None
            size: hero_from.size

To enable hero animation before setting the name of the current screen for the
screen manager, you must specify the name of the tag of the :class:`~MDHeroFrom`
container in which the hero is located:

.. code-block:: kv

    MDRaisedButton:
        text: "Move Hero To Screen B"
        on_release:
            root.current_hero = "hero"
            root.current = "screen 2"

If you need to switch to a screen that does not contain heroes, set the
`current_hero` attribute for the screen manager as "" (empty string):

.. code-block:: kv

    MDRaisedButton:
        text: "Go To Another Screen"
        on_release:
            root.current_hero = ""
            root.current = "another screen"

Example
-------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreenManager:

        MDScreen:
            name: "screen A"
            md_bg_color: "lightblue"

            MDHeroFrom:
                id: hero_from
                tag: "hero"
                size_hint: None, None
                size: "120dp", "120dp"
                pos_hint: {"top": .98}
                x: 24

                FitImage:
                    source: "https://github.com/kivymd/internal/raw/main/logo/kivymd_logo_blue.png"
                    size_hint: None, None
                    size: hero_from.size

            MDRaisedButton:
                text: "Move Hero To Screen B"
                pos_hint: {"center_x": .5}
                y: "36dp"
                on_release:
                    root.current_hero = "hero"
                    root.current = "screen B"

        MDScreen:
            name: "screen B"
            hero_to: hero_to
            md_bg_color: "cadetblue"

            MDHeroTo:
                id: hero_to
                size_hint: None, None
                size: "220dp", "220dp"
                pos_hint: {"center_x": .5, "center_y": .5}

            MDRaisedButton:
                text: "Go To Screen C"
                pos_hint: {"center_x": .5}
                y: "52dp"
                on_release:
                    root.current_hero = ""
                    root.current = "screen C"

            MDRaisedButton:
                text: "Move Hero To Screen A"
                pos_hint: {"center_x": .5}
                y: "8dp"
                on_release:
                    root.current_hero = "hero"
                    root.current = "screen A"

        MDScreen:
            name: "screen C"

            MDLabel:
                text: "Screen C"
                halign: "center"

            MDRaisedButton:
                text: "Back To Screen B"
                pos_hint: {"center_x": .5}
                y: "36dp"
                on_release:
                    root.current = "screen B"
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hero-switch-another-screen.gif
    :align: center

Events
------

Two events are available for the hero:

- `on_transform_in` - when the hero flies from screen **A** to screen **B**.
- `on_transform_out` - when the hero back from screen **B** to screen **A**.

The `on_transform_in`, `on_transform_out` events relate to the
:class:`~MDHeroFrom` container. For example, let's change the radius and
background color of the hero during the flight between the screens:

.. code-block:: python

    from kivy import utils
    from kivy.animation import Animation
    from kivy.lang import Builder
    from kivy.utils import get_color_from_hex

    from kivymd.app import MDApp
    from kivymd.uix.hero import MDHeroFrom
    from kivymd.uix.relativelayout import MDRelativeLayout

    KV = '''
    MDScreenManager:

        MDScreen:
            name: "screen A"
            md_bg_color: "lightblue"

            MyHero:
                id: hero_from
                tag: "hero"
                size_hint: None, None
                size: "120dp", "120dp"
                pos_hint: {"top": .98}
                x: 24

                MDRelativeLayout:
                    size_hint: None, None
                    size: hero_from.size
                    md_bg_color: "blue"
                    radius: [24, 12, 24, 12]

                    FitImage:
                        source: "https://github.com/kivymd/internal/raw/main/logo/kivymd_logo_blue.png"

            MDRaisedButton:
                text: "Move Hero To Screen B"
                pos_hint: {"center_x": .5}
                y: "36dp"
                on_release:
                    root.current_hero = "hero"
                    root.current = "screen B"

        MDScreen:
            name: "screen B"
            hero_to: hero_to
            md_bg_color: "cadetblue"

            MDHeroTo:
                id: hero_to
                size_hint: None, None
                size: "220dp", "220dp"
                pos_hint: {"center_x": .5, "center_y": .5}

            MDRaisedButton:
                text: "Move Hero To Screen A"
                pos_hint: {"center_x": .5}
                y: "36dp"
                on_release:
                    root.current_hero = "hero"
                    root.current = "screen A"
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    class MyHero(MDHeroFrom):
        def on_transform_in(
            self, instance_hero_widget: MDRelativeLayout, duration: float
        ):
            '''
            Called when the hero flies from screen **A** to screen **B**.

            :param instance_hero_widget: dhild widget of the `MDHeroFrom` class.
            :param duration of the transition animation between screens.
            '''

            Animation(
                radius=[12, 24, 12, 24],
                duration=duration,
                md_bg_color=(0, 1, 1, 1),
            ).start(instance_hero_widget)

        def on_transform_out(
            self, instance_hero_widget: MDRelativeLayout, duration: float
        ):
            '''Called when the hero back from screen **B** to screen **A**.'''

            Animation(
                radius=[24, 12, 24, 12],
                duration=duration,
                md_bg_color=get_color_from_hex(utils.hex_colormap["blue"]),
            ).start(instance_hero_widget)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hero-events.gif
    :align: center

Usage with ScrollView
---------------------

.. code-block:: python

    from kivy.animation import Animation
    from kivy.clock import Clock
    from kivy.lang import Builder
    from kivy.properties import StringProperty, ObjectProperty

    from kivymd.app import MDApp
    from kivymd.uix.hero import MDHeroFrom

    KV = '''
    <HeroItem>
        size_hint_y: None
        height: "200dp"
        radius: 24

        MDSmartTile:
            id: tile
            radius: 24
            box_radius: 0, 0, 24, 24
            box_color: 0, 0, 0, .5
            source: "image.jpg"
            size_hint: None, None
            size: root.size
            mipmap: True
            on_release: root.on_release()

            MDLabel:
                text: root.tag
                bold: True
                font_style: "H6"
                opposite_colors: True


    MDScreenManager:

        MDScreen:
            name: "screen A"

            ScrollView:

                MDGridLayout:
                    id: box
                    cols: 2
                    spacing: "12dp"
                    padding: "12dp"
                    adaptive_height: True

        MDScreen:
            name: "screen B"
            hero_to: hero_to

            MDHeroTo:
                id: hero_to
                size_hint: 1, None
                height: "220dp"
                pos_hint: {"top": 1}

            MDRaisedButton:
                text: "Move Hero To Screen A"
                pos_hint: {"center_x": .5}
                y: "36dp"
                on_release:
                    root.current_hero = "hero"
                    root.current = "screen A"
    '''


    class HeroItem(MDHeroFrom):
        text = StringProperty()
        manager = ObjectProperty()

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.ids.tile.ids.image.ripple_duration_in_fast = 0.05

        def on_transform_in(self, instance_hero_widget, duration):
            Animation(
                radius=[0, 0, 0, 0],
                box_radius=[0, 0, 0, 0],
                duration=duration,
            ).start(instance_hero_widget)

        def on_transform_out(self, instance_hero_widget, duration):
            Animation(
                radius=[24, 24, 24, 24],
                box_radius=[0, 0, 24, 24],
                duration=duration,
            ).start(instance_hero_widget)

        def on_release(self):
            def switch_screen(*args):
                self.manager.current_hero = self.tag
                self.manager.current = "screen B"

            Clock.schedule_once(switch_screen, 0.2)


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for i in range(12):
                hero_item = HeroItem(
                    text=f"Item {i + 1}", tag=f"Tag {i}", manager=self.root
                )
                if not i % 2:
                    hero_item.md_bg_color = "lightgrey"
                self.root.ids.box.add_widget(hero_item)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hero-usage-with-scrollview.gif
    :align: center
"""

from kivy.properties import StringProperty

from kivymd.uix.boxlayout import MDBoxLayout


class MDHeroFrom(MDBoxLayout):
    """
    The container from which the hero begins his flight.

    :Events:
        `on_transform_in`
            when the hero flies from screen **A** to screen **B**.
        `on_transform_out`
            Called when the hero back from screen **B** to screen **A**.
    """

    tag = StringProperty(allownone=True)
    """
    Tag ID for heroes.

    :attr:`shift_right` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_transform_in")
        self.register_event_type("on_transform_out")

    def on_transform_in(self, *args):
        """Called when the hero flies from screen **A** to screen **B**."""

    def on_transform_out(self, *args):
        """Called when the hero back from screen **B** to screen **A**."""


class MDHeroTo(MDBoxLayout):
    """The container in which the hero comes."""
