from manim import *
import math
import numpy as np
from utils import * 

# Electric Circuit Simulator
class SquareInd(Scene):
    r = ValueTracker(10)
    l = ValueTracker(0.05)
    c = ValueTracker(0.0000001)
    m = ValueTracker(0.2)

    emf = 0.1
    i = 0
    q = c.get_value() * emf

    time = ValueTracker(0.00044)
    dt = .001 * time.get_value()
    delta = ValueTracker(0)

#---Functions---

    def get_varying_inductance(self, t):
        l_var = (
            self.l.get_value() * (
            1 + (self.m.get_value() * -np.sin(
            2 * PI * get_resonant_frequency(self.l.get_value(), self.c.get_value()) * 2 * t
            )))
        )
        return l_var

    def get_square_inductance(self, t):
        if(self.get_varying_inductance(t) > self.l.get_value()):
            l_square = self.l.get_value() + (self.l.get_value() * self.m.get_value())
        else:
            l_square = self.l.get_value() - (self.l.get_value() * self.m.get_value())
        return l_square

    # Returns voltage and current as an array at time t
    def get_voltage_and_current(self, t):
        alpha = (self.q / (self.get_square_inductance(t) * self.c.get_value())) - (self.i * self.r.get_value() / self.get_square_inductance(t))

        self.i = self.i + (alpha * self.dt)
        self.q = self.q - (self.i * self.dt)

        Vc = self.q / self.c.get_value()
        lvar = self.get_square_inductance(t)
        return Vc, self.i, lvar
    
    # Returns voltage and current as an array at time t
    def get_normal_voltage_and_current(self, t):
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
        return axes.plot(lambda t: self.get_voltage_and_current(t)[0], [0, self.delta.get_value(), self.dt]).set_color(YELLOW)

    # Generates the plot Current by Time
    def generate_current_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_voltage_and_current(t)[1], [0, self.delta.get_value(), self.dt]).set_color(BLUE)

    def generate_lvar_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_voltage_and_current(t)[2], [0, self.delta.get_value(), self.dt]).set_color(GREEN)
   
    # Generates the plot Volatage by Time
    def generate_normal_voltage_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_normal_voltage_and_current(t)[0], [0, self.delta.get_value(), self.dt]).set_color(YELLOW)

    # Generates the plot Current by Time
    def generate_normal_current_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_normal_voltage_and_current(t)[1], [0, self.delta.get_value(), self.dt]).set_color(BLUE)

    def generate_normal_lvar_plot(self, axes):
        self.q = self.c.get_value() * self.emf
        self.i = 0
        return axes.plot(lambda t: self.get_normal_voltage_and_current(t)[2], [0, self.delta.get_value(), self.dt]).set_color(GREEN)
   
    # /// ORIENTERS ///

    # for inductor
    def set_orientation_l_plus(self, mobj, next):
        if self.get_voltage_and_current(0)[0] > 0:
            mobj.next_to(next, DL, buff=0)
        else:
            mobj.next_to(next, UL, buff=0)

    def set_orientation_l_minus(self, mobj, next):
        if self.get_voltage_and_current(0)[0] > 0:
            mobj.next_to(next, UL, buff=0)
        else:
            mobj.next_to(next, DL, buff=0)

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

    def set_orientation_c_arrow(self, mobj, next):
        if self.get_voltage_and_current(0)[1] > 0:
            mobj.put_start_and_end_on(start=UP, end=DOWN).next_to(next, LEFT).scale(0.4)
        else:
            mobj.put_start_and_end_on(start=DOWN, end=UP).next_to(next, LEFT).scale(0.4)

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

