class Shirt_measurements:
    def measurements(self, breast, ubl, shoulder, arm, hip, sl, slack, size):
        self.breast = breast
        self.ubl = ubl
        # upper-body lenght from shoulder to belly button
        self.shoulder = shoulder
        self.arm = arm
        # arm circumference
        self.hip = hip
        self.sl = sl
        # shirt lenght
        self.slack = slack
        self.size = size
        # on average, what size is the user for shirts


class Simple_Shirt:
    def __init__(self, shirt_measurements: Shirt_measurements):
        self.shirt_measurements = shirt_measurements

    def shoulder_measurements(self):
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
        self.shirt_lenght_front = self.shirt_measurements.sl - (
            ((1 / 2) * self.shirt_measurements.shoulder) + self.size_measurement_front()
        )
        self.shirt_leght_back = self.shirt_measurements.sl - (
            ((1 / 2) * self.shirt_measurements.shoulder) + self.size_measurement_back()
        )
        self.width_front_up = self.shirt_measurements.shoulder - 1
        self.width_back_up = (
            (1 / 4) * self.shirt_measurements.breast
        ) + self.shirt_measurements.slack
        self.width_front_down = (
            (1 / 4) * self.shirt_measurements.breast
        ) + self.shirt_measurements.slack
        self.width_back_down = (
            (1 / 4) * self.shirt_measurements.breast
        ) + self.shirt_measurements.slack
