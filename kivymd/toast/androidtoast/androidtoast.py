# -*- coding: utf-8 -*-

'''
VKGroups

Copyright © 2010-2018 HeaTTheatR

Для предложений и вопросов:
<kivydevelopment@gmail.com>

Данный файл распространяется по услолвиям той же лицензии,
что и фреймворк Kivy.

'''

from kivy.logger import Logger
from jnius import autoclass, PythonJavaClass, java_method, cast
from android import activity
from android.runnable import run_on_ui_thread

Toast = autoclass('android.widget.Toast')
context = autoclass('org.renpy.android.PythonActivity').mActivity    

@run_on_ui_thread
def toast(text, length_long=False):
    duration = Toast.LENGTH_LONG if length_long else Toast.LENGTH_SHORT
    String = autoclass('java.lang.String')
    c = cast('java.lang.CharSequence', String(text))
    t = Toast.makeText(context, c, duration)
    t.show()
