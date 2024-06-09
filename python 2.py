def calculator():
    # Prompt user for input numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Prompt user to choose an operation
    print("Choose the operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input("Enter the operation (1/2/3/4): ")
    
    # Perform the calculation based on the user's choice
    if operation == '1':
        result = num1 + num2
        operation_sign = '+'
    elif operation == '2':
        result = num1 - num2
        operation_sign = '-'
    elif operation == '3':
        result = num1 * num2
        operation_sign = '*'
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            operation_sign = '/'
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation choice.")
        return
    
    # Display the result
    print(f"{num1} {operation_sign} {num2} = {result}")

# Run the calculator
calculator()
