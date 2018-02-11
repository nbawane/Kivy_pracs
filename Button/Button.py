from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Weather(BoxLayout):
	search_input = ObjectProperty()
	#this will act as the property of text input
	#all the functions of textinput now can be accessed with
	#this property. search_input is assigned the id of textinput.
	#so id of textinput has property. In KV lang file, that
	# property is assigned to search_input var, that search_input
	# can now be accessed in python code with ObjecgProperty and in
	# this way functionality of textinput can be acccessed in python
	# with the help of search_input
	def search_loc(self):
		#this the event handeler on search button press
		print('lololololo : %s'%self.search_input.text)


class WeatherApp(App):
	def build(self):
		return Weather()

WeatherApp().run()