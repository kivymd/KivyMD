from kivy.uix.screenmanager import Screen


class KitchenSinkPickers(Screen):
    previous_date = None
    previous_time = None

    def get_time_picker_date(self, instance, time):
        self.ids.time_picker_label.text = str(time)
        self.previous_time = time

    def show_example_time_picker(self):
        from kivymd.uix.picker import MDTimePicker

        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time_picker_date)

        if self.ids.time_picker_use_previous_time.active:
            try:
                time_dialog.set_time(self.previous_time)
            except AttributeError:
                pass
        time_dialog.open()

    def set_previous_date(self, date_obj):
        self.previous_date = date_obj
        self.ids.date_picker_label.text = str(date_obj)

    def show_example_date_picker(self):
        from kivymd.uix.picker import MDDatePicker

        if self.ids.date_picker_use_previous_date.active:
            pd = self.previous_date
            try:
                MDDatePicker(
                    self.set_previous_date, pd.year, pd.month, pd.day
                ).open()
            except AttributeError:
                MDDatePicker(self.set_previous_date).open()
        else:
            MDDatePicker(self.set_previous_date).open()
