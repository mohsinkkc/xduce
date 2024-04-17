''' 
1).Class Implementation:
Write a program in Python (or any other object-oriented language of your choice) to implement a simple class called Car. The Car class should have the following attributes and methods:

Attributes: make, model, year, color, mileage
Methods:
__init__(): Constructor method to initialize the attributes.
drive(miles): Method to simulate driving the car for a certain number of miles and updating the mileage attribute accordingly.
display_info(): Method to display all the information about the car.
You can also add additional methods or attributes if you like.


2).Inheritance:
Extend the Car class from the previous question to create a new class called ElectricCar. The ElectricCar class should inherit from the Car class and have an additional attribute battery_capacity representing the capacity of the electric car's battery in kWh. Override the drive() method to include information about electric cars.

3).Polymorphism:
Create a program in Python (or any other object-oriented language) that demonstrates polymorphism using a common interface. Define a base class called Shape with a method calculate_area(). Then, create two subclasses Rectangle and Circle, each with their own implementation of the calculate_area() method. Finally, write a function called print_area() that takes an instance of Shape as a parameter and prints its area.
'''
import math

#1) Class Implementation

class Car:
    def __init__(self, make, model, year, color, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def drive(self, miles):
        self.mileage += miles
        print(f"Driving {miles} miles...")

    def display_info(self):
        print(f"Car Info:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nColor: {self.color}\nMileage: {self.mileage} miles")

#2) Inheritance

class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity, mileage=0):
        super().__init__(make, model, year, color, mileage)
        self.battery_capacity = battery_capacity

    def drive(self, miles):
        self.mileage += miles
        print(f"Driving {miles} miles on electric power...")

#3) Polymorphism

class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

def print_area(shape):
    area = shape.calculate_area()
    print(f"The area of the shape is: {area}")

car1 = Car("Toyota", "Camry", 2020, "Black")
car1.drive(100)
car1.display_info()

electric_car = ElectricCar("Tesla", "Model S", 2022, "Red", battery_capacity=75)
electric_car.drive(50)
electric_car.display_info()

rectangle = Rectangle(5, 10)
circle = Circle(7)

print_area(rectangle)
print_area(circle)
