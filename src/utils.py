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

# /// ORIENTERS ///

# for inductor
def set_oriention_l_plus(self, mobj, next):
    if self.get_voltage_and_current(0)[0] > 0:
        mobj.next_to(next, DL, buff=0)
    else:
        mobj.next_to(next, UL, buff=0)

def set_oriention_l_minus(self, mobj, next):
    if self.get_voltage_and_current(0)[0] > 0:
        mobj.next_to(next, UL, buff=0)
    else:
        mobj.next_to(next, DL, buff=0)

# for resistor
def set_oriention_r_plus(self, mobj, next):
    if self.get_voltage_and_current(0)[1] > 0:
        mobj.next_to(next, UR, buff=0)
    else:
        mobj.next_to(next, UL, buff=0)

def set_oriention_r_minus(self, mobj, next):
    if self.get_voltage_and_current(0)[1] > 0:
        mobj.next_to(next, UL, buff=0)
    else:
        mobj.next_to(next, UR, buff=0)

# for capacitor
def set_oriention_c_plus(self, mobj, next):
    if self.get_voltage_and_current(0)[0] > 0:
        mobj.next_to(next, UR)
    else:
        mobj.next_to(next, DR)

def set_oriention_c_minus(self, mobj, next):
    if self.get_voltage_and_current(0)[0] > 0:
        mobj.next_to(next, DR)
    else:
        mobj.next_to(next, UR)

# for arrows
def set_orienation_l_arrow(self, mobj, next):
    if self.get_voltage_and_current(0)[1] > 0:
        mobj.put_start_and_end_on(start=DOWN, end=UP).next_to(next, RIGHT, buff=0.1).scale(0.4)
    else:
        mobj.put_start_and_end_on(start=UP, end=DOWN).next_to(next, RIGHT, buff=0.1).scale(0.4)

def set_orienation_r_arrow(self, mobj, next):
    if self.get_voltage_and_current(0)[1] > 0:
        mobj.put_start_and_end_on(start=LEFT, end=RIGHT).next_to(next, DOWN).scale(0.4)
    else:
        mobj.put_start_and_end_on(start=RIGHT, end=LEFT).next_to(next, DOWN).scale(0.4)

def set_orienation_c_arrow(self, mobj, next):
    if self.get_voltage_and_current(0)[1] > 0:
        mobj.put_start_and_end_on(start=UP, end=DOWN).next_to(next, LEFT).scale(0.4)
    else:
        mobj.put_start_and_end_on(start=DOWN, end=UP).next_to(next, LEFT).scale(0.4)