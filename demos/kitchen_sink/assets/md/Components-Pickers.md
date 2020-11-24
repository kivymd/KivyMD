from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.picker import MDThemePicker, MDTimePicker, MDDatePicker


KV = """
BoxLayout:
    orientation: 'vertical'
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        title: 'Pickers'

    BoxLayout:
        spacing: dp(40)
        orientation: 'vertical'
        size_hint_x: None
        pos_hint: {'center_x': .5, 'center_y': .5}

        BoxLayout:
            orientation: 'vertical'

            MDRaisedButton:
                text: "Open time picker"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_example_time_picker()

            MDLabel:
                id: time_picker_label
                size_hint: None, None
                size: dp(48)*3, dp(48)
                pos_hint: {'center_x': .5, 'center_y': .5}

        BoxLayout:
            orientation: 'vertical'

            MDRaisedButton:
                text: "Open theme picker"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_example_theme_picker()

        BoxLayout:
            orientation: 'vertical'

            MDRaisedButton:
                text: "Open date picker"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_example_date_picker()

            MDLabel:
                id: date_picker_label
                size_hint: None, None
                size: dp(48)*3, dp(48)
                pos_hint: {'center_x': .5, 'center_y': .5}
"""


class Example(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def get_time(self, instance, time):
        self.root.ids.time_picker_label.text = str(time)

    def show_example_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_date(self, date_obj):
        self.root.ids.date_picker_label.text = str(date_obj)

    def show_example_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

    def show_example_theme_picker(self):
        MDThemePicker().open()


if __name__ == "__main__":
    Example().run()
