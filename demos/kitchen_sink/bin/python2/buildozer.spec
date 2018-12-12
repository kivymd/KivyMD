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
requirements = kivy==1.10.1,pil,android,git+https://github.com/HeaTTheatR/KivyMD.git

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/presplash.png

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
android.presplash_color = #FFFFFF

# (str) Icon of the application
icon.filename = %(source.dir)s/../../kivymd/images/kivymd_logo.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to use
android.api = 19

# (int) Minimum API required
android.minapi = 19

# (int) Android SDK version to use
android.sdk = 23

# (str) Android NDK version to use
android.ndk = 16b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = False

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = /home/kivy/Android/android-ndk-r16b

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = /home/kivy/.buildozer/android/platform/android-sdk-23

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
p4a.branch = master


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
