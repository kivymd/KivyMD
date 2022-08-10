from kivy.tests.common import GraphicUnitTest


class CardTest(GraphicUnitTest):
    def test_card_m3_style_raw_app(self):
        from kivymd.app import MDApp
        from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
        from kivymd.uix.card import MDCard
        from kivymd.uix.screen import MDScreen

        class MD3Card(MDCard, RoundedRectangularElevationBehavior):
            pass

        render = self.render
        app = MDApp()
        app.theme_cls.material_style = "M3"
        self.screen = MDScreen(
            MD3Card(
                size_hint=(None, None),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                size=("200dp", "100dp"),
                line_color=(0.2, 0.2, 0.2, 0.8),
                style="elevated",
                md_bg_color="lightblue",
            )
        )
        render(self.screen)
