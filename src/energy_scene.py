from manim import *
import math
import numpy as np
from utils import * 
from math_equations import *

class EnergyScene(Scene):
    r = ValueTracker(0)
    l = ValueTracker(0.2)
    c = ValueTracker(0.0000001)
    m = ValueTracker(0.2)

    emf = 1.0
    i = 0
    q = c.get_value() * emf
    
    time = ValueTracker(0.01)
    dt = .001 * time.get_value()
    delta = ValueTracker(0)
    y_range = ValueTracker(5)

    # Returns varying inductance at time t
    def get_varying_inductance(self, t):
        l_var = (
            self.l.get_value() * (
            1 + (self.m.get_value() * np.sin(
            2 * PI * get_resonant_frequency(self.l.get_value(), self.c.get_value()) * 2 * t
            )))
        )
        return l_var

    # Returns the Voltage and Current at frame
    def get_power_and_energy(self):
        alpha = (self.q / (self.l.get_value() * self.c.get_value())) - (self.i * self.r.get_value() / self.l.get_value())

        self.i = self.i + (alpha * self.dt)
        self.q = self.q - (self.i * self.dt)

        power = self.l.get_value() * self.i * alpha
        energy = (self.l.get_value() * (self.i ** 2)) * 0.5
        return power, energy, self.l.get_value(), self.i, alpha
    
    # Returns the Voltage and Current with Parametric Variation at frame
    def get_para_power_and_energy(self, t):
        alpha = (self.q / (self.get_varying_inductance(t) * self.c.get_value())) - (self.i * self.r.get_value() / self.get_varying_inductance(t))

        self.i = self.i + (alpha * self.dt)
        self.q = self.q - (self.i * self.dt)

        lvar = self.get_varying_inductance(t)
        power = self.get_varying_inductance(t) * self.i * alpha
        energy = (self.get_varying_inductance(t) * (self.i ** 2)) * 0.5
        return power, energy, lvar, self.i, alpha
    
    # Returns the Voltage and Current at frame
    def get_voltage_and_current(self):
        alpha = (self.q / (self.l.get_value() * self.c.get_value())) - (self.i * self.r.get_value() / self.l.get_value())

        self.i = self.i + (alpha * self.dt)
        self.q = self.q - (self.i * self.dt)

        Vc = self.q / self.c.get_value()
        Vr = self.i * self.r.get_value()
        Vl = -Vc - Vr
        return Vc, -self.i, Vr, Vl
    
    def get_para_voltage_and_current(self, t):
        alpha = (self.q / (self.get_varying_inductance(t) * self.c.get_value())) - (self.i * self.r.get_value() / self.get_varying_inductance(t))

        self.i = self.i + (alpha * self.dt)
        self.q = self.q - (self.i * self.dt)

        Vc = self.q / self.c.get_value()
        Vr = self.i * self.r.get_value()
        lvar = self.get_varying_inductance(t)
        return Vc, self.i, Vr, lvar


# ---Plotting Functions---

    # ---Regular Functions---

    def generate_para_power_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_para_power_and_energy(t)[0], [0, self.delta.get_value(), self.dt]).set_color(RED)

    def generate_para_energy_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_para_power_and_energy(t)[1], [0, self.delta.get_value(), self.dt]).set_color(YELLOW)

    def generate_para_voltage_plot_l(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_para_voltage_and_current(t)[3], [0, self.delta.get_value(), self.dt]).set_color(GREEN)

    def generate_para_current_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: -self.get_para_voltage_and_current(t)[1], [0, self.delta.get_value(), self.dt]).set_color(BLUE)
    
    def generate_para_l_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_para_power_and_energy(t)[2], [0, self.delta.get_value(), self.dt]).set_color(ORANGE)
    
    def generate_para_alpha_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_para_power_and_energy(t)[4], [0, self.delta.get_value(), self.dt]).set_color(PURE_BLUE)

    # ---Parametric Plotting Functions---
    def generate_power_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_power_and_energy()[0], [0, self.delta.get_value(), self.dt]).set_color(RED)

    def generate_energy_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_power_and_energy()[1], [0, self.delta.get_value(), self.dt]).set_color(YELLOW)

    def generate_voltage_plot_l(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_voltage_and_current()[3], [0, self.delta.get_value(), self.dt]).set_color(GREEN)

    def generate_current_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: -self.get_power_and_energy()[3], [0, self.delta.get_value(), self.dt]).set_color(BLUE)
    
    def generate_l_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_power_and_energy()[2], [0, self.delta.get_value(), self.dt]).set_color(ORANGE)
    
    def generate_alpha_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_power_and_energy()[4], [0, self.delta.get_value(), self.dt]).set_color(ORANGE)
    
    
# ---CONSTRUCTOR------------------------------------------------------------------------------------------------------

    def construct(self):

# --- Axes ---

        axes = Axes(
            x_range=[0, self.time.get_value()+0.00001,self.time.get_value()],
            y_range=[-0.001, 0.001],
            x_length=10,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": np.arange(0, self.time.get_value()+0.00001,self.time.get_value())},        
            tips=False,
        ).scale(0.7).to_edge(LEFT)
        axes_2 = Axes(
            x_range=[0, self.time.get_value()+0.00001,self.time.get_value()],
            y_range=[-1, 1.01, 0.1],
            x_length=10,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": np.arange(0, self.time.get_value()+0.00001,self.time.get_value())},        
            tips=False,
        ).scale(0.7).to_edge(LEFT)
        axes_3 = Axes(
            x_range=[0, self.time.get_value()+0.00001,self.time.get_value()],
            y_range=[-0.000001, 0.000001],
            x_length=10,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": np.arange(0, self.time.get_value()+0.00001,self.time.get_value())},        
            tips=False,
        ).scale(0.7).to_edge(LEFT)

