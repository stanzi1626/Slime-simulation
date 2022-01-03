import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from slime_class import slime
from sample import sample
from trail_data import trail

time_step = 1
number_ants = 100

fig = plt.figure() 
ax = plt.axes(xlim=(0, 1000), ylim=(0, 1000)) 
line, = ax.plot([], [], 'or', markersize=1) 

colony = [slime(np.random.rand(2)*1000, np.random.uniform(-1, 1), np.random.uniform(-1, 1)) for _ in range(number_ants)]
trail = trail()

################################################################

def init():
    line.set_data([], [])
    return line,

def animate(i):

    xdata = []
    ydata = []

    temp = np.zeros((0, 3))

    for j, k in enumerate(colony):
        if i > 0:
            direction = sample(k.x_position, k.y_position, k.x_velocity, k.y_velocity, trail.data)
        else:
            direction = 0
        x_previous, y_previous = k.x_position, k.y_position
        temp = np.vstack((temp, k.trail(x_previous, y_previous)))   
        x, y = k.update(time_step, direction)
        xdata.append(x)
        ydata.append(y)

    trail.data = np.zeros((0, 3))
    trail.data = np.vstack((trail.data, temp))
   
    line.set_data(trail.data[:, 0], trail.data[:, 1])

    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, interval=1, blit=True, repeat=False)

anim.save('Slime.gif', writer=animation.PillowWriter(fps=25))
ax.set_aspect('equal', adjustable='box')
plt.show(block=True)