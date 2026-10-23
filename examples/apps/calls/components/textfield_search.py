from kivy.properties import ObjectProperty

from kivymd.uix.textfield import (
    IOSTextField,
    IOSTextFieldLeadingIcon,
    IOSTextFieldTrailingIcon,
)


class TextFieldSearch(IOSTextField):
    target_background = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.widgets = [
            IOSTextFieldLeadingIcon(
                icon="magnify",
                on_release=lambda x: print("Tap gmail"),
            ),
            IOSTextFieldTrailingIcon(
                icon="microphone",
                on_release=lambda x: print("Tap account"),
            ),
        ]
