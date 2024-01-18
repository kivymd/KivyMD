from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
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
                source: "bg.jpg"
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
"""


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()
