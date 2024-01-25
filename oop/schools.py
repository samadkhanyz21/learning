# OOP
# # Multiple Classes
# # How they interact with each other
class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # marks = 0 - 100

    def get_grade(self):
        return self.grade


class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students

        # add empty list so that students are being added to the list automatically
        # attributes can be defined even if they are not mentioned as a parameter
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return  True
        return False

    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


# Students
s1 = Student('Dill', 18, 95)
s2 = Student('Bill', 18, 75)
s3 = Student('Kill', 18, 65)

# Adding students to course(s)
course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)

# print(course.students[0].name)
print(course.get_avg_grade())