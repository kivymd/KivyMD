from kivymd.tests.base_test import BaseTest


class NavigationDrawerTest(BaseTest):
    def test_navigationdrawer_raw_app(self):
        from kivymd.uix.navigationdrawer import (
            MDNavigationDrawer,
            MDNavigationDrawerDivider,
            MDNavigationDrawerHeader,
            MDNavigationDrawerItem,
            MDNavigationDrawerLabel,
            MDNavigationDrawerMenu,
            MDNavigationLayout,
        )
        from kivymd.uix.screen import MDScreen
        from kivymd.uix.screenmanager import MDScreenManager
        from kivymd.uix.toolbar import MDTopAppBar

        class DrawerClickableItem(MDNavigationDrawerItem):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.focus_color = "#e7e4c0"
                self.unfocus_color = "#f7f4e7"
                self.text_color = "#4a4939"
                self.icon_color = "#4a4939"
                self.ripple_color = "#c5bdd2"
                self.selected_color = "#0c6c4d"

        class DrawerLabelItem(MDNavigationDrawerItem):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.bg_color = "#f7f4e7"
                self.text_color = "#4a4939"
                self.icon_color = "#4a4939"
                _no_ripple_effect = True  # NOQA

        self.app.theme_cls.material_style = "M3"
        self.render(
            MDNavigationLayout(
                MDScreenManager(
                    MDScreen(
                        MDTopAppBar(
                            title="Navigation Drawer",
                            elevation=10,
                            pos_hint={"top": 1},
                            md_bg_color="#e7e4c0",
                            specific_text_color="#4a4939",
                            left_action_items=[
                                ["menu", lambda x: self.nav_drawer_open()]
                            ],
                        )
                    )
                ),
                MDNavigationDrawer(
                    MDNavigationDrawerMenu(
                        MDNavigationDrawerHeader(
                            title="Header title",
                            title_color="#4a4939",
                            text="Header text",
                            spacing="4dp",
                            padding=("12dp", 0, 0, "56dp"),
                        ),
                        MDNavigationDrawerLabel(
                            text="Mail",
                        ),
                        DrawerClickableItem(
                            icon="gmail",
                            right_text="+99",
                            text_right_color="#4a4939",
                            text="Inbox",
                            radius=24,
                        ),
                        DrawerClickableItem(
                            icon="send",
                            text="Outbox",
                            radius=24,
                        ),
                        MDNavigationDrawerDivider(),
                        MDNavigationDrawerLabel(
                            text="Labels",
                        ),
                        DrawerLabelItem(
                            icon="information-outline",
                            text="Label",
                        ),
                        DrawerLabelItem(
                            icon="information-outline",
                            text="Label",
                        ),
                    ),
                    id="nav_drawer",
                ),
            )
        )
