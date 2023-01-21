from manim import *
import math
import numpy as np
from utils import * 
from math_equations import *

class LCScene(Scene):

    R = ValueTracker(0)
    L = ValueTracker(0.02)
    C = ValueTracker(0.0001)

    EMF = 5
    I = 0
    Q = C.get_value() * EMF

    time = ValueTracker(0.04)
    dt = time.get_value() / 1000
    delta = ValueTracker(0)

    # Returns the Voltage and Current at frame
    def get_voltage_and_current(self):
        alpha = (self.Q / (self.L.get_value() * self.C.get_value())) - (self.I * self.R.get_value() / self.L.get_value())

        self.I = self.I + (alpha * self.dt)
        self.Q = self.Q - (self.I * self.dt)

        Vc = self.Q / self.C.get_value()
        Vr = self.I * self.R.get_value()
        Vl = -Vc - Vr
        return Vc, -self.I, Vr, Vl

    def generate_loss_plot(self, axes):
        self.Q = self.C.get_value() * self.EMF
        self.I = 0
        return axes.plot(lambda t: self.get_voltage_and_current()[0] * (1 - np.exp((self.R.get_value() * t) / self.L.get_value()))).set_color(GRAY_B)

    # Generates the plot Volatage by Time
    def generate_voltage_plot_c(self, axes):
        self.Q = self.C.get_value() * self.EMF
        self.I = 0
        return axes.plot(lambda t: self.get_voltage_and_current()[0], [0, self.delta.get_value(), self.dt]).set_color(YELLOW)

    # Generates the plot Current by Time
    def generate_current_plot(self, axes):
        self.Q = self.C.get_value() * self.EMF
        self.I = 0
        return axes.plot(lambda t: self.get_voltage_and_current()[1], [0, self.delta.get_value(), self.dt]).set_color(BLUE)

    def generate_voltage_plot_r(self, axes):
        self.Q = self.C.get_value() * self.EMF
        self.I = 0
        return axes.plot(lambda t: self.get_voltage_and_current()[2], [0, self.delta.get_value(), self.dt]).set_color(RED)

    def generate_voltage_plot_l(self, axes):
        self.Q = self.C.get_value() * self.EMF
        self.I = 0
        return axes.plot(lambda t: self.get_voltage_and_current()[3], [0, self.delta.get_value(), self.dt]).set_color(GOLD)

    # /// ORIENTERS ///

    # for inductor
    def set_orientation_l_plus(self, mobj, next):
        if self.get_voltage_and_current()[0] > 0:
            mobj.next_to(next, DL, buff=0)
        else:
            mobj.next_to(next, UL, buff=0)

    def set_orientation_l_minus(self, mobj, next):
        if self.get_voltage_and_current()[0] > 0:
            mobj.next_to(next, UL, buff=0)
        else:
            mobj.next_to(next, DL, buff=0)

    # for capacitor
    def set_orientation_c_plus(self, mobj, next):
        if self.get_voltage_and_current()[0] > 0:
            mobj.next_to(next, UR)
        else:
            mobj.next_to(next, DR)

    def set_orientation_c_minus(self, mobj, next):
        if self.get_voltage_and_current()[0] > 0:
            mobj.next_to(next, DR)
        else:
            mobj.next_to(next, UR)

    # for arrows
    def set_orientation_l_arrow(self, mobj, next):
        if self.get_voltage_and_current()[1] > 0:
            mobj.put_start_and_end_on(start=DOWN, end=UP).next_to(next, RIGHT, buff=0.1).scale(0.4)
        else:
            mobj.put_start_and_end_on(start=UP, end=DOWN).next_to(next, RIGHT, buff=0.1).scale(0.4)

    def set_orientation_c_arrow(self, mobj, next):
        if self.get_voltage_and_current()[1] > 0:
            mobj.put_start_and_end_on(start=UP, end=DOWN).next_to(next, LEFT).scale(0.4)
        else:
            mobj.put_start_and_end_on(start=DOWN, end=UP).next_to(next, LEFT).scale(0.4)

    # Constructs the Scene
    def construct(self):

