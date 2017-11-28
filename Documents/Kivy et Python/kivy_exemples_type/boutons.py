from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

class SignallingApp(App):
	def build (self) :
		self.title = 'Feu de signalisation'
		# Selection de la ville du feu (et la ville de l'eau alors? lolilol)
		city = BoxLayout (orientation = 'horizontal')
		city.add_widget (Label (text = 'Feu'))
		cities = ('Bruxelles', 'Gent', 'Namur')
		#---------- liste deroulante ----------
		city.add_widget (Spinner (values=cities))
		# Activation ou non du feu
		activation = BoxLayout (orientation = 'horizontal')
		#----------	case a cocher ----------
		activation.add_widget(CheckBox())
		activation.add_widget (Label (text = 'Activer le feu'))
		# Choix de l'etat du feu (rouge, orange ou vert)
		state = BoxLayout (orientation = 'horizontal')
		#----------	bouton radio ----------
		state.add_widget (CheckBox(group='state'))
		state.add_widget(Label(text='Rouge'))
		state.add_widget(CheckBox(group='state'))
		state.add_widget(Label(text='Orange'))
		state.add_widget(CheckBox(group='state'))
		state.add_widget(Label(text='Vert'))
		
		#Composant principal
		box = BoxLayout (orientation = 'vertical')
		box.add_widget(city)
		box.add_widget(activation)
		box.add_widget(state)
		
		return box

SignallingApp().run()
