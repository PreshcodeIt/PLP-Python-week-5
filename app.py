# Assignment 1: Design Your Own Class
class Superhero:
    def __init__(self, name, alias, power, strength_level):
        self.name = name
        self.alias = alias
        self.power = power
        self.strength_level = strength_level

    def display_info(self):
        return f"{self.alias} (Real Name: {self.name}) - Power: {self.power}, Strength: {self.strength_level}/10"

    def use_power(self):
        return f"{self.alias} uses their {self.power}!"

# Inheriting from Superhero class


class Villain(Superhero):
    def __init__(self, name, alias, power, strength_level, evil_plan):
        super().__init__(name, alias, power, strength_level)
        self.__evil_plan = evil_plan  # Private attribute

    def reveal_plan(self):
        return f"{self.alias}'s evil plan is: {self.__evil_plan}"

    def use_power(self):
        return f"{self.alias} uses their {self.power} to execute their evil plan!"


# Assignment 1 Demonstration
hero = Superhero("Clark Kent", "Superman", "Super Strength", 10)
villain = Villain("Lex Luthor", "Lex", "Genius Intellect",
                  8, "World Domination")

print("Assignment 1: Superhero and Villain")
print(hero.display_info())
print(hero.use_power())
print(villain.display_info())
print(villain.reveal_plan())
print(villain.use_power())

print("\n" + "=" * 50 + "\n")

# Activity 2: Polymorphism Challenge


class Animal:
    def move(self):
        pass  # Base method to be overridden by subclasses


class Dog(Animal):
    def move(self):
        return "Running on four legs 🐕"


class Bird(Animal):
    def move(self):
        return "Flying in the sky 🦅"


class Fish(Animal):
    def move(self):
        return "Swimming in water 🐟"


class Vehicle:
    def move(self):
        pass  # Base method to be overridden by subclasses


class Car(Vehicle):
    def move(self):
        return "Driving on roads 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying in the air ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing on water 🚤"


# Activity 2 Demonstration
animals = [Dog(), Bird(), Fish()]
vehicles = [Car(), Plane(), Boat()]

print("Activity 2: Polymorphism with Animals and Vehicles")
print("Animal Movements:")
for animal in animals:
    print(animal.move())

print("\nVehicle Movements:")
for vehicle in vehicles:
    print(vehicle.move())