#--------------------------------------CIRCUIT DIAGRAM------------------------------------------
       
        # Assign SVG
        circuit2 = SVGMobject("src/assets/circuit2.svg")

        # Define Shapes
        ellipse_1 = Ellipse(width=2.0, height=4.0, color=GREEN).set_fill(GREEN, opacity=0.5)
        ellipse_2 = Ellipse(width=2.0, height=4.0, color=GREEN).set_fill(GREEN, opacity=0.5)
        torus_1 = Group(ellipse_1,ellipse_2).arrange(buff=.1).scale(0.4).next_to(circuit2, LEFT)
        rect_1 = Rectangle(width=0.9, height=0.25).set_stroke(color=PURPLE).set_fill(PURPLE, opacity = 0.5)

        # Assign and arrange shapes
        magnetic_field = torus_1.next_to(circuit2, LEFT)
        dielectric_field = rect_1.next_to(circuit2, RIGHT + 1.8 * RIGHT)

        circuit_diagram2 = Group(circuit2.scale(4), magnetic_field, dielectric_field)


#-------------------------------------OSCILOSCOPE GRAPH-----------------------------------------

        # Create Graph
        graph_scale = 0.6
        axes = Axes(
                x_range=[0, self.time.get_value(), .1],
                y_range=[-6, 6, 1],
                x_length=10,
                y_length=8,
                axis_config={"color": WHITE},
                x_axis_config={"numbers_to_include": np.arange(0, self.time.get_value().round(1), .1)},
                y_axis_config={"numbers_to_include": np.arange(-6.01, 6.01, 1)},        
                tips=False,
            ).scale(graph_scale).to_edge(DL, buff = 1.0)
        axes.add_updater(lambda mob: mob.become(Axes(
                x_range=[0, self.time.get_value(), .1],
                y_range=[-6, 6, 1],
                x_length=10,
                y_length=8,
                axis_config={"color": WHITE},
                x_axis_config={"numbers_to_include": np.arange(0, self.time.get_value().round(1), .1)},
                y_axis_config={"numbers_to_include": np.arange(-6.01, 6.01, 1)},          
                tips=False,
            ).scale(graph_scale).to_edge(DL, buff = 1.0)))
        # axes_labels = axes.get_axis_labels('t', 'V,A').scale(graph_scale)

        x_axis = axes.get_x_axis()
        x_axis.add_updater(lambda mob: mob.set(x_range = [0, self.time.get_value(), .1]))

        # Generate plot of Voltage and Current and adds updater to be redrawn every frame
        voltage = self.generate_voltage_plot_c(axes)
        current = self.generate_current_plot(axes)
        l_voltage = self.generate_voltage_plot_l(axes)
        loss = self.generate_loss_plot(axes)
        voltage.add_updater(lambda mob: mob.become(self.generate_voltage_plot_c(axes)))
        current.add_updater(lambda mob: mob.become(self.generate_current_plot(axes)))
        l_voltage.add_updater(lambda mob: mob.become(self.generate_voltage_plot_l(axes)))
        loss.add_updater(lambda mob: mob.become(self.generate_loss_plot(axes)))


#-------------------------------------------TEXT-----------------------------------------------

        # Create Inductance text
        l_text, l_number, l_units = l_label = VGroup(
            Text("L = ", font_size=18).set_color(GREEN),
            DecimalNumber(
                self.L.get_value(),
                num_decimal_places = 2
            ).scale(graph_scale),
            Text("H", font_size=14, slant = ITALIC).set_color(WHITE)
        ).arrange(RIGHT)
        # Create Capacitance text
        c_text, c_number, c_units = c_label = VGroup(
            Text("C = ", font_size=18).set_color(PURPLE),
            DecimalNumber(
                self.C.get_value(),
                num_decimal_places = 4
            ).scale(graph_scale),
            Text("F", font_size=14, slant = ITALIC).set_color(WHITE)
        ).arrange(RIGHT)
        current_eq = MathTex(r"I",r"=",r"\frac{Q}{t}", font_size=32).set_color_by_tex("I", BLUE)
        lc_label = VGroup(l_label, c_label).arrange(RIGHT).next_to(axes, DOWN)
        
        # Create Frequency Text
        frequency_text = Text("Frequency = ", font_size=20).set_color(ORANGE)
        frequency_number = DecimalNumber(
                    get_resonant_frequency(self.L.get_value(), self.C.get_value()),
                    num_decimal_places = 2
                ).scale(graph_scale)
        frequency_units = Text("Hz", font_size=16, slant = ITALIC)
        frequency_label = VGroup(frequency_text, frequency_number, frequency_units)
        frequency_label.arrange(RIGHT).scale(1.3).next_to(axes, UP)

        # Create Voltage and Current Text
        va_label = VGroup(
            Text('CURRENT (I)', font_size=16).set_color(BLUE)
        ).next_to(lc_label, UP)

        # add updaters to decimal numbers
        l_number.add_updater(lambda m: m.set_value(self.L.get_value()))
        c_number.add_updater(lambda m: m.set_value(self.C.get_value()))
        frequency_number.add_updater(lambda m: m.set_value(get_resonant_frequency(self.L.get_value(), self.C.get_value())))

        slide_title = Text("Electric Harmonic Oscillator", font_size=48).to_edge(UP, buff=0.5).set_color(BLUE)
        electric_title = Text("Resonant Electric Circuit (LCR)", font_size=32).next_to(slide_title,DOWN)

