from abc import ABC, abstractmethod
from typing import Type

# SOLID (5 principle)
# SRP, OCP, LSP, ISP, DIP
# Single Responsibility Principle (SRP): class should have only one reason to change
class FileManager:
    def read_file(self):
        pass

    def write_file(self):
        pass


# OPEN / CLOSED PRINCIPLE (OCP): software entities harus di open for extension but closed for modification
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# LISKOV SUBSTITUTION PRINCIPLE (LSP): bojects dari superclass harus replicable dengan objects dari subclasses tanpa
# bereffect ke correctness dari program
class Animal:
    def fly(self):
        pass


class Merpati(Animal):
    def fly(self):
        print("MERPATI TERBANG")


class Ayam(Animal):
    def fly(self):
        raise NotImplementedError("AYAM GAK BISA TERBANG")


def buat_binatang_terbang(binatang):
    binatang.fly()


merpatiInstance = Merpati()
ayamInstance = Ayam()

buat_binatang_terbang(merpatiInstance)
try:
    buat_binatang_terbang(ayamInstance)
except Exception as e:
    print("E", e)


# INTERFACE SEGREGATION PRINCIPLE (ISP): clients harus tidak di forced untuk bergantung pada methods yang
# dia tidak gunakan
class Document:
    def open(self):
        pass

    def save(self):
        pass


class Editor:
    def __init__(self, document):
        self.document = document

    def edit(self):
        self.document.open()
        # edit document implement
        self.document.save()


class SimpleDocument:
    def open(self):
        pass

    def save(self):
        pass


class SimpleEditor:
    def __init__(self, document):
        self.document = document

    def edit(self):
        self.document.open()
        # edit document implementation
        self.document.save()


# DEPENDENCY INVERSION PRINCIPLE (DIP):
# high level modules should not depend on low-level modules. both should depend on abstractions.
# abstractions should not depend on details.
# details should depend on abstractions
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        pass


class PaypalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        pass


class PaymentGateway:
    def __init__(self, payment_processor: Type[PaymentProcessor]):
        self.payment_processor = payment_processor

    def purchase(self, amount):
        self.payment_processor.process_payment(amount)
