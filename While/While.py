# print("Yaqin do'stlarinigiz ro'yxatini tuzamiz!")
# dostlar = []
# n = 1
# while True:
#     savol = f"{n} - Do'stingiz ismini kiriting: "
#     dost = input(savol)
#     dostlar.append(dost)
#     restart = input("Yana do'stlar qoshasizmi(Ha / Yo'q) ")
#     a = restart.lower()
#     n += 1
#     if a != "ha":
#         break

# print("Dostlarnigiz ro'yxati:")
# print("\t")
# for dost in dostlar:
#     print(dost.title())





print("Do'stlaringzni sanaymiz!")
dostlar = {}
i = True
while i:
    ism = input("Do'stingizni ismini kiriting - ")
    yosh = input(f"{ism} yoshini kiriting - ")
    dostlar[ism] = int(yosh)

    javob = input("Yana do'stingizni kiritasizmi - ")
    if javob  == "yo'q":
        False
    
for ism, yosh in dostlar.items():
    print(f"{ism.title()}- Yoshi {yosh}")