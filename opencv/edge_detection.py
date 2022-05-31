from pathlib import Path
import numpy as np
import cv2 as cv
from matplotlib import cm, pyplot as plt
import re

from opencv import DrawAnimation

class DrawEdgeDetection(DrawAnimation):
    def animation_func(self, i) -> None:
        folder=Path(r"/Users/scottjones_admin/Library/Mobile Documents/com~apple~CloudDocs/Mac files/Repos/python_animations/opencv/messi/")
        images=sorted([{"idx": int(re.findall(r"[0-9]+", str(image))[0]), "img": image} for image in folder.glob("*.jpeg")], key=lambda d: d["idx"])
        speed=1e-1
        width=50
        l1=width*(np.sin(speed*i))+50
        l2=width*(np.sin(speed*i))+200
        frame_rate=0.5
        frame_idx=int((i*frame_rate)%len(images))
        img = cv.imread(str(images[frame_idx]["img"]),0)
        edges = cv.Canny(img,100, 200)

        self.set_theme()
        self.ax.clear()
        self.ax2.clear()

        self.ax.imshow(edges,cmap = cm.jet)
        self.ax2.imshow(img)

        