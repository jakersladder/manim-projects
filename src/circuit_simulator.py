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
    time = 1

    # Returns the Voltage at frame
    def get_voltage(self):
        alpha = (self.Q / (self.L.get_value() * self.C.get_value())) - (self.I * self.R.get_value() / self.L.get_value())

        self.I = self.I + (alpha * self.dt)
        self.Q = self.Q - (self.I * self.dt)

        Vc = self.Q / self.C.get_value()
        return Vc

    # Generates the plot Volatage by Time
    def generate_plot(self, axes):
        self.Q = self.C.get_value() * self.EMF
        return axes.plot(lambda t: self.get_voltage(), [0, 1, self.dt])

    # I am the CONTRUCTOR!
    def construct(self):
      axes = Axes(
          x_range=[0, 1, .1],
          y_range=[-6, 6, 1],
          x_length=10,
          axis_config={"color": GREEN},
          x_axis_config={"numbers_to_include": np.arange(0, 1, .1)},
          y_axis_config={"numbers_to_include": np.arange(-6.01, 6.01, 1)},          
          tips=False,
      )

      # Adding voltage to the scene will call generate plot every frame
      voltage = always_redraw(lambda: self.generate_plot(axes))

      #Create Text
      r_text = Text("R = ")
      l_text = Text("L = ")
      c_text = Text("C = ")
      resistance_text = DecimalNumber(self.R.get_value()).next_to(axes, UP)
      inductance_text = DecimalNumber(self.L.get_value(), 6).next_to(resistance_text, LEFT)
      capacitance_text = DecimalNumber(self.C.get_value(), 6).next_to(resistance_text, RIGHT)
      resistance_text.add_updater(lambda m: m.set_value(self.R.get_value()))
      inductance_text.add_updater(lambda m: m.set_value(self.L.get_value()))
      capacitance_text.add_updater(lambda m: m.set_value(self.C.get_value()))
      

      self.add(resistance_text, inductance_text, capacitance_text)
      self.add(axes)
      self.play(Create(voltage), run_time = 2)
      self.wait()
      self.play(self.R.animate.set_value(6), run_time = 3)
      self.play(self.L.animate.set_value(0.5), run_time = 2)
      self.play(self.C.animate.set_value(0.002), run_time = 2)
