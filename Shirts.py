class Shirt:
    def measurements(self, breast, ubl, shoulder, arm, hip, sl, slack):
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

        if shoulder == 5:
            ...
        if shoulder == 5:
            ...
        if shoulder == 5:
            ...
        if shoulder == 5:
            ...
        if shoulder == 5:
            ...
        if shoulder == 5:
            ...
        if shoulder == 5:
            ...
        if shoulder == 5:
            ...
        if shoulder == 5:
            ...
        if shoulder == 5:
            ...

    def simple_shirt(self):
        self.shirt_lenght = self.sl
        self.width_front = ((1 / 4) * self.breast) + self.slack
        self.width_back = ((1 / 4) * self.breast) + self.slack
