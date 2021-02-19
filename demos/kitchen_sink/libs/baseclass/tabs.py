from kivy.factory import Factory
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons


class KitchenSinkTabs(Screen):
    # Icons to be used to populate the tabs.
    list_name_icons = list(md_icons.keys())[0:15]
    # lock the memory to avoid duplicity.
    tabs_created = False

    def on_enter(self):
        # updates the screen afther the animation ends.
        if not self.tabs_created:
            for name_tab in self.list_name_icons:
                self.ids.android_tabs.add_widget(
                    Factory.KitchenSinkTabItem(title=name_tab)
                )
            self.tabs_created = True

    def switch_tabs_to_text(self, instance_android_tabs):
        # This function will toggle between text title label to icon title
        # label for each tab
        slides = instance_android_tabs.get_slides()
        for slide in slides:
            if slide.icon:
                slide.title = slide.icon
                slide.icon = ""

    def switch_tabs_to_icon(self, instance_android_tabs):
        # This function will toggle between text title label to icon title
        # label for each tab
        slides = instance_android_tabs.get_slides()
        for slide in slides:
            if slide.title:
                slide.icon = slide.title.lower()
                slide.title = ""

    def new_update_label(self, instance_android_tabs):
        # This function will add either the tittle or the icon to the
        # tab's title label.
        slides = instance_android_tabs.get_slides()
        for slide in slides:
            if slide.icon:
                slide.title = slide.icon
            elif slide.title:
                slide.icon = slide.title.lower()

    def update_mode(self, instance_android_tabs):
        # This function will update the way in wich the title label displays
        # the title text and icon.
        if instance_android_tabs.title_icon_mode == "Lead":
            instance_android_tabs.title_icon_mode = "Top"
        else:
            instance_android_tabs.title_icon_mode = "Lead"