# --- Plot Generators and Updaters ---

        power = self.generate_power_plot(axes)
        energy = self.generate_energy_plot(axes_3)
        voltage = self.generate_voltage_plot_l(axes)
        current = self.generate_current_plot(axes)
        inductance = self.generate_l_plot(axes_2)
        power.add_updater(lambda mob: mob.become(self.generate_power_plot(axes)))
        energy.add_updater(lambda mob: mob.become(self.generate_energy_plot(axes_3)))
        voltage.add_updater(lambda mob: mob.become(self.generate_voltage_plot_l(axes_2)))
        current.add_updater(lambda mob: mob.become(self.generate_current_plot(axes)))
        inductance.add_updater(lambda mob: mob.become(self.generate_l_plot(axes_2)))

        para_power = self.generate_para_power_plot(axes)
        para_energy = self.generate_para_energy_plot(axes_3)
        para_voltage = self.generate_para_voltage_plot_l(axes_2)
        para_current = self.generate_para_current_plot(axes)
        para_inductance = self.generate_para_l_plot(axes_2)
        para_power.add_updater(lambda mob: mob.become(self.generate_para_power_plot(axes)))
        para_energy.add_updater(lambda mob: mob.become(self.generate_para_energy_plot(axes_3)))
        para_voltage.add_updater(lambda mob: mob.become(self.generate_para_voltage_plot_l(axes_2)))
        para_current.add_updater(lambda mob: mob.become(self.generate_para_current_plot(axes)))
        para_inductance.add_updater(lambda mob: mob.become(self.generate_para_l_plot(axes_2)))

    
# --- Decimal Numbers ---

        num_inductance = DecimalNumber(0, num_decimal_places=6, include_sign=True)
        num_current = DecimalNumber(0, num_decimal_places=6, include_sign=True)
        num_para_inductance = DecimalNumber(0, num_decimal_places=6, include_sign=True)
        num_para_current = DecimalNumber(0, num_decimal_places=6, include_sign=True)
        num_energy = DecimalNumber(0, num_decimal_places=12, include_sign=True)
        num_para_energy = DecimalNumber(0, num_decimal_places=12, include_sign=True)

        num_inductance.add_updater(lambda num: num.set_value(axes_2.input_to_graph_coords(self.delta.get_value(), inductance)[1]))
        num_current.add_updater(lambda num: num.set_value(axes.input_to_graph_coords(self.delta.get_value(), current)[1]))
        num_energy.add_updater(lambda num: num.set_value(axes_3.input_to_graph_coords(self.delta.get_value(), energy)[1]))
        num_para_inductance.add_updater(lambda num: num.set_value(axes_2.input_to_graph_coords(self.delta.get_value(), para_inductance)[1]))
        num_para_current.add_updater(lambda num: num.set_value(axes.input_to_graph_coords(self.delta.get_value(), para_current)[1]))
        num_para_energy.add_updater(lambda num: num.set_value(axes_3.input_to_graph_coords(self.delta.get_value(), para_energy)[1]))

# --- Dots and Lines ---
    # ---Dots---
        inductance_dot = Dot(axes_2.i2gp(self.delta.get_value(), inductance))
        current_dot = Dot(axes.i2gp(self.delta.get_value(), current))
        energy_dot = Dot(axes_3.i2gp(self.delta.get_value(), energy))
        para_inductance_dot = Dot(axes_2.i2gp(self.delta.get_value(), para_inductance))
        para_current_dot = Dot(axes.i2gp(self.delta.get_value(), para_current))
        para_energy_dot = Dot(axes_3.i2gp(self.delta.get_value(), para_energy))

        inductance_dot.add_updater(lambda d: d.move_to(axes_2.i2gp(self.delta.get_value(), inductance)))
        current_dot.add_updater(lambda d: d.move_to(axes.i2gp(self.delta.get_value(), current)))
        energy_dot.add_updater(lambda d: d.move_to(axes_3.i2gp(self.delta.get_value(), energy)))
        para_inductance_dot.add_updater(lambda d: d.move_to(axes_2.i2gp(self.delta.get_value(), para_inductance)))
        para_current_dot.add_updater(lambda d: d.move_to(axes.i2gp(self.delta.get_value(), para_current)))
        para_energy_dot.add_updater(lambda d: d.move_to(axes_3.i2gp(self.delta.get_value(), para_energy)))

# --- Scene ---
        self.add(axes, power, energy, voltage, current, inductance)
        self.add(axes_2, axes_3)
        self.add(
            num_current.next_to(axes, RIGHT, buff=1), 
            num_inductance.next_to(num_current, UP, buff=0.5), 
            num_energy.next_to(num_current, DOWN, buff=0.5)
        )
        self.add(inductance_dot, current_dot, energy_dot)
        self.play(self.delta.animate.set_value(self.time.get_value()),run_time=12,rate_func=linear)
        self.wait()
        self.remove(power, energy, voltage, current, inductance)
        self.remove(num_current, num_inductance, num_energy)
        self.delta.set_value(0)
        self.wait()
        self.add(para_power, para_energy, para_voltage, para_current, para_inductance)
        self.add(
            num_para_current.next_to(axes, RIGHT, buff=1), 
            num_para_inductance.next_to(num_para_current, UP, buff=0.5), 
            num_para_energy.next_to(num_para_current, DOWN, buff=0.5)
        )
        self.add(para_inductance_dot, para_current_dot, para_energy_dot)
        self.play(self.delta.animate.set_value(self.time.get_value()),run_time=12,rate_func=linear)
        self.wait()



    

