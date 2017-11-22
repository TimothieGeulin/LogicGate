import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


class PongPaddle(Widget):
    score = NumericProperty(0)


class PongGame(Widget):
    player1 = ObjectProperty(None)

    def on_touch_move(self, touch):
        if (touch.x > self.player1.x) & (touch.y > self.player1.y) & (touch.x < self.player1.x + self.player1.size[0]) & (touch.y < self.player1.y + self.player1.size[1]):
            self.player1.center_y = touch.y
            self.player1.center_x = touch.x

class PongApp(App):
    def build(self):
        game = PongGame()
        return game


if __name__ == '__main__':
    PongApp().run()
