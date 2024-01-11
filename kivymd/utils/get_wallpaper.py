from __future__ import annotations

import os

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
            Context = mActivity.getApplicationContext() 
            mWallpaperManager = WallpaperManager.getInstance(Context)
            mWallpaperManager.getBitmap().compress(
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
