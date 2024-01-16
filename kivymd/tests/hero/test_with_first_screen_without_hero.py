# Test for https://github.com/kivymd/KivyMD/issues/1412 issue.

from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class ScreenWithoutHero(MDScreen):
    """
    This is the first screen from which we go to the screen that contains hero.
    """


class ScreenWithHeroFrom(MDScreen):
    """This is the screen that contains hero."""


class ScreenWithHeroTo(MDScreen):
    """This is the screen where the hero moves"""


KV = """
<ScreenWithoutHero>
    name: "Screen Without Hero"


<ScreenWithHeroFrom>
    name: "Screen With Hero From"

    MDHeroFrom:
        id: hero_from
        tag: "hero"
        size_hint: None, None
        size: "120dp", "120dp"
        pos_hint: {"top": .98}
        x: 24

        FitImage:
            source: "kivymd/images/logo/kivymd-icon-256.png"
            size_hint: None, None
            size: hero_from.size

<ScreenWithHeroTo>
    name: "Screen With Hero To"
    heroes_to: [hero_to]

    MDHeroTo:
        id: hero_to
        tag: "hero"
        size_hint: None, None
        size: "220dp", "220dp"
        pos_hint: {"center_x": .5, "center_y": .5}


MDScreenManager:

    ScreenWithoutHero:

    ScreenWithHeroFrom:

    ScreenWithHeroTo:
"""


class TestWithFirstScreenWithoutHero(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def move_hero_to_another_screen(self, *args):
        self.root.transition._direction = "in"
        self.root.current_heroes = ["hero"]
        self.root.current = "Screen With Hero To"
        Clock.schedule_once(self.move_hero_to_previous_screen, 1)

    def move_hero_to_previous_screen(self, *args):
        self.root.current_heroes = ["hero"]
        self.root.current = "Screen With Hero From"
        Clock.schedule_once(self.set_screen_without_hero, 1)

    def set_screen_without_hero(self, *args):
        self.root.current_heroes = []
        self.root.current = "Screen Without Hero"
        Clock.schedule_once(lambda x: self.stop(), 1)

    def set_screen_with_hero_from(self, *args):
        self.root.current = "Screen With Hero From"
        Clock.schedule_once(self.move_hero_to_another_screen, 1)

    def on_start(self):
        super().on_start()
        Clock.schedule_once(self.set_screen_with_hero_from, 1)


TestWithFirstScreenWithoutHero().run()
