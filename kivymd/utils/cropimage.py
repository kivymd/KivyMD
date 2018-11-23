# -*- coding: utf-8 -*-


def crop_image(size_screen, path_to_image, path_to_save_crop_image,
               corner=0):
    im = _crop_image(size_screen, path_to_image, path_to_save_crop_image)
    if corner:
        im = add_corners(im, corner)
    im.save(path_to_save_crop_image)


def _crop_image(size_screen, path_to_image, path_to_save_crop_image):
    """Обрезает фоновое изображение под размеры карточки."""

    from PIL import Image

    im = Image.open(path_to_image)
    width, height = im.size
    width_screen,  height_screen = size_screen
    left = (width - width_screen) / 2
    top = (height - height_screen) / 2
    right = (width + width_screen) / 2
    bottom = (height + height_screen) / 2
    im.crop((left, top, right, bottom)).save(path_to_save_crop_image)
    im = Image.open(path_to_save_crop_image)

    return im


def add_corners(im, rad):
    """Добавлет сглаженые углы изображению."""

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


def resize_image(path):
    from PIL import Image

    im = Image.open(path)
    w, h = im.size
    im.thumbnail((int(w // 1.5), int(h // 1.5)), Image.ANTIALIAS)

    return im
