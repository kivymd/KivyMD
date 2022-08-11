from kivymd.tests.base_test import BaseTest


class BackdropTest(BaseTest):
    def test_backdrop_raw_app(self):
        from kivymd.uix.backdrop import MDBackdrop
        from kivymd.uix.backdrop.backdrop import (
            MDBackdropBackLayer,
            MDBackdropFrontLayer,
        )
        from kivymd.uix.screen import MDScreen
        from kivymd.uix.widget import MDWidget

        self.render(
            MDScreen(
                MDBackdrop(
                    MDBackdropBackLayer(MDWidget()),
                    MDBackdropFrontLayer(MDWidget()),
                    id="backdrop",
                    title="Example Backdrop",
                    header_text="Menu:",
                )
            )
        )
