import math
from abc import ABC, abstractmethod


class Mahum(ABC):

    @abstractmethod
    def parametor(self):
        pass

    @abstractmethod
    def yuzi(self):
        pass




class Uchburchak(Mahum):
    def __int__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def parametor(self):
        return self.a +self.b+self.c

    def yuzi(self):
        p = self.parametor()
        s = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return s


class Torburchak(Mahum):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def parametor(self):
        return 2*(self.a + self.b)

    def yuzi(self):
        return self.a * self.b






















# from abc import ABC, abstractmethod
#
# #Abstraksiya == Mahum
#
# class Paket(ABC):
#     @abstractmethod
#     def kattoshka(self):
#         pass
#
#     @abstractmethod
#     def pamidor(self):
#         pass
#
#     @abstractmethod
#     def laptop(self):
#         pass
#

