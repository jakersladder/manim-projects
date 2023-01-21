from manim import *

# /// MATH CALCULATIONS ///

# returns resonant frequency
def get_resonant_frequency(L, C):
    frequency = 1 / ((L * C) ** 0.5)
    resonant_frequency = frequency / (2 * PI)
    return resonant_frequency

# returns mean resonant frequency
def get_mean_resonant_frequency(L, C, M):
    mean_resonance = (
        get_resonant_frequency(L * (1 + M), C) +
        get_resonant_frequency(L, C)
    ) / 2
    return mean_resonance
