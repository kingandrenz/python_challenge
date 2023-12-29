print("Simple Calculator\n")

try:
    operation = int(input("Enter operation (1 for addition, 2 for subtraction, 3 for division, 4 for multiplication): "))
    a, b = map(float, input("Enter two numbers separated by a comma: ").split(','))

    if operation == 1:
        result = a + b
    elif operation == 2:
        result = a - b
    elif operation == 3:
        result = a / b
    elif operation == 4:
        result = a * b
    else:
        print("Invalid operation code. Please enter a valid code (1-4).")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
else:
    print("Result:", result)

