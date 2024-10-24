# Static methods: A method that belongs to a class rather than any object from that class (instance)
#                 Usually used for general utility functions

# Instance: Best for operations on instances of the class(objects)
# static methods = best for utility functions that do not need access to data


class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cook", "Cashier", "Janitor"]
        return position in valid_positions


employee1 = Employee("Sheldon", "Manager")
employee2 = Employee("Lenord", "Cook")
employee3 = Employee("Raj", "Cashier")

print(Employee.is_valid_position("Developer"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
