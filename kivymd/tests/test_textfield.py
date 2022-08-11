# from kivy.clock import Clock
# from kivy.uix.textinput import TextInput
from kivy.tests.common import GraphicUnitTest


class TextFieldTest(GraphicUnitTest):
    def test_textfield_raw_app(self):
        from kivymd.app import MDApp
        from kivymd.uix.boxlayout import MDBoxLayout
        from kivymd.uix.button import MDFlatButton
        from kivymd.uix.screen import MDScreen
        from kivymd.uix.textfield import MDTextField

        # def set_text():
        #     for widget in self.screen.ids.box.children:
        #         if issubclass(widget.__class__, TextInput):
        #             widget.text = "Input text"

        render = self.render
        app = MDApp()  # NOQA
        self.screen = MDScreen(
            MDBoxLayout(
                MDTextField(
                    hint_text="Label",
                    helper_text="Error massage",
                    mode="rectangle",
                    max_text_length=5,
                ),
                MDTextField(
                    icon_left="git",
                    hint_text="Label",
                    helper_text="Error massage",
                    mode="rectangle",
                ),
                MDTextField(
                    icon_left="git",
                    hint_text="Label",
                    helper_text="Error massage",
                    mode="fill",
                ),
                MDTextField(
                    hint_text="Label",
                    helper_text="Error massage",
                    mode="fill",
                ),
                MDTextField(
                    hint_text="Label",
                    helper_text="Error massage",
                ),
                MDTextField(
                    icon_left="git",
                    hint_text="Label",
                    helper_text="Error massage",
                ),
                MDTextField(
                    hint_text="Round mode",
                    mode="round",
                    max_text_length=15,
                    helper_text="Massage",
                ),
                MDFlatButton(
                    text="SET TEXT",
                    pos_hint={"center_x": 0.5},
                ),
                id="box",
                orientation="vertical",
                spacing="20dp",
                adaptive_height=True,
                size_hint_x=0.8,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        render(self.screen)
