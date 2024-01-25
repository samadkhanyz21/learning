# OOP in Python
# Classes work with help of functions.
# Functions are the programs that carry out our required operations for our classes.
# Functions works as defines methods for classes.
class Dog:

    # instantiates the class
    def __init__(self, name, age):

        # created an attribute of class dog with name
        self.name = name
        self.age = age

    # Methods define for class
    def get_name(self):
        return self.name

    # Every  attribute that is added shall have its own method to be called as well
    def get_age(self):
        return self.age

    # Can also change the age value
    def set_age(self, age):
        self.age = age

    # def bark(self):
    #     print('bark')
    #
    # def add_one(self, x):
    #     return x + 1


# d = Dog()
# d.bark()
# print(d.add_one(65))

# d = Dog('doggo')
# print(d.name)
# d2 = Dog('tommy')
# print(d2.name)

d = Dog('doggo', 34)
# print(f"Name of 1st Dog:{d.get_name()}, Age of 1rst Dog:{d.get_age()}")
# d2 = Dog('tommy', 12)
# print(f"Name of 2nd Dog:{d2.get_name()}, Age of 2nd Dog:{d2.get_age()}")
d.set_age(23)
print(d.get_age())
