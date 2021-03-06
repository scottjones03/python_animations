from matplotlib import animation, pyplot as plt
from parametrics.parametric_rose import DrawRose
from parametrics.parametric_tube import TubeAnimation


if __name__ == "__main__":
    drawAnimation = TubeAnimation()
    drawAnimation.set_theme()
    ani_ = animation.FuncAnimation(
        drawAnimation.fig,
        drawAnimation.animation_func_tube,
        interval=100
    )

    plt.show()