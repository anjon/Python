# Nested class = A class defined within another class
#               class Outer:
#                   class Inner:
# Benifits: Allows you to logically group classes that are closely related
#           Encapsulates private details that aren't relevant outside of the outer class
#           keeps the namespace clean; resude the possbility of naming conflicts


class Company:

    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]


company1 = Company("Krusty Krab")
company2 = Company("Intrum")

company1.add_employee("AlexT", "Manager")
company1.add_employee("Ashwin", "Lead Developer")
company1.add_employee("Anjon", "Tech Lead")

company2.add_employee("A", "Manager")
company2.add_employee("B", "Tester")

for employee in company2.list_employees():
    print(employee)
