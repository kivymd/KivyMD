from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.theming import ThemableBehavior


class ShrineItemMenu(ThemableBehavior, BoxLayout):
    text = StringProperty()
    color = ListProperty([0, 0, 0, 0])
    color_text = ListProperty()


class ShrineMenu(ThemableBehavior, BoxLayout):
    """`Menu` for `ShrineRootScreen` screen."""

    def press_on_item_menu(self, instance_item):
        """Sets the color of the separator for a pressed menu item."""

        for widget in self.children:
            if widget.ids.separator.color == self.theme_cls.primary_color:
                widget.ids.separator.color = [0, 0, 0, 0]
                break

        instance_item.ids.separator.color = self.theme_cls.primary_color
