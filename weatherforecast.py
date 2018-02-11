from kivy.app import App
from kivy.uix.widget import Widget

class Weather(Widget):
	def on_touch_down(self, touch):
		print('no touching')
	def on_touch_move(self, touch):
		print(touch.profile)
	def on_touch_up(self, touch):
		print('oh yeah')
class WeatherApp(App):
	def build(self):
		return Weather()
WeatherApp().run()