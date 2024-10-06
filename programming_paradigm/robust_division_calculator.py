# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division with error handling for division by zero and non-numeric inputs."""
    try:
        num = float(numerator)  # Convert numerator to float
        denom = float(denominator)  # Convert denominator to float
        
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        result = num / denom
        return f"The result of the division is {result:.2f}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
