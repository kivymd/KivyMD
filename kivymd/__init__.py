"""
KivyMD
======

KivyMD is a collection of Material Design compliant widgets for use with Kivy,
a framework for cross-platform, touch-enabled graphical applications.
The project's goal is to approximate Google's Material Design spec as close
as possible without sacrificing ease of use or application performance.

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.
"""

import os

from kivy import Logger

__version_info__ = (0, 100, 2)
__version__ = "0.100.2"

path = os.path.dirname(__file__)
fonts_path = os.path.join(path, f"fonts{os.sep}")
images_path = os.path.join(path, f"images{os.sep}")

Logger.info(f"KivyMD: KivyMD version: {__version__}")
