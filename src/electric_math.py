from manim import *
import math
import numpy as np
from math_equations import * 

class ElectricMath(Scene):
    def construct(self):

        #---Construcing Circuit Diagram-----------------------------------------------------------------------------
       
        # Assign SVG
        circuit = SVGMobject("src/assets/circuit-20220323-1531.svg")
        circuit2 = SVGMobject("src/assets/circuit2.svg")

        # Define Shapes
        ellipse_1 = Ellipse(width=2.0, height=4.0, color=GREEN).set_fill(GREEN, opacity=0.5)
        ellipse_2 = Ellipse(width=2.0, height=4.0, color=GREEN).set_fill(GREEN, opacity=0.5)
        torus_1 = Group(ellipse_1,ellipse_2).arrange(buff=.1).scale(0.4).next_to(circuit, LEFT)
        rect_1 = Rectangle(width=0.9, height=0.25).set_stroke(color=PURPLE).set_fill(PURPLE, opacity = 0.5)
        star_1 = Star(16, outer_radius=2, density=6, color=RED).scale(0.5).stretch_to_fit_height(1.2).set_fill(RED, opacity = 0.5)

        # Assign and arrange shapes
        magnetic_field = torus_1.next_to(circuit, LEFT)
        dielectric_field = rect_1.next_to(circuit, RIGHT + 1.8 * RIGHT)
        resistive_loss = star_1.next_to(circuit, UP + UP)

        circuit_diagram = Group(circuit.scale(4), magnetic_field, dielectric_field, resistive_loss).scale(0.75).shift(2*DOWN)
        circuit_diagram_2 = Group(circuit2.scale(3), magnetic_field, dielectric_field, resistive_loss)

        #---Circuit Diagram------------------------------------------------------------------------------------------
        
        slide_title = Text("Electric Harmonic Oscillator", font_size=48).to_edge(UP, buff=0.5).set_color(BLUE)
        electric_title = Text("Resonant Electric Circuit", font_size=32).next_to(slide_title,DOWN)

        # Opening to Scene
        self.add(slide_title)
        self.wait()
        self.play(Write(electric_title))
        self.wait()
        self.play(Write(electric_eqs[1].next_to(electric_title,DOWN,buff=0.5)))
        self.wait()
        self.bring_to_back(circuit)
        self.play(FadeIn(circuit))
        self.wait()
        self.play(ReplacementTransform(electric_eqs[1],electric_eqs[2].next_to(electric_title,DOWN,buff=0.5)))
        self.wait()
        self.play(ReplacementTransform(electric_eqs[2],electric_eqs[3].next_to(electric_title,DOWN,buff=0.5)))
        self.wait()
        self.play(ReplacementTransform(electric_eqs[3],electric_eqs[4].next_to(electric_title,DOWN,buff=0.5)))
        self.wait()
        
        # Introduce RLC 
        electric_eqs[5].set_color_by_tex("L", GREEN).set_color_by_tex("C", PURPLE).set_color_by_tex("R", RED)
        self.play(FadeOut(electric_eqs[4]),FadeIn(electric_eqs[5].next_to(electric_title,DOWN,buff=0.5)))
        self.wait()
        l = electric_eqs[5][1].copy()
        c = electric_eqs[5][7].copy()
        r = electric_eqs[5][4].copy()

        self.play(Indicate(l))
        self.wait()
        self.play(FadeIn(magnetic_field),l.animate.next_to(magnetic_field,LEFT))
        self.wait()
        self.play(FadeOut(magnetic_field), l.animate.shift(0.5*RIGHT))
        self.wait()

        self.play(Indicate(c))
        self.wait()
        self.play(FadeIn(dielectric_field),c.animate.next_to(dielectric_field,RIGHT))
        self.wait()
        self.play(FadeOut(dielectric_field), c.animate.shift(0.1*LEFT))
        self.wait()

        self.play(Indicate(r))
        self.wait()
        self.play(FadeIn(resistive_loss),r.animate.next_to(resistive_loss,DOWN))
        self.wait()
        self.play(FadeOut(resistive_loss), r.animate.shift(0.3*UP))
        self.wait()

        # Continue with math
        electric_eqs[6].set_color_by_tex("L", GREEN).set_color_by_tex("C", PURPLE).set_color_by_tex("R", RED)
        self.play(ReplacementTransform(electric_eqs[5],electric_eqs[6].next_to(electric_title,DOWN,buff=0.5)))
        self.wait()
        electric_eqs[7].set_color_by_tex("L", GREEN).set_color_by_tex("C", PURPLE).set_color_by_tex("R", RED)
        self.play(ReplacementTransform(electric_eqs[6],electric_eqs[7].next_to(electric_title,DOWN,buff=0.5),runtime=2))
        self.wait()
        electric_eqs[8].set_color_by_tex("L", GREEN).set_color_by_tex("C", PURPLE).set_color_by_tex("R", RED)
        self.play(ReplacementTransform(electric_eqs[7],electric_eqs[8].next_to(electric_title,DOWN,buff=0.5)))
        self.wait()

        self.bring_to_back(circuit2)
        self.play(
            FadeOut(circuit,r),FadeIn(circuit2.move_to(circuit))
        )
        self.wait()
        electric_eqs[9].set_color_by_tex("L", GREEN).set_color_by_tex("C", PURPLE).set_color_by_tex("R", RED)
        self.play(
            TransformMatchingTex(
                electric_eqs[8],electric_eqs[9].next_to(electric_title,DOWN,buff=0.5)
            )
        )
        self.wait()
        electric_eqs[10].set_color_by_tex("L", GREEN).set_color_by_tex("C", PURPLE).set_color_by_tex("R", RED)
        self.play(
            TransformMatchingTex(electric_eqs[9],electric_eqs[10].next_to(electric_title,DOWN,buff=0.5))
        )
        self.wait()
        electric_res_eqs[0].set_color_by_tex("L", GREEN).set_color_by_tex("C", PURPLE)
        self.play(
            FadeIn(electric_res_eqs[0].scale(0.75).next_to(electric_eqs[10],DOWN))
        )
        self.wait()
        electric_res_eqs[1].set_color_by_tex("L", GREEN).set_color_by_tex("C", PURPLE)
        self.play(ReplacementTransform(electric_res_eqs[0],electric_res_eqs[1].scale(0.75).next_to(electric_eqs[10],DOWN)))
        self.wait()
        electric_eqs[11].set_color_by_tex("L", GREEN).set_color_by_tex("C", PURPLE).set_color_by_tex("R", RED)
        self.play(TransformMatchingTex(electric_eqs[10],electric_eqs[11].next_to(electric_title,DOWN,buff=0.5)))
        self.wait()
        self.play(FadeOut(electric_res_eqs[0],electric_res_eqs[1]))
        self.wait()
        self.play(TransformMatchingTex(electric_eqs[11],electric_eqs[12].next_to(electric_title,DOWN,buff=1.0)))
        self.wait()
        self.bring_to_front(electric_eqs[12])
        self.play(FadeOut(circuit2, l, c))
        self.wait()
        self.play(electric_eqs[12].animate.scale(1.75))
        self.wait()
        self.play(
            FadeIn(
                spring_eqs[7].scale(1.75).next_to(electric_eqs[12],DOWN,buff=0.75), 
                pendulum_eqs[4].scale(1.75).next_to(spring_eqs[7],DOWN,buff=0.75)
            )
        )
        self.wait()

