from manim import *
import math
import numpy as np
from utils import * 


slide_title = Text("Simple Harmonic Oscillators", font_size=48).to_edge(UP, buff=1).set_color(ORANGE)

# Electric Resonance Equations
electric_eqs = VGroup(
    MathTex(r"V_{L}",r"+",r"V_{R}",r"+",r"V_{C}",r"=",r"V_{T}"),
    MathTex(r"V_{L}",r"+",r"V_{R}",r"+",r"V_{C}",r"=",r"0"),
    MathTex(r"V_{L}",r"+",r"V_{R}",r"+",r"\frac{Q}{C}",r"=",r"0"),
    MathTex(r"V_{L}",r"+",r"\frac{d Q}{d t} R",r"+",r"\frac{Q}{C}",r"=",r"0"),
    MathTex(r"\frac{d^2 Q}{d t^2}",r"L",r"+",r"\frac{d Q}{d t}",r"R",r"+",r"\frac{Q}{",r"C}",r"=",r"0"),
    MathTex(r"\frac{d^2 Q}{d t^2}",r"L",r"+",r"\frac{d Q}{d t}",r"R",r"+",r"\frac{Q}{",r"C}",r"=",r"0"),
    MathTex(r"\frac{d I}{d t}",r"L",r"+",r"I",r"R",r"+",r"\frac{1}{",r"C}",r"\int I d t",r"=",r"0"),
    MathTex(r"\frac{d^2 Q}{d t^2}",r"L",r"+",r"\frac{d Q}{d t}",r"R",r"+",r"\frac{Q}{",r"C}",r"=",r"0"),
    MathTex(r"\ddot{Q}",r"L",r"+",r"\dot{Q}",r"R",r"+",r"Q\frac{1}{",r"C}",r"=",r"0"),
    MathTex(r"L",r"\ddot{Q}",r"+",r"\frac{1}{",r"C}",r"Q",r"=",r"0"),
    MathTex(r"\ddot{Q}",r"+",r"\frac{1}{",r"L",r"C}",r"Q",r"=",r"0"),
    MathTex(r"\ddot{Q}",r"=",r"-",r"\frac{1}{",r"L",r"C}",r"Q"),
    MathTex(r"\ddot{Q}",r"=",r"-",r"\omega^2",r"Q")
)

# Electric Parametric Equations
parametric_eqs = VGroup(
    MathTex(r"0=\frac{d I}{d t}L_{o}(1+m\sin \theta ) + I R + \frac{1}{C}\int I d t"),
    MathTex(r"0=\frac{d I}{d t}(L_{o}+L_{o}m\sin \theta ) + I R + \frac{1}{C}\int I d t"),
    MathTex(r"0=\frac{d I}{d t}(L_{o}+L_{o}m\sin (2\pi f_{p}) ) + I R + \frac{1}{C}\int I d t"),
    MathTex(r"0=\frac{d I}{d t}(L_{o}+L_{o}m\sin (\omega _{p}) ) + I R + \frac{1}{C}\int I d t"),
)
# Electric Resonant Frequency Equations
electric_res_eqs = VGroup(
    MathTex(r"\omega_{res}",r"=",r"\frac{1}{",r"\sqrt{",r"L",r"C}}"),
    MathTex(r"\omega^2",r"=",r"\frac{1}{",r"L",r"C}"),
    MathTex(r"\omega_{par} = 2\cdot \omega_{res}")
)
# Spring Resonance Equations
spring_title = Text("Mass on a Spring", font_size=32).next_to(slide_title, DOWN)
spring_eqs = VGroup(
    MathTex(r"m",r"a",r"=",r"-",r"k",r"x"),
    MathTex(r"m",r"a",r"+",r"k",r"x",r"=",r"0"),
    MathTex(r"a",r"+",r"\frac{k}{m}",r"x",r"=",r"0"),
    MathTex(r"a=\frac{d^2x}{dt^2}=",r"\ddot{x}"),
    MathTex(r"\omega",r"=\sqrt{\frac{k}{m}}"),
    MathTex(r"\omega^2",r"=\frac{k}{m}"),
    MathTex(r"\ddot{x}",r"+",r"\omega",r" ^2x",r"=",r"0"),
    MathTex(r"\ddot{x}",r"=",r"-",r"\omega",r" ^2x"),
    MathTex(r"m",r"a",r"+",r"b",r"v",r"+",r"k",r"x",r"=",r"0")
)

