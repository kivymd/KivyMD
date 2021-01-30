"""
AndroidToast
============

.. rubric:: Native implementation of toast for Android devices.

.. code-block:: python

    # Will be automatically used native implementation of the toast
    # if your application is running on an Android device.
    # Otherwise, will be used toast implementation
    # from the kivymd/toast/kivytoast package.

    from kivy.lang import Builder
    from kivy.uix.screenmanager import ScreenManager

    from kivymd.toast import toast
    from kivymd.app import MDApp

    KV = '''
    MDScreen:

         MDFlatButton:
             text: "My Toast"
             pos_hint:{"center_x": .5, "center_y": .5}
             on_press: app.show_toast()
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def show_toast(self):
            toast("Hello World", True, 80, 200, 0)


    Test().run()
"""
__all__ = ("toast",)

from android.runnable import run_on_ui_thread
from jnius import autoclass

activity = autoclass("org.kivy.android.PythonActivity").mActivity
Toast = autoclass("android.widget.Toast")
String = autoclass("java.lang.String")


@run_on_ui_thread
def toast(text, length_long=False, gravity=0, y=0, x=0):
    """
    Displays a toast.

    :param length_long: the amount of time (in seconds) that the toast is
           visible on the screen.
    :param text: text to be displayed in the toast;
    :param short_duration:  duration of the toast, if `True` the toast
           will last 2.3s but if it is `False` the toast will last 3.9s;
    :param gravity: refers to the toast position, if it is 80the toast will
           be shown below, if it is 40 the toast will be displayed above;
    :param y: refers to the vertical position of the toast;
    :param x: refers to the horizontal position of the toast;

    Important: if only the text value is specified and the value of
    the `gravity`, `y`, `x` parameters is not specified, their values ​​will
    be 0 which means that the toast will be shown in the center.
    """

    duration = Toast.LENGTH_SHORT if length_long else Toast.LENGTH_LONG
    t = Toast.makeText(activity, String(text), duration)
    t.setGravity(gravity, x, y)
    t.show()
