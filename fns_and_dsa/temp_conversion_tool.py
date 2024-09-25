# Conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


if __name__ == "__main__":

    # User input for temperature conversion
    user_input = float(input("Enter the temperature to convert: "))
    scale = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').strip().upper()

    if scale == 'C':
        temp_f = celsius_to_fahrenheit(user_input)
        print(f"{user_input}°C is {temp_f:.2f}°F")
    elif scale == 'F':
        temp_c = fahrenheit_to_celsius(user_input)
        print(f"{user_input}°F is {temp_c:.2f}°C")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
