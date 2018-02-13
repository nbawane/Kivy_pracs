from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.listview import ListItemButton
from kivy.factory import Factory


class LocationButton(ListItemButton):
	print(dir(ListItemButton))
	'''
	list adapter is given the refereance of this class,
	class inherits LitstItemButton
	action perfromed by this vlass is defined in KV lang file
	KV file , on listviewbutton press triggers the method in root
	that is show_current_weather, which recievs text, that text is
	used as label to create the other widget. that will work as simple label widget
	doubt: how in KV lanf self.text is getting value
	ans: probably that is the text on button in list
	'''
	pass

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

	def show_addlocation_form(self):
		self.clear_widgets()
		self.add_widget(Weather())

	def show_current_weather(self,location):
		from kivy.uix.label import Label
		self.clear_widgets()
		currentweather = Factory.CurrentWeather()
		#Current weather is dynamically created class in KVland
		#so we cant directly import. We have a interface of
		# Factory which is deveoped based on factory design pattern
		currentweather.location = location	#accessing the property defined in KVlang
		self.add_widget(currentweather)

class WeatherApp(App):
	def build(self):
		return Weather()

WeatherApp().run()