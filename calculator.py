# check for number
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# number input
num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

# operation choose
operation = input("Choose the operation (+, -, *, /): ")

# calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    while num2 == 0:
        num2 = float(input("Division by 0 is not allowed. Enter a new number: "))
    result = num1 / num2
else:
    print("Invalid input")

print(f"The result is {result}")