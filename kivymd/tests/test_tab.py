from kivy.tests.common import GraphicUnitTest


class TabTest(GraphicUnitTest):
    def test_tab_raw_app(self):
        from kivymd.app import MDApp
        from kivymd.uix.floatlayout import MDFloatLayout
        from kivymd.uix.tab import MDTabs, MDTabsBase

        class Tab(MDFloatLayout, MDTabsBase):
            pass

        render = self.render
        app = MDApp()  # NOQA
        tab = MDTabs()
        tab.add_widget(Tab(title="Tab"))
        render(tab)
