from kivy.uix.screenmanager import Screen

from kivymd.toast import toast


class KitchenSinkChips(Screen):
    def callback_for_menu_items(self, instance):
        toast(instance.text)
