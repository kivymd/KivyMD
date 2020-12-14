from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import (
    MDExpansionPanel,
    MDExpansionPanelThreeLine,
)

KV = """
<Content>
    adaptive_height: True

    TwoLineIconListItem:
        text: '(050)-123-45-67'
        secondary_text: 'Mobile'

        IconLeftWidget:
            icon: 'phone'


ScrollView:

    MDList:
        id: box
"""


class Content(MDBoxLayout):
    """Custom content."""


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(10):
            self.root.ids.box.add_widget(
                MDExpansionPanel(
                    icon="data/logo/kivy-icon-512.png",
                    content=Content(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text="Text",
                        secondary_text="Secondary text",
                        tertiary_text="Tertiary text",
                    ),
                )
            )


Example().run()
