import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, BooleanProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Gate(Widget):
    selected = BooleanProperty(0)
    
    
class LGGame(Widget):
    gateList = []

    def on_touch_move(self, touch):
		for gate in self.gateList:
			if (touch.x > gate.x) & (touch.y > gate.y) & (touch.x < gate.x + gate.size[0]) & (touch.y < gate.y + gate.size[1]):
				gate.center_y = touch.y
				gate.center_x = touch.x
				break
            
    def new_gate(self):
		gate = Gate()
		self.add_widget(gate)
		self.gateList.append(gate)
		
	def cycle(my_list, start_at=None):
		start_at = 0 if start_at is None else my_list.index(start_at)
		while True:
			yield my_list[start_at]
			start_at = (start_at + 1) % len(my_list)
		

class LGApp(App):
	game = Widget()
	def build(self):
		self.game = LGGame()
		return self.game


if __name__ == '__main__':
    LGApp().run()
