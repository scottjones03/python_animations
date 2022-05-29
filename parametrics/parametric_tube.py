
from matplotlib import animation, pyplot as plt
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import numpy as np
import numpy.typing as npt

from parametrics import DrawAnimation


LIMITS = (-100, 100)

class TubeAnimation(DrawAnimation):
    def animation_func_many(self, i) -> None:
        speed=1e-2
        width=5
        r=width*np.sin(i*speed)**2
        theta=np.linspace(-np.pi, np.pi, 20)
        us, vs = np.meshgrid(
                theta,
                r**2*theta,
        )
        
        ring_radius=3*r
        helix_radius=r
        a = r

        self.ax.clear()
        self.set_theme()

        x = helix_radius*vs + ring_radius*a*np.sin(us)/np.sqrt(ring_radius**2+helix_radius**2)
        y = ring_radius*np.cos(vs) - a*np.cos(vs)*np.cos(us) + helix_radius*a*np.sin(vs)*np.sin(us)/np.sqrt(ring_radius**2+helix_radius**2)
        z = ring_radius*np.sin(vs) - a*np.sin(vs)*np.cos(us) - helix_radius*a*np.cos(vs)*np.sin(us)/np.sqrt(ring_radius**2+helix_radius**2)

        self.ax.plot_surface(x, z, y, cmap="viridis")

        
        
        self.ax.view_init(90, 45)
        self.ax.set_xlim(*LIMITS)
        self.ax.set_xlim(*LIMITS)
        self.ax.set_xlim(*LIMITS)

    def animation_func_surface(self, i) -> None:
        speed=1e-2
        width=50
        r=width*np.cos(i*speed)**2
        theta=np.linspace(-np.pi, np.pi, 20)
        u, v = np.meshgrid(
            theta,
            theta,
        )
        ring_radius=2*r
        helix_radius=r
        x = np.cos(v) * (ring_radius+helix_radius*np.cos(u))
        y = np.sin(v) * (ring_radius+helix_radius*np.cos(u))
        z = helix_radius * np.sin(u)
        

        self.ax.clear()
        self.set_theme()

        self.ax.plot_surface(x, y, z, cmap='viridis')
        self.ax.view_init(45+i, 35)
        self.ax.set_xlim(*LIMITS)
        self.ax.set_xlim(*LIMITS)
        self.ax.set_xlim(*LIMITS)

    def animation_func_lines(self, i) -> None:
        speed=5e-2
        width=100
        r=width*np.sin(i*speed)**2
        theta=np.linspace(-np.pi, np.pi, 20)
        us, vs = np.meshgrid(
            theta,
            theta,
        )
        ring_radius=40
        helix_radius=5
        xlines = [np.cos(v) * (ring_radius+helix_radius*np.cos(u)) for u, v in zip(us, vs)]
        ylines = [np.sin(v) * (ring_radius+helix_radius*np.cos(u)) for u, v in zip(us, vs)]
        zlines = [helix_radius * np.sin(u) for u in us]
        sigma = 10*speed*i
        transformxy = np.array([
            [np.cos(sigma), -np.sin(sigma), 0],
            [np.sin(sigma), np.cos(sigma), 0],
            [0, 0, 1]
        ])
        sigma=np.pi/2
        transformxz = np.array([
            [np.cos(sigma), 0, np.sin(sigma)],
            [0, 1, 0],
            [-np.sin(sigma), 0, np.cos(sigma)]
        ])
        self.ax.clear()
        self.set_theme()
        for xline, yline, zline in zip(xlines, ylines, zlines):
            lines1 = np.array([xline, yline, zline])
            tlines1 = np.matmul(transformxy, lines1)
            tlines2 = np.matmul(transformxz, tlines1)
            tlines3 = np.array([tlines2[0]-r, tlines2[1], tlines2[2]])
            tlines4 = np.array([tlines2[0]+r, tlines2[1], tlines2[2]])
            self.ax.plot3D(*tlines2, color="r")
            self.ax.plot3D(*tlines3, color="g")
            self.ax.plot3D(*tlines4, color="y")

        self.ax.view_init(15*i, 75)

        self.ax.set_xlim(*LIMITS)
        self.ax.set_xlim(*LIMITS)
        self.ax.set_xlim(*LIMITS)
   

        
        





