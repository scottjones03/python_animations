# First import everthing you need
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

# Create some random data, I took this piece from here:
# http://matplotlib.org/mpl_examples/mplot3d/scatter3d_demo.py
def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin
n = 100
xx = randrange(n, 23, 32)
yy = randrange(n, 0, 100)
zz = randrange(n, -50, -25)

# Create a figure and a 3D Axes
fig = plt.figure()
ax = Axes3D(fig)

# Create an init function and the animate functions.
# Both are explained in the tutorial. Since we are changing
# the the elevation and azimuth and no objects are really
# changed on the plot we don't have to return anything from
# the init and animate function. (return value is explained
# in the tutorial.
def init():
    ax.scatter(xx, yy, zz, marker='o', s=20, c="goldenrod", alpha=0.6)
    return fig,

def animate(i):
    ax.view_init(elev=10., azim=i)
    return fig,

# Animate
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=360, interval=20, blit=True)

plt.show()


from scipy.stats import multivariate_normal

mu_x=0
variance_x=3
mu_y=0
variance_y=15

def animation_func(i) -> None:
    speed=1e-2
    width=100
    ani = np.linspace(
        -width*(np.sin((i+1)*speed))**4,
        +width*(np.sin((i+1)*speed))**4,
        10,
    )
    x, y= np.meshgrid(ani, ani)
    pos = np.empty(x.shape+(2,))
    pos[:, :, 0] =x
    pos[:,:,1]=y
    z = multivariate_normal(
        [mu_x, mu_y], 
        [[variance_x, 0], [0, variance_y]]
    ).pdf(pos)
    ax.clear()
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.contour(x, y, z, 50, cmap="binary")
    ax.view_init(60, 35)

LIMITS  = (-50, 50)
fig=plt.figure()
ax=fig.add_subplot(111, projection="3d")
plt.xlim(*LIMITS)
plt.ylim(*LIMITS)

ani_ = animation.FuncAnimation(
    fig,
    animation_func,
    interval=100
)

plt.show()



def animation_func(i):
    speed=1e-2
    width=500
    ani=width*(np.sin(speed*i))**3
    resolution=max(10, int(i))
    render=np.linspace(-ani, ani, resolution)
    func_=lambda x, y: np.sin((x**2+y**2)**(1/4))
    x, y=np.meshgrid(render, render)
    z=np.array([func_(px, py) for px, py in zip(x, y)])

    ax.clear()
    ax.view_init(60, 35)
    ax.plot_surface(x, y, z, cmap='viridis')

fig=plt.figure()
ax=plt.axes(projection="3d")

animation.FuncAnimation(
    fig,
    animation_func,
    interal=100
)
plt.show()