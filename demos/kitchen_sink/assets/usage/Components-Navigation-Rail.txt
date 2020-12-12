from kivy.lang import Builder
from kivy.uix.image import Image

from kivymd.app import MDApp

KV = """
#:import gch kivy.utils.get_color_from_hex

MDBoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: 'MDNavigationRail'
        md_bg_color: gch('#344954')

    MDBoxLayout:

        MDNavigationRail:
            id: rail
            md_bg_color: gch('#344954')
            color_normal: gch('#718089')
            color_active: gch('#f3ab44')

            MDNavigationRailItem:
                icon: 'language-cpp'
                text: 'C++'

            MDNavigationRailItem:
                icon: 'language-python'
                text: 'Python'

            MDNavigationRailItem:
                icon: 'language-swift'
                text: 'Swift'

        MDBoxLayout:
            padding: '24dp'

            ScrollView:

                MDList:
                    id: box
                    cols: 3
                    spacing: '12dp'
"""


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(9):
            tile = Image(source="data/logo/kivy-icon-256.png", size_hint_y=None)
            self.root.ids.box.add_widget(tile)


Example().run()
