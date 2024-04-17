class LI:
    def __init__(self, di):
        self.dictionary = di

    def ish(self):
        return dict(sorted(self.dictionary.items(), key=lambda item: item[1]))



my_dict = {'apple': 5, 'banana': 2, 'orange': 7, 'grape': 3}


sorted_dict = LI(my_dict)
lugat = sorted_dict.ish()

print("Lug'at:", lugat)
