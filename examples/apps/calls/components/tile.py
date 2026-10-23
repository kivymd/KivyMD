from kivy.properties import StringProperty

from kivymd.uix.list import (
    MDListItem,
    MDListItemHeadlineText,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
    MDListItemTrailingIcon,
    MDListItemTrailingSupportingText,
)


class CallsTile(MDListItem):
    icon = StringProperty("account")
    trailing_icon = StringProperty("info")
    title = StringProperty("")
    text = StringProperty("")
    color = StringProperty("white")

    def __init__(self, **kwargs):
        self.divider = True
        super().__init__(**kwargs)

        self.theme_bg_color = "Custom"
        self.md_bg_color = [0, 0, 0, 0]

        self.widgets = [
            MDListItemLeadingIcon(
                icon=self.icon,
                theme_icon_color="Custom",
                icon_color=[1, 1, 1, 0.9],
            ),
            MDListItemHeadlineText(
                text=self.title,
                theme_text_color="Custom",
                text_color=self.color,
            ),
            MDListItemSupportingText(
                text=self.text,
                theme_text_color="Custom",
                text_color=[1, 1, 1, 1],
            ),
            MDListItemTrailingIcon(
                icon=self.trailing_icon,
                theme_icon_color="Custom",
                icon_color="#42AAFF",
            ),
            MDListItemTrailingSupportingText(
                text="text",
                theme_text_color="Custom",
                text_color=[1, 1, 1, 1],
            ),
        ]

    def on_trailing_icon(self, *args):
        self.widgets[3].icon = self.trailing_icon

    def on_icon(self, *args):
        self.widgets[0].icon = self.icon

    def on_title(self, *args):
        self.widgets[1].text = self.title

    def on_color(self, *args):
        self.widgets[1].text_color = self.color

    def on_text(self, *args):
        self.widgets[2].text = self.text
