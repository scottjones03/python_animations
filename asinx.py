







from matplotlib import animation, pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import numpy as np
import numpy.typing as npt

LIMITS = (-10, 10)
class DrawAnimation:
    def __init__(self) -> None:
        self.fig:Figure=plt.figure(figsize=(20,6))
        self.ax: Axes=plt.axes()
        self.x = np.array([])
        self.y = np.array([])
        self.func_=lambda x: np.random.randint(*LIMITS)*np.sin(LIMITS[1]*x)

    
    def set_theme(self) -> None:
        self.fig.patch.set_facecolor('black')
        self.ax.set_facecolor('black')
        self.ax.get_yaxis().set_visible(False)
        self.ax.get_xaxis().set_visible(False)

    def get_color(self) -> npt.NDArray[np.float_]:
        return np.random.random(4)

    def animation_func(self, i) -> None:
        self.x=np.sort(
            np.append(self.x, np.linspace(*LIMITS, 1000))
        )
        self.y=self.func_(self.x)
        plt.plot(self.x, self.y, c=(tuple(self.get_color())))
        plt.xlim(*LIMITS)
        plt.ylim(*LIMITS)

drawAnimation = DrawAnimation()
drawAnimation.set_theme()
ani_ = animation.FuncAnimation(
    drawAnimation.fig,
    drawAnimation.animation_func,
    interval=300
)

plt.show()