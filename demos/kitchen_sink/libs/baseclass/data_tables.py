from kivy.metrics import dp
from kivy.uix.widget import Widget

from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen


class KitchenSinkDataTables(MDScreen):
    def open_table(self, use_checkbox_state, use_pagination_state):
        data_tables = MDDataTable(
            size_hint=(0.9, 0.7),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            use_pagination=use_pagination_state,
            check=use_checkbox_state,
            rows_num=10,
            column_data=[
                ("Desert (100g serving)", dp(70)),
                ("Calories", dp(30)),
                ("Fat (g)", dp(30)),
                ("Carbs (g)", dp(30)),
                ("Protein (g)", dp(30)),
                ("Sodium (mg)", dp(30)),
                ("Calcium (%)", dp(30)),
                ("Iron (%)", dp(30)),
            ],
            row_data=[
                ("Yogurt", "159", "6.0", "24", "4.0", "87", "14%", "1%"),
                ("Cream", "23", "8.0", "67", "9.0", "187", "24%", "1%"),
                ("Eclair", "159", "180", "6.1", "4.4", "90", "18%", "0.1%"),
                ("Cupcake", "204", "7.0", "32", "5.0", "100", "9%", "2%"),
                ("Gingerbread", "302", "12.1", "89", "8.2", "95", "24%", "2%"),
                ("Jelly bean", "436", "7.3", "76", "6.7", "365", "0.6%", "3%"),
                ("Lollipop", "235", "6.0", "21", "0.0", "99", "6%", "1%"),
                ("KitKat", "445", "9.8", "123", "7.0", "324", "13%", "12%"),
                ("Honeycomb", "332", "1.8", "23", "1.0", "655", "43%", "2%"),
                ("Donut", "215", "2.4", "43", "2.0", "24", "1%", "0.3%"),
                # -------------------------------------------------------------
                ("Yogurt", "159", "6.0", "24", "4.0", "87", "14%", "1%"),
                ("Cream", "23", "8.0", "67", "9.0", "187", "24%", "1%"),
                ("Eclair", "159", "180", "6.1", "4.4", "90", "18%", "0.1%"),
                ("Cupcake", "204", "7.0", "32", "5.0", "100", "9%", "2%"),
                ("Gingerbread", "302", "12.1", "89", "8.2", "95", "24%", "2%"),
                ("Jelly bean", "436", "7.3", "76", "6.7", "365", "0.6%", "3%"),
                ("Lollipop", "235", "6.0", "21", "0.0", "99", "6%", "1%"),
                ("KitKat", "445", "9.8", "123", "7.0", "324", "13%", "12%"),
                ("Honeycomb", "332", "1.8", "23", "1.0", "655", "43%", "2%"),
                ("Donut", "215", "2.4", "43", "2.0", "24", "1%", "0.3%"),
                # -------------------------------------------------------------
                ("Yogurt", "159", "6.0", "24", "4.0", "87", "14%", "1%"),
                ("Cream", "23", "8.0", "67", "9.0", "187", "24%", "1%"),
                ("Eclair", "159", "180", "6.1", "4.4", "90", "18%", "0.1%"),
                ("Cupcake", "204", "7.0", "32", "5.0", "100", "9%", "2%"),
                ("Gingerbread", "302", "12.1", "89", "8.2", "95", "24%", "2%"),
                ("Jelly bean", "436", "7.3", "76", "6.7", "365", "0.6%", "3%"),
                ("Lollipop", "235", "6.0", "21", "0.0", "99", "6%", "1%"),
                ("KitKat", "445", "9.8", "123", "7.0", "324", "13%", "12%"),
                ("Honeycomb", "332", "1.8", "23", "1.0", "655", "43%", "2%"),
                ("Donut", "215", "2.4", "43", "2.0", "24", "1%", "0.3%"),
            ],
        )
        data_tables.ids.container.add_widget(
            Widget(size_hint_y=None, height="5dp")
        )
        data_tables.ids.container.add_widget(
            MDRaisedButton(
                text="CLOSE",
                pos_hint={"right": 1},
                on_release=lambda x: self.remove_widget(data_tables),
            )
        )
        self.add_widget(data_tables)
