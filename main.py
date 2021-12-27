import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from slime_class import slime

time_step = 1
number_ants = 1

fig = plt.figure()
ax = plt.axes(xlim=(0, 1000), ylim=(0, 1000))

patches = []
for i in range(number_ants):
    patches.append(plt.Circle((0, 0), radius=5, fill = True, color = 'red'))
colony = [slime(np.random.rand(2)*1000, np.random.uniform(-1, 1), np.random.uniform(-1, 1)) for _ in range(number_ants)]

################################################################

def init():
    for i in range(len(patches)):
        patches[i].center = (0, 0)
        ax.add_patch(patches[i])
    
    return patches

def animate(i):
    for j, k in enumerate(patches):
        (a, b) = (colony[j].update(time_step))
        print(colony[j].trail())
        k.center = (a, b)

    return patches

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=4000, interval=1, blit=True, repeat=False)

'''anim.save('Slime.gif', writer=animation.PillowWriter(fps=25))'''
ax.set_aspect('equal', adjustable='box')
plt.show(block=True)