from tkinter import LEFT
from manim import *
import math
import numpy as np
from utils import * 
from math_equations import *

# Electric Circuit Simulator
class ParametricScene(Scene):
    r = ValueTracker(10)
    l = ValueTracker(0.2)
    c = ValueTracker(0.0000001)
    m = ValueTracker(0.2)

    emf = 0.1
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
            1 + (self.m.get_value() * -np.sin(
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
        Vr = self.i * self.r.get_value()
        lvar = self.get_varying_inductance(t)
        return Vc, self.i, Vr, lvar

    # Generates the plot Volatage by Time
    def generate_voltage_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_voltage_and_current(t)[0], [0, self.delta.get_value(), self.dt]).set_color(YELLOW)

    # Generates the plot Current by Time
    def generate_current_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_voltage_and_current(t)[1], [0, self.delta.get_value(), self.dt]).set_color(BLUE)

    def generate_resistor_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_voltage_and_current(t)[2], [0, self.delta.get_value(), self.dt]).set_color(RED)

    def generate_lvar_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_voltage_and_current(t)[3], [0, self.delta.get_value(), self.dt]).set_color(GREEN)

    # /// ORIENTERS ///

    # for inductor
    def set_orientation_l_plus(self, mobj, next):
        if self.get_voltage_and_current(0)[0] > 0:
            mobj.next_to(next, DR, buff=0)
        else:
            mobj.next_to(next, UR, buff=0)

    def set_orientation_l_minus(self, mobj, next):
        if self.get_voltage_and_current(0)[0] > 0:
            mobj.next_to(next, UR, buff=0)
        else:
            mobj.next_to(next, DR, buff=0)

    # for resistor
    def set_orientation_r_plus(self, mobj, next):
        if self.get_voltage_and_current(0)[1] > 0:
            mobj.next_to(next, UR, buff=0)
        else:
            mobj.next_to(next, UL, buff=0)

    def set_orientation_r_minus(self, mobj, next):
        if self.get_voltage_and_current(0)[1] > 0:
            mobj.next_to(next, UL, buff=0)
        else:
            mobj.next_to(next, UR, buff=0)

    # for capacitor
    def set_orientation_c_plus(self, mobj, next):
        if self.get_voltage_and_current(0)[0] > 0:
            mobj.next_to(next, UR)
        else:
            mobj.next_to(next, DR)

    def set_orientation_c_minus(self, mobj, next):
        if self.get_voltage_and_current(0)[0] > 0:
            mobj.next_to(next, DR)
        else:
            mobj.next_to(next, UR)

    # for arrows
    def set_orientation_l_arrow(self, mobj, next):
        if self.get_voltage_and_current(0)[1] > 0:
            mobj.put_start_and_end_on(start=DOWN, end=UP).next_to(next, RIGHT, buff=0.1).scale(0.4)
        else:
            mobj.put_start_and_end_on(start=UP, end=DOWN).next_to(next, RIGHT, buff=0.1).scale(0.4)

    def set_orientation_r_arrow(self, mobj, next):
        if self.get_voltage_and_current(0)[1] > 0:
            mobj.put_start_and_end_on(start=LEFT, end=RIGHT).next_to(next, DOWN).scale(0.4)
        else:
            mobj.put_start_and_end_on(start=RIGHT, end=LEFT).next_to(next, DOWN).scale(0.4)

    def set_orientation_c_arrow(self, mobj, next):
        if self.get_voltage_and_current(0)[1] > 0:
            mobj.put_start_and_end_on(start=UP, end=DOWN).next_to(next, LEFT).scale(0.4)
        else:
            mobj.put_start_and_end_on(start=DOWN, end=UP).next_to(next, LEFT).scale(0.4)

    # Constructs the Scene
    def construct(self):
#--------------------------------------CIRCUIT DIAGRAM------------------------------------------
       
        # Assign SVG
        circuit = SVGMobject("src/assets/circuit-20220323-1531.svg")
        rotor_disk = SVGMobject("src/assets/rotorDisk.svg")

        # Define Shapes
        ellipse_1 = Ellipse(width=2.0, height=4.0, color=GREEN).set_fill(GREEN, opacity=0.5)
        ellipse_2 = Ellipse(width=2.0, height=4.0, color=GREEN).set_fill(GREEN, opacity=0.5)
        torus_1 = Group(ellipse_1,ellipse_2).arrange(buff=.1).scale(0.4).next_to(circuit, LEFT)
        rect_1 = Rectangle(width=0.9, height=0.25).set_stroke(color=PURPLE).set_fill(PURPLE, opacity = 0.5)
        star_1 = Star(16, outer_radius=2, density=6, color=RED).scale(0.5).stretch_to_fit_height(1.2).set_fill(RED, opacity = 0.5)

        # Assign and arrange shapes
        magnetic_field = torus_1.next_to(circuit, LEFT)
        dielectric_field = rect_1.next_to(circuit, RIGHT + 1.8 * RIGHT)
        resistive_loss = star_1.next_to(circuit, UP + UP)

        circuit_diagram = Group(circuit.scale(4), magnetic_field, dielectric_field, resistive_loss)


