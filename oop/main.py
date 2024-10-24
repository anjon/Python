
# Object: A bundle of related attributes(variables) and methods(functions)
#       Ex. Phone, Cup, Book
#       You need a class to create many objects

# Class: Blueprint which is used to design the structure and layout of an object


from car import Car


car1 = Car("Mustang", 2024, "Red", False)
car2 = Car("Corvette", 2023, 'Blue', True)
car3 = Car('Charger', 2024, 'Yellow', True)

car2.describe()