import os

from kivy.factory import Factory
from kivy.uix.screenmanager import Screen


class KitchenSinkUserCard(Screen):
    user_card = None

    def show_user_example_animation_card(self):
        """Create and open instance MDUserAnimationCard."""

        from kivymd.uix.useranimationcard import MDUserAnimationCard

        def main_back_callback():
            from kivymd.toast import toast

            toast("Close card")

        if not self.user_card:
            self.user_card = MDUserAnimationCard(
                user_name="Lion Lion",
                path_to_avatar=f"{os.environ['KITCHEN_SINK_ASSETS']}guitar-1139397_1280.png",
                callback=main_back_callback,
            )
            self.user_card.box_content.add_widget(
                Factory.KitchenSinkBaseContent()
            )
        self.user_card.open()
