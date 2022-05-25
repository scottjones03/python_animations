from re import I
from matplotlib import animation, pyplot as plt
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import numpy as np
import numpy.typing as npt

LIMITS = (-100, 100)
class DrawAnimation:
    def __init__(self) -> None:
        self.fig:Figure=plt.figure(figsize=(20,6))
        self.ax=self.fig.add_subplot(111,projection=Axes3D.name)
        self.fig.subplots_adjust(top=1.1, bottom=-0.1)

    
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
        width=40
        r=80+width*np.cos(i*speed)
        theta=np.linspace(-np.pi, np.pi, 20)
        u, v = np.meshgrid(
            theta,
            theta,
        )
        x = r*np.cos(u)*np.sin(v)-2*np.sin(i*speed)*r
        y = r*np.sin(u)*np.sin(v)+2*np.sin(i*speed)*r
        z = r*np.cos(v)+2*np.cos(i*speed)*r
        self.ax.clear()
        self.set_theme()

        self.ax.plot_surface(x, y, z, cmap='viridis')
        self.ax.plot_surface(y, x, z, cmap='viridis')
        self.ax.plot_surface(y, x, np.sin(i*speed)*z, cmap='viridis')
        self.ax.plot_surface(x, y, np.sin(i*speed)*z, cmap='viridis')
    
        self.ax.set_xlim(*LIMITS)
        self.ax.set_xlim(*LIMITS)
        self.ax.set_xlim(*LIMITS)
   

        
        

drawAnimation = DrawAnimation()
drawAnimation.set_theme()
ani_ = animation.FuncAnimation(
    drawAnimation.fig,
    drawAnimation.animation_func,
    interval=100
)

plt.show()



