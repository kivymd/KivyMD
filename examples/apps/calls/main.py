from examples.apps.calls.screen import CallsScreen
from kivymd.app import MDApp


class App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = CallsScreen()

        return screen


if __name__ == "__main__":
    App().run()
