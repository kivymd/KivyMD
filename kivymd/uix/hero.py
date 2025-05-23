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
- On screen **B**, place the :class:`~MDHeroTo` container - our hero from screen **A** will fly into this container.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hero-base.png
    :align: center

.. warning::

    :class:`~MDHeroFrom` container cannot have more than one child widget.

Base example
------------

.. tabs::

    .. tab:: Declarative python style with KV

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
                            source: "kivymd/images/logo/kivymd-icon-512.png"
                            size_hint: None, None
                            size: hero_from.size

                    MDButton:
                        pos_hint: {"center_x": .5}
                        y: "36dp"
                        on_release:
                            root.current_heroes = ["hero"]
                            root.current = "screen B"

                        MDButtonText:
                            text: "Move Hero To Screen B"

                MDScreen:
                    name: "screen B"
                    hero_to: hero_to
                    md_bg_color: "cadetblue"

                    MDHeroTo:
                        id: hero_to
                        tag: "hero"
                        size_hint: None, None
                        size: "220dp", "220dp"
                        pos_hint: {"center_x": .5, "center_y": .5}

                    MDButton:
                        pos_hint: {"center_x": .5}
                        y: "36dp"
                        on_release:
                            root.current_heroes = ["hero"]
                            root.current = "screen A"

                        MDButtonText:
                            text: "Move Hero To Screen A"
            '''


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.clock import Clock

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.hero import MDHeroFrom, MDHeroTo
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.screenmanager import MDScreenManager


            class Example(MDApp):
                def go_to_screen(self, *args):
                    self.root.current_heroes = ["hero"]
                    if self.root.current == "screen A":
                        self.root.current = "screen B"
                    else:
                        self.root.current = "screen A"

                def on_start(self):
                    def on_start(*args):
                        self.root.get_ids().image.size = self.root.get_ids().hero_from.size
                        self.root.get_ids().screen_b.hero_to = self.root.get_ids().hero_to

                    self.root.get_ids().button_b.bind(on_release=self.go_to_screen)
                    self.root.get_ids().button_a.bind(on_release=self.go_to_screen)
                    Clock.schedule_once(on_start)

                def build(self):
                    return (
                        MDScreenManager(
                            MDScreen(
                                MDHeroFrom(
                                    FitImage(
                                        id="image",
                                        source="kivymd/images/logo/kivymd-icon-512.png",
                                        size_hint=(None, None),
                                    ),
                                    id="hero_from",
                                    tag="hero",
                                    size_hint=(None, None),
                                    size=("120dp", "120dp"),
                                    pos_hint={"top": .98},
                                    x=24,
                                ),
                                MDButton(
                                    MDButtonText(
                                        text="Move Hero To Screen B"
                                    ),
                                    id="button_b",
                                    pos_hint={"center_x": .5},
                                    y="36dp",
                                ),
                                name="screen A",
                                md_bg_color="lightblue",
                            ),
                            MDScreen(
                                MDHeroTo(
                                    id="hero_to",
                                    tag="hero",
                                    size_hint=(None, None),
                                    size=("220dp", "220dp"),
                                    pos_hint={"center_x": .5, "center_y": .5},
                                ),
                                MDButton(
                                    MDButtonText(
                                        text="Move Hero To Screen A"
                                    ),
                                    id="button_a",
                                    pos_hint={"center_x": .5},
                                    y="36dp",
                                ),
                                id="screen_b",
                                name="screen B",
                                md_bg_color="cadetblue",
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hero-usage.gif
    :align: center


Note that the child of the :class:`~MDHeroFrom` widget must have the size of the parent:

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDHeroFrom:
                id: hero_from
                tag: "hero"

                FitImage:
                    size_hint: None, None
                    size: hero_from.size

    .. tab:: Declarative python style

        .. code-block:: python

            class Example(MDApp):
                def on_start(self):
                    def on_start(*args):
                        self.root.get_ids().image.size = self.root.get_ids().hero_from.size

                    Clock.schedule_once(on_start)

                def build(self):
                    return (
                        [...]

                        MDHeroFrom(
                            FitImage(
                                id="image",
                                size_hint=(None, None),
                            ),
                            id="hero_from",
                        ),

                        [...]
                    )

To enable hero animation before setting the name of the current screen for the
screen manager, you must specify the name of the tag of the :class:`~MDHeroFrom`
container in which the hero is located:

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDButton:
                on_release:
                    root.current_heroes = ["hero"]
                    root.current = "screen 2"

                MDButtonText:
                    text: "Move Hero To Screen B"

    .. tab:: Declarative python style

        .. code-block:: python

            class Example(MDApp):
                def go_to_screen(self, *args):
                    self.root.current_heroes = ["hero"]
                    self.root.current = "screen 2"

                def on_start(self):
                    self.root.get_ids().button_b.bind(on_release=self.go_to_screen)

                def build(self):
                    return (
                        [...]

                        MDButton(
                            MDButtonText(
                                text="Move Hero To Screen B"
                            ),
                            id="button_b",
                        ),

                        [...]
                    )


If you need to switch to a screen that does not contain heroes, set the
`current_hero` attribute for the screen manager as "" (empty string):

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDButton:
                on_release:
                    root.current_heroes = []
                    root.current = "another screen"

                MDButtonText:
                    text: "Go To Another Screen"

    .. tab:: Declarative python style

        .. code-block:: python

            class Example(MDApp):
                def go_to_screen(self, *args):
                    self.root.current_heroes = []
                    self.root.current = "another screen"

                def on_start(self):
                    self.root.get_ids().button_b.bind(on_release=self.go_to_screen)

                def build(self):
                    return (
                        [...]

                        MDButton(
                            MDButtonText(
                                text="Go To Another Screen"
                            ),
                            id="button_b",
                        ),

                        [...]
                    )

Example
-------

.. tabs::

    .. tab:: Declarative python style with KV

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
                            source: "kivymd/images/logo/kivymd-icon-512.png"
                            size_hint: None, None
                            size: hero_from.size

                    MDButton:
                        pos_hint: {"center_x": .5}
                        y: "36dp"
                        on_release:
                            root.current_heroes = ["hero"]
                            root.current = "screen B"

                        MDButtonText:
                            text: "Move Hero To Screen B"

                MDScreen:
                    name: "screen B"
                    hero_to: hero_to
                    md_bg_color: "cadetblue"

                    MDHeroTo:
                        id: hero_to
                        tag: "hero"
                        size_hint: None, None
                        size: "220dp", "220dp"
                        pos_hint: {"center_x": .5, "center_y": .5}

                    MDButton:
                        pos_hint: {"center_x": .5}
                        y: "52dp"
                        on_release:
                            root.current_heroes = []
                            root.current = "screen C"

                        MDButtonText:
                            text: "Go To Screen C"

                    MDButton:
                        pos_hint: {"center_x": .5}
                        y: "8dp"
                        on_release:
                            root.current_heroes = ["hero"]
                            root.current = "screen A"

                        MDButtonText:
                            text: "Move Hero To Screen A"

                MDScreen:
                    name: "screen C"
                    md_bg_color: "olive"

                    MDLabel:
                        text: "Screen C"
                        halign: "center"

                    MDButton:
                        pos_hint: {"center_x": .5}
                        y: "36dp"
                        on_release:
                            root.current = "screen B"

                        MDButtonText:
                            text: "Back To Screen B"
            '''


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.clock import Clock

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.hero import MDHeroFrom, MDHeroTo
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.screenmanager import MDScreenManager


            class Example(MDApp):
                def on_start(self):
                    def on_start(*args):
                        self.root.get_ids().screen_b.hero_to = self.root.get_ids().hero_to

                    Clock.schedule_once(on_start)

                def build(self):
                    return MDScreenManager(
                        MDScreen(
                            MDHeroFrom(
                                FitImage(
                                    source="kivymd/images/logo/kivymd-icon-512.png",
                                    size_hint=(None, None),
                                ),
                                id="hero_from",
                                tag="hero",
                                size_hint=(None, None),
                                size=("120dp", "120dp"),
                                pos_hint={"top": 0.98},
                                x=24,
                            ),
                            MDButton(
                                MDButtonText(text="Move Hero To Screen B"),
                                pos_hint={"center_x": 0.5},
                                y="36dp",
                                on_release=lambda x: (
                                    setattr(self.root, "current_heroes", ["hero"]),
                                    setattr(self.root, "current", "screen B")
                                )
                            ),
                            name="screen A",
                            md_bg_color="lightblue",
                        ),
                        MDScreen(
                            MDHeroTo(
                                id="hero_to",
                                tag="hero",
                                size_hint=(None, None),
                                size=("220dp", "220dp"),
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                            ),
                            MDButton(
                                MDButtonText(text="Go To Screen C"),
                                pos_hint={"center_x": 0.5},
                                y="52dp",
                                on_release=lambda x: (
                                    setattr(self.root, "current_heroes", []),
                                    setattr(self.root, "current", "screen C")
                                )
                            ),
                            MDButton(
                                MDButtonText(text="Move Hero To Screen A"),
                                pos_hint={"center_x": 0.5},
                                y="8dp",
                                on_release=lambda x: (
                                    setattr(self.root, "current_heroes", ["hero"]),
                                    setattr(self.root, "current", "screen A")
                                )
                            ),
                            id="screen_b",
                            name="screen B",
                            md_bg_color="cadetblue",
                        ),
                        MDScreen(
                            MDLabel(
                                text="Screen C",
                                halign="center",
                            ),
                            MDButton(
                                MDButtonText(text="Back To Screen B"),
                                pos_hint={"center_x": 0.5},
                                y="36dp",
                                on_release=lambda x: setattr(self.root, "current", "screen B")
                            ),
                            name="screen C",
                            md_bg_color="olive",
                        )
                    )


            Example().run()

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

