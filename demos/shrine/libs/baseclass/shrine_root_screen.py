import os

from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen

from .box_bottom_sheet import PreviousImage
from .product_gallery import ProductsBox

# splits the list into equal parts
split_list = lambda l, s: [l[i : i + s] for i in range(0, len(l), s)]


class ShrineRootScreen(ThemableBehavior, MDScreen):
    """The screen that opens after user registration."""

    title = StringProperty()

    def hide_image_list(self):
        Animation(y=-self.height + dp(100), d=0.2).start(self.ids.image_list)

    def open_image_list(self):
        Animation(y=0, d=0.2).start(self.ids.image_list)

    def set_products_list(self):
        path_do_image_dir = f"{os.environ['SHRINE_ROOT']}/assets/images/clock"
        products_list = []
        products_description = [
            [
                "[b]Casio[/b]\n$ 120",
                "[b]Q&Q[/b]\n$ 190.99",
                "[b]Slava[/b]\n$ 90",
            ],
            [
                "[b]Guardo[/b]\n$ 329.50",
                "[b]Timex[/b]\n$ 100",
                "[b]Royal London[/b]\n$ 99.99",
            ],
            [
                "[b]Daniel Klein[/b]\n$ 1499.99",
                "[b]Pierre Ricaud[/b]\n$ 420",
                "[b]Orient[/b]\n$ 130",
            ],
            [
                "[b]Swiss Military[/b]\n$ 160",
                "[b]Fossil$ 120[/b]\n",
                "[b]Romanson[/b]\n$ 260",
            ],
        ]

        for name_image in os.listdir(path_do_image_dir):

            path_to_image = f"{path_do_image_dir}/{name_image}"
            products_list.append(path_to_image)
        products_list = split_list(products_list, 3)

        return products_list, products_description

    def add_products_box_to_image_list(
        self, products_list, products_description
    ):
        for i, paths_to_images in enumerate(products_list):
            self.ids.product_gallery.add_widget(
                ProductsBox(
                    paths_to_images=paths_to_images,
                    products_description=products_description[i],
                    box_width=self.ids.image_list.width,
                    box_height=self.ids.image_list.height,
                    callback=self.add_product_to_box_bottom_sheet,
                    _root=self,
                )
            )

    def add_product_to_box_bottom_sheet(self, instanse_box_image):
        self.ids.box_bottom_sheet.ids.previous_box.add_widget(
            PreviousImage(
                source=instanse_box_image.ids.image_product.source,
                size_hint=(None, None),
                size=(dp(42), dp(42)),
                description=instanse_box_image.ids.description.text,
                _root=self,
            )
        )
        width = self.ids.box_bottom_sheet.width + dp(52)
        Animation.stop_all(self)
        Animation(width=width, d=0.1).start(self.ids.box_bottom_sheet)
