# Create a base class Animal with properties like name and species, and a method speak(). Derive two classes Dog and Cat from Animal, 
# each with its own implementation of the speak() method (e.g., "Woof!" for Dog and "Meow!" for Cat). 
# Write a function that takes an Animal object and calls its speak() method to demonstrate polymorphism.

class Animal:
    def __init__(self, name, species):
        self.name = name 
        self.species = species
    
    def speak(self):
        print("Animal is Speaking!")

class Dog(Animal):
    def __init__(self, name , species):
        super().__init__(name, species)

    def speak(self):
        print(f"{self.name} : Woof!")

class Cat(Animal):
    def __init__(self, name , species):
        super().__init__(name, species)

    def speak(self):
        print(f"{self.name} : Meow!")


def different_Animals():
    ani1 = Dog("Tommy", "Dog")
    ani1.speak()
    ani2 = Cat("Bella", "Cat")
    ani2.speak()
    ani3 = Cat("Lilly", "Cat")
    ani3.speak()
    ani4 = Dog("Bob", "Dog")
    ani4.speak()

diff_Animals = different_Animals()
diff_Animals

