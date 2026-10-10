class Professor:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        return f"""Age  : {self.age}
Name: {self.name}
Course: {self.course}
"""

class Student(Professor):

    def introduce(self):
        return f"""Age: {self.age}
Name: {self.name}
Course: {self.course}
"""


p1 = Professor("Alex", 40, "Python")
s1 = Student("Steve", 20, "Python")

print(p1.introduce())
print(s1.introduce())