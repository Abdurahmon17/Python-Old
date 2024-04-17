class SortedDictByKeys:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def keys(self):
        return dict(sorted(self.dictionary.items()))


my_dict = {'apple': 5, 'banana': 2, 'orange': 7, 'grape': 3}

key = SortedDictByKeys(my_dict)
sorted_by_keys = key.keys()

print("Kalitlar:", sorted_by_keys)
