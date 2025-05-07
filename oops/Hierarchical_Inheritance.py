
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def show_manager(self):
        print(f"{self.name} is the manager of {self.department} department.")

class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id)
        self.programming_language = programming_language

    def show_developer(self):
        print(f"{self.name} coder in {self.programming_language}.")


mgr = Manager("sharan", "M11", "HR")
dev = Developer("sony", "D202", "Python")


mgr.details()
mgr.show_manager()

dev.details()
dev.show_developer()
