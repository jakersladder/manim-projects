from manim import *
import math
import numpy as np

class NumberGrid(ThreeDScene):
    def construct(self):
        x = 5
        y = 5
        z = 5
        axes = ThreeDAxes()
        def dots_2D(): 
            dot_group = VGroup()
            num_group = VGroup()       
            for i in range(-x, x, 1):
                for j in range(-y, y, 1):
                    for k in range(-z, z):
                        dot = Dot3D([i, j, k])
                        num = (i+(j*4))%9
                        if num == 0:
                            num = 9
                        number = Text(str(num)).move_to(dot)
                        dot_group.add(dot)
                        num_group.add(number)
            return dot_group, num_group
        self.set_camera_orientation(phi=45 * DEGREES, theta=45 * DEGREES)
        self.add(axes, dots_2D()[0])