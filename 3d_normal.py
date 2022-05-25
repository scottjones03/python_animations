from matplotlib import animation, pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import numpy as np
import numpy.typing as npt
from scipy.stats import multivariate_normal

LIMITS = (-10, 10)
class DrawAnimation:
    def __init__(self) -> None:
        self.fig:Figure=plt.figure(figsize=(15,10))
        self.ax=self.fig.add_subplot(111,projection="3d")
        self.fig.subplots_adjust(top=1.1, bottom=-0.1)
      
        #Parameters to set
        mu_x = 0
        variance_x = 3

        mu_y = 0
        variance_y = 15

        self.func_ = multivariate_normal([mu_x, mu_y], [[variance_x, 0], [0, variance_y]])

    
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
        ani=np.linspace(-width*(np.sin((i+1)*speed))**4, width*(np.sin((i+1)*speed))**4, 10)
        x, y = np.meshgrid(ani, ani)
        pos = np.empty(x.shape + (2,))
        pos[:, :, 0] = x; pos[:, :, 1] = y
        z=self.func_.pdf(pos)
        self.ax.clear()
        self.set_theme()
        self.ax.plot_surface(x, y, z ,cmap='viridis',rstride=1, cstride=1, edgecolor='blue')
        self.ax.contour(x, y, z, 50, cmap='binary')
        self.ax.view_init(60, 35)
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