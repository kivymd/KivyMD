"""
AndroidToast
============

.. rubric:: Native implementation of toast for Android devices.

.. code-block:: python

    from kivymd.app import MDApp
    # Will be automatically used native implementation of the toast
    # if your application is running on an Android device.
    # Otherwise, will be used toast implementation
    # from the kivymd/toast/kivytoast package.
    from kivymd.toast import toast

    KV = '''
    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            id: toolbar
            title: 'Test Toast'
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['menu', lambda x: '']]

        FloatLayout:

            MDRaisedButton:
                text: 'TEST KIVY TOAST'
                on_release: app.show_toast()
                pos_hint: {'center_x': .5, 'center_y': .5}

    '''


    class Test(MDApp):
        def show_toast(self):
            '''Displays a toast on the screen.'''

            toast('Test Kivy Toast')

        def build(self):
            return Builder.load_string(KV)

    Test().run()
"""

__all__ = ("toast",)

from android.runnable import run_on_ui_thread
from jnius import autoclass, cast

Toast = autoclass("android.widget.Toast")
context = autoclass("org.kivy.android.PythonActivity").mActivity


@run_on_ui_thread
def toast(text, length_long=False):
    """Displays a toast.

    :length_long: The amount of time (in seconds) that the toast is visible on the screen.
    """

    duration = Toast.LENGTH_LONG if length_long else Toast.LENGTH_SHORT
    String = autoclass("java.lang.String")
    c = cast("java.lang.CharSequence", String(text))
    t = Toast.makeText(context, c, duration)
    t.show()
