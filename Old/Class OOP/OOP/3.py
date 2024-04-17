class SortedDictByKeys:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def sort_by_keys(self):
        return dict(sorted(self.dictionary.items()))

    def fff(self, key, value):
        self.dictionary[key] = value


my_dict = {'apple': 5, 'banana': 2, 'orange': 7, 'grape': 3}


keys = SortedDictByKeys(my_dict)


keys.fff('pineapple', 10)

sorted_by_keys = keys.sort_by_keys()
print("Kalitlar - Lug'at:", sorted_by_keys)
