from manim import *
import math
import numpy as np

# Electric Circuit Simulator
class IntroText(Scene):
    def construct(self):
        intro_text = Tex(r'I want to talk today about a lesser known \linebreak phenomenon in electricity...').scale(0.8)
        para_text = Text("Parametric Resonance").set_color(GOLD_A)
        self.play(Write(intro_text.next_to(para_text, UP, buff=1)), run_time=3.5)
        self.wait(2)
        self.play(FadeIn(para_text))
        self.wait(3)
         