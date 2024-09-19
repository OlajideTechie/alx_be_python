
number = int(input('Enter a number to see its multiplication table:')) #Take user input.

for numbers in range(1, 11): #loop to iterate the number times to display 
        
        product = number * numbers
        
        print(f"{number} x {numbers} = {product}", end="\t")

        print() 