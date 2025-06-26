user_input = input("Enter the value between 5 and 9 (or type 'quit' to exit): ")

if user_input.lower() == "quit":
    print("Goodbye!")
else:
    try:
        a = int(user_input)
        if a < 5 or a > 9:
            # raise is used to raise an ValueError 
            raise ValueError("Value should be between 5 and 9.")
        else:
            print("You have entered a valid value:", a)
    except ValueError as ve:
        print("Invalid input:", ve)
