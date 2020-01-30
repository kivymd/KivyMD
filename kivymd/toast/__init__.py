"""
.. rubric:: Toast for Android device.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toast.png

"""


from kivy.utils import platform


if platform == "android":
    from .androidtoast import toast
else:
    from .kivytoast import toast
