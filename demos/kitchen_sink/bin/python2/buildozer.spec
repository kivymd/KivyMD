[app]

# (str) Title of your application
title = KivyMD Kitchen Sink

# (str) Package name
package.name = kitchen_sink

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kivymd

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = bin

# (list) List of exclusions using pattern matching
source.exclude_patterns = buildozer.spec

# (str) Application versioning (method 2)
version.regex = __version__ = ['\"]([^'\"]*)['\"]
version.filename = %(source.dir)s/../../kivymd/__init__.py

# (list) Application requirements
# comma seperated e.g. requirements = sqlite3,kivy
requirements = kivy==master,android,git+https://github.com/HeaTTheatR/KivyMD.git

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/../../kivymd/images/kivymd_logo.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = True


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
