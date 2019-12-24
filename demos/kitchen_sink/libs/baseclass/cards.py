import os

from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from kivymd.toast import toast
from kivymd.utils.cropimage import crop_image


class KitchenSinkCards(Screen):
    cards_created = False
    app = ObjectProperty()

    def add_cards(self, instance_grid_card):
        """Adds MDCardPost objects to the screen Cards
        when the screen is open."""

        from kivymd.uix.card import MDCardPost

        def callback(instance, value):
            if value is None:
                toast("Delete post %s" % str(instance))
            elif isinstance(value, int):
                toast("Set like in %d stars" % value)
            elif isinstance(value, str):
                toast("Repost with %s " % value)
            elif isinstance(value, list):
                toast(value[1])

        if not self.cards_created:
            self.cards_created = True
            menu_items = [
                {
                    "viewclass": "MDMenuItem",
                    "text": "Example item %d" % i,
                    "callback": self.app.callback_for_menu_items,
                }
                for i in range(2)
            ]
            buttons = ["facebook", "vk", "twitter"]

            instance_grid_card.add_widget(
                MDCardPost(
                    text_post="Card with text", swipe=True, callback=callback
                )
            )
            instance_grid_card.add_widget(
                MDCardPost(
                    right_menu=menu_items,
                    swipe=True,
                    text_post="Card with a button to open the menu MDDropDown",
                    callback=callback,
                )
            )
            instance_grid_card.add_widget(
                MDCardPost(
                    likes_stars=True,
                    callback=callback,
                    swipe=True,
                    text_post="Card with asterisks for voting.",
                )
            )

            image_for_card = f"{os.environ['KITCHEN_SINK_ASSETS']}kitten-for_card-1049129_1280-crop.png"
            if not os.path.exists(image_for_card):
                crop_image(
                    (int(Window.width), int(dp(200))),
                    f"{os.environ['KITCHEN_SINK_ASSETS']}kitten-1049129_1280.png",
                    image_for_card,
                )
            instance_grid_card.add_widget(
                MDCardPost(
                    source=image_for_card,
                    tile_text="Little Baby",
                    tile_font_style="H5",
                    text_post="This is my favorite cat. He's only six months "
                    "old. He loves milk and steals sausages :) "
                    "And he likes to play in the garden.",
                    with_image=True,
                    swipe=True,
                    callback=callback,
                    buttons=buttons,
                )
            )