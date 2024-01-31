class Student:

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def avg_grades(self):

        """Finds the average grades of the student"""
        result = sum(self.grades)/len(self.grades)
        return result


# Instantiate the class
student = Student('Abdul', (95, 89, 93, 78, 74))

# This could be done for multiple students .e.g.
student1 = Student('Jose', (64, 90, 85, 90, 100))

print(f"Average grade of {student.name} is {student.avg_grades()}")
print(f"Average grade of {student1.name} is {student1.avg_grades()}")