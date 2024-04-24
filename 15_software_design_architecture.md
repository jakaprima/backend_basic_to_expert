# CLEAN CODE PRINCIPLE
``` python
# Clarity: The code should be easy to read and understand.
def calculate_circle_area(radius):
    """
    Calculates the area of a circle given its radius.
    """
    return 3.14 * radius ** 2

# Simplicity: The code should be as simple as possible, avoiding unnecessary complexity.
def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Comments: Comments should be used sparingly and only when necessary to explain complex or non-obvious code.
def factorial(n):
    """
    Computes the factorial of a number.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Naming: Variables, functions, and classes should have meaningful and descriptive names.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year

# Formatting: The code should be consistently formatted to improve readability.
def fibonacci(n):
    """
    Generates the Fibonacci sequence up to n terms.
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

# Functionality: The code should be organized into small, single-purpose functions and classes.
def calculate_area(length, width):
    """
    Calculates the area of a rectangle.
    """
    return length * width

def calculate_perimeter(length, width):
    """
    Calculates the perimeter of a rectangle.
    """
    return 2 * (length + width)

# Error handling: The code should handle errors in a consistent and predictable way.
def divide(a, b):
    """
    Divides two numbers.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = float('inf')  # handle division by zero
    return result

# Testing: The code should be testable and have high test coverage.
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True

# Reusability: The code should be designed to be reusable and modular.
def greet(name):
    """
    Greets the user with a personalized message.
    """
    return f"Hello, {name}!"

# Performance: The code should be designed to be efficient and performant.
def sum_of_squares(n):
    """
    Computes the sum of squares up to n.
    """
    return sum([i ** 2 for i in range(1, n + 1)])
```

