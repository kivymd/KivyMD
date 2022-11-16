from kivy.graphics import Color

from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.recyclegridlayout import MDRecycleGridLayout
from kivymd.uix.recycleview import MDRecycleView
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.widget import MDWidget


class TestMdBgColorLayouts(MDApp):
    def build(self):
        return MDScreen()

    def on_start(self):
        for layout in [
            MDBoxLayout,
            MDRelativeLayout,
            MDWidget,
            MDStackLayout,
            MDScrollView,
            MDScreen,
            MDRecycleGridLayout,
            MDRecycleView,
            MDGridLayout,
            MDFloatLayout,
            MDAnchorLayout,
        ]:
            layout = layout(md_bg_color="red")

            self.root.clear_widgets()
            self.root.add_widget(layout)
            self.check_md_bg_color(layout)
        self.stop()

    def check_md_bg_color(self, widget):
        for instruction in widget.canvas.children:
            if isinstance(instruction, Color):
                assert instruction.rgba == [1.0, 0.0, 0.0, 1.0]
                break


TestMdBgColorLayouts().run()
