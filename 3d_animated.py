from matplotlib import animation, pyplot as plt
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import numpy as np
import numpy.typing as npt

LIMITS = (-50, 50)
class DrawAnimation:
    def __init__(self) -> None:
        self.fig:Figure=plt.figure(figsize=(20,6))
        self.ax=self.fig.add_subplot(111,projection=Axes3D.name)
        self.fig.subplots_adjust(top=1.1, bottom=-0.1)
        self.func_=lambda x, y: x*y**3-y*x**3

    
    def set_theme(self) -> None:
        self.fig.patch.set_facecolor('black')
        self.ax.set_facecolor('black')
        self.ax.get_yaxis().set_visible(False)
        self.ax.get_xaxis().set_visible(False)
        self.ax.set_axis_off()

    def get_color(self) -> npt.NDArray[np.float_]:
        return np.random.random(4)

    def animation_func(self, i) -> None:
        speed=1e-2
        width=100
        ani=width*np.sin(i*speed)**4
        render=np.linspace(-ani, ani, 10)
        x, y = np.meshgrid(render, render)
        pos = np.empty(x.shape + (2,))
        pos[:, :, 0] = x; pos[:, :, 1] = y
        z=np.array([self.func_(px, py) for px, py in zip(x, y)])
        self.ax.clear()
        self.set_theme()
        self.ax.contour(x, y, z, 50, cmap='binary')
        self.ax.view_init(60, 35)
        self.ax.plot_surface(x, y, z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
        plt.xlim(*LIMITS)
        plt.ylim(*LIMITS)

drawAnimation = DrawAnimation()
drawAnimation.set_theme()
ani_ = animation.FuncAnimation(
    drawAnimation.fig,
    drawAnimation.animation_func,
    interval=100
)

plt.show()