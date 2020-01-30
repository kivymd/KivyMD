import os
from kivy.logger import Logger

__version_info__ = (0, 103, 0)
__version__ = "0.103.0"

path = os.path.dirname(__file__)
fonts_path = os.path.join(path, f"fonts{os.sep}")
images_path = os.path.join(path, f"images{os.sep}")

Logger.info(f"KivyMD: v{__version__}")

import kivymd.factory_registers
from kivymd.tools.packaging.pyinstaller import hooks_path
