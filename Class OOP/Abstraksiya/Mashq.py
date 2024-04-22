import math
from abc import ABC, abstractmethod

class Mahum(ABC):
    @abstractmethod
    def qoshish(self):
        pass



class Kopaytirish(Mahum):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def qoshish(self):
        k = self.a + self.b
        n = k + k
        return n

ob1 = Kopaytirish(5,2)
print(ob1.qoshish())


