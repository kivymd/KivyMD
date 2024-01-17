from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        layout = AnchorLayout()
        data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            check=True,
            column_data=[
                ("Column 1", dp(20)),
                ("Column 2", dp(30)),
                ("Column 3", dp(50), self.sort_on_col_3),
                ("Column 4", dp(30)),
                ("Column 5", dp(30)),
                ("Column 6", dp(30)),
                ("Column 7", dp(30), self.sort_on_col_2),
            ],
            row_data=[
                # The number of elements must match the length
                # of the `column_data` list.
                (
                    "1",
                    ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                    "Astrid: NE shared managed",
                    "Medium",
                    "Triaged",
                    "0:33",
                    "Chase Nguyen",
                ),
                (
                    "2",
                    ("alert-circle", [1, 0, 0, 1], "Offline"),
                    "Cosmo: prod shared ares",
                    "Huge",
                    "Triaged",
                    "0:39",
                    "Brie Furman",
                ),
                (
                    "3",
                    (
                        "checkbox-marked-circle",
                        [39 / 256, 174 / 256, 96 / 256, 1],
                        "Online",
                    ),
                    "Phoenix: prod shared lyra-lists",
                    "Minor",
                    "Not Triaged",
                    "3:12",
                    "Jeremy lake",
                ),
                (
                    "4",
                    (
                        "checkbox-marked-circle",
                        [39 / 256, 174 / 256, 96 / 256, 1],
                        "Online",
                    ),
                    "Sirius: NW prod shared locations",
                    "Negligible",
                    "Triaged",
                    "13:18",
                    "Angelica Howards",
                ),
                (
                    "5",
                    (
                        "checkbox-marked-circle",
                        [39 / 256, 174 / 256, 96 / 256, 1],
                        "Online",
                    ),
                    "Sirius: prod independent account",
                    "Negligible",
                    "Triaged",
                    "22:06",
                    "Diane Okuma",
                ),
            ],
        )
        layout.add_widget(data_tables)
        return layout

    def sort_on_col_3(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][3]))

    def sort_on_col_2(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))


Example().run()
