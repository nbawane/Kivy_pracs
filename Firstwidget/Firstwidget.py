from kivy.app import App
from kivy.uix.widget import Widget


class WidgetOne(Widget):
	pass


class WidgetOneApp(App):
	def build(self):
		return WidgetOne()


if __name__ == "__main__":
	WidgetOneApp().run()