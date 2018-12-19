# -*- coding: utf-8 -*-


def crop_image(size_screen, path_to_image, path_to_save_crop_image,
               corner=False):
    im = _crop_image(size_screen, path_to_image, path_to_save_crop_image)
    if corner:
        im = add_corners(im, 25)
    try:
        im.save(path_to_save_crop_image)
    except IOError:
        im.save(path_to_save_crop_image, 'JPEG')


def _crop_image(size_screen, path_to_image, path_to_save_crop_image):
    from PIL import Image, ImageOps

    image = Image.open(path_to_image)
    image = ImageOps.fit(image, size_screen)
    image.save(path_to_save_crop_image)

    return image


def add_corners(im, rad):
    from PIL import Image, ImageDraw

    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)

    return im
