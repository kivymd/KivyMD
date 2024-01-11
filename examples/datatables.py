from kivy.clock import Clock
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen


class Example(MDApp):
    def build(self):
        print("BUILD")
        self.theme_cls.theme_style = "Dark"

        return MDScreen(
            MDDataTable(
                size_hint=(0.9, 0.6),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                use_pagination=True,
                check=True,
                column_data=[
                    ("No.", dp(30)),
                    ("Column 1", dp(30)),
                    ("Column 2", dp(30)),
                    ("Column 3", dp(30)),
                    ("Column 4", dp(30)),
                    ("Column 5", dp(30)),
                ],
                row_data=[
                    (f"{i + 1}", "1", "2", "3", "4", "5") for i in range(50)
                ],
            ),
            md_bg_color=self.theme_cls.backgroundColor,
        )

    def on_start(self):
        def on_start(*args):
            self.root.md_bg_color = self.theme_cls.backgroundColor

        Clock.schedule_once(on_start)


Example().run()
