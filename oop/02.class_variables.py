# Class Vairable
class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student('Spongebob', 30)
student2 = Student('Nandita', 32)
student3 = Student('Ayan', 28)
student4 = Student('Sandy', 40)

print(f'My graduating class of {Student.class_year} has {Student.num_students} students')
print(f'{student1.name}')
print(f'{student2.name}')
print(f'{student3.name}')
print(f'{student4.name}')