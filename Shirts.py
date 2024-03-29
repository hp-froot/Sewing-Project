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


class Simple_Shirt:
    def __init__(self, measurements: Shirt_measurements):
        # __init__ allows to start the class for each function, so I could add shirt_measurements to the instance of the class
        # self is the instance of the class that I am calling, otherwise it will be confused
        self.measurements = measurements

    def shoulder_measurements_drop_calculation(self):
        # there is a drop from the shoulder measurements
        if int(self.measurements.shoulder) in range(5, 7):
            drop = 1.5
        elif int(self.measurements.shoulder) in range(6, 9):
            drop = 2
        elif int(self.measurements.shoulder) in range(8, 10):
            drop = 2.5
        elif int(self.measurements.shoulder) in range(9, 12):
            drop = 3
        elif int(self.measurements.shoulder) in range(11, 21):
            drop = 4
        return drop

    def size_measurement_front_cleavage_calculation(self):
        # cleavage is based on person's size, and changes if it is in the front vs. the back
        match int(self.measurements.size):
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
        match int(self.measurements.size):
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
            float(self.measurements.sl)
            - (
                ((1 / 2) * float(self.measurements.shoulder))
                + self.size_measurement_front_cleavage_calculation()
            )
        ) * 10

        # width of the shirt front = 1/4 hip + 3cm
        self.width_front = (((1 / 4) * float(self.measurements.hip)) + 3) * 10

        # length of the shirt front back - (1/2 arm + shoulder drop + 4cm)
        self.length_front_b = (
            float(self.measurements.sl)
            - (
                (1 / 2) * float(self.measurements.arm)
                + self.shoulder_measurements_drop_calculation()
                + 4
            )
        ) * 10

        # mid-shirt width = (1/4 hip) - ((1/2 shoulder) + shoulder)
        self.mid_shirt_width = (
            (float(self.measurements.hip) / 4)
            - (
                (float(self.measurements.shoulder) / 2)
                + float(self.measurements.shoulder)
            )
        ) * 10

        # mid-shirt length = 1/2 arm + shoulder drop + 4cm
        self.mid_shirt_length = (
            (float(self.measurements.arm) / 2)
            + self.shoulder_measurements_drop_calculation()
            + 4
        ) * 10

        # cleavage straight line = 1/2 shoulder + 1
        self.shirt_cleavage = (((1 / 2) * float(self.measurements.shoulder)) + 1) * 10

        # cleavage straight line perpendicular = 1/2 shoulder + cleavage
        self.shirt_cleavage_perpendicular = (
            ((1 / 2) * float(self.measurements.shoulder))
            + self.size_measurement_front_cleavage_calculation()
        ) * 10

        return (
            self.length_front,
            self.width_front,
            self.length_front_b,
            self.mid_shirt_width,
            self.mid_shirt_length,
            self.shirt_cleavage,
            self.shirt_cleavage_perpendicular,
        )

    def simple_shirt_calculation_angle(self):
        # pythagorean theorem for the width of the shirt to go up at an angle = 180 - tan-1((sl - shoulder drop - 1/2arm - 4)/3)
        self.width_angle_base = 180 - math.degrees(
            math.atan(
                (
                    float(self.measurements.sl)
                    - self.shoulder_measurements_drop_calculation()
                    - ((1 / 2) * float(self.measurements.arm))
                    - 4
                )
                / 3
            )
        )
        self.width_angle_top = math.degrees(
            math.atan(
                (
                    float(self.measurements.sl)
                    - self.shoulder_measurements_drop_calculation()
                    - ((1 / 2) * float(self.measurements.arm))
                    - 4
                )
                / 3
            )
        )

        # pythagorean theorem for the shoulder of the shirt = tan-1((shoulder - 1)/shoulder drop)
        self.shoulder_angle = math.degrees(
            math.atan(
                (float(self.measurements.shoulder) - 1)
                / self.shoulder_measurements_drop_calculation()
            )
        )
        self.shoulder_angle_top = 90 - float(self.shoulder_angle)

        return (
            self.width_angle_base,
            self.width_angle_top,
            self.shoulder_angle,
            self.shoulder_angle_top,
        )

    def hypotenuse_calculation(self):
        # hypotenuse of the width/length of the shirt
        self.hypotenuse_w_l = (
            math.hypot(
                (
                    float(self.measurements.sl)
                    - self.shoulder_measurements_drop_calculation()
                    - ((1 / 2) * float(self.measurements.arm))
                    - 4
                ),
                3,
            )
        ) * 10

        # hypotenuse of the shoulder drop
        self.hypotenuse_shoulder = (
            math.hypot(
                (float(self.measurements.shoulder) - 1),
                self.shoulder_measurements_drop_calculation(),
            )
        ) * 10

        return (self.hypotenuse_w_l, self.hypotenuse_shoulder)


class Simple_Shirt_Turtle:
    def __init__(self, simple_shirt: Simple_Shirt):
        self.simple_shirt = simple_shirt

    def simple_shirt_drawing(self):
        t = turtle.Turtle()
        t.forward(self.simple_shirt.length_front)
        t.left(90)
        t.forward(self.simple_shirt.width_front)
        t.left(self.simple_shirt.width_angle_base)
        t.forward(self.simple_shirt.hypotenuse_w_l)

        t.left(self.simple_shirt.width_angle_top)
        t.forward(self.simple_shirt.mid_shirt_width)
        t.right(90)
        n = 0
        while n <= self.simple_shirt.mid_shirt_length:
            t.pencolor("red")
            t.forward(15)
            t.penup()
            t.forward(15)
            t.pendown()
            n += 30
        t.pencolor("black")
        t.left(self.simple_shirt.shoulder_angle)
        t.forward(self.simple_shirt.hypotenuse_shoulder)
        t.left(self.simple_shirt.shoulder_angle_top)
        x = 0
        while x <= self.simple_shirt.shirt_cleavage:
            t.pencolor("red")
            t.forward(15)
            t.penup()
            t.forward(15)
            t.pendown()
            x += 30
        t.left(90)
        w = 0
        while w <= self.simple_shirt.shirt_cleavage_perpendicular:
            t.forward(15)
            t.penup()
            t.forward(15)
            t.pendown()
            w += 30


window = turtle.getscreen()


def main():
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

    user_simple_shirt = Simple_Shirt(user)
    user_simple_shirt.shoulder_measurements_drop_calculation()
    user_simple_shirt.size_measurement_front_cleavage_calculation()
    user_simple_shirt.size_measurement_back_cleavage_calculation()
    user_simple_shirt.simple_shirt_calculation_straight()
    user_simple_shirt.simple_shirt_calculation_angle()
    user_simple_shirt.hypotenuse_calculation()

    drawing_user = Simple_Shirt_Turtle(user_simple_shirt)
    drawing_user.simple_shirt_drawing()


if __name__ == "__main__":
    main()

turtle.exitonclick()
