from manim import *
import math
import numpy as np
from utils import * 

# Electric Circuit Simulator
class ParaExample(Scene):
    r = ValueTracker(10)
    l = ValueTracker(0.05)
    c = ValueTracker(0.0000001)
    m = ValueTracker(0.2)

    emf = 0.1
    i = 0
    q = c.get_value() * emf

    time = ValueTracker(0.00022)
    dt = .001 * time.get_value()
    delta = ValueTracker(0)

    # def get_mean_resonant_frequency(self):
    #     mean_resonance = (
    #         get_resonant_frequency(self.l.get_value() * (1 + self.m.get_value()), self.c.get_value()) +
    #         get_resonant_frequency(self.l.get_value(), self.c.get_value())
    #     ) / 2
    #     return mean_resonance

    def get_varying_inductance(self, t):
        l_var = (
            self.l.get_value() * (
            1 + (self.m.get_value() * np.sin(
            2 * PI * get_resonant_frequency(self.l.get_value(), self.c.get_value()) * 2 * t
            )))
        )
        return l_var


    # Returns voltage and current as an array at time t
    def get_voltage_and_current(self, t):
        alpha = (self.q / (self.get_varying_inductance(t) * self.c.get_value())) - (self.i * self.r.get_value() / self.get_varying_inductance(t))

        self.i = self.i + (alpha * self.dt)
        self.q = self.q - (self.i * self.dt)

        Vc = self.q / self.c.get_value()
        lvar = self.get_varying_inductance(t)
        return Vc, self.i, lvar

    # Generates the plot Volatage by Time
    def generate_voltage_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_voltage_and_current(t)[0], [0, self.delta.get_value(), self.dt]).set_color(PURPLE)

    # Generates the plot Current by Time
    def generate_current_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_voltage_and_current(t)[1], [0, self.delta.get_value(), self.dt]).set_color(BLUE)

    def generate_lvar_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_voltage_and_current(t)[2], [0, self.delta.get_value(), self.dt]).set_color(ORANGE)

    # Constructs the Scene
    def construct(self):
      
        # Create axes and and add updater
        axes = Axes(
                x_range=[0, self.time.get_value()+0.00001,self.time.get_value()],
                y_range=[-0.1, 0.101, 0.1],
                x_length=10,
                axis_config={"color": WHITE},
                x_axis_config={"numbers_to_include": np.arange(0, self.time.get_value()+0.00001,self.time.get_value())},
                y_axis_config={"numbers_to_include": np.arange(-0.1, 0.101, 0.1)},        
                tips=False,
            )
        axes.add_updater(lambda mob: mob.become(Axes(
                x_range=[0, self.time.get_value()+0.00001,self.time.get_value()],
                y_range=[-0.1, 0.101, 0.1],
                x_length=10,
                axis_config={"color": WHITE},
                x_axis_config={"numbers_to_include": np.arange(0, self.time.get_value()+0.00001,self.time.get_value())},
                y_axis_config={"numbers_to_include": np.arange(-0.1, 0.101, 0.1)},        
                tips=False,
            )))
        labels = axes.get_axis_labels('t', 'V,A')

        x_axis = axes.get_x_axis()
        x_axis.add_updater(lambda mob: mob.set(x_range = [0, self.time.get_value(), .1]))

        # generate plot of Voltage and Current and adds updater to be redrawn every frame
        voltage = self.generate_voltage_plot(axes)
        current = self.generate_current_plot(axes)
        l_varry = self.generate_lvar_plot(axes)
        voltage.add_updater(lambda mob: mob.become(self.generate_voltage_plot(axes)))
        current.add_updater(lambda mob: mob.become(self.generate_current_plot(axes)))
        l_varry.add_updater(lambda mob: mob.become(self.generate_lvar_plot(axes)))

        # Create Resistance text
        r_text, r_number, r_units = r_label = VGroup(
            Text("R = ", font_size=36).set_color(RED),
            DecimalNumber(
                self.r.get_value(),
                num_decimal_places = 2,
                include_sign = True
            ),
            Tex("$\Omega$", font_size=44).set_color(WHITE)
        )
        r_label.arrange(RIGHT).next_to(axes, DOWN)
        
        # Create Inductance text
        l_text, l_number, l_units = l_label = VGroup(
            Text("L = ", font_size=36).set_color(GREEN),
            DecimalNumber(
                self.l.get_value(),
                num_decimal_places = 6
            ),
            Text("H", font_size=28, slant = ITALIC).set_color(WHITE)
        )
        l_label.arrange(RIGHT).next_to(r_label, LEFT)
        
        # Create Capacitance text
        c_text, c_number, c_units = c_label = VGroup(
            Text("C = ", font_size=36).set_color(PURPLE),
            DecimalNumber(
                self.c.get_value(),
                num_decimal_places = 7
            ),
            Text("F", font_size=28, slant = ITALIC).set_color(WHITE)
        )
        c_label.arrange(RIGHT).next_to(r_label, RIGHT)

        # Create Para Frequency Text
        var_freq_text = MathTex(r"f_{para} = ", font_size=36).set_color(ORANGE)
        var_freq_number = DecimalNumber(
                    2*get_resonant_frequency(self.l.get_value(), self.c.get_value()),
                    num_decimal_places = 2
                )
        var_freq_units = MathTex(r"Hz", font_size=36)
        var_freq_label = VGroup(var_freq_text, var_freq_number, var_freq_units)
        var_freq_label.arrange(RIGHT)

        # Create Frequency Text
        frequency_text = MathTex(r"f_{res}=", font_size=36).set_color(GOLD_A)
        frequency_number = DecimalNumber(
                    get_resonant_frequency(self.l.get_value(), self.c.get_value()),
                    num_decimal_places = 2
                )
        frequency_units = MathTex(r"Hz", font_size=36)
        frequency_label = VGroup(frequency_text, frequency_number, frequency_units)
        frequency_label.arrange(RIGHT)
        freqs = VGroup(frequency_label, var_freq_label).arrange(RIGHT).next_to(axes, UP)

        # Create Voltage and Current Text
        va_label = VGroup(
            VGroup(Text("m", font_size=28).set_color(MAROON_B), Text("="),DecimalNumber(self.m.get_value(), num_decimal_places=1)).arrange(RIGHT),
            Text('CURRENT (I)', font_size=28).set_color(BLUE)
        ).arrange(RIGHT, buff=0.7).next_to(r_label, UP)

        # add updaters to decimal numbers
        r_number.add_updater(lambda m: m.set_value(self.r.get_value()))
        l_number.add_updater(lambda m: m.set_value(self.l.get_value()))
        c_number.add_updater(lambda m: m.set_value(self.c.get_value()))
        frequency_number.add_updater(lambda m: m.set_value(get_resonant_frequency(self.l.get_value(), self.c.get_value())))

        # add objects and animations
        self.add(r_label, l_label, c_label, freqs, va_label)
        self.add(axes, voltage, current, l_varry)

        # play animations
        self.wait()
        self.play(self.delta.animate.set_value(self.time.get_value()),run_time=10,rate_func=linear)
        self.wait()
        self.play(FadeOut(voltage,current,l_varry))
        self.wait()
        self.delta.set_value(0)
        self.time.set_value(0.005)
        self.add(voltage,current,l_varry)
        self.play(self.delta.animate.set_value(self.time.get_value()),run_time=10,rate_func=linear)
        self.wait()

        # self.play(self.r.animate.set_value(10), run_time = 10)
        # self.play(self.l.animate.set_value(0.5), run_time = 2)
        # self.play(self.c.animate.set_value(0.002), run_time = 2)
        # self.play(self.m.animate.set_value(0.5), run_time = 2)


        # self.play(self.l.animate.set_value(0.2), run_time = 1)
        # self.play(self.c.animate.set_value(0.0001), run_time = 1)
        # self.play(self.r.animate.set_value(0), run_time = 2)

        # self.play(self.time.animate.set_value(2))
        # self.wait()
        # self.play(self.time.animate.set_value(.5), run_time = 2)
       
        # self.play(Indicate(voltage_label))
        # self.play(Indicate(current_label))
        # self.play(Indicate(r_label))
        # self.play(Indicate(l_label))
        # self.play(Indicate(c_label))
        # self.wait()

        # graph = VGroup(axes, labels, r_label, l_label, c_label, frequency_label)
        # self.play(graph.animate.scale(.6).to_edge(DL))




