from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder

monEcran=Builder.load_file("main.kv")
 
class MonAppli(App):
 
    def build(self):
        return monEcran

Config.set('graphics','width','800')
Config.set('graphics','height','400')
 
MonAppli().run()
