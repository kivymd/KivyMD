from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
Screen:

    MDCard:
        size_hint: None, None
        size: "280dp", "180dp"
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class TestCard(MDApp):
    def build(self):
        return Builder.load_string(KV)


TestCard().run()
