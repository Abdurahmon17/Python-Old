# class Person:
#     name = "Anvar"
#     __pawword = "123456"
#     last_open = "12:04"
#     age = 19
#
#     def getter(self):
#         return self.__pawword
#
#     def setter(self, new_password):
#         self.__pawword = new_password
#
# ob1 = Person()
# ob1.setter("Hayer")
# print(ob1.setter())







# Eslatma

class Uy:
    __hat = "Sen zo'rrisan"

    def hatni_opkeluvchi_getter(self):
        return self.__hat

    def hatni_opketuvchi_setter(self, new_hat):
        self.__hat = new_hat

ob1 = Uy()
ob1.hatni_opketuvchi_setter("Adashdim men zo'r ekanman")
print(ob1.hatni_opketuvchi_setter())

