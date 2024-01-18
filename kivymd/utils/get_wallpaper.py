from __future__ import annotations

import os
import math

from kivy import platform, Logger


def get_wallpaper(
    user_data_dir: str, path_to_wallpaper: str = ""
) -> bool | str:
    if platform == "android":
        try:
            from jnius import autoclass, cast
            from android import mActivity

            CompressFormat = autoclass("android.graphics.Bitmap$CompressFormat")
            FileOutputStream = autoclass("java.io.FileOutputStream")
            WallpaperManager = autoclass("android.app.WallpaperManager")
            Bitmap = autoclass("android.graphics.Bitmap")
            
            Context = mActivity.getApplicationContext()
            mWallpaperManager = WallpaperManager.getInstance(Context)
            bitmap = mWallpaperManager.getBitmap()

            # Scale the bitmap down as needed
            # Taken from:
            # https://android.googlesource.com/platform/frameworks/support/+/refs/heads/androidx-main/palette/palette/src/main/java/androidx/palette/graphics/Palette.java#890
            DEFAULT_RESIZE_BITMAP_AREA = 112 * 112 # Android default
            bitmapArea = bitmap.getWidth() * bitmap.getHeight()
            scaleRatio = -1

            if bitmapArea > DEFAULT_RESIZE_BITMAP_AREA:
                    scaleRatio = math.sqrt(DEFAULT_RESIZE_BITMAP_AREA / bitmapArea)

            if scaleRatio >= 0:
                bitmap = Bitmap.createScaledBitmap(
                    bitmap,
                    math.ceil(bitmap.getWidth() * scaleRatio),
                    math.ceil(bitmap.getHeight() * scaleRatio),
                    False
                )

            bitmap.compress(
                CompressFormat.PNG,
                100,
                FileOutputStream(f"{user_data_dir}/wallpaper.png"),
            )
            return f"{user_data_dir}/wallpaper.png"
        except Exception as exc:
            Logger.error(
                f"KivyMD: Dynamic color will not be used. "
                f"The default palette is set. "
                f"{exc}"
            )
            return False
    else:
        if path_to_wallpaper:
            return (
                path_to_wallpaper
                if os.path.exists(path_to_wallpaper)
                else False
            )
        else:
            return False
