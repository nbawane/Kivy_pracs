import kivy

from kivy.app import App
from kivy.uix.button import Label

class FirstOne(App):

	def build(self):
		return Label()

if __name__ == "__main__":
	FirstOne().run()