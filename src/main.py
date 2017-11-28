import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, BooleanProperty
from kivy.vector import Vector
from kivy.clock import Clock




"""
Classe basique d'une porte logique.
Attributs:
	-selected: indique si l'objet est en train d'etre deplace
	-outx: coordonnees x de la fin du fil de sortie
	-outy: coordonees y de la fin du fil de sortie
"""
class Gate(Widget):

    selected = BooleanProperty(0)
    outx = NumericProperty(0)
    outy = NumericProperty(0)





"""
Classe definissant les evenements qui constituent le fonctionnement du jeu
Attributs:
	-gateList: Liste des portes actuellement en jeu
"""
class LGGame(Widget):
	gateList = []
	
	#Evenement se declenchant au toucher de l'utilisateur sur l'ecran ou au clic de la souris
	#Permet la selection et le deplacement des portes
	def on_touch_move(self, touch):
		gate_grab = False
		
		for gate in self.gateList:
			if(gate.selected) & (touch.x > gate.x) & (touch.y > gate.y) & (touch.x < gate.x + gate.size[0]) & (touch.y < gate.y + gate.size[1]):
				if not (gate_grab):
					gate.center_y = touch.y
					gate.center_x = touch.x
					gate_grab = True
			else:
				gate.selected = False

		if not (gate_grab):
			for gate in self.gateList:
				if(touch.x > gate.x) & (touch.y > gate.y) & (touch.x < gate.x + gate.size[0]) & (touch.y < gate.y + gate.size[1]):
					gate.center_y = touch.y
					gate.center_x = touch.x
					gate.selected = True
					gate_grab = True
					return
			
	#Methode de creation d'une nouvelle porte, appele par le bouton correspondant dans l'interface
	def new_gate(self):
		gate = Gate()
		self.add_widget(gate)
		self.gateList.append(gate)





"""
Classe definissant l'application, elle represente le coeur du programme
Attributs:
	-game: Le jeu lui meme, qui sera par la suite recupere par le processus de Kivy
"""
class LGApp(App):
	game = Widget()
	
	#Builder du jeu
	def build(self):
		self.game = LGGame()
		return self.game




#Lancement du jeu
if __name__ == '__main__':
    LGApp().run()
