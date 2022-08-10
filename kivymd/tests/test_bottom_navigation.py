from kivy.tests.common import GraphicUnitTest


class BottomNavigationTest(GraphicUnitTest):
    def test_bottom_navigation_m3_style_raw_app(self):
        from kivymd.app import MDApp
        from kivymd.uix.bottomnavigation import (
            MDBottomNavigation,
            MDBottomNavigationItem,
        )
        from kivymd.uix.screen import MDScreen

        render = self.render
        app = MDApp()
        app.theme_cls.material_style = "M3"
        self.screen = MDScreen(
            MDBottomNavigation(
                MDBottomNavigationItem(
                    name="screen 1",
                    text="Mail",
                    icon="gmail",
                ),
                MDBottomNavigationItem(
                    name="screen 2",
                    text="Twitter",
                    icon="twitter",
                    badge_icon="numeric-10",
                ),
                panel_color="#eeeaea",
                selected_color_background="#97ecf8",
                text_color_active="red",
            )
        )
        render(self.screen)
