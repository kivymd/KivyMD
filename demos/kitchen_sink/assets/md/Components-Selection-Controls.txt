from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''

FloatLayout:

    MDCheckbox:
    	size_hint: (None, None)
        active: True
        pos_hint: {'center_x': .5, 'center_y': .4}

    MDSwitch:
        pos_hint: {'center_x': .5, 'center_y': .6}
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()