#---GRAPHS AND LABELS--------------------------------------------------------------------------------------------------
       
        # Create axes and and add updater
        graph_scale = 0.6
        axes = Axes(
                x_range=[0, self.time.get_value().round(4), (self.time.get_value()/ 4).round(4)],
                y_range=[-self.y_range.get_value(), self.y_range.get_value(), 1],
                x_length=10,
                axis_config={"color": WHITE},    
                tips=False,
            ).scale(graph_scale).to_edge(DL, buff = 1.0)
        axes.add_updater(lambda mob: mob.become(Axes(
                x_range=[0, self.time.get_value().round(4), (self.time.get_value()/ 4).round(4)],
                y_range=[-self.y_range.get_value(), self.y_range.get_value(), 1],
                x_length=10,
                axis_config={"color": WHITE},      
                tips=False,
            ).scale(graph_scale).to_edge(DL, buff = 1.0)))
        # labels = axes.get_axis_labels('t', 'V,A')
        x_axis = axes.get_x_axis()
        x_axis.add_updater(lambda mob: mob.set(x_range = [0, self.time.get_value(), self.time.get_value()/4]))
        y_axis = axes.get_y_axis()
        y_axis.add_updater(lambda mob: mob.set(y_range = [0, self.y_range.get_value(), self.y_range.get_value()/4]))

        lvar_axes = Axes(
                x_range=[0, self.time.get_value().round(4), (self.time.get_value()/ 4).round(4)],
                y_range=[0, 0.3, 0.1],
                x_length=10,
                y_length=3,
                axis_config={"color": WHITE},       
                tips=False,
            ).scale(graph_scale).next_to(axes, UP)
        lvar_axes.add_updater(lambda mob: mob.become(Axes(
                x_range=[0, self.time.get_value().round(4), (self.time.get_value()/ 4).round(4)],
                y_range=[0, 0.3, 0.1],
                x_length=10,
                y_length=3,
                axis_config={"color": WHITE},      
                tips=False,
            ).scale(graph_scale).next_to(axes, UP)))
        lvar_x_axis = lvar_axes.get_x_axis()
        lvar_x_axis.add_updater(lambda mob: mob.set(x_range = [0, self.time.get_value(), .1]))

        # generate plot of Voltage and Current and Resistor and adds updater to be redrawn every frame
        voltage = self.generate_voltage_plot(axes)
        current = self.generate_current_plot(axes)
        resistor = self.generate_resistor_plot(axes)
        l_var = self.generate_lvar_plot(lvar_axes)
        voltage.add_updater(lambda mob: mob.become(self.generate_voltage_plot(axes)))
        current.add_updater(lambda mob: mob.become(self.generate_current_plot(axes)))
        resistor.add_updater(lambda mob: mob.become(self.generate_resistor_plot(axes)))
        l_var.add_updater(lambda mob: mob.become(self.generate_lvar_plot(lvar_axes)))
        
        # Create Resistance text
        r_text, r_number, r_units = r_label = VGroup(
            Text("R = ", font_size=18).set_color(RED),
            DecimalNumber(
                self.r.get_value(),
                num_decimal_places = 2,
                include_sign = True
            ).scale(graph_scale),
            Tex("$\Omega$", font_size=22).set_color(WHITE)
        )
        r_label.arrange(RIGHT).next_to(axes, DOWN)
        
        # Create Inductance text
        l_text, l_number, l_units = l_label = VGroup(
            Text("L = ", font_size=18).set_color(GREEN),
            DecimalNumber(
                self.l.get_value(),
                num_decimal_places = 6
            ).scale(graph_scale),
            Text("H", font_size=14, slant = ITALIC).set_color(WHITE)
        )
        l_label.arrange(RIGHT).next_to(r_label, LEFT)
        
        # Create Capacitance text
        c_text, c_number, c_units = c_label = VGroup(
            Text("C = ", font_size=18).set_color(PURPLE),
            DecimalNumber(
                self.c.get_value(),
                num_decimal_places = 7
            ).scale(graph_scale),
            Text("F", font_size=14, slant = ITALIC).set_color(WHITE)
        )
        c_label.arrange(RIGHT).next_to(r_label, RIGHT)

        # Create Para Frequency Text
        var_freq_text = MathTex(r"f_{para} = ", font_size=28).set_color(ORANGE)
        var_freq_number = DecimalNumber(
                    2*get_resonant_frequency(self.l.get_value(), self.c.get_value()),
                    num_decimal_places = 2
                ).scale(graph_scale)
        var_freq_units = MathTex(r"Hz", font_size=16)
        var_freq_label = VGroup(var_freq_text, var_freq_number, var_freq_units)
        var_freq_label.arrange(RIGHT).next_to(lvar_axes, UP).shift(0.3*DOWN)

        # Create Frequency Text
        frequency_text = MathTex(r"f_{res}=", font_size=28).set_color(GOLD_A)
        frequency_number = DecimalNumber(
                    get_resonant_frequency(self.l.get_value(), self.c.get_value()),
                    num_decimal_places = 2
                ).scale(graph_scale)
        frequency_units = MathTex(r"Hz", font_size=16)
        frequency_label = VGroup(frequency_text, frequency_number, frequency_units)
        frequency_label.arrange(RIGHT).next_to(var_freq_label, UP)

        # Create Voltage and Current Text
        va_label = VGroup(
            Text('CURRENT (I)', font_size=14).set_color(BLUE)
        ).next_to(r_label, UP)

        # add updaters to decimal numbers
        r_number.add_updater(lambda m: m.set_value(self.r.get_value()))
        l_number.add_updater(lambda m: m.set_value(self.l.get_value()))
        c_number.add_updater(lambda m: m.set_value(self.c.get_value()))
        frequency_number.add_updater(lambda m: m.set_value(get_resonant_frequency(self.l.get_value(), self.c.get_value())))

        # ARROWS and PLUS MINUS
        op_ratio_v = 0.1
        op_ratio_i = 100
        arrow_l = Arrow(start=DOWN, end=UP, color = BLUE, tip_length=0.2)
        arrow_c = Arrow(start=UP, end=DOWN, color = BLUE, tip_length=0.2)
        arrow_r = Arrow(start=LEFT, end=RIGHT, color = BLUE, tip_length=0.2)

        plus_l = Text("+", font_size=20).set_color(YELLOW).next_to(magnetic_field, DL, buff=0)
        minus_l = Text("-", font_size=40).set_color(YELLOW).next_to(magnetic_field, UL, buff=0)
        plus_c = Text("+", font_size=20).set_color(YELLOW).next_to(dielectric_field, UR)
        minus_c = Text("-", font_size=40).set_color(YELLOW).next_to(dielectric_field, DR)
        plus_r = Text("+", font_size=20).set_color(RED_B).next_to(resistive_loss, UL, buff=0)
        minus_r = Text("-", font_size=40).set_color(RED_B).next_to(resistive_loss, UR, buff=0)

        arrow_l.add_updater(lambda m: m.set_opacity(abs(self.i*1000)))
        arrow_l.add_updater(lambda m: self.set_orientation_l_arrow(m, magnetic_field))
        arrow_c.add_updater(lambda m: m.set_opacity(abs(self.i*1000)))
        arrow_c.add_updater(lambda m: self.set_orientation_c_arrow(m, dielectric_field))
        arrow_r.add_updater(lambda m: m.set_opacity(abs(self.i*1000)))
        arrow_r.add_updater(lambda m: self.set_orientation_r_arrow(m, resistive_loss))

        plus_l.add_updater(lambda m: m.set_opacity(abs(axes.i2gc(self.delta.get_value(),voltage)[1])*9))
        plus_l.add_updater(lambda m: self.set_orientation_l_plus(m, magnetic_field))
        minus_l.add_updater(lambda m: m.set_opacity(abs(axes.i2gc(self.delta.get_value(),voltage)[1])*9))
        minus_l.add_updater(lambda m: self.set_orientation_l_minus(m, magnetic_field))

        plus_c.add_updater(lambda m: m.set_opacity(abs(axes.i2gc(self.delta.get_value(),voltage)[1])*9))
        plus_c.add_updater(lambda m: self.set_orientation_c_plus(m, dielectric_field))
        minus_c.add_updater(lambda m: m.set_opacity(abs(axes.i2gc(self.delta.get_value(),voltage)[1])*9))
        minus_c.add_updater(lambda m: self.set_orientation_c_minus(m, dielectric_field))

        plus_r.add_updater(lambda m: m.set_opacity(abs(axes.i2gc(self.delta.get_value(),resistor)[1])*9))
        plus_r.add_updater(lambda m: self.set_orientation_r_plus(m, resistive_loss))
        minus_r.add_updater(lambda m: m.set_opacity(abs(axes.i2gc(self.delta.get_value(),resistor)[1])*9))
        minus_r.add_updater(lambda m: self.set_orientation_r_minus(m, resistive_loss))

        ellipse_1.add_updater(lambda m: m.set_opacity(abs(self.i*op_ratio_i)))
        ellipse_2.add_updater(lambda m: m.set_opacity(abs(self.i*op_ratio_i)))
        dielectric_field.add_updater(lambda m: m.set_opacity(abs(axes.i2gc(self.delta.get_value(),voltage)[1]*op_ratio_v)))
        star_1.add_updater(lambda m: m.set_opacity(abs(self.i*op_ratio_i)))

        slide_title = Text("Parametric Resonance", font_size=48).set_color(YELLOW).to_edge(UP,buff=0.5)
        para_title = Text("Series LCR Circuit", font_size=20).next_to(slide_title,DOWN)
        para_title.add_updater(lambda m: m.next_to(slide_title,DOWN))

        avg = MathTex(r"L",r"_{o}",font_size=28).set_color_by_tex("L",GREEN)
        l_avg = DashedVMobject(
            lvar_axes.plot(lambda t: self.l.get_value(), [0,self.time.get_value(),self.dt]),
            num_dashes = 30,
            dashed_ratio = 0.25
        ).set_opacity(0.8)
        l_low = DashedVMobject(
            lvar_axes.plot(lambda t: self.l.get_value() - (self.m.get_value() * self.l.get_value()), [0,self.time.get_value(),self.dt]),
            num_dashes = 30,
            dashed_ratio = 0.25
        ).set_color(GREEN_B).set_opacity(0.8)
        l_high = DashedVMobject(
            lvar_axes.plot(lambda t: self.l.get_value() + (self.m.get_value() * self.l.get_value()), [0,self.time.get_value(),self.dt]),
            num_dashes = 30,
            dashed_ratio = 0.25   
        ).set_color(GREEN_E).set_opacity(0.8)
        eng_group = VGroup(
            MathTex(r"W_{\Delta", r"L}",r"=",r"\frac{1}{2}",r"\Delta",r"L",r"i",r"^{2}").set_color_by_tex("L",GREEN).set_color_by_tex("i",BLUE),
            MathTex(r"W_{",r"R}",r"=",r"R",r"i",r"^{2}t").set_color_by_tex("R",RED).set_color_by_tex("i",BLUE)
        ).arrange(DOWN, buff = 0.5)
        eng_inequality = MathTex(r"\frac{1}{2}",r"\Delta",r"L",r"i",r"^{2}",r">",r"R",r"i",r"^{2}t").set_color_by_tex("L",GREEN).set_color_by_tex("R",RED).set_color_by_tex("i",BLUE)

