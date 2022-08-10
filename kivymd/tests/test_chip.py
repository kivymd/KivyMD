from kivy.tests.common import GraphicUnitTest


class ChipTest(GraphicUnitTest):
    def test_chip_raw_app(self):
        from kivymd.app import MDApp
        from kivymd.uix.chip import MDChip
        from kivymd.uix.screen import MDScreen

        render = self.render
        app = MDApp()  # NOQA
        self.screen = MDScreen(
            MDChip(
                text="Portland",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        render(self.screen)
