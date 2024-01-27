class Animal:
    # initialize the class
    # the parameters should be initiated if you don't want error
    def __init__(self, height = 100, weight = 30):
        self.height = height
        self.weight = weight

    # define a method to carry out the process
    def print_height(self):
        print(f"This animal's height is:{self.height}")


animal_1 = Animal(height=120, weight=88)
animal_2 = Animal(height=170, weight=100)
animal_3 = Animal()

#           *** ABOVE ALL IS IN CLASS ***
animal_1.print_height()