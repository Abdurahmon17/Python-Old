# class T1:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
    
#     def s(self):
#         return (self.x ** 2)+(self.y ** 2)
    
#     def p(self):
#         return self.x + self.y + self.z
    
#     def __str__(self):
#         return f"Yuzasi: {self.s()}, Parametori: {self.p()}"

# car1 = T1(1, 4, 6)
# print(car1)        


# class AUS:
#     def __init__(self, r):
#         self.r = r

#     def S(self):
#         return 3.14 * (self.r ** 2)
    
#     def U(self):
#         return 2*3.14*self.r
    
#     def __str__(self):
#         return f"Aylananing uzunligi: {self.U()}, Doiraning yuzi: {self.S()}"
    
# aus = AUS(5)
# print(aus)


































# class Cars:
#     model = 'Gentra'
#     year = 2024
#     color = "Black"
#     money = "19,000$"

# car1 = Cars()

# print(f"\n Modeli - {car1.model},\n Yili - {car1.year},\n Rangi - {car1.color},\n Narxi - {car1.money}")
# print("\n")
















# class Cars:
#     def __init__(self, modeli, year, color, money):
#         self.modeli = modeli
#         self.year = year
#         self.color = color
#         self.money = money


#     def __str__(self):
#         return f"Mashina Modeli - {self.modeli}, Yili - {self.year} Rangi - {self.color}, Narxi - {self.money}"
    
# car1 = Cars("Spark", 2015, "Oq", "7,000$")
# car2 = Cars("Kia", 2024, "Qora", "19,000$")
# print(car1)
# print(car2)
# print("\n")





















# class Canc:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def qosh(self):
#         return self.x + self.y
    
#     def ayirma(self):
#         return self.x - self.y
    
#     def kop(self):
#         return self.x * self.y
    
#     def bolinma(self):
#         return self.x / self.y

#     def __str__(self):
#         return f"Raqamlar yig'indisi - {self.qosh()}, Airmasi - {self.ayirma()}, Ko'paytmasi - {self.kop()}, Bolinmasi - {self.bolinma()}"


# ob1 = Canc(4, 2)
# print(ob1)

















# if a == ob1:
#     print("\n")
#     print(f" Yig'indisi - {ob1.qosh()}")
#     print("\n")
#     print(f" Ayirmasi - {ob1.ayirma()}")
#     print("\n")
#     print(f" Ko'paytmasi - {ob1.kop()}")
#     print("\n")
#     print(f" Bolinmasi - {ob1.bolinma()}")
#     print("\n")
# elif a == ob2:
#     print("\n")
#     print(f" Yig'indisi - {ob2.qosh()}")
#     print("\n")
#     print(f" Ayirmasi - {ob2.ayirma()}")
#     print("\n")
#     print(f" Ko'paytmasi - {ob2.kop()}")
#     print("\n")
#     print(f" Bolinmasi - {ob2.bolinma()}")
#     print("\n")
# else:
#     print("Bunday obyekt yo'q!")