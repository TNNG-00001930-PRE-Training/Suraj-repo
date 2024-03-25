def calculator_function():
    while True:
        print("Choose operation:")
        print("Addition")
        print("Subtraction")
        print("Multiplication")
        print("Division")
        print("Exit")

        choice = input("Enter choice: ")

        if choice in ('Addition', 'Subtraction', 'Multiplication', 'Division'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 'Addition':
                print("Result:", num1 + num2)
            elif choice == 'Subtraction':
                print("Result:", num1 - num2)
            elif choice == 'Multiplication':
                print("Result:", num1 * num2)
            elif choice == 'Division':
                if num2 == 0:
                    print("Error! Division by zero.")
                else:
                    print("Result:", num1 / num2)
        elif choice == 'Exit':
            print("Exited")
            break
        else:
            print("Invalid input")
        
calculator_function()