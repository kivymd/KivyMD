from kivy.factory import Factory
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons


class KitchenSinkTabs(Screen):
    list_name_icons = list(md_icons.keys())[0:15]
    tabs_created = False

    def on_enter(self):
        if not self.tabs_created:
            for name_tab in self.list_name_icons:
                self.ids.android_tabs.add_widget(
                    Factory.KitchenSinkTabItem(text=name_tab)
                )
            self.tabs_created = True

    def switch_tabs_to_text(self, instance_android_tabs):
        for instance_tab in instance_android_tabs.ids.scrollview.children[
            0
        ].children:
            for k, v in md_icons.items():
                if v == instance_tab.text:
                    instance_android_tabs.ids.scrollview.children[
                        0
                    ].remove_widget(instance_tab)
                    instance_android_tabs.add_widget(
                        Factory.KitchenSinkTabItem(
                            text=" ".join(k.split("-")).capitalize()
                        )
                    )
                    break

    def switch_tabs_to_icon(self, instance_android_tabs):
        for i, instance_tab in enumerate(
            instance_android_tabs.ids.scrollview.children[0].children
        ):
            instance_android_tabs.ids.scrollview.children[0].remove_widget(
                instance_tab
            )
            instance_android_tabs.add_widget(
                Factory.KitchenSinkTabItem(text=self.list_name_icons[i])
            )
