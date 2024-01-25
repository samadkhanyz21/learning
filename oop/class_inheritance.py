# In class inheritance there is a main class which has all the control.
# while subclasses work based on the main class.
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I dont know what to say")


# Child Classes
class Cat(Pet):
    def speak(self):
        print('meow')


class Dog(Pet):
    def speak(self):
        print('bark')


p = Pet("Kill", 19)
p.speak()
c = Pet("Bill", 34)
# p.show()
# c.show()

c.speak()