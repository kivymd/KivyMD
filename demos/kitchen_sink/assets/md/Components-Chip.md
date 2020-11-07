from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast


kv = """
MDChooseChip:
    pos_hint: {'center_x': .5, 'center_y': .5}

    MDChip:
        label: 'Earth'
        icon: 'earth'
        selected_chip_color: .21176470535294, .098039627451, 1, 1
        callback: app.callback_for_menu_items

    MDChip:
        label: 'Face'
        icon: 'face'
        selected_chip_color: .21176470535294, .098039627451, 1, 1
        callback: app.callback_for_menu_items

    MDChip:
        label: 'Facebook'
        icon: 'facebook'
        selected_chip_color: .21176470535294, .098039627451, 1, 1
        callback: app.callback_for_menu_items
"""


class MyApp(MDApp):

    def build(self):
        return Builder.load_string(kv)

    def callback_for_menu_items(self, instance, value):
        toast(value)

if __name__ == "__main__":
    MyApp().run()
