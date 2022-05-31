from matplotlib import animation, pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import numpy as np
import numpy.typing as npt

LIMITS = (-100, 100)
class DrawAnimation:
    def __init__(self) -> None:
        self.fig:Figure=plt.figure(figsize=(5,6))
        self.ax: Axes=plt.subplot(121)
        self.ax2: Axes = plt.subplot(122)

    
    def set_theme(self) -> None:
        self.fig.patch.set_facecolor('black')
        self.ax.set_facecolor('black')
        self.ax.get_yaxis().set_visible(False)
        self.ax.get_xaxis().set_visible(False)
        self.ax.set_axis_off()
        self.ax2.set_facecolor('black')
        self.ax2.get_yaxis().set_visible(False)
        self.ax2.get_xaxis().set_visible(False)
        self.ax2.set_axis_off()

    def get_color(self) -> npt.NDArray[np.float_]:
        return np.random.random(4)
