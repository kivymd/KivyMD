# from kivymd.icon_definitions import md_icons
#
# from kivymd.uix.screen import MDScreen
# from kivymd.uix.tab import MDTabs, MDTabsItem, MDTabsIcon
# from kivymd.app import MDApp
# from kivymd.uix.tab.tab import MDTabsText
#
#
# class Example(MDApp):
#     def build(self):
#         screen = MDScreen(
#             MDTabs(
#                 id="tabs",
#                 pos_hint={"top": 1},
#             ),
#             md_bg_color=self.theme_cls.backgroundColor,
#         )
#         for i, icon in enumerate(list(md_icons.keys())[0:30]):
#             screen.get_ids()["tabs"].add_widget(
#                 MDTabsItem(
#                     MDTabsIcon(
#                         icon=icon,
#                         text_color="red",
#                     ),
#                     MDTabsText(
#                         text=f"Tab {i + 1}",
#                     ),
#                     theme_text_color="Custom",
#                 )
#             )
#         return screen
#
#
# Example().run()
