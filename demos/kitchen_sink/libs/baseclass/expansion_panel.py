from os import environ

from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.screen import MDScreen


class KitchenSinkExpansionPanel(MDScreen):
    def add_expansion_panel(self):
        content = KitchenSinkExpansionPanelContent()
        self.ids.card.add_widget(
            MDExpansionPanel(
                icon=f"{environ['KITCHEN_SINK_ASSETS']}avatar.png",
                content=content,
                panel_cls=MDExpansionPanelOneLine(text="KivyMD 0.104.2.dev0"),
            )
        )


class KitchenSinkExpansionPanelCard(MDCard, FakeRectangularElevationBehavior):
    pass


class KitchenSinkExpansionPanelContent(MDBoxLayout):
    pass
