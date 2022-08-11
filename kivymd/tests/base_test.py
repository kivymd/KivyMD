from kivy.tests.common import GraphicUnitTest

from kivymd.app import MDApp


class BaseTest(GraphicUnitTest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = MDApp()  # NOQA
