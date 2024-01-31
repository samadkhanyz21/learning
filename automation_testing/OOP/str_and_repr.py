class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

# Both are known as magic methods
    def __str__(self):

        """For representation of object in str generated format"""
        str_result = f"Person: {self.name}\nAge: {self.age} yrs\n"
        return str_result

    def __repr__(self):

        """Unambiguous  representation. Not shown in console. Mainly for
        programmers viewing the object. Works as behind the scene. The
        greater than and smaller than signs are just for visual
        representation"""
        repr_result = f"<Person: {self.name}, Age: {self.age}>"
        return repr_result


# Saves all the info related to bob in Bob's directory
bob = Person("Bob", 33)
smith = Person('Smith', 45)
anna = Person('Anna', 28)

print(bob)
print(smith)
print(anna)