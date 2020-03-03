from kivy.uix.screenmanager import Screen


class KitchenSinkStackButtons(Screen):
    already_create_buttons = False

    def on_enter(self, *args):
        if not self.already_create_buttons:
            from kivymd.uix.button import MDFloatingActionButtonSpeedDial

            def callback(instance_button):
                from kivymd.toast import toast

                toast(instance_button.icon)

            button_speed_dial = MDFloatingActionButtonSpeedDial()
            button_speed_dial.rotation_root_button = True
            button_speed_dial.data = {
                "language-python": "Python",
                "language-php": "PHP",
                "language-cpp": "C++",
            }
            button_speed_dial.callback = callback
            self.add_widget(button_speed_dial)
            self.already_create_buttons = True
