import math

class VEKTOR_XY:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Qosh(self):
        return self.x + self.y


ob1 = VEKTOR_XY(7, 6)
print(ob1.Qosh())