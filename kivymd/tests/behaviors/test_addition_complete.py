import pytest
from kivy.clock import Clock
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivymd.uix.behaviors.addition_complete_behaviour import AdditionComplete
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen


class Something(AdditionComplete, Widget):
    def on_fully_added(self, parent_widget):
        assert "MDBoxLayout" == self.parent.__class__.__name__
        assert [] != self.parent.children
        MDApp.get_running_app().stop()

    def on_parent(self, *args):
        assert [] == self.parent.children


class AdditionComplete(MDApp):
    def build(self):
        s = MDScreen(layout := MDBoxLayout())
        layout.add_widget(Something())
        return s


def test_addition_complete():
    AdditionComplete().run()
