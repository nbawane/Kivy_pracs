from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

class ComicCreator(AnchorLayout):
	pass


class ComicCreatorApp(App):
	def build(self):
		return ComicCreator()


ComicCreatorApp().run()