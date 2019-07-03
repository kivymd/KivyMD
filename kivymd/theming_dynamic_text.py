"""
Bottom Sheets
=============

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

Two implementations. The first is based on color brightness obtained from:-
https://www.w3.org/TR/AERT#color-contrast
The second is based on relative luminance calculation for sRGB obtained from:-
https://www.w3.org/TR/2008/REC-WCAG20-20081211/#relativeluminancedef
and contrast ratio calculation obtained from:-
https://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef

Preliminary testing suggests color brightness more closely matches the
Material Design spec suggested text colors, but the alternative implementation
is both newer and the current 'correct' recommendation, so is included here
as an option.
"""


def _color_brightness(color):
    # Implementation of color brightness method
    brightness = color[0] * 299 + color[1] * 587 + color[2] * 114
    brightness = brightness
    return brightness


def _black_or_white_by_color_brightness(color):
    if _color_brightness(color) >= 500:
        return "black"
    else:
        return "white"


def _normalized_channel(color):
    # Implementation of contrast ratio and relative luminance method
    if color <= 0.03928:
        return color / 12.92
    else:
        return ((color + 0.055) / 1.055) ** 2.4


def _luminance(color):
    rg = _normalized_channel(color[0])
    gg = _normalized_channel(color[1])
    bg = _normalized_channel(color[2])
    return 0.2126 * rg + 0.7152 * gg + 0.0722 * bg


def _black_or_white_by_contrast_ratio(color):
    l_color = _luminance(color)
    l_black = 0.0
    l_white = 1.0
    b_contrast = (l_color + 0.05) / (l_black + 0.05)
    w_contrast = (l_white + 0.05) / (l_color + 0.05)
    return "white" if w_contrast >= b_contrast else "black"


def get_contrast_text_color(color, use_color_brightness=True):
    if use_color_brightness:
        contrast_color = _black_or_white_by_color_brightness(color)
    else:
        contrast_color = _black_or_white_by_contrast_ratio(color)
    if contrast_color == "white":
        return 1, 1, 1, 1
    else:
        return 0, 0, 0, 1


if __name__ == "__main__":
    from kivy.utils import get_color_from_hex
    from kivymd.color_definitions import colors, text_colors

    for c in colors.items():
        if c[0] in ["Light", "Dark"]:
            continue
        color = c[0]
        print(f"For the {color} color palette:")
        for name, hex_color in c[1].items():
            if hex_color:
                col = get_color_from_hex(hex_color)
                col_bri = get_contrast_text_color(col)
                con_rat = get_contrast_text_color(col, use_color_brightness=False)
                text_color = text_colors[c[0]][name]
                print(
                    f"   The {name} hue gives {col_bri} using color "
                    f"brightness, {con_rat} using contrast ratio, and "
                    f"{text_color} from the MD spec"
                )
