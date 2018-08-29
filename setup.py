# -*- coding: utf-8 -*-

import re
from distutils.core import setup

VERSION_FILE = "kivymd/__init__.py"
ver_file_data = open(VERSION_FILE, "rt").read()
ver_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
ver_reg_search = re.search(ver_regex, ver_file_data, re.M)
if ver_reg_search:
    version = ver_reg_search.group(1)
else:
    raise ValueError("Unable to find version string in {}.".format(VERSION_FILE))

setup(name='kivymd',
      version=version,
      description='Set of widgets for Kivy inspired by Google\'s Material '
                  'Design',
      author='Andrés Rodríguez',
      author_email='andres.rodriguez@lithersoft.com',
      url='https://gitlab.com/kivymd/KivyMD',
      packages=['kivymd'],
      package_data={
          'kivymd': ['images/*.png', 'images/*.jpg', 'images/*.atlas',
                     'vendor/*.py',
                     'fonts/*.ttf', 'vendor/circleLayout/*.py',
                     'vendor/circularTimePicker/*.py',
                     'vendor/navigationdrawer/*.py']},
      requires=['kivy']
      )
