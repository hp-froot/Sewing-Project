import pytest
from Shirts import *

def simple_shirt_test():
    # length of the shirt front front - (1/2 shoulder + cleavage front)
    assert shirt_length_front == self.shirt_measurements.sl - (
            ((1 / 2) * self.shirt_measurements.shoulder) + self.size_measurement_front()
        )
        # length of the shirt back front - cleavage back
        self.shirt_length_back = self.shirt_measurements.sl - (
            ((1 / 2) * self.shirt_measurements.shoulder) + self.size_measurement_back()
        )
        # length of the shirt front back - shoulder drop
        self.shirt_length_front_f = (
            self.shirt_measurements.sl - self.shoulder_measurements()
        )
        # length of the shirt back back
        # front cleavage is a curve between the y-axis (1/2 shoulder + 1cm) and the x-axis (1/2 shoulder + cleavage size)
        # shoulder strap front top = shoulder - 1cm
        self.width_front_up_top = self.shirt_measurements.shoulder - 1
        # shoulder strap front drop = pythagoras (c = square root of a^2 + b^2)
        self.width_front_up_drop = math.sqrt(
            (self.width_front_up_top**2) + (self.shoulder_measurements() ** 2)
        )
        # shoulder strap back
        self.width_back_up = (
            (1 / 4) * self.shirt_measurements.breast
        ) + self.shirt_measurements.slack
        # 1/4 width of hip + 3cm
        self.width_front_down = (
            (1 / 4) * self.shirt_measurements.breast
        ) + self.shirt_measurements.slack
        # 1/4 width of hip + 3cm
        self.width_back_down = (
            (1 / 4) * self.shirt_measurements.breast
        ) + self.shirt_measurements.slack