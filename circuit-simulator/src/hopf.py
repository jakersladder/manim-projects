from manim import *
import math
import numpy as np

class Hopf(ThreeDScene):
    def construct(self):

        eta_tracker = ValueTracker(PI / 3)

        def get_4d_coords(e1,e2,eta):
            x1 = np.cos((e1+e2)/2) * np.sin(eta)
            x2 = np.sin((e1+e2)/2) * np.sin(eta)
            x3 = np.cos((e2-e1)/2) * np.cos(eta)
            x4 = np.sin((e2-e1)/2) * np.cos(eta)
            return x1, x2, x3, x4
        
        def get_3d_proj_coords(e1,e2,eta):
            x = get_4d_coords(e1,e2,eta)[0] / (1 - get_4d_coords(e1,e2,eta)[3])
            y = get_4d_coords(e1,e2,eta)[1] / (1 - get_4d_coords(e1,e2,eta)[3])
            z = get_4d_coords(e1,e2,eta)[2] / (1 - get_4d_coords(e1,e2,eta)[3])
            return x, y, z

        def get_torus_fibration(step, eta):
            fibration_group = VGroup()
            for e in range (0, step, 1):
                circle = ParametricFunction(
                    lambda t: np.array([
                        get_3d_proj_coords(PI * e / (step / 2), t, eta)[0],
                        get_3d_proj_coords(PI * e / (step / 2), t, eta)[1],
                        get_3d_proj_coords(PI * e / (step / 2), t, eta)[2]
                    ]), t_range = np.array([0, 4 * PI, 0.01])
                ).set_shade_in_3d(True)
                if e % 3 == 0:
                    circle.set_color(GREEN)
                if e % 3 == 1:
                    circle.set_color(RED)
                if e % 3 == 2:
                    circle.set_color(BLUE)
                fibration_group.add(circle)
            return fibration_group

        axes = ThreeDAxes()
        torus = always_redraw(lambda: get_torus_fibration(24, eta_tracker.get_value()))

        self.set_camera_orientation(phi=45 * DEGREES, theta=45 * DEGREES)
        self.add(axes, torus)
        self.wait()
        self.play(eta_tracker.animate.set_value(PI / 5), run_time = 2)
        self.wait()
        self.play(eta_tracker.animate.set_value(PI / 2), run_time = 2)
        self.wait()
        self.play(eta_tracker.animate.set_value(PI / 3), run_time = 2)
        self.wait()
        self.move_camera(phi = 0, theta = 0)

