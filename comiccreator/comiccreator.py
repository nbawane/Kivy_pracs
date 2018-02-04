from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang.builder import Builder


Builder.load_file('tools.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('controls.kv')


class ComicCreator(AnchorLayout):
	pass


class ComicCreatorApp(App):
	def build(self):
		return ComicCreator()


ComicCreatorApp().run()