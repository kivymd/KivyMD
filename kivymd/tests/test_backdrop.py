from kivy.tests.common import GraphicUnitTest


class BackdropTest(GraphicUnitTest):
    def test_backdrop_raw_app(self):
        from kivymd.app import MDApp
        from kivymd.uix.backdrop import MDBackdrop
        from kivymd.uix.backdrop.backdrop import (
            MDBackdropBackLayer,
            MDBackdropFrontLayer,
        )
        from kivymd.uix.screen import MDScreen
        from kivymd.uix.widget import MDWidget

        render = self.render
        app = MDApp()  # NOQA
        self.screen = MDScreen(
            MDBackdrop(
                MDBackdropBackLayer(MDWidget()),
                MDBackdropFrontLayer(MDWidget()),
                id="backdrop",
                title="Example Backdrop",
                header_text="Menu:",
            )
        )
        render(self.screen)
