class Canculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Qosh(self):
        return f'Yigindisi: {self.x + self.y}'

    def ayir(self):
        return f'Ayirmasi: {self.x - self.y}'

    def kop(self):
        return f'Kopaytmasi: {self.x * self.y}'

    def bolish(self):
        return f'Bolinmasi: {self.x / self.y}'

    def __str__(self):
        return f'{self.Qosh()} \n{self.ayir()} \n{self.kop()} \n{self.bolish()}'


class SupperCanc(Canculator):
    def __init__(self, x, y):
        super().__init__(x, y)

    def pow(self):
        return self.x ** self.y

x = int(input('X ni kiriting: '))
y = int(input('Y ni kiriting: '))

ob1 = SupperCanc(x, y)
print(ob1.pow())


























# class Person:
#     color = 'Black'
#     age = 30
#     white = '100kg'
#
# class Father:
#     def hello(self):
#         print('Hello World')
#
# class Child(Person, Father):
#     name = "Anvar"
#     genar = "M"
#
#
# ob1 = Child()
# ob1.age = 50
# ob1.name = 'Nilufar'
# ob1.genar = "F"
# print(
#     ob1.hello()
# )
#

























# class Canculator:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def Qosh(self):
#         return f'Yigindisi: {self.x + self.y}'
#
#     def ayir(self):
#         return f'Ayirmasi: {self.x - self.y}'
#
#     def kop(self):
#         return f'Kopaytmasi: {self.x * self.y}'
#
#     def bolish(self):
#         return f'Bolinmasi: {self.x / self.y}'
#
#     def __str__(self):
#         return f'{self.Qosh()} \n{self.ayir()} \n{self.kop()} \n{self.bolish()}'
#
#
# ob1 = Canculator(5, 2)
# print(ob1)




















# class Car:
#     model = 'Malilbu'
#     year = 2005
#     prist = '200.000 USD'
#
#
# ob1 = Car
# print(ob1.model, ob1.year, ob1.prist)









# class Car2:
#     def __init__(self, model, year, color, price):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.price = price
#     #
#     # def __str__(self):
#     #     return f'{self.model, self.year, self.color, self.price}'
#
#     def info_cars(self):
#         print(f'Models: {self.model} \nColor: {self.color} \nYear: {self.year} \nNarxi: {self.price} ')
#
#
# ob1 = Car2('Spark', 2021, 'wihte', '8.000$')
# ob1.info_cars()