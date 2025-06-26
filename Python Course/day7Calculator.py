def calculator():
    print("Welcome to the Python Calculator!")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == '5':
        print(f"{num1} % {num2} = {num1 % num2}")
    elif choice == '6':
        print(f"{num1} ** {num2} = {num1 ** num2}")
    else:
        print("Invalid choice. Please select a number from 1 to 6.")

# Run the calculator
calculator()
