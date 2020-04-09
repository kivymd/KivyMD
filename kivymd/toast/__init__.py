from kivy.utils import platform


if platform == "android":
    try:
        from .androidtoast import toast
    except:
        from .kivytoast import toast
else:
    from .kivytoast import toast
