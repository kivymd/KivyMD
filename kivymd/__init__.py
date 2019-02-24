# -*- coding: utf-8 -*-

"""
KivyMD
======

Copyright © 2010-2018 HeaTTheatR

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.
"""

import os

from kivy import Logger

__version_info__ = (0, 92, 1)
__version__ = '0.92.1'

path = os.path.dirname(__file__)
fonts_path = os.path.join(path, "fonts/")
images_path = os.path.join(path, 'images/')

Logger.info("KivyMD: KivyMD version: {}".format(__version__))
