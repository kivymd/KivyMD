from kivymd.tests.base_test import BaseTest


class ListTest(BaseTest):
    def test_list_raw_app(self):
        import os

        from kivymd import images_path
        from kivymd.uix.list import (
            IconLeftWidget,
            IconRightWidget,
            ImageLeftWidget,
            IRightBodyTouch,
            MDList,
            OneLineAvatarIconListItem,
            OneLineAvatarListItem,
            OneLineIconListItem,
            OneLineListItem,
            ThreeLineListItem,
            TwoLineListItem,
        )
        from kivymd.uix.screen import MDScreen
        from kivymd.uix.scrollview import MDScrollView
        from kivymd.uix.selectioncontrol import MDCheckbox

        class RightCheckbox(IRightBodyTouch, MDCheckbox):
            pass

        self.render(
            MDScreen(
                MDScrollView(
                    MDList(
                        OneLineListItem(text="Text"),
                        TwoLineListItem(
                            text="Text", secondary_text="secondary text"
                        ),
                        ThreeLineListItem(
                            text="Text",
                            secondary_text="secondary text",
                            tertiary_text="tertiary text",
                        ),
                        OneLineAvatarListItem(
                            ImageLeftWidget(
                                source=os.path.join(
                                    images_path, "logo", "kivymd-icon-512.png"
                                )
                            ),
                            text="Text",
                        ),
                        OneLineIconListItem(
                            IconLeftWidget(icon="plus"),
                            text="Text",
                        ),
                        OneLineAvatarIconListItem(
                            IconLeftWidget(icon="plus"),
                            IconRightWidget(icon="minus"),
                            text="Text",
                        ),
                        OneLineAvatarIconListItem(
                            IconLeftWidget(icon="plus"),
                            RightCheckbox(),
                            text="Text",
                        ),
                    )
                )
            )
        )
