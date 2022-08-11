from kivymd.tests.base_test import BaseTest


class TabTest(BaseTest):
    def test_tab_raw_app(self):
        from kivymd.uix.floatlayout import MDFloatLayout
        from kivymd.uix.tab import MDTabs, MDTabsBase

        class Tab(MDFloatLayout, MDTabsBase):
            pass

        tab = MDTabs()
        tab.add_widget(Tab(title="Tab"))
        self.render(tab)
