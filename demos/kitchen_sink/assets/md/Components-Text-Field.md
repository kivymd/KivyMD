from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: 'vertical'
    padding: dp(48)
    spacing: dp(15)

    MDTextField:
        hint_text: "Line"

    MDTextField:
        hint_text: "Fill"
        mode: "fill"
        fill_color: 0, 0, 0, .4

    MDTextField:
        hint_text: "Rectangle"
        mode: "rectangle"

    MDTextFieldRect:

'''


class Test(MDApp):

    def build(self):
        return  Builder.load_string(KV)


Test().run()