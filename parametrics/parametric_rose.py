from matplotlib import cm
import matplotlib
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

    def draw_rose_3d(self, i):
        a=4
        b=1
        theta = np.linspace(0, 2*i/180*np.pi, 50)
        u, v = np.meshgrid(
            theta,
            theta,
        )
        r = np.cos(a/b*u)
        x = r*np.cos(u)
        y = r*np.sin(u)
        z = r*np.cos(v+r)

        self.ax.clear()
        self.set_theme()

        cmap3 = (matplotlib.colors.ListedColormap(['r', 'g', 'b', 'c'])
         .with_extremes(over='0.35', under='0.75'))

        self.ax.plot_surface(x, y, z, cmap=cmap3)
        self.ax.view_init(75, 35)

    def draw_rose_3d_random(self, i):
        a=12*np.sin(i*1e-2)
        theta = np.linspace(0, 1, 50)
        t, v = np.meshgrid(
            theta,
            theta,
        )
        x1 = a*t-np.sin(a*t)*np.sin(v)
        y1 = 1-np.cos(a*t)*np.sin(v)
        z1 = np.cos(v)
        # x2 = (np.sin(v*2*np.pi)+a)
        # y2 = (np.cos(v*2*np.pi)+1)
        # z2 = np.cos(t)
    

        self.ax.clear()
        self.set_theme()

        cmap3 = (matplotlib.colors.ListedColormap(['r', 'g', 'b', 'c'])
         .with_extremes(over='0.35', under='0.75'))

        self.ax.plot_surface(x1, y1, z1, cmap=cmap3)
        # self.ax.plot_surface(x2, y2, z2, cmap=cmap3)
        self.ax.view_init(90, 35)