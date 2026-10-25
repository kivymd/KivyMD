from kivy.metrics import dp
from kivy.properties import ListProperty, OptionProperty

from kivymd.uix.tab import (
    IOSTabBarHorizontal,
    IOSTabBarItem,
    IOSTabBarItemIcon,
    IOSTabBarItemText,
)


class TabBarHorizontal(IOSTabBarHorizontal):
    display_mode = OptionProperty(None, options=["both", "text"])
    items_data = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.glass_color = [0.0, 0.0, 0.0, 0.1]

    def on_display_mode(self, instance, value):
        self._update_widgets()

    def _update_widgets(self):
        inactive_color = self.theme_cls.secondaryColor
        active_color = self.theme_cls.primaryColor
        mode = self.display_mode
        widgets = []

        self.height = dp(50) if mode == "text" else dp(65)

        for icon, text in self.items_data:
            children = []

            if mode == "both":
                children.append(IOSTabBarItemIcon(icon=icon))

            if mode in ("both", "text"):
                children.append(
                    IOSTabBarItemText(
                        text=text,
                        padding=[0, 0, 0, dp(6)],
                        role="medium",
                    )
                )

                if mode == "text":
                    self.padding = [dp(4), dp(4), dp(4), dp(4)]

            item = IOSTabBarItem(
                *children,
                inactive_color=inactive_color,
                active_color="#42AAFF",
            )
            widgets.append(item)

            if mode == "text":
                item.padding = [0, dp(6), 0, dp(8)]

        self.widgets = widgets