#-------------------------------------CREATING THE SCENE---------------------------------------

        # add objects and animations
        self.add(slide_title)
        self.play(Write(electric_title))
        self.wait()
        self.play(FadeIn(circuit_diagram2.shift(DOWN)))
        self.wait()
        self.play(circuit_diagram2.animate.scale(0.6).to_edge(DR))
        self.wait()
        
        volt_eqs = VGroup(
            voltage_eqs[0].set_color_by_tex("L", GREEN).set_color_by_tex("C", PURPLE).set_color_by_tex("R", RED).set_color_by_tex("V", GOLD),
            voltage_eqs[2].set_color_by_tex("L", GREEN).set_color_by_tex("C", PURPLE).set_color_by_tex("R", RED).set_color_by_tex("V", YELLOW)
        ).arrange(RIGHT, buff=0.5)
        self.play(FadeIn(volt_eqs.next_to(circuit2, UP).shift(0.7*DOWN)), FadeIn(current_eq.next_to(circuit2,DOWN).shift(UP*0.85)))
        self.wait()

        blackbox = Rectangle(color=BLACK, width=1, height=1).set_fill(BLACK, opacity=1.0)
        self.play(FadeOut(magnetic_field), FadeIn(blackbox.next_to(circuit2, DOWN).shift(2*UP)))
        self.wait()

        # ARROWS and PLUS MINUS
        arrow_l = Arrow(start=DOWN, end=UP, color = BLUE, tip_length=0.2)
        arrow_c = Arrow(start=UP, end=DOWN, color = BLUE, tip_length=0.2)

        plus_l = Text("+", font_size=20).set_color(GOLD).next_to(magnetic_field, DL, buff=0)
        minus_l = Text("-", font_size=40).set_color(GOLD).next_to(magnetic_field, UL, buff=0)
        plus_c = Text("+", font_size=20).set_color(YELLOW).next_to(dielectric_field, UR)
        minus_c = Text("-", font_size=40).set_color(YELLOW).next_to(dielectric_field, DR)

        arrow_l.add_updater(lambda m: m.set_opacity(abs(self.get_voltage_and_current()[1])*2))
        arrow_l.add_updater(lambda m: self.set_orientation_l_arrow(m, magnetic_field))
        arrow_c.add_updater(lambda m: m.set_opacity(abs(self.get_voltage_and_current()[1])*2))
        arrow_c.add_updater(lambda m: self.set_orientation_c_arrow(m, dielectric_field))

        plus_l.add_updater(lambda m: m.set_opacity(abs(self.get_voltage_and_current()[0])/5))
        plus_l.add_updater(lambda m: self.set_orientation_l_plus(m, magnetic_field))
        minus_l.add_updater(lambda m: m.set_opacity(abs(self.get_voltage_and_current()[0])/5))
        minus_l.add_updater(lambda m: self.set_orientation_l_minus(m, magnetic_field))

        plus_c.add_updater(lambda m: m.set_opacity(abs(self.get_voltage_and_current()[0])/5))
        plus_c.add_updater(lambda m: self.set_orientation_c_plus(m, dielectric_field))
        minus_c.add_updater(lambda m: m.set_opacity(abs(self.get_voltage_and_current()[0])/5))
        minus_c.add_updater(lambda m: self.set_orientation_c_minus(m, dielectric_field))

        # Graph Animation
        self.wait()
        self.play(FadeIn(lc_label, va_label, 
                         axes, voltage, current, l_voltage), run_time = 0.5)
        self.wait()
        ellipse_1.add_updater(lambda m: m.set_opacity(abs(self.I*2)))
        ellipse_2.add_updater(lambda m: m.set_opacity(abs(self.I*2)))
        dielectric_field.add_updater(lambda m: m.set_opacity(abs(self.get_voltage_and_current()[0])/5))

        self.wait()
        self.remove(blackbox)
        self.add(magnetic_field, arrow_l, arrow_c, plus_l, plus_c, minus_l, minus_c)
        self.play(self.delta.animate.set_value(self.time.get_value()), run_time = 12, rate_func = linear)
        self.wait()
