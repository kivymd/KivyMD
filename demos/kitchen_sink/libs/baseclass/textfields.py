from kivy.uix.screenmanager import Screen


class KitchenSinkTextFields(Screen):
    def on_enter(self, *args):
        self.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )

    def set_error_message(self, instance_textfield):
        self.ids.text_field_error.error = True
