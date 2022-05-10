from manim import *
import math
import numpy as np
from utils import * 

# Electric Circuit Simulator
class MathEquations(Scene):
    def construct(self):

        # Basic Equations
        eq1 = MathTex(r"V_{L}",r"+",r"V_{R}",r"+",r"V_{C}",r"=",r"V_{T}")
        eq2 = MathTex(r"V_{L}",r"+",r"V_{R}",r"+",r"V_{C}",r"=",r"0")
        eq3 = MathTex(r"\frac{d^2 Q}{d t^2}L",r"+",r"V_{R}",r"+",r"V_{C}",r"=",r"0")
        eq4 = MathTex(r"\frac{d^2 Q}{d t^2}L",r"+",r"\frac{d Q}{d t} R",r"+",r"V_{C}",r"=",r"0")
        eq5 = MathTex(r"\frac{d^2 Q}{d t^2}L",r"+",r"\frac{d Q}{d t} R",r"+",r"\frac{Q}{C}",r"=",r"0")
        eq6 = MathTex(r"\frac{d I}{d t}L",r"+",r"I R",r"+",r"\frac{1}{C}\int I d t",r"=",r"0")
        eq7 = MathTex(r"\ddot{Q}L",r"+",r"\dot{Q}R",r"+",r"Q\frac{1}{C}",r"=",r"0")
        eq8 = MathTex(r"L\ddot{Q}",r"+",r"\frac{1}{C}Q=0")
        eq9 = MathTex(r"L\ddot{Q}",r"=",r"-\frac{1}{C}Q")
        eq10 = MathTex(r"\ddot{Q}",r"+",r"\frac{1}{LC}Q=0")
        eq11 = MathTex(r"\ddot{Q}",r"+",r"\omega^2Q=0")
        
        # Parametric Equations
        p_eq1 = MathTex(r"0=\frac{d I}{d t}L_{o}(1+m\sin \theta ) + I R + \frac{1}{C}\int I d t")
        p_eq2 = MathTex(r"0=\frac{d I}{d t}(L_{o}+L_{o}m\sin \theta ) + I R + \frac{1}{C}\int I d t")
        p_eq3 = MathTex(r"0=\frac{d I}{d t}(L_{o}+L_{o}m\sin (2\pi f_{p}) ) + I R + \frac{1}{C}\int I d t")
        p_eq4 = MathTex(r"0=\frac{d I}{d t}(L_{o}+L_{o}m\sin (\omega _{p}) ) + I R + \frac{1}{C}\int I d t")

        # Resonant Frequency Equations
        resonant_freq_eq1 = MathTex(r"\omega_{res} =\frac{1}{\sqrt{LC}}")
        resonant_freq_eq2 = MathTex(r"\omega^2 =\frac{1}{LC}")
        parametric_freq_eq1 = MathTex(r"\omega_{par} = 2\cdot \omega_{res}")

        # equations = VGroup(eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8,
        #                   resonant_freq_eq1, resonant_freq_eq2, parametric_freq_eq1).arrange(DOWN).scale(0.5)
        
        self.play(Write(eq1), runtime=3)
        self.play(ReplacementTransform(eq1, eq2))
        self.play(ReplacementTransform(eq2, eq3))
        self.play(ReplacementTransform(eq3, eq4))
        self.play(ReplacementTransform(eq4, eq5))
        self.play(ReplacementTransform(eq5, eq7))
        self.play(ReplacementTransform(eq7, eq8))
        self.play(ReplacementTransform(eq8, eq9))
        self.play(ReplacementTransform(eq9, eq10))
        self.play(ReplacementTransform(eq10, eq11))
        self.play(eq11.animate.move_to(2*LEFT))
        self.play(Write(resonant_freq_eq1.next_to(eq11, RIGHT, buff=2)))

