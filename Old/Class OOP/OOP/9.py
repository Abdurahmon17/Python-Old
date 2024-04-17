def ish(d):
    return not bool(d)
my_dict = {}

if ish(my_dict):
    print("Berilgan lug'at bo'sh.")
else:
    print("Berilgan lug'at bo'sh emas.")
