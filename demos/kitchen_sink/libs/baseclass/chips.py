from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivymd.toast import toast


class KitchenSinkChips(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.binder, 0)

    def binder(self, time):
        self.ids.multiselect.bind(selected = self.toast_selected)

    def toast_selected(self,instance,value):
        toast(str(value))

    def callback_for_menu_items(self, instance):
        toast(instance.text)
