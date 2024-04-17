def RIBK(d, k):

    if k in d:
        del d[k]
        print(f"'{k}' kalit bo'yicha qiymat muvaffaqiyatli o'chirildi.")
    else:
        print(f"'{k}' kalit mavjud emas.")


my_d = {'a': 10, 'b': 20, 'c': 30}
k_to_remove = input("O'chirish uchun kalitni kiriting: ")
RIBK(my_d, k_to_remove)
print("Yangi lug'at:", my_d)
