from kivymd.tests.base_test import BaseTest


class ChipTest(BaseTest):
    def test_chip_raw_app(self):
        from kivymd.uix.chip import MDChip
        from kivymd.uix.screen import MDScreen

        self.render(
            MDScreen(
                MDChip(
                    text="Portland",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
            )
        )
