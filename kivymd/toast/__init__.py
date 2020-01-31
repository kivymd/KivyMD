from kivy.utils import platform


if platform == "android":
    from .androidtoast import toast
else:
    from .kivytoast import toast
