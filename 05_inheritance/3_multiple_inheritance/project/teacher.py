from project1.employee import Employee
from project1.person import Person


class Teacher(Employee, Person):
    def teach(self):
        return 'teaching...'
