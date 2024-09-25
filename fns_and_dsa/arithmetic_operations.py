def perform_operation():
    print('Arithmetic Operations')

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

            # Logic to handle each operation
            if operation == 'add':
                result = num1 + num2
                print(f"The result of adding {num1} and {num2} is: {result}")

            elif operation == 'subtract':
                result = num1 - num2
                print(f"The result of subtracting {num2} from {num1} is: {result}")

            elif operation == 'multiply':
                result = num1 * num2
                print(f"The result of multiplying {num1} and {num2} is: {result}")

            elif operation == 'divide':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of dividing {num1} by {num2} is: {result}")

            else:
                print("Invalid operation. Please enter one of the following: add, subtract, multiply, divide.")

        except ValueError:
            print("Invalid input. Please enter a numeric value!.")

        # Ask if the user wants to perform another operation
        again = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if again != 'yes':
            break  # Exit the loop if the user does not want to continue


if __name__ == "__main__":
    perform_operation()
