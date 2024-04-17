# a = input("Son kiriting - ")
# a = a[::-1]
# b = 0
# for i in range(len(a)):
#     b += 2 ** i * int(a[i])
# print(b)


# def ish():
#     a1 = int(input("A1ni kiriting: "))
#     a2 = int(input("A2ni kiriting: "))
#     b1 = int(input("B1ni kiriting: "))
#     b2 = int(input("B2ni kiriting: "))
#     c1 = int(input("C1ni kiriting: "))
#     c2 = int(input("C2ni kiriting: "))
#     D = a1*b2-a2*b1
#     Dy = a1*c2-a2*c1
#     Dx = c1*b2-c2*b1
#     if D != 0:
#         x = Dx/D
#         y = Dy/D
#         print("X -",x,"Y -",y)
#     elif D == 0:
#         print("Bosh toplam!")
#     else:
#         ("Cheksiz!")
#
# print(ish())


# import random
# def make_number():
#     a = [9, 9, 8]
#     for _ in range(9):
#         number = random.randint(0, 9)
#         a.append(number)
#     return a
# def make_to_str(a: list) -> str:
#     s = ''
#     for i in a:
#         s += str(i)
#     return s
# def generate_numbers(n: int):
#     a = []
#     for _ in range(n):
#         number = make_number()
#         a.append(make_to_str(number))
#     return a
# for i in generate_numbers(100):
#     print(i)


a = int(input("A son kiriting: "))
c = input("Belgini kiriting: ")
b = int(input("B soni kiritng: "))
if c == "*":
    j = a*b
    print(a, "*", b, "=",j)
elif c == "//":
    j = a//b
    print(a, "//", b, "=",j)
elif c == "/":
    j = a/b
    print(a, "/", b, "=",j)
elif c == "%":
    j = a%b
    print(a, "%", b, "=",j)
elif c == "+":
    j = a+b
    print(a, "+", b, "=",j)
elif c == "-":
    j = a-b
    print(a, "-", b, "=",j)
else:
    print("Bunday belgi yo'q!!!")






















