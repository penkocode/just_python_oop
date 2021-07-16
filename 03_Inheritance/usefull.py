class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError('Age can not be negative or zero')
        return age


class Employee(Person):
    def __init__(self, name, age, date):
        super().__init__(name, age)
        self.date = date


e = Employee('ivan', 18, '2020-07-07')
print(e.age, e.date)
