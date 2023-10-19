def get_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    while True:
        operation = input("Which operation do you want to perform? (+, -, /, x): ")
        if operation in ['+', '-', '/', 'x']:
            return operation
        else:
            print("Invalid operation. Please try again.")

def calculator():
    while True:
        try:
            num_count = int(input("How many numbers will you enter? (At least 2): "))
            if num_count >= 2:
                break
            else:
                print("You need to enter at least two numbers. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    numbers = [get_number(f"Enter number {i + 1}: ") for i in range(num_count)]

    operation = get_operation()

    if operation == '+':
        result = sum(numbers)
    elif operation == '-':
        result = numbers[0] - sum(numbers[1:])
    elif operation == '/':
        result = numbers[0]
        for number in numbers[1:]:
            result /= number
    elif operation == 'x':
        result = 1
        for number in numbers:
            result *= number

    print(f"Result: {result}")

# Call the calculator function
calculator()
