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
    MathTex(r"\ddot{Q}",r"L",r"+",r"\dot{Q}",r"R",r"+",r"Q",r"\frac{1}{",r"C}",r"=",r"0"),
    MathTex(r"L",r"\ddot{Q}",r"+",r"\frac{1}{",r"C}",r"Q",r"=",r"0"),
    MathTex(r"\ddot{Q}",r"+",r"\frac{1}{",r"L",r"C}",r"Q",r"=",r"0"),
    MathTex(r"\ddot{Q}",r"=",r"-",r"\frac{1}{",r"L",r"C}",r"Q"),
    MathTex(r"\ddot{Q}",r"=",r"-",r"\omega^2",r"Q")
)
# Voltage Equations
voltage_eqs = VGroup(
    MathTex(r"V_{",r"L}",r"=",r"\frac{d^2 Q}{d t^2}",r"L", font_size=32),
    MathTex(r"V_{",r"R}",r"=",r"\frac{d Q}{d t}",r"R", font_size=32),
    MathTex(r"V_{",r"C}",r"=",r"\frac{Q}{",r"C}", font_size=32)
)
# Electric Parametric Equations
parametric_eqs = VGroup(
    MathTex(r"\ddot{Q}",r"L",r"_{o}",r"(1",r"+",r"m",r"\sin",r"\omega_{p}",r"t)",r"+",r"\dot{Q}",r"R",r"+",r"Q",r"\frac{1}{",r"C}",r"=",r"0"),
    MathTex(r"\ddot{Q}",r"(",r"L_{o}",r"+",r"L_{o}",r"m",r"\sin",r"\omega_{p}",r"t)",r"+",r"\dot{Q}",r"R",r"+",r"Q",r"\frac{1}{",r"C}",r"=",r"0"),
    MathTex(r"\ddot{Q}",r"(",r"L_{o}",r"+",r"L_{\Delta }",r"\sin",r"\omega_{p}",r"t)",r"+",r"\dot{Q}",r"R",r"+",r"Q",r"\frac{1}{",r"C}",r"=",r"0"),
    MathTex(r"\frac{dI}{dt}(L_{o}+L_{o}m\sin (\omega _{p}) ) + I R + \frac{1}{C}\int I d t",r"=",r"0"),
)
# Electric Resonant Frequency Equations
electric_res_eqs = VGroup(
    MathTex(r"\omega_{r}",r"=",r"2\pi",r"\frac{1}{",r"\sqrt{",r"L",r"C}}"),
    MathTex(r"\omega^2",r"=",r"\frac{1}{",r"L",r"C}"),
    MathTex(r"\omega_{p} = 2\cdot \omega_{r}"),
    MathTex(r"f_{r}",r"=",r"\frac{1}{",r"\sqrt{",r"L",r"C}}"),
    MathTex(r"f_{p} = 2\cdot f_{r}")
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