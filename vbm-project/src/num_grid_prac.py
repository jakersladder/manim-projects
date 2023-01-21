from manim import *
import math
import numpy as np

class NumGridPrac(ThreeDScene):
    def construct(self):

        scale_factor = 0.7

        modulus = 9
        extent = 9

        def step_array(first_num, step_size, step_number):
            array = []
            for i in range(0, step_number, 1):
                array.append((first_num + step_size * i) % modulus)
            return array

        axis_1 = step_array(3, 2, extent)
        neg_axis_1 = step_array(3, 7, extent)

        def get_grid(axis):
            grid = []
            for x in axis:
                axis_2 = step_array(x, 4, extent)
                grid.append(axis_2)
            return grid
        
        def get_neg_grid(axis):
            grid = []
            for x in axis:
                axis_2 = step_array(x, 5, extent)
                grid.append(axis_2)
            return grid

        def nums_2D(grid):
            number_group = VGroup()
            square_group = VGroup()

            for x in range(0, extent, 1):
                for y in range(0, extent, 1):
                    num = grid[x][y]
                    if num == 0:
                        num = 9

                    number = Text(str(num), font_size = 36).set_color(BLACK).move_to([x,y,0]).rotate(PI/2)
                    square = Square(side_length = .707).set_color(BLACK).move_to([x,y,0]).rotate(PI/4)
                    
                    if num == 1 or num == 4 or num == 7:
                        square.set_fill(RED, opacity = 1.0)
                    if num == 2 or num == 5 or num == 8:
                        square.set_fill(BLUE, opacity = 1.0)
                    if num == 3 or num == 6 or num == 9:
                        square.set_fill(GREEN, opacity = 1.0)

                    number_group.add(number)
                    square_group.add(square)
            
            return number_group.move_to(ORIGIN).scale(scale_factor), square_group.move_to(ORIGIN).scale(scale_factor)

        def negative_nums_2D(grid):
            number_group = VGroup()
            square_group = VGroup()

            for x in range(0, extent-1, 1):
                for y in range(0, extent-1, 1):
                    num = grid[x][y]
                    if num == 0:
                        num = 9
                    number = Text(str(num), font_size = 36).set_color(BLACK).move_to([x,y,0]).rotate(PI/2)
                    square = Square(side_length = .707).set_color(BLACK).set_fill(WHITE, opacity= 1.0).move_to([x,y,0]).rotate(PI/4)
                    number_group.add(number)
                    square_group.add(square)
            return number_group.move_to(ORIGIN).scale(scale_factor), square_group.move_to(ORIGIN).scale(scale_factor)

        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES)
        self.camera.background_color=WHITE

        self.add(nums_2D(get_grid(axis_1))[1])
        self.add_foreground_mobjects(nums_2D(get_grid(axis_1))[0])
        self.add(negative_nums_2D(get_neg_grid(neg_axis_1))[1])
        self.add_foreground_mobjects(negative_nums_2D(get_neg_grid(neg_axis_1))[0])


        