class Person:
    name = "Anvar"
    __pawword = "123456"
    last_open = "12:04"
    age = 19

    def getter(self):
        return self.__pawword

    def setter(self, new_password):
        self.__pawword = new_password

ob1 = Person()
ob1.setter("Hayer")
print(ob1.setter())