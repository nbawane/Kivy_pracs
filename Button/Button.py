from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Weather(BoxLayout):
	def search_loc(self):
		print('lololololo')


class WeatherApp(App):
	def build(self):
		return Weather()

WeatherApp().run()