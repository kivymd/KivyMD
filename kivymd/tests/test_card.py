from kivymd.tests.base_test import BaseTest


class CardTest(BaseTest):
    def test_card_m3_style_raw_app(self):
        from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
        from kivymd.uix.card import MDCard
        from kivymd.uix.screen import MDScreen

        class MD3Card(MDCard, RoundedRectangularElevationBehavior):
            pass

        self.app.theme_cls.material_style = "M3"
        self.render(
            MDScreen(
                MD3Card(
                    size_hint=(None, None),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    size=("200dp", "100dp"),
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style="elevated",
                    md_bg_color="lightblue",
                )
            )
        )
