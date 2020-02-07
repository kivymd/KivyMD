from kivy.properties import (
    StringProperty,
    NumericProperty,
    ListProperty,
    ObjectProperty,
)
from kivy.uix.boxlayout import BoxLayout

from kivymd.theming import ThemableBehavior


class ProductsBox(BoxLayout):
    box_height = NumericProperty()
    box_width = NumericProperty()
    _root = ObjectProperty()
    paths_to_images = ListProperty()
    """List of paths to images. It should be as follows:

    [
        [path1, path2, path3], [path1, path2, path3], ...
    ]
    """
    products_description = ListProperty()
    """List of description images. It should be as follows:

    [
        [desc1, desc2, desc3], [desc1, desc2, desc3], ...
    ]
    """
    callback = ObjectProperty()


class ImageProduct(ThemableBehavior, BoxLayout):
    path_to_image = StringProperty()
    products_description = StringProperty()
    callback = ObjectProperty()
    _root = ObjectProperty()
