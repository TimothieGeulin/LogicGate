from kivy.app import App
from kivy.config import Config 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginApp(App):
    def build(self):
        self.title = 'Se connecter'
        box = BoxLayout(orientation='horizontal')
        box.add_widget(Label(text='Pin code'))
        box.add_widget(TextInput())
        box.add_widget(Button(text='Entrer'))
        return box

Config.set('graphics', 'width', '700') 
Config.set('graphics', 'height', '200')

LoginApp().run()
