# Each class should be responsible for only one thing.
class Student:
    _id = 0

    def __init__(self, name):
        self.id = Student._id + 1
        self.name = name
        Student._id += 1

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Student ID: {self.id}, Student Name: {self.name}.\n"


class Register:
    @staticmethod
    def register(obj):
        with open("students.txt", "a") as file:
            file.write(str(obj))

    def get_info(self, id):
        with open("students.txt", "r") as file:
            for line in file.readlines():
                if id in line:
                    return line
        return None


registrator = Register()
student_1 = Student('Test Student One')
student_2 = Student('Test Student Two')
registrator.register(student_1)
registrator.register(student_2)
