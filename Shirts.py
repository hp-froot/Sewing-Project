from dataclasses import dataclass
import math
import turtle


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


user = Shirt_measurements(
    input("Enter measurements in cm - breast: "),
    input("Upper-body length: "),
    input("Shoulder: "),
    input("Arm: "),
    input("Hip: "),
    input("Shirt length: "),
    input("Size: "),
    input("Slack: "),
)


class Simple_Shirt:
    def __init__(self, measurements: Shirt_measurements):
        # __init__ allows to start the class for each function, so I could add shirt_measurements to the instance of the class
        # self is the instance of the class that I am calling, otherwise it will be confused
        self.measurements = measurements

    def shoulder_measurements_drop_calculation(self):
        # there is a drop from the shoulder measurements
        if self.measurements.shoulder in range(5, 7):
            drop = 1.5
        elif self.measurements.shoulder in range(6, 9):
            drop = 2
        elif self.measurements.shoulder in range(8, 10):
            drop = 2.5
        elif self.measurements.shoulder in range(9, 12):
            drop = 3
        elif self.measurements.shoulder in range(11, 21):
            drop = 4
        return drop

    def size_measurement_front_cleavage_calculation(self):
        # cleavage is based on person's size, and changes if it is in the front vs. the back
        match self.measurements.size:
            case 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41:
                cleavage_front = 2
            case 42 | 43 | 44 | 45 | 46 | 47:
                cleavage_front = 2.5
            case 48 | 49 | 50 | 51 | 52 | 53:
                cleavage_front = 3
            case 54 | 55 | 56 | 57 | 58 | 59:
                cleavage_front = 3.5
            case 60 | 61 | 62 | 63 | 64 | 65:
                cleavage_front = 4
        return cleavage_front

    def size_measurement_back_cleavage_calculation(self):
        match self.measurements.size:
            case 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41:
                cleavage_back = 2
            case 42 | 43 | 44 | 45 | 46 | 47:
                cleavage_back = 2.5
            case 48 | 49 | 50 | 51 | 52 | 53:
                cleavage_back = 3
            case 54 | 55 | 56 | 57 | 58 | 59:
                cleavage_back = 3.5
            case 60 | 61 | 62 | 63 | 64 | 65:
                cleavage_back = 4
        return cleavage_back

    def simple_shirt_calculation_straight(self):
        # length of the shirt front front - (1/2 shoulder + cleavage front)
        self.length_front = (
            self.measurements.sl
            - (
                ((1 / 2) * self.measurements.shoulder)
                + self.size_measurement_front_cleavage_calculation()
            )
        ) * 10

        # width of the shirt front = 1/4 hip + 3cm
        self.width_front = (((1 / 4) * self.measurements.hip) + 3) * 10

        # length of the shirt front back - (1/2 arm + shoulder drop + 4cm)
        self.length_front_b = (
            self.measurements.sl
            - (
                (1 / 2) * self.measurements.arm
                + self.shoulder_measurements_drop_calculation
                + 4
            )
        ) * 10

        # mid-shirt width = (1/4 hip) - ((1/2 shoulder) + 1 + shoulder - 1)
        self.mid_shirt_width = ((1 / 4) * self.measurements.hip) - (
            ((1 / 2) * self.measurements.shoulder) + 1 + self.measurements.shoulder - 1
        ) * 10

        # mid-shirt length = 1/2 arm + shoulder drop + 4cm
        self.mid_shirt_length = (
            ((1 / 2) * self.measurements.shoulder)
            + self.shoulder_measurements_drop_calculation
            + 4
        ) * 10

        # cleavage straight line = 1/2 shoulder + 1
        self.shirt_cleavage = (((1 / 2) * self.measurements.shoulder) + 1) * 10

        # cleavage straight line perpendicular = 1/2 shoulder + cleavage
        self.shirt_cleavage_perpendicular = (
            ((1 / 2) * self.measurements.shoulder)
            + self.size_measurement_front_cleavage_calculation
        ) * 10

    def simple_shirt_calculation_angle(self):
        # pythagorean theorem for the width of the shirt to go up at an angle = 180 - tan-1((sl - shoulder drop - 1/2arm - 4)/3)
        width_angle = 180 - math.degrees(
            math.atan(
                (
                    self.measurements.sl
                    - self.shoulder_measurements_drop_calculation
                    - ((1 / 2) * self.measurements.arm)
                    - 4
                )
                / 3
            )
        )
        # pythagorean theorem for the shoulder of the shirt = tan-1((shoulder - 1)/shoulder drop)
        shoulder_angle = math.degrees(
            math.atan(
                (self.measurements.shoulder - 1)
                / self.shoulder_measurements_drop_calculation
            )
        )

    def hypotenuse_calculation(self):
        # hypotenuse of the width/length of the shirt
        hypotenuse_w_l = (
            math.hypot(
                (
                    self.measurements.sl
                    - self.shoulder_measurements_drop_calculation
                    - ((1 / 2) * self.measurements.arm)
                    - 4
                ),
                3,
            )
        ) * 10

        # hypotenuse of the shoulder drop
        hypotenuse_shoulder = (
            math.hypot(
                (self.measurements.shoulder - 1),
                self.shoulder_measurements_drop_calculation,
            )
        ) * 10


window = turtle.getscreen()
t = turtle.Turtle()
