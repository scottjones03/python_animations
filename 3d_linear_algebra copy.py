from re import I
from matplotlib import animation, pyplot as plt
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import numpy as np
import numpy.typing as npt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import proj3d

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
        speed=1e-1
        width=100
        r=width*np.sin(i*speed)**2
        theta=np.linspace(-np.pi, np.pi, 20)
        us, vs = np.meshgrid(
            theta,
            theta,
        )
        
        zlines= [np.cos(v) for v in vs]
        xlines = [np.cos(u)*np.sin(v) for u, v in zip(us, vs)]
        ylines = [np.sin(u)*np.sin(v) for u, v in zip(us, vs)]
        sigma = i*speed
        expansion = r * np.array([[1, 0, 0], [0, 1, 0], [0, 0 , 1]])
        transformxy = np.array([
            [np.cos(sigma), -np.sin(sigma), 0],
            [np.sin(sigma), np.cos(sigma), 0],
            [0, 0, 1]
        ])
        transformxz = np.array([
            [np.cos(sigma), 0, np.sin(sigma)],
            [0, 1, 0],
            [-np.sin(sigma), 0, np.cos(sigma)]
        ])
        transformyz = np.array([
            [1, 0, 0],
            [0, np.cos(sigma), -np.sin(sigma)],
            [0, np.sin(sigma), np.cos(sigma)],
        ])
        self.ax.clear()
        self.set_theme()
        for xline, yline, zline in zip(xlines, ylines, zlines):
            lines = np.array([xline, yline, zline])
            transformedyz_lines = np.matmul(transformyz,lines)
            scaledxy_lines = np.matmul(expansion, transformedyz_lines)
            if i>20:
                transformedxz_lines = np.matmul(transformxz,lines)
                self.ax.plot3D(*transformedxz_lines, color="b")
            elif i>100:
                self.ax.plot3D(*transformedyz_lines, color="r")
            
            self.ax.plot3D(*scaledxy_lines, color="g")

        self.ax.set_xlim(*LIMITS)
        self.ax.set_xlim(*LIMITS)
        self.ax.set_xlim(*LIMITS)
   

        
        

drawAnimation = DrawAnimation()
# drawAnimation.set_theme()
ani_ = animation.FuncAnimation(
    drawAnimation.fig,
    drawAnimation.animation_func,
    interval=100
)

plt.show()



