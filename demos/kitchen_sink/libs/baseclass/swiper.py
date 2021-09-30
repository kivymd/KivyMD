import os

from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen
from kivymd.uix.swiper import MDSwiperItem


class KitchenSinkSwiperItem(MDSwiperItem):
    source = StringProperty()


class KitchenSinkSwiper(MDScreen):
    def on_enter(self):
        if len(self.ids.swiper.children) == 1:
            for images in (
                "african-lion-951778_1280.png",
                "beautiful-931152_1280.png",
                "guitar-1139397_1280.png",
                "kitten-1049129_1280.png",
                "light-bulb-1042480_1280.png",
                "robin-944887_1280.png",
            ):
                self.ids.swiper.add_widget(
                    KitchenSinkSwiperItem(
                        source=os.path.join(
                            os.environ["KITCHEN_SINK_ASSETS"], images
                        )
                    )
                )
