def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    if a == 0 and b == 0:
        raise ValueError("0 raised to the power of 0 is undefined")
    return a ** b