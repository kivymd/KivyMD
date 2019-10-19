from os.path import join, basename, dirname
import kivymd

datas = [
    (kivymd.fonts_path, join("kivymd", basename(dirname(kivymd.fonts_path)))),
    (kivymd.images_path, join("kivymd", basename(dirname(kivymd.images_path)))),
]
