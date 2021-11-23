__all__ = ("toast",)

from kivy.utils import platform

if platform == "android":
    try:
        from .androidtoast import toast
    except ModuleNotFoundError:
        from .kivytoast import toast
else:
    from .kivytoast import toast
