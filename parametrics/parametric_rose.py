import numpy as np
from parametrics import DrawAnimation

class DrawRose(DrawAnimation):
    def draw_rose_2d(self, i):
        speed=1e-1
        a=float(np.sin(i*speed)*5+1)
        b=float(np.cos(i*speed)*5+1)
        theta = np.linspace(-np.pi, np.pi, 50)
        u, v = np.meshgrid(
            theta,
            theta,
        )
        r = np.cos(a/b*u)
        x = r*np.cos(u)*np.sin(v)
        y = r*np.sin(u)*np.sin(v)
        z = r*np.cos(v)

        self.ax.clear()
        self.set_theme()

        self.ax.plot_surface(x, y, z, cmap='viridis')
        self.ax.view_init(80, 35)