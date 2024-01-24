from dataclasses import dataclass
from math import *


@dataclass
class Shirt_measurements:
    # Class for keeping track of the measurements needed for shirts
    breast: float
    # Upper-body length from shoulder to belly button
    ubl: float
    shoulder: float
    # Arm circumference
    arm: float
    hip: float
    # Shirt length from shoulder to base of the desired size of the shirt
    sl: float
    # Average size for shirts of the user
    size: int
    # Slack for shirt, usually 2cm
    slack: int = 2


class Simple_Shirt:
    def __init__(self, measurements: Shirt_measurements):
        # __init__ allows to start the class for each function, so I could add shirt_measurements to the instance of the class
        # self is the instance of the class that I am calling, otherwise it will be confused
        self.measurements = measurements

    def shoulder_measurements(self):
        # there is a drop from the shoulder measurements
        match self.measurements.shoulder:
            case range(5, 7):
                drop = 1.5
            case range(6.1, 9):
                drop = 2
            case range(8.1, 10):
                drop = 2.5
            case range(9.1, 12):
                drop = 3
            case range(11.1, 21):
                drop = 4
        return drop

    def size_measurement_front(self):
        # cleavage is based on person's size, and changes if it is in the front vs. the back
        match self.measurements.size:
            case range(34, 41):
                cleavage_front = 2
            case range(42, 47):
                cleavage_front = 2.5
            case range(48, 53):
                cleavage_front = 3
            case range(54, 59):
                cleavage_front = 3.5
            case range(60, 65):
                cleavage_front = 4
        return cleavage_front

    def size_measurement_back(self):
        match self.measurements.size:
            case range(34, 41):
                cleavage_back = 2
            case range(42, 47):
                cleavage_back = 2.5
            case range(48, 53):
                cleavage_back = 3
            case range(54, 59):
                cleavage_back = 3.5
            case range(60, 65):
                cleavage_back = 4
        return cleavage_back

    def simple_shirt(self):
        # length of the shirt front front - (1/2 shoulder + cleavage front)
        self.length_front = self.measurements.sl - (
            ((1 / 2) * self.measurements.shoulder) + self.size_measurement_front()
        )
        # length of the shirt back front - cleavage back
        self.length_back = self.measurements.sl - self.size_measurement_back()
        # length of the shirt front back - (1/2 arm + shoulder drop + 4cm)
        self.length_front_b = self.measurements.sl - (
            (1 / 2) * self.measurements.arm + self.shoulder_measurements() + 4
        )

        return (
            self.length_front,
            self.length_back,
            self.length_front_b,
        )
