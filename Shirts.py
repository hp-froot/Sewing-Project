import math


class Shirt_measurements:
    def __init__(self, breast, ubl, shoulder, arm, hip, sl, slack, size):
        # defining measurements needed for shirts
        self.breast = breast
        self.ubl = ubl
        # upper-body length from shoulder to belly button
        self.shoulder = shoulder
        self.arm = arm
        # arm circumference
        self.hip = hip
        self.sl = sl
        # shirt length from shoulder to base
        self.slack = slack
        self.size = size
        # on average, what size is the user for shirts


class Simple_Shirt:
    def __init__(self, shirt_measurements: Shirt_measurements):
        # __init__ allows to start the class for each function, so I could add shirt_measurements to the instance of the class
        # self is the instance of the class that I am calling, otherwise it will be confused
        self.shirt_measurements = shirt_measurements

    def shoulder_measurements(self):
        # there is a drop from the shoulder measurements
        match self.shirt_measurements.shoulder:
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
        match self.shirt_measurements.size:
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
        match self.shirt_measurements.size:
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
        self.shirt_length_front = self.shirt_measurements.sl - (
            ((1 / 2) * self.shirt_measurements.shoulder) + self.size_measurement_front()
        )
        # length of the shirt back front - cleavage back
        self.shirt_length_back = (
            self.shirt_measurements.sl - self.size_measurement_back()
        )
        # length of the shirt front back - (1/2 arm + shoulder drop + 4cm)
        self.shirt_length_front_f = self.shirt_measurements.sl - (
            (1 / 2) * self.shirt_measurements.arm + self.shoulder_measurements() + 4
        )
        """
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
        """
        return (
            self.shirt_length_front,
            self.shirt_length_back,
            self.shirt_length_front_f,
        )

    shirt_length_front, shirt_length_back, shirt_length_front_f = simple_shirt()
