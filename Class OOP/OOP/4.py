class DictionaryMerger:
    def __init__(self, dict1, dict2, dict3):
        self.dict1 = dict1
        self.dict2 = dict2
        self.dict3 = dict3

    def MD(self):
        merged_dict = {}
        for key, value in self.dict1.items():
            merged_dict[key] = value
        for key, value in self.dict2.items():
            merged_dict[key] = value
        for key, value in self.dict3.items():
            merged_dict[key] = value
        return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

merger = DictionaryMerger(dict1, dict2, dict3)


result = merger.MD()

print("Lugat:", result)
