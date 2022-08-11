from kivymd.tests.base_test import BaseTest


class FitImageTest(BaseTest):
    def test_fitimage_raw_app(self):
        import os

        from kivymd import images_path
        from kivymd.uix.fitimage import FitImage
        from kivymd.uix.screen import MDScreen

        self.render(
            MDScreen(
                FitImage(
                    source=os.path.join(
                        images_path, "logo", "kivymd-icon-512.png"
                    ),
                    size_hint=(0.5, 0.5),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    radius=[36, 36, 0, 0],
                    mipmap=True,
                )
            )
        )
