# Drawing pattern with nested loops

while True:
    user_input = input('Enter the size of the pattern: ')
    try:
        pattern_length = int(user_input)
        if pattern_length > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid entry. Please enter a positive integer.")

row = 0  # Initialize row counter
while row < pattern_length:
    for col in range(pattern_length):  # Inner loop for columns
        print("*", end="")  # Print an asterisk without newline
    print()  # Move to the next line after finishing one row
    row += 1  # Increment row counter

