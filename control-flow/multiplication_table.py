number = int(input('Enter a number to see its multiplication table:'))  # Take user input.

for multiplier in range(1, 11):  # Loop to iterate the number from 1 to 10.
    product = number * multiplier  
    print(f"{number} * {multiplier} = {product}")