.. tabs::

    .. tab:: Declarative python style with KV

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
                                source: "kivymd/images/logo/kivymd-icon-512.png"

                    MDButton:
                        pos_hint: {"center_x": .5}
                        y: "36dp"
                        on_release:
                            root.current_heroes = ["hero"]
                            root.current = "screen B"

                        MDButtonText:
                            text: "Move Hero To Screen B"

                MDScreen:
                    name: "screen B"
                    hero_to: hero_to
                    md_bg_color: "cadetblue"

                    MDHeroTo:
                        id: hero_to
                        tag: "hero"
                        size_hint: None, None
                        size: "220dp", "220dp"
                        pos_hint: {"center_x": .5, "center_y": .5}

                    MDButton:
                        pos_hint: {"center_x": .5}
                        y: "36dp"
                        on_release:
                            root.current_heroes = ["hero"]
                            root.current = "screen A"

                        MDButtonText:
                            text: "Move Hero To Screen A"
            '''


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            class MyHero(MDHeroFrom):
                def on_transform_in(
                    self, instance_hero_widget: MDRelativeLayout, duration: float
                ):
                    '''
                    Fired when the hero flies from screen **A** to screen **B**.

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
                    '''Fired when the hero back from screen **B** to screen **A**.'''

                    Animation(
                        radius=[24, 12, 24, 12],
                        duration=duration,
                        md_bg_color=get_color_from_hex(utils.hex_colormap["blue"]),
                    ).start(instance_hero_widget)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.clock import Clock
            from kivy.animation import Animation
            from kivy.utils import get_color_from_hex
            from kivy import utils

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.hero import MDHeroFrom, MDHeroTo
            from kivymd.uix.relativelayout import MDRelativeLayout
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.screenmanager import MDScreenManager


            class MyHero(MDHeroFrom):
                def on_transform_in(
                        self, instance_hero_widget: MDRelativeLayout, duration: float
                ):
                    '''
                    Fired when the hero flies from screen **A** to screen **B**.

                    :param instance_hero_widget: dhild widget of the `MDHeroFrom` class.
                    :param duration of the transition animation between screens.
                    '''

                    Animation(
                        radius=[12, 24, 12, 24],
                        duration=0.1,
                        md_bg_color=(0, 1, 1, 1),
                    ).start(instance_hero_widget)

                def on_transform_out(
                        self, instance_hero_widget: MDRelativeLayout, duration: float
                ):
                    '''Fired when the hero back from screen **B** to screen **A**.'''

                    Animation(
                        radius=[24, 12, 24, 12],
                        duration=0.1,
                        md_bg_color=get_color_from_hex(utils.hex_colormap["blue"]),
                    ).start(instance_hero_widget)


            class Example(MDApp):
                def go_to_screen(self, *args):
                    self.root.current_heroes = ["hero"]
                    if self.root.current == "screen A":
                        self.root.current = "screen B"
                    else:
                        self.root.current = "screen A"

                def on_start(self):
                    def on_start(*args):
                        self.root.get_ids().relative.size = self.root.get_ids().hero_from.size
                        self.root.get_ids().screen_b.hero_to = self.root.get_ids().hero_to

                    self.root.get_ids().button_b.bind(on_release=self.go_to_screen)
                    self.root.get_ids().button_a.bind(on_release=self.go_to_screen)
                    Clock.schedule_once(on_start)

                def build(self):
                    return (
                        MDScreenManager(
                            MDScreen(
                                MyHero(
                                    MDRelativeLayout(
                                        FitImage(
                                            source="kivymd/images/logo/kivymd-icon-512.png",
                                        ),
                                        id="relative",
                                        size_hint=(None, None),
                                        md_bg_color="blue",
                                        radius=[24, 12, 24, 12],
                                    ),
                                    id="hero_from",
                                    tag="hero",
                                    size_hint=(None, None),
                                    size=("120dp", "120dp"),
                                    pos_hint={"top": .98},
                                    x=24,
                                ),
                                MDButton(
                                    MDButtonText(
                                        text="Move Hero To Screen B"
                                    ),
                                    id="button_b",
                                    pos_hint={"center_x": .5},
                                    y="36dp",
                                ),
                                name="screen A",
                                md_bg_color="lightblue",
                            ),
                            MDScreen(
                                MDHeroTo(
                                    id="hero_to",
                                    tag="hero",
                                    size_hint=(None, None),
                                    size=("220dp", "220dp"),
                                    pos_hint={"center_x": .5, "center_y": .5},
                                ),
                                MDButton(
                                    MDButtonText(
                                        text="Move Hero To Screen A"
                                    ),
                                    id="button_a",
                                    pos_hint={"center_x": .5},
                                    y="36dp",
                                ),
                                id="screen_b",
                                name="screen B",
                                md_bg_color="cadetblue",
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hero-events.gif
    :align: center

Usage with ScrollView
---------------------

.. tabs::

    .. tab:: Declarative python style with KV

        .. code-block:: python

            from kivy.animation import Animation
            from kivy.clock import Clock
            from kivy.lang import Builder
            from kivy.metrics import dp
            from kivy.properties import StringProperty, ObjectProperty

            from kivymd.app import MDApp
            from kivymd.uix.hero import MDHeroFrom

            KV = '''
            <HeroItem>
                size_hint_y: None
                height: "200dp"
                radius: "24dp"

                MDSmartTile:
                    id: tile
                    size_hint: None, None
                    size: root.size
                    on_release: root.on_release()

                    MDSmartTileImage:
                        id: image
                        source: "kivymd/images/logo/kivymd-icon-512.png"
                        radius: dp(24)

                    MDSmartTileOverlayContainer:
                        id: overlay
                        md_bg_color: 0, 0, 0, .5
                        adaptive_height: True
                        padding: "8dp"
                        spacing: "8dp"
                        radius: [0, 0, dp(24), dp(24)]

                        MDLabel:
                            text: root.tag
                            theme_text_color: "Custom"
                            text_color: "white"
                            adaptive_height: True


            MDScreenManager:
                md_bg_color: self.theme_cls.backgroundColor

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
                    heroes_to: [hero_to]

                    MDHeroTo:
                        id: hero_to
                        size_hint: 1, None
                        height: "220dp"
                        pos_hint: {"top": 1}

                    MDButton:
                        pos_hint: {"center_x": .5}
                        y: "36dp"
                        on_release:
                            root.current_heroes = [hero_to.tag]
                            root.current = "screen A"

                        MDButtonText:
                            text: "Move Hero To Screen A"
            '''


            class HeroItem(MDHeroFrom):
                text = StringProperty()
                manager = ObjectProperty()

                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.ids.image.ripple_duration_in_fast = 0.05

                def on_transform_in(self, instance_hero_widget, duration):
                    for instance in [
                        instance_hero_widget,
                        instance_hero_widget._overlay_container,
                        instance_hero_widget._image,
                    ]:
                        Animation(radius=[0, 0, 0, 0], duration=duration).start(instance)

                def on_transform_out(self, instance_hero_widget, duration):
                    for instance, radius in {
                        instance_hero_widget: [dp(24), dp(24), dp(24), dp(24)],
                        instance_hero_widget._overlay_container: [0, 0, dp(24), dp(24)],
                        instance_hero_widget._image: [dp(24), dp(24), dp(24), dp(24)],
                    }.items():
                        Animation(
                            radius=radius,
                            duration=duration,
                        ).start(instance)

                def on_release(self):
                    def switch_screen(*args):
                        self.manager.current_heroes = [self.tag]
                        self.manager.ids.hero_to.tag = self.tag
                        self.manager.current = "screen B"

                    Clock.schedule_once(switch_screen, 0.2)


            class Example(MDApp):
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


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.animation import Animation
            from kivy.clock import Clock
            from kivy.metrics import dp
            from kivy.properties import StringProperty, ObjectProperty

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.gridlayout import MDGridLayout
            from kivymd.uix.hero import MDHeroFrom, MDHeroTo
            from kivymd.uix.imagelist import (
                MDSmartTile, MDSmartTileImage, MDSmartTileOverlayContainer
            )
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.screenmanager import MDScreenManager
            from kivymd.uix.scrollview import MDScrollView


            class HeroItem(MDHeroFrom):
                text = StringProperty()
                manager = ObjectProperty()

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.size_hint_y = None
                    self.height = "200dp"
                    self.radius = "24dp"
                    Clock.schedule_once(self.build_widgets, 0.4)

                def build_widgets(self, *args):
                    self.add_widget(
                        MDSmartTile(
                            MDSmartTileImage(
                                id="image",
                                source="kivymd/images/logo/kivymd-icon-512.png",
                                radius=dp(24),
                            ),
                            MDSmartTileOverlayContainer(
                                MDLabel(
                                    text=self.tag,
                                    theme_text_color="Custom",
                                    text_color="white",
                                    adaptive_height=True,
                                ),
                                id="overlay",
                                md_bg_color=(0, 0, 0, .5),
                                adaptive_height=True,
                                padding="8dp",
                                spacing="8dp",
                                radius=[0, 0, dp(24), dp(24)],
                            ),
                            id="tile",
                            size_hint=(None, None),
                            size=self.size,
                            on_release=lambda x: self.on_release(),
                        )
                    )
                    self.get_ids().image.ripple_duration_in_fast = 0.05

                def on_transform_in(self, instance_hero_widget, duration):
                    for instance in [
                        instance_hero_widget,
                        instance_hero_widget._overlay_container,
                        instance_hero_widget._image,
                    ]:
                        Animation(radius=[0, 0, 0, 0], duration=duration).start(instance)

                def on_transform_out(self, instance_hero_widget, duration):
                    for instance, radius in {
                        instance_hero_widget: [dp(24), dp(24), dp(24), dp(24)],
                        instance_hero_widget._overlay_container: [0, 0, dp(24), dp(24)],
                        instance_hero_widget._image: [dp(24), dp(24), dp(24), dp(24)],
                    }.items():
                        Animation(radius=radius, duration=duration).start(instance)

                def on_release(self):
                    def switch_screen(*args):
                        self.manager.current_heroes = [self.tag]
                        self.manager.get_ids().hero_to.tag = self.tag
                        self.manager.current = "screen B"

                    Clock.schedule_once(switch_screen, 0.2)


            class Example(MDApp):
                def build(self):
                    return (
                        MDScreenManager(
                            MDScreen(
                                MDScrollView(
                                    MDGridLayout(
                                        id="box",
                                        cols=2,
                                        spacing="12dp",
                                        padding="12dp",
                                        adaptive_height=True,
                                    )
                                ),
                                name="screen A"
                            ),
                            MDScreen(
                                MDHeroTo(
                                    id="hero_to",
                                    size_hint=(1, None),
                                    height="220dp",
                                    pos_hint={"top": 1},
                                ),
                                MDButton(
                                    MDButtonText(
                                        text="Move Hero To Screen A"
                                    ),
                                    id="button_move_to_screen_a",
                                    pos_hint={"center_x": .5},
                                    y="36dp",
                                ),
                                id="screen_b",
                                name="screen B",
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )

                def go_to_screen(self, *args):
                    self.root.current_heroes = [self.root.get_ids().hero_to.tag]
                    self.root.current = "screen A"

                def on_start(self):
                    self.root.get_ids().screen_b.heroes_to = [self.root.get_ids().hero_to]
                    self.root.get_ids().button_move_to_screen_a.bind(
                        on_release=self.go_to_screen
                    )
                    for i in range(12):
                        hero_item = HeroItem(
                            text=f"Item {i + 1}", tag=f"Tag {i}", manager=self.root
                        )
                        if not i % 2:
                            hero_item.md_bg_color = "lightgrey"
                        self.root.get_ids().box.add_widget(hero_item)


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hero-usage-with-scrollview.gif
    :align: center

Using multiple heroes at the same time
--------------------------------------

.. tabs::

    .. tab:: Declarative python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreenManager:

                MDScreen:
                    name: "screen A"
                    md_bg_color: "lightblue"

                    MDHeroFrom:
                        id: hero_kivymd
                        tag: "kivymd"
                        size_hint: None, None
                        size: "200dp", "200dp"
                        pos_hint: {"top": .98}
                        x: "24dp"

                        FitImage:
                            source: "kivymd/images/logo/kivymd-icon-512.png"
                            size_hint: None, None
                            size: hero_kivymd.size
                            radius: self.height / 2

                    MDHeroFrom:
                        id: hero_kivy
                        tag: "kivy"
                        size_hint: None, None
                        size: "200dp", "200dp"
                        pos_hint: {"top": .98}
                        x: "324dp"

                        FitImage:
                            source: "data/logo/kivy-icon-512.png"
                            size_hint: None, None
                            size: hero_kivy.size
                            radius: self.height / 2

                    MDButton:
                        pos_hint: {"center_x": .5}
                        y: "36dp"
                        on_release:
                            root.current_heroes = ["kivymd", "kivy"]
                            root.current = "screen B"

                        MDButtonText:
                            text: "Move Hero To Screen B"

                MDScreen:
                    name: "screen B"
                    heroes_to: hero_to_kivymd, hero_to_kivy
                    md_bg_color: "cadetblue"

                    MDHeroTo:
                        id: hero_to_kivy
                        tag: "kivy"
                        size_hint: None, None
                        pos_hint: {"center_x": .5, "center_y": .5}

                    MDHeroTo:
                        id: hero_to_kivymd
                        tag: "kivymd"
                        size_hint: None, None
                        pos_hint: {"right": 1, "top": 1}

                    MDButton:
                        pos_hint: {"center_x": .5}
                        y: "36dp"
                        on_release:
                            root.current_heroes = ["kivy", "kivymd"]
                            root.current = "screen A"

                        MDButtonText:
                            text: "Move Hero To Screen A"
            '''


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.clock import Clock

            from kivymd.app import MDApp
            from kivymd.material_resources import dp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.hero import MDHeroFrom, MDHeroTo
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.screenmanager import MDScreenManager


            class Example(MDApp):
                def go_to_screen(self, *args):
                    if self.root.current == "screen A":
                        self.root.current_heroes = ["kivymd", "kivy"]
                        self.root.current = "screen B"
                    else:
                        self.root.current_heroes = ["kivy", "kivymd"]
                        self.root.current = "screen A"

                def on_start(self):
                    def on_start(*args):
                        logo_kivymd = self.root.get_ids().logo_kivymd
                        logo_kivy = self.root.get_ids().logo_kivy

                        logo_kivymd.size = self.root.get_ids().hero_kivymd.size
                        logo_kivymd.radius = logo_kivymd.height / 2

                        logo_kivy.size = self.root.get_ids().hero_kivy.size
                        logo_kivy.radius = logo_kivy.height / 2

                    self.root.get_ids().button_move_heto_to_screen_b.bind(
                        on_release=self.go_to_screen
                    )
                    self.root.get_ids().button_move_heto_to_screen_a.bind(
                        on_release=self.go_to_screen
                    )

                    self.root.get_ids().screen_b.heroes_to = [
                        self.root.get_ids().hero_to_kivymd, self.root.get_ids().hero_to_kivy
                    ]
                    Clock.schedule_once(on_start)

                def build(self):
                    return (
                        MDScreenManager(
                            MDScreen(
                                MDHeroFrom(
                                    FitImage(
                                        id="logo_kivymd",
                                        source="kivymd/images/logo/kivymd-icon-512.png",
                                        size_hint=(None, None),
                                    ),
                                    id="hero_kivymd",
                                    tag="kivymd",
                                    size_hint=(None, None),
                                    size=("200dp", "200dp"),
                                    pos_hint={"top": .98},
                                    x=dp(24),
                                ),
                                MDHeroFrom(
                                    FitImage(
                                        id="logo_kivy",
                                        source="data/logo/kivy-icon-512.png",
                                        size_hint=(None, None),
                                    ),
                                    id="hero_kivy",
                                    tag="kivy",
                                    size_hint=(None, None),
                                    size=("200dp", "200dp"),
                                    pos_hint={"top": .98},
                                    x="324dp",
                                ),
                                MDButton(
                                    MDButtonText(
                                        text="Move Hero To Screen B"
                                    ),
                                    id="button_move_heto_to_screen_b",
                                    pos_hint={"center_x": .5},
                                    y="36dp",
                                ),
                                name="screen A",
                                md_bg_color="lightblue",
                            ),
                            MDScreen(
                                MDHeroTo(
                                    id="hero_to_kivy",
                                    tag="kivy",
                                    size_hint=(None, None),
                                    pos_hint={"center_x": .5, "center_y": .5},
                                ),
                                MDHeroTo(
                                    id="hero_to_kivymd",
                                    tag="kivymd",
                                    size_hint=(None, None),
                                    pos_hint={"right": 1, "top": 1},
                                ),
                                MDButton(
                                    MDButtonText(
                                        text="Move Hero To Screen A"
                                    ),
                                    id="button_move_heto_to_screen_a",
                                    pos_hint={"center_x": .5},
                                    y="36dp",
                                ),
                                id="screen_b",
                                name="screen B",
                                md_bg_color="cadetblue",
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hero-multiple-heroes.gif
    :align: center
"""

from kivy.properties import StringProperty

from kivymd.uix.boxlayout import MDBoxLayout


class MDHeroFrom(MDBoxLayout):
    """
    The container from which the hero begins his flight.

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` class documentation.

    :Events:
        `on_transform_in`
            when the hero flies from screen **A** to screen **B**.
        `on_transform_out`
            Fired when the hero back from screen **B** to screen **A**.
    """

    tag = StringProperty(allownone=True)
    """
    Tag ID for heroes.

    :attr:`tag` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    __events__ = ("on_transform_in", "on_transform_out")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_transform_in(self, *args):
        """Fired when the hero flies from screen **A** to screen **B**."""

    def on_transform_out(self, *args):
        """Fired when the hero back from screen **B** to screen **A**."""


class MDHeroTo(MDBoxLayout):
    """
    The container in which the hero comes.

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` class documentation.
    """

    tag = StringProperty(allownone=True)
    """
    Tag ID for heroes.

    :attr:`tag` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """
