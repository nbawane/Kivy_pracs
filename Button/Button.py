from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest



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
	import kivy.adapters.listadapter
	search_result = ObjectProperty()
	#property for listview
	def search_loc(self):
		weatherAPI = 'http://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'
		#this the event handeler on search button press
		cityname = self.search_input.text
		weatherAPI = weatherAPI.format(cityname)
		request = UrlRequest(weatherAPI,self.found_location)
		#above is the specific request api from kivy which collects data and
		#pass it to function objeect with request and decoded json data.
		#we need to decode json data

	def found_location(self,request, data):
		cities = ["{} temp ({})F".format(data['name'], data['main']['temp'])]
		print('\n'.join(cities))
		templist = ['Nagpur 30C','Mumbai 28C','Pune 23C']
		# self.search_result.item_strings = cities
		#search_result is the property defined for
		# listview. using the property we are assigning the
		#  cities list to item_strings, which holds the list
		# to display list contednt
		cities.extend(templist)
		self.search_result.adapter.data.clear()
		#data here is a list,clear clears the list so it doesnt creat the stack of replicated data
		#disable the clear see fr yrself
		self.search_result.adapter.data.extend(cities)


class WeatherApp(App):
	def build(self):
		return Weather()

WeatherApp().run()