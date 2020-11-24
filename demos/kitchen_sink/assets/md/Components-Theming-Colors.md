from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivy.properties import ListProperty, StringProperty

from kivymd.color_definitions import colors
from kivymd.uix.tab import MDTabsBase

demo = '''
<Root@BoxLayout>
    orientation: 'vertical'

    MDToolbar:
        title: app.title

    MDTabs:
        id: android_tabs
        on_tab_switch: app.on_tab_switch(*args)
        size_hint_y: None
        height: "48dp"
        tab_indicator_anim: False

    ScrollView:

        MDList:
            id: box


<ItemColor>:
    size_hint_y: None
    height: "42dp"

    canvas:
        Color:
            rgba: root.color
        Rectangle:
            size: self.size
            pos: self.pos

    MDLabel:
        text: root.text
        halign: "center"


<Tab>:
'''

from kivy.factory import Factory
from kivymd.app import MDApp


class Tab(BoxLayout, MDTabsBase):
    pass


class ItemColor(BoxLayout):
    text = StringProperty()
    color = ListProperty()


class Palette(MDApp):
    title = "Colors definitions"

    def build(self):
        Builder.load_string(demo)
        self.screen = Factory.Root()

        for name_tab in colors.keys():
            tab = Tab(text=name_tab)
            self.screen.ids.android_tabs.add_widget(tab)
        return self.screen

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tabs_label, tab_text):
        self.screen.ids.box.clear_widgets()
        for value_color in colors[tab_text]:
            self.screen.ids.box.add_widget(
                ItemColor(
                    color=get_color_from_hex(colors[tab_text][value_color]),
                    text=value_color,
                )
            )

    def on_start(self):
        self.on_tab_switch(
            None,
            None,
            None,
            self.screen.ids.android_tabs.ids.layout.children[-1].text,
        )


Palette().run()