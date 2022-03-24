from manim import *
import math
import numpy as np

# Electric Circuit Simulator
class RLC(Scene):
    R = ValueTracker(0)
    L = ValueTracker(0.2)
    C = ValueTracker(0.0001)

    EMF = 5
    I = 0
    Q = C.get_value() * EMF

    dt = .001
    time = ValueTracker(1)

    # Returns the Voltage at frame
    def get_voltage_and_current(self, t):
        alpha = (self.Q / (self.L.get_value() * self.C.get_value())) - (self.I * self.R.get_value() / self.L.get_value())

        self.I = self.I + (alpha * ((self.dt + t)-t))
        self.Q = self.Q - (self.I * ((self.dt + t)-t))

        Vc = self.Q / self.C.get_value()
        return Vc, self.I
    
    def get_resonant_frequency(self):
        frequency = 1 / ((self.L.get_value() * self.C.get_value()) ** 0.5)
        resonant_frequency = frequency / (2 * PI)
        return resonant_frequency


    # Generates the plot Volatage by Time
    def generate_voltage_plot(self, axes):
        self.Q = self.C.get_value() * self.EMF
        return axes.plot(lambda t: self.get_voltage_and_current(t)[0], [0, 1 / self.time.get_value(), self.dt]).set_color(YELLOW)

    def generate_current_plot(self, axes):
        self.Q = self.C.get_value() * self.EMF
        return axes.plot(lambda t: self.get_voltage_and_current(t)[1], [0, 1 / self.time.get_value(), self.dt]).set_color(BLUE)

    # I am the CONTRUCTOR!
    def construct(self):
        axes = always_redraw(lambda: Axes(
                x_range=[0, self.time.get_value().round(2), .1],
                y_range=[-6, 6, 1],
                x_length=10,
                axis_config={"color": GREEN},
                x_axis_config={"numbers_to_include": np.arange(0, self.time.get_value().round(2), .1)},
                y_axis_config={"numbers_to_include": np.arange(-6.01, 6.01, 1)},          
                tips=False,
            )
        )

        # Adding voltage to the scene will call generate plot every frame
        voltage = always_redraw(lambda: self.generate_voltage_plot(axes))
        current = always_redraw(lambda: self.generate_current_plot(axes))

        #Create Text
        r_text, r_number, r_units = r_label = VGroup(
            Text("R = ", font_size=36).set_color(RED),
            DecimalNumber(
                self.R.get_value(),
                num_decimal_places = 2,
                include_sign = True
            ),
            Tex("$\Omega$", font_size=44).set_color(WHITE)
        )
        r_label.arrange(RIGHT).next_to(axes, DOWN)

        l_text, l_number, l_units = l_label = VGroup(
            Text("L = ", font_size=36).set_color(GREEN),
            DecimalNumber(
                self.L.get_value(),
                num_decimal_places = 6
            ),
            Text("H", font_size=28, slant = ITALIC).set_color(WHITE)
        )
        l_label.arrange(RIGHT).next_to(r_label, LEFT)

        c_text, c_number, c_units = c_label = VGroup(
            Text("C = ", font_size=36).set_color(PURPLE),
            DecimalNumber(
                self.C.get_value(),
                num_decimal_places = 6
            ),
            Text("F", font_size=28, slant = ITALIC).set_color(WHITE)
        )
        c_label.arrange(RIGHT).next_to(r_label, RIGHT)

        
        frequency_text = Text("Frequency = ", font_size=36).set_color(ORANGE)
        frequency_number = DecimalNumber(
                    self.get_resonant_frequency(),
                    num_decimal_places = 2
                )
        frequency_units = Text("Hz", font_size=28, slant = ITALIC)

        frequency_label = VGroup(frequency_text, frequency_number, frequency_units)
        frequency_label.arrange(RIGHT).next_to(axes, UP)


        #add updaters to decimal numbers
        r_number.add_updater(lambda m: m.set_value(self.R.get_value()))
        l_number.add_updater(lambda m: m.set_value(self.L.get_value()))
        c_number.add_updater(lambda m: m.set_value(self.C.get_value()))
        frequency_number.add_updater(lambda m: m.set_value(self.get_resonant_frequency()))
        

        labels = axes.get_axis_labels('t', 'V, I').set_color(WHITE)

        #add objects and animations
        self.add(r_label, l_label, c_label, frequency_label)
        self.add(axes, labels)
        self.add(voltage, current)
        # self.play(Create(voltage), run_time = 2)
        # self.play(Create(current), run_time = 2)
        self.wait()
        self.play(self.R.animate.set_value(6), run_time = 3)
        self.play(self.L.animate.set_value(0.5), run_time = 2)
        self.play(self.C.animate.set_value(0.002), run_time = 2)

        graph = VGroup(axes, labels, r_label, l_label, c_label, frequency_label)
        # CIRCUIT = "circuit-20220323-1531.svg"
        # circuit = SVGMobject(f"{CIRCUIT}\\")
        
        # self.play(graph.animate.scale(.6).to_edge(DL))
        # self.add(circuit.to_edge(DR))

        self.play(self.L.animate.set_value(0.2), run_time = 1)
        self.play(self.C.animate.set_value(0.0001), run_time = 1)
        self.play(self.R.animate.set_value(0), run_time = 2)
        self.play(self.time.animate.set_value(.5))

        self.play(graph.animate.scale(.6).to_edge(DL))




