from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivymd.uix.screen import MDScreen


class KitchenSinkPickers(MDScreen):
    def get_time_picker_date(self, instance, time):
        self.ids.time_picker_label.text = str(time)

    def show_example_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time_picker_date)
        time_dialog.open()

    def set_previous_date(self, instance, value, date_rang):
        self.ids.date_picker_label.text = (
            f"{value.day}.{value.month}.{value.year}"
        )

    def show_example_date_picker(self):
        dialog = MDDatePicker()
        dialog.bind(on_save=self.set_previous_date)
        dialog.open()
