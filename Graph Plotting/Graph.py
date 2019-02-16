from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
from kivy.uix.button import Button
import matplotlib.animation as anime
from matplotlib import style
x=[]
y=[]
for i in range(10):
    x.append(i)
    y.append(i*i)
style.use('fivethirtyeight')
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
class graph(Widget):
    def plot(self,obj):
        plt.plot(x,y)
        plt.show()
    def __init__(self):
        super(graph,self).__init__()
        btn1=Button(text="plot")
        btn1.bind(on_press=self.plot)
        self.add_widget(btn1)
        
            
class graphplot(App):
    def build(self):
        return graph()
graphplot().run()



            
            
