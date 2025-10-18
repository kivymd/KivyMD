from kivy.clock import Clock
from kivy.lang import Builder

from examples.common_app import CommonApp
from kivymd.app import MDApp

KV = """
MDScreen:
    md_bg_color:app.theme_cls.surfaceColor
    BoxLayout:
        orientation:"vertical"
        BoxLayout:
            size_hint_y:None
            height:dp(50)
            MDIconButton:
                size_hint:None, None
                size:[dp(50)] * 2
                on_release: app.open_menu(self)
                icon: "dots-vertical"
            Widget:

        Widget:
        AnchorLayout:
            MDLoadingIndicator:
                id:indicator
                shape_size: dp(100)
        Widget:
"""


class ExampleApp(MDApp, CommonApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.indicator.start()
        print(self.root.ids.indicator.get_shape_names())
        # stop animation
        # Clock.schedule_once(self.root.ids.indicator.stop, 5)

ExampleApp().run()
