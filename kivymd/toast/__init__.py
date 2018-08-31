# -*- coding: utf-8 -*-

''' 
Разработано специально для проекта VKGroups -
https://github.com/HeaTTheatR/VKGroups

Copyright © 2010-2018 HeaTTheatR

Для предложений и вопросов:
<kivydevelopment@gmail.com>

Данный файл распространяется по услолвиям той же лицензии,
что и фреймворк Kivy.

'''

from kivy import platform


if platform == 'android': 
    from . androidtoast import toast
else:
    from . kivytoast import toast
