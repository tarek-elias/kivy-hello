import kivy
from kivy.app import App
from kivy.uix.label import Label
  
kivy.require(str(kivy.__version__))  
  
# Defining a class
class MyFirstKivyApp(App):
      
    def build(self):
          

        return Label(text ="Hello World !")          
  

MyFirstKivyApp().run()