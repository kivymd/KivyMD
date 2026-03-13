from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import (
    MDTabsPrimary,
    MDTabsItem,
    MDTabsItemText,
    MDTabsCarousel
)
from kivymd.uix.appbar import MDTopAppBarTitle
KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            type: "small"
            MDTopAppBarTitle:
                text: "Tab Manager Test"

        MDTabsPrimary:
            id: tabs_manager
            # Ensure the tabs component takes up the remaining vertical space
            size_hint_y: 1

            MDDivider:

            MDTabsCarousel:
                id: content_carousel

        MDBoxLayout:
            adaptive_height: True
            padding: "10dp"
            spacing: "10dp"
            # md_bg_color: self.theme_cls.surfaceContainerColor

            MDButton:
                style: "filled"
                on_release: app.add_custom_tab()
                MDButtonText:
                    text: "Add Tab"
            
            MDButton:
                style: "filled"
                on_release: app.remove_tab()
                MDButtonText:
                    text: "Remove Tab"
'''


class TabContent(MDBoxLayout):
    """Custom content widget that knows how to remove itself."""

    def __init__(self, tab_title, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = "20dp"
        self.spacing = "20dp"
        # Ensure content fills the carousel slide
        self.size_hint = (1, 1)

        self.add_widget(MDLabel(
            text=f"Content for {tab_title}",
            halign="center",
            theme_text_color="Primary"
        ))

        btn = MDButton(
            MDButtonText(text="Remove this Tab"),
            style="tonal",
            pos_hint={"center_x": .5},
            on_release=lambda x: self.remove_me()
        )
        self.add_widget(btn)

    def remove_me(self):
        app = MDApp.get_running_app()
        app.root.ids.tabs_manager.remove_widget(self)


class TabManagementApp(MDApp):
    index = 0

    def build(self):
        self.theme_cls.primary_palette = "Olive"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(2):
            self.add_custom_tab()

    def add_custom_tab(self):
        self.index += 1
        title = f"Tab {self.index}"

        # 1. Create the Header
        tab_header = MDTabsItem(
            MDTabsItemText(text=title)
        )

        # 2. Create the Content
        tab_content = TabContent(tab_title=title)

        # 3. Add widgets
        self.root.ids.tabs_manager.add_widget(tab_header)
        self.root.ids.content_carousel.add_widget(tab_content)

        # 4. Switch to the new tab
        self.root.ids.tabs_manager.switch_tab(instance=tab_header)

    def remove_tab(self):
        tab_item = self.root.ids.content_carousel.current_slide.tab_item
        self.root.ids.tabs_manager.remove_widget(tab_item)


if __name__ == "__main__":
    TabManagementApp().run()