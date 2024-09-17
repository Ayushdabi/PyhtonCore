#Encapsulation

class Person:
    def __init__(self, name, age):
        self.__age = age
        self.name = name

    def get_age(self):
        return self.__age


    def get_name(self):
        return  self.name

p = Person("Ravi", 25)


print(p.get_name())# Output: 25
print(p.get_age())

