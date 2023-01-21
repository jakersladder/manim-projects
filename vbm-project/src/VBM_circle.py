from manim import *
import math
import numpy as np

class VBMCircle(ThreeDScene):
    def construct(self):
        circle = Circle(radius=3.03, color=BLACK).set_stroke(width=10)
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
                    number = Text(str(point_number),font_size=40).set_color(BLACK)
                else:
                    number = Text(str(i),font_size=40).set_color(BLACK)
                number.move_to(get_points(radius, point_number)[i])
                self.add(number)
        
        def make_red_lines(radius, point_number):
            doubling = [1,2,4,8,7,5]
            for i in range(0, len(doubling),1):
                line = Line(
                    start=get_points(3.0,9)[doubling[i]],
                    end=get_points(3,9)[doubling[(i+1)%6]]
                    ).set_color(RED)
                self.play(Create((line.shift(RIGHT*0.03).set_stroke(width=6))))
        
        def make_blue_lines(radius, point_number):
            doubling = [1,5,7,8,4,2]
            for i in range(0, len(doubling),1):
                line = Line(
                    start=get_points(3.0,9)[doubling[i]],
                    end=get_points(3,9)[doubling[(i+1)%6]]
                    ).set_color(BLUE)
                self.play(Create(line.shift(LEFT*0.03).set_stroke(width=6)))
        
        def make_tri_lines(radius, point_number):
            line1 = DashedLine(
                start=get_points(3.0,9)[0],
                end=get_points(3,9)[3],
                dash_length=0.05, dashed_ratio=0.5
                ).set_color(GREEN).set_stroke(width=6)
            line2 = DashedLine(
                start=get_points(3.0,9)[0],
                end=get_points(3,9)[6],
                dash_length=0.05, dashed_ratio=0.5
                ).set_color(GREEN).set_stroke(width=6)
            self.play(Create(line1), Create(line2))
                
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.camera.background_color=WHITE
        self.add_foreground_mobject(circle)
        make_nums(3.4,9)
        make_red_lines(3.0,9)
        make_blue_lines(3.0,9)
        make_tri_lines(3.0,9)
        
