# Prompt user to enter two numbers and select an operation (addition, subtraction, multiplication, or division).
num1 = int(input('Enter your first number:')).strip()
num2 = int(input('Enter your second number:')).strip()

operation_type = input('Choose the operation (+, -, *, /):').strip()

# Match case conditions to handle the logic
match operation_type:
    case '+':
        number_sum = num1 + num2
        print(f'The result is {number_sum}.')
    case '-':
        number_subtraction = num1 - num2
        print(f'The result is {number_subtraction}.')
    case '*':
        number_multiplication = num1 * num2
        print(f'The result is {number_multiplication}.')
    case '/':
        if num2 != 0:
            number_division = num1 / num2
            print(f'The result is {number_division}.')
        else:
            print('Error: Division by zero is not allowed.')
    case _:
        print('Invalid operation selected.')