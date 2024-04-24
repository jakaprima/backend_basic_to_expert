from abc import ABC, abstractmethod


# ENCAPSULATION
class Player:
    def __init__(self, name):
        self.name = name
        # Encapsulating health attribute with a starting value and private access modifier
        self._health = 100  # underscore for private attribute

    def get_health(self):
        return self._health

    def take_damage(self, damage: int):
        self._health -= damage


# INHERITANCE
class Book:
    def __init__(self, title):
        self.title = title

    def display_info(self):
        print(f"Title {self.title}")


class Ebook(Book):
    def __init__(self, title):
        super().__init__(title)


class Car:
    def __init__(self, make, model, year):
        self.__make = make  # private attribute
        self.__model = model  # private attribute
        self.__year = year  # private attribute

    def get_make(self):  # getter method
        return self.__make

    def get_model(self):  # getter method
        return self.__model

    def get_year(self):  # getter method
        return self.__year

    def set_make(self, make):  # setter method
        self.__make = make

    def set_model(self, model):  # setter method
        self.__model = model

    def set_year(self, year):  # setter method
        self.__year = year


# INTERFACE / ABSTRACT REPRESENTATION A SHAPE
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# CONCRETE SUBCLASS REPRESENTING A RECTABLE
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Concrete subclass representing a circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


def main():
    # --------------------------------------------------------- ENCAPSULATION
    """
    Encapsulation is one of the fundamental principles of object-oriented programming (OOP).
    It refers to the bundling of data and methods that operate on the data into a single unit,
    called a class. In encapsulation, the internal state of an object is hidden from the outside world,
    and access to it is restricted to methods of the class.
    :return:
    """
    print("-------------------------------------------- ENCAPSULATION")
    player_instance = Player(name="jaka")

    print("GET HEALTH", player_instance.get_health())
    player_instance.take_damage(damage=10)
    print("GET HEALTH", player_instance.get_health())

    # --------------------------------------------------------- INHERITANCE
    """
    Inheritance is a key concept in object-oriented programming where a new class can be created 
    by extending an existing class. The new class, called a subclass or derived class, 
    inherits attributes and methods from the existing class, called a superclass or base class
    """
    ebook_instance = Ebook(title="buku jaka")
    ebook_instance.display_info()

    # --------------------------------------------------------- POLYMORPHIS
    """
    Polymorphism is another fundamental concept in object-oriented programming, 
    which allows objects of different classes to be treated as objects of a common 
    superclass. This allows for flexibility and code reuse.
    """
    car = Car("toyota", "camry", 2024)
    print("make: ", car.get_make())
    print("model: ", car.get_model())
    print("year: ", car.get_year())

    # Modifying attributes using setter methods
    car.set_make("Honda")
    car.set_model("Accord")
    car.set_year(2023)
    print("make: ", car.get_make())
    print("model: ", car.get_model())
    print("year: ", car.get_year())

    # --------------------------------------------------------- ABSTRACTION
    """
    Abstraction is another core principle of object-oriented programming that focuses on hiding 
    the complex implementation details of a system and exposing only the necessary features or 
    functionalities to the outside world. This allows for simpler interaction with objects 
    and helps in managing complexity.
    """
    rectangle = Rectangle(5, 4)
    circle = Circle(3)
    print("AREA RECTANGLE: ", rectangle.area())
    print("PERIMETER RECTANGLE: ", rectangle.perimeter())
    print("AREA CIRCLE: ", circle.area())
    print("PERIMETER CIRCLE: ", circle.perimeter())


main()
