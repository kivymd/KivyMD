from kivymd.tests.base_test import BaseTest


class ImageListTest(BaseTest):
    def test_imagelist_raw_app(self):
        import os

        from kivymd import images_path
        from kivymd.uix.button import MDIconButton
        from kivymd.uix.imagelist import MDSmartTile
        from kivymd.uix.label import MDLabel
        from kivymd.uix.screen import MDScreen

        self.render(
            MDScreen(
                MDSmartTile(
                    MDIconButton(
                        icon="heart-outline",
                        theme_icon_color="Custom",
                        icon_color="red",
                        pos_hint={"center_y": 0.5},
                    ),
                    MDLabel(
                        text="Julia and Julie",
                        bold=True,
                        color="white",
                    ),
                    radius=24,
                    box_radius=[0, 0, 24, 24],
                    box_color="grey",
                    source=os.path.join(
                        images_path, "logo", "kivymd-icon-512.png"
                    ),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    size_hint=(None, None),
                    size=("320dp", "320dp"),
                )
            )
        )
