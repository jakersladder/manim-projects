from manim import *
import math
import numpy as np

# Electric Circuit Simulator
class JakerLadder(Scene):
    def construct(self):
        ladder1 = SVGMobject("src/assets/ladder1.svg").set_color(YELLOW_E).scale(2.25)
        title = VGroup(
            Text("J", font_size=180, font="Comic Sans MS").set_color(YELLOW_E).next_to(ladder1,LEFT,buff=0.2),
            Text("L", font_size=180, font="Comic Sans MS").set_color(YELLOW_E).next_to(ladder1,RIGHT).shift(LEFT*0.2)
        )
        self.add(ladder1, title)