
import matplotlib.pyplot as plt
import matplotlib.animation as anime
from matplotlib import style


x=[]
y=[]
for i in range(10):
    x.append(0)
    y.append(0)
style.use('fivethirtyeight')
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
def animate(i):
    
    for j in range(10):
        x[j]=j
        y[j]=j*j
    ax1.clear()
    ax1.plot(x,y)
print(x,y) 
ani=anime.FuncAnimation(fig,animate,interval=1000)
plt.show()

