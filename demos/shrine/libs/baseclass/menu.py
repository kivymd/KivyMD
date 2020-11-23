from kivy.properties import ListProperty, StringProperty

from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout


class ShrineItemMenu(ThemableBehavior, MDBoxLayout):
    text = StringProperty()
    color = ListProperty([0, 0, 0, 0])
    color_text = ListProperty()


class ShrineMenu(ThemableBehavior, MDBoxLayout):
    """`Menu` for `ShrineRootScreen` screen."""

    def press_on_item_menu(self, instance_item):
        """Sets the color of the separator for a pressed menu item."""

        if instance_item.text == "EXIT":
            exit()

        for widget in self.children:
            if widget.ids.separator.color == self.theme_cls.primary_color:
                widget.ids.separator.color = [0, 0, 0, 0]
                break

        instance_item.ids.separator.color = self.theme_cls.primary_color
