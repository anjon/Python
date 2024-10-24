# Inheritance
# Allow a class to inherit attributes and methods from another class. Helps with code reuseability and extensibility class Child(Parent).

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

class Dog(Animal):
    def speak(self):
        print('WOFF!')

class Cat(Animal):
    def speak(self):
        print('MEOW!')

class Mouse(Animal):
    def speak(self):
        print('SQUEEK!')

dog = Dog('Scooby')
cat = Cat('Mini')
mouse = Mouse('Miki')

dog.speak()
cat.speak()
mouse.speak()