# Pendulum Resonance Equations
pendulum_title = Text("Pendulum", font_size=32).next_to(slide_title, DOWN)
pendulum_eqs = VGroup(
    MathTex(r"\frac{d^2\theta}{dt^2}",r"=",r"-",r"\frac{g}{l}",r"\theta"),
    MathTex(r"\frac{d^2\theta}{dt^2}",r"=",r"\ddot{\theta}"),
    MathTex(r"\omega",r"=",r"\sqrt{\frac{g}{l}}"),
    MathTex(r"\omega^2", r" =\frac{g}{l}"),
    MathTex(r"\ddot{\theta}",r"=",r"-",r"\omega^2\theta "),
    MathTex(r"l",r"\ddot{\theta}",r"+",r"l",r"b",r"\dot{\theta}",r"+",r"g",r"\sin",r"\theta",r"=",r"0")
)

        # self.add(slide_title)
        # self.play(Write(spring_title))
        # self.play(Write(spring_eqs[0].next_to(spring_title, DOWN), runtime=2))
        # self.play(TransformMatchingTex(spring_eqs[0].copy(), spring_eqs[1].next_to(spring_eqs[0], DOWN, buff=0.5), path_arc=90*DEGREES))
        # self.play(TransformMatchingTex(spring_eqs[1].copy(), spring_eqs[2].next_to(spring_eqs[1], DOWN, buff=0.5)))
        # self.remove(spring_eqs[0],spring_eqs[1])
        # self.play(spring_eqs[2].animate.shift(2*LEFT))
        # self.play(Write(spring_eqs[3].next_to(spring_eqs[2], RIGHT, buff=1).shift(UP)))
        # self.play(Write(spring_eqs[4].next_to(spring_eqs[3], DOWN, buff=0.8)))
        # self.play(spring_eqs[4].animate.become(spring_eqs[5]. next_to(spring_eqs[3], DOWN, buff=0.8)))
        
        # self.play(spring_eqs[2][0].animate.become(spring_eqs[3][1].copy().move_to(spring_eqs[2][0])))
        # self.play(spring_eqs[2][2].animate.become(spring_eqs[5][0].move_to(spring_eqs[2][2])))
        
        # self.play(ReplacementTransform(spring_eqs[2],spring_eqs[6].scale(1.5)), FadeOut(spring_eqs[3],spring_eqs[4],spring_eqs[5]))
        # self.play(TransformMatchingTex(spring_eqs[6].copy(), spring_eqs[7].scale(1.5).next_to(spring_eqs[6], DOWN, buff=0.5), path_arc=90*DEGREES))
        # self.play(FadeOut(spring_eqs[6]), spring_eqs[7].animate.shift(UP))
        # self.play(FadeOut(spring_eqs[7], spring_title))
        
        # self.play(Write(pendulum_title))
        # self.play(Write(pendulum_eqs[0].shift(0.8*DOWN)))
        # self.play(pendulum_eqs[0].animate.shift(2*LEFT))
        # self.play(Write(pendulum_eqs[1].next_to(pendulum_eqs[0], RIGHT, buff=1).shift(UP)))
        # self.play(Write(pendulum_eqs[2].next_to(pendulum_eqs[1], DOWN, buff=0.8)))
        # self.play(pendulum_eqs[2].animate.become(pendulum_eqs[3].next_to(pendulum_eqs[1], DOWN, buff=0.8)))

        # self.play(pendulum_eqs[0][0].animate.become(pendulum_eqs[1][2].copy().move_to(pendulum_eqs[0][0])))
        # self.play(pendulum_eqs[0][3].animate.become(pendulum_eqs[3][0].move_to(pendulum_eqs[0][3])))

        # self.play(ReplacementTransform(pendulum_eqs[0], pendulum_eqs[4].scale(1.5)), FadeOut(pendulum_eqs[1],pendulum_eqs[2],pendulum_eqs[3]))
        # self.play(FadeIn(spring_eqs[7].next_to(pendulum_eqs[4], DOWN, buff=0.8)))