#---Axes and Titles---
        axes = Axes(
                x_range=[0, self.time.get_value()+0.00001,self.time.get_value()],
                y_range=[-0.2, 0.2, 0.1],
                x_length=8,
                y_length=3,
                axis_config={"color": WHITE},
                tips=False,
        )
        axes_2 = Axes(
            x_range=[0, self.time.get_value()+0.00001,self.time.get_value()],
            y_range=[-0.0005, 0.0005, 0.00025],
            x_length=8,
            y_length=3,
            axis_config={"color": WHITE},
            tips=False,
        )
        axes_ind = Axes(
            x_range=[0, self.time.get_value()+0.00001,self.time.get_value()],
            y_range=[0.025, 0.075, 0.05],
            x_length=8,
            y_length=2,
            axis_config={"color": WHITE},
            tips=False,
        )

        title = Text("Parametric Resonance").set_color(YELLOW).to_edge(UP)

#---Math---

        energy_eqs = VGroup(
            MathTex(r"W",r"_{",r"L}",r"=",r"\frac{1}{2}",r"\cdot",r"L",r"_{-\Delta}",r"\cdot",r"i",r"^{2}", font_size=40),
            MathTex(r"W",r"_{",r"C}",r"=",r"\frac{1}{2}",r"\cdot",r"C",r"_{o}",r"\cdot",r"e",r"^{2}", font_size=40),
        ).arrange(DOWN,buff=0.5)
        frequency_eqs = VGroup(
            MathTex(r"\omega",r"_{o}",r"=",r"2\pi",r"\frac{1}{",r"\sqrt{",r"L",r"_{o}",r"C}}", font_size=40).set_color_by_tex("L",GREEN).set_color_by_tex("C",PURPLE),
            MathTex(r"\omega",r"_{para}",r"=",r"2",r"\omega",r"_{o}", font_size=40)
        ).arrange(DOWN,buff=0.5)
        energy_eqs[0].set_color_by_tex("L",GREEN_B).set_color_by_tex("-\Delta",GREEN_B).set_color_by_tex("i",BLUE)
        energy_eqs[1].set_color_by_tex("C",PURPLE).set_color_by_tex("e",YELLOW)        
        circle_l = Circle(radius = 0.5)
        circle_c = Circle(radius = 0.5)
        para_energy_eqs = VGroup(
            MathTex(r"W",r"_{",r"L}",r"=",r"\frac{1}{2}",r"\cdot",r"L",r"_{\Delta}",r"\cdot",r"i",r"^{2}", font_size=40),
            MathTex(r"W",r"_{",r"C}",r"=",r"\frac{1}{2}",r"\cdot",r"C",r"_{o}",r"\cdot",r"e",r"^{2}", font_size=40),
        ).arrange(DOWN,buff=0.5)
        para_energy_eqs[0].set_color_by_tex("L",GREEN_E).set_color_by_tex("\Delta",GREEN_E).set_color_by_tex("i",BLUE) 
        power_eqs = VGroup(
            MathTex(r"P",r"=",r"L",r"\cdot",r"i",r"\cdot",r"\frac{di}{dt}", font_size=32),
            MathTex(r"P=L\cdot \frac{i^{2}\omega}{2}  sin(2\omega t)-Lm\cdot \frac{i^{2}\omega}{2}  sin^{2}(2\omega t)\cdot", font_size=32)
        )
        low = MathTex(r"L",r"_{-\Delta}",font_size=28).set_color(GREEN_B)
        avg = MathTex(r"L",r"_{o}",font_size=28).set_color_by_tex("L",GREEN)
        high = MathTex(r"L",r"_{\Delta}",font_size=28).set_color(GREEN_E)

#---Plotting and Updaters

        voltage = self.generate_voltage_plot(axes)
        current = self.generate_current_plot(axes_2)
        l_varry = self.generate_lvar_plot(axes_ind)
        voltage.add_updater(lambda mob: mob.become(self.generate_voltage_plot(axes)))
        current.add_updater(lambda mob: mob.become(self.generate_current_plot(axes_2)))
        l_varry.add_updater(lambda mob: mob.become(self.generate_lvar_plot(axes_ind)))

        normal_voltage = self.generate_normal_voltage_plot(axes)
        normal_current = self.generate_normal_current_plot(axes_2)
        normal_l_varry = self.generate_normal_lvar_plot(axes_ind)
        normal_voltage.add_updater(lambda mob: mob.become(self.generate_normal_voltage_plot(axes)))
        normal_current.add_updater(lambda mob: mob.become(self.generate_normal_current_plot(axes_2)))
        normal_l_varry.add_updater(lambda mob: mob.become(self.generate_normal_lvar_plot(axes_ind)))
        
        circle_l.add_updater(lambda mob: mob.set_opacity())
        circle_c.add_updater(lambda mob: mob.set_opacity())

