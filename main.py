import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from slime_class import slime

time_step = 1
number_ants = 5

fig = plt.figure() 
ax = plt.axes(xlim=(0, 1000), ylim=(0, 1000)) 
line, = ax.plot([], [], 'ro',lw=2) 

colony = [slime(np.random.rand(2)*1000, np.random.uniform(-1, 1), np.random.uniform(-1, 1)) for _ in range(number_ants)]

################################################################

def init():
    line.set_data([], [])
    return line,

def animate(i):
    xdata = []
    ydata = []
    for j, k in enumerate(colony):
        x, y = k.update(time_step)
        k.trail() 
        xdata.append(x)
        ydata.append(y)  
    
    line.set_data(xdata, ydata)

    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=4000, interval=1, blit=True, repeat=False)

'''anim.save('Slime.gif', writer=animation.PillowWriter(fps=25))'''
ax.set_aspect('equal', adjustable='box')
plt.show(block=True)