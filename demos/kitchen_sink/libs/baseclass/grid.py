import os

from kivy.uix.screenmanager import Screen

from kivymd.utils.cropimage import crop_image


class KitchenSinkGrid(Screen):
    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        """Crop images for Grid screen."""

        if not os.path.exists(
            os.path.join(os.environ["KITCHEN_SINK_ASSETS"], path_to_crop_image)
        ):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace("_tile_crop", "")
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image
