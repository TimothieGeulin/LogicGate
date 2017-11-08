from time import time
from kivy.app import App
from os.path import dirname, join
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ListProperty
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen

class GameScreen(Screen):
    fullscreen = BooleanProperty(False)

    def add_widget(self, *args):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args)
        return super(GameScreen, self).add_widget(*args)

class LogicGateApp(App):
	
	index = NumericProperty(-1)
	current_title = StringProperty()
	time = NumericProperty(0)
	show_sourcecode = BooleanProperty(False)
	sourcecode = StringProperty()
	screen_names = ListProperty([])
	hierarchy = ListProperty([])
    
	def build(self):
		self.title = 'Logic Gate'
		Clock.schedule_interval(self._update_clock, 1 / 60.)
		self.screens = {}
		self.available_screens = (['MainMenu', 'LevelSelect', 'Level1'])
		self.screen_names = self.available_screens
		curdir = dirname(__file__)
		self.available_screens = [join(curdir, 'data', 'screens',
			'{}.kv'.format(fn).lower()) for fn in self.available_screens]
		self.go_mainmenu()
	"""	
	def go_previous_screen(self):
		self.index = (self.index - 1) % len(self.available_screens)
		screen = self.load_screen(self.index)
		sm = self.root.ids.sm
		sm.switch_to(screen, direction='right')
		self.current_title = screen.name
		#self.update_sourcecode()
	
	def go_next_screen(self):
		self.index = (self.index + 1) % len(self.available_screens)
		screen = self.load_screen(self.index)
		sm = self.root.ids.sm
		sm.switch_to(screen, direction='left')
		self.current_title = screen.name
		#self.update_sourcecode()
		"""
		
	def go_mainmenu(self):
		self.index = 0 % len(self.available_screens)
		screen = self.load_screen(self.index)
		sm = self.root.ids.sm
		sm.switch_to(screen, direction='right')
		self.current_title = screen.name
	
	def go_levelselect(self):
		if(self.index!=0): 
			side = 'up'
		else: 
			side = 'left'
		self.index = 1 % len(self.available_screens)
		screen = self.load_screen(self.index)
		sm = self.root.ids.sm
		sm.switch_to(screen, direction = side)
		self.current_title = screen.name
		
	def go_level1(self):
		self.index = 2 % len(self.available_screens)
		screen = self.load_screen(self.index)
		sm = self.root.ids.sm
		sm.switch_to(screen, direction='down')
		self.current_title = screen.name
		
	def load_screen(self, index):
		if index in self.screens:
			return self.screens[index]
		screen = Builder.load_file(self.available_screens[index])
		self.screens[index] = screen
		return screen
		
	def _update_clock(self, dt):
		self.time = time()
 
LogicGateApp().run()
