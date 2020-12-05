from os import environ

from kivy.uix.screenmanager import Screen

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine


class KitchenSinkExpansionPanel(Screen):
    def add_expansion_panel(self):
        content = KitchenSinkExpansionPanelContent()
        self.ids.card.add_widget(
            MDExpansionPanel(
                icon=f"{environ['KITCHEN_SINK_ASSETS']}avatar.png",
                content=content,
                panel_cls=MDExpansionPanelOneLine(text="KivyMD 0.104.2.dev0"),
            )
        )


class KitchenSinkExpansionPanelContent(MDBoxLayout):
    pass
