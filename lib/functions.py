#!/usr/bin/env python3

def greet_programmer():
    """Greets the programmer with a fixed message."""
    print("Hello, programmer!")    

def greet(name):
    """Greets the provided name."""
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    """Greets the provided name, or uses 'programmer' if no name is provided."""
    print(f"Hello, {name}!")

def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

def halve(number):
    """Returns half the value of the number, or None if input isn't a number."""
    if not isinstance(number, (int, float)):
        return None
    return number / 2
