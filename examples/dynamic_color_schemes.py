from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.app import MDApp
from kivymd.dynamic_color import DynamicColor
from examples.common_app import CommonApp, KV

Builder.load_string("""
<DynamicColorInfo>:
    name: "primaryColor"
    color:[0,0,0,0]
    size_hint_y:None
    height:dp(120)
    orientation:"vertical"
    BoxLayout:
        spacing:dp(10)
        MDIconButton:
            icon:"clipboard-text"
            size_hint_x:None
            width:dp(50)
        MDLabel:
            text:root.name
            adaptive_height:True
    MDBoxLayout:
        md_bg_color:root.color
        radius:dp(10)

<Container>:
    ScrollView:
        MDBoxLayout:
            orientation:"vertical"
            id:main_view
            adaptive_height:True
            spacing:dp(20)
""")

class Container(MDBoxLayout):
    pass

class DynamicColorInfo(BoxLayout):
    pass

class Example(MDApp, CommonApp):
    def build(self):
        #self.theme_cls.dynamic_color = True
        #self.theme_cls.path_to_wallpaper = "/home/tdynamos/Downloads/fortuti.png"
        self.theme_cls.on_colors = lambda : Clock.schedule_once(self.refresh)
        return Builder.load_string(KV)

    def on_start(self):
        super().on_start()
        parent_widget = self.root.ids.widget_box.parent.parent
        parent_widget.clear_widgets() 
        self.container = Container()
        parent_widget.add_widget(self.container)
        self.container.ids.main_view.clear_widgets()

        for color in vars(DynamicColor).keys():
            if "__" in color:
                continue
            widget = DynamicColorInfo()
            widget.name = color
            widget.color = getattr(self.theme_cls, color)
            self.container.ids.main_view.add_widget(widget)

        Clock.schedule_once(self.refresh)
    
    def refresh(self, *arg):
        for widget in self.container.ids.main_view.children:
            widget.color = getattr(self.theme_cls, widget.name) 

Example().run()
