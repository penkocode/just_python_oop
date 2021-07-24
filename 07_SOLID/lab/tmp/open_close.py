# Open for Modification but Close for Extension
from abc import ABC, abstractmethod


class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    @abstractmethod
    def get_discount(self):
        pass


class FortyPercentDiscount(StudentTaxes):
    def get_discount(self):
        if self.average_grade >= 5:
            return f"Student Name: {self.name}, Grade: {self.average_grade}, Semester Tax: {self.semester_tax * 0.4}"
        return f"Discount not apply! The average grade'{self.average_grade}' not met the requirements"


class TwentyPercentDiscount(StudentTaxes):
    def get_discount(self):
        if 4 <= self.average_grade <= 5:
            return f"Student Name: {self.name}, Grade: {self.average_grade}, Semester Tax: {self.semester_tax * 0.2}"
        return f"Discount not apply! The average grade '{self.average_grade}' not met the requirements"


discounter = TwentyPercentDiscount('test 1', 360, 4)
discounter.get_discount()
print(discounter.get_discount())
discounter_2 = FortyPercentDiscount('test 2', 360, 5)
discounter_2.get_discount()
print(discounter_2.get_discount())
