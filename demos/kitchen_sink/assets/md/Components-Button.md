from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
Screen:

    MDIconButton:
        icon: "language-python"
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()