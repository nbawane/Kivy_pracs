from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class MyGridLayout(GridLayout):
	pass

class LayoutApp(App):
	def build(self):
		return MyGridLayout()

LayoutApp().run()