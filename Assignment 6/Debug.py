class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department


class Cake:
    # can you fill out the rest of this for me? im dumb
    # the cake needs to have the cake flavor and cake frosting stored
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting


class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length

    def breedGuess(self):
        if self.fur_length == "long":
            return "Domestic Longhair"
        else:
            return "Domestic Shorthair"


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    # create your own function! what do you want it to do?
    def isOrange(self):
        if self.color == "orange":
            return "The car is orange, the best color!"
        else:
            return "The car isn't orange :("


def main():
    # fill this one out with a dog's name and age... can be your dog, friend's dog, etc
    dog1 = Dog("Bono", 6)
    print(dog1.name, dog1.age)

    # and what about a new employee
    newEmployee = Employee("John", 782943, "IT")
    # how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)

    # now create and print out a cake you make
    cake1 = Cake("Good", "Vanilla")
    print(cake1.flavor, cake1.frosting)
    # and now create another cake and print it out
    cake2 = Cake("Bad", "Chocolate")
    print(cake2.flavor, cake2.frosting)

    # create a cat!
    cat1 = Cat("Bozi", 9, "long")
    # create another cat!
    cat2 = Cat("Mango", 5, "short")
    # What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())

    # create a car!
    car1 = Car("Traverse", 2018, "black")
    # Now print out the function you made for car :)
    print(car1.isOrange())


main()
