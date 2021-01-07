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
        : param text: texto que se mostrará en el brindis 
        ;: param short_duration: duración del brindis, si` True` el brindis 
               durará 2.3s pero si es "Falso" el brindis durará 3.9s;: 
        param gravity: se refiere a la posición del brindis, si es 80 el brindis se 
               mostrará abajo, si es 40 el brindis se mostrará arriba ; 
        : param y: se refiere a la posición vertical del brindis;
        : param x: se refiere a la posición horizontal del brindis;

        Importante: si solo se especifica el valor de texto y no se especifica el valor de 
        los parámetros `gravedad`,` y`, `x`, sus valores serán 
        0, lo que significa que el brindis se mostrará en el centro. 
        """


  
    duration = __Toast.LENGTH_SHORT if short_duration else __Toast.LENGTH_LONG        
    toast = __Toast.makeText(__activity, __String(text), duration)        	
    toast.setGravity(gravity, x, y)
    toast.show()
    

