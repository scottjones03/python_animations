from matplotlib import animation, pyplot as plt
from opencv.edge_detection import DrawEdgeDetection


if __name__=="__main__":
    drawAnimation = DrawEdgeDetection()
    drawAnimation.set_theme()
    ani_ = animation.FuncAnimation(
        drawAnimation.fig,
        drawAnimation.animation_func,
        interval=10
    )

    plt.show()