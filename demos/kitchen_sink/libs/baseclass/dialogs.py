from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


class KitchenSinkCDialogs(Screen):
    app = ObjectProperty()
    input_dialog = None
    alert_dialog = None
    ok_cancel_dialog = None
    long_dialog = None

    def show_example_input_dialog(self):
        """Creates an instance of the dialog box and displays it
        on the screen for the screen Dialogs."""

        def result(text_button, instance):
            from kivymd.toast import toast

            toast(instance.text_field.text)

        if not self.input_dialog:
            from kivymd.uix.dialog import MDInputDialog

            self.input_dialog = MDInputDialog(
                title="Title",
                hint_text="Hint text",
                size_hint=(0.8, 0.4),
                text_button_ok="Ok",
                events_callback=result,
            )
        self.input_dialog.open()

    def show_example_alert_dialog(self):
        if not self.alert_dialog:
            from kivymd.uix.dialog import MDDialog

            self.alert_dialog = MDDialog(
                title="Title",
                size_hint=(0.8, 0.4),
                text_button_ok="Ok",
                text="This is Alert dialog",
                events_callback=self.app.callback_for_menu_items,
            )
        self.alert_dialog.open()

    def show_example_ok_cancel_dialog(self):
        if not self.ok_cancel_dialog:
            from kivymd.uix.dialog import MDDialog

            self.ok_cancel_dialog = MDDialog(
                title="Title",
                size_hint=(0.8, 0.4),
                text_button_ok="Ok",
                text="This is Ok Cancel dialog",
                text_button_cancel="Cancel",
                events_callback=self.app.callback_for_menu_items,
            )
        self.ok_cancel_dialog.open()

    def show_example_long_dialog(self):
        if not self.long_dialog:
            from kivymd.uix.dialog import MDDialog

            self.long_dialog = MDDialog(
                text="Lorem ipsum dolor sit amet, consectetur adipiscing "
                "elit, sed do eiusmod tempor incididunt ut labore et "
                "dolore magna aliqua. Ut enim ad minim veniam, quis "
                "nostrud exercitation ullamco laboris nisi ut aliquip "
                "ex ea commodo consequat. Duis aute irure dolor in "
                "reprehenderit in voluptate velit esse cillum dolore eu "
                "fugiat nulla pariatur. Excepteur sint occaecat "
                "cupidatat non proident, sunt in culpa qui officia "
                "deserunt mollit anim id est laborum.",
                title="Title",
                size_hint=(0.8, 0.4),
                text_button_ok="Yes",
                events_callback=self.app.callback_for_menu_items,
            )
        self.long_dialog.open()
