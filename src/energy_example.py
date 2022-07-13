from manim import *
import math
import numpy as np
from utils import * 
from math_equations import *

class EnergyExample(Scene):
    r = ValueTracker(0)
    l = ValueTracker(0.2)
    c = ValueTracker(0.0000001)
    m = ValueTracker(0.2)

    emf = 1.0
    i = 0
    q = c.get_value() * emf
    
    time = ValueTracker(0.006)
    dt = .001 * time.get_value()
    start = ValueTracker(0)
    delta = ValueTracker(0)
    y_range = ValueTracker(5)

    # Returns varying inductance at time t
    def get_varying_inductance(self, t):
        l_var = (
            self.l.get_value() * (
            1 + (self.m.get_value() * -np.sin(
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
        return axes.plot(lambda t: self.get_para_power_and_energy(t)[0], [self.start.get_value(), self.delta.get_value(), self.dt]).set_color(RED)

    def generate_para_energy_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_para_power_and_energy(t)[1], [self.start.get_value(), self.delta.get_value(), self.dt]).set_color(YELLOW)

    def generate_para_voltage_plot_l(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_para_voltage_and_current(t)[3], [self.start.get_value(), self.delta.get_value(), self.dt]).set_color(GREEN)

    def generate_para_current_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: -self.get_para_voltage_and_current(t)[1], [self.start.get_value(), self.delta.get_value(), self.dt]).set_color(BLUE)
    
    def generate_para_l_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_para_power_and_energy(t)[2], [self.start.get_value(), self.delta.get_value(), self.dt]).set_color(ORANGE)
    
    def generate_para_alpha_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_para_power_and_energy(t)[4], [self.start.get_value(), self.delta.get_value(), self.dt]).set_color(PURE_BLUE)

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
            x_range=[self.start.get_value(), self.time.get_value()+0.00001,self.time.get_value()],
            y_range=[-0.001, 0.001],
            x_length=10,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": np.arange(self.start.get_value(), self.time.get_value()+0.00001,self.time.get_value())},        
            tips=False,
        ).scale(0.8).to_edge(LEFT)
        axes_2 = Axes(
            x_range=[self.start.get_value(), self.time.get_value()+0.00001,self.time.get_value()],
            y_range=[-1, 1.01, 0.1],
            x_length=10,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": np.arange(self.start.get_value(), self.time.get_value()+0.00001,self.time.get_value())},        
            tips=False,
        ).scale(0.8).to_edge(LEFT).shift(LEFT*0.09)
        axes_3 = Axes(
            x_range=[self.start.get_value(), self.time.get_value()+0.00001,self.time.get_value()],
            y_range=[-0.0000002, 0.0000002],
            x_length=10,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": np.arange(self.start.get_value(), self.time.get_value()+0.00001,self.time.get_value())},        
            tips=False,
        ).scale(0.8).to_edge(LEFT)

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

        num_inductance = DecimalNumber(0, num_decimal_places=6).set_color(ORANGE)
        num_current = DecimalNumber(0, num_decimal_places=6, include_sign=True).set_color(BLUE)
        num_para_inductance = DecimalNumber(0, num_decimal_places=6).set_color(ORANGE)
        num_para_current = DecimalNumber(0, num_decimal_places=6, include_sign=True).set_color(BLUE)
        num_energy = DecimalNumber(0, num_decimal_places=12).set_color(YELLOW)
        num_para_energy = DecimalNumber(0, num_decimal_places=12).set_color(YELLOW)

        num_inductance.add_updater(lambda num: num.set_value(axes_2.input_to_graph_coords(self.delta.get_value(), inductance)[1]))
        num_current.add_updater(lambda num: num.set_value(axes.input_to_graph_coords(self.delta.get_value(), current)[1]))
        num_energy.add_updater(lambda num: num.set_value(axes_3.input_to_graph_coords(self.delta.get_value(), energy)[1]))
        num_para_inductance.add_updater(lambda num: num.set_value(axes_2.input_to_graph_coords(self.delta.get_value(), para_inductance)[1]))
        num_para_current.add_updater(lambda num: num.set_value(axes.input_to_graph_coords(self.delta.get_value(), para_current)[1]))
        num_para_energy.add_updater(lambda num: num.set_value(axes_3.input_to_graph_coords(self.delta.get_value(), para_energy)[1]))

# --- Equations and Text ---
        title = Text("Parametric Effect on Energy", font_size=48).to_edge(UP, buff=0.5).set_color(BLUE)
        energy_equation = MathTex(r"W", r"=", r"\frac{1}{2}",r"\times",r"L",r"\times",r"i",r"^{2}")
        squared = MathTex(r"^{2}")

        decimal_equation = VGroup(
            num_energy.copy(), 
            MathTex(r"="), MathTex(r"\frac{1}{2}"), MathTex(r"\times"), 
            num_inductance.copy(), 
            MathTex(r"\times"),
            num_current.copy()
        ).arrange(RIGHT)
        
        para_decimal_equation = VGroup(
            num_para_energy.copy(), 
            MathTex(r"="), MathTex(r"\frac{1}{2}"), MathTex(r"\times"), 
            num_para_inductance.copy(), 
            MathTex(r"\times"),
            num_para_current.copy()
        ).arrange(RIGHT)

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
        self.add(axes, title, voltage, energy, current, inductance)
        # self.add(decimal_equation.to_edge(DOWN, buff=0.5), squared.next_to(decimal_equation, UR, buff=0).shift(DOWN*0.2+RIGHT*0.1))
        # self.add(inductance_dot, current_dot, energy_dot)
        # self.wait()
        # self.play(self.delta.animate.set_value(self.time.get_value()),run_time=30,rate_func=linear)
        # self.wait()
        # self.remove(energy, current, inductance)
        # self.delta.set_value(0)
        # self.wait()

        # self.remove(decimal_equation)
        self.add(para_energy, para_voltage, para_current, para_inductance)
        # self.add(para_decimal_equation.to_edge(DOWN, buff=0.5), squared.next_to(para_decimal_equation, UR, buff=0).shift(DOWN*0.2+RIGHT*0.1))
        # self.add(para_inductance_dot, para_current_dot, para_energy_dot)
        self.play(self.delta.animate.set_value(self.time.get_value()),run_time=30,rate_func=linear)
        self.wait()
        # self.remove(para_energy, para_current, para_inductance)
        # self.remove(para_inductance_dot, para_current_dot, para_energy_dot)

