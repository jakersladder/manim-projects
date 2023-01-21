from manim import *
import math
import numpy as np

class VBMTables(ThreeDScene):
    def construct(self):
        circle = Circle(radius=2.5, color=BLACK).set_stroke(width=10)
        def get_points(radius, point_number):
            points = []
            for i in range(0,point_number,1):
                x = radius * np.sin(2*PI*i/point_number)
                y = radius * np.cos(2*PI*i/point_number)
                point = [x,y,0]
                points.append(point)
            return points
                
        def make_nums(radius, point_number):
            for i in range(0,point_number,1):
                if(i == 0):
                    number = Text(str(point_number),font_size=36).set_color(BLACK)
                else:
                    number = Text(str(i),font_size=36).set_color(BLACK)
                number.move_to(get_points(radius, point_number)[i])
                self.add(number)
        
        def make_mult_lines(radius, point_number, mult, color):
            nums = VGroup()
            for n in range(0, point_number,1):
                if(((n+1)*mult)%9 == 0):
                    nums.add(Text(str(9),font_size=44).set_color(BLACK))
                else:
                    nums.add(Text(str(((n + 1) * mult) % 9),font_size=44).set_color(BLACK))
            nums.arrange(RIGHT).next_to(circle, DOWN * 3.5)
            for i in range(0, point_number,1):
                line = Line(
                    start=get_points(2.5,9)[i * mult % 9],
                    end=get_points(2.5,9)[(i * mult + mult) % 9]
                    ).set_color(color)
                self.play(Create((line.set_stroke(width=6)),rate_func=linear),FadeIn(nums[i],rate_func=linear))
        
            
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.camera.background_color=WHITE
        self.add_foreground_mobject(circle)
        make_nums(2.9,9)
        make_mult_lines(2.5,9,4,PURPLE)
        self.wait()
        
