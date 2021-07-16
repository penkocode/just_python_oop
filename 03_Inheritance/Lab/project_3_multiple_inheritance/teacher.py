from Lab.project_3_multiple_inheritance.employee import Employee
from Lab.project_3_multiple_inheritance.person import Person


class Teacher(Person, Employee):
    def teach(self) -> str:
        return 'teaching...'
