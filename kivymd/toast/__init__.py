"""
Toast
=====

Copyright (c) 2013 Brian Knapp - androidtoast module
Copyright (c) 2019 Ivanov Yuri - kivytoast module

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.
"""

from kivy.utils import platform


if platform == "android":
    from .androidtoast import toast
else:
    from .kivytoast import toast
