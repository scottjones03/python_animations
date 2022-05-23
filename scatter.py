from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np
  
x = []
y = []
colors = []
fig = plt.figure(figsize=(5,5))
ax=plt.axes()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)

def animation_func(i):
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))
    colors.append(np.random.rand(1))
    area = random.randint(0,30) * random.randint(0,30)
    plt.xlim(0,50)
    plt.ylim(0,50)
    plt.scatter(x, y, c = colors, s = area, alpha = 0.2)
  
animation = FuncAnimation(fig, animation_func, interval = 10)
plt.show()


x=random.randint(0, 100)
y=random.randint(0, 100)
color=np.random.rand(1)
area=random.randint(0,30)*random.randint(0, 30)

plt.xlim(0, 50)
plt.ylim(0, 50)
plt.scatter(x, y ,c=color, s=area, alpha=0.2)

plt.show()