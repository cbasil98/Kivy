from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
class username(GridLayout):
    def __init__(self,**kwargs):
        super(username,self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text="username"))
        self.user=TextInput()
        self.add_widget(self.user)
        self.add_widget(Label(text="Password"))
        self.password=TextInput(password=True)
        self.add_widget(self.password)
class _2ndprogram(App):
    def build(self):
        return username()
_2ndprogram().run()
