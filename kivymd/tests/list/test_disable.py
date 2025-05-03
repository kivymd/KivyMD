from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.input.providers.mouse import MouseMotionEvent
from kivy.lang.builder import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDBoxLayout:
        orientation: 'vertical'

        MDListItem:
            id: item1

            MDListItemLeadingIcon:
                icon: "account"

            MDListItemHeadlineText:
                text: "Headline1"

            MDListItemSupportingText:
                text: "Supporting text"

            MDListItemTertiaryText:
                text: "Tertiary text"

            MDListItemTrailingCheckbox:

        MDListItem:
            id: item2

            MDListItemHeadlineText:
                text: "Headline2"

            MDListItemSupportingText:
                text: "Supporting text"

            MDListItemTertiaryText:
                text: "Tertiary text"

        MDListItem:
            id: item3

            MDListItemHeadlineText:
                text: "Headline3"

        MDListItem:
            id: item4

"""


class TestDisableList(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        def _enabled(*args):
            self.root.ids.item1.disabled = False
            self.root.ids.item2.disabled = False
            self.root.ids.item3.disabled = False
            self.root.ids.item4.disabled = False
            self.stop()

        def _disable(*args):
            self.root.ids.item1.disabled = True
            self.root.ids.item2.disabled = True
            self.root.ids.item3.disabled = True
            self.root.ids.item4.disabled = True
            Clock.schedule_once(_enabled, 1)

        Clock.schedule_once(_disable, 1)


TestDisableList().run()
