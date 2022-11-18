from kivy import lang
from kivy.clock import Clock
from kivy.tests.common import GraphicUnitTest

from kivymd.app import MDApp
from kivymd.theming import ThemeManager


class AppTest(GraphicUnitTest):
    def test_start_raw_app(self):
        lang._delayed_start = None
        a = MDApp()
        Clock.schedule_once(a.stop, 0.1)
        a.run()

    def test_theme_manager_existance(self):
        lang._delayed_start = None
        a = MDApp()
        Clock.schedule_once(a.stop, 0.1)
        a.run()
        assert isinstance(a.theme_cls, ThemeManager)
