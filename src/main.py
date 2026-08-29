from datetime import date
from utils import add, subtract, multiply, divide, power

name = "Maysha Khanom Moon"

print("My name is", name)
print("Today's date:", date.today())

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))

try:
    print("Division:", divide(10, 2))
except ValueError as error:
    print("Error:", error)

try: 
    print("Power:", power(2, 3))
except ValueError as error:
    print("Error:", error)