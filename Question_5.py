# Define a class Vehicle with a method max_speed(). Create three derived classes: Car, Bike, and Truck, 
# each overriding the max_speed() method to provide different maximum speeds. 
# Write a function that takes a list of Vehicle objects and prints the maximum speed for each one.

class Vehicle:
    def __init__(self):
        pass

    def max_speed():
        print("Max Speed...")

class Car(Vehicle):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def max_speed(self):
        print(f"Max Speed of {self.name} is {self.speed}")

class Bike(Vehicle):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def max_speed(self):
        print(f"Max Speed of {self.name} is {self.speed}")

class Truck(Vehicle):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def max_speed(self):
        print(f"Max Speed of {self.name} is {self.speed}")

veh1 = Car("BMW", "340 KM/H")
veh2 = Bike("YBR", "220 KM/H")
veh3 = Truck("Petterbult", "140 KM/H")
veh4 = Truck("Mazda", "110 KM/H")
veh5 = Car("Roco", "280 KM/H")
veh6 = Bike("CD70", "120 KM/H")

list = [veh1,veh2, veh3, veh4, veh5, veh6]

def Vehicle_Max_speed(list):
    for item in list:
        item.max_speed()


Vehicle_Max_speed(list) 