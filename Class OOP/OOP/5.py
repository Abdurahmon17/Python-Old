def CHVD(value, dictionary):
    return value in dictionary.values()

d = {'a': 1, 'b': 2, 'c': 3}

# Qiymatni tekshirish
V = 2
if CHVD(V, d):
    print(f"{V} lug'atda mavjud")
else:
    print(f"{V} lug'atda mavjud emas")
