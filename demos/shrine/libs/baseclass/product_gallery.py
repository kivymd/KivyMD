from kivy.properties import (
    ListProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)

from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout


class ProductsBox(MDBoxLayout):
    box_height = NumericProperty()
    box_width = NumericProperty()
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
    _root = ObjectProperty()


class ImageProduct(ThemableBehavior, MDBoxLayout):
    path_to_image = StringProperty()
    products_description = StringProperty()
    callback = ObjectProperty()
    _root = ObjectProperty()
