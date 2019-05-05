"""
Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

"""


def crop_image(cutting_size, path_to_image, path_to_save_crop_image,
               corner=0, blur=0, corner_mode='all'):
    """Call functions of cropping/blurring/rounding image.

    cutting_size:            size to which the image will be cropped;
    path_to_image:           path to origin image;
    path_to_save_crop_image: path to new image;
    corner:                  value of rounding corners;
    blur:                    blur value;
    corner_mode:             'all'/'top'/'bottom' - indicates which corners to round out;

    """

    im = _crop_image(cutting_size, path_to_image, path_to_save_crop_image)
    if corner:
        im = add_corners(im, corner, corner_mode)
    if blur:
        im = add_blur(im, blur)
    try:
        im.save(path_to_save_crop_image)
    except IOError:
        im.save(path_to_save_crop_image, 'JPEG')


def add_blur(im, mode):
    from PIL import ImageFilter

    im = im.filter(ImageFilter.GaussianBlur(mode))

    return im


def _crop_image(cutting_size, path_to_image, path_to_save_crop_image):
    from PIL import Image, ImageOps

    image = Image.open(path_to_image)
    image = ImageOps.fit(image, cutting_size)
    image.save(path_to_save_crop_image)

    return image


def add_corners(im, corner, corner_mode):
    def add_top_corners():
        alpha.paste(circle.crop((0, 0, corner, corner)), (0, 0))
        alpha.paste(circle.crop(
            (corner, 0, corner * 2, corner)), (w - corner, 0))
        print(corner)

    def add_bottom_corners():
        alpha.paste(circle.crop(
            (0, corner, corner, corner * 2)), (0, h - corner))
        alpha.paste(
            circle.crop((corner, corner, corner * 2, corner * 2)), (w - corner, h - corner))
        print(corner)

    from PIL import Image, ImageDraw

    circle = Image.new('L', (corner * 2, corner * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, corner * 2, corner * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size

    if corner_mode == 'all':
        add_top_corners()
        add_bottom_corners()
    elif corner_mode == 'top':
        add_top_corners()
    if corner_mode == 'bottom':
        add_bottom_corners()
    im.putalpha(alpha)

    return im
