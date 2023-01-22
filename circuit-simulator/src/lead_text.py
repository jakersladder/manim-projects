from manim import *
import math
import numpy as np

# Electric Circuit Simulator
class LeadText(Scene):
    def construct(self):
        intro_text = Tex(r'Before we talk about the theory and experimental setup of \linebreak parametric resonance in electric circuits...').scale(0.8)
        para_text = Text("Oscilators").set_color(BLUE)
        self.play(Write(intro_text.next_to(para_text, UP, buff=1)), run_time=5.8)
        self.wait(2)
        self.play(FadeIn(para_text))
        self.wait(3)         