#----SCENE-----------------------------------------------------------------------------------------------------------------

        # add objects and animations
        self.add(slide_title,para_title).remove(axes,lvar_axes)
        self.wait()
        self.play(slide_title.animate.to_edge(UR).scale(0.75).shift(RIGHT))
        self.wait()
        self.play(FadeIn(axes, lvar_axes))
        self.wait()
        self.remove(magnetic_field,dielectric_field,resistive_loss).play(FadeIn(circuit_diagram.scale(0.6).to_edge(DR).shift(0.5*RIGHT+0.5*DOWN)))
        self.wait()
        self.play(FadeIn(rotor_disk.scale(0.75).next_to(circuit,LEFT).shift(1.9*RIGHT)))
        self.wait()
        self.play(Rotate(rotor_disk, angle=2*PI, rate_func=linear, run_time=4))
        self.wait()
        self.play(
            FadeIn(
                voltage, resistor, current, l_var, 
                r_label, l_label, c_label, va_label,
                l_avg, l_high, l_low, avg.next_to(l_avg,LEFT)
            )
        )
        self.wait()
        self.play(FadeIn(eng_group.next_to(para_title,DOWN,buff=0.5).scale(0.75)))
        self.wait()
        self.play(FadeOut(eng_group), FadeIn(eng_inequality.move_to(eng_group.get_center()).scale(0.75)))
        self.wait()
        self.add(arrow_l, arrow_c, arrow_r, plus_l, plus_c, plus_r, minus_l, minus_c, minus_r)
        self.play(
            Rotate(rotor_disk, angle=7*PI, rate_func=linear, run_time=10),
            self.delta.animate.set_value(self.time.get_value()), run_time = 10, rate_func = linear
        )
        self.wait()

        self.play(self.time.animate.set_value(0.04), run_time = 4)
        self.wait()
        self.play(
            Rotate(rotor_disk, angle=21*PI, rate_func=linear, run_time=15),
            self.delta.animate.set_value(self.time.get_value()), run_time = 20, rate_func = linear
        )
        self.wait()


#---Backlog Animations----------------------------------------------------------------------------------------

        # self.play(self.l.animate.set_value(0.5), run_time = 2)
        # self.play(self.c.animate.set_value(0.002), run_time = 2)
        # self.play(self.m.animate.set_value(0.5), run_time = 2)


        # self.play(self.l.animate.set_value(0.2), run_time = 1)
        # self.play(self.c.animate.set_value(0.0001), run_time = 1)
        # self.play(self.r.animate.set_value(0), run_time = 2)

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




