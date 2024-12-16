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

# def calculator():
#     print("Enter your numbers")
#
#     num1 = float(input("First number: "))
#     num2 = float(input("Second number: "))
#
#     print("addition: ", round(add(num1, num2), 2))
#     print("Subtraction: ", round(subtract(num1, num2), 2))
#     print("Multiplication: ", round(multiply(num1, num2), 2))
#     print("Division: ", round(divide(num1, num2), 2))

# calculator()



def calculator2():
    # List to store number inputs
    numbers = []

    while True:
        user_input = input("Enter an number or 'add': ").strip()    # Removes leading or trailing whitespace characters

        if user_input.lower() == "add":   # This ensures both upper and lower cases or mix of two is accepted
            if numbers:
                print(f" The sum of the numbers is: {sum(numbers)}")
                numbers.clear()
            else:
                print("No numbers to add")
        else:
            try:
                number = float(user_input)
                numbers.append(number)
                print(f"Number {number} added to the list.")
                print(numbers)
            except ValueError:
                print("Invalid input. Please enter a number or 'add'.")

calculator2()


