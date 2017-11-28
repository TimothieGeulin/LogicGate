import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, BooleanProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Gate(Widget):
    selected = BooleanProperty(0)
    outx = NumericProperty(0)
    outy = NumericProperty(0)
    
#class Wire(Widget):
#	sourceGate = Gate()
#	targetGate = Gate()
#
#	def __init__(self, SG, TG):
#		self.sourceGate = SG
#		self.targetGate = TG
    
class LGGame(Widget):
	gateList = []
	#wiring = False


	def on_touch_move(self, touch):
		gate_grab = False
		
		#for gate in self.gateList:
		#	if(touch.x > gate.x+180) & (touch.y > gate.y+80) & (touch.x < gate.x+180 + gate.outSize[0]) & (touch.y < gate.y+80 + gate.outSize[1]):
		#		self.wiring = True
		#		new_wire(self, gate)
		#		return
		
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
					
					            
	def new_gate(self):
		gate = Gate()
		self.add_widget(gate)
		self.gateList.append(gate)
		
	#def new_wire(self, SG, TG):
	#	wire = Wire(self,SG,TG)
	#	self.add_widget(wire)
	#	self.wireList.append(wire)
	

class LGApp(App):
	game = Widget()
	def build(self):
		self.game = LGGame()
		return self.game


if __name__ == '__main__':
    LGApp().run()
