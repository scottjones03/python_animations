
import numpy as np
import manim
from manim.animation.transform import ApplyFunction


HEIGHT=10
WIDTH=10
class VectorArrow(manim.MovingCameraScene):
    

    def construct_arrow(self) -> None:
        origin = np.array([0, 0, 0])
        down = manim.DOWN
        up = manim.UP
        
        dot = manim.Dot(origin)
        origin_text  = manim.Text(f"{origin[0:2]}").next_to(dot, down)

        vector = np.array([2, 2, 0])
        arrow = manim.Arrow(origin, vector, buff=0)

        tip_text = manim.Text(f"{vector[0:2] - origin[0:2]}").next_to(arrow.get_end(), up)

        numberplane = manim.NumberPlane()
        self.add(numberplane, dot, arrow, origin_text, tip_text)

        def trans_func(x) -> None:
            return x*3

        self.play(arrow.animate.apply_function(trans_func), run_time=5)

    def get_evolving_trajectory(self, mobject):
        trajectory = manim.VMobject()
        trajectory.start_new_path(mobject.get_center())
        trajectory.set_stroke(manim.color.RED, 1)

        def update_trajectory(traj):
            point = mobject.get_center()
            traj.add_smooth_curve_to(point)
        trajectory.add_updater(update_trajectory)
        return trajectory

    def get_vector_field(self, change):
        def pendulum_vector_field_func(point):
            mu=0.1
            g=9.8
            L=3
            theta, omega = point[:2]
            return np.array([
                omega,
                -np.sqrt(g / L) * np.sin(theta+change) - mu * omega+np.random.rand(),
                0,
            ])
        return manim.ArrowVectorField(pendulum_vector_field_func, y_range=[-HEIGHT, HEIGHT]), pendulum_vector_field_func
        

    def construct_field(self) -> None:
        change=0
        zoom=1
        speed = 1*zoom
        vector_fied=self.get_vector_field(change)
        self.add(vector_fied)

        options = np.linspace(-HEIGHT*zoom, HEIGHT*zoom, 10)
        xs_options, ys_options=np.meshgrid(options, options)

        for (xs, ys) in zip(xs_options, ys_options):
            for x, y in zip(xs, ys):
                end_dot=manim.Dot(point=np.array([x, y, 0]), radius=manim.DEFAULT_DOT_RADIUS/3)
                vector_fied.nudge(end_dot, speed, 1, pointwise=False)
                end_dot.add_updater(vector_fied.get_nudge_updater(pointwise=False))
                trajectory = self.get_evolving_trajectory(end_dot)
                self.add(end_dot, trajectory)

        line = manim.Arc()
        vector_fied.nudge(line)
        line.add_updater(vector_fied.get_nudge_updater(pointwise=True))
        
        for i in range(3):
            change=i
            new_vector_field = self.get_vector_field(change)
            self.play(vector_fied.animate.become(new_vector_field), subcaption_duration=10)
            

        # self.wait(1)

    def construct_stream_lines(self):
        vector_field, func = self.get_vector_field(0)
        stream_lines = manim.StreamLines(
            func, stroke_width=3, max_anchors_per_line=30
        )
        self.add(stream_lines)
        self.add(vector_field)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
        self.wait(10)

    def construct(self):
        self.camera.frame.set(width=WIDTH, height=HEIGHT)
        self.construct_stream_lines()
