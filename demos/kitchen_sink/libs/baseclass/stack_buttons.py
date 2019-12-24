from kivy.uix.screenmanager import Screen


class KitchenSinkStackButtons(Screen):
    already_create_stack_floating_buttons = False

    def on_enter(self, *args):
        if not self.already_create_stack_floating_buttons:
            from kivymd.uix.stackfloatingbutton import MDStackFloatingButtons

            def set_my_language(instance_button):
                from kivymd.toast import toast

                toast(instance_button.icon)

            if not self.already_create_stack_floating_buttons:
                self.add_widget(
                    MDStackFloatingButtons(
                        icon="lead-pencil",
                        floating_data={
                            "Python": "language-python",
                            "Php": "language-php",
                            "C++": "language-cpp",
                        },
                        callback=set_my_language,
                    )
                )
                self.already_create_stack_floating_buttons = True
