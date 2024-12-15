### Functions

# Add two numbers
def add(x, y):
    return x + y

# Subtract two numbers (y from x)
def subtract(x, y):
    return x - y

# Multiply two numbers
def multiply(x, y):
    return x * y

# Divide two numbers
def divide(x, y):
    return x / y

def calculator():
    print("Enter your numbers")

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    print("addition: ", round(add(num1, num2), 2))
    print("Subtraction: ", round(subtract(num1, num2), 2))
    print("Multiplication: ", round(multiply(num1, num2), 2))
    print("Division: ", round(divide(num1, num2), 2))

calculator()

