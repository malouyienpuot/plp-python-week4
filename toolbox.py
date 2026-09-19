"""Small reusable functions for the Week 4 assignment."""


def double(number):
    """Return number multiplied by two."""
    return number * 2


def is_pass(score):
    """Return whether score is at least 50."""
    return score >= 50


def greet(name, greeting="Hello"):
    """Return a greeting for name."""
    return greeting + ", " + name + "!"


print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Amina"))
print(greet("Brian", "Habari"))
