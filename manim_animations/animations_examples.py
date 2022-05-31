import manim

HEIGHT=20
WIDTH=10
class AnimationsDemos(manim.MovingCameraScene):
    def construct(self):
        self.camera.frame.set(width=WIDTH, height=HEIGHT)
        return super().construct()