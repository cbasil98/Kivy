from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
class widgets(Widget):
    pass

class Program(App):
    def build(self):
        return widgets()
Program().run()
