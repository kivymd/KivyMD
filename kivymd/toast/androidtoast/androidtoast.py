"""

 # Will be automatically used native implementation of the toast
 # if your application is running on an Android device.
 # Otherwise, will be used toast implementation
 # from the kivymd/toast/kivytoast package.
    
 from kivymd.toast import toast
 from kivymd.app import MDApp
 from kivy.lang import Builder
 from kivy.uix.screenmanager import ScreenManager
 from kivymd.uix.screen import MDScreen
    
    
    
    
 Builder.load_string('''
 <Example>
 
     MDFlatButton:
         text:"My Toast"
         pos_hint:{"center_x": .5, "center_y": .05}
         on_press:root.show_toast()
 ''')
 
    
 class Example(MDScreen):     
     def show_toast(self):
         toast("hello world", True, 80, 200, 0) 
                        
            
        	
 class Iniciar(MDApp):     
     def build(self):
         pantalla = ScreenManager()
         screen = Example(name="one")
         pantalla.add_widget(screen)
         return pantalla
    
 Iniciar().run() 
"""
__all__ = ("toast",)

from jnius import autoclass    
from android.runnable import run_on_ui_thread as run_thread
      
__activity = autoclass( 'org.kivy.android.PythonActivity').mActivity
__Toast = autoclass('android.widget.Toast')
__String = autoclass('java.lang.String')
    
@run_thread
def toast(text, short_duration=True, gravity=0, y=0, x=0):
    """
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
  
    duration = __Toast.LENGTH_SHORT if short_duration else __Toast.LENGTH_LONG        
    toast = __Toast.makeText(__activity, __String(text), duration)        	
    toast.setGravity(gravity, x, y)
    toast.show()
    

