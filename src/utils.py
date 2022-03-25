from manim import PI

def get_resonant_frequency(L, C):
    frequency = 1 / ((L.get_value() * C.get_value()) ** 0.5)
    resonant_frequency = frequency / (2 * PI)
    return resonant_frequency
    