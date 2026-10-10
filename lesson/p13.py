class Student:
    def __init__(self, name, surname, student_id, age):
        self.name = name
        self.surname = surname
        self.student_id = student_id
        self.age = age

    def get_info(self):
        print(f"{self.name} {self.surname} {self.student_id} {self.age}")

s1 = Student("John", "Smith", 1, 20)
s2 = Student("Jane", "Smith", 2, 20)
s1.get_info()