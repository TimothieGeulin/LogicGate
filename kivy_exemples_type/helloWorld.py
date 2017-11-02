from kivy.app import App
from kivy.config import Config 
from kivy.uix.button import Label

class HelloApp(App):
    def build(self):
        self.title = 'Hello World!'
        self.icon = 'hello.png'
        return Label(text='Hello World!')

Config.set('graphics', 'width', '1000') 
Config.set('graphics', 'height', '500')

HelloApp().run()