# ---Dots---
        inductance_dot = Dot(axes_ind.i2gp(self.delta.get_value(), l_varry))
        current_dot = Dot(axes_2.i2gp(self.delta.get_value(), current))
        voltage_dot = Dot(axes.i2gp(self.delta.get_value(), voltage))

        inductance_dot.add_updater(lambda d: d.move_to(axes_ind.i2gp(self.delta.get_value(), l_varry))).set_color(GREEN)
        current_dot.add_updater(lambda d: d.move_to(axes_2.i2gp(self.delta.get_value(), current))).set_color(BLUE)
        voltage_dot.add_updater(lambda d: d.move_to(axes.i2gp(self.delta.get_value(), voltage))).set_color(YELLOW)

#---Scene---
        self.add(title)
        self.wait()
        self.play(
            FadeIn(
                axes_ind.next_to(title,DOWN,buff=0.5).shift(2.4*LEFT), 
                axes.next_to(axes_ind,DOWN), 
                axes_2.next_to(axes_ind,DOWN), 
                voltage, current, l_varry,
                inductance_dot, current_dot, voltage_dot
            )
        )
        self.wait()
        self.remove(magnetic_field, dielectric_field)
        self.play(FadeIn(circuit_diagram2.scale(0.6).next_to(axes_2,RIGHT).shift(0.4*LEFT)))
        self.wait()
        energy_eqs.next_to(circuit_diagram2,UP).shift(0.8*DOWN)
        para_energy_eqs.next_to(circuit_diagram2,UP).shift(0.8*DOWN)
        self.play(FadeIn(energy_eqs[0]))
        self.wait()
        self.play(FadeIn(energy_eqs[1]))
        self.wait()
        self.play(FadeOut(magnetic_field, dielectric_field))
        self.wait()
        
        # ARROWS and PLUS MINUS
        arrow_l = Arrow(start=DOWN, end=UP, color = BLUE, tip_length=0.2)
        arrow_c = Arrow(start=UP, end=DOWN, color = BLUE, tip_length=0.2)

        plus_l = Text("+", font_size=20).set_color(YELLOW).next_to(magnetic_field, DL, buff=0)
        minus_l = Text("-", font_size=40).set_color(YELLOW).next_to(magnetic_field, UL, buff=0)
        plus_c = Text("+", font_size=20).set_color(YELLOW).next_to(dielectric_field, UR)
        minus_c = Text("-", font_size=40).set_color(YELLOW).next_to(dielectric_field, DR)

        arrow_l.add_updater(lambda m: m.set_opacity(abs(self.i*4000)))
        arrow_l.add_updater(lambda m: self.set_orientation_l_arrow(m, magnetic_field))
        arrow_c.add_updater(lambda m: m.set_opacity(abs(self.i*4000)))
        arrow_c.add_updater(lambda m: self.set_orientation_c_arrow(m, dielectric_field))

        plus_l.add_updater(lambda m: m.set_opacity(abs(axes.i2gc(self.delta.get_value(),voltage)[1])*9))
        plus_l.add_updater(lambda m: self.set_orientation_l_plus(m, magnetic_field))
        minus_l.add_updater(lambda m: m.set_opacity(abs(axes.i2gc(self.delta.get_value(),voltage)[1])*9))
        minus_l.add_updater(lambda m: self.set_orientation_l_minus(m, magnetic_field))

        plus_c.add_updater(lambda m: m.set_opacity(abs(axes.i2gc(self.delta.get_value(),voltage)[1])*9))
        plus_c.add_updater(lambda m: self.set_orientation_c_plus(m, dielectric_field))
        minus_c.add_updater(lambda m: m.set_opacity(abs(axes.i2gc(self.delta.get_value(),voltage)[1])*9))
        minus_c.add_updater(lambda m: self.set_orientation_c_minus(m, dielectric_field))


        ellipse_1.add_updater(lambda m: m.set_opacity(abs(self.i*4000)))
        ellipse_2.add_updater(lambda m: m.set_opacity(abs(self.i*4000)))
        dielectric_field.add_updater(lambda m: m.set_opacity(abs(axes.i2gc(self.delta.get_value(),voltage)[1])*9))

        l_avg = DashedVMobject(
            axes_ind.plot(lambda t: self.l.get_value(), [0,self.time.get_value(),self.dt]),
            num_dashes = 30,
            dashed_ratio = 0.25
        ).set_opacity(0.8)
        l_low = DashedVMobject(
            axes_ind.plot(lambda t: self.l.get_value() - (self.m.get_value() * self.l.get_value()), [0,self.time.get_value(),self.dt]),
            num_dashes = 30,
            dashed_ratio = 0.25
        ).set_color(GREEN_B).set_opacity(0.8)
        l_high = DashedVMobject(
            axes_ind.plot(lambda t: self.l.get_value() + (self.m.get_value() * self.l.get_value()), [0,self.time.get_value(),self.dt]),
            num_dashes = 30,
            dashed_ratio = 0.25   
        ).set_color(GREEN_E).set_opacity(0.8)

        self.wait()
        self.play(FadeIn(l_low), FadeIn(low.next_to(l_low,RIGHT)))
        self.wait()

        self.add(magnetic_field, dielectric_field)
        self.add(arrow_l,arrow_c,plus_l,minus_l,plus_c,minus_c)

        self.play(self.delta.animate.set_value(0.0001),run_time=10,rate_func=linear)
        self.wait()
        self.play(FadeIn(l_high), FadeIn(high.next_to(l_high,RIGHT)))
        self.wait()
        self.play(self.delta.animate.set_value(0.000113),run_time=2,rate_func=linear)
        self.wait()
        self.play(TransformMatchingTex(energy_eqs[0], para_energy_eqs[0]))
        self.wait()
        self.play(Indicate(current_dot),Indicate(para_energy_eqs[0][9]))
        self.wait()
        self.play(Indicate(inductance_dot), Indicate(para_energy_eqs[0][6]))
        self.wait()
        self.play(Indicate(para_energy_eqs[0][0]))
        self.wait()

        self.play(self.delta.animate.set_value(0.00022),run_time=10,rate_func=linear)
        self.wait()
        self.play(Indicate(voltage_dot), Indicate(para_energy_eqs[1][0]))
        self.wait()
        self.play(self.delta.animate.set_value(0.000225),run_time=2,rate_func=linear)
        self.wait()
        self.play(TransformMatchingTex(para_energy_eqs[0], energy_eqs[0]))
        self.wait()
        self.play(Indicate(inductance_dot), Indicate(energy_eqs[0][6]))
        self.wait()

        self.play(self.delta.animate.set_value(0.00032),run_time=10,rate_func=linear)
        self.wait()
        self.play(TransformMatchingTex(energy_eqs[0], para_energy_eqs[0]))
        self.wait()
        self.play(self.delta.animate.set_value(self.time.get_value()),run_time=5,rate_func=linear)
        self.wait()
        self.play(FadeOut(inductance_dot, current_dot, voltage_dot))
        self.wait()
        self.play(FadeOut(energy_eqs[0],energy_eqs[1],para_energy_eqs))
        self.wait()
        self.play(FadeIn(l_avg), FadeIn(avg.next_to(l_avg,RIGHT)))
        self.wait()
        self.play(FadeIn(frequency_eqs.next_to(circuit_diagram2,UP).shift(0.5*DOWN)))
        self.wait()
        self.play(
            ReplacementTransform(voltage, normal_voltage),
            ReplacementTransform(current, normal_current),
            ReplacementTransform(l_varry, normal_l_varry)
        )
        self